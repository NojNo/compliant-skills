"""Jurisdiction and overlay resolver."""
from __future__ import annotations
from typing import Mapping

def active_overlays(jurisdictions: list[str]) -> list[str]:
    overlays = []
    if "EU_EPRIVACY" in jurisdictions or "EU_GDPR" in jurisdictions:
        overlays.append("eprivacy-eu")
    if "UK_PECR" in jurisdictions:
        overlays.append("pecr-uk")
    if "DE_TDDDG" in jurisdictions:
        overlays.append("tdddg-de")
    return sorted(set(overlays))

def control_active_for_overlay(control: Mapping, overlays: list[str]) -> bool:
    c_overlays = control.get("overlays", [])
    return not c_overlays or bool(set(c_overlays) & set(overlays))
