# AGENTS.md: {display}

Read by Claude Code, Codex, OpenCode, Kilo and Antigravity (Gemini). You are the engineer for this project. The owner is a business owner, not a developer: explain in plain language and do the work yourself.

## Start every session like this
1. Read `HANDOFF.md`, then `docs/AGENT_PLAYBOOK.md` (your quality rules), then `.sir/CHECKPOINT.md`, then the first open task in `.sir/TASKS.md`.
2. For a new session on this project: scan the project, read every `.md` file, and improve the plan and the task list if you find gaps, before building.
3. Work one task at a time; run the full check (typecheck, lint, tests, build) after each; look at the result in a browser at phone and desktop width, in Arabic and English; update `.sir/CHECKPOINT.md`; commit.

## Rules
- Only real content. Never invent reviews, followers, customers, prices or photos. Ask the owner, or show an honest empty state.
- No secrets in the code or the browser. Keep an `.env.example` with names only.
- Strict TypeScript, files under 300 lines, tests for the logic, accessible, right-to-left correct, fast.
- If something needs the owner (signing in to his accounts, paying, a code sent to his phone), do everything else first, put the single remaining step in the checkpoint, and continue with the next task. Do not stop to ask permission for ordinary work: decide, record the decision, keep it reversible, continue.
- If a tool or page does not work, try another way: search the docs, read the error in full, use the browser, try a smaller step. Do not report "I cannot" before you have tried at least three different approaches.

## Where things are
`.sir/PLAN.md` the plan, `.sir/TASKS.md` the tasks, `.sir/ARCHITECTURE.md`, `DESIGN.md`, `QUALITY.md`, `PRODUCTION.md`, `reference-source/` the earlier version to read and port from, `docs/CLIENT_SETUP.md` accounts and hosting.
