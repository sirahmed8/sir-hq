"""HQ Verifier (secretary): proves every task the autopilot marked done.

For every done task with no file in ops/verifications/, it picks one free model from the shared pool and
runs a verification prompt built from that task's own checklist: run the tests, read CI status, open the app
headless, take a screenshot at 390 px, then compare the result with each numbered item and write
ops/verifications/<task>.md with PASS/FAIL per item and an evidence path per PASS.

Rules:
  - Nothing is ever marked verified without evidence. A PASS row with an empty evidence cell is rewritten to
    FAIL by this script itself, whatever the model wrote.
  - FAIL items become a new fix task <task>-fix1 in the autopilot queue (brief + prompt file included).
  - AHome: only source under apps/, tests and screenshots of the running app. Never messages, notes, photos, vault.

Usage: python hq_verifier.py [--task NAME] [--limit N] [--dry]
Exit code 0 when the run itself worked (even if a task FAILed); 1 on a setup problem.
"""
import nowindow  # noqa: F401  (no console windows for child processes)
import re
import sys
from pathlib import Path

from hq_team import (OPS, PROJECTS, QUEUE_ADD, ROOT, game_mode_active, lessons_text, load_queue, log,
                     lower_priority, pool_pick, read_text, run_agent)

VERIFICATIONS = OPS / "verifications"
SHOTS = VERIFICATIONS / "evidence"
NAME = "verifier"
MIN_EVIDENCE = 4


def checklist_files(task_name: str, folder: str) -> list:
    """Files the verifier must check the task against: the task brief and any project checklist."""
    found = []
    brief = OPS / "briefs" / f"{task_name}.md"
    if brief.exists():
        found.append(brief)
    project = Path(folder)
    for pattern in (".sir/*CHECKLIST*.md", ".sir/*_CHECKLIST.md", ".sir/plans/*CHECKLIST*.md"):
        for path in sorted(project.glob(pattern)):
            if path not in found:
                found.append(path)
    # keep the checklists that mention this task, plus the newest one when none does
    token = task_name.split("-")[0]
    matching = [p for p in found if token.lower() in p.name.lower() or token.lower() in read_text(p)[:4000].lower()]
    return matching or found[:1]


def build_prompt(task: dict, checklists: list) -> str:
    name, folder, title = task["name"], task["folder"], task.get("title", task["name"])
    checklist_block = "\n".join(f"- {p}" for p in checklists) or "- (no checklist file found: use the brief items)"
    return f"""You are the SIR verifier for task {name} ({title}).

CI RULE: if the file D:/Projects/_SIR/ops/ci-quota-exhausted.flag exists, GitHub Actions minutes are used up and every CI job ends in about 3 seconds with zero steps. For the checklist item about CI being green, do NOT mark FAIL for that reason: mark it PASS only if the same commit passes the full LOCAL verification you run yourself (tests, lint, build), and write 'CI blocked by the Actions quota, local verification passed' in the evidence column. If local verification fails, mark FAIL as usual.
Project folder: {folder}
Project key: {project_key(folder)}

Prove whether this task is really done. You are the one who stops a false "done".

Steps:
1. Read the checklist and the task brief listed below. Number every item exactly as it is numbered there.
2. Run the project's own checks (tests, lint, type check, build) and paste the real command output.
3. Read CI: `gh run list --limit 3` in the project folder. A red run is a FAIL for the CI item.
4. If it is a web app, serve or open it headless, take a screenshot at 390 px wide, and look at it.
   Save screenshots to {SHOTS}
5. Compare what you saw and ran with each numbered item. Mark PASS only when you have a command output,
   a CI run id or a screenshot path as proof. Otherwise FAIL with the exact reason.
6. Check the shared lessons below against the touched screens; a violated lesson is a FAIL item.

Shared lessons every project must follow:
{lessons_text()}

Checklist and brief files:
{checklist_block}

Write the file {VERIFICATIONS / (name + '.md')} in exactly this shape:

# Verification: {name}

## Checklist Results
| Item | Description | PASS/FAIL | Evidence |
|------|-------------|-----------|----------|
| 1 | <item as written in the checklist> | PASS | <command, CI run id or screenshot path> |
| 2 | <item> | FAIL | <exact reason and what is missing> |

## Overall: PASS
(or "## Overall: FAIL" when any item is FAIL)

## Notes
<short facts: what you ran, what you could not check, what the fix task must do>

Never write PASS with an empty Evidence cell. Never invent a run id, a test result or a screenshot.
AHome: only read source under apps/, tests, and screenshots of the running app. Never read messages, notes,
photos or the vault.
"""


