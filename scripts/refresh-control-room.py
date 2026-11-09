#!/usr/bin/env python3
"""Refreshes SIR Control Room dashboard and Claude artifact from live workspace telemetry.
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


def refresh():
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now_str}] Starting SIR Control Room telemetry refresh...")
    
    # Run generator
    cmd = [sys.executable, GEN_SCRIPT]
    res = subprocess.run(cmd, cwd=SIR_ROOT, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[{now_str}] ERROR: generate_dashboard.py failed (exit {res.returncode}):")
        print(res.stderr)
        sys.exit(res.returncode)
    
    print(res.stdout.strip())

    changed_hash = ""
    if os.path.exists(CHANGED_FILE):
        with open(CHANGED_FILE, "r", encoding="utf-8") as f:
            changed_hash = f.read().strip()

    published_hash = ""
    if os.path.exists(PUBLISHED_FILE):
        with open(PUBLISHED_FILE, "r", encoding="utf-8") as f:
            published_hash = f.read().strip()

    if changed_hash and published_hash and changed_hash == published_hash:
        status_msg = f"Artifact IN SYNC (hash {changed_hash})"
    else:
        status_msg = f"Artifact OUT OF SYNC: changed={changed_hash or 'none'} vs published={published_hash or 'none'}"

    print(f"[{now_str}] Refresh complete. {status_msg}")
    return 0


if __name__ == "__main__":
    sys.exit(refresh())
