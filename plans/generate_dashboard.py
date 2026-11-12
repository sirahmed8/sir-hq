"""Builds the SIR Control Room page and keeps every copy of it truthful.

One page, one build, four truthful outputs (all written atomically, all byte-identical):
  ops/artifact/control-room.html  the artifact the owner reads
  ops/dashboard.html               the historical page path
  ops/public/dashboard.html        the page the local server serves at /dashboard.html
  ops/artifact/CHANGED.txt         the content hash of the artifact (compare with PUBLISHED.txt)

Run: python D:/Projects/_SIR/plans/generate_dashboard.py  (scheduled as SIR_HQ_Dashboard every 30 minutes, pythonw).
Read-only sources only. AHome: counts, dates and CI state, never its files or text.
Truth rules: a task is 'done by worker' until a verification PASS exists; workers = live runner processes.
"""
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
import dashboard_page as page  # noqa: E402
from dashboard_privacy import assert_no_private_leaks  # noqa: E402

OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
OUT = os.path.join(OPS, "artifact", "control-room.html")
MIRRORS = (os.path.join(OPS, "dashboard.html"), os.path.join(OPS, "public", "dashboard.html"))
CHANGED = os.path.join(OPS, "artifact", "CHANGED.txt")
GAME_SNAP = os.path.normpath(os.path.join(HERE, "..", "..", "SIR Laptop Manager", ".sir", "game_mode_snapshot.json"))


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


def render(payload):
    """Return the page HTML for a payload: the template with the data block injected."""
    template = page.assemble()
    if page.PLACEHOLDER not in template:
        raise RuntimeError("template has no data placeholder")
    data_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return template.replace(page.PLACEHOLDER, data_json, 1)


def write_atomic(path, text):
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def publish(html):
    """Write the page and its mirrors, then record the content hash. Returns the hash."""
    assert_no_private_leaks(html)
    digest = hashlib.sha256(html.encode("utf-8")).hexdigest()[:8]
    for path in (OUT,) + MIRRORS:
        write_atomic(path, html)
    write_atomic(CHANGED, digest + "\n")
    return digest


def main():
    if os.path.exists(GAME_SNAP):
        print("game mode active: control room refresh paused")
        return 0
    payload = build_payload()
    html = render(payload)
    digest = publish(html)
    if page.write_mirror():
        print("template mirror updated from parts")
    print(f"generated {OUT} ({len(html.encode('utf-8'))} bytes, {digest}) at {payload['generated_at']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
