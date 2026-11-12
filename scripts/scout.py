"""Project scouts: one per project, daily, on free models.

Each scout reads the project checkpoint, recent commits, CI status, the owner feedback files and the shared
lessons, tests the running app through a NEW lens (a different lens every run), and appends concrete findings
to ops/SUGGESTIONS.md: bug, missing feature, polish, risk, next best idea, each with project, severity,
evidence and a proposed brief. Findings already open in the queue, already suggested, or rejected by the owner
are dropped (dedupe), so the manager never reads the same item twice.

Usage:
  python scout.py <project-key> [--dry] [--lens "..."]     one project
  python scout.py --all [--dry]                            every project in hq_team.PROJECTS
Exit code 0 when the run itself worked.
"""
import json
import re
import sys
import time
from pathlib import Path

from hq_team import (OPS, PROJECTS, game_mode_active, is_duplicate, is_rejected, lessons_text, load_json,
                     load_queue, load_suggestions, log, lower_priority, pool_pick, read_text,
                     rewrite_suggestions, run_agent, save_json, suggestion_id)

NAME = "scout"
LENSES_FILE = OPS / "scout-lenses.json"
MAX_FINDINGS = 5
LENSES = [
    "accessibility and keyboard: focus order, labels, contrast, 44 px targets",
    "narrow phone layout at 320 and 390 px: clipping, overflow, one-letter wrapping",
    "empty, loading, error and offline states: does every screen explain itself and offer retry",
    "Arabic and RTL: bidi per character, logical CSS, no literal (RTL)/(LTR)",
    "motion and performance: spring open and close, transform/opacity only, jank on scroll",
    "data correctness: counts, dates, currencies and totals match the real data source",
    "failure handling: network errors, retries, partial saves, what the user sees",
    "privacy and input safety: what is stored where, what leaves the device, validation",
    "navigation and information architecture: duplicate entries, dead ends, back behaviour",
    "the owner's own workflow: the three most frequent tasks, measured by clicks",
]


def next_lens(key: str, forced: str = "") -> tuple:
    """Rotate the lens per project so each daily run looks through a new pair of eyes."""
    if forced:
        return forced, -1
    data = load_json(LENSES_FILE, {})
    if not isinstance(data, dict):
        data = {}
    idx = int(data.get(key, 0)) % len(LENSES)
    data[key] = (idx + 1) % len(LENSES)
    save_json(LENSES_FILE, data)
    return LENSES[idx], idx


def tail(text: str, limit: int) -> str:
    return text[-limit:] if len(text) > limit else text


def feedback_text(folder: str) -> str:
    """Owner complaints and requests that touch this project (never AHome private content)."""
    parts = []
    bus = read_text(OPS / "bus" / "ahmed-telegram.md")
    if bus:
        parts.append("Owner Telegram notes (newest last):\n" + tail(bus, 3000))
    ledger = read_text(OPS / "OWNER_REQUEST_LEDGER.md")
    if ledger:
        parts.append("Owner request ledger:\n" + tail(ledger, 2000))
    for pattern in (".sir/*FEEDBACK*.md", ".sir/OWNER*.md", ".sir/feedback/*.md"):
        for path in sorted(Path(folder).glob(pattern)):
            parts.append(f"{path.name}:\n" + tail(read_text(path), 1500))
    return "\n\n".join(parts) or "No owner feedback files found."


def git_lines(folder: str, args: list) -> str:
    import subprocess
    try:
        res = subprocess.run(["git", "-C", folder] + args, capture_output=True, text=True, timeout=60)
        return (res.stdout or res.stderr or "").strip()
    except (OSError, subprocess.TimeoutExpired):
        return ""


def build_prompt(key: str, lens: str) -> str:
    name, folder = PROJECTS[key]
    checkpoint = read_text(Path(folder) / ".sir" / "CHECKPOINT.md")
    commits = git_lines(folder, ["log", "-8", "--oneline"])
    ci = git_lines(folder, ["status", "-sb"]) + "\n" + git_lines(folder, ["log", "-1", "--stat"])
    known = []
    for entry in load_suggestions()[-12:]:
        known.append("- " + entry["fields"].get("Finding", "")[:120] + f" [{entry['fields'].get('Status', 'pending')}]")
    for task in load_queue():
        if not task.get("done"):
            known.append(f"- open task {task.get('name')}: {task.get('title', '')}")
    return f"""You are the daily scout for {name} ({folder}).

Today's lens: {lens}

What you know:
- Checkpoint (newest notes last):
{tail(checkpoint, 4000) if checkpoint else 'NO CHECKPOINT'}

- Recent commits:
{commits or 'NO COMMITS'}

- Working tree and last commit:
{ci or 'NO GIT DATA'}

- Owner feedback that touches this project:
{feedback_text(folder)}

- Shared lessons every project must follow:
{lessons_text()}

- Already known, do not repeat any of these:
{chr(10).join(known) if known else '- nothing recorded yet'}

Do this:
1. Run the app or the project's own commands and test it through today's lens. For a web app, open it headless
   at 390 px and take a screenshot into D:/Projects/_SIR/ops/scout-evidence/. Never leave a browser open.
2. Look for real defects and real improvements only: bug, missing feature, polish, risk, next best idea.
3. Check the shared lessons: every violated lesson is a finding.
4. Do not repeat an item from "Already known". Do not invent data, users, reviews or numbers.
5. For each finding give the exact evidence (screenshot path, command output, file:line) and a short proposed
   brief name in lower case with dashes, like r43-jobs-tabbar-scroll.

Answer with ONLY a JSON array, at most {MAX_FINDINGS} items, no prose around it:
[
  {{"finding": "one sentence, specific", "evidence": "path or command output", "severity": "critical|high|medium|low",
    "category": "bug|feature|polish|risk|idea", "proposed_brief": "r43-project-topic"}}
]
Write [] when you truly found nothing worth fixing.
"""


