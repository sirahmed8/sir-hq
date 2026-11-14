"""Hourly: publish ops/artifact/control-room.html to the owner's Claude artifact with a cheap headless Haiku run, so the page the owner reads stays current without any chat open.
Skips in game mode, skips when the generated file did not change since the last publish.
ops/artifact/PUBLISHED.txt holds the hash of the last artifact that was really published (one hash per line);
ops/artifact/CHANGED.txt holds the hash of the artifact on disk. Log: ops/artifact/publish.log"""
import hashlib
import subprocess
import sys
import time
from pathlib import Path

import nowindow  # noqa: F401

ROOT = Path("D:/Projects/_SIR")
HTML = ROOT / "ops" / "artifact" / "control-room.html"
STATE = ROOT / "ops" / "artifact" / "PUBLISHED.txt"
LOG = ROOT / "ops" / "artifact" / "publish.log"
GAME = Path("D:/Projects/SIR Optimizer/.sir/game_mode_snapshot.json")
CLAUDE = Path.home() / ".local" / "bin" / "claude.exe"
URL = "https://claude.ai/code/artifact/5903680d-7f79-4595-a8ea-31b0f4c3b2db"


def log(msg: str) -> None:
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")


def main() -> int:
    if GAME.exists():
        log("skip: game mode")
        return 0
    gen = subprocess.run([sys.executable, str(ROOT / "plans" / "generate_dashboard.py")], capture_output=True, text=True, timeout=300)
    if gen.returncode != 0 or not HTML.exists():
        log(f"generate failed: {gen.returncode}")
        return 1
    digest = hashlib.sha256(HTML.read_bytes()).hexdigest()[:8]
    last = STATE.read_text(encoding="utf-8").strip().split()[-1] if STATE.exists() else ""
    if digest == last:
        log(f"skip: unchanged {digest}")
        return 0
    prompt = (f"Use the Artifact tool to publish the file {HTML.as_posix()} to the existing artifact url {URL} (parameter url). "
              "If the tool refuses because you have not read it, first call the Artifact tool with action read on that url, then publish the file again. "
              "Reply with one line: published or the exact error.")
    res = subprocess.run([str(CLAUDE), "-p", prompt, "--model", "haiku", "--permission-mode", "bypassPermissions"],
                         capture_output=True, text=True, timeout=600, stdin=subprocess.DEVNULL)
    out = (res.stdout or res.stderr or "").strip().splitlines()[-1:] or [""]
    # The helper must say "published" and nothing else: "not published" is a failure, not a success.
    ok = out[0].strip().lower().startswith("published")
    if ok:
        log(f"published {digest}")
        STATE.write_text(digest + "\n", encoding="utf-8")
    else:
        log(f"FAILED {digest}: {out[0].strip()[:160]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
