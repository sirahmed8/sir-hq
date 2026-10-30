"""Writes the per-project readiness kit into every project folder (idempotent; never touches CHECKPOINT.md, PLAN.md or legacy/).
Run: python D:/Projects/_SIR/plans/generate_kit.py   (after generate_plans.py)"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from products import PRODUCTS  # noqa: E402
from kit_archetypes import ARCH  # noqa: E402
from kit_products_a import A  # noqa: E402
from kit_products_b import B  # noqa: E402
import kit_render as R  # noqa: E402

ROOT = "D:/Projects"
DATA = {**A, **B}
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
OWNER_RULES = [("create the folder|file set|checkpoint|readme", "docs-keeper"), ("firebase|oauth|security|secret|webhook|owner-auth|owner dashboard|security rules|forged|licence", "security-auditor"), ("ci:|ci |release|store|changelog|installer", "release-manager"),
               ("ai |tutor|assistant|eval|prompt|model", "ai-engineer"), ("legal|privacy|cookie|terms", "legal-compliance-counsel"), ("seo|sitemap|structured", "seo-specialist"),
               ("locale|translation|arabic|i18n", "localizer"), ("screen|design|a11y|screenshot|theme|skeleton", "ui-craftsman"), ("test|e2e|lighthouse", "qa-breaker"),
               ("adr|decide|spike|merge matrix|inventory|threat|data map", "architect"), ("android|ios|expo|widget|watch|mobile", "mobile-engineer"),
               ("electron|tauri|installer|desktop|winui", "desktop-engineer")]


def w(path, text, overwrite=True):
    if os.path.exists(path) and not overwrite:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8", newline="\n").write(text.rstrip("\n") + "\n")


def owner(text):
    low = text.lower()
    for pat, ag in OWNER_RULES:
        if re.search(pat, low):
            return ag
    return "builder"


def parse_plan(folder):
    t = io.open(os.path.join(folder, ".sir", "PLAN.md"), encoding="utf-8").read()
    out, cur = [], None
    for ln in t.splitlines():
        m = re.match(r"### (M\d .*)", ln)
        if m:
            cur = [m.group(1), []]
            out.append(cur)
        elif cur and re.match(r"- \[[ x]\] ", ln):
            cur[1].append((ln[3] == "x", ln[6:].strip()))
        elif ln.startswith("## ") and cur:
            cur = None
    return out


SCAN_LEGACY = ("Deep scan first (nobody has done one yet): read `legacy/` (or `materials/`), the old source code you port from and must never delete before M6, plus `D:/Projects/_SIR/ops/inventory/` for each source. "
               "Map features, routes, data models, secrets, licences, dead code and hidden bugs; run gitleaks and a dependency and licence audit; write `.sir/reports/deep-scan.md`; then upgrade PLAN.md, ARCHITECTURE.md and TASKS.md with what you found")
SCAN_NEW = ("Deep scan first: there is no old code here, so scan the other SIR projects' `legacy/` folders and `ops/inventory/` for reusable parts, read the standard modules that apply, benchmark the category leaders, "
            "write `.sir/reports/deep-scan.md`, then upgrade PLAN.md, ARCHITECTURE.md and TASKS.md with what you found")


SCAN_INPLACE = ("Deep scan first (nobody has done one yet): this project is improved in place, so scan this folder itself: map modules, data, daemons and their ports, secrets, licences, dead code and hidden bugs; "
                "run gitleaks and a dependency audit; snapshot the data first; write `.sir/reports/deep-scan.md`; then upgrade PLAN.md, ARCHITECTURE.md and TASKS.md with what you found. Never put anything about the people involved in a repo, log or outside AI")


DESKTOP_TASK = ("Wire the Desktop shortcuts: the folder `Desktop/SIR Projects/<folder name>` has Open, Start dev (green play icon) and Stop dev (red stop icon) shortcuts that run `scripts/dev-start.ps1`, `dev-stop.ps1` and their `.vbs` wrappers; "
                "make them start and stop the real dev command, check each one works, and re-run `D:/Projects/_SIR/scripts/make-icons-and-desktop.ps1` whenever the logo or scripts change")


def build_tasks(slug, plan, has_legacy=True):
    extra = DATA[slug].get("tasks", {})
    n, out, prev = 0, [], None
    for ms, items in plan:
        key = ms.split()[0]
        rows = [(d, x) for d, x in items] + [(False, "(kit) " + x) for x in extra.get(key, [])]
        if key == "M0":
            rows.insert(2 if len(rows) > 2 else 0, (False, "(kit) " + (SCAN_INPLACE if slug == "ahome" else SCAN_LEGACY if has_legacy else SCAN_NEW)))
            rows.append((False, "(kit) " + DESKTOP_TASK))
        cur = []
        for done, text in rows:
            n += 1
            tid = f"T-{n:03d}"
            cur.append(dict(id=tid, done=done, text=text, owner=owner(text), dep=prev if (prev and not done and not cur) else ""))
            if not done:
                prev = tid
        out.append((ms, cur))
    return out


PM_AGENT = """---
name: {slug}-pm
description: Project Manager for {display}. Use at the start of every chat in this folder: reads the kit, plans, writes task specs, delegates, reviews, updates the checkpoint.
tools: Read, Grep, Glob, Bash, Edit, Write, WebFetch, WebSearch, Agent
model: sonnet
---
You are the Project Manager of {display} ({label}).
Start: read `D:/Projects/_SIR/NEXT.md`, `D:/Projects/_SIR/plans/MAIN_PLAN.md`, your inbox `D:/Projects/_SIR/ops/bus/{slug}.md`, `.sir/CHECKPOINT.md`, `.sir/PLAN.md` section 8, then the first unchecked task in `.sir/TASKS.md`. Read `.sir/ARCHITECTURE.md`, `DESIGN.md`, `TEAM.md`, `TOOLKIT.md` when the task needs them.
Delegate always: pick the task level in `D:/Projects/_SIR/plans/MODEL_ROUTING.md` and spawn subagents with `model` and `effort` set (haiku for search and spec-driven work, sonnet for design, review and security, opus only when stuck). Work: write 5 lines in the checkpoint (Goal, Approach, Files, Proof, Risks), split work into task specs, delegate to the agents in TEAM.md with disjoint file ownership, review every diff, keep files under 300 lines, strict typing, tests first for domain rules.
Desktop: your shortcuts live in `Desktop/SIR Projects/<folder>` with their own icons (assets/brand); keep `scripts/dev-start.ps1` and `dev-stop.ps1` correct and re-run `D:/Projects/_SIR/scripts/make-icons-and-desktop.ps1` when the logo changes.
Computer: use the computer, Chrome and apps for any task and work out how (`D:/Projects/_SIR/plans/COMPUTER_USE.md`); never hand Ahmed steps. Mods: `D:/Projects/_SIR/mods` is his dashboard; improve it or add a pane for this project. Other projects: message them in `D:/Projects/_SIR/ops/bus/<slug>.md`.
Legacy: `legacy/` (or `materials/`) is the old source code to port from; never delete or edit it, keep it until M6, then move it to `D:/Projects/old projects/`. Your first task is a deep scan of it and of the plan; improve the plan from what you find.
Rules: commit and push straight to `main` once `verify` passes (no pull requests); never ask Ahmed, put owner-only items in `D:/Projects/_SIR/ops/OWNER_ACTIONS.md`; no mock data, no hype, no secrets in git; legacy/ is read-only.
End: update the checkpoint (Now, Next step with the exact command, Open promises, Re-read list), append a line to `D:/Projects/_SIR/ops/MISSION_LOG.md`, commit, push.
"""
CMD_CONTINUE = """---
description: Continue this project from the checkpoint
---
Read `.sir/CHECKPOINT.md`, then the first unchecked task in `.sir/TASKS.md` (dependencies done). Use the {slug}-pm role: plan in the checkpoint, delegate per `.sir/TEAM.md`, build, prove with `verify` and evidence, tick the task, update the checkpoint, commit and push to `main`. Never ask Ahmed; keep replies short.
"""
CMD_END = """---
description: End the session cleanly
---
Update `.sir/CHECKPOINT.md` (Now, Next step with the exact command or file, Open promises, Re-read list), append one line to `D:/Projects/_SIR/ops/MISSION_LOG.md`, run `verify`, commit and push to `main`, then stop.
"""
ADR_T = """# ADR-000: template
Date: YYYY-MM-DD | Status: proposed | accepted | superseded by ADR-NNN | Deciders: <agent>
## Context
## Options (pros and cons)
## Decision
## Consequences
## Sources checked (with dates)
"""
SECURITY = """# Security

