"""Guard functions for stage inclusion, evidence policy, and catalog invariants."""
from __future__ import annotations
import sys
from typing import Any, Mapping

class CatalogError(Exception):
    pass

def get_stage_profile(control: Mapping[str, Any], stage: str) -> Mapping[str, Any] | None:
    return control.get("stage_profile", {}).get(stage)

def get_evidence_policy(control: Mapping[str, Any], stage: str) -> Mapping[str, Any] | None:
    profile = get_stage_profile(control, stage)
    if not profile or profile.get("included") is not True:
        return None
    return control.get("stage_evidence_policy", {}).get(stage)

def validate_stage_counts(controls: list) -> dict[str, int]:
    counts: dict[str, int] = {"early": 0, "growth": 0, "enterprise": 0}
    for c in controls:
        for stage in counts:
            if c.get("stage_profile", {}).get(stage, {}).get("included") is True:
                counts[stage] += 1
    return counts

def validate_catalog(catalog: Mapping[str, Any]) -> None:
    controls = catalog.get("controls", [])
    if len(controls) != catalog.get("control_count"):
        raise CatalogError("control_count does not match controls length")
    ids: set[str] = set()
    for c in controls:
        cid = c.get("control_id")
        if not cid or cid in ids:
            raise CatalogError(f"missing or duplicate control_id: {cid}")
        ids.add(cid)
        for field in ["severity_if_failed", "decision_flags", "stage_profile", "stage_evidence_policy", "applies_if"]:
            if field not in c:
                raise CatalogError(f"{cid} missing {field}")
        for stage, profile in c["stage_profile"].items():
            included = profile.get("included")
            priority = profile.get("priority")
            if included is True and priority == "out_of_scope":
                raise CatalogError(f"{cid}:{stage} included with out_of_scope priority (INVAR-01)")
            if included is False and priority not in ("out_of_scope", "deferred"):
                raise CatalogError(f"{cid}:{stage} excluded with invalid priority '{priority}' — must be out_of_scope or deferred (INVAR-02)")
    counts = validate_stage_counts(list(controls))
    if counts["enterprise"] != 131:
        raise CatalogError(f"enterprise included count {counts['enterprise']} != 131 (INVAR-03)")
    if counts["early"] > 30:
        raise CatalogError(f"early included count {counts['early']} > 30 (INVAR-04)")
    if not (60 <= counts["growth"] <= 90):
        print(f"WARNING INVAR-05: growth included count {counts['growth']} outside 60-90 — explicit acceptance required", file=sys.stderr)