def project_key(folder: str) -> str:
    norm = folder.replace("\\", "/").lower()
    for key, (_name, path) in PROJECTS.items():
        if path.lower() == norm:
            return key
    return "sir-hq" if norm.rstrip("/").endswith("_sir") else "unknown"


def parse_rows(text: str) -> list:
    """Return [{item, description, verdict, evidence}] from the checklist table."""
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        verdict = cells[2].upper()
        if verdict not in ("PASS", "FAIL"):
            continue
        rows.append({"item": cells[0], "description": cells[1], "verdict": verdict,
                     "evidence": " | ".join(cells[3:]).strip()})
    return rows


def enforce_evidence(text: str) -> tuple:
    """Downgrade every PASS without evidence to FAIL. Returns (new_text, changed_count, rows)."""
    rows = parse_rows(text)
    changed = 0
    out_lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cells) >= 4 and cells[2].upper() == "PASS":
                evidence = " | ".join(cells[3:]).strip()
                if len(evidence) < MIN_EVIDENCE or evidence in ("-", "none", "n/a"):
                    cells[2] = "FAIL"
                    cells[3] = "no evidence given by the verifier (downgraded automatically)"
                    line = "| " + " | ".join(cells) + " |"
                    changed += 1
        out_lines.append(line)
    new_text = "\n".join(out_lines)
    if changed:
        rows = parse_rows(new_text)
        fails = [r for r in rows if r["verdict"] == "FAIL"]
        overall = "FAIL" if fails else "PASS"
        new_text = re.sub(r"(?m)^## Overall:.*$", f"## Overall: {overall}", new_text)
        note = (f"\n\n## Verifier notes\n{changed} PASS row(s) had no evidence and were downgraded to FAIL "
                f"by scripts/hq_verifier.py. Nothing is verified without proof.\n")
        if "## Verifier notes" not in new_text:
            new_text += note
    return new_text, changed, rows


def overall_of(text: str, rows: list) -> str:
    m = re.search(r"(?m)^## Overall:\s*(PASS|FAIL)", text)
    if not rows:
        return "FAIL"
    if m:
        return m.group(1)
    return "FAIL" if any(r["verdict"] == "FAIL" for r in rows) else "PASS"


def write_fix_task(task: dict, rows: list, verification_file: Path) -> str:
    """Create <task>-fix1 with a real brief + prompt file so the autopilot can run it."""
    fix_name = f"{task['name']}-fix1"
    if any(t.get("name") == fix_name for t in load_queue()):
        return "already queued"
    failed = [r for r in rows if r["verdict"] == "FAIL"]
    if not failed:
        return "no failures"
    lines = [f"- Item {r['item']}: {r['description']} -> {r['evidence']}" for r in failed]
    brief = OPS / "briefs" / f"{fix_name}.md"
    brief.parent.mkdir(parents=True, exist_ok=True)
    brief.write_text(
        f"Fix every item that failed verification of {task['name']}.\n\n"
        f"Verification file: {verification_file}\n"
        f"Project: {task['folder']}\n\n"
        "Failed items:\n" + "\n".join(lines) + "\n\n"
        "Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. "
        "Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. "
        "Run the project's checks and CI until green, commit and push to main, update the project checkpoint, "
        "and write a short report with the real command output.\n",
        encoding="utf-8")
    import subprocess
    res = subprocess.run([sys.executable, str(QUEUE_ADD), fix_name, str(brief), task["folder"],
                          f"Fix failures from {task['name']} verification"], capture_output=True, text=True,
                         timeout=180)
    log(NAME, f"fix task {fix_name}: {(res.stdout or res.stderr).strip()[:160]}")
    return "queued" if res.returncode == 0 else "queue-add failed"


