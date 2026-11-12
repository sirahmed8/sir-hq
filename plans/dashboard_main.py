"""Builds D:/Projects/_SIR/ops/dashboard.html (the SIR Control Room page) from the real project files.
Run: python D:/Projects/_SIR/plans/generate_dashboard.py, then HQ republishes the artifact (same file path).
AHome is private: counts and status only, never task text or notes.
Truth rule: Every project is being rebuilt from zero. A project is only 'verified' if verified end-to-end today."""
import datetime
import hashlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit_platforms import PLATFORM_NAMES  # noqa: E402
from dashboard_sources import attention, lines, parse_request_ledgers  # noqa: E402
from dashboard_autopilot import parse_account_ledger, parse_autopilot, parse_cli_workers  # noqa: E402
from dashboard_reports import (  # noqa: E402
    archived_count,
    get_ci_status,
    load_models,
    parse_suggestions,
    parse_verifications,
    translate_log_entry,
)
from dashboard_artifacts import (  # noqa: E402
    get_git_short_hash,
    get_published_hash,
    notify_hq_artifact_outdated,
    publish_dashboard,
)
from dashboard_projects import collect_projects  # noqa: E402
from dashboard_data import (  # noqa: E402
    get_control_room_daemon_health,
    load_active,
    load_checklist,
    load_models_info,
)
from dashboard_handover import parse_gemini_handover  # noqa: E402

ROOT = os.environ.get("SIR_ROOT", "D:/Projects")
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
ORDER = json.load(io.open(os.path.join(HERE, "order.json"), encoding="utf-8"))
WAVEMAP = json.load(io.open(os.path.join(HERE, "waves.json"), encoding="utf-8"))
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

SHORT = {
    "web": "Web",
    "pwa": "PWA",
    "windows": "Win",
    "macos": "Mac",
    "linux": "Linux",
    "android": "Andr",
    "ios": "iOS",
    "ipados": "iPad",
    "wearos": "Wear",
    "watchos": "Watch",
    "android_tv": "ATV",
    "tvos": "tvOS",
    "android_auto": "Auto",
    "carplay": "CarP",
    "widgets": "Widg",
    "browser_ext": "Ext",
    "docker": "Dock",
}

WAVE_NAMES = {
    1: "AHome first",
    2: "Automations",
    3: "Friend's project",
    4: "AI and content",
    5: "Earn the most",
    6: "Other paying products",
    7: "Extract and polish",
    8: "Optional, last",
}

WAVE_NAMES_AR = {
    1: "منظومة AHome أولاً (خاصة)",
    2: "الأتمتة والعمليات الأساسية",
    3: "مشروع الصديق (مجمّد)",
    4: "الذكاء الاصطناعي وصناعة المحتوى",
    5: "المنتجات التجارية الأعلى عائداً",
    6: "المنتجات والمنظومات الإضافية",
    7: "الاستخلاص والصقل النهائي",
    8: "إضافي، في النهاية",
}


