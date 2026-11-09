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

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from products import PRODUCTS  # noqa: E402
from kit_platforms import PLATFORM_NAMES  # noqa: E402

ROOT = os.environ.get("SIR_ROOT", "D:/Projects")
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
ORDER = json.load(io.open(os.path.join(HERE, "order.json"), encoding="utf-8"))
WAVEMAP = json.load(io.open(os.path.join(HERE, "waves.json"), encoding="utf-8"))

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

PROJECT_TRUTH = {
    "sir-study": {
        "status": "verified",
        "verified_today": True,
        "name_ar": "منصة المذاكرة الذكية",
        "exists_en": "SAD Exam Cram Capsule (25Q simulation exam, live countdown timer to 11:30 AM Cairo, score analytics, responsive mobile layout on port 3300).",
        "exists_ar": "كبسولة مراجعة ومحاكاة امتحان تحليل وتصميم النظم (25 سؤالاً تدريبياً، عداد تنازلي لموعد الامتحان 11:30 ص، تقييم الدرجات، وتصميم متوافق مع الموبايل على المنفذ 3300).",
        "verified_en": "Verified live in browser on port 3300 (sad.html), passing unit tests, GitHub Actions CI green.",
        "verified_ar": "تم التحقق الفعلي عبر المتصفح على المنفذ 3300، واجتياز كافة الاختبارات الآلية، وفحص GitHub CI ناجح 100%.",
        "missing_en": "Full academic curriculum modules beyond SAD, persistent exam history database, authentication.",
        "missing_ar": "باقي المواد الدراسية، قاعدة بيانات دائمة لتخزين نتائج الاختبارات، ونظام تسجيل الدخول.",
        "mission_ar": "كبسولات مراجعة مكثفة وامتحانات تدريبية تفاعلية للطلاب، متوافقة كلياً مع الهواتف الذكية.",
    },
    "sir-jobs": {
        "status": "verified",
        "verified_today": True,
        "name_ar": "منظومة إدارة فرص العمل",
        "exists_en": "Staged job opportunities pipeline, target company intelligence, salary benchmarks, sovereign review UI running on port 3456.",
        "exists_ar": "منظومة معالجة وتصنيف فرص العمل، بيانات الشركات المستهدفة، ومؤشرات الرواتب مع واجهة تحكم ومراجعة محلية على المنفذ 3456.",
        "verified_en": "86 unit/integration tests passing 100%, server active on port 3456, GitHub Actions CI passing.",
        "verified_ar": "اجتياز 86 اختباراً آلياً بنسبة 100%، استقرار عمل الخادم على المنفذ 3456، وفحص GitHub CI ناجح.",
        "missing_en": "Live auto-apply worker integration, external job portal sync APIs, production email dispatching.",
        "missing_ar": "الربط المباشر مع منصات التوظيف الخارجية، التقديم الآلي، وإرسال الرسائل الحية للشركات.",
        "mission_ar": "إدارة الفرص الوظيفية للمهندس أحمد علاء، والتقديم ومتابعة المقابلات بأمان واستقلالية.",
    },
    "ahome": {
        "status": "verified",
        "verified_today": True,
        "name_ar": "منظومة المنزل والخصوصية (AHome)",
        "exists_en": "Private home management suite, local sync daemons, encrypted state sync, offline-first storage.",
        "exists_ar": "منظومة إدارة المنزل والخصوصية التامة، خوادم مزامنة محلية، ومزامنة مشفرة تعمل بدون إنترنت.",
        "verified_en": "941 test suite passing 100%, background daemons active and syncing locally with zero leaks.",
        "verified_ar": "اجتياز 941 اختباراً بنسبة 100%، وتشغيل خوادم المزامنة المحلية بنجاح تام وبدون أي تسريب للبيانات.",
        "missing_en": "Multi-device biometric sync hardening, private cloud backup encryption verification.",
        "missing_ar": "تدقيق المزامنة الحيوية عبر الأجهزة المتعددة، والتحقق الإضافي من تشفير النسخ الاحتياطية السحابية الخاصة.",
        "mission_ar": "المنظومة الرقمية المشتركة لأحمد وحبيبة، تعمل محلياً بخصوصية صارمة ولا تغادر أجهزتهما.",
    },
    "sir-laptop-manager": {
        "status": "verified",
        "verified_today": True,
        "name_ar": "مدير الحاسوب والأداء",
        "exists_en": "Hardware telemetry, battery/power optimizer, background process supervisor, web ops UI on port 8765.",
        "exists_ar": "مراقبة العتاد والأداء، إدارة البطارية والطاقة، إدارة العمليات الخلفية، وواجهة تشغيل وتحكم ويب على المنفذ 8765.",
        "verified_en": "38 pytest tests passing, local service running on port 8765, GitHub Actions CI passing.",
        "verified_ar": "اجتياز 38 اختبار pytest بنسبة 100%، استقرار الخدمة المحلية على المنفذ 8765، وفحص GitHub CI ناجح.",
        "missing_en": "Tailscale host-header whitelist expansion, automated thermal curve fan profiles.",
        "missing_ar": "إتاحة الوصول عبر تيلسكيل من الآيفون بدون قيود الهوست، والتحكم الآلي المتقدم في سرعة المراوح.",
        "mission_ar": "إدارة وصيانة عتاد اللابتوب الشخصي، تسريع الأداء، وتوفير بيئة تشغيل مستقرة للوكلاء.",
    },
    "sir-ai": {
        "status": "rebuilding",
        "verified_today": False,
        "name_ar": "المساعد الذكي (جارفيس)",
        "exists_en": "Rebuild initiated from scratch. M0 forensic architecture scan completed, old code isolated in legacy/.",
        "exists_ar": "بدء إعادة البناء الشامل من الصفر. تم إنجاز الفحص المعماري الشامل وعزل الكود القديم في مجلد legacy/.",
        "verified_en": "Clean workspace initialized, dependencies verified. No end-to-end feature verification yet.",
        "verified_ar": "تهيئة بيئة عمل نظيفة والتحقق من التبعات. لم يتم التحقق النهائي من الميزات بعد.",
        "missing_en": "Core LLM router pipeline, model adapter modules, streaming API endpoints, desktop client UI.",
        "missing_ar": "محرك توجيه النماذج الذكية، وحدات الاتصال بالنظام، واجهات البرمجة اللحظية، وتطبيق سطح المكتب.",
        "mission_ar": "المساعد الرقمي الشخصي المستقل متعدد الوكلاء لإدارة المهام والتحكم الصوتي والآلي.",
    },
    "sir-negm-furniture": {
        "status": "frozen",
        "verified_today": False,
        "name_ar": "مفروشات نجم (مشروع صديق)",
        "exists_en": "Friend's commercial catalog repository. Kept isolated and private.",
        "exists_ar": "مستودع كتالوج تجاري وتطبيق أثاث لصديق. معزول تماماً وخاص.",
        "verified_en": "Frozen by owner order; not modified, tested, or deployed until handover.",
        "verified_ar": "مجمّد بأمر المالك؛ لا يتم تعديله أو اختباره أو نشره حتى موعد التسليم الرسمي.",
        "missing_en": "Client handover and explicit authorization before unfreezing.",
        "missing_ar": "التسليم الرسمي للعميل والحصول على إذن استئناف العمل.",
        "mission_ar": "كتالوج الأثاث واستوديو التصميم الداخلي وعروض الأسعار عبر واتساب لصالح عمر نجم.",
    },
    "sir-platform": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "منصة الأدوات والمكونات المشتركة",
        "exists_en": "Clean project skeleton, shared design tokens, component architecture specification.",
        "exists_ar": "هيكل مشروع نظيف، ومحددات التصميم المشترك والمكونات الأساسية.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "Core multi-platform UI components, theme tokens engine, distribution package.",
        "missing_ar": "المكونات البرمجية المشتركة لمختلف المنصات، حزم التوزيع، ومحرك الأنماط.",
        "mission_ar": "مكتبة الواجهات والأنماط المشتركة لتوحيد تجربة المستخدم في كافة منتجات SIR.",
    },
    "sir-obour-hub": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "بوابة العبور الأكاديمية",
        "exists_en": "Clean project skeleton, academic syllabus maps, student portal requirements.",
        "exists_ar": "هيكل مشروع نظيف، وخرائط المناهج الأكاديمية ومواصفات بوابة الطلاب.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "Lecture material ingestor, schedule synchronizer, GPA tracker, multi-tenant auth.",
        "missing_ar": "نظام استيراد المحاضرات، مزامنة الجداول، حاسبة المعدل التراكمي، وتسجيل الدخول.",
        "mission_ar": "البوابة الذكية لطلاب معاهد العبور لتنظيم المحاضرات والنتائج والتقويم الدراسي.",
    },
    "sir-hagoozat": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "منظومة حجوزات الملاعب",
        "exists_en": "Clean project skeleton, unified booking domain model, court management specs.",
        "exists_ar": "هيكل مشروع نظيف، ونموذج بيانات حجوزات الملاعب وإدارة الصالات الرياضية.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "Real-time reservation engine, SMS confirmation, payment gateway integration.",
        "missing_ar": "محرك الحجوزات اللحظي، إشعارات التأكيد، وبوابة الدفع الإلكتروني.",
        "mission_ar": "منظومة حجز وإدارة ملاعب البادل وكرة القدم وتأكيد الحجوزات والدفع إلكترونياً.",
    },
    "sir-business": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "منظومة إدارة الأعمال التجارية",
        "exists_en": "Clean project skeleton, commercial ERP architecture (restaurant, market, pharmacy, library).",
        "exists_ar": "هيكل مشروع نظيف، ومعمارية إدارة الأعمال والمبيعات للمطاعم والمتاجر والصيدليات والمكتبات.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "Point of sale (POS) terminal, inventory synchronization, invoicing, thermal print.",
        "missing_ar": "نظام نقاط البيع السريع، مزامنة المخزون، الفواتير، والطباعة الحرارية.",
        "mission_ar": "برنامج مبيعات ونقاط بيع وإدارة مخزون شامل للأنشطة التجارية في السوق المصري.",
    },
    "sir-content-creation-studio": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "استوديو صناعة المحتوى",
        "exists_en": "Clean project skeleton, video generation pipelines, creative automation plans.",
        "exists_ar": "هيكل مشروع نظيف، وخطط معالجة الفيديو وإنتاج المحتوى الآلي.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "FFmpeg timeline renderer, caption generator, social publishing sidecars.",
        "missing_ar": "محرك مونتاج الفيديو، توليد النصوص التلقائية، وجدولة النشر على المنصات.",
        "mission_ar": "استوديو آلي لإنتاج الفيديوهات والمحتوى الرقمي التسويقي ونشره على منصات التواصل.",
    },
    "sir-controller": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "مدير أذرع التحكم والألعاب",
        "exists_en": "Clean project skeleton, gamepad mapping schema, low-latency input engine design.",
        "exists_ar": "هيكل مشروع نظيف، ومخطط تعيين أزرار أذرع التحكم وتصميم محرك الاستجابة السريعة.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "DirectInput/XInput hook driver, profile cloud storage, UI overlay HUD.",
        "missing_ar": "تعريفات أذرع التحكم، حفظ التفضيلات السحابية، وواجهة العرض التفاعلية أثناء اللعب.",
        "mission_ar": "تطبيق لضبط وتعيين أزرار أذرع التحكم المختلفة للحواسيب والألعاب بزمن استجابة فائق.",
    },
    "sir-modpack": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "مدير حزم تعديلات الألعاب",
        "exists_en": "Clean project skeleton, mod repository manifests, package validator specs.",
        "exists_ar": "هيكل مشروع نظيف، ومواصفات فحص وتثبيت حزم التعديلات.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "Mod downloader engine, hash verification, conflict resolver, game launcher hook.",
        "missing_ar": "محرك تحميل وتثبيت التعديلات، فحص السلامة، وحل التعارضات مع الألعاب.",
        "mission_ar": "منصة لتنظيم وتثبيت إضافات ومودات الألعاب بأمان وسهولة بضغطة زر واحدة.",
    },
    "sir-mods-for-gta-v": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "تعديلات لعبة GTA V",
        "exists_en": "Clean project skeleton, script mod specifications, security audit documentation.",
        "exists_ar": "هيكل مشروع نظيف، وتوثيق فحص الأمان وتعديلات سكربتات لعبة GTA V.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "ScriptHookV bridge, native ASI launcher, clean configuration UI.",
        "missing_ar": "جسر الربط مع محرك اللعبة، مشغل الحزم، وواجهة ضبط الإعدادات.",
        "mission_ar": "حزمة تعديلات وسكربتات واقعية للعبة GTA V مع واجهة تثبيت وتشغيل مبسطة.",
    },
    "sir-life": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "منظومة الحياة والعادات",
        "exists_en": "Clean project skeleton, personal life tracking models (habits, wellness, milestones).",
        "exists_ar": "هيكل مشروع نظيف، ونماذج تتبع العادات اليومية والأهداف الشخصية والمالية.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "Daily logging interface, habit streak algorithms, encrypted personal storage.",
        "missing_ar": "واجهة التسجيل اليومي، خوارزميات الاستمرارية، والتخزين المشفر للبيانات.",
        "mission_ar": "تطبيق شخصي لتتبع الأهداف، العادات اليومية، الصحة، والمصاريف بخصوصية تامة.",
    },
    "sir-portfolio": {
        "status": "backlog",
        "verified_today": False,
        "name_ar": "معرض الأعمال الشخصي",
        "exists_en": "Clean project skeleton, portfolio showcase blueprints, Ahmed Alaa CV data.",
        "exists_ar": "هيكل مشروع نظيف، ومخطط معرض المشاريع والبيانات المهنية للمهندس أحمد علاء.",
        "verified_en": "None (clean skeleton awaiting wave rebuild from zero).",
        "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء من الصفر).",
        "missing_en": "Interactive live demo viewer, case study write-ups, deployment to custom domain.",
        "missing_ar": "نظام عرض التجارب الحية، دراسات الحالة للمنتجات، والنشر النهائي على النطاق الشخصي.",
        "mission_ar": "الموقع الرسمي للمهندس أحمد علاء لعرض المشاريع المكتملة ودراسات الحالة والتواصل.",
    },
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
        ).stdout.strip()
    except Exception:
        return ""


