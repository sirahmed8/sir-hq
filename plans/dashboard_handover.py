"""Gemini handover checklist and per-project master-plan task extraction (split from dashboard_data.py, R19-M3).
AHome is private: counts and status only, never task text or notes."""
import datetime
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dashboard_data import extract_tasks_from_markdown  # noqa: E402

ROOT = os.environ.get("SIR_ROOT", "D:/Projects")
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))


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



