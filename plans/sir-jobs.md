# PLAN: SIR Jobs
Status: planned, not started. Wave 4. Replaces: Jobs. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

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
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Personal documents stay local; relabel unproven rows 'unverified'; no bypassing CAPTCHAs or platform rules.

## 8. Milestones
### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-jobs`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-jobs-private` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Jobs", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Clean tracker (unverified labels), `git init` private, backup.
### M2 Parity with the old project
- [ ] Scraper -> shortlist -> draft -> approval flow with tests.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Fit scoring with evals on past real outcomes.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Weekly run registered in Task Scheduler; report in the Monday brief.

## 9. Risks and open decisions
- Platforms forbid automation: manual approval step stays.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
