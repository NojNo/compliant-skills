"""Executable condition evaluator for control applies_if trees."""
from __future__ import annotations
from typing import Any, Mapping

OPS = {
    "equals": lambda a, b: a == b,
    "not_equals": lambda a, b: a != b,
    "in": lambda a, b: a in b,
    "not_in": lambda a, b: a not in b,
    "exists": lambda a, b=True: (a is not None) is bool(b),
    "truthy": lambda a, b=True: bool(a) is bool(b),
    "gt": lambda a, b: a > b,
    "gte": lambda a, b: a >= b,
    "lt": lambda a, b: a < b,
    "lte": lambda a, b: a <= b,
}

def eval_condition(expr: Any, facts: Mapping[str, Any]) -> bool:
    if expr in (None, [], {}):
        return True
    if isinstance(expr, list):
        return all(eval_condition(e, facts) for e in expr)
    if "all" in expr:
        return all(eval_condition(e, facts) for e in expr["all"])
    if "any" in expr:
        return any(eval_condition(e, facts) for e in expr["any"])
    if "not" in expr:
        return not eval_condition(expr["not"], facts)
    field = expr.get("field")
    op = expr.get("operator", "equals")
    expected = expr.get("value", True)
    if op not in OPS:
        raise ValueError(f"Unsupported condition operator: {op}")
    return OPS[op](facts.get(field), expected)
