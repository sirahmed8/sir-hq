"""Compose a short Arabic status brief for Ahmed from git and GitHub (no private content) and print it.

Used by telegram-inbox.mjs when Ahmed sends /status to the bot.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1])); import nowindow  # noqa: F401
import subprocess, json

P = "D:/Projects"
PROJECTS = [("AHome", "التطبيق الخاص", "sirahmed8/ahmed-and-habiba"), ("SIR Study", "المذاكرة", "sirahmed8/sir-study"),
            ("SIR Jobs", "الوظائف", "sirahmed8/sir-jobs"), ("SIR Optimizer", "محسّن النظام", "sirahmed8/sir-optimizer"),
            ("_SIR", "غرفة التحكم", "sirahmed8/sir-hq")]


def run(*a):
    return subprocess.run(a, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()


lines = ["[الإدارة] الحالة الآن:"]
for folder, ar, repo in PROJECTS:
    last = run("git", "-C", f"{P}/{folder}", "log", "-1", "--format=%ar")
    ci = run("gh", "run", "list", "-R", repo, "--limit", "1", "--json", "conclusion,status", "-q", ".[0] | .conclusion // .status")
    mark = {"success": "سليم", "failure": "فيه خطأ", "in_progress": "قيد الفحص"}.get(ci, ci or "-")
    lines.append(f"- {ar}: آخر تحديث {last}، الفحص: {mark}")
lines.append("الشغل مستمر في كل المشاريع، ومش محتاج منك حاجة.")
print("\n".join(lines))
