#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, sys
from control_engine_guard import validate_catalog

if __name__ == "__main__":
    path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "gdpr-shared/controls/control-catalog.json")
    catalog = json.loads(path.read_text())
    validate_catalog(catalog)
    print(f"OK: {len(catalog['controls'])} controls validated")
