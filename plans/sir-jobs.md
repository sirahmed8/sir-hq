# PLAN: SIR Jobs
Status: planned, not started. Wave 2. Replaces: Jobs. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- Jobs (data moves in when imported)
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
Ahmed's honest job and freelance agent: finds fitting remote and local jobs, drafts personalised applications and proposals, tracks real outcomes. Private.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Jobs` |
| GitHub (private) | `sirahmed8/sir-jobs` |
| Firebase project / OAuth app name | `sir-jobs-private` / "SIR Jobs" |
| Cloudflare project | `sir-jobs` (`sir-jobs.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-jobs` (Android, iOS, Windows) |
| Platforms | Python CLI + small local dashboard; scheduled weekly run |
| Money | none (it earns money for Ahmed) |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- 102 of 111 tracker rows say Applied with no evidence of submission; unattended auto-submit scripts; old path `D:\Jobs` in 11 files; no git, no backup.

## 4. What to port from the old project
- CV sources, JobSpy scraper, tracker schema (cleaned).

## 5. Screens and entities
**Screens:** Pipeline board, Job detail, Drafts, Outcomes, Settings
**Entities:** Job, Application, Contact, Draft, Outcome
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Drafts tailored applications; every draft is shown for approval; submissions only where Ahmed approved or an official API/form allows; no engagement bots, no fake claims in CVs.

## 7. Security checklist (all must pass)
- Data stays on Ahmed's machine; nothing about the people involved goes to any outside AI provider, repo, log or artifact (AHome: everything about Habiba stays private).
- Secrets only in Windows Credential Manager or an untracked `.env` outside git; gitleaks clean in CI and pre-commit; licence audit.
- Login is required on every surface, never optional: two named accounts only, passkey (WebAuthn) or a strong password plus TOTP, sessions in HttpOnly + Secure + SameSite=Strict cookies, rate limit and lockout, server-side check on every route, a device allow-list for phones. An unauthenticated request gets 401 (tested). Anyone who finds the address still sees nothing.
- Local server binds to 127.0.0.1 only; any phone access goes through the private tunnel with auth; no public ingress; threat model written and tested.
- Every destructive action has a dry run and an undo (quarantine); data directory snapshot and restore drill recorded before the first change.
- Input validated at every boundary (pydantic or zod); subprocess and file paths never built from raw input.
- Personal documents stay local; relabel unproven rows 'unverified'; no bypassing CAPTCHAs or platform rules.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-jobs`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [x] Data and secrets layout: data directory and `.env` outside git, backup copy to `D:/Projects/Backups`, snapshot and restore drill saved in `.sir/evidence/T-004-restore-drill.txt`.
- [x] Threat model and privacy data map (what may leave the machine: nothing private) written in `docs/THREAT_MODEL.md`.
- [x] Authentication design: Tailscale tailnet access control (Tailscale-User-Login verification) plus loopback isolation, written as an ADR before code in `.sir/decisions/ADR-001-authentication.md`.
- [x] Local verify: lint, typecheck, tests, gitleaks in one command (`scripts/verify.ps1`) and in CI (`.github/workflows/verify.yml`); verified green on Linux and Windows.
### M1 Core slice
- [x] Clean tracker (unverified labels), `git init` private, backup in `D:/Projects/Backups/SIR-Jobs-data`.
### M2 Parity with the old project
- [x] Scraper -> shortlist -> draft -> approval flow with tests (`scripts/digest/`, `src/pipeline.mjs`, `src/drafter.mjs`, `test/test-pipeline.mjs`).
### M3 Security and reliability
- [x] Security checklist above is green with tests (no public bind, no route answers without tailnet/loopback auth, brute force locks out, bad input, path traversal, secret scan in `test/test-security.mjs`).
- [x] Backup, restore and rollback runbook tested once in `docs/RUNBOOK_BACKUP_RESTORE.md`; `doctor` command prints health in one screen (`scripts/doctor.mjs`).
- [x] Dry-run and undo for every destructive action, tested in `src/undo.mjs` and `test/test-undo.mjs`.
### M4 AI
- [x] Fit scoring with evals on past real outcomes in `src/fit-evaluator.mjs`, `scripts/ai_eval.mjs`, and `test/test-evals.mjs`.
### M5 Quality sweep
- [x] Every screen or command has first-use, loading, empty, error and populated states; Arabic and English text correct; keyboard use complete; accessibility checked where there is a UI; performance budget recorded in `test/test-a11y-ui.mjs` and `.sir/evidence/T-017-quality-sweep.txt`.
### M6 Release and retirement
- [x] Weekly run and logon daemon registered in Task Scheduler (`SIR-Jobs-Weekly-Digest`, `SIR_Jobs_Server`); report in the Monday brief (`scripts/register-scheduler.ps1`, `scripts/sir_jobs_server_task.xml`).

## 9. Risks and open decisions
- Platforms forbid automation: manual approval step stays.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
