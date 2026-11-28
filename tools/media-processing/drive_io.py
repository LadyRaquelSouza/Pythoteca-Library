"""Local private Drive bridge using an explicitly configured rclone remote.
No credentials, real file identifiers, or academic data in public CI.
"""
import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile

from batch import process
from transcribe import MODELS, SUFFIXES, outside

def remote_path(value):
    # Restrict to a named remote and an explicit non-root directory.
    if not re.fullmatch(r"[A-Za-z0-9_-]+:[^\x00-\x1f]+", value):
        raise ValueError("Expected named remote and non-root directory")
    remote, path = value.split(":", 1)
    parts = path.strip("/").split("/")
    if any(p in ("", ".", "..") for p in parts):
        raise ValueError("Invalid remote directory")
    return remote, "/".join(parts)

def validate_pair(source, dest):
    a, x = remote_path(source)
    b, y = remote_path(dest)
    if a != b:
        raise ValueError("Use a single explicitly configured remote")
    if x == y or x.startswith(y+"/") or y.startswith(x+"/"):
        raise ValueError("Source and destination must be disjoint")
    return a+":"+x, b+":"+y

class Rclone:
    def __init__(self, config):
        self.config = outside(config)
        if not self.config.is_file() or self.config.stat().st_mode & 0o077:
            raise ValueError("Use a private rclone configuration (chmod 600)")

    def call(self, *args):
        # Do not inherit verbose logging or credential-related overrides.
        env = {k:v for k,v in os.environ.items() if not k.upper().startswith("RCLONE_")}
        return subprocess.run(["rclone", "--config", str(self.config), "--log-level", "ERROR", *args],
                              env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout

    def check_drive(self, remote):
        # config redacted does not expose tokens. Only inspect the requested type.
        import configparser
        config = configparser.ConfigParser(interpolation=None)
        config.read_string(self.call("config", "redacted").decode())
        if config.get(remote, "type", fallback="") != "drive":
            raise ValueError("Expected Google Drive remote")

    def list(self, remote):
        return json.loads(self.call("lsjson", "--recursive", "--files-only", remote))

    def download(self, source, local):
        self.call("copyto", source, str(local), "--immutable")

    def upload(self, local, dest):
        self.call("copyto", str(local), dest, "--immutable")

def safe_relative(raw):
    if not isinstance(raw, str) or "\\" in raw or any(ord(c)<32 for c in raw):
        raise ValueError("Invalid path")
    parts = raw.split("/")
    if any(p in ("", ".", "..") for p in parts):
        raise ValueError("Invalid relative path")
    return PurePosixPath(raw)

def sync(source, dest, client, model="small", model_dir=None, dry_run=True, processor=process):
    source, dest = validate_pair(source, dest)
    if model not in MODELS:
        raise ValueError("Invalid model")
    client.check_drive(source.split(":",1)[0])
    items = []
    seen = set()
    for item in client.list(source):
        path = safe_relative(item["Path"])
        if path.suffix.lower() not in SUFFIXES:
            continue
        if path in seen:
            raise ValueError("Ambiguous duplicate Drive path")
        seen.add(path)
        items.append(path)
    report = {"discovered":len(items),"downloaded":0,"processed":0,"skipped":0,"failed":0,"uploaded":0}
    if dry_run:
        return report
    # Local copies of remote outputs are restored first for hash-based resumption.
    # Never accept arbitrary remote output filenames or follow links.
    with tempfile.TemporaryDirectory(prefix="pythoteca-drive-") as temp:
        root = outside(temp)
        incoming = root/"input"
        results = root/"results"
        incoming.mkdir(mode=0o700)
        results.mkdir(mode=0o700)
        remote_names = set()
        for item in client.list(dest):
            p = safe_relative(item["Path"])
            if len(p.parts)!=2 or not re.fullmatch(r"[a-f0-9]{64}",p.parts[0]) or p.name not in {"manifest.json","transcript.json","transcript.txt","transcript.srt"}:
                continue
            if p in remote_names:
                raise ValueError("Ambiguous duplicate remote result")
            remote_names.add(p)
            local = results.joinpath(*p.parts)
            local.parent.mkdir(mode=0o700,exist_ok=True)
            client.download(dest+"/"+str(p),local)
            local.chmod(0o600)
        for p in items:
            local = incoming.joinpath(*p.parts)
            try:
                local.parent.mkdir(mode=0o700,parents=True,exist_ok=True)
                client.download(source+"/"+str(p),local)
                local.chmod(0o600)
                report["downloaded"] += 1
            except Exception:
                local.unlink(missing_ok=True)
                report["failed"] += 1
        stats = processor(incoming, results, model=model, model_dir=model_dir)
        for k in ("processed","skipped","failed"):
            report[k] += stats[k]
        from batch import complete
        for folder in sorted(results.iterdir()):
            try:
                if not re.fullmatch(r"[a-f0-9]{64}",folder.name):
                    continue
                meta = json.loads((folder/"manifest.json").read_text())
                if not complete(folder,meta["source_sha256"],model):
                    continue
                # Manifest last: incomplete upload is not marked complete.
                for name in ("transcript.json","transcript.txt","transcript.srt","manifest.json"):
                    p = PurePosixPath(folder.name)/name
                    if p not in remote_names:
                        client.upload(folder/name,dest+"/"+str(p))
                        report["uploaded"] += 1
            except Exception:
                report["failed"] += 1
    return report

def main():
    parser = argparse.ArgumentParser(description="Private Drive transcription bridge; dry run by default")
    parser.add_argument("--source",required=True)
    parser.add_argument("--destination",required=True)
    parser.add_argument("--config",required=True)
    parser.add_argument("--model",choices=sorted(MODELS),default="small")
    parser.add_argument("--execute",action="store_true")
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS","").lower()=="true":
        print("Private Drive processing disabled in GitHub Actions.",file=sys.stderr)
        return 1
    try:
        report=sync(args.source,args.destination,Rclone(args.config),model=args.model,dry_run=not args.execute)
    except Exception:
        print("Drive setup or transfer failed. Inspect configuration privately.",file=sys.stderr)
        return 1
    print(json.dumps(report))
    return int(report["failed"]>0)

if __name__=="__main__":
    raise SystemExit(main())
