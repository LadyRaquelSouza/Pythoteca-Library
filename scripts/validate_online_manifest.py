#!/usr/bin/env python3
"""Validate the v2 online manifest against exact module bytes, independently of the v1 catalog."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "modules"
IDENTIFIER = re.compile(r"aula(?:0[1-9]|[1-9][0-9]{1,3})\Z")
DISCIPLINES = {"python", "portugol", "java", "arquitetura", "sistemas_operacionais", "ti", "modelagem_dados"}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def main():
    raw = (ROOT / "index.json").read_bytes()
    require(0 < len(raw) <= 256 * 1024, "Index is missing or too large")
    manifest = json.loads(raw.decode("utf-8"))
    require(set(manifest) == {"schema_version", "lessons"} and type(manifest["schema_version"]) is int and manifest["schema_version"] == 2, "Invalid version or root keys")
    entries = manifest["lessons"]
    require(isinstance(entries, list) and 0 < len(entries) <= 250, "Invalid entries")
    ids = set()
    for entry in entries:
        require(isinstance(entry, dict) and set(entry) == {"id", "title", "subtitle", "discipline", "sha256", "bytes"}, "Invalid entry fields")
        identifier = entry["id"]
        require(isinstance(identifier, str) and IDENTIFIER.fullmatch(identifier) and identifier not in ids, "Invalid or repeated id")
        ids.add(identifier)
        require(entry["discipline"] in DISCIPLINES, "Invalid discipline")
        require(isinstance(entry["sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]), "Invalid hash")
        require(type(entry["bytes"]) is int and 0 < entry["bytes"] <= 1024 * 1024, "Invalid byte size")
        for key, limit in (("title", 180), ("subtitle", 160)):
            require(isinstance(entry[key], str) and 0 < len(entry[key].strip()) <= limit, "Invalid metadata")
        data = (ROOT / (identifier + ".json")).read_bytes()
        require(len(data) == entry["bytes"], "Byte size mismatch: " + identifier)
        require(hashlib.sha256(data).hexdigest() == entry["sha256"], "SHA-256 mismatch: " + identifier)
        module = json.loads(data.decode("utf-8"))
        require(type(module.get("schema_version")) is int and module["schema_version"] == 2, "Module version mismatch")
        for key in ("id", "title", "subtitle", "discipline"):
            require(module.get(key) == entry[key], "Metadata mismatch: " + identifier + "/" + key)
    require(ids == {f.stem for f in ROOT.glob("aula*.json")}, "Manifest and module files differ")
    print(f"Online v2 manifest validated: {len(ids)} modules")

if __name__ == "__main__":
    main()
