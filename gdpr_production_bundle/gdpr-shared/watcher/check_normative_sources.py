"""Maintainer watcher scaffold. Does not run during audits."""
from __future__ import annotations
import json, datetime, pathlib

def queue_review(control_id: str, reason: str, out="review_queue.jsonl") -> None:
    entry = {"control_id": control_id, "reason": reason, "queued_at": datetime.datetime.utcnow().isoformat()+"Z"}
    pathlib.Path(out).open("a").write(json.dumps(entry)+"\n")