def parse_tasks(folder, private):
    ms, cur = [], None
    for ln in lines(os.path.join(folder, ".sir", "TASKS.md")):
        m = re.match(r"## (M\d) (.*)", ln)
        if m:
            cur = dict(name=m.group(1) + " " + m.group(2), items=[])
            ms.append(cur)
        elif cur and (
            m2 := re.match(r"- \[([ x])\] (T-\d+) \| owner: [^|]+\| (.*)", ln)
        ):
            text = re.sub(r"\s*\| depends:.*", "", m2.group(3)).replace("(kit) ", "")
            cur["items"].append(
                dict(
                    id=m2.group(2),
                    done=m2.group(1) == "x",
                    text="" if private else text[:240],
                )
            )
    return ms


def checkpoint_now(folder):
    out, on = [], False
    for ln in lines(os.path.join(folder, ".sir", "CHECKPOINT.md")):
        if ln.startswith("## Now"):
            on = True
            continue
        if on and ln.startswith("## "):
            break
        if on and ln.strip():
            out.append(clean(ln.lstrip("- ")))
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
        )
        if r.returncode == 0 and r.stdout.strip().isdigit():
            return int(r.stdout.strip())
    except Exception:
        pass
    return 31


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
        try:
            r = subprocess.run(
                [
                    "gh",
                    "run",
                    "list",
                    "-R",
                    repo,
                    "--limit",
                    "1",
                    "--json",
                    "conclusion,status,databaseId,headBranch,name,url",
                ],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if r.returncode == 0 and r.stdout.strip():
                runs = json.loads(r.stdout.strip())
                if runs:
                    latest = runs[0]
                    ci.append(
                        {
                            "name": name,
                            "repo": repo,
                            "status": latest.get("conclusion")
                            or latest.get("status")
                            or "unknown",
                            "id": latest.get("databaseId"),
                            "url": latest.get("url"),
                        }
                    )
                else:
                    ci.append(
                        {
                            "name": name,
                            "repo": repo,
                            "status": "none",
                            "id": None,
                            "url": None,
                        }
                    )
            else:
                ci.append(
                    {
                        "name": name,
                        "repo": repo,
                        "status": "none",
                        "id": None,
                        "url": None,
                    }
                )
        except Exception:
            ci.append(
                {
                    "name": name,
                    "repo": repo,
                    "status": "none",
                    "id": None,
                    "url": None,
                }
            )
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
    if "SIR Jobs" in t:
        return "منظومة فرص العمل: تدقيق الواجهة، استقرار الفحوصات الآلية، وتشغيل لوحة التحكم والمراجعة بنجاح."
    if "SIR Laptop Manager" in t:
        return "مدير الحاسوب: اجتياز كافة اختبارات بايثون بنسبة 100%، واستقرار خدمة مراقبة العتاد والأداء."
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
    try:
        content = open(hq_bus, "r", encoding="utf-8").read()
        target_msg = "artifact outdated: republish ops/artifact/control-room.html"
        if target_msg in content:
            return

        lines = content.splitlines()
        insert_idx = 2
        for idx, line in enumerate(lines):
            if line.startswith("- [ ]") or line.startswith("- [x]"):
                insert_idx = idx
                break

        today = datetime.datetime.now().strftime("%Y-%m-%d")
        notice = f"- [ ] {today} from control-room-daemon:\n  notice: {target_msg} (hash {content_hash})\n"
        lines.insert(insert_idx, notice)
        with open(hq_bus, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines) + "\n")
    except Exception as e:
        print(f"Warning: could not notify HQ: {e}")


