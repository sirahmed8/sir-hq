"""Folder task board shared by the manager (Claude or the backup manager) and every free tool (owner order 2026-11-12).

ops/tasks/inbox/    new tasks and rounds: one markdown file each. Drop a file here and the autopilot queues it.
ops/tasks/active/   claimed and running: the file header says who took it, when, and the last note.
ops/tasks/review/   the worker says it is finished: waiting for a verifier.
ops/tasks/done/     verified (or accepted) tasks, with the report path.
ops/tasks/reports/  one report per finished round (workers write it; the manager reads it and adds the next tasks).

File format (a plain markdown file named <priority>-<name>.md, priority 1 = first):
    ---
    folder: D:/Projects/SIR Study
    title: one line
    parallel_ok: false
    claimed_by:
    claimed_at:
    ---
    brief text (what to do, how it is verified)
    ## Log
    - time tool: note

Commands (for humans and agents):  python taskboard.py add <name> <folder> "<title>" <brief.md> [priority] [parallel_ok]
  list | claim <name> <tool> | note <name> "<text>" | finish <name> "<result>" | pass <name> | handoff <name> "<where you stopped>"
  next <tool>  -> claims the first unclaimed inbox task and prints its path (an idle tool takes work with this)
  sync         -> run by the autopilot every tick: ingests inbox files into the queue, mirrors states of queued tasks
"""
import nowindow  # noqa: F401
import csv
import io
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
BOARD = ROOT / "ops" / "tasks"
QUEUE = ROOT / "ops" / "AUTOPILOT_QUEUE.json"
DONE_DIR = ROOT / "ops" / "agy-runs" / "done"
STATE_FILE = ROOT / "ops" / "autopilot_state.json"
VERIFICATIONS = ROOT / "ops" / "verifications"
CREATE_NO_WINDOW = 0x08000000
RECLAIM_MINUTES = 15
HQ_PATHSPEC = ["plans/dashboard_template.html", "plans/generate_dashboard.py", "plans/status_rules.py", "ops/public"]
STAGES = ("inbox", "active", "review", "done", "reports")
for s in STAGES:
    (BOARD / s).mkdir(parents=True, exist_ok=True)


def pid_alive(pid: int) -> bool:
    """True when `pid` is a running bash, node, or python process."""
    if isinstance(pid, bool):
        return False
    try:
        pid_int = int(pid)
    except (TypeError, ValueError):
        return False
    if pid_int <= 0:
        return False
    try:
        res = subprocess.run(
            ["tasklist", "/FI", f"PID eq {pid_int}", "/NH", "/FO", "CSV"],
            capture_output=True,
            text=True,
            timeout=10,
            creationflags=CREATE_NO_WINDOW if os.name == "nt" else 0,
            env={**os.environ, "MSYS_NO_PATHCONV": "1"},
        )
    except (OSError, subprocess.SubprocessError):
        return False
    for row in csv.reader(io.StringIO(res.stdout or "")):
        if len(row) >= 2 and row[1].strip() == str(pid_int):
            image = row[0].strip().lower()
            return any(tok in image for tok in ("bash", "node", "python"))
    return False


def minutes_since_activity(folder: str) -> float:
    """Minutes since the last commit or newest uncommitted edit in `folder`."""
    if not folder or not Path(folder).exists():
        return 9999.0
    flags = CREATE_NO_WINDOW if os.name == "nt" else 0
    try:
        is_hq = Path(folder).resolve() == ROOT.resolve()
    except OSError:
        return 9999.0
    if is_hq:
        try:
            res = subprocess.run(
                ["git", "-C", folder, "log", "-1", "--format=%ct", "--"] + HQ_PATHSPEC,
                capture_output=True,
                text=True,
                timeout=15,
                creationflags=flags,
            )
            out = (res.stdout or "").strip()
            age = (time.time() - int(out)) / 60 if res.returncode == 0 and out.isdigit() else 9999.0
            for rel in HQ_PATHSPEC:
                p = Path(folder) / rel
                if p.is_file():
                    age = min(age, (time.time() - p.stat().st_mtime) / 60)
                elif p.is_dir():
                    for sub in p.rglob("*"):
                        if sub.is_file():
                            age = min(age, (time.time() - sub.stat().st_mtime) / 60)
            return age
        except Exception:
            return 0.0
    try:
        res = subprocess.run(
            ["git", "-C", folder, "log", "-1", "--format=%ct"],
            capture_output=True,
            text=True,
            timeout=15,
            creationflags=flags,
        )
        dirty_res = subprocess.run(
            ["git", "-C", folder, "status", "--porcelain"],
            capture_output=True,
            text=True,
            timeout=15,
            creationflags=flags,
        )
        out = (res.stdout or "").strip()
        age = (time.time() - int(out)) / 60 if res.returncode == 0 and out.isdigit() else 9999.0
        newest = 0.0
        for line in (dirty_res.stdout or "").rstrip().splitlines():
            if len(line) < 4:
                continue
            rel = line[3:].strip().split(" -> ")[-1].strip('"')
            if rel.startswith("ops/") or rel.startswith("assets/brand/") or rel.endswith((".ico", "desktop.ini")):
                continue
            p = Path(folder) / rel
            if p.exists():
                newest = max(newest, p.stat().st_mtime)
        if newest:
            age = min(age, (time.time() - newest) / 60)
        return age
    except Exception:
        return 0.0


