"""Ask Ahmed for a one-tap approval on Telegram and wait for the answer.

Usage: python approval.py <id> "<question in simple Arabic>" [timeout_minutes]
Sends the question with two buttons (callback data ok:<id> / no:<id>). telegram-inbox.mjs writes the answer to
ops/approvals.jsonl. Exit code: 0 approved, 1 rejected, 2 no answer in time (treat as NOT approved), 3 send failed.
The id must be unique per question (letters, digits, dot, dash, underscore; up to 60 characters).
Never put AHome or Habiba content in the question.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
APPROVALS = ROOT / "ops" / "approvals.jsonl"


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


def main() -> int:
    if len(sys.argv) < 3 or not re.fullmatch(r"[\w.-]{1,60}", sys.argv[1]):
        print(__doc__)
        return 3
    approval_id, question = sys.argv[1], sys.argv[2]
    minutes = float(sys.argv[3]) if len(sys.argv) > 3 else 720
    previous = answer_for(approval_id)
    if previous:
        return 0 if previous == "approved" else 1
    sent = subprocess.run(
        ["node", str(ROOT / "scripts/deliver/send-buttons.mjs"), question, f"موافق=ok:{approval_id}", f"لا=no:{approval_id}"],
        capture_output=True, text=True, creationflags=0x08000000,
    )
    if sent.returncode != 0:
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
