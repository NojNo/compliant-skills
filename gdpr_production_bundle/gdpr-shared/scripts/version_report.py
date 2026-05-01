"""Version helpers for stamp/diff/compare placeholders."""
from __future__ import annotations
import hashlib, json, pathlib

def sha256_file(path: str) -> str:
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

def stamp_catalog(path: str) -> dict:
    data = json.loads(pathlib.Path(path).read_text())
    return {"version": data.get("version"), "schema_version": data.get("schema_version"), "sha256": sha256_file(path)}
