"""Deploys the SIR Control Room page to a free Cloudflare Pages mirror, so the owner always has a live URL
that updates itself without any Claude session (r62, 2026-11-12).

Flow: skip in game mode -> make sure ops/artifact/control-room.html is fresh (runs plans/generate_dashboard.py
when the file is missing or older than STALE_SECONDS) -> privacy and secret gate -> skip when the content hash
was already deployed -> write a temp deploy folder (index.html + noindex meta + robots.txt disallow all) ->
`npx wrangler pages deploy` with credentials read from _local/api-keys.env (process env only, never written
to disk or printed). Log: ops/artifact/publish-pages.log. Deployed hash: ops/artifact/PAGES_PUBLISHED.txt.

Scheduled as SIR_HQ_Publish (every 30 minutes, pythonw, hidden, BelowNormal priority).
"""
import ctypes
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import nowindow  # noqa: F401  (hidden console windows for child processes)

ROOT = Path("D:/Projects/_SIR")
sys.path.insert(0, str(ROOT / "plans"))
sys.path.insert(0, str(ROOT / "scripts"))
from dashboard_privacy import assert_no_private_leaks  # noqa: E402

HTML = ROOT / "ops" / "artifact" / "control-room.html"
STATE = ROOT / "ops" / "artifact" / "PAGES_PUBLISHED.txt"
LOG = ROOT / "ops" / "artifact" / "publish-pages.log"
KEYS_ENV = ROOT / "_local" / "api-keys.env"
GENERATOR = ROOT / "plans" / "generate_dashboard.py"
GAME = Path("D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json")
PAGES_PROJECT = "sir-control-room-0dce50"
PAGES_URL = f"https://{PAGES_PROJECT}.pages.dev/"
STALE_SECONDS = 40 * 60
NOINDEX = '<meta name="robots" content="noindex,nofollow">'

# Values that must never appear in a public deploy: every secret key name in api-keys.env plus common token shapes.
SECRET_VALUE_RES = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\b(xox[baprs]-|sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|glpat-[A-Za-z0-9_-]{15,})"),
    re.compile(r"\b\d{6,12}:[A-Za-z0-9_-]{30,}\b"),  # Telegram bot token shape
]


def log(msg: str) -> None:
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")


def below_normal_priority() -> None:
    if os.name == "nt":
        try:
            BELOW_NORMAL_PRIORITY_CLASS = 0x00004000
            ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), BELOW_NORMAL_PRIORITY_CLASS)
        except Exception:
            pass


def load_keys() -> dict:
    """KEY=VALUE pairs from _local/api-keys.env. Values stay in memory only."""
    keys = {}
    for line in KEYS_ENV.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            keys[k.strip()] = v.strip().strip('"').strip("'")
    return keys


def ensure_fresh() -> bool:
    """Regenerate the artifact when it is missing or older than STALE_SECONDS. Returns False on failure."""
    if HTML.exists() and (time.time() - HTML.stat().st_mtime) < STALE_SECONDS:
        return True
    gen = subprocess.run([sys.executable, str(GENERATOR)], capture_output=True, text=True, timeout=300)
    if gen.returncode != 0 or not HTML.exists():
        log(f"generate failed: rc={gen.returncode} {(gen.stderr or '')[-200:]}")
        return False
    log(f"regenerated: {(gen.stdout or '').strip()[-120:]}")
    return True


def privacy_gate(html: str) -> None:
    """Raise ValueError when the page carries private strings, secret key names or token-shaped values."""
    assert_no_private_leaks(html)
    low = html.lower()
    for name in load_keys():
        if name.endswith("_TOKEN") or name.endswith("_SECRET") or name.endswith("_KEY") or name.endswith("_ID"):
            if name.lower() in low:
                raise ValueError(f"secret key name '{name}' found in dashboard html")
    for rx in SECRET_VALUE_RES:
        if rx.search(html):
            raise ValueError(f"secret-shaped value found in dashboard html ({rx.pattern[:40]})")


def wrangler_env() -> dict:
    keys = load_keys()
    token = keys.get("CLOUDFLARE_FULL_TOKEN") or keys.get("CLOUDFLARE_API_TOKEN")
    account = keys.get("CLOUDFLARE_ACCOUNT_ID")
    if not token or not account:
        raise RuntimeError("CLOUDFLARE_FULL_TOKEN or CLOUDFLARE_ACCOUNT_ID missing in _local/api-keys.env")
    env = dict(os.environ)
    env["CLOUDFLARE_API_TOKEN"] = token
    env["CLOUDFLARE_ACCOUNT_ID"] = account
    return env


def deploy_dir(html: str) -> str:
    """Temp folder with index.html (noindex injected) and a disallow-all robots.txt."""
    d = Path(tempfile.mkdtemp(prefix="sir_pages_"))
    head = html
    if "</head>" in head:
        head = head.replace("</head>", NOINDEX + "\n</head>", 1)
    else:
        head = NOINDEX + "\n" + head
    (d / "index.html").write_text(head, encoding="utf-8", newline="\n")
    (d / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8", newline="\n")
    return str(d)


def main() -> int:
    below_normal_priority()
    if GAME.exists():
        log("skip: game mode")
        return 0
    if not ensure_fresh():
        return 1
    html = HTML.read_text(encoding="utf-8")
    digest = hashlib.sha256(html.encode("utf-8")).hexdigest()[:8]
    last = STATE.read_text(encoding="utf-8").strip() if STATE.exists() else ""
    if digest == last:
        log(f"skip: unchanged {digest}")
        return 0
    try:
        privacy_gate(html)
    except ValueError as e:
        log(f"REFUSED deploy {digest}: {e}")
        return 1
    folder = deploy_dir(html)
    try:
        npx = shutil.which("npx.cmd") or shutil.which("npx") or "npx.cmd"
        cmd = [npx, "--yes", "wrangler", "pages", "deploy", folder,
               "--project-name", PAGES_PROJECT, "--branch", "main"]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=600,
                             env=wrangler_env(), stdin=subprocess.DEVNULL)
        tail = ((res.stdout or "") + (res.stderr or "")).strip().splitlines()[-3:]
        if res.returncode != 0:
            log(f"FAILED {digest}: rc={res.returncode} {' | '.join(tail)[:300]}")
            return 1
        log(f"deployed {digest} -> {PAGES_URL} ({' | '.join(tail)[:200]})")
        STATE.write_text(digest + "\n", encoding="utf-8")
        return 0
    finally:
        shutil.rmtree(folder, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
