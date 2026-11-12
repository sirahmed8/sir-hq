"""HQ autopilot: keeps the work moving while the owner sleeps or Claude is closed. Runs at logon (hidden) as a scheduled task.

Every 5 minutes:
1. game running (Laptop Manager game-mode snapshot file exists) -> stop the CLI runner and pause until the game ends
2. keeps the Telegram listener alive (one instance, pid in ops/telegram-listener.pid)
3. takes the first two unfinished tasks (different project folders) of ops/AUTOPILOT_QUEUE.json
   - done marker exists -> mark it done, tell Ahmed once in simple Arabic, take the next
   - the project folder had a commit or an edit in the last 25 minutes -> somebody (Antigravity or a CLI) is working: do nothing
   - otherwise (stalled) -> start scripts/cli-run2.sh for that task (kilo, opencode, devin rotation), unless a runner is already alive
4. when the free tools all report a usage limit, wait 60 minutes before trying again and tell Ahmed once
5. writes a heartbeat (last_tick) to ops/autopilot_state.json for the dashboard and the Telegram queue button
No product code is written here; the free CLI agents do the work from the brief files.
To add work: python scripts/queue-add.py <name> <brief.md> <folder> "<title>" (builds the prompt file and appends to the queue).
"""
import nowindow  # noqa: F401  (no console windows for child processes)
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
OPS = ROOT / "ops"
QUEUE = OPS / "AUTOPILOT_QUEUE.json"
STATE = OPS / "autopilot_state.json"
LOG = OPS / "autopilot.log"
LISTENER_PID = OPS / "telegram-listener.pid"
GAME_SNAPSHOT = Path("D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json")
BASH = r"C:\Program Files\Git\bin\bash.exe"
NODE = "node"
NO_WINDOW = 0x08000000  # CREATE_NO_WINDOW
DETACHED = 0x00000008  # DETACHED_PROCESS
STALL_MINUTES = 25
LIMIT_WORDS = re.compile(r"usage limit|rate limit|quota (exceeded|reached)|out of credits|429", re.I)
LOG_MAX_BYTES = 512 * 1024


def log(msg: str) -> None:
    if LOG.exists() and LOG.stat().st_size > LOG_MAX_BYTES:
        LOG.replace(LOG.with_suffix(".log.old"))
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")


def load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def save(path: Path, data) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def telegram(text: str) -> None:
    try:
        subprocess.run([NODE, str(ROOT / "scripts/deliver/send-telegram.mjs"), text], creationflags=NO_WINDOW, timeout=60)
    except Exception as exc:
        log(f"telegram failed: {exc}")


def pid_alive(pid: int, image: str = "") -> bool:
    """True when the pid exists (and, when given, its image name contains `image`)."""
    out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH", "/FO", "CSV"], capture_output=True, text=True,
                         creationflags=NO_WINDOW).stdout
    for line in out.splitlines():
        cols = [c.strip('"') for c in line.split('","')]
        if len(cols) > 1 and cols[1] == str(pid):
            return image.lower() in cols[0].lower()
    return False


def kill_tree(pid: int) -> None:
    subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], capture_output=True, creationflags=NO_WINDOW)


HQ_PATHSPEC = ["plans/dashboard_template.html", "plans/generate_dashboard.py", "plans/status_rules.py", "ops/public"]


def minutes_since_activity(folder: str) -> float:
    """Minutes since the last commit or the newest uncommitted edit. 0 on any error, so a broken check never starts a runner.
    For the HQ folder itself only the Control Room files count, so HQ's own notes and briefs never make that project look busy."""
    if Path(folder).resolve() == ROOT.resolve():
        try:
            out = subprocess.run(["git", "-C", folder, "log", "-1", "--format=%ct", "--"] + HQ_PATHSPEC, capture_output=True,
                                 text=True, creationflags=NO_WINDOW).stdout.strip()
            age = (time.time() - int(out)) / 60 if out else 9999
            for rel in HQ_PATHSPEC:
                p = Path(folder) / rel
                if p.is_file():
                    age = min(age, (time.time() - p.stat().st_mtime) / 60)
            return age
        except Exception:
            return 0.0
    try:
        out = subprocess.run(["git", "-C", folder, "log", "-1", "--format=%ct"], capture_output=True, text=True,
                             creationflags=NO_WINDOW).stdout.strip()
        dirty = subprocess.run(["git", "-C", folder, "status", "--porcelain"], capture_output=True, text=True,
                               creationflags=NO_WINDOW).stdout.strip()
        age = (time.time() - int(out)) / 60 if out else 9999
        newest = 0.0
        for line in dirty.splitlines()[:80]:
            rel = line[3:].strip().strip('"')
            if rel.startswith("ops/"):  # HQ runtime files (logs, state) change all the time and are not work
                continue
            p = Path(folder) / rel
            if p.exists():
                newest = max(newest, p.stat().st_mtime)
        if newest:
            age = min(age, (time.time() - newest) / 60)
        return age
    except Exception:
        return 0.0


def ensure_listener() -> None:
    try:
        pid = int(LISTENER_PID.read_text().strip())
    except Exception:
        pid = 0
    if pid and pid_alive(pid, "node"):
        return
    p = subprocess.Popen([NODE, str(ROOT / "scripts/deliver/telegram-inbox.mjs")], creationflags=NO_WINDOW | DETACHED,
                         stdout=open(OPS / "telegram-listener.log", "a"), stderr=subprocess.STDOUT)
    LISTENER_PID.write_text(str(p.pid))
    log(f"telegram listener started pid {p.pid}")


