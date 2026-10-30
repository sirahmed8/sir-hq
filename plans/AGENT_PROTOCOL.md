# AGENT PROTOCOL: how any AI works on any SIR project (Claude, Codex, OpenCode, Kilo, Antigravity, anyone)

## 1. Start (always, in this order, every chat and after every reset)
1. `D:\Projects\_SIR\NEXT.md` (done / next / only-Ahmed). 2. The project's `.sir/CHECKPOINT.md`. 3. The project's `.sir/PLAN.md` section 8: the first unchecked box is your task. 4. `D:\Projects\AGENTS.md` laws. Read only what the box needs.
## 2. Think like a senior engineer, out loud in files not chat
Before code: write 5 lines in `.sir/CHECKPOINT.md` ("Goal / Approach / Files I will touch / How I will prove it / Risks"). Small steps; one box = one small commit (Conventional Commits). Prefer deleting code over adding it. Ask: what is the simplest design that stays correct under empty, error, offline, slow, concurrent, RTL and huge-data cases?
## 3. Code quality contract (non-negotiable)
- Clean architecture in four layers: presentation (UI), domain (use-cases, rules, no I/O), data (repositories, API clients, DB), core (config, utils). Dependencies point inward only. Domain code has no framework imports.
- TypeScript `strict`, no `any`, zod at every boundary, discriminated unions for state. Python: typed, pydantic v2, ruff + mypy.
- Files under 300 lines, one responsibility each, kebab-case file names, absolute imports (`@/`), no deep relative paths.
- Tests first for domain rules; negative tests for every security rule; e2e for critical journeys. CI green (typecheck, lint, test, build, gitleaks) before a box is ticked.
- No mock data in production paths, no TODO placeholders, no dead buttons, no hype words, no em-dashes in copy.
## 4. Standard folder layout of a product (create it in M0)
```
SIR <Product>/
  apps/web          Next.js on Cloudflare (or Vite SPA)   apps/api   Workers (Hono) if needed
  apps/desktop      Electron/Tauri (if the plan says so)  apps/mobile Expo (if the plan says so)
  packages/core     domain types, zod schemas, rules (no I/O)
  packages/data     repositories, Firestore/D1 access     packages/ui  product UI on @sir/ui
  docs/             architecture.md, decisions/ (ADRs), runbook.md
  scripts/          dev-start.vbs, dev-stop.vbs, verify.ps1
  .sir/             PLAN.md, CHECKPOINT.md, BOARD.md, project.yml, evidence/
  folder.ico  desktop.ini  AGENTS.md  CLAUDE.md  GEMINI.md  README.md
```
## 5. Evidence and honesty
A box is ticked only with evidence saved in `.sir/evidence/` (command output file or screenshot) and one line in the checkpoint. Report failures and unknowns plainly. Never present a guess as a fact.
## 5b. Computer use, mods and talking to other projects
Use the computer for any task and work out how (`plans/COMPUTER_USE.md`). Read `plans/MAIN_PLAN.md`; message other projects in `ops/bus/<slug>.md` and live with ListAgents/SendMessage. The dashboard mods in `_SIR/mods` are shared: improve them or add a pane for your project there.
## 6. Blocked?
Never ask Ahmed. If a permission or classifier blocks an action: finish everything else, put the single command in `D:\Projects\_SIR\ops\OWNER_ACTIONS.md`, and continue with the next box. Never work around a refusal.
## 7. End (always)
Update the checkpoint (Now / Next step with the exact command or file / Open promises / Re-read list), append one line to `_SIR/ops/MISSION_LOG.md`, commit, push straight to `main` of the private repo (Ahmed, 2026-10-30: no pull requests, ever). Then stop.
## 8. Never (Tier 3)
Leak secrets; bypass CAPTCHAs, 2FA or platform security; fake reviews/followers; engagement bots; script X's website; make payments; pose as Ahmed; do graded work for him; expose SIR Home data.
