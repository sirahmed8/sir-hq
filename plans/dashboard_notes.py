"""Text feeds for the SIR Control Room: owner one-tap items, suggestions, tool limits, key names, checkpoint head,
background helpers. Read-only. Key values are never read: only service names and status words."""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
ROOT = os.path.normpath(os.path.join(HERE, ".."))


def _lines(path):
    try:
        with io.open(path, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except OSError:
        return []


def _table_rows(lines):
    rows = []
    for ln in lines:
        s = ln.strip()
        if not s.startswith("|") or set(s) <= set("|-: "):
            continue
        rows.append([c.strip() for c in s.strip("|").split("|")])
    return rows[1:] if rows else []  # first row is the header


def owner_actions():
    items = []
    for ln in _lines(os.path.join(OPS, "OWNER_ACTIONS.md")):
        if ln.startswith("## "):
            items.append({"title": ln[3:].strip()[:160]})
    return items


def suggestions():
    counts = {"pending": 0, "approved": 0, "rejected": 0}
    pending = []
    current = None
    for ln in _lines(os.path.join(OPS, "SUGGESTIONS.md")):
        if ln.startswith("## "):
            current = {"head": ln[3:].strip(), "finding": "", "status": "pending"}
            parts = [p.strip() for p in current["head"].split("|")]
            current["project"] = parts[1] if len(parts) > 1 else ""
            current["severity"] = parts[2] if len(parts) > 2 else ""
            pending.append(current)
        elif current is not None:
            m = re.match(r"\*\*Status:\*\*\s*(\w+)", ln)
            if m:
                current["status"] = m.group(1).lower()
            m = re.match(r"\*\*Finding:\*\*\s*(.+)", ln)
            if m and not current["finding"]:
                current["finding"] = m.group(1)[:220]
    open_items = []
    for it in pending:
        st = it["status"] if it["status"] in counts else "pending"
        counts[st] += 1
        if st == "pending":
            open_items.append({"project": it["project"], "severity": it["severity"], "finding": it["finding"]})
    return {"counts": counts, "pending": open_items[-20:]}


def usage_limits():
    rows = _table_rows(_lines(os.path.join(OPS, "USAGE_LIMITS.md")))
    out = []
    for r in rows:
        if len(r) >= 5:
            out.append({"tool": r[0][:120], "expected_return": r[4][:160]})
    return out


def key_names():
    rows = _table_rows(_lines(os.path.join(OPS, "research", "keys-status-2026-11-12.md")))
    return [{"service": r[0][:60], "status": r[1][:40]} for r in rows if len(r) >= 2]


def checkpoint_head():
    lines = [ln for ln in _lines(os.path.join(OPS, "HQ_CHECKPOINT.md")) if ln.strip()][:12]
    return "\n".join(lines)[:900]


def helpers():
    names = []
    for ln in _lines(os.path.join(OPS, "RUNNING_STATE.md")):
        if ln.startswith("sir-ai-builder") or ln.startswith("sir-portfolio-builder"):
            names.append({"name": ln.split(" ", 1)[0], "note": ln[:220]})
    return names


def collect():
    return {
        "owner_actions": owner_actions(),
        "suggestions": suggestions(),
        "usage_limits": usage_limits(),
        "key_names": key_names(),
        "checkpoint_head": checkpoint_head(),
        "helpers": helpers(),
    }
