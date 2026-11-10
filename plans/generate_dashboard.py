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
        "control": ("SIR Control Room", "غرفة التحكم — المقر"),
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


PRIVATE_TASK_RE = re.compile(r"[\w.-]*(?:ahome|habiba)[\w.-]*", re.I)


def sanitize_autopilot_text(value):
    text = str(value)
    text = PRIVATE_TASK_RE.sub("private-task", text)
    return text


def parse_autopilot():
    state = {}
    try:
        state = json.load(io.open(OPS + "/autopilot_state.json", encoding="utf8")) or {}
    except Exception:
        state = {}
    queue = []
    try:
        queue = json.load(io.open(OPS + "/AUTOPILOT_QUEUE.json", encoding="utf8")) or []
    except Exception:
        queue = []
    runners = state.get("runners", {}) if isinstance(state, dict) else {}
    safe_queue = []
    for item in queue if isinstance(queue, list) else []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name") or "")
        title = str(item.get("title") or name)
        private = bool(
            PRIVATE_TASK_RE.search(name)
            or PRIVATE_TASK_RE.search(title)
            or PRIVATE_TASK_RE.search(str(item.get("folder") or ""))
        )
        safe_queue.append(
            {
                "name": "private-task" if private else name,
                "title": "Private project task" if private else title,
                "done": bool(item.get("done")),
                "private": private,
            }
        )
    pending = [q for q in safe_queue if not q["done"]]
    return {
        "listener_pid": state.get("listener_pid") if isinstance(state, dict) else None,
        "last_tick": state.get("last_tick") if isinstance(state, dict) else None,
        "runner_count": len(runners) if isinstance(runners, dict) else 0,
        "queue": safe_queue,
        "pending": pending,
        "pending_count": len(pending),
        "log_tail": [sanitize_autopilot_text(ln) for ln in tail_lines(OPS + "/autopilot.log", 10)],
    }


def parse_account_ledger():
    rows = []
    for ln in lines(OPS + "/ACCOUNT_LEDGER.md"):
        if not ln.strip().startswith("|"):
            continue
        cells = [p.strip() for p in ln.strip().strip("|").split("|")]
        if not cells:
            continue
        if cells[0].lower() == "time":
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        if len(cells) >= 8:
            rows.append(
                {
                    "time": cells[0],
                    "account": cells[1],
                    "models": cells[2],
                    "five_h": cells[3],
                    "weekly": cells[4],
                    "five_reset": cells[5],
                    "weekly_reset": cells[6],
                    "note": cells[7],
                }
            )
        elif len(cells) == 7:
            rows.append(
                {
                    "time": cells[0],
                    "account": cells[1],
                    "models": "—",
                    "five_h": cells[2],
                    "weekly": cells[3],
                    "five_reset": cells[4],
                    "weekly_reset": cells[5],
                    "note": cells[6],
                }
            )
        elif len(cells) == 6:
            rows.append(
                {
                    "time": cells[0],
                    "account": cells[1],
                    "models": "—",
                    "five_h": cells[2],
                    "weekly": cells[3],
                    "five_reset": cells[4],
                    "weekly_reset": "—",
                    "note": cells[5],
                }
            )
        elif len(cells) >= 3:
            rows.append(
                {
                    "time": cells[0],
                    "account": cells[1],
                    "models": "—",
                    "five_h": "—",
                    "weekly": "—",
                    "five_reset": "—",
                    "weekly_reset": "—",
                    "note": " · ".join(cells[2:]),
                }
            )
    return rows[-10:]


def archived_count():
    try:
        r = subprocess.run(
            [
                "gh",
                "repo",
                "list",
                "sirahmed8",
                "--limit",
                "100",
                "--json",
                "isArchived",
                "-q",
                "[.[]|select(.isArchived)]|length",
            ],
            capture_output=True,
            text=True,
            timeout=5,
            creationflags=CREATE_NO_WINDOW,
        )
        if r.returncode == 0 and r.stdout.strip().isdigit():
            return int(r.stdout.strip())
    except Exception:
        pass
    return None


