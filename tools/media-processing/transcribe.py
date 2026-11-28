"""Local-only transcription. No public CI execution with private media."""
import argparse
import contextlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import wave

ROOT = Path(__file__).resolve().parents[2]
SUFFIXES = {".mp3", ".mp4", ".m4a", ".wav", ".flac", ".ogg", ".opus", ".webm", ".mov", ".mkv"}
MODELS = {"tiny", "base", "small", "medium", "large-v3", "turbo"}

def outside(path, root=ROOT):
    path = Path(path).expanduser().resolve()
    if path == root or root in path.parents:
        raise ValueError("Private paths must be outside the repository")
    return path

def prepare(input_path, output_path):
    source = outside(input_path)
    target = outside(output_path)
    if not source.is_file() or source.suffix.lower() not in SUFFIXES:
        raise ValueError("Unsupported input")
    if target.suffix.lower() != ".json" or target.exists() or not target.parent.is_dir():
        raise ValueError("Output must be a new JSON file in an existing private directory")
    return source, target

def pcm_samples(path):
    """Read the exact PCM format produced by FFmpeg, bypassing PyAV decoding."""
    import numpy as np
    with wave.open(str(path), "rb") as audio:
        if (audio.getnchannels(), audio.getsampwidth(), audio.getframerate(), audio.getcomptype()) != (1, 2, 16000, "NONE"):
            raise ValueError("Unexpected normalized audio format")
        frames = audio.readframes(audio.getnframes())
    if not frames:
        raise ValueError("Empty audio")
    return np.frombuffer(frames, dtype="<i2").astype(np.float32) / np.float32(32768.0)

def recognize(source, model="small", model_dir=None, engine=None):
    source = outside(source)
    if not source.is_file() or source.suffix.lower() not in SUFFIXES:
        raise ValueError("Unsupported input")
    if model not in MODELS:
        raise ValueError("Unsupported model")
    if not shutil.which("ffmpeg"):
        raise RuntimeError("FFmpeg is required")
    cache = outside(model_dir or Path.home()/".cache"/"pythoteca-whisper")
    cache.mkdir(mode=0o700, parents=True, exist_ok=True)
    # Suppress dependency output; never log filenames or transcript text.
    with open(os.devnull, "w") as sink, contextlib.redirect_stdout(sink), contextlib.redirect_stderr(sink):
        from faster_whisper import WhisperModel
        with tempfile.TemporaryDirectory(prefix="pythoteca-media-") as temp:
            audio = outside(Path(temp)/"audio.wav")
            subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error",
                            "-i", str(source), "-vn", "-ac", "1", "-ar", "16000",
                            "-c:a", "pcm_s16le", str(audio)],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if engine is None:
                engine = WhisperModel(model, device="cpu", compute_type="int8", download_root=str(cache))
            segments, info = engine.transcribe(pcm_samples(audio), language="pt", beam_size=5, vad_filter=True)
            result = {"schema_version": 1, "language": "pt", "model": model,
                      "segments": [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments]}
    return result, engine

def run(input_path, output_path, model="small", model_dir=None):
    source, target = prepare(input_path, output_path)
    result, _ = recognize(source, model, model_dir)
    # Exclusive creation; never overwrite. Restrictive permissions on POSIX.
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as out:
            json.dump(result, out, ensure_ascii=False, indent=2)
            out.write("\n")
    except BaseException:
        target.unlink(missing_ok=True)
        raise

def main():
    parser = argparse.ArgumentParser(description="Private local transcription")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--model", choices=sorted(MODELS), default="small")
    parser.add_argument("--model-dir")
    args = parser.parse_args()
    # Never run against course media on public hosted CI.
    if os.environ.get("GITHUB_ACTIONS", "").lower() == "true":
        print("Private transcription is disabled in GitHub Actions.", file=sys.stderr)
        return 1
    try:
        run(args.input, args.output, args.model, args.model_dir)
    except Exception:
        print("Transcription failed. Check private input, output, FFmpeg and model setup locally.", file=sys.stderr)
        return 1
    print("Transcription completed. Output retained outside the repository.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
