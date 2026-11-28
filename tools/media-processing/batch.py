"""Private, resumable local transcription. Public CI uses fixed synthetic fixtures only."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import sys
import tempfile

from transcribe import MODELS, SUFFIXES, outside, recognize

PIPELINE = "pcm16-whisper-pt-v1"

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def timestamp(seconds):
    ms = round(seconds * 1000)
    hours, ms = divmod(ms, 3600000)
    minutes, ms = divmod(ms, 60000)
    sec, ms = divmod(ms, 1000)
    return f"{hours:02}:{minutes:02}:{sec:02},{ms:03}"

def export(data):
    segments = data["segments"]
    for s in segments:
        if not (math.isfinite(s["start"]) and math.isfinite(s["end"]) and 0 <= s["start"] <= s["end"]):
            raise ValueError("Invalid timestamps")
        if not isinstance(s["text"], str):
            raise ValueError("Invalid segment")
    return {
        "transcript.json": json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        "transcript.txt": "\n".join(s["text"].strip() for s in segments) + "\n",
        "transcript.srt": "".join(f"{i}\n{timestamp(s['start'])} --> {timestamp(s['end'])}\n{' '.join(s['text'].split())}\n\n" for i,s in enumerate(segments, 1)),
    }

def private_write(path, text):
    fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        stream.write(text)

def complete(target, digest, model):
    if target.is_symlink() or not target.is_dir():
        return False
    try:
        names = ("manifest.json", "transcript.json", "transcript.txt", "transcript.srt")
        if any((target / n).is_symlink() or not (target / n).is_file() for n in names):
            return False
        meta = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
        return (meta["source_sha256"] == digest and meta["model"] == model and
                meta["pipeline"] == PIPELINE and
                all(sha256(target / n) == meta["outputs"][n] for n in names[1:]))
    except (OSError, ValueError, KeyError, TypeError):
        return False

def process(input_dir, output_dir, model="small", model_dir=None, recognizer=recognize):
    source = outside(input_dir)
    dest = outside(output_dir)
    if not source.is_dir() or model not in MODELS:
        raise ValueError("Invalid input or model")
    if source == dest or source in dest.parents or dest in source.parents:
        raise ValueError("Input and output directories must be separate")
    if model_dir is not None:
        outside(model_dir)
    dest.mkdir(mode=0o700, parents=True, exist_ok=True)
    if dest.stat().st_mode & 0o077:
        raise ValueError("Output directory must be private (chmod 700)")
    stats = {"processed": 0, "skipped": 0, "failed": 0}
    engine = None
    # Do not follow symbolic links. Only files beneath the input directory are accepted.
    for root, dirs, names in os.walk(source, followlinks=False):
        dirs[:] = sorted(d for d in dirs if not (Path(root)/d).is_symlink())
        for name in sorted(names):
            path = Path(root)/name
            if path.suffix.lower() not in SUFFIXES:
                continue
            try:
                if path.is_symlink() or not path.is_file():
                    raise ValueError("Unsupported source")
                path = outside(path)
                if source not in path.parents:
                    raise ValueError("Source escaped input directory")
                digest = sha256(path)
                key = hashlib.sha256((digest + ":" + model + ":" + PIPELINE).encode()).hexdigest()
                target = dest/key
                if complete(target, digest, model):
                    stats["skipped"] += 1
                    continue
                if target.exists() or target.is_symlink():
                    raise ValueError("Existing incomplete result; inspect privately")
                # Snapshot and recheck content before transcription, so the manifest identifies the exact input.
                with tempfile.TemporaryDirectory(prefix="pythoteca-batch-") as tmp:
                    snapshot = outside(Path(tmp)/("input"+path.suffix.lower()))
                    shutil.copyfile(path, snapshot)
                    if sha256(snapshot) != digest:
                        raise ValueError("Input changed")
                    data, engine = recognizer(snapshot, model, model_dir, engine=engine)
                    if data.get("model") != model or data.get("language") != "pt":
                        raise ValueError("Unexpected recognition metadata")
                    outputs = export(data)
                    # Stage all exports in a private directory on the same filesystem.
                    stage = Path(tempfile.mkdtemp(prefix=".stage-", dir=dest))
                    try:
                        for filename, text in outputs.items():
                            private_write(stage/filename, text)
                        meta = {"source_sha256": digest, "model": model, "pipeline": PIPELINE,
                                "outputs": {n: sha256(stage/n) for n in outputs}}
                        private_write(stage/"manifest.json", json.dumps(meta, indent=2)+"\n")
                        if target.exists() or target.is_symlink():
                            raise ValueError("Concurrent result")
                        stage.rename(target)
                    finally:
                        if stage.exists():
                            shutil.rmtree(stage)
                stats["processed"] += 1
            except Exception:
                stats["failed"] += 1
    return stats

def main():
    parser = argparse.ArgumentParser(description="Private local batch transcription")
    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    parser.add_argument("--model", choices=sorted(MODELS), default="small")
    parser.add_argument("--model-dir")
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS", "").lower() == "true":
        print("Private batch transcription is disabled in GitHub Actions.", file=sys.stderr)
        return 1
    try:
        result = process(args.input_dir, args.output_dir, args.model, args.model_dir)
    except Exception:
        print("Batch setup failed. Inspect private directories locally.", file=sys.stderr)
        return 1
    print(json.dumps(result))
    return int(result["failed"] > 0)

if __name__ == "__main__":
    raise SystemExit(main())
