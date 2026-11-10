"""Dashboard data privacy helpers."""
from __future__ import annotations

PRIVATE_STRINGS = [
    "habiba",
    "ahmed-and-habiba",
    "camouflage",
    "consent switch",
    "notification channels",
]


def assert_no_private_leaks(text: str) -> None:
    low = text.lower()
    for s in PRIVATE_STRINGS:
        if s in low:
            raise ValueError(f"CRITICAL PRIVACY VIOLATION: Forbidden private string '{s}' detected in generated dashboard")
