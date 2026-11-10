"""Single task-count parser for SIR Control Room.
Counts checkboxes in TASKS.md. A checkbox line is: - [x] or - [ ] (case-insensitive x).
Section headings do not affect counting; all checkbox items in the file are counted.
This gives consistent numbers for dashboard and audit.
"""
from __future__ import annotations

import re
from pathlib import Path


CHECKBOX_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s+")


def parse_tasks_file(path: str | Path) -> tuple[int, int]:
    """Return (total, done) checkbox counts for a TASKS.md file."""
    total = 0
    done = 0
    try:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return 0, 0
    for line in text.splitlines():
        m = CHECKBOX_RE.match(line)
        if m:
            total += 1
            if m.group(1).lower() == "x":
                done += 1
    return total, done


def parse_tasks_for_folder(folder: str | Path) -> tuple[int, int]:
    return parse_tasks_file(Path(folder) / ".sir" / "TASKS.md")
