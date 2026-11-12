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
import subprocess
import sys
import time
from datetime import date
from status_rules import state_for
from dashboard_privacy import assert_no_private_leaks

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from products import PRODUCTS  # noqa: E402
from kit_platforms import PLATFORM_NAMES  # noqa: E402

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



def load_checklist():
    p = os.path.join(OPS, "checklist.json")
    if not os.path.isfile(p):
        return {"items": [], "metrics": {"ready": 0, "total": 0}}
    try:
        items = json.load(io.open(p, encoding="utf-8")) or []
    except Exception:
        items = []
    today = datetime.date.today()
    out = []
    ready = 0
    for it in items:
        checked = it.get("checked")
        age_days = None
        status = it.get("status", "unknown")
        stale = False
        try:
            if checked:
                d = datetime.date.fromisoformat(str(checked))
                age_days = (today - d).days
                if age_days > 3 and status not in ("action_needed", "in_progress"):
                    status = "unknown"
                    stale = True
        except Exception:
            stale = True
        if status == "ready":
            ready += 1
        row = dict(it)
        row["status"] = status
        row["age_days"] = age_days
        row["stale"] = stale
        out.append(row)
    return {"items": out, "metrics": {"ready": ready, "total": len(out)}}



def load_active():
    p = os.path.join(OPS, "active.json")
    meta = {"items": [], "mtime": None, "age_hours": None, "stale": False}
    try:
        st = os.stat(p)
        mtime = datetime.datetime.fromtimestamp(st.st_mtime)
        age_h = (datetime.datetime.now() - mtime).total_seconds() / 3600.0
        meta["mtime"] = mtime.isoformat(timespec="seconds")
        meta["age_hours"] = round(age_h, 1)
        meta["stale"] = age_h > 6
        meta["items"] = json.load(io.open(p, encoding="utf-8")) or []
    except Exception:
        pass
    return meta



def load_models():
    models_file = os.path.join(OPS, "MODELS.json")
    if os.path.exists(models_file):
        try:
            return json.load(io.open(models_file, encoding="utf-8"))
        except Exception:
            pass
    return {
        "manager": {"name": "Claude Sonnet 5.5", "role_en": "Claude Sonnet 5.5 High (Manager & Reviewer)", "role_ar": "كلود سونيت 5.5 هاي (المدير والمراجع)"},
        "workers": {"name": "Gemini 3.8 Flash High", "role_en": "Gemini 3.8 Flash High (Autonomous Workers)", "role_ar": "جيميني 3.8 فلاش هاي (الوكلاء المنفذون المستقلون)"},
    }


def load_models_info():
    p = os.path.join(OPS, "MODELS.json")
    info = {"data": load_models(), "source": "ops/MODELS.json", "checked": None, "age_days": None, "stale": False}
    try:
        data = json.load(io.open(p, encoding="utf-8"))
        info["data"] = data
        checked = data.get("checked")
        if checked:
            info["checked"] = str(checked)
            d = datetime.date.fromisoformat(str(checked))
            age = (datetime.date.today() - d).days
            info["age_days"] = age
            info["stale"] = age > 1
    except Exception:
        pass
    return info


def extract_tasks_from_markdown(file_path, limit=10):
    """Robustly extracts up to limit tasks from any MASTER_PLAN.md, *-DEEP.md, or TASKS.md file."""
    tasks = []
    if not os.path.isfile(file_path):
        return tasks
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            file_lines = f.readlines()
        in_tasks = False
        for line in file_lines:
            line_str = line.strip()
            # Recognize section headers like:
            # ## 6. The Next 25 Prioritized Tasks
            # ## 5. The First 25 Prioritized Tasks
            # ## 4. Prioritized Engineering Backlog (First 25 Tasks)
            # ## Next 10 Tasks
            # ## Current Sprint
            if line_str.startswith("## ") and re.search(r"(?:Tasks|Backlog|Sprint|Blueprint)", line_str, re.I):
                in_tasks = True
                continue
            if in_tasks and line_str.startswith("## ") and not re.search(r"(?:Tasks|Backlog|Sprint|Blueprint)", line_str, re.I):
                break
            if in_tasks:
                # 1. Table row: | **01** | Task Title | ...
                m_tbl = re.match(r"^\|\s*\*{0,2}\d+\*{0,2}\s*\|\s*([^|]+?)\s*\|", line_str)
                # 2. H3 heading: ### CR-101 | ... or ### Task 1: ...
                m_h3 = re.match(r"^###\s*(?:Task\s*\d+:|[A-Z0-9]+-\d+\s*\||\d+\.)\s*(.*)", line_str)
                # 3. Numbered list: 1. ...
                m_num = re.match(r"^\d+\.\s*(.*)", line_str)
                # 4. Checkbox item: - [ ] ...
                m_chk = re.match(r"^-\s*\[\s*\]\s*(.*)", line_str)

                clean_t = None
                if m_tbl and not m_tbl.group(1).startswith("---") and "Task Title" not in m_tbl.group(1):
                    clean_t = m_tbl.group(1)
                elif m_h3:
                    clean_t = m_h3.group(1)
                elif m_num:
                    clean_t = m_num.group(1)
                elif m_chk:
                    clean_t = m_chk.group(1)

                if clean_t:
                    clean_t = re.sub(r"\|\s*owner:\s*[^|]+\|", "", clean_t)
                    clean_t = re.sub(r"[*_`]", "", clean_t).strip()
                    if clean_t and not clean_t.startswith("---") and clean_t not in tasks:
                        tasks.append(clean_t[:120])
                        if len(tasks) >= limit:
                            break
    except Exception:
        pass
    return tasks


def get_control_room_daemon_health():
    health_file = os.path.join(OPS, "control-room-health.json")
    if os.path.exists(health_file):
        try:
            with open(health_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "service": "SIR Control Room",
        "task_name": "SIR_ControlRoom_Server",
        "port": 8899,
        "status": "unknown",
        "mode": "detached_daemon",
    }



