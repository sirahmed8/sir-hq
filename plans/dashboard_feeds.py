"""Read-only feeds for the SIR Control Room: live runners, free tool pool, rounds.
Every function returns plain dicts/lists and never raises: a missing file gives an empty value and a note.
Worker count = autopilot_state.json runners whose pid is a real running process (tasklist), not queue entries."""
import csv
import io
import json
import os
import re
import subprocess
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("SIR_ROOT", os.path.normpath(os.path.join(HERE, "..", "..")))
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
CREATE_NO_WINDOW = 0x08000000


def _read(path):
    try:
        with io.open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def _json(path, default):
    try:
        with io.open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def live_pids(pids):
    """Return the subset of pids that are running right now (Windows tasklist, one call)."""
    alive = set()
    for pid in pids:
        try:
            r = subprocess.run(
                ["tasklist", "/FI", f"PID eq {int(pid)}", "/FO", "CSV", "/NH"],
                capture_output=True, text=True, timeout=8, creationflags=CREATE_NO_WINDOW,
                env={**os.environ, "MSYS_NO_PATHCONV": "1"},
            )
        except (OSError, subprocess.SubprocessError, ValueError):
            continue
        for row in csv.reader(io.StringIO(r.stdout)):
            if len(row) >= 2 and row[1].strip() == str(int(pid)):
                alive.add(int(pid))
                row_image = row[0].strip().lower()
                _IMAGES[int(pid)] = row_image
    return alive


_IMAGES = {}

_TOOL_WORDS = {
    "bash.exe": "shell runner",
    "python.exe": "script runner",
    "pythonw.exe": "script runner",
    "node.exe": "script runner",
}


def runners():
    """Live runners right now. Each entry: task name, title from the queue, start time, process kind."""
    state = _json(os.path.join(OPS, "autopilot_state.json"), {})
    queue = _json(os.path.join(OPS, "AUTOPILOT_QUEUE.json"), [])
    titles = {e.get("name"): e.get("title", "") for e in queue if isinstance(e, dict)}
    done_names = {e.get("name") for e in queue if isinstance(e, dict) and e.get("done")}
    entries = []
    for name, info in (state.get("runners") or {}).items():
        pid = info.get("pid") if isinstance(info, dict) else None
        if pid and name not in done_names:  # a finished task whose old pid was reused by another process is not a live worker
            entries.append((name, int(pid), info.get("started")))
    alive = live_pids([p for _, p, _ in entries])
    out = []
    for name, pid, started in entries:
        if pid not in alive:
            continue
        out.append({
            "task": name,
            "title": titles.get(name, ""),
            "since": time.strftime("%Y-%m-%d %H:%M", time.localtime(started)) if started else "",
            "kind": _TOOL_WORDS.get(_IMAGES.get(pid, ""), "worker"),
            "pid": pid,
        })
    out.sort(key=lambda r: r["since"])
    return out


def queue_open():
    """Queue entries not yet done (waiting or not started)."""
    queue = _json(os.path.join(OPS, "AUTOPILOT_QUEUE.json"), [])
    return [{"task": e.get("name", ""), "title": e.get("title", ""), "folder": os.path.basename(str(e.get("folder", "")))}
            for e in queue if isinstance(e, dict) and not e.get("done")]


def pool():
    """Free tool pool state from ops/agy-runs/model-pool.json (written by scripts/cli_pool.py)."""
    raw = _json(os.path.join(OPS, "agy-runs", "model-pool.json"), {})
    now = time.time()
    rows = []
    for key, info in raw.items():
        tool, _, model = key.partition("|")
        until = float(info.get("until") or 0)
        cooling = until > now
        rows.append({
            "tool": tool,
            "model": model,
            "state": "cooling" if cooling else "ready",
            "until": time.strftime("%Y-%m-%d %H:%M", time.localtime(until)) if cooling else "",
            "why": info.get("why", ""),
            "last_ok": time.strftime("%Y-%m-%d %H:%M", time.localtime(float(info.get("last_ok") or 0))) if info.get("last_ok") else "",
        })
    return rows


_ROUND_RE = re.compile(r"^\s*\|\s*(?P<label>[^|]+?)\s*\|\s*(?P<task>[^|]+?)\s*\|\s*(?P<state>[^|]+?)\s*\|\s*(?P<ver>[^|]*?)\s*\|\s*(?P<title>[^|]*?)\s*\|")


def rounds():
    """Round labels (R1, A1, F1 per project) from ops/round_labels.json, with verification read from verifications/."""
    items = _json(os.path.join(OPS, "round_labels.json"), [])
    verdicts = verification_verdicts()
    out = []
    for it in items:
        if not isinstance(it, dict):
            continue
        task = it.get("task", "")
        v = verdicts.get(task, "")
        if v == "PASS":
            status = "verified"
        elif v == "FAIL":
            status = "failed"
        else:
            status = "not verified"
        out.append({
            "label": it.get("label", ""),
            "task": task,
            "title": it.get("title", ""),
            "state": it.get("state", ""),
            "verified": status,
        })
    return out


def verification_verdicts():
    """Per task id: PASS when every checklist row in its verification file is PASS, FAIL when any row is FAIL."""
    folder = os.path.join(OPS, "verifications")
    verdicts = {}
    if not os.path.isdir(folder):
        return verdicts
    for fn in sorted(os.listdir(folder)):
        if not fn.endswith(".md"):
            continue
        text = _read(os.path.join(folder, fn))
        m = re.search(r"^#\s*Verification:\s*(\S+)", text, re.M)
        task = m.group(1) if m else fn[:-3]
        marks = []
        for line in text.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 3 and cells[2] in ("PASS", "FAIL"):
                marks.append(cells[2])
        if not marks:
            continue
        verdicts[task] = "FAIL" if "FAIL" in marks else ("PASS" if all(x == "PASS" for x in marks) else "")
    return verdicts
