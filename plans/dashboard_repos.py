"""Repo freshness and CI state for the SIR Control Room. Git log and gh only; never reads project files.
AHome: only the last commit date and the CI conclusion are returned, never its subjects or paths."""
import json
import os
import subprocess
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("SIR_ROOT", os.path.normpath(os.path.join(HERE, "..", "..")))
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
CREATE_NO_WINDOW = 0x08000000
PRIVATE = {"AHome"}

PROJECTS = [
    ("SIR AI", "SIR AI"),
    ("SIR Portfolio", "SIR Portfolio"),
    ("SIR Jobs", "SIR Jobs"),
    ("SIR Study", "SIR Study"),
    ("SIR Laptop Manager", "SIR Laptop Manager"),
    ("_SIR", "_SIR"),
    ("AHome", "AHome"),
]


def _run(args, cwd, timeout=20):
    env = {**os.environ, "MSYS_NO_PATHCONV": "1"}
    try:
        r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout,
                           creationflags=CREATE_NO_WINDOW, env=env)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def last_commit(folder):
    """Unix time of the last commit on the checked-out branch, or 0."""
    out = _run(["git", "log", "-1", "--format=%ct"], cwd=folder, timeout=10)
    try:
        return int(out)
    except ValueError:
        return 0


def ci_state(folder, private):
    """Latest GitHub Actions run for the repo: status, conclusion and time. Names are dropped for private repos."""
    slug = _run(["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"], cwd=folder, timeout=25)
    if not slug:
        return {"state": "unknown", "conclusion": "", "at": ""}
    raw = _run(["gh", "run", "list", "--repo", slug, "--limit", "1", "--json",
                "status,conclusion,createdAt,displayTitle"], cwd=folder, timeout=25)
    try:
        run = json.loads(raw)[0]
    except (ValueError, IndexError, TypeError):
        return {"state": "unknown", "conclusion": "", "at": ""}
    return {
        "state": run.get("status", ""),
        "conclusion": run.get("conclusion", "") or "",
        "at": (run.get("createdAt", "") or "")[:16].replace("T", " "),
    }


def quota_banner():
    """ops/ci-quota-exhausted.flag: when present, GitHub Actions minutes are used up (red CI is the quota)."""
    path = os.path.join(OPS, "ci-quota-exhausted.flag")
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except OSError:
        text = ""
    return {"text": text[:400], "since": time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(path)))}


def projects():
    now = time.time()
    rows = []
    for name, folder_name in PROJECTS:
        folder = os.path.join(ROOT, folder_name)
        private = name in PRIVATE
        ts = last_commit(folder) if os.path.isdir(folder) else 0
        age_h = round((now - ts) / 3600, 1) if ts else None
        rows.append({
            "name": name,
            "private": private,
            "last_commit": time.strftime("%Y-%m-%d %H:%M", time.localtime(ts)) if ts else "",
            "age_hours": age_h,
            "ci": ci_state(folder, private) if os.path.isdir(folder) else {"state": "unknown", "conclusion": "", "at": ""},
        })
    return rows
