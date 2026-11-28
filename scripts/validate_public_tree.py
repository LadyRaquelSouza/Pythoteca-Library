"""Fail closed for tracked paths outside the public publication contract.

Path screening is not a content or copyright audit. Never print rejected paths.
"""
import re
import subprocess
import sys

ALLOWED = (
    r"README\.md", r"\.gitignore",
    r"\.github/workflows/(?:catalog|media-smoke)\.yml",
    r"(?:catalog|modules)/(?:index|aula[0-9]{2,4})\.json",
    r"modules/README\.md",
    r"docs/(?:editorial|desenvolvimento)/[A-Za-z0-9_-]+\.md",
    r"scripts/(?:validate_catalog|validate_modules|validate_online_manifest|validate_public_tree)\.py",
    r"tools/media-processing/(?:README\.md|requirements\.txt|transcribe\.py|test_transcribe\.py|test_public_tree\.py|smoke_synthetic\.py|batch\.py|test_batch\.py|drive_io\.py|test_drive_io\.py)",
)

def allowed(path):
    return any(re.fullmatch(pattern, path) for pattern in ALLOWED)

def main():
    raw = subprocess.check_output(["git", "ls-files", "--stage", "-z"])
    rejected = 0
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, path = record.split(b"\t", 1)
        mode = metadata.split()[0]
        if mode not in (b"100644", b"100755") or not allowed(path.decode("utf-8", errors="replace")):
            rejected += 1
    if rejected:
        print(f"Privacy gate: {rejected} prohibited tracked entries. Inspect locally.", file=sys.stderr)
        return 1
    print("Privacy gate: tracked paths approved; editorial review still required.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