def verify_task(task: dict, dry: bool) -> dict:
    name = task["name"]
    result = {"task": name, "status": "skipped", "model": "", "reason": ""}
    checklists = checklist_files(name, task["folder"])
    prompt = build_prompt(task, checklists)
    if dry:
        result.update(status="dry", reason=f"would verify with checklist {[str(p) for p in checklists]}")
        return result
    pick = pool_pick()
    if not pick:
        result.update(status="no-model", reason="every free model is cooling down")
        log(NAME, f"{name}: no free model available")
        return result
    result["model"] = pick
    log(NAME, f"verifying {name} with {pick}")
    pdir = VERIFICATIONS / "_prompts"
    pdir.mkdir(parents=True, exist_ok=True)
    pfile = pdir / f"{name}.txt"
    pfile.write_text(prompt, encoding="utf-8")
    short = f"Read the file {pfile} completely and do exactly what it says. Write the result file it asks for."
    code, out, log_file = run_agent(pick, short, ROOT, f"verifier-{name}")
    result["log"] = str(log_file)
    target = VERIFICATIONS / f"{name}.md"
    if not target.exists():
        result.update(status="no-file", reason=f"model wrote no verification file (exit {code})")
        log(NAME, f"{name}: no verification file, exit {code}, output {out[-200:]!r}")
        return result
    text = read_text(target)
    fixed_text, changed, rows = enforce_evidence(text)
    if changed:
        target.write_text(fixed_text, encoding="utf-8")
        text = fixed_text
    if not rows:
        result.update(status="invalid", reason="verification file has no PASS/FAIL table")
        log(NAME, f"{name}: verification file has no table")
        return result
    overall = overall_of(text, rows)
    result["overall"] = overall
    result["items"] = len(rows)
    result["fails"] = [r["item"] for r in rows if r["verdict"] == "FAIL"]
    if overall == "FAIL":
        result["fix"] = write_fix_task(task, rows, target)
    result["status"] = "verified"
    log(NAME, f"{name}: {overall} {len(rows)} items, {len(result['fails'])} fail, downgraded {changed}")
    return result


def main(argv: list) -> int:
    VERIFICATIONS.mkdir(parents=True, exist_ok=True)
    SHOTS.mkdir(parents=True, exist_ok=True)
    if game_mode_active():
        log(NAME, "skip: game mode active")
        print("skip: game mode active")
        return 0
    lower_priority()
    dry = "--dry" in argv
    only = ""
    limit = 2
    if "--task" in argv:
        only = argv[argv.index("--task") + 1]
    if "--limit" in argv:
        limit = int(argv[argv.index("--limit") + 1])

    todo = []
    for task in load_queue():
        if not task.get("done") or not task.get("folder"):
            continue
        if only and task.get("name") != only:
            continue
        if (VERIFICATIONS / f"{task['name']}.md").exists():
            continue
        if "AHome" in task.get("folder", ""):
            continue  # private: never to an outside model; local-only verification is not wired yet
        todo.append(task)
    todo.reverse()  # newest finished rounds first
    if not todo:
        log(NAME, "nothing to verify")
        print("nothing to verify")
        return 0

    results = []
    for task in todo[:limit]:
        results.append(verify_task(task, dry))
    for row in results:
        print(f"{row['task']}: {row['status']} {row.get('overall', '')} {row.get('reason', '')}".strip())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
