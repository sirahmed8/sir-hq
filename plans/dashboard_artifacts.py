"""Dashboard generator modules split from dashboard_main.py (R19-M3).
Run: python D:/Projects/_SIR/plans/generate_dashboard.py, then HQ republishes the artifact.
AHome is private: counts and status only, never task text or notes.
Git hash, published-hash and HQ bus notification helpers."""
"""Git hash, published-hash, HQ bus notification and final publish helpers."""
import datetime
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dashboard_privacy import assert_no_private_leaks  # noqa: E402

ROOT = os.environ.get("SIR_ROOT", "D:/Projects")
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
ORDER = json.load(io.open(os.path.join(HERE, "order.json"), encoding="utf-8"))
WAVEMAP = json.load(io.open(os.path.join(HERE, "waves.json"), encoding="utf-8"))
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0


def get_git_short_hash():
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=os.path.normpath(os.path.join(HERE, "..")),
            capture_output=True,
            text=True,
            timeout=5,
            creationflags=CREATE_NO_WINDOW,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except Exception:
        pass
    return "main"



def get_published_hash():
    pub_file = os.path.join(OPS, "artifact", "PUBLISHED.txt")
    if os.path.exists(pub_file):
        try:
            with open(pub_file, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            pass
    return ""



def notify_hq_artifact_outdated(content_hash):
    hq_bus = os.path.join(OPS, "bus", "sir-hq.md")
    if not os.path.exists(hq_bus):
        return
    lock_path = os.path.join(OPS, "locks", "sir-hq-bus.lock")
    os.makedirs(os.path.dirname(lock_path), exist_ok=True)
    try:
        if os.path.isfile(lock_path):
            try:
                with open(lock_path, "r", encoding="utf-8") as f:
                    if f.read().strip() == content_hash:
                        return
            except Exception:
                pass
        with open(hq_bus, "r", encoding="utf-8") as f:
            content = f.read()
        target_msg = f"artifact outdated: republish ops/artifact/control-room.html (hash {content_hash})"
        if target_msg in content:
            with open(lock_path, "w", encoding="utf-8") as f:
                f.write(content_hash)
            return
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        notice = f"- [ ] {today} from control-room-daemon:\n  notice: {target_msg}\n"
        with open(hq_bus, "a", encoding="utf-8", newline="\n") as f:
            f.write("\n" + notice)
        with open(lock_path, "w", encoding="utf-8") as f:
            f.write(content_hash)
    except Exception as e:
        print(f"Warning: could not notify HQ: {e}")


def publish_dashboard(data, content_hash, git_hash):
    tpl = "".join(
        io.open(os.path.join(HERE, name), encoding="utf-8").read()
        for name in (
            "dashboard_template_head.html",
            "dashboard_template_css.html",
            "dashboard_template_css2.html",
            "dashboard_template_css3.html",
            "dashboard_template_css4.html",
            "dashboard_template_css5.html",
            "dashboard_template_body.html",
            "dashboard_template_body2.html",
            "dashboard_template_js.html",
            "dashboard_template_js2.html",
            "dashboard_template_js3.html",
            "dashboard_template_js4.html",
            "dashboard_template_js5.html",
            "dashboard_template_js6.html",
            "dashboard_template_js7.html",
        )
    )
    out = tpl.replace("/*__DATA__*/{}", json.dumps(data, ensure_ascii=False))
    assert_no_private_leaks(out)

    # Assertive check: Generator fails if any outdated model name appears in generated output
    forbidden_models = [
        "Sonnet 3.5",
        "Sonnet 3.7",
        "Sonnet 4.",
        "Gemini 2.5",
        "Gemini 2.0",
        "Gemini 3.0",
        "Opus 4.",
        "claude-3-5",
        "claude-3-7",
        "gemini-2.5",
        "gemini-2.0",
    ]
    for fm in forbidden_models:
        if fm.lower() in out.lower():
            raise ValueError(f"CRITICAL: Outdated model string '{fm}' detected in generated dashboard HTML!")

    # Assertive check: Generator fails if any private repo name or Habiba appears in generated output
    privacy_leaks = [
        "ahmed-and-habiba",
        "habiba",
    ]
    for pl in privacy_leaks:
        if pl in out.lower():
            raise ValueError(f"CRITICAL PRIVACY VIOLATION: Forbidden private string '{pl}' detected in generated dashboard/artifact HTML!")

    # Write public site (served) and artifact copy
    public_dir = os.path.join(OPS, "public")
    os.makedirs(public_dir, exist_ok=True)
    os.makedirs(os.path.join(OPS, "artifact"), exist_ok=True)
    site_path = os.path.join(public_dir, "dashboard.html")
    artifact_path = os.path.join(OPS, "artifact", "control-room.html")
    changed_path = os.path.join(OPS, "artifact", "CHANGED.txt")

    io.open(site_path, "w", encoding="utf-8", newline="\n").write(out)
    io.open(artifact_path, "w", encoding="utf-8", newline="\n").write(out)
    io.open(changed_path, "w", encoding="utf-8", newline="\n").write(content_hash + "\n")
    # copy static assets to public if they exist in ops
    for asset in ("favicon.ico", "favicon.svg", "manifest.json"):
        src = os.path.join(OPS, asset)
        if os.path.isfile(src):
            try:
                with open(src, "rb") as fsrc, open(os.path.join(public_dir, asset), "wb") as fdst:
                    fdst.write(fsrc.read())
            except Exception:
                pass
    # write public health placeholder only if missing; server manages live health
    health_pub = os.path.join(public_dir, "health.json")
    if not os.path.exists(health_pub):
        try:
            io.open(health_pub, "w", encoding="utf-8").write("{}")
        except Exception:
            pass

    if not data["artifact_synced"]:
        notify_hq_artifact_outdated(content_hash)

    print(f"dashboard.html & control-room.html generated ({len(out)} bytes, hash {content_hash}, git {git_hash}, synced={data['artifact_synced']})")