MAX_PARALLEL = 5  # owner 2026-11-11: run every project at once; one writer per project folder is still enforced


def rstate(state: dict, name: str) -> dict:
    return state.setdefault("runners", {}).setdefault(name, {})


def runner_alive(rs: dict) -> bool:
    pid = rs.get("pid")
    return bool(pid and pid_alive(pid, "bash"))


def start_runner(task: dict, state: dict) -> None:
    rs = rstate(state, task["name"])
    prompt = OPS / "briefs" / f"{task['name']}.prompt.txt"
    if not prompt.exists():
        if not rs.get("missing_told"):
            log(f"brief missing for {task['name']}: {prompt}")
            rs["missing_told"] = True
        return
    p = subprocess.Popen([BASH, str(ROOT / "scripts/cli-run2.sh"), task["name"], task["folder"].replace("\\", "/")],
                         creationflags=NO_WINDOW | DETACHED,
                         stdout=open(OPS / "agy-runs" / f"autopilot-{task['name']}.out", "a"), stderr=subprocess.STDOUT)
    rs["pid"] = p.pid
    rs["started"] = time.time()
    log(f"runner started for {task['name']} pid {p.pid}")
    if not rs.get("start_told"):
        log(f"owner message skipped (start): {task['name']}")  # per-task Telegram messages stopped 2026-11-12: one daily summary instead
        rs["start_told"] = True


def limits_hit(task: dict, rs: dict) -> bool:
    """True when the runner's log since its last start shows at least two usage-limit messages."""
    outp = OPS / "agy-runs" / f"cli-{task['name']}.log"
    if not outp.exists() or time.time() - rs.get("started", 0) > 4 * 3600:
        return False
    tail = outp.read_text(encoding="utf-8", errors="ignore")[-4000:]
    if len(LIMIT_WORDS.findall(tail)) < 2:
        return False
    # one tool out of limit is not "all free tools are out": only claim it when the shared pool has nothing left
    pool = subprocess.run([sys.executable, str(ROOT / "scripts/cli_pool.py"), "pick"], capture_output=True, text=True).stdout.strip()
    return pool.startswith("WAIT")


def handle(task: dict, queue: list, state: dict) -> None:
    rs = rstate(state, task["name"])
    if (OPS / "agy-runs" / "done" / f"{task['name']}.done").exists():
        task["done"] = True
        save(QUEUE, queue)
        log(f"task done: {task['name']}")
        log(f"owner message skipped (done): {task['name']}")
        return
    if minutes_since_activity(task["folder"]) < STALL_MINUTES or runner_alive(rs):
        return  # someone is working on it
    if time.time() < rs.get("retry_after", 0):
        return
    if limits_hit(task, rs):
        if not state.get("limit_told"):
            telegram("[الإدارة] أدوات البناء المجانية وصلت لحد الاستخدام. هجرب تاني كل ساعة لحد ما ترجع.")
            state["limit_told"] = True
        rs["retry_after"] = time.time() + 3600
        rs["started"] = 0  # so the next attempt is judged on its own log
        log(f"free limits hit on {task['name']}: retry in 60 min")
        return
    state["limit_told"] = False
    start_runner(task, state)


def step(state: dict) -> None:
    state["last_tick"] = time.time()
    if "runner_pid" in state:  # state written by the single-runner version
        rstate(state, "r14-ahome").update(pid=state.pop("runner_pid"), started=state.pop("runner_started", 0), start_told=True)
    if GAME_SNAPSHOT.exists():
        for rs in state.get("runners", {}).values():
            if runner_alive(rs):
                kill_tree(rs["pid"])
                log("game mode active: runner stopped")
        # Telegram poller pauses while gaming; alert sending (send-telegram.mjs) still works.
        # ensure_listener() restarts it as soon as the game ends.
        try:
            lpid = int(LISTENER_PID.read_text().strip())
        except Exception:
            lpid = 0
        if lpid and pid_alive(lpid, "node"):
            kill_tree(lpid)
            LISTENER_PID.unlink(missing_ok=True)
            log("game mode active: telegram listener stopped")
        if not state.get("paused_for_game"):
            log("game mode active: paused")
        state["paused_for_game"] = True
        return
    if state.pop("paused_for_game", None):
        log("game ended: resumed")
    ensure_listener()
    queue = load(QUEUE, [])
    open_tasks, folders = [], set()
    for t in queue:  # first MAX_PARALLEL unfinished tasks, one per project folder
        if not t.get("done") and t["folder"].lower() not in folders:
            open_tasks.append(t)
            folders.add(t["folder"].lower())
        if len(open_tasks) == MAX_PARALLEL:
            break
    if not open_tasks:
        if queue and not state.get("empty_told"):
            telegram("[الإدارة] كل المهام اللي في القايمة خلصت.")
            state["empty_told"] = True
        return
    state["empty_told"] = False
    for task in open_tasks:
        handle(task, queue, state)


def main() -> None:
    state = load(STATE, {})
    log("autopilot started")
    while True:
        try:
            step(state)
            save(STATE, state)
        except Exception as exc:
            log(f"error: {exc!r}")
        time.sleep(300)


if __name__ == "__main__":
    main()
