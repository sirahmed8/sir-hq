import subprocess, sys

COMMON = (
    "ROUND 11 ADDENDUM FROM THE MANAGER (2026-11-09, owner's new orders). Finish round 10 first, then add these to it, same rules "
    "(charter D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md, version 1.0.0, no emoji, truth rule, verify green, push to main). "
    "1) SETTINGS WINDOW: if the top navigation bar holds several settings-type controls (theme, language, help, density, account, "
    "notifications, tools), move them all into ONE Settings button at the top that opens a small, smooth window (a compact modal or "
    "popover that grows from the button, Dynamic Island style) holding every setting in clear groups. "
    "2) SIDE MENU: if the top bar has many tabs, move them into a simple side menu (drawer on phones, collapsible rail on desktop) "
    "with icon plus label, the active item highlighted; keep at most 4 or 5 top-level items visible on phones. "
    "3) RTL AND LTR: mirror everything correctly (logical CSS properties, mirrored arrows and icons, drawer side, animation "
    "direction, number and punctuation order), test both directions at every size. "
    "4) SELF-IMPROVEMENT: after every change, test and watch it, then improve it again on your own: more and smoother animations "
    "(spring growth like the Dynamic Island), more logic, more backend work (validation, caching, retries, background jobs, data "
    "integrity), more polish in every part of your project, without waiting to be told. "
    "5) CONSOLE WINDOWS: black CMD windows still flash on the owner's screen. Everything your project starts must run hidden "
    "(hidden launchers, pythonw, CREATE_NO_WINDOW, -WindowStyle Hidden, scheduled tasks with hidden actions). Check by watching the "
    "screen during a refresh, and write the proof in the report. "
    "Report to ops/agy-runs/reports/r11-SLUG.md and run agy-done.py r11-SLUG. "
)

EXTRA = {
    "laptop": "Console windows are YOUR top priority (the owner sees them when he opens your site and during games): find and fix every source. ",
    "jobs": "",
    "control": "",
    "study": "",
    "ahome": (
        "UPDATE NOTICE IN THE DYNAMIC ISLAND: when a new app update is available it must appear in the Dynamic Island as a notice. Rules: "
        "show it ONCE per update version; if the user dismisses or chooses later, never show that version's notice again (store the "
        "dismissed version locally); the Update now button and every button of the notice must really work (download and install flow "
        "for Android, reload for the web app, clear states: available, downloading with progress, ready, installing, failed with "
        "retry); spring open and close animation; works in Arabic RTL and English LTR; test with a fake newer version and prove "
        "it with screenshots. Version number stays 1.0.0 for users: use a hidden build id to detect updates. "
    ),
}

for slug, cwd in [("laptop", "D:/Projects/SIR Laptop Manager"), ("jobs", "D:/Projects/SIR Jobs"), ("control", "D:/Projects/_SIR"),
                  ("study", "D:/Projects/SIR Study"), ("ahome", "D:/Projects/AHome")]:
    path = f"D:/Projects/_SIR/ops/briefs/r11-{slug}.md"
    body = f"You are the {slug} chat. " + COMMON.replace("SLUG", slug) + EXTRA[slug]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    subprocess.run([sys.executable, "D:/Projects/_SIR/scripts/agy-task.py", f"r11-{slug}", path, cwd], check=True)