Private project. Report issues to the owner (Ahmed Alaa, @sirahmed8) directly. Secrets never go in git; env var names are listed in `docs/ENV.md`. Owner and admin checks run only on the server. See `.sir/PLAN.md` section 7.
"""
EDITORCFG = "root = true\n\n[*]\ncharset = utf-8\nend_of_line = lf\ninsert_final_newline = true\ntrim_trailing_whitespace = true\nindent_style = space\nindent_size = 2\n\n[*.{py,ps1}]\nindent_size = 4\n\n[Makefile]\nindent_style = tab\n"
AGENTS_BLOCK = """
<!-- SIR-KIT:START -->
## Project kit (generated by HQ, 2026-10-30)
Everything a new chat needs is in `.sir/`: PLAN.md (the contract), TASKS.md (ordered tasks), BOARD.md, ARCHITECTURE.md, DESIGN.md, PLATFORMS.md, PRODUCTION.md, QUALITY.md, BENCHMARK.md, TEAM.md (your sub-agents), TOOLKIT.md (MCPs, skills, CLIs), decisions/, evidence/. Desktop shortcuts: `Desktop/SIR Projects/<folder>` (open, start dev, stop dev, each with its own icon from `assets/brand`); keep `scripts/dev-start.ps1` and `dev-stop.ps1` correct and re-run `D:/Projects/_SIR/scripts/make-icons-and-desktop.ps1` when the logo changes. Slash commands: `/continue`, `/end`. Role: `.claude/agents/{slug}-pm.md`.
Read `D:/Projects/_SIR/plans/MAIN_PLAN.md` and your inbox `D:/Projects/_SIR/ops/bus/{slug}.md`; use the computer for any task (`plans/COMPUTER_USE.md`). Old source code lives in `legacy/` (or `materials/`): read it, port from it, never delete it before M6; your first task is a deep scan and plan upgrade. Rules from Ahmed: HQ never builds products, the project chat does; never open pull requests, commit and push straight to `main` when `verify` passes; repo is private; legacy/ is read-only.
<!-- SIR-KIT:END -->
"""


CHECKPOINT = """# CHECKPOINT: {display}
Updated 2026-10-30 (written by HQ; the project chat owns it from the first session)