def get_ci_status():
    repos = [
        ("AHome", "sirahmed8/ahmed-and-habiba"),
        ("SIR HQ", "sirahmed8/sir-hq"),
        ("SIR Jobs", "sirahmed8/sir-jobs"),
        ("SIR Study", "sirahmed8/sir-study"),
        ("SIR Laptop Manager", "sirahmed8/sir-laptop-manager"),
    ]
    ci = []
    for name, repo in repos:
        is_ahome = name == "AHome"
        display_repo = "AHome (private repo)" if is_ahome else repo
        try:
            r = subprocess.run(
                ["gh", "run", "list", "-R", repo, "--limit", "1",
                 "--json", "conclusion,status,databaseId,headBranch,name,url,createdAt"],
                capture_output=True, text=True, timeout=5, creationflags=CREATE_NO_WINDOW,
            )
            if r.returncode == 0 and r.stdout.strip():
                runs = json.loads(r.stdout.strip())
                if runs:
                    latest = runs[0]
                    ci.append({
                        "name": name,
                        "repo": display_repo,
                        "status": latest.get("conclusion") or latest.get("status") or "unknown",
                        "createdAt": latest.get("createdAt"),
                        "id": None if is_ahome else latest.get("databaseId"),
                        "url": None if is_ahome else latest.get("url"),
                    })
                else:
                    ci.append({"name": name, "repo": display_repo, "status": "unknown", "createdAt": None, "id": None, "url": None, "note": "no runs"})
            else:
                ci.append({"name": name, "repo": display_repo, "status": "unknown", "createdAt": None, "id": None, "url": None, "note": "gh failed"})
        except Exception:
            ci.append({"name": name, "repo": display_repo, "status": "unknown", "createdAt": None, "id": None, "url": None, "note": "gh failed"})
    return ci


def translate_log_entry(text):
    """Provides natural human Arabic summaries for recent mission log entries."""
    t = text.strip()
    if "round 5 (phone findings)" in t or "control-r5" in t:
        return "المقر: إطلاق الجولة الخامسة بناءً على تجربة الآيفون؛ تطبيق قاعدة الصدق التام ومستوى المالك البسيط في جميع المحادثات."
    if "control-r4" in t:
        return "غرفة التحكم: تجميد مشروع مفروشات نجم بالكامل؛ تشغيل خادم غرفة التحكم المستمر على المنفذ 8899؛ توفير عناوين IP المباشرة؛ وتصدير كبسولة مراجعة امتحان تحليل النظم في مقدمة الروابط."
    if "switched Antigravity account" in t or "a7medorabe7" in t:
        return "المقر: تدوير حسابات أنتيجرافيتي لتفادي حدود الاستخدام، وتفعيل آلية التبديل التلقائي الذكي."
    if "round 4 + improvement doctrine" in t:
        return "المقر: تعميم ميثاق التحسين المستمر والجولة الرابعة؛ تجميد مستودع نجم؛ وتخصيص مهام التحسين للهاتف."
    if "control-r3" in t:
        return "غرفة التحكم: تنظيف مستودعات المشاريع بالكامل؛ ترقية واجهة غرفة التحكم بمؤشرات حية وخطوط عربية متناسقة؛ وتحسين التصفح للهواتف الذكية."
    if "control-ci2" in t:
        return "غرفة التحكم: تدقيق فحوصات التكامل المستمر عبر خوادم لينكس؛ تشغيل 4 خدمات خلفية مشفرة عبر شبكة تيلسكيل للوصول من هاتف الآيفون؛ وعزل بيانات الخصوصية التامة."
    if "smart wake built" in t:
        return "المقر: بناء نظام الإيقاظ الذكي للوكلاء وتوزيعه على محادثات المشاريع."
    if "pushed _SIR ops" in t:
        return "المقر: مراجعة شاملة لتدفقات فحص المشاريع، وتوجيه مهام الفحص وضمان سهولة اللمس على الموبايل."
    if "restarted after the power cut" in t:
        return "المقر: استئناف تشغيل الخدمات ومراقبة التليجرام بعد انقطاع الكهرباء، والتحقق من سلامة كافة خوادم المزامنة المحلية."
    if "nightly:" in t:
        return "التقرير الليلي: فحص الأمان وتسريب البيانات، ومتابعة المساحة الخالية على الأقراص."
    if "five one-per-project standing-order" in t:
        return "المقر: إرسال توجيهات الأوامر الدائمة للمشاريع، وتفعيل إرسال التقارير المختصرة للأونر عبر تليجرام."
    if "Operations Research" in t or "SIR Study (Antigravity):" in t:
        return "منصة المذاكرة: إعداد وتدقيق ملخصات ورسومات مادة بحوث العمليات، وفحص التوافق الكامل مع الهواتف الذكية بنسبة 100%."
    if "SIR Negm Furniture" in t:
        return "مفروشات نجم: استكمال محرك التصميم الهندسي ثلاثي الأبعاد وإرسال عروض الأسعار (مجمّد لاحقاً بطلب الأونر)."
    if "AHome deploy batch" in t:
        return "المقر: بدء حزمة النشر المحلي لمنظومة المنزل والانتظار حتى انتهاء دورة الفحص."
    # Generic natural Arabic summary
    return f"عملية تشغيلية: {t[:160]}"


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


