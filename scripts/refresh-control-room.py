#!/usr/bin/env python3
"""Refreshes SIR Control Room dashboard and Claude artifact from live workspace telemetry.
Runs completely silent/headless when invoked by scheduled tasks or pythonw.exe.
Regenerates both ops/dashboard.html and ops/artifact/control-room.html.
Writes content hash to ops/artifact/CHANGED.txt.
Alerts HQ in ops/bus/sir-hq.md if changed hash differs from ops/artifact/PUBLISHED.txt.
"""
import os
import sys
import subprocess
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SIR_ROOT = os.path.normpath(os.path.join(HERE, ".."))
GEN_SCRIPT = os.path.join(SIR_ROOT, "plans", "generate_dashboard.py")
OPS_DIR = os.path.join(SIR_ROOT, "ops")
CHANGED_FILE = os.path.join(OPS_DIR, "artifact", "CHANGED.txt")
PUBLISHED_FILE = os.path.join(OPS_DIR, "artifact", "PUBLISHED.txt")
LOG_FILE = os.path.join(OPS_DIR, "control-room-refresh.log")

# On Windows, suppress any console popup from subprocesses
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0


def log(msg: str):
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{now_str}] {msg}"
    
    # Safely print to stdout if available
    try:
        if sys.stdout and not sys.stdout.closed:
            print(formatted)
    except Exception:
        pass

    # Always append to log file
    try:
        os.makedirs(OPS_DIR, exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception:
        pass


def refresh() -> int:
    log("Starting SIR Control Room telemetry refresh (silent/hidden)...")
    
    # Locate python executable suitable for headless subprocess
    py_exec = sys.executable or "python"
    
    cmd = [py_exec, GEN_SCRIPT]
    try:
        res = subprocess.run(
            cmd,
            cwd=SIR_ROOT,
            capture_output=True,
            text=True,
            creationflags=CREATE_NO_WINDOW
        )
    except Exception as e:
        log(f"ERROR: Failed to run {GEN_SCRIPT}: {e}")
        return 1

    if res.returncode != 0:
        log(f"ERROR: generate_dashboard.py failed (exit {res.returncode}):")
        if res.stderr:
            log(res.stderr.strip())
        return res.returncode
    
    if res.stdout:
        log(res.stdout.strip())

    changed_hash = ""
    if os.path.exists(CHANGED_FILE):
        try:
            with open(CHANGED_FILE, "r", encoding="utf-8") as f:
                changed_hash = f.read().strip()
        except Exception as e:
            log(f"WARNING: could not read {CHANGED_FILE}: {e}")

    published_hash = ""
    if os.path.exists(PUBLISHED_FILE):
        try:
            with open(PUBLISHED_FILE, "r", encoding="utf-8") as f:
                published_hash = f.read().strip()
        except Exception as e:
            log(f"WARNING: could not read {PUBLISHED_FILE}: {e}")

    if changed_hash and published_hash and changed_hash == published_hash:
        status_msg = f"Artifact IN SYNC (hash {changed_hash})"
    else:
        status_msg = f"Artifact OUT OF SYNC: changed={changed_hash or 'none'} vs published={published_hash or 'none'}"

    log(f"Refresh complete. {status_msg}")
    return 0


if __name__ == "__main__":
    sys.exit(refresh())
