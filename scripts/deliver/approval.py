"""Ask Ahmed for a one-tap approval on Telegram and wait for the answer.

Usage: python approval.py <id> "<question in simple Arabic>" [timeout_minutes]
Sends the question with two buttons (callback data ok:<id> / no:<id>). telegram-inbox.mjs writes the answer to
ops/approvals.jsonl. Exit code: 0 approved, 1 rejected, 2 no answer in time (treat as NOT approved), 3 send failed.
The id must be unique per question (letters, digits, dot, dash, underscore; up to 60 characters).
Before sending, the id is registered as a pending request in ops/bus/approvals.json with its creation time;
telegram-inbox.mjs only accepts button presses for registered, unexpired (<24h), unanswered ids.
Never put AHome or Habiba content in the question.
"""
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
APPROVALS = ROOT / "ops" / "approvals.jsonl"
APPROVALS_JSON = ROOT / "ops" / "bus" / "approvals.json"
MAX_AGE_HOURS = 24


def _read_registry() -> list:
    if not APPROVALS_JSON.exists():
        return []
    try:
        rows = json.loads(APPROVALS_JSON.read_text(encoding="utf-8"))
        return rows if isinstance(rows, list) else []
    except Exception:
        return []


def _write_registry(rows: list) -> None:
    APPROVALS_JSON.parent.mkdir(parents=True, exist_ok=True)
    tmp = APPROVALS_JSON.parent / (APPROVALS_JSON.name + ".tmp")
    tmp.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    tmp.replace(APPROVALS_JSON)


def answer_for(approval_id: str) -> str | None:
    if not APPROVALS.exists():
        return None
    found = None
    for line in APPROVALS.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if row.get("id") == approval_id:
            found = row.get("answer")
    return found


def registry_answer(approval_id: str) -> str | None:
    """Answer already recorded in the shared registry, if any."""
    for row in _read_registry():
        if row and row.get("id") == approval_id and row.get("status") in ("approved", "rejected"):
            return row.get("answer") or row.get("status")
    return None


def is_expired(created_at: str | None) -> bool:
    """True when the request is older than MAX_AGE_HOURS or has no timestamp."""
    if not created_at:
        return True
    try:
        created = datetime.fromisoformat(str(created_at).replace("Z", "+00:00"))
    except ValueError:
        return True
    if created.tzinfo is None:
        created = created.replace(tzinfo=timezone.utc)
    return datetime.now(timezone.utc) - created > timedelta(hours=MAX_AGE_HOURS)


def register_pending(approval_id: str, question: str) -> None:
    """Record the request as system-created so the inbox accepts its buttons."""
    rows = _read_registry()
    now = datetime.now(timezone.utc).isoformat()
    existing = next((row for row in rows if row and row.get("id") == approval_id), None)
    if existing:
        existing.update({"text": question, "status": "pending", "answer": None,
                         "created_at": now, "answered_at": None})
    else:
        rows.append({"id": approval_id, "text": question, "status": "pending",
                     "answer": None, "created_at": now, "answered_at": None})
    _write_registry(rows)


def mark_send_failed(approval_id: str) -> None:
    rows = _read_registry()
    row = next((item for item in rows if item and item.get("id") == approval_id), None)
    if row:
        row["status"] = "send_failed"
        row["answered_at"] = datetime.now(timezone.utc).isoformat()
        _write_registry(rows)


def main() -> int:
    if len(sys.argv) < 3 or not re.fullmatch(r"[\w.-]{1,60}", sys.argv[1]):
        print(__doc__)
        return 3
    approval_id, question = sys.argv[1], sys.argv[2]
    minutes = float(sys.argv[3]) if len(sys.argv) > 3 else 720

    previous = answer_for(approval_id) or registry_answer(approval_id)
    if previous:
        return 0 if previous == "approved" else 1

    register_pending(approval_id, question)
    sent = subprocess.run(
        ["node", str(ROOT / "scripts/deliver/send-buttons.mjs"), question, f"موافق=ok:{approval_id}", f"لا=no:{approval_id}"],
        capture_output=True, text=True, creationflags=0x08000000,
    )
    if sent.returncode != 0:
        mark_send_failed(approval_id)
        print("send failed:", sent.stdout.strip()[:200])
        return 3
    deadline = time.time() + minutes * 60
    while time.time() < deadline:
        answer = answer_for(approval_id)
        if answer:
            print(answer)
            return 0 if answer == "approved" else 1
        time.sleep(10)
    print("no answer")
    return 2


if __name__ == "__main__":
    sys.exit(main())
