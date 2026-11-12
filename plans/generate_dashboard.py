"""Builds ops/artifact/control-room.html: the SIR Control Room (Claude artifact and local site share this one file).
Run: python D:/Projects/_SIR/plans/generate_dashboard.py  (scheduled as SIR_HQ_Dashboard every 30 minutes, pythonw).
Read-only sources only. AHome: counts, dates and CI state, never its files or text.
Truth rules: a task is 'done by worker' until a verification PASS exists; workers = live runner processes."""
import datetime
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.normpath(os.path.join(HERE, "..", "scripts"))
sys.path.insert(0, HERE)
sys.path.insert(0, SCRIPTS)
import nowindow  # noqa: E402,F401  (no console windows for child processes)
import dashboard_feeds as feeds  # noqa: E402
import dashboard_repos as repos  # noqa: E402
import dashboard_notes as notes  # noqa: E402

OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
TEMPLATE = os.path.join(HERE, "dashboard_template.html")
OUT = os.path.join(OPS, "artifact", "control-room.html")
GAME_SNAP = os.path.normpath(os.path.join(HERE, "..", "..", "SIR Laptop Manager", ".sir", "game_mode_snapshot.json"))
PLACEHOLDER = "/*__DATA__*/{}"


def build_payload():
    now = time.time()
    return {
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "generated_epoch": int(now),
        "team": feeds.runners(),
        "queue": feeds.queue_open(),
        "pool": feeds.pool(),
        "rounds": feeds.rounds(),
        "projects": repos.projects(),
        "ci_banner": repos.quota_banner(),
        "notes": notes.collect(),
    }


def write_atomic(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def main():
    if os.path.exists(GAME_SNAP):
        print("game mode active: control room refresh paused")
        return 0
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    if PLACEHOLDER not in template:
        print("template has no data placeholder", file=sys.stderr)
        return 1
    payload = build_payload()
    data_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = template.replace(PLACEHOLDER, data_json, 1)
    write_atomic(OUT, html)
    digest = hashlib.sha256(html.encode("utf-8")).hexdigest()[:8]
    print(f"generated {OUT} ({len(html)} bytes, {digest}) at {payload['generated_at']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
