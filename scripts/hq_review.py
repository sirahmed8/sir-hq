"""HQ review loop for scout suggestions.

HQ (the manager) reads ops/SUGGESTIONS.md, approves the good items by queueing them through
scripts/queue-add.py, and rejects the rest with a reason in the same file. Items the owner rejects with the
Telegram buttons are recorded in ops/suggestion-rejects.json and never proposed again.

What one run does, in order:
1. Applies the owner's button answers from ops/approvals.jsonl (ids start with sug-).
2. Auto-approves pending items that are clear: critical/high severity, a real brief name, a project folder that
   exists, not rejected before, not already queued.
3. Sends the remaining pending items to Ahmed as one message with approve/reject buttons (max 3 per run),
   registered in ops/bus/approvals.json so the inbox accepts the taps within 24 hours.

Usage: python hq_review.py [--dry] [--no-telegram] [--limit N]
Exit code 0 when the run itself worked.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

from hq_team import (OPS, PROJECTS, QUEUE_ADD, add_reject, game_mode_active, is_rejected, load_json,
                     load_queue, load_suggestions, log, lower_priority, rewrite_suggestions, save_json)

NAME = "review"
APPROVALS_JSONL = OPS / "approvals.jsonl"
REGISTRY = OPS / "bus" / "approvals.json"
STATE = OPS / "review-state.json"
AUTO_SEVERITIES = ("critical", "high")
OFFER_PER_RUN = 3
MAX_AGE_HOURS = 24


def folder_for(project_name: str) -> str:
    for key, (name, folder) in PROJECTS.items():
        if name.lower() == (project_name or "").strip().lower() or key == (project_name or "").strip().lower():
            return folder
    return ""


def brief_name(entry: dict) -> str:
    proposed = entry["fields"].get("Proposed Brief", "").strip()
    if re.fullmatch(r"[a-z0-9][a-z0-9-]{2,60}", proposed or ""):
        return proposed
    key = next((k for k, (n, _f) in PROJECTS.items() if n.lower() == entry["fields"].get("Project", "").lower()),
               "sir-hq")
    slug = re.sub(r"[^a-z0-9]+", "-", entry["fields"].get("Finding", "").lower()).strip("-")[:40]
    return f"r43-{key}-{slug}"[:70].strip("-")


def register_pending(sug_id: str, question: str) -> None:
    rows = load_json(REGISTRY, [])
    if not isinstance(rows, list):
        rows = []
    now = time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime())
    existing = next((r for r in rows if r.get("id") == sug_id), None)
    if existing:
        existing.update({"text": question, "status": "pending", "answer": None, "created_at": now,
                         "answered_at": None})
    else:
        rows.append({"id": sug_id, "text": question, "status": "pending", "answer": None,
                     "created_at": now, "answered_at": None})
    save_json(REGISTRY, rows)


def owner_answers() -> dict:
    """Approved/rejected ids for suggestion buttons, newest answer wins."""
    answers = {}
    path = APPROVALS_JSONL
    if not path.exists():
        return answers
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            row = json.loads(line)
        except ValueError:
            continue
        sid = str(row.get("id", ""))
        if sid.startswith("sug-") and row.get("answer") in ("approved", "rejected"):
            answers[sid] = row["answer"]
    return answers


def approve(entry: dict, reason: str) -> bool:
    """Queue the suggestion through queue-add.py so the autopilot really picks it up."""
    name = brief_name(entry)
    if any(t.get("name") == name for t in load_queue()):
        entry["fields"]["Status"] = "approved"
        entry["fields"]["HQ Note"] = f"already queued as {name}"
        return False
    folder = folder_for(entry["fields"].get("Project", ""))
    if not folder or not Path(folder).is_dir():
        entry["fields"]["Status"] = "rejected"
        entry["fields"]["HQ Note"] = f"project folder not found for {entry['fields'].get('Project', '?')}"
        add_reject(entry["fields"].get("Finding", ""), "project folder not found")
        return False
    brief = OPS / "briefs" / f"{name}.md"
    brief.parent.mkdir(parents=True, exist_ok=True)
    brief.write_text(
        f"Scout finding approved by HQ.\n\n"
        f"Project: {entry['fields'].get('Project', '')}\n"
        f"Severity: {entry['fields'].get('Severity', '')}\n"
        f"Category: {entry['fields'].get('Category', '')}\n\n"
        f"Finding: {entry['fields'].get('Finding', '')}\n\n"
        f"Evidence: {entry['fields'].get('Evidence', '')}\n\n"
        "Do this: reproduce the finding with the evidence above, fix the cause (not the report), add or update a "
        "test where the project has tests, and check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for "
        "the touched screens. Run the project's checks and CI until green, commit and push to main, update the "
        "project checkpoint, write a short report with the real command output, then tick this item in "
        "ops/SUGGESTIONS.md (Status: done) so the next scout does not propose it again.\n",
        encoding="utf-8")
    res = subprocess.run([sys.executable, str(QUEUE_ADD), name, str(brief), folder,
                          entry["fields"].get("Finding", name)[:90]], capture_output=True, text=True, timeout=180)
    ok = res.returncode == 0
    entry["fields"]["Status"] = "approved"
    entry["fields"]["HQ Note"] = f"queued as {name} ({reason})" if ok else f"queue-add failed: {(res.stdout or res.stderr)[:120]}"
    return ok


def reject(entry: dict, reason: str) -> None:
    entry["fields"]["Status"] = "rejected"
    entry["fields"]["HQ Note"] = reason
    add_reject(entry["fields"].get("Finding", ""), reason)


def offer_to_owner(pending: list, dry: bool, no_telegram: bool) -> int:
    """One Telegram message with approve/reject buttons for the next pending items."""
    state = load_json(STATE, {})
    if not isinstance(state, dict):
        state = {}
    offered = state.get("offered", {})
    now = time.time()
    fresh = []
    for entry in pending:
        sid = entry["id"]
        last = float(offered.get(sid, 0))
        if now - last < MAX_AGE_HOURS * 3600:
            continue
        fresh.append(entry)
    batch = fresh[:OFFER_PER_RUN]
    if not batch:
        return 0
    lines = ["اقتراحات من كشافة المشاريع", ""]
    pairs = []
    for entry in batch:
        sid = entry["id"]
        finding = entry["fields"].get("Finding", "")[:110]
        project = entry["fields"].get("Project", "")
        severity = entry["fields"].get("Severity", "medium")
        lines.append(f"- {project} ({severity}): {finding}")
        pairs.extend([f"موافق {len(pairs) // 2 + 1}=ok:{sid}", f"لا {len(pairs) // 2 + 1}=no:{sid}"])
    lines.append("")
    lines.append("المطلوب منك: اضغط موافق أو لا، أو لا شيء.")
    text = "\n".join(lines)
    if dry or no_telegram:
        log(NAME, f"would offer {len(batch)} items: {[e['id'] for e in batch]}")
        return 0
    for entry in batch:
        register_pending(entry["id"], entry["fields"].get("Finding", "")[:200])
    script = OPS.parent / "scripts" / "deliver" / "send-buttons.mjs"
    try:
        res = subprocess.run(["node", str(script), text] + pairs, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as exc:
        log(NAME, f"send buttons failed: {exc!r}")
        return 0
    if res.returncode != 0:
        log(NAME, f"send buttons failed: {(res.stdout or '').strip()[:160]}")
        return 0
    for entry in batch:
        offered[entry["id"]] = now
    state["offered"] = offered
    save_json(STATE, state)
    stamp = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    try:
        with open(OPS / "bus" / "telegram-outbox.md", "a", encoding="utf-8") as fh:
            fh.write(f"{stamp} | HQ-review | {len(batch)} scout suggestions with approve/reject buttons\n")
    except OSError:
        pass
    log(NAME, f"offered {len(batch)} items to the owner")
    return len(batch)


def main(argv: list) -> int:
    if game_mode_active():
        log(NAME, "skip: game mode active")
        print("skip: game mode active")
        return 0
    lower_priority()
    dry = "--dry" in argv
    no_telegram = "--no-telegram" in argv
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 50

    entries = load_suggestions()
    if not entries:
        log(NAME, "no suggestions to review")
        print("no suggestions")
        return 0

    answers = owner_answers()
    changed = False
    approved = rejected = 0
    for entry in entries:
        status = (entry["fields"].get("Status") or "pending").lower()
        if status not in ("pending",):
            continue
        sid = entry["id"]
        if answers.get(sid) == "approved":
            if not dry:
                approve(entry, "owner approved on Telegram")
            approved += 1
            changed = True
            continue
        if answers.get(sid) == "rejected":
            if not dry:
                reject(entry, "owner rejected on Telegram")
            rejected += 1
            changed = True
            continue
        severity = (entry["fields"].get("Severity") or "medium").lower()
        if severity in AUTO_SEVERITIES and not is_rejected(entry["fields"].get("Finding", "")):
            if not dry:
                approve(entry, "HQ auto-approved: clear defect")
            approved += 1
            changed = True

    pending = [e for e in entries if (e["fields"].get("Status") or "pending").lower() == "pending"]
    if changed and not dry:
        rewrite_suggestions(entries)
    offered = offer_to_owner(pending[:limit], dry, no_telegram)
    log(NAME, f"approved {approved}, rejected {rejected}, offered {offered}, pending {len(pending)}")
    print(f"approved={approved} rejected={rejected} offered={offered} pending={len(pending)} dry={dry}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
