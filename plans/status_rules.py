"""Status rules for SIR Control Room projects.
A project is verified only if <project>/.sir/evidence/verified.json exists,
is dated today, and contains command, exit_code 0, reviewer.
"""
from __future__ import annotations

import json
import os
from datetime import date


def state_for(project_folder: str, today: str | date) -> str:
    """Return one of: verified, built_unverified, not_started."""
    if isinstance(today, date):
        today = today.isoformat()
    evidence_path = os.path.join(project_folder, ".sir", "evidence", "verified.json")
    if not os.path.isfile(evidence_path):
        # check checkpoint for signs of work
        cp = os.path.join(project_folder, ".sir", "CHECKPOINT.md")
        if os.path.isfile(cp):
            try:
                with open(cp, "r", encoding="utf-8") as f:
                    text = f.read(2000)
                if "not started" in text.lower() or "clean skeleton" in text.lower():
                    return "not_started"
                # if checkpoint has real content beyond template, consider built
                if len(text.strip()) > 50:
                    return "built_unverified"
            except Exception:
                pass
        return "not_started"
    try:
        with open(evidence_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return "built_unverified"
    if not isinstance(data, dict):
        return "built_unverified"
    if str(data.get("date", "")) != str(today):
        return "built_unverified"
    if "command" not in data or "reviewer" not in data:
        return "built_unverified"
    try:
        exit_code = int(data.get("exit_code", -1))
    except Exception:
        return "built_unverified"
    if exit_code != 0:
        return "built_unverified"
    return "verified"
