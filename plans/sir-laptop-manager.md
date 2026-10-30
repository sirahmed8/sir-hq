# PLAN: SIR Laptop Manager
Status: planned, not started. Wave 5. Replaces: Laptop manager + antigravity-agent-suite. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- antigravity-agent-suite
- Laptop manager (moves in when replaced)
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
Ahmed's Personal OS: PC care, cleanup with quarantine, routines, the one canonical agent configuration (agents, skills, rules) synced to every AI tool, local RAG and automations. Internal tool, not sold.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Laptop Manager` |
| GitHub (private) | `sirahmed8/sir-laptop-manager` |
| Firebase project / OAuth app name | `sir-laptop-manager` / "SIR Laptop Manager" |
| Cloudflare project | `sir-laptop-manager` (`sir-laptop-manager.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-laptop-manager` (Android, iOS, Windows) |
| Platforms | Windows (PowerShell + Python + small desktop UI); private repo |
| Money | none (internal) |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- A Telegram bot token is hard-coded in 5 tracked files; cleaners delete without quarantine; an academic automation script conflicts with the graded-work rule; skills in antigravity-agent-suite (97) are synced nowhere and mix licences.

## 4. What to port from the old project
- agent-config (18 agents, rules, sync script), local-ai RAG, PC cleaner logic, storage watchdog, the 97 skills after a licence audit.

## 5. Screens and entities
**Screens:** Dashboard (disk, startup, health), Cleanup (dry run -> quarantine), Routines, Agent config sync, Local AI (RAG), Settings
**Entities:** CleanupPlan, QuarantineItem, Routine, AgentProfile, Skill, SyncRun
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Local models only for private text; routine briefs; skill discovery.

## 7. Security checklist (all must pass)
- Data stays on Ahmed's machine; nothing about the people involved goes to any outside AI provider, repo, log or artifact (AHome: everything about Habiba stays private).
- Secrets only in Windows Credential Manager or an untracked `.env` outside git; gitleaks clean in CI and pre-commit; licence audit.
- Login is required on every surface, never optional: two named accounts only, passkey (WebAuthn) or a strong password plus TOTP, sessions in HttpOnly + Secure + SameSite=Strict cookies, rate limit and lockout, server-side check on every route, a device allow-list for phones. An unauthenticated request gets 401 (tested). Anyone who finds the address still sees nothing.
- Local server binds to 127.0.0.1 only; any phone access goes through the private tunnel with auth; no public ingress; threat model written and tested.
- Every destructive action has a dry run and an undo (quarantine); data directory snapshot and restore drill recorded before the first change.
- Input validated at every boundary (pydantic or zod); subprocess and file paths never built from raw input.
- Secrets only in Credential Manager/env; deletes always quarantine first; sync script never deletes; no graded-work automation.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-laptop-manager`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] Data and secrets layout: data directory and `.env` outside git, backup copy to `D:/Projects/Backups`, snapshot and restore drill saved in `.sir/evidence/`.
- [ ] Threat model and privacy data map (what may leave the machine: nothing private) written in `docs/`.
- [ ] Authentication design: two named accounts, passkey or password plus TOTP, sessions, lockout, device allow-list, phone access only through a private tunnel with its own identity check (Cloudflare Access limited to the two accounts, or Tailscale; verify current terms first); written as an ADR before any code.
- [ ] Local verify: lint, typecheck, tests, gitleaks in one command and in CI; first green run.
### M1 Core slice
- [ ] Dry-run cleanup report + quarantine with manifest and restore, tests.
### M2 Parity with the old project
- [ ] Agent config sync tested on a temp workspace; skills imported after licence audit; routines registered.
### M3 Security and reliability
- [ ] Security checklist above is green with tests (no public bind, no route answers without a valid session, brute force locks out, bad input, path traversal, secret scan).
- [ ] Backup, restore and rollback runbook tested once; `doctor` command prints health in one screen.
- [ ] Dry-run and undo for every destructive action, tested.
### M4 AI
- [ ] RAG over notes with Arabic + English evals.
### M5 Quality sweep
- [ ] Every screen or command has first-use, loading, empty, error and populated states; Arabic and English text correct; keyboard use complete; accessibility checked where there is a UI; performance budget recorded.
### M6 Release and retirement
- [ ] Retire both v1 folders; archive suite repo.

## 9. Risks and open decisions
- Global config edits are blocked by the safety classifier: project-scope parity only.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