## Goal (current phase)
M0 Foundations, in the order of `.sir/TASKS.md`. HQ has finished the setup; nothing is built yet.

## Now
Ready for the first project chat. Private repo `sirahmed8/{repo}` exists with remote `origin`; the kit in `.sir/` is complete.

## Next step (exact)
Run `/continue` (or read `.sir/TASKS.md`): first open task is **{first}**. Then the two after it: {nxt}.

## Done (evidence)
HQ setup: plan, kit (project.yml, TASKS, BOARD, TEAM, TOOLKIT, DESIGN, ARCHITECTURE, PLATFORMS, PRODUCTION, QUALITY, BENCHMARK), `.claude/` PM role and commands, hygiene `.gitignore`, private repo.

## In progress
Nothing.

## Decisions this phase
- No pull requests: commit and push straight to `main` when verify passes (Ahmed, 2026-10-30).
- HQ does not build; this chat does.

## Open promises
None yet.

## Owner actions listed (never blocking)
See `D:/Projects/_SIR/ops/OWNER_ACTIONS.md`.

## Re-read after a reset
`D:/Projects/_SIR/NEXT.md`, `.sir/PLAN.md` section 8, `.sir/TASKS.md`, `.sir/ARCHITECTURE.md`, `.sir/DESIGN.md`
"""


def kit(p):
    slug = p["slug"]
    folder = os.path.join(ROOT, p["folder"])
    if not os.path.isdir(os.path.join(folder, ".sir")) or slug not in DATA:
        print("skip", slug)
        return
    b = DATA[slug]
    a = ARCH[b["arch"]]
    matrix = {**a["platforms"], **b.get("overrides", {})}
    brand = BRAND[slug] if slug in BRAND else dict(color="#475569", mono="AH")
    tasks = build_tasks(slug, parse_plan(folder), any(os.path.isdir(os.path.join(folder, d)) for d in ("legacy", "materials")))
    s = os.path.join(folder, ".sir")
    w(f"{s}/project.yml", R.project_yml(p, a, b, brand, matrix))
    w(f"{s}/TASKS.md", R.tasks_md(p, tasks))
    w(f"{s}/BOARD.md", R.board_md(p, tasks))
    w(f"{s}/TEAM.md", R.team_md(p, a))
    w(f"{s}/TOOLKIT.md", R.toolkit_md(p, a))
    w(f"{s}/DESIGN.md", R.design_md(p, a, b, brand))
    w(f"{s}/ARCHITECTURE.md", R.architecture_md(p, a, b))
    w(f"{s}/PRODUCTION.md", R.production_md(p, a, matrix))
    w(f"{s}/PLATFORMS.md", R.platforms_md(p, matrix))
    w(f"{s}/QUALITY.md", R.quality_md(p, a))
    w(f"{s}/BENCHMARK.md", R.benchmark_md(p, b))
    flat = [t for _, items in tasks for t in items]
    w(f"{s}/status.json", json.dumps(dict(id=slug, version="0.0.0", status="planned", wave=p["wave"], tasksDone=sum(t["done"] for t in flat), tasksTotal=len(flat),
                                          platforms={k: v[0] for k, v in matrix.items()}, ci="none", blockers=[], ownerActions=0), indent=2))
    cp = os.path.join(s, "CHECKPOINT.md")
    if not os.path.isfile(cp) or ("created by HQ" in io.open(cp, encoding="utf-8").read() or "written by HQ" in io.open(cp, encoding="utf-8").read()):
        todo = [x for x in flat if not x["done"]]
        w(cp, CHECKPOINT.format(display=p["display"], repo=p["repo"], first=f"{todo[0]['id']} {todo[0]['text'][:90]}" if todo else "none",
                                nxt=", ".join(x["id"] for x in todo[1:3]) or "none"))
    w(f"{s}/decisions/ADR-000-template.md", ADR_T)
    for d in ("evidence", "reports"):
        w(f"{s}/{d}/.gitkeep", "")
    w(f"{s}/inbox/orchestrator.md", f"# Inbox: orchestrator ({p['display']})\nEscalations and questions from agents go here. Newest first.\n", overwrite=False)
    ctx = dict(slug=slug, display=p["display"], label=a["label"])
    w(f"{folder}/.claude/agents/{slug}-pm.md", PM_AGENT.format(**ctx))
    w(f"{folder}/.claude/commands/continue.md", CMD_CONTINUE.format(**ctx))
    w(f"{folder}/.claude/commands/end.md", CMD_END)
    w(f"{folder}/SECURITY.md", SECURITY, overwrite=False)
    w(f"{folder}/.editorconfig", EDITORCFG, overwrite=False)
    w(f"{folder}/README.md", f"# {p['display']}\n\n{p['mission']}\n\nStatus: planned, not started. Plan: `.sir/PLAN.md`. Owner: Ahmed Alaa. Private repository.\n", overwrite=False)
    ag = os.path.join(folder, "AGENTS.md")
    t = io.open(ag, encoding="utf-8").read() if os.path.isfile(ag) else ""
    t = re.sub(r"\n?<!-- SIR-KIT:START -->.*?<!-- SIR-KIT:END -->\n?", "", t, flags=re.S)
    w(ag, t.rstrip("\n") + "\n" + AGENTS_BLOCK.format(slug=slug))
    print("kit", slug, len(flat), "tasks")


if __name__ == "__main__":
    for prod in PRODUCTS:
        kit(prod)