PLANNER = (
    "You are the SIR PLANNER chat (new, owner's order 2026-11-09). Claude's subscription ends in about two weeks and Gemini will work alone, "
    "so you write the plans, instructions and memory that make every later Gemini chat work like a senior team. You do NOT write product code. "
    "STEP 1, UNDERSTAND HOW WE WORK: read D:/Projects/AGENTS.md, D:/Projects/_SIR/START_HERE.md, ops/HQ_CHECKPOINT.md, ops/MISSION_LOG.md, "
    "plans/*.md (especially GEMINI_QUALITY_CHARTER, PERPETUAL_LOOP, IMPROVEMENT_DOCTRINE, ANTIGRAVITY_OPERATOR, USAGE_POLICY, MAIN_PLAN, WAVE_STUDY), "
    "every brief in ops/briefs (*.md), the request ledgers ops/requests/*.md, the reports in ops/agy-runs/reports and the bus files ops/bus. "
    "Write D:/Projects/_SIR/plans/WORKING_METHOD.md: how the owner works (his level, rules, preferences, what he complained about), how the manager, "
    "the chats, operators, quota rotation, reviews and cross-reviews work, and what went wrong before. "
    "STEP 2, THE FOUR BUILT PROJECTS: read AHome (code structure, docs, plans; NEVER open or quote private couple data, local vault, messages, notes, "
    "photos or anything about Habiba's personal life: understand architecture only), SIR Study, SIR Jobs, SIR Laptop Manager, and the Control Room in _SIR. "
    "For each write <project>/.sir/MASTER_PLAN.md: purpose, users, architecture, design identity (its OWN look: colours, type, motion personality, logo), "
    "feature list with state (verified today or not), gaps, and the NEXT 25 TASKS each with files, steps and acceptance checks, ordered by value. "
    "STEP 3, ALL OTHER PROJECTS AND LEGACY: walk every other folder in D:/Projects (SIR AI, SIR Negm Furniture is frozen: plan only, no work, "
    "Obour Academic Hub, Hagoozat and its legacy, 11Players, EGFootball5, Business apps, Content Creation Studio, Controller, Optimizer, ModPack, "
    "GTA mods, Odysseus, Life, Portfolio, the shared kit, every legacy/ folder and old projects). Never delete or move anything. For each project "
    "write plans/<slug>-DEEP.md (or its .sir/MASTER_PLAN.md): what it is, what exists in legacy, what is valuable to port, what is missing, what "
    "OTHER projects need from it or can reuse, dependencies and links between projects, risks, and the first 25 tasks in detail. Also write "
    "plans/PORTFOLIO_LINKS.md: a map of what connects to what and what shared packages or services should exist. "
    "STEP 4, ONE FAMILY, SEPARATE FACES: every site and app gets its own design identity but they share the same qualities: smooth Dynamic-Island "
    "style animation, simple thoughtful interfaces, no complexity, organised, fast, premium, zero glitches, RTL and LTR, every state handled. "
    "Write plans/DESIGN_FAMILY.md with the shared rules and a per-project identity table. Think about everything that could happen and everything "
    "not yet mentioned: missing pieces, edge cases, failure modes, accessibility, offline, security, performance, backups, updates, onboarding. "
    "STEP 5, MEMORY FOR THE MANAGER: write plans/MANAGER_MEMORY.md, a compact (under 400 lines) digest for the Claude manager and for any Gemini "
    "manager: per project one paragraph with state, next 5 tasks, risks and links to the plan files. "
    "The Claude manager will review and improve your plans, so write them complete, concrete and checkable (real file names, real commands). "
    "Use the Haiku-style discipline: small steps, verify files exist after writing. Commit the plan files inside each project repo with "
    "'docs(plan): ...' where the repo exists and push to main (no PRs); _SIR plans go in the sir-hq repo. Version stays 1.0.0. "
    "Write the full report to D:/Projects/_SIR/ops/agy-runs/reports/planner-1.md and run python D:/Projects/_SIR/scripts/agy-done.py planner-1 ok '<one line>'. "
    "Do it in stages and write each document as soon as it is done, so nothing is lost if the quota ends; after each stage write a line to "
    "D:/Projects/_SIR/ops/bus/planner.md."
)
path = "D:/Projects/_SIR/ops/briefs/planner-1.md"
with open(path, "w", encoding="utf-8") as fh:
    fh.write(PLANNER)
subprocess.run([sys.executable, "D:/Projects/_SIR/scripts/agy-task.py", "planner-1", path, "D:/Projects"], check=True)
