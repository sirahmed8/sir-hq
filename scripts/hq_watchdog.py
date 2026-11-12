"""HQ watchdog: runs every 10 minutes (scheduled task SIR_HQ_Watchdog) next to the autopilot and keeps the whole team moving.

What it does each run (no AI, no network except `gh`):
1. snapshot: per project last commit age, last edit age, CI state of the last run on main, open queue tasks, live runners -> ops/watchdog_state.json
2. autopilot heartbeat older than 12 minutes -> start the scheduled task SIR_HQ_Autopilot again
3. a project whose last CI run on main is red and that has no open task -> queue a "fix CI" task for it (brief written from a template)
4. queue empty -> queue an audit-loop task for up to 2 projects (the project that has gone longest without a commit first)
5. C: free space under 4.5 GB -> clear temp, npm, pip, uv and pnpm caches (regenerable only); under 2 GB -> also tell Ahmed once per episode
6. every model in the pool cooling for more than 3 hours -> one Telegram note (once)
Never touches AHome files: for AHome it only reads git and gh output. Log: ops/watchdog.log.
"""
import nowindow  # noqa: F401  (no console windows for child processes)
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
OPS = ROOT / "ops"
STATE = OPS / "watchdog_state.json"
LOG = OPS / "watchdog.log"
QUEUE = OPS / "AUTOPILOT_QUEUE.json"
PROJECTS = {
    "AHome": "D:/Projects/AHome",
    "SIR Jobs": "D:/Projects/SIR Jobs",
    "SIR Study": "D:/Projects/SIR Study",
    "SIR Laptop Manager": "D:/Projects/SIR Laptop Manager",
    "_SIR": "D:/Projects/_SIR",
}
NO_WINDOW = 0x08000000
CI_FIX = """{project}, CI repair round (written by the HQ watchdog {stamp}). Read AGENTS.md, .sir/CHECKPOINT.md and D:/Projects/_SIR/ops/WORKER_PREAMBLE.md first.
The last run of the main workflow on main is RED. Run `gh run list --limit 5`, open the newest failed run with `gh run view <id> --log-failed`, find the real cause, fix it properly (never skip, delete or loosen a test), push, and wait until `gh run list --limit 3` shows green. Then write a short report to D:/Projects/_SIR/ops/agy-runs/reports/{task}.md and run `python D:/Projects/_SIR/scripts/agy-done.py {task} ok "<one line>"`."""
AUDIT = """{project}, audit loop round (written by the HQ watchdog {stamp}). Read AGENTS.md, .sir/CHECKPOINT.md, D:/Projects/_SIR/ops/WORKER_PREAMBLE.md and D:/Projects/_SIR/plans/PERPETUAL_LOOP.md first.
Open every page, tab, sheet and flow of the running app at 320, 390, 768 and 1280 px, light and dark, in every language it supports, in a real browser. Log every defect (overlap, clipping, wrong colours, missing or jumpy animation, dead buttons, empty states without action, two names for one thing, slow feedback) in .sir/DEFECTS_{stamp}.md, fix each at its root, add a browser test, commit and push after each fix, keep CI green. Ship at least 10 visible improvements with before and after screenshots under .sir/evidence/. Repeat until two cycles in a row find nothing. Report in D:/Projects/_SIR/ops/agy-runs/reports/{task}.md, then run `python D:/Projects/_SIR/scripts/agy-done.py {task} ok "<one line>"`."""


def log(msg: str) -> None:
    if LOG.exists() and LOG.stat().st_size > 300_000:
        LOG.replace(LOG.with_suffix(".log.old"))
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")


def run(cmd: list[str], timeout: int = 60) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, creationflags=NO_WINDOW).stdout.strip()
    except Exception:
        return ""


def load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def telegram(text: str) -> None:
    run(["node", str(ROOT / "scripts/deliver/send-telegram.mjs"), text])


def commit_age_min(folder: str) -> float:
    out = run(["git", "-C", folder, "log", "-1", "--format=%ct"])
    return (time.time() - int(out)) / 60 if out.isdigit() else 99999.0


