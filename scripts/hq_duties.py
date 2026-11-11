"""Owner's day rhythm as OS background duties (scheduled task SIR_HQ_Duties, every 10 minutes). Independent of any chat session.
Real prayer times each day (Aladhan, Egyptian method, Cairo area) decide when each duty is due:
  fajr = Fajr + 3 min, health_asr = Asr + 10, isha_summary = Isha + 15, health_isha = Isha + 75.
A duty runs once per day, within 120 minutes after its time, and never while a game runs (game-mode snapshot).
It starts `claude -p` headless with ops/duties/<name>.md (Gmail and Calendar tools; fallback manager may swap the command for another agent CLI).
State: _local/duties_state.json, log: ops/duties.log."""
import json
import subprocess
import time
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
LOCAL = ROOT / "_local"
LOG = ROOT / "ops" / "duties.log"
STATE = LOCAL / "duties_state.json"
GAME = Path("D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json")
CLAUDE = Path.home() / ".local" / "bin" / "claude.exe"
NO_WINDOW = 0x08000000
OFFSETS = {"fajr": ("Fajr", 3), "health_asr": ("Asr", 10), "isha_summary": ("Isha", 15), "health_isha": ("Isha", 75)}
MODEL = {"fajr": "sonnet", "isha_summary": "sonnet", "health_asr": "haiku", "health_isha": "haiku"}


def log(msg: str) -> None:
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")


def prayer_times(day: datetime) -> dict:
    cache = LOCAL / f"prayer_{day:%Y-%m-%d}.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    url = f"https://api.aladhan.com/v1/timings/{day:%d-%m-%Y}?latitude=30.2&longitude=31.47&method=5&timezonestring=Africa/Cairo"
    with urllib.request.urlopen(url, timeout=30) as r:
        t = json.load(r)["data"]["timings"]
    out = {k: t[k][:5] for k in ("Fajr", "Dhuhr", "Asr", "Maghrib", "Isha")}
    cache.write_text(json.dumps(out), encoding="utf-8")
    return out


def main() -> None:
    LOCAL.mkdir(exist_ok=True)
    if GAME.exists():
        log("skip: game mode active")
        return
    now = datetime.now()
    state = {}
    try:
        state = json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        pass
    today = f"{now:%Y-%m-%d}"
    done = state.get(today, [])
    try:
        times = prayer_times(now)
    except Exception as exc:
        log(f"prayer times failed: {exc!r}")
        return
    for name, (prayer, minutes) in OFFSETS.items():
        h, m = map(int, times[prayer].split(":"))
        due = now.replace(hour=h, minute=m, second=0, microsecond=0) + timedelta(minutes=minutes)
        if name in done or not (due <= now < due + timedelta(minutes=120)):
            continue
        prompt = (ROOT / "ops" / "duties" / f"{name}.md").read_text(encoding="utf-8")
        log(f"start {name} (due {due:%H:%M}, {prayer} {times[prayer]})")
        done.append(name)
        state = {today: done}
        STATE.write_text(json.dumps(state), encoding="utf-8")
        try:
            res = subprocess.run([str(CLAUDE), "-p", prompt, "--model", MODEL[name], "--permission-mode", "bypassPermissions"],
                                 cwd=str(ROOT), capture_output=True, text=True, timeout=1200, creationflags=NO_WINDOW)
            log(f"finished {name} code {res.returncode}: {(res.stdout or res.stderr)[-200:].strip()!r}")
        except Exception as exc:
            log(f"{name} failed: {exc!r}")
        return  # one duty per run


if __name__ == "__main__":
    main()
