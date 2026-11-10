#!/usr/bin/env python3
"""Refreshes SIR Control Room dashboard and public files.
Silent/headless. Records refresh result in ops/control-room-health.json.
"""
import os
import sys
import subprocess
import datetime
import json

HERE = os.path.dirname(os.path.abspath(__file__))
SIR_ROOT = os.path.normpath(os.path.join(HERE, ".."))
GEN_SCRIPT = os.path.join(SIR_ROOT, "plans", "generate_dashboard.py")
OPS_DIR = os.path.join(SIR_ROOT, "ops")
LOG_FILE = os.path.join(OPS_DIR, "control-room-refresh.log")
HEALTH_FILE = os.path.join(OPS_DIR, "control-room-health.json")
CHANGED_FILE = os.path.join(OPS_DIR, "artifact", "CHANGED.txt")
PUBLISHED_FILE = os.path.join(OPS_DIR, "artifact", "PUBLISHED.txt")

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
LOG_MAX_BYTES = 1_000_000
LOG_BACKUPS = 3


def rotate_log_if_needed():
    try:
        if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) < LOG_MAX_BYTES:
            return
        oldest = f"{LOG_FILE}.{LOG_BACKUPS}"
        if os.path.exists(oldest):
            os.remove(oldest)
        for i in range(LOG_BACKUPS - 1, 0, -1):
            src = f"{LOG_FILE}.{i}"
            if os.path.exists(src):
                os.replace(src, f"{LOG_FILE}.{i + 1}")
        os.replace(LOG_FILE, f"{LOG_FILE}.1")
    except Exception:
        pass


def log(msg: str):
    rotate_log_if_needed()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{now_str}] {msg}"
    try:
        if sys.stdout and not sys.stdout.closed:
            print(formatted)
    except Exception:
        pass
    try:
        os.makedirs(OPS_DIR, exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception:
        pass


def record_refresh(ok: bool, error: str | None = None):
    try:
        data = {}
        if os.path.exists(HEALTH_FILE):
            with open(HEALTH_FILE, "r", encoding="utf-8") as f:
                data = json.load(f) or {}
        data["last_refresh_ok"] = ok
        data["last_refresh_time"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        data["last_error"] = error
        tmp = HEALTH_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, HEALTH_FILE)
    except Exception:
        pass


def refresh() -> int:
    log("Starting SIR Control Room telemetry refresh...")
    py_exec = sys.executable or "python"
    cmd = [py_exec, GEN_SCRIPT]
    try:
        res = subprocess.run(
            cmd,
            cwd=SIR_ROOT,
            capture_output=True,
            text=True,
            timeout=120,
            creationflags=CREATE_NO_WINDOW,
        )
    except Exception as e:
        log(f"ERROR: Failed to run {GEN_SCRIPT}: {e}")
        record_refresh(False, str(e)[:500])
        return 1

    if res.returncode != 0:
        log(f"ERROR: generate_dashboard.py failed (exit {res.returncode}):")
        if res.stderr:
            log(res.stderr.strip()[:1000])
        record_refresh(False, (res.stderr or res.stdout or "generator failed")[:500])
        return res.returncode

    if res.stdout:
        log(res.stdout.strip()[:1000])

    changed_hash = ""
    if os.path.exists(CHANGED_FILE):
        try:
            with open(CHANGED_FILE, "r", encoding="utf-8") as f:
                changed_hash = f.read().strip()
        except Exception:
            pass
    published_hash = ""
    if os.path.exists(PUBLISHED_FILE):
        try:
            with open(PUBLISHED_FILE, "r", encoding="utf-8") as f:
                published_hash = f.read().strip()
        except Exception:
            pass
    if changed_hash and published_hash and changed_hash == published_hash:
        status_msg = f"Artifact IN SYNC (hash {changed_hash})"
    else:
        status_msg = f"Artifact OUT OF SYNC: changed={changed_hash or 'none'} vs published={published_hash or 'none'}"
    log(f"Refresh complete. {status_msg}")
    record_refresh(True, None)
    return 0


if __name__ == "__main__":
    sys.exit(refresh())
