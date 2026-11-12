"""Dashboard generator modules split from dashboard_main.py (R19-M3).
Run: python D:/Projects/_SIR/plans/generate_dashboard.py, then HQ republishes the artifact.
AHome is private: counts and status only, never task text or notes.
Verification, suggestion, CI status and model registry readers."""
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


def parse_verifications(ops_dir=None):
    """Parse ops/verifications/ for verification results."""
    if ops_dir is None:
        ops_dir = OPS
    verifications_dir = os.path.join(ops_dir, "verifications")
    if not os.path.isdir(verifications_dir):
        return []
    items = []
    for fname in sorted(os.listdir(verifications_dir)):
        if not fname.endswith(".md"):
            continue
        task_name = fname[:-3]
        fpath = os.path.join(verifications_dir, fname)
        try:
            content = io.open(fpath, encoding="utf-8").read()
        except Exception:
            continue
        # Extract PASS/FAIL items
        pass_count = len(re.findall(r"\|\s*PASS\s*\|", content, re.I))
        fail_count = len(re.findall(r"\|\s*FAIL\s*\|", content, re.I))
        overall = "PASS" if "Overall: PASS" in content or "## Overall: PASS" in content else "FAIL"
        items.append({
            "task": task_name,
            "overall": overall,
            "pass": pass_count,
            "fail": fail_count,
            "total": pass_count + fail_count,
        })
    return items



def parse_suggestions(ops_dir=None):
    """Parse ops/SUGGESTIONS.md for scout findings."""
    if ops_dir is None:
        ops_dir = OPS
    fpath = os.path.join(ops_dir, "SUGGESTIONS.md")
    if not os.path.isfile(fpath):
        return []
    try:
        content = io.open(fpath, encoding="utf-8").read()
    except Exception:
        return []
    # Parse each suggestion entry
    entries = []
    sections = re.split(r"^## ", content, flags=re.MULTILINE)
    for sec in sections[1:]:  # Skip header
        lines_sec = sec.splitlines()
        if not lines_sec:
            continue
        header = lines_sec[0].strip()
        # Parse header: timestamp | project | severity
        parts = [p.strip() for p in header.split("|")]
        timestamp = parts[0] if len(parts) > 0 else ""
        project = parts[1] if len(parts) > 1 else ""
        severity = parts[2] if len(parts) > 2 else "medium"
        
        finding = ""
        evidence = ""
        proposed_brief = ""
        status = "pending"
        hq_note = ""
        
        for ln in lines_sec[1:]:
            ln = ln.strip()
            if ln.startswith("**Finding:**"):
                finding = ln.replace("**Finding:**", "").strip()
            elif ln.startswith("**Evidence:**"):
                evidence = ln.replace("**Evidence:**", "").strip()
            elif ln.startswith("**Proposed Brief:**"):
                proposed_brief = ln.replace("**Proposed Brief:**", "").strip()
            elif ln.startswith("**Status:**"):
                status = ln.replace("**Status:**", "").strip()
            elif ln.startswith("**HQ Note:**"):
                hq_note = ln.replace("**HQ Note:**", "").strip()
        
        if finding and not finding.startswith("<") and "<" not in header:
            entries.append({
                "timestamp": timestamp,
                "project": project,
                "severity": severity,
                "finding": finding,
                "evidence": evidence,
                "proposed_brief": proposed_brief,
                "status": status,
                "hq_note": hq_note,
            })
    return entries



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
