"""One entry point for the r42 background rounds, called by Windows scheduled tasks.

Every round: pauses while a game runs (game mode snapshot), runs at below-normal priority, takes a lock so two
rounds never overlap, then hands over to the real script:

  verifier     scripts/hq_verifier.py   (prove every done task, :30 round times)
  scouts       scripts/scout.py --all   (daily, every project, new lens)
  review       scripts/hq_review.py     (approve/reject suggestions, :00 round times)
  notify-fails scripts/hq_notify.py --fails
  notify-daily scripts/hq_notify.py --daily  (21:00)

Usage: python r42_rounds.py <verifier|scouts|review|notify-fails|notify-daily> [--dry]
Exit code 0 when the round itself worked.
"""
import nowindow  # noqa: F401  (no console windows for child processes)
import subprocess
import sys
import time
from pathlib import Path

from hq_team import OPS, ROOT, game_mode_active, log, lower_priority

JOBS = {
    "verifier": ["hq_verifier.py", "--limit", "5"],
    "scouts": ["scout.py", "--all"],
    "review": ["hq_review.py"],
    "notify-fails": ["hq_notify.py", "--fails"],
    "notify-daily": ["hq_notify.py", "--daily"],
}
STALE_SECONDS = 5400
NO_WINDOW = 0x08000000


def main(argv: list) -> int:
    if not argv or argv[0] not in JOBS:
        print(__doc__)
        return 2
    job = argv[0]
    extra = [a for a in argv[1:] if a.startswith("--")]
    if game_mode_active():
        log("rounds", f"{job}: skip, game mode active")
        print("skip: game mode active")
        return 0
    lower_priority()
    locks = OPS / "locks"
    locks.mkdir(parents=True, exist_ok=True)
    lock = locks / f"r42-{job}.lock"
    if lock.exists() and time.time() - lock.stat().st_mtime < STALE_SECONDS:
        log("rounds", f"{job}: skip, previous round still running")
        print("skip: previous round still running")
        return 0
    lock.write_text(time.strftime("%Y-%m-%d %H:%M:%S"), encoding="utf-8")
    started = time.time()
    try:
        cmd = [sys.executable, str(ROOT / "scripts" / JOBS[job][0])] + JOBS[job][1:] + extra
        res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=7200,
                             creationflags=NO_WINDOW)
        out = ((res.stdout or "") + (res.stderr or "")).strip()
        log("rounds", f"{job}: exit {res.returncode} in {time.time() - started:.0f}s, {out[-300:]!r}")
        print(out[-2000:])
        return 0 if res.returncode == 0 else res.returncode
    except subprocess.TimeoutExpired:
        log("rounds", f"{job}: timeout")
        return 1
    finally:
        try:
            lock.unlink()
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