def main():
    projects = collect_projects()

    # Honest portfolio truth counts
    n_verified = sum(1 for p in projects if p["status"] == "verified")
    n_rebuilding = sum(1 for p in projects if p["status"] == "rebuilding")
    n_backlog = sum(1 for p in projects if p["status"] == "backlog")
    n_frozen = sum(1 for p in projects if p["status"] == "frozen")

    by_slug = {p["slug"]: p for p in projects}

    waves = {}
    for pr in projects:
        w = waves.setdefault(
            pr["wave"],
            dict(
                wave=pr["wave"],
                name=WAVE_NAMES.get(pr["wave"], ""),
                name_ar=WAVE_NAMES_AR.get(pr["wave"], ""),
                verified=0,
                total=0,
                projects=[],
            ),
        )
        w["total"] += 1
        if pr["status"] == "verified":
            w["verified"] += 1
        w["projects"].append(pr["slug"])

    active_info = load_active()
    active = active_info.get("items", [])

    nxt = next(
        (pr for pr in projects if pr["status"] == "rebuilding"),
        None,
    )
    if not nxt:
        nxt = next(
            (pr for pr in projects if pr["status"] == "backlog"),
            None,
        )

    raw_logs = [
        ln[2:][:260] for ln in lines(OPS + "/MISSION_LOG.md") if ln.startswith("- 20")
    ][-14:]

    log_entries = []
    for l in reversed(raw_logs):
        if "ahome" in l.lower():
            continue
        clean_l = re.sub(r"ahmed-and-habiba", "AHome", l, flags=re.IGNORECASE)
        clean_l = re.sub(r"habiba", "AHome private data", clean_l, flags=re.IGNORECASE)
        log_entries.append({"en": clean_l, "ar": translate_log_entry(clean_l)})

    checklist_info = load_checklist()
    models_info = load_models_info()
    data = dict(
        generated=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        projects=projects,
        truth_metrics=dict(
            verified=n_verified,
            rebuilding=n_rebuilding,
            backlog=n_backlog,
            frozen=n_frozen,
            total=len(projects),
        ),
        waves=sorted(waves.values(), key=lambda w: w["wave"]),
        attention=attention(),
        active=active,
        active_info=active_info,
        nextStart=(nxt["name"] if nxt else ""),
        nextStart_ar=(nxt["name_ar"] if nxt else ""),
        log=log_entries,
        repos=dict(
            new_private=len([p for p in projects if p.get("matrix")]),
            archived=archived_count(),
        ),
        platforms=[dict(key=k, name=n, short=SHORT[k]) for k, n in PLATFORM_NAMES],
        request_ledgers=parse_request_ledgers(),
        ci=get_ci_status(),
        checklist=checklist_info,
        models_info=models_info,
        remote_access=(lambda cfg: [
            {
                "name": "SIR Study",
                "name_ar": "منصة المذاكرة",
                "port": 3300,
                "url": f"https://{cfg.get('tailnet_host','ahmed.tail9e9aa7.ts.net')}:3300/START_HERE.html",
                "ip_url": f"https://{cfg.get('tailnet_ip','100.85.112.10')}:3300/START_HERE.html",
                "desc_en": "Study hub",
                "desc_ar": "صفحة البداية",
            },
            {
                "name": "SIR Jobs",
                "name_ar": "منظومة فرص العمل",
                "port": 3456,
                "url": f"https://{cfg.get('tailnet_host','ahmed.tail9e9aa7.ts.net')}:3456/",
                "ip_url": f"https://{cfg.get('tailnet_ip','100.85.112.10')}:3456/",
                "desc_en": "Jobs review UI",
                "desc_ar": "واجهة مراجعة فرص العمل",
            },
            {
                "name": "SIR Control Room",
                "name_ar": "غرفة التحكم: المقر الرئيسي",
                "port": 8899,
                "url": f"https://{cfg.get('tailnet_host','ahmed.tail9e9aa7.ts.net')}:8899/dashboard.html",
                "ip_url": f"https://{cfg.get('tailnet_ip','100.85.112.10')}:8899/dashboard.html",
                "desc_en": "Portfolio ground truth",
                "desc_ar": "لوحة الحقيقة التشغيلية",
            },
            {
                "name": "SIR Laptop Manager",
                "name_ar": "مدير الحاسوب والأداء",
                "port": 8765,
                "url": f"https://{cfg.get('tailnet_host','ahmed.tail9e9aa7.ts.net')}:8765/",
                "ip_url": f"https://{cfg.get('tailnet_ip','100.85.112.10')}:8765/",
                "desc_en": "Ops UI",
                "desc_ar": "لوحة التشغيل",
            },
        ])(json.load(io.open(os.path.join(OPS, "config.json"), encoding="utf-8")) if os.path.isfile(os.path.join(OPS, "config.json")) else {}),
        daemon_health=get_control_room_daemon_health(),
        autopilot=(lambda ap: {**ap, "workers": parse_cli_workers()})(parse_autopilot()),
        account_ledger=parse_account_ledger(),
        verifications=parse_verifications(),
        suggestions=parse_suggestions(),
    )

    data["gemini_handover"] = parse_gemini_handover(projects)
    models = load_models()
    git_hash = get_git_short_hash()
    published_hash = get_published_hash()

    data["models"] = models
    data["git_hash"] = git_hash
    data["published_hash"] = (published_hash or "").split()[0] if isinstance(published_hash, str) else ""

    hash_seed_dict = {
        "projects": [{k: v for k, v in p.items() if k not in ("commit", "hash", "sync", "now", "next")} for p in data.get("projects", [])],
        "ci": data.get("ci"),
        "models": data.get("models_info", {}).get("data"),
        "checklist": [{k: v for k, v in i.items() if k not in ("age_days", "stale")} for i in data.get("checklist", {}).get("items", [])],
        "truth_metrics": data.get("truth_metrics"),
    }
    hash_seed = json.dumps(hash_seed_dict, sort_keys=True, ensure_ascii=False)
    content_hash = hashlib.sha256(hash_seed.encode("utf-8")).hexdigest()[:8]
    data["content_hash"] = content_hash
    data["published_hash"] = (published_hash or "").split()[0] if isinstance(published_hash, str) else ""
    data["artifact_synced"] = bool(data.get("published_hash") and data["published_hash"] == content_hash)

    publish_dashboard(data, content_hash, git_hash)


if __name__ == "__main__":
    main()
