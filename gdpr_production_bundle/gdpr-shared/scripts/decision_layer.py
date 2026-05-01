"""Decision layer for coverage, severity, summary gating, and A6 routing."""
from __future__ import annotations
from typing import Any, Mapping, Sequence

def coverage(results: Sequence[Mapping[str, Any]]) -> float:
    applicable = [r for r in results if r.get("result") != "not_applicable"]
    if not applicable:
        return 0.0
    assessed = [r for r in applicable if r.get("result") in {"pass", "fail", "unknown", "needs_legal_review"}]
    return len(assessed) / len(applicable)

def high_risk_unknown(result: Mapping[str, Any], control: Mapping[str, Any]) -> bool:
    return (
        result.get("result") == "unknown"
        and control.get("decision_flags", {}).get("counts_as_high_risk_unknown", False)
    )

def critical_failure_count(results: Sequence[Mapping[str, Any]], controls_by_id: Mapping[str, Mapping[str, Any]]) -> int:
    return sum(
        1 for r in results
        if r.get("result") == "fail"
        and controls_by_id.get(r["control_id"], {}).get("severity_if_failed") == "critical"
    )

def can_emit_summary(
    results: Sequence[Mapping[str, Any]],
    controls_by_id: Mapping[str, Mapping[str, Any]],
    coverage_threshold: float,
    anti_overclaiming_guard_passed: bool,
) -> bool:
    if coverage(results) < coverage_threshold:
        return False
    if critical_failure_count(results, controls_by_id) > 0:
        return False
    if any(high_risk_unknown(r, controls_by_id.get(r["control_id"], {})) for r in results):
        return False
    return anti_overclaiming_guard_passed

def aggregate_risk(results: Sequence[Mapping[str, Any]], controls_by_id: Mapping[str, Mapping[str, Any]]) -> str:
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for r in results:
        if r.get("result") == "fail":
            sev = controls_by_id.get(r["control_id"], {}).get("severity_if_failed", "low")
            counts[sev] = counts.get(sev, 0) + 1
    if counts["critical"] >= 1 or counts["high"] >= 3:
        return "high_risk"
    if counts["medium"] >= 5:
        return "moderate_risk"
    return "low_risk"

def route_to_a6(control: Mapping[str, Any]) -> bool:
    flags = control.get("decision_flags", {})
    routing = control.get("output_routing", {})
    return (
        control.get("needs_legal_review", False)
        and flags.get("routes_to_legal_review_if_triggered", False)
        and control.get("enforceability") != "technical"
        and routing.get("legal_review_packet") != "off"
    )
