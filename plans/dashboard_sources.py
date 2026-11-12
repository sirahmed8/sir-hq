"""Dashboard generator modules split from dashboard_main.py (R19-M3).
Run: python D:/Projects/_SIR/plans/generate_dashboard.py, then HQ republishes the artifact.
AHome is private: counts and status only, never task text or notes.
File and git readers plus markdown section parsers."""
import io
import json
import os
import sys
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

ROOT = os.environ.get("SIR_ROOT", "D:/Projects")
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
ORDER = json.load(io.open(os.path.join(HERE, "order.json"), encoding="utf-8"))
WAVEMAP = json.load(io.open(os.path.join(HERE, "waves.json"), encoding="utf-8"))
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0


def lines(path):
    try:
        return io.open(path, encoding="utf-8").read().splitlines()
    except OSError:
        return []



def clean(s):
    return re.sub(r"\*\*|`", "", s).strip()



def git(folder, *args):
    try:
        return subprocess.run(
            ["git", "-C", folder] + list(args),
            capture_output=True,
            text=True,
            timeout=20,
            creationflags=CREATE_NO_WINDOW,
        ).stdout.strip()
    except Exception:
        return ""



def git_sync_status(folder):
    try:
        sb = git(folder, "status", "-sb")
        if sb == "" and not os.path.isdir(os.path.join(folder, ".git")):
            return "unknown"
        rows = [l for l in sb.splitlines() if l.strip()]
        if not rows:
            return "in sync"
        first = rows[0]
        dirty = len(rows) - 1
        is_ahead = "ahead" in first
        is_behind = "behind" in first
        if is_ahead and is_behind:
            branch_st = "diverged"
        elif is_ahead:
            branch_st = "ahead"
        elif is_behind:
            branch_st = "behind"
        else:
            branch_st = "in sync"
        if branch_st == "in sync":
            return "in sync" if dirty == 0 else f"dirty ({dirty})"
        return f"{branch_st}" if dirty == 0 else f"{branch_st} & dirty ({dirty})"
    except Exception:
        return "unknown"



def parse_tasks(folder, private):
    path = os.path.join(folder, ".sir", "TASKS.md")
    items = []
    try:
        with io.open(path, encoding="utf-8", errors="ignore") as f:
            for ln in f:
                m = re.match(r"^\s*- \[([ xX])\]\s+(.+)$", ln.rstrip("\n"))
                if not m:
                    continue
                raw = m.group(2).strip()
                m2 = re.match(r"((?:T|L)-[A-Za-z0-9_-]+)\s*(?:\|\s*owner:[^|]+\s*)?\|\s*(.*)", raw)
                if m2:
                    tid = m2.group(1)
                    ttext = re.sub(r"\s*\| depends:.*", "", m2.group(2)).replace("(kit) ", "")
                else:
                    tid = raw[:40]
                    ttext = raw
                ttext = re.sub(r"habiba", "private data", ttext, flags=re.I)
                ttext = re.sub(r"ahmed-and-habiba", "ahome", ttext, flags=re.I)
                items.append({"id": tid, "done": m.group(1).lower() == "x", "text": "" if private else ttext[:240]})
    except Exception:
        pass
    return [dict(name="Tasks", items=items)] if items or os.path.isfile(path) else []



def checkpoint_now(folder):
    out, on = [], False
    for ln in lines(os.path.join(folder, ".sir", "CHECKPOINT.md")):
        if ln.startswith("## Now"):
            on = True
            continue
        if on and ln.startswith("## "):
            break
        if on and ln.strip():
            cln = clean(ln.lstrip("- "))
            cln = re.sub(r"habiba", "private data", cln, flags=re.IGNORECASE)
            cln = re.sub(r"ahmed-and-habiba", "ahome", cln, flags=re.IGNORECASE)
            out.append(cln)
    return " ".join(out)[:420]



def section_items(path, wanted):
    out, on = [], False
    for ln in lines(path):
        if ln.startswith("## "):
            on = any(ln.startswith("## " + w) for w in wanted)
            continue
        if on and ln.startswith("- [ ]"):
            out.append(clean(ln[5:])[:320])
    return out



def attention():
    out = []
    for x in section_items(OPS + "/OWNER_ACTIONS.md", ["Open"]):
        out.append(
            dict(
                level="warn",
                tag_en="Needs you now",
                tag_ar="يتطلب تدخلك الآن",
                text_en=x,
                text_ar=x,
            )
        )
    for x in section_items(OPS + "/AGENT_QUEUE.md", ["Now"]):
        out.append(
            dict(
                level="info",
                tag_en="Agents are on it",
                tag_ar="الوكلاء يعملون عليه",
                text_en=x,
                text_ar=x,
            )
        )
    for x in section_items(OPS + "/OWNER_ACTIONS.md", ["Optional"]):
        out.append(
            dict(
                level="mute",
                tag_en="When you like",
                tag_ar="في أي وقت يناسبك",
                text_en=x,
                text_ar=x,
            )
        )
    unread = sum(1 for ln in lines(OPS + "/bus/sir-hq.md") if ln.startswith("- [ ]"))
    if unread:
        out.append(
            dict(
                level="info",
                tag_en="Reports for HQ",
                tag_ar="تقارير بانتظار المقر",
                text_en=f"{unread} project report(s) waiting for HQ review in ops/bus/sir-hq.md.",
                text_ar=f"{unread} تقرير بانتظار مراجعة المقر في ops/bus/sir-hq.md.",
            )
        )
    return out



def parse_request_ledgers():
    req_dir = os.path.join(OPS, "requests")
    ledgers = []
    if not os.path.isdir(req_dir):
        return ledgers
    names = {
        "ahome": ("AHome (Private)", "منظومة AHome (خاصة)"),
        "control": ("SIR Control Room", "غرفة التحكم - المقر"),
        "jobs": ("SIR Jobs", "منظومة فرص العمل"),
        "laptop": ("SIR Laptop Manager", "مدير الحاسوب والأداء"),
        "study": ("SIR Study", "منصة المذاكرة الذكية"),
    }
    for fname in sorted(os.listdir(req_dir)):
        if not fname.endswith(".md"):
            continue
        slug = fname[:-3]
        fpath = os.path.join(req_dir, fname)
        text = io.open(fpath, encoding="utf-8").read()
        open_items = len(re.findall(r"^\d+\.\s*\[\s* \s*\]", text, re.M))
        in_progress = len(re.findall(r"^\d+\.\s*\[\s*~\s*\]", text, re.M))
        done = len(re.findall(r"^\d+\.\s*\[\s*x\s*\]", text, re.M))
        blocked = len(re.findall(r"^\d+\.\s*\[\s*!\s*\]", text, re.M))
        total = open_items + in_progress + done + blocked
        en_name, ar_name = names.get(slug, (slug.upper(), slug))
        ledgers.append({
            "slug": slug,
            "name_en": en_name,
            "name_ar": ar_name,
            "open": open_items + in_progress,
            "done": done,
            "blocked": blocked,
            "total": total,
        })
    return ledgers



def tail_lines(path, n=12):
    try:
        with io.open(path, encoding="utf8") as f:
            return f.read().splitlines()[-n:]
    except OSError:
        return []

def extract_tasks_from_markdown(file_path, limit=10):
    """Robustly extracts up to limit tasks from any MASTER_PLAN.md, *-DEEP.md, or TASKS.md file."""
    tasks = []
    if not os.path.isfile(file_path):
        return tasks
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        in_tasks = False
        for line in lines:
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
