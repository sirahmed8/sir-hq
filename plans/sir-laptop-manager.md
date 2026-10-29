# PLAN: SIR Laptop Manager
Status: planned, not started. Wave 4. Replaces: Laptop manager + antigravity-agent-suite. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

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
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Secrets only in Credential Manager/env; deletes always quarantine first; sync script never deletes; no graded-work automation.

## 8. Milestones
### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-laptop-manager`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-laptop-manager` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Laptop Manager", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Dry-run cleanup report + quarantine with manifest and restore, tests.
### M2 Parity with the old project
- [ ] Agent config sync tested on a temp workspace; skills imported after licence audit; routines registered.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] RAG over notes with Arabic + English evals.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Retire both v1 folders; archive suite repo.

## 9. Risks and open decisions
- Global config edits are blocked by the safety classifier: project-scope parity only.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