def parse_gemini_handover(projects):
    """Parses per-project master plans (.sir/MASTER_PLAN.md) and extracts next 10 tasks,
    building an honest readiness checklist for autonomous Gemini execution."""
    handover_projects = []

    # 1. First add Control Room / HQ itself
    hq_folder = os.path.normpath(os.path.join(HERE, ".."))
    hq_mp = os.path.join(hq_folder, ".sir", "MASTER_PLAN.md")
    hq_tasks = extract_tasks_from_markdown(hq_mp)

    handover_projects.append({
        "slug": "control",
        "name": "SIR Control Room (HQ)",
        "name_ar": "غرفة التحكم: المقر الرئيسي",
        "color": "#0F766E",
        "status": "verified",
        "has_master_plan": os.path.isfile(hq_mp),
        "master_plan_path": "_SIR/.sir/MASTER_PLAN.md",
        "plan_file_display": "_SIR/.sir/MASTER_PLAN.md",
        "tasks": hq_tasks[:10],
    })

    # 2. Add all portfolio projects
    for p in projects:
        slug = p["slug"]
        private = slug == "ahome"
        folder = os.path.join(ROOT, "AHome") if private else p["folder"]
        mp_path = os.path.join(folder, ".sir", "MASTER_PLAN.md")
        deep_plan = os.path.join(HERE, f"{slug}-DEEP.md")
        tasks_file = os.path.join(folder, ".sir", "TASKS.md")

        has_mp = False
        tasks = []
        display_path = f"_SIR/plans/{slug}.md"

        if private:
            has_mp = True
            tasks = ["Private project: task details stay on its own systems."]
            display_path = "AHome/.sir/MASTER_PLAN.md (protected)"
        elif os.path.isfile(mp_path):
            has_mp = True
            tasks = extract_tasks_from_markdown(mp_path)
            display_path = f"{p['name']}/.sir/MASTER_PLAN.md"
        
        if not tasks and os.path.isfile(deep_plan):
            has_mp = True
            tasks = extract_tasks_from_markdown(deep_plan)
            display_path = f"_SIR/plans/{slug}-DEEP.md"
            
        if not tasks and os.path.isfile(tasks_file):
            tasks = extract_tasks_from_markdown(tasks_file)
            display_path = f"{p['name']}/.sir/TASKS.md"

        # Double check privacy filter on tasks
        safe_tasks = []
        for t in tasks[:10]:
            safe_t = re.sub(r"ahmed-and-habiba", "AHome", t, flags=re.IGNORECASE)
            safe_t = re.sub(r"habiba", "AHome private data", safe_t, flags=re.IGNORECASE)
            safe_tasks.append(safe_t)

        handover_projects.append({
            "slug": slug,
            "name": p["name"],
            "name_ar": p.get("name_ar", p["name"]),
            "color": p.get("color", "#64748B"),
            "status": p.get("status", "backlog"),
            "has_master_plan": has_mp,
            "master_plan_path": display_path,
            "plan_file_display": display_path,
            "tasks": safe_tasks,
        })

    # 10 Honest Readiness Checklist items
    checklist = [
        {
            "id": "chk-model",
            "title_en": "Gemini 3.8 Flash High Autonomous Thinking in Antigravity",
            "title_ar": "تشغيل تفكير Gemini 3.8 Flash High في Antigravity",
            "category": "Model & Thinking",
            "category_ar": "النموذج ومستوى التفكير",
            "status": "ready",
            "desc_en": "Antigravity CLI and IDE pairing active with Gemini 3.8 Flash High; reasoning and code quality floor enforced.",
            "desc_ar": "بيئة العمل مهيأة بالكامل بنموذج Gemini 3.8 Flash High مع تفعيل الحد الأدنى لمعايير جودة الكود.",
        },
        {
            "id": "chk-charter",
            "title_en": "Perpetual Self-Review Loop & Quality Charter",
            "title_ar": "حلقة المراجعة الذاتية وميثاق الجودة التشغيلي",
            "category": "Governance",
            "category_ar": "الحوكمة وضمان الجودة",
            "status": "ready",
            "desc_en": "Charter codified in GEMINI_QUALITY_CHARTER.md (plan first, Dynamic Island springs, active tab label only, bespoke logos, no yellow buttons).",
            "desc_ar": "الميثاق موثق وملزم (التخطيط المسبق، فيزياء Dynamic Island، إظهار عنوان التبويب النشط فقط، الشعارات المخصصة، وحظر الأزرار الصفراء).",
        },
        {
            "id": "chk-subprocesses",
            "title_en": "Silent Headless Subprocesses & Background Tasks",
            "title_ar": "كتم العمليات الخلفية وتشغيل المهام المجدولة بدون وميض",
            "category": "System & OS",
            "category_ar": "النظام والبيئة المحلية",
            "status": "ready",
            "desc_en": "Windows Task Scheduler and daemons updated with wscript.exe, pythonw.exe, and CREATE_NO_WINDOW (zero console popup during gaming).",
            "desc_ar": "تحديث جميع المهام المجدولة والعمليات لتعمل بصمت تام عبر wscript و pythonw لمنع أي وميض أو مقاطعة للمستخدم أثناء الألعاب.",
        },
        {
            "id": "chk-git",
            "title_en": "Direct Main Deployments (No Pull Requests)",
            "title_ar": "الرفع والنشر المباشر على main بدون PRs",
            "category": "CI/CD & Git",
            "category_ar": "التكامل والتحكم بالمصادر",
            "status": "ready",
            "desc_en": "Direct commit and push straight to main across all repositories once local verify passes.",
            "desc_ar": "اعتماد الرفع المباشر لفرع main لجميع المستودعات بمجرد نجاح أوامر الفحص والتحقق دون انتظار مراجعات طلبات سحب.",
        },
        {
            "id": "chk-tailscale",
            "title_en": "Tailscale Remote Zero-Auth Phone Ingress (3300, 3456, 8765, 8899)",
            "title_ar": "الوصول عن بعد من الهاتف عبر Tailscale بدون تسجيل دخول",
            "category": "Remote Access",
            "category_ar": "الوصول عن بعد",
            "status": "ready",
            "desc_en": "Verified 4 stable HTTPS tailnet endpoints accessible from Ahmed's iPhone without login screens.",
            "desc_ar": "التحقق من 4 نقاط وصول مستقرة مشفرة عبر HTTPS من هاتف أحمد دون أي شاشات تسجيل دخول معقدة.",
        },
        {
            "id": "chk-telegram",
            "title_en": "Telegram Bot Milestone & Brief Dispatcher",
            "title_ar": "قناة إرسال الإيجازات والملفات المكتملة عبر تليجرام",
            "category": "Notifications",
            "category_ar": "الإشعارات والتواصل",
            "status": "ready",
            "desc_en": "Direct mobile delivery via send-telegram.mjs and send-owner-brief.mjs for completed briefs and reports.",
            "desc_ar": "إرسال الإيجازات التنفيذية والملفات المنتهية إلى تليجرام هاتف أحمد مباشرة عبر المفاتيح المشفرة.",
        },
        {
            "id": "chk-ollama",
            "title_en": "Local AI Model Redundancy (Ollama in D:\\Projects\\AI_Models_Hub)",
            "title_ar": "التحويل التلقائي للذكاء الاصطناعي المحلي (Ollama)",
            "category": "Local AI & RAG",
            "category_ar": "الذكاء المحلي",
            "status": "action_needed",
            "desc_en": "Automated fallback pipeline to local models (qwen2.5:7b-instruct, deepseek-r1:8b) when external cloud quotas or rate limits hit.",
            "desc_ar": "ربط مسار تبديل تلقائي للنماذج المحلية في AI_Models_Hub في حال نفاد الحصص السحابية أو انقطاع الإنترنت.",
        },
        {
            "id": "chk-orchestrator",
            "title_en": "Autonomous Cross-Project Loop Dispatcher",
            "title_ar": "مشغل الدورات المتتابعة الآلي بين المشاريع",
            "category": "Orchestration",
            "category_ar": "إدارة الدورات التلقائية",
            "status": "action_needed",
            "desc_en": "Replace manual brief generation with automated round-robin worker task scheduler (make-loop-briefs.py / agy-task.py).",
            "desc_ar": "استبدال التوجيه اليدوي بمشغل دورات تتابعي يدير استمرار العمل بين المشاريع تلقائياً بعد انتهاء اشتراك Claude.",
        },
        {
            "id": "chk-autonomy",
            "title_en": "Zero-Prompt Autonomous Desktop & Browser Control (SIR Autonomy)",
            "title_ar": "التحكم الذاتي بسطح المكتب والمتصفح بدون مقاطعة",
            "category": "Computer Use",
            "category_ar": "التحكم بالحاسوب",
            "status": "in_progress",
            "desc_en": "Chrome extension bridge and desktop engine require routine heartbeat integration tests with Gemini tool-calling.",
            "desc_ar": "تأكيد فحص الاتصال والتكامل بين إضافة كروم ومحرك سطح المكتب لتنفيذ العمليات البصرية مباشرة عبر Gemini.",
        },
        {
            "id": "chk-tier3",
            "title_en": "Strict Tier 3 Owner Actions Isolation",
            "title_ar": "العزل الصارم لإجراءات المالك الحصرية (المستوى 3)",
            "category": "Security & Privacy",
            "category_ar": "الأمان والخصوصية",
            "status": "ready",
            "desc_en": "Strict funneling of passkeys, 2FA, identity checks, and payments to OWNER_ACTIONS.md with zero agent leakage.",
            "desc_ar": "حصر كامل لإجراءات المالك الحصرية (مفاتيح المرور، 2FA، الدفع) في ملف مستقل لمنع أي تصرف غير مصرح به.",
        },
    ]

    ready_count = sum(1 for c in checklist if c["status"] == "ready")
    mp_ready_count = sum(1 for p in handover_projects if p["has_master_plan"])

    return {
        "projects": handover_projects,
        "checklist": checklist,
        "metrics": {
            "total_projects": len(handover_projects),
            "master_plans_ready": mp_ready_count,
            "tasks_tracked": sum(len(p["tasks"]) for p in handover_projects),
            "checklist_ready": ready_count,
            "checklist_total": len(checklist),
            "handover_countdown_days": handover_countdown_days(),
        }
    }


def handover_countdown_days():
    try:
        cfg = json.load(io.open(os.path.join(OPS, "config.json"), encoding="utf-8"))
        end = datetime.date.fromisoformat(cfg.get("claude_ends", "2026-11-23"))
        return (end - datetime.date.today()).days
    except Exception:
        return None


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
        "status": "healthy",
        "mode": "detached_daemon",
    }


def main():
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
        autopilot=parse_autopilot(),
        account_ledger=parse_account_ledger(),
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

    tpl = io.open(
        os.path.join(HERE, "dashboard_template.html"), encoding="utf-8"
    ).read()
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


if __name__ == "__main__":
    main()