def _load_state() -> dict:
    try:
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _save_state(data: dict) -> None:
    tmp = STATE_FILE.with_suffix(STATE_FILE.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STATE_FILE)


def stamp() -> str:
    return time.strftime("%m-%d %H:%M")


def find(name: str):
    for s in STAGES[:4]:
        for p in (BOARD / s).glob("*.md"):
            if re.sub(r"^\d+-", "", p.stem) == name:
                return p, s
    return None, None


def header(text: str):
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def write(p: Path, meta: dict, body: str) -> None:
    head = "\n".join(f"{k}: {v}" for k, v in meta.items())
    p.write_text(f"---\n{head}\n---\n{body}", encoding="utf-8")


def move(p: Path, stage: str) -> Path:
    dest = BOARD / stage / p.name
    os.replace(p, dest)  # atomic on one disk: the first tool to move a file owns it
    return dest


def add(name, folder, title, brief, priority="5", parallel_ok="false") -> Path:
    body = Path(brief).read_text(encoding="utf-8") if Path(brief).exists() else brief
    p = BOARD / "inbox" / f"{priority}-{name}.md"
    write(p, {"folder": folder, "title": title, "parallel_ok": parallel_ok, "claimed_by": "", "claimed_at": ""},
          body.rstrip() + "\n\n## Log\n")
    return p


def claim(name, tool):
    p, st = find(name)
    if not p or st != "inbox":
        return None
    try:
        q = move(p, "active")
    except OSError:
        return None  # another tool was faster
    meta, body = header(q.read_text(encoding="utf-8"))
    meta.update(claimed_by=tool, claimed_at=stamp())
    write(q, meta, body.rstrip() + f"\n- {stamp()} {tool}: claimed\n")
    return q


def note(name, text, tool="worker"):
    p, _ = find(name)
    if p:
        with p.open("a", encoding="utf-8") as f:
            f.write(f"- {stamp()} {tool}: {text}\n")


def stage_to(name, stage, text):
    p, st = find(name)
    if p and st != stage:
        q = move(p, stage)
        note(name, text, "board")
        return q
    return p


def queue_names():
    try:
        return {t["name"]: t for t in json.loads(QUEUE.read_text(encoding="utf-8"))}
    except (OSError, ValueError):
        return {}