def parse_findings(output: str) -> list:
    match = re.search(r"\[.*\]", output, re.DOTALL)
    if not match:
        return []
    try:
        data = json.loads(match.group())
    except ValueError:
        return []
    if not isinstance(data, list):
        return []
    clean = []
    for row in data:
        if not isinstance(row, dict):
            continue
        finding = str(row.get("finding", "")).strip()
        if len(finding) < 12:
            continue
        clean.append({
            "finding": finding,
            "evidence": str(row.get("evidence", "")).strip(),
            "severity": str(row.get("severity", "medium")).strip().lower(),
            "category": str(row.get("category", "polish")).strip().lower(),
            "proposed_brief": re.sub(r"[^a-z0-9-]+", "-", str(row.get("proposed_brief", "")).lower()).strip("-"),
        })
    return clean[:MAX_FINDINGS]


def append_findings(key: str, findings: list) -> tuple:
    """Add new findings to ops/SUGGESTIONS.md. Returns (added, dropped)."""
    name = PROJECTS[key][0]
    entries = load_suggestions()
    existing = {entry["id"] for entry in entries}
    added, dropped = 0, 0
    stamp = time.strftime("%Y-%m-%dT%H:%M")
    for row in findings:
        if is_rejected(row["finding"]) or is_duplicate(row["finding"], row["proposed_brief"]):
            dropped += 1
            continue
        sid = suggestion_id(row["finding"])
        if sid in existing:
            dropped += 1
            continue
        entry = {
            "header": f"{stamp} | {name} | {row['severity']}",
            "fields": {
                "Finding": row["finding"],
                "Evidence": row["evidence"] or "no evidence given",
                "Proposed Brief": row["proposed_brief"] or "",
                "Project": name,
                "Severity": row["severity"],
                "Category": row["category"],
                "Status": "pending",
                "Id": sid,
            },
            "extra": [],
            "id": sid,
        }
        entries.append(entry)
        existing.add(sid)
        added += 1
    if added:
        rewrite_suggestions(entries)
    return added, dropped


def run_project(key: str, dry: bool, forced_lens: str = "") -> dict:
    if key not in PROJECTS:
        return {"project": key, "status": "unknown-project"}
    name, folder = PROJECTS[key]
    if not Path(folder).is_dir():
        log(NAME, f"{key}: folder missing {folder}")
        return {"project": key, "status": "missing-folder", "folder": folder}
    lens, idx = next_lens(key, forced_lens)
    prompt = build_prompt(key, lens)
    if dry:
        return {"project": key, "status": "dry", "lens": lens, "prompt_chars": len(prompt)}
    pick = pool_pick()
    if not pick:
        log(NAME, f"{key}: no free model available")
        return {"project": key, "status": "no-model", "lens": lens}
    log(NAME, f"{key}: lens {idx} with {pick}")
    code, out, log_file = run_agent(pick, prompt, folder, f"scout-{key}")
    findings = parse_findings(out)
    added, dropped = append_findings(key, findings)
    log(NAME, f"{key}: {len(findings)} found, {added} added, {dropped} dropped, exit {code}, log {log_file}")
    return {"project": key, "status": "ran", "lens": lens, "found": len(findings), "added": added,
            "dropped": dropped, "model": pick}


def main(argv: list) -> int:
    if game_mode_active():
        log(NAME, "skip: game mode active")
        print("skip: game mode active")
        return 0
    lower_priority()
    dry = "--dry" in argv
    forced = argv[argv.index("--lens") + 1] if "--lens" in argv else ""
    skip_next = False
    keys = []
    for arg in argv:
        if skip_next:
            skip_next = False
            continue
        if arg == "--lens":
            skip_next = True
            continue
        if arg.startswith("--"):
            continue
        keys.append(arg)
    if "--all" in argv:
        keys = list(PROJECTS)
    if not keys:
        print(__doc__)
        return 2
    for key in keys:
        result = run_project(key, dry, forced)
        print(" ".join(f"{k}={v}" for k, v in result.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
