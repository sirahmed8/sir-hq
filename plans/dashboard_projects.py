"""Project row collection for the SIR Control Room dashboard (split from dashboard_main.py, R19-M3).
AHome is private: counts and status only, never task text or notes."""
import datetime
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from status_rules import state_for  # noqa: E402
from products import PRODUCTS  # noqa: E402
from dashboard_sources import checkpoint_now, git, git_sync_status, lines, parse_tasks  # noqa: E402

ROOT = os.environ.get("SIR_ROOT", "D:/Projects")
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
ORDER = json.load(io.open(os.path.join(HERE, "order.json"), encoding="utf-8"))
WAVEMAP = json.load(io.open(os.path.join(HERE, "waves.json"), encoding="utf-8"))

def collect_projects():
    today = datetime.date.today().isoformat()
    projects = []
    for p in PRODUCTS:
        folder = ROOT + "/" + p["folder"]
        if not os.path.isfile(folder + "/.sir/TASKS.md"):
            continue
        private = p["slug"] == "ahome"
        try:
            st = json.load(io.open(folder + "/.sir/status.json", encoding="utf-8"))
        except Exception:
            st = {"platforms": {}}
        ms = parse_tasks(folder, private)
        items = [i for m in ms for i in m["items"]]
        done_count = sum(1 for i in items if i.get("done"))
        total_count = len(items)
        yml = "\n".join(lines(folder + "/.sir/project.yml"))
        arch = re.search(r"archetype: (.*)", yml)

        ev_state = state_for(folder, today)
        cp_path = os.path.join(folder, ".sir", "CHECKPOINT.md")
        cp_lines = [ln.strip() for ln in lines(cp_path) if ln.strip()]
        goal_text = ""
        next_text = ""
        for i, ln in enumerate(cp_lines):
            low = ln.lower()
            if low.startswith("## goal") and i + 1 < len(cp_lines):
                goal_text = cp_lines[i + 1][:200]
            if low.startswith("## next") and i + 1 < len(cp_lines):
                next_text = cp_lines[i + 1][:200]
        if ev_state == "verified":
            status = "verified"
            verified_today = True
            verified_date = today
        elif ev_state == "built_unverified":
            status = "built_unverified"
            verified_today = False
            verified_date = "Pending"
        else:
            status = "not_started"
            verified_today = False
            verified_date = "Pending"

        name_ar = p.get("name_ar") or p.get("display") or p["display"]
        if private:
            ms_out = []
            next_items = []
            now_text = ""
            mission = "Private. Counts only."
            mission_ar = "خاص. الأعداد والحالة فقط."
            folder_disp = "withheld"
            commit = ""
            ghash = ""
            sync = ""
            matrix = None
            arch_s = "private, details withheld"
            name = "AHome (private)"
            name_ar = "AHome (خاص ومحمي)"
        else:
            ms_out = [dict(name=m.get("name", "Tasks"), items=m.get("items", [])) for m in ms]
            next_items = [f"{i['id']} {i['text'][:150]}" for i in items if not i.get("done")][:4]
            now_text = checkpoint_now(folder)
            mission = p.get("mission", "")[:260]
            mission_ar = p.get("mission", "")[:260]
            folder_disp = "D:\\Projects\\" + p["folder"]
            commit = git(folder, "log", "-1", "--format=%cs")
            ghash = git(folder, "rev-parse", "--short", "HEAD")
            sync = git_sync_status(folder)
            matrix = st.get("platforms")
            arch_s = (arch.group(1) if arch else "")
            name = p["display"]

        truth = {
            "status": status,
            "verified_today": verified_today,
            "name_ar": name_ar,
            "exists_en": (goal_text or "State derived from checkpoint.").replace("habiba", "private data"),
            "exists_ar": "",
            "verified_en": "Evidence verified today." if verified_today else "No evidence file dated today.",
            "verified_ar": "",
            "missing_en": next_text or "See checkpoint next step.",
            "missing_ar": "",
            "mission_ar": mission_ar,
        }

        projects.append(dict(
            slug=p["slug"],
            name=name,
            name_ar=name_ar,
            wave=WAVEMAP.get(p["slug"], 9),
            order=ORDER.index(p["slug"]) if p["slug"] in ORDER else 99,
            color=BRAND.get(p["slug"], {}).get("color", "#64748B"),
            arch=arch_s,
            status=status,
            verified_today=verified_today,
            verified_date=verified_date,
            verified_by=("evidence file" if verified_today else "none"),
            verified_by_ar=("ملف دليل" if verified_today else "لا يوجد"),
            control_note_en="",
            control_note_ar="",
            truth=truth,
            done=done_count,
            total=total_count,
            milestones=ms_out,
            next=next_items,
            now=now_text,
            mission=mission,
            mission_ar=mission_ar,
            repo=("AHome (private repo)" if private else "github.com/sirahmed8/" + p["repo"] + " (private)"),
            folder=folder_disp,
            commit=commit,
            hash=ghash,
            sync=sync,
            required=sum(1 for v in st.get("platforms", {}).values() if v == "required"),
            matrix=matrix,
        ))

    projects.sort(key=lambda x: (x["wave"], x["order"]))
    return projects
