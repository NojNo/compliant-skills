"""Minimal deterministic GDPR control engine skeleton."""
from __future__ import annotations
from typing import Any, Mapping
from condition_eval import eval_condition
from control_engine_guard import get_evidence_policy

def evaluate_control(control: Mapping[str, Any], facts: Mapping[str, Any], stage: str) -> dict[str, Any]:
    policy = get_evidence_policy(control, stage)
    if policy is None:
        return {"control_id": control["control_id"], "result": "not_applicable", "reason": "inactive_for_stage"}
    if not eval_condition(control.get("applies_if"), facts):
        return {"control_id": control["control_id"], "result": "not_applicable", "reason": "applies_if_false"}
    if control.get("enforceability") == "non_enforceable" and control.get("needs_legal_review"):
        return {"control_id": control["control_id"], "result": "needs_legal_review", "reason": "non_enforceable"}
    required = control.get("evidence_required", [])
    missing = [e for e in required if not facts.get(e)]
    if missing:
        return {"control_id": control["control_id"], "result": "unknown", "missing_evidence": missing}
    confirmed = facts.get("required_evidence_confirms_control")
    if confirmed is True:
        return {"control_id": control["control_id"], "result": "pass"}
    if confirmed is False:
        return {"control_id": control["control_id"], "result": "fail"}
    return {"control_id": control["control_id"], "result": "unknown", "reason": "no_result_signal"}

def evaluate_catalog(catalog: Mapping[str, Any], facts: Mapping[str, Any], stage: str) -> list[dict[str, Any]]:
    return [evaluate_control(c, facts, stage) for c in catalog.get("controls", [])]