def sync() -> str:
    """Autopilot tick: inbox files become queue tasks; the queue's real state moves the files between folders."""
    q = json.loads(QUEUE.read_text(encoding="utf-8")) if QUEUE.exists() else []
    names = {t["name"] for t in q}
    changed = 0
    for p in sorted((BOARD / "inbox").glob("*.md")):
        name = re.sub(r"^\d+-", "", p.stem)
        meta, body = header(p.read_text(encoding="utf-8"))
        if name in names or not meta.get("folder"):
            continue
        prompt = ROOT / "ops" / "briefs" / f"{name}.md"
        prompt.write_text(body, encoding="utf-8")
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "queue-add.py"), name, str(prompt), meta["folder"],
             meta.get("title", name)],
            capture_output=True,
            creationflags=CREATE_NO_WINDOW if os.name == "nt" else 0,
        )
        q = json.loads(QUEUE.read_text(encoding="utf-8"))
        for t in q:
            if t["name"] == name:
                t["parallel_ok"] = meta.get("parallel_ok", "false").lower() == "true"
                if p.name[0].isdigit() and int(p.name.split("-")[0]) <= 2:  # priority 1 and 2 go first
                    pass
        QUEUE.write_text(json.dumps(q, ensure_ascii=False, indent=2), encoding="utf-8")
        names.add(name)
        changed += 1
    runners = _load_state().get("runners", {})
    if not isinstance(runners, dict):
        runners = {}
    for t in q:
        name = t["name"]
        p, st = find(name)
        if not p:  # mirror older queue entries into the board once
            p = BOARD / ("done" if t.get("done") else "inbox") / f"5-{name}.md"
            write(p, {"folder": t["folder"], "title": t.get("title", name), "parallel_ok": str(bool(t.get("parallel_ok"))).lower(),
                      "claimed_by": "", "claimed_at": ""}, f"(mirrored from the queue) {t.get('title', name)}\n\n## Log\n")
            st = "done" if t.get("done") else "inbox"
        rs = runners.get(name, {})
        if not isinstance(rs, dict):
            rs = {}
        if t.get("done") and st in ("inbox", "active"):
            stage_to(name, "review", "finished (done marker); waiting for a verifier")
            changed += 1
        elif not t.get("done") and rs.get("pid") and pid_alive(rs["pid"]) and st == "inbox":
            q2 = stage_to(name, "active", "runner started by the autopilot")
            meta, body = header(q2.read_text(encoding="utf-8"))
            meta.update(claimed_by="autopilot runner", claimed_at=stamp())
            write(q2, meta, body)
            changed += 1
    # reclaim active tasks whose autopilot runner PID is dead and whose folder is idle >= 15 min
    qmap = {t["name"]: t for t in q if isinstance(t, dict) and "name" in t}
    cleared_pids = {}
    for p in sorted((BOARD / "active").glob("*.md")):
        name = re.sub(r"^\d+-", "", p.stem)
        meta, _ = header(p.read_text(encoding="utf-8"))
        if meta.get("claimed_by") != "autopilot runner":
            continue
        t = qmap.get(name, {})
        if t.get("done"):
            continue
        rs = runners.get(name, {})
        pid = rs.get("pid", 0) if isinstance(rs, dict) else 0
        if pid_alive(pid):
            continue
        folder = t.get("folder") or meta.get("folder", "")
        if minutes_since_activity(folder) < RECLAIM_MINUTES:
            continue
        q2 = stage_to(name, "inbox", "runner dead and folder idle >= 15m; returned to inbox")
        if q2:
            m2, b2 = header(q2.read_text(encoding="utf-8"))
            m2.update(claimed_by="", claimed_at="")
            write(q2, m2, b2)
        if isinstance(rs, dict) and "pid" in rs:
            cleared_pids[name] = rs.get("pid")
        changed += 1
    if cleared_pids:
        latest = _load_state()
        latest_runners = latest.setdefault("runners", {})
        dirty = False
        for name, dead_pid in cleared_pids.items():
            entry = latest_runners.get(name)
            if isinstance(entry, dict) and entry.get("pid") == dead_pid:
                entry.pop("pid", None)
                dirty = True
        if dirty:
            _save_state(latest)
    # verified tasks: ## Overall: PASS moves review -> done; keep FAIL in review unless <name>-fix1 has Overall: PASS
    pass_re = re.compile(r"(?m)^##\s*Overall:\s*PASS\b", re.I)
    fail_re = re.compile(r"(?m)^##\s*Overall:\s*FAIL\b", re.I)
    for p in sorted((BOARD / "review").glob("*.md")):
        name = re.sub(r"^\d+-", "", p.stem)
        direct = [
            v for v in sorted(VERIFICATIONS.glob("*.md"))
            if v.stem == name or re.sub(r"^\d+-", "", v.stem) == name
        ]
        passed_file = None
        has_fail = False
        for v in direct:
            try:
                text = v.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if pass_re.search(text):
                passed_file = v
                break
            if fail_re.search(text):
                has_fail = True
        if passed_file:
            stage_to(name, "done", f"verified: {passed_file.name}")
            changed += 1
        elif has_fail:
            fix_name = f"{name}-fix1"
            fix_files = [
                v for v in sorted(VERIFICATIONS.glob("*.md"))
                if v.stem == fix_name or re.sub(r"^\d+-", "", v.stem) == fix_name
            ]
            for fv in fix_files:
                try:
                    ftext = fv.read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    continue
                if pass_re.search(ftext):
                    stage_to(name, "done", f"verified via {fv.name}")
                    changed += 1
                    break
    return f"board synced, {changed} changes"


def lst():
    for s in STAGES[:4]:
        files = sorted((BOARD / s).glob("*.md"))
        print(f"{s:7} {len(files)}")
        if s != "done":
            for p in files[:40]:
                meta, _ = header(p.read_text(encoding="utf-8"))
                print(f"   {p.stem:55} {meta.get('claimed_by', '')}")


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else "list"
    a = sys.argv[2:]
    if c in ("-h", "--help", "help"):
        print(__doc__)
    elif c == "add":
        print(add(*a))
    elif c == "claim":
        if len(a) < 2 or a[1].startswith("-"):
            sys.exit("usage: taskboard.py claim <name> <tool>")
        print(claim(a[0], a[1]))
    elif c == "next":
        if a and a[0].startswith("-"):
            print(__doc__)
            sys.exit(0)
        got = None
        for p in sorted((BOARD / "inbox").glob("*.md")):
            got = claim(re.sub(r"^\d+-", "", p.stem), a[0] if a else "worker")
            if got:
                break
        print(got or "nothing to claim")
    elif c == "note":
        note(a[0], a[1], a[2] if len(a) > 2 else "worker")
    elif c == "finish":
        stage_to(a[0], "review", "finished: " + a[1])
    elif c == "pass":
        stage_to(a[0], "done", "verified")
    elif c == "handoff":
        note(a[0], "HANDOFF " + a[1])
        p, st = find(a[0])
        if p and st == "active":
            move(p, "inbox")
    elif c == "sync":
        print(sync())
    else:
        lst()