def ci_state(folder: str) -> str:
    try:
        res = subprocess.run(["gh", "run", "list", "--limit", "1", "--json", "status,conclusion"], cwd=folder,
                             capture_output=True, text=True, timeout=40, creationflags=NO_WINDOW).stdout
        runs = json.loads(res or "[]")
    except Exception:
        return "unknown"
    if not runs:
        return "none"
    r = runs[0]
    return "running" if r.get("status") != "completed" else (r.get("conclusion") or "unknown")


def audio_players() -> list[dict]:
    """Windows audio sessions actively playing sound, via Core Audio (pycaw).

    Returns [{pid, process, display_name, peak}] for sessions in the Active state with a
    non-zero peak. Empty list when pycaw is not installed or the call fails."""
    try:
        from pycaw.constants import AudioSessionState
        from pycaw.pycaw import AudioUtilities, IAudioMeterInformation
    except Exception:
        return []
    players = []
    try:
        sessions = AudioUtilities.GetAllSessions()
    except Exception:
        return []
    for sess in sessions:
        try:
            if int(sess.State) != int(AudioSessionState.Active):
                continue
            meter = sess._ctl.QueryInterface(IAudioMeterInformation)
            peak = float(meter.GetPeakValue())
            if peak < 0.001:
                continue
            proc = sess.Process
            players.append({
                "pid": int(sess.ProcessId),
                "process": proc.name() if proc is not None else "",
                "display_name": sess._ctl.GetDisplayName() or "",
                "peak": round(peak, 4),
            })
        except Exception:
            continue
    return players


def queue_task(name: str, folder: str, title: str, text: str) -> None:
    brief = OPS / "briefs" / f"{name}.md"
    brief.write_text(text, encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "scripts/queue-add.py"), name, str(brief), folder, title],
                   capture_output=True, creationflags=NO_WINDOW)
    log(f"queued {name} for {folder}")


