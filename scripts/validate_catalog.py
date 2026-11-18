#!/usr/bin/env python3
"""Validate public catalog entries and exact file bytes, without executing lessons."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "catalog"

def require(ok, message):
    if not ok:
        raise ValueError(message)

def main():
    raw = (ROOT / "index.json").read_bytes()
    require(len(raw) <= 256 * 1024, "Index too large")
    index = json.loads(raw.decode("utf-8"))
    require(set(index) == {"schema_version", "lessons"} and type(index["schema_version"]) is int and index["schema_version"] == 1, "Invalid index format")
    items = index["lessons"]
    require(isinstance(items, list) and len(items) <= 250, "Invalid entries")
    ids = set()
    for entry in items:
        require(set(entry) == {"id", "title", "subtitle", "bytes", "sha256"}, "Unexpected fields")
        id_ = entry["id"]
        require(isinstance(id_, str) and re.fullmatch(r"aula(?:0[1-9]|[1-9][0-9]{1,3})", id_) and id_ not in ids, "Invalid or duplicate ID")
        ids.add(id_)
        data = (ROOT / (id_ + ".json")).read_bytes()
        require(type(entry["bytes"]) is int and 0 < len(data) == entry["bytes"] <= 1024 * 1024, "Invalid size: " + id_)
        require(hashlib.sha256(data).hexdigest() == entry["sha256"], "Hash mismatch: " + id_)
        lesson = json.loads(data.decode("utf-8"))
        require(lesson.get("schema_version") == 1, "Invalid lesson version")
        for field, maxlen in [("title", 180), ("subtitle", 160)]:
            value = entry[field]
            require(isinstance(value, str) and 0 < len(value.strip()) and len(value) <= maxlen and lesson.get(field) == value, "Invalid metadata: " + field)
        require(lesson.get("id") == id_, "ID mismatch")
        require(isinstance(lesson.get("chapters"), list) and isinstance(lesson.get("exercises"), list), "Invalid lesson lists")
    require({p.stem for p in ROOT.glob("aula*.json")} == ids, "Unexpected or missing lesson files")
    print(f"Catalog verified: {len(ids)} lesson(s)")

if __name__ == "__main__":
    main()