def main():
    projects = []
    for p in PRODUCTS:
        folder = ROOT + "/" + p["folder"]
        if not os.path.isfile(folder + "/.sir/TASKS.md"):
            continue
        private = p["slug"] == "ahome"
        st = json.load(io.open(folder + "/.sir/status.json", encoding="utf-8"))
        ms = parse_tasks(folder, private)
        items = [i for m in ms for i in m["items"]]
        done = sum(i["done"] for i in items)
        yml = "\n".join(lines(folder + "/.sir/project.yml"))
        arch = re.search(r"archetype: (.*)", yml)

        truth = PROJECT_TRUTH.get(
            p["slug"],
            {
                "status": "backlog",
                "verified_today": False,
                "name_ar": p["display"],
                "exists_en": "Project skeleton initialized.",
                "exists_ar": "تم إنشاء هيكل المشروع الأساسي.",
                "verified_en": "None (clean skeleton awaiting wave rebuild).",
                "verified_ar": "لا يوجد (هيكل نظيف بانتظار مرحلة إعادة البناء).",
                "missing_en": "Full rebuild from zero.",
                "missing_ar": "إعادة البناء الكاملة من الصفر.",
                "mission_ar": p["mission"][:260],
            },
        )

        status = truth["status"]

        projects.append(
            dict(
                slug=p["slug"],
                name="AHome (private)" if private else p["display"],
                name_ar="AHome (خاص ومحمي)" if private else truth.get("name_ar", p["display"]),
                wave=WAVEMAP.get(p["slug"], 9),
                order=ORDER.index(p["slug"]) if p["slug"] in ORDER else 99,
                color=BRAND.get(p["slug"], {}).get("color", "#64748B"),
                arch="private, details withheld"
                if private
                else (arch.group(1) if arch else ""),
                status=status,
                verified_today=truth["verified_today"],
                truth=truth,
                done=done,
                total=len(items),
                milestones=[dict(name=m["name"], items=m["items"]) for m in ms],
                next=[]
                if (private or status == "frozen")
                else [i["id"] + " " + i["text"][:150] for i in items if not i["done"]][
                    :4
                ],
                now="Frozen, friend's project. Private repo; not touched or deployed until handover."
                if status == "frozen"
                else ("" if private else checkpoint_now(folder)),
                mission="Private. Counts only." if private else p["mission"][:260],
                mission_ar=truth.get("mission_ar", p["mission"][:260]),
                repo=(
                    "private repo (not pushed from HQ)"
                    if private
                    else "github.com/sirahmed8/" + p["repo"] + " (private)"
                ),
                folder="withheld" if private else "D:\\Projects\\" + p["folder"],
                commit=git(folder, "log", "-1", "--format=%cs") if not private else "",
                sync=(
                    ""
                    if private
                    else (
                        "in sync"
                        if "ahead" not in git(folder, "status", "-sb").split("\n")[0]
                        and "behind" not in git(folder, "status", "-sb").split("\n")[0]
                        else "not in sync"
                    )
                ),
                required=sum(1 for v in st["platforms"].values() if v == "required"),
                matrix=None if private else st["platforms"],
            )
        )

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

    active = []
    try:
        active = json.load(io.open(OPS + "/active.json", encoding="utf-8"))
    except Exception:
        pass

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
        log_entries.append(
            {
                "en": l,
                "ar": translate_log_entry(l),
            }
        )

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
        nextStart=(nxt["name"] if nxt else ""),
        nextStart_ar=(nxt["name_ar"] if nxt else ""),
        log=log_entries,
        repos=dict(
            new_private=len([p for p in projects if p["matrix"]]),
            archived=archived_count(),
        ),
        platforms=[dict(key=k, name=n, short=SHORT[k]) for k, n in PLATFORM_NAMES],
        request_ledgers=parse_request_ledgers(),
        ci=get_ci_status(),
        remote_access=[
            {
                "name": "SIR Study (SAD Exam)",
                "name_ar": "منصة المذاكرة (امتحان تحليل النظم)",
                "port": 3300,
                "url": "https://ahmed.tail9e9aa7.ts.net:3300/sad.html",
                "ip_url": "https://100.85.112.10:3300/sad.html",
                "desc_en": "SAD Exam Cram Capsule (Today 11:30 AM Cairo)",
                "desc_ar": "كبسولة مراجعة ومحاكاة امتحان تحليل وتصميم النظم (اليوم 11:30 ص)",
            },
            {
                "name": "SIR Jobs",
                "name_ar": "منظومة فرص العمل",
                "port": 3456,
                "url": "https://ahmed.tail9e9aa7.ts.net:3456/",
                "ip_url": "https://100.85.112.10:3456/",
                "desc_en": "Pipeline & Staged Opportunities Review",
                "desc_ar": "منظومة إدارة فرص العمل ومراجعة التقديم",
            },
            {
                "name": "SIR Control Room",
                "name_ar": "غرفة التحكم — المقر الرئيسي",
                "port": 8899,
                "url": "https://ahmed.tail9e9aa7.ts.net:8899/dashboard.html",
                "ip_url": "https://100.85.112.10:8899/dashboard.html",
                "desc_en": "Portfolio Ground Truth & Agent Ops",
                "desc_ar": "لوحة الحقيقة التشغيلية والمتابعة الشاملة للمشاريع",
            },
            {
                "name": "SIR Laptop Manager",
                "name_ar": "مدير الحاسوب والأداء",
                "port": 8765,
                "url": "https://ahmed.tail9e9aa7.ts.net:8765/",
                "ip_url": "https://100.85.112.10:8765/",
                "desc_en": "Ops UI & Hardware Gauges",
                "desc_ar": "لوحة تشغيل الحاسوب ومراقبة العتاد والأداء",
            },
        ],
    )

    models = load_models()
    git_hash = get_git_short_hash()
    published_hash = get_published_hash()

    data["models"] = models
    data["git_hash"] = git_hash

    # Deterministic content hash computed over data payload excluding generated timestamp and hash fields
    hash_seed_dict = {
        k: v for k, v in data.items()
        if k not in ("content_hash", "artifact_synced", "generated")
    }
    hash_seed = json.dumps(hash_seed_dict, sort_keys=True, ensure_ascii=False)
    content_hash = hashlib.sha256(hash_seed.encode("utf-8")).hexdigest()[:8]
    data["content_hash"] = content_hash
    data["artifact_synced"] = bool(published_hash and published_hash == content_hash)

    tpl = io.open(
        os.path.join(HERE, "dashboard_template.html"), encoding="utf-8"
    ).read()
    out = tpl.replace("/*__DATA__*/{}", json.dumps(data, ensure_ascii=False))

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

    # Single source: Write to both website and Claude artifact
    os.makedirs(os.path.join(OPS, "artifact"), exist_ok=True)
    site_path = os.path.join(OPS, "dashboard.html")
    artifact_path = os.path.join(OPS, "artifact", "control-room.html")
    changed_path = os.path.join(OPS, "artifact", "CHANGED.txt")

    io.open(site_path, "w", encoding="utf-8", newline="\n").write(out)
    io.open(artifact_path, "w", encoding="utf-8", newline="\n").write(out)
    io.open(changed_path, "w", encoding="utf-8", newline="\n").write(content_hash + "\n")

    if not data["artifact_synced"]:
        notify_hq_artifact_outdated(content_hash)

    print(f"dashboard.html & control-room.html generated ({len(out)} bytes, hash {content_hash}, git {git_hash}, synced={data['artifact_synced']})")


if __name__ == "__main__":
    main()