def main() -> None:
    if Path("D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json").exists():  # a game is running: stay quiet
        log("skip: game mode active")
        return
    state = load(STATE, {})
    now, stamp = time.time(), time.strftime("%Y%m%d-%H%M")
    queue = load(QUEUE, [])
    open_tasks = [t for t in queue if not t.get("done")]
    open_folders = {t["folder"].lower() for t in open_tasks}
    ap = load(OPS / "autopilot_state.json", {})
    if now - ap.get("last_tick", 0) > 720:
        run(["powershell", "-NoProfile", "-Command", "Start-ScheduledTask -TaskName SIR_HQ_Autopilot"])
        log("autopilot heartbeat old: started task SIR_HQ_Autopilot")
    snap = {}
    for name, folder in PROJECTS.items():
        snap[name] = {"last_commit_min": round(commit_age_min(folder)), "ci": ci_state(folder),
                      "open_tasks": [t["name"] for t in open_tasks if t["folder"].lower() == folder.lower()]}
    state["snapshot"], state["at"] = snap, now
    for name, folder in PROJECTS.items():
        s = snap[name]
        if name == "AHome":
            continue  # private: only the Haiku run inside the AHome folder works on it, never the free-CLI queue
        if (ROOT / "ops" / "ci-quota-exhausted.flag").exists():
            continue  # GitHub Actions minutes are used up: red CI is not a code defect, workers test locally
        if s["ci"] == "failure" and not s["open_tasks"] and folder.lower() not in open_folders:
            task = f"ci-{name.lower().replace(' ', '-').strip('_')}-{stamp}"
            queue_task(task, folder, f"{name}: إصلاح الفحص الآلي الأحمر", CI_FIX.format(project=name, stamp=stamp, task=task))
            telegram(f"[الإدارة] الفحص الآلي أحمر في {name}. حطيت مهمة إصلاح في القايمة.")
            open_folders.add(folder.lower())
    if not open_tasks and not any(snap[n]["open_tasks"] for n in snap):
        for name in [n for n in sorted(PROJECTS, key=lambda n: -snap[n]["last_commit_min"]) if n != "AHome"][:2]:
            if name == "_SIR":
                continue
            task = f"audit-{name.lower().replace(' ', '-')}-{stamp}"
            queue_task(task, PROJECTS[name], f"{name}: دورة فحص ذاتي", AUDIT.format(project=name, stamp=stamp, task=task))
    # log every process that is playing audio right now (names the unknown-sound culprit)
    players = audio_players()
    if players:
        names = ", ".join(f"{p['process'] or p['display_name'] or 'pid ' + str(p['pid'])}" for p in players)
        log(f"audio playing: {names}")
        state["last_audio_players"] = {"at": now, "players": players}
    # test browsers leaked by workers (they also play audio): kill Playwright and headless
    # browser processes older than 25 minutes, nothing else
    run(["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process | ? { (($_.CommandLine -match 'ms-playwright') -or "
         "($_.CommandLine -match '--headless' -and $_.Name -match 'chrome|msedge|chromium')) -and "
         "((Get-Date)-$_.CreationDate).TotalMinutes -gt 25 } | % { Stop-Process -Id $_.ProcessId -Force -EA 0 }"])
    free_gb = shutil.disk_usage("C:/").free / 1024**3
    state["c_free_gb"] = round(free_gb, 1)
    if free_gb < 4.5:
        run(["powershell", "-NoProfile", "-Command",
             "Get-ChildItem $env:TEMP -Force -EA 0 | ? { $_.Name -ne 'claude' } | % { Remove-Item $_.FullName -Recurse -Force -EA 0 }; "
             "Remove-Item \"$env:LOCALAPPDATA\\CrashDumps\\*\" -Recurse -Force -EA 0; "
             "npm cache clean --force 2>$null; pip cache purge 2>$null; uv cache clean --force 2>$null; "
             "Remove-Item \"$env:LOCALAPPDATA\\pnpm-cache\\*\" -Recurse -Force -EA 0"], timeout=240)
        after = shutil.disk_usage("C:/").free / 1024**3
        log(f"C: low ({free_gb:.1f} GB): cleaned temp and caches, now {after:.1f} GB")
        if free_gb < 2.0 and not state.get("disk_told"):
            telegram(f"[الإدارة] مساحة C: نزلت تحت 2 جيجا ({free_gb:.1f} جيجا). نضفت الملفات المؤقتة والكاشات، بقت {after:.1f} جيجا. لو لسه بتقل كل يوم قولّي.")
            state["disk_told"] = True
    elif free_gb > 6:
        state["disk_told"] = False
    d_free_gb = shutil.disk_usage("D:/").free / 1024**3  # read-only check: D: holds projects and games, never auto-cleaned here (needs judgment)
    state["d_free_gb"] = round(d_free_gb, 1)
    if d_free_gb < 5 and not state.get("d_disk_told"):
        telegram(f"[الإدارة] مساحة D: قربت تخلص ({d_free_gb:.1f} جيجا فاضية). محتاجة تنضيف يدوي (ألعاب أو ملفات مشاريع قديمة)، المراقب مش بيمسح منها لوحده.")
        state["d_disk_told"] = True
        log(f"D: low ({d_free_gb:.1f} GB): alerted, no auto-clean on D:")
    elif d_free_gb > 8:
        state["d_disk_told"] = False
    pool = load(OPS / "agy-runs" / "model-pool.json", {})
    cooling = [v.get("until", 0) - now for v in pool.values() if v.get("until", 0) > now]
    if len(cooling) >= 8 and min(cooling) > 3 * 3600 and not state.get("pool_told"):
        telegram("[الإدارة] كل الموديلات المجانية واقفة أكتر من 3 ساعات. بنستنى التجديد.")
        state["pool_told"] = True
    elif len(cooling) < 8:
        state["pool_told"] = False
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    log("ok " + " ".join(f"{n}:{s['ci']}/{s['last_commit_min']}m" for n, s in snap.items()) + f" C:{free_gb:.1f}GB")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        log(f"error: {exc!r}")
