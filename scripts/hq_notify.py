"""Telegram output for the r42 team: FAIL only, plus one plain daily summary at 21:00.

Rules (ops/WORKER_PREAMBLE.md 12 and 17): short title first, at most 5 one-fact lines, plain words, numbers with
their meaning, no file paths or commit hashes, no mixed Arabic and English in one sentence, and never repeat a
message another duty already sent in the last hours (checked in ops/bus/telegram-outbox.md).

Usage:
  python hq_notify.py --fails     one message per verification that FAILed and was not reported yet
  python hq_notify.py --daily     the 21:00 summary (one message, skipped if already sent today)
  python hq_notify.py --fails --dry
Exit code 0 when the run itself worked.
"""
import sys
import time
from datetime import datetime
from pathlib import Path

from hq_team import (OPS, game_mode_active, load_json, load_queue, load_suggestions, log, lower_priority,
                     notify_owner, read_text, save_json)

NAME = "notify"
VERIFICATIONS = OPS / "verifications"
STATE = OPS / "notify-state.json"


def rows_of(path: Path) -> list:
    text = read_text(path)
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[2].upper() in ("PASS", "FAIL"):
            rows.append({"item": cells[0], "verdict": cells[2].upper()})
    return rows


def overall_of(path: Path) -> str:
    text = read_text(path)
    for line in text.splitlines():
        if line.startswith("## Overall:"):
            return "PASS" if "PASS" in line else "FAIL"
    rows = rows_of(path)
    return "FAIL" if any(r["verdict"] == "FAIL" for r in rows) else ("PASS" if rows else "UNKNOWN")


def label_of(task: str) -> str:
    try:
        import json
        for r in json.loads((Path("D:/Projects/_SIR/ops/round_labels.json")).read_text(encoding="utf-8")):
            if r["task"] == task:
                return f"{r['label']} ({r['title'][:40]})"
    except Exception:
        pass
    return task


def fails(argv: list) -> int:
    dry = "--dry" in argv
    state = load_json(STATE, {})
    if not isinstance(state, dict):
        state = {}
    told = state.get("fails", {})
    sent = 0
    for path in sorted(VERIFICATIONS.glob("*.md")):
        task = path.stem
        if overall_of(path) != "FAIL" or task in told or task.startswith("ci-"):
            continue  # CI-fix tasks are not owner news; one daily summary covers them
        rows = rows_of(path)
        bad = [r["item"] for r in rows if r["verdict"] == "FAIL"]
        text = ("تدقيق مهمة لم ينجح\n"
                f"المهمة: {label_of(task)}\n"
                f"البنود الفاشلة: {len(bad)} من {len(rows)}.\n"
                "تم إنشاء مهمة تصحيح لها في قائمة العمل تلقائيا.\n"
                "المطلوب منك: لا شيء.")
        if dry:
            print(f"would send FAIL for {task}")
            continue
        if notify_owner(text, "verifier-fail", hours=6):
            told[task] = time.strftime("%Y-%m-%dT%H:%M:%S")
            sent += 1
    if sent and not dry:
        state["fails"] = told
        save_json(STATE, state)
    log(NAME, f"fails: sent {sent}")
    print(f"fails sent={sent} dry={dry}")
    return 0


def finished_today() -> int:
    done_dir = OPS / "agy-runs" / "done"
    if not done_dir.is_dir():
        return 0
    today = datetime.now().date()
    count = 0
    for path in done_dir.glob("*.done"):
        try:
            if datetime.fromtimestamp(path.stat().st_mtime).date() == today:
                count += 1
        except OSError:
            continue
    return count


def daily(argv: list) -> int:
    dry = "--dry" in argv
    stamp = time.strftime("%Y-%m-%d")
    state = load_json(STATE, {})
    if not isinstance(state, dict):
        state = {}
    if state.get("daily") == stamp:
        log(NAME, "daily summary already sent today")
        print("daily already sent")
        return 0

    verifications = list(VERIFICATIONS.glob("*.md"))
    passed = sum(1 for p in verifications if overall_of(p) == "PASS")
    failed = sum(1 for p in verifications if overall_of(p) == "FAIL")
    entries = load_suggestions()
    pending = sum(1 for e in entries if (e["fields"].get("Status") or "pending").lower() == "pending")
    approved = sum(1 for e in entries if (e["fields"].get("Status") or "").lower() == "approved")
    open_tasks = sum(1 for t in load_queue() if not t.get("done"))

    text = ("ملخص اليوم\n"
            f"مهام خلصت النهارده: {finished_today()}.\n"
            f"مهام مستنية في القائمة: {open_tasks}.\n"
            f"تدقيقات: {passed} ناجحة و {failed} فاشلة.\n"
            f"اقتراحات الكشافة: {pending} مستنية قرار و {approved} اتوافق عليها.\n"
            "المطلوب منك: لا شيء.")
    if dry:
        print(text)
        return 0
    if notify_owner(text, "daily-summary", hours=12):
        state["daily"] = stamp
        save_json(STATE, state)
    return 0


def main(argv: list) -> int:
    if game_mode_active():
        log(NAME, "skip: game mode active")
        print("skip: game mode active")
        return 0
    lower_priority()
    if "--daily" in argv:
        return daily(argv)
    if "--fails" in argv:
        return fails(argv)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
