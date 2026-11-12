"""Dashboard generator modules split from dashboard_main.py (R19-M3).
Run: python D:/Projects/_SIR/plans/generate_dashboard.py, then HQ republishes the artifact.
AHome is private: counts and status only, never task text or notes.
Autopilot state, CLI worker, model pool and account ledger parsers."""
import io
import json
import os
import sys
import re
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dashboard_sources import git, lines, tail_lines  # noqa: E402

ROOT = os.environ.get("SIR_ROOT", "D:/Projects")
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
ORDER = json.load(io.open(os.path.join(HERE, "order.json"), encoding="utf-8"))
WAVEMAP = json.load(io.open(os.path.join(HERE, "waves.json"), encoding="utf-8"))
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0


PRIVATE_TASK_RE = re.compile(r"[\w.-]*(?:ahome|habiba)[\w.-]*", re.I)



def sanitize_autopilot_text(value):
    text = str(value)
    text = PRIVATE_TASK_RE.sub("private-task", text)
    return text



def parse_autopilot():
    state = {}
    try:
        state = json.load(io.open(OPS + "/autopilot_state.json", encoding="utf8")) or {}
    except Exception:
        state = {}
    queue = []
    try:
        queue = json.load(io.open(OPS + "/AUTOPILOT_QUEUE.json", encoding="utf8")) or []
    except Exception:
        queue = []
    runners = state.get("runners", {}) if isinstance(state, dict) else {}
    safe_queue = []
    for item in queue if isinstance(queue, list) else []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name") or "")
        title = str(item.get("title") or name)
        private = bool(
            PRIVATE_TASK_RE.search(name)
            or PRIVATE_TASK_RE.search(title)
            or PRIVATE_TASK_RE.search(str(item.get("folder") or ""))
        )
        safe_queue.append(
            {
                "name": "private-task" if private else name,
                "title": "Private project task" if private else title,
                "done": bool(item.get("done")),
                "private": private,
            }
        )
    pending = [q for q in safe_queue if not q["done"]]
    return {
        "listener_pid": state.get("listener_pid") if isinstance(state, dict) else None,
        "last_tick": state.get("last_tick") if isinstance(state, dict) else None,
        "runner_count": len(runners) if isinstance(runners, dict) else 0,
        "queue": safe_queue,
        "pending": pending,
        "pending_count": len(pending),
        "log_tail": [sanitize_autopilot_text(ln) for ln in tail_lines(OPS + "/autopilot.log", 10)],
    }



def load_model_pool():
    path = os.path.join(OPS, "agy-runs", "model-pool.json")
    try:
        return json.load(io.open(path, encoding="utf8")) or {}
    except Exception:
        return {}



def project_folder_for_task(task_name):
    queue = []
    try:
        queue = json.load(io.open(OPS + "/AUTOPILOT_QUEUE.json", encoding="utf8")) or []
    except Exception:
        queue = []
    for item in queue if isinstance(queue, list) else []:
        if not isinstance(item, dict):
            continue
        if str(item.get("name") or "") == task_name:
            return str(item.get("folder") or "")
    if task_name.endswith("-control"):
        return os.path.normpath(os.path.join(HERE, ".."))
    return ""



def model_cooling(pool, model):
    if not isinstance(pool, dict) or not model:
        return None
    for key, info in pool.items():
        if not isinstance(info, dict):
            continue
        if key.split("|")[-1] != model:
            continue
        until = info.get("until", 0)
        try:
            until_f = float(until)
        except Exception:
            until_f = 0
        if until_f > time.time():
            return {"why": info.get("why", ""), "until": until_f, "last_ok": info.get("last_ok")}
    return None



def parse_cli_workers():
    workers = []
    log_dir = os.path.join(OPS, "agy-runs")
    pool = load_model_pool()
    now = time.time()
    try:
        names = [f for f in os.listdir(log_dir) if f.startswith("cli-") and f.endswith(".log")]
    except Exception:
        names = []
    for fname in sorted(names):
        task = fname[len("cli-"):-len(".log")]
        path = os.path.join(log_dir, fname)
        model = ""
        try:
            with io.open(path, encoding="utf8", errors="ignore") as f:
                first = f.readline()
        except Exception:
            continue
        m = re.match(r"===\s*round\s+\d+\s+(\S+)\s+(\S+)", first or "")
        if m:
            model = m.group(2)
        try:
            mins = round((now - os.path.getmtime(path)) / 60)
        except Exception:
            mins = None
        folder = project_folder_for_task(task)
        subject = git(folder, "log", "-1", "--format=%s") if folder else ""
        workers.append({
            "task": task,
            "folder": folder,
            "model": model,
            "minutes": mins,
            "commit": subject,
            "cooling": model_cooling(pool, model),
        })
    workers.sort(key=lambda w: (w["minutes"] is None, w["minutes"] if w["minutes"] is not None else 10 ** 9))
    return workers



def parse_account_ledger():
    rows = []
    for ln in lines(OPS + "/ACCOUNT_LEDGER.md"):
        if not ln.strip().startswith("|"):
            continue
        cells = [p.strip() for p in ln.strip().strip("|").split("|")]
        if not cells:
            continue
        if cells[0].lower() == "time":
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        if len(cells) >= 8:
            rows.append(
                {
                    "time": cells[0],
                    "account": cells[1],
                    "models": cells[2],
                    "five_h": cells[3],
                    "weekly": cells[4],
                    "five_reset": cells[5],
                    "weekly_reset": cells[6],
                    "note": cells[7],
                }
            )
        elif len(cells) == 7:
            rows.append(
                {
                    "time": cells[0],
                    "account": cells[1],
                    "models": "-",
                    "five_h": cells[2],
                    "weekly": cells[3],
                    "five_reset": cells[4],
                    "weekly_reset": cells[5],
                    "note": cells[6],
                }
            )
        elif len(cells) == 6:
            rows.append(
                {
                    "time": cells[0],
                    "account": cells[1],
                    "models": "-",
                    "five_h": cells[2],
                    "weekly": cells[3],
                    "five_reset": cells[4],
                    "weekly_reset": "-",
                    "note": cells[5],
                }
            )
        elif len(cells) >= 3:
            rows.append(
                {
                    "time": cells[0],
                    "account": cells[1],
                    "models": "-",
                    "five_h": "-",
                    "weekly": "-",
                    "five_reset": "-",
                    "weekly_reset": "-",
                    "note": " · ".join(cells[2:]),
                }
            )
    return rows[-10:]
