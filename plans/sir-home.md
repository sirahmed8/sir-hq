# PLAN: SIR Home
Status: planned, not started. Wave 4. Replaces: AHome (AhmedAndHabiba). Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- AHome (moves in when SIR Home replaces it, daemons stopped)
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
Private home app for Ahmed and Habiba: shared calendar, notes, dates, reminders, local AI assistant and Telegram/phone bridge. Two users only. Never public, never sold, no subscriptions.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Home` |
| GitHub (private) | `sirahmed8/sir-home` |
| Firebase project / OAuth app name | `sir-home-private` / "SIR Home" |
| Cloudflare project | `sir-home` (`sir-home.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-home` (Android, iOS, Windows) |
| Platforms | Local core (FastAPI on 127.0.0.1) + PWA for phones through a private tunnel; Windows daemons |
| Money | none |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- Secrets in `.env.local` and 4 commits of history; `apps/web/package-lock.json` corrupt; security headers file ignored by Vercel; CSP and 87 lint errors open; old folder name already retired, daemons hardcode paths.

## 4. What to port from the old project
- local-core services, Telegram gateway, firebase bridge, web push delivery, web app screens.

## 5. Screens and entities
**Screens:** Today, Calendar, Notes, Dates, Reminders, Assistant, Settings
**Entities:** Person(2), Event, Note, Reminder, Message, Device
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Local models only (Ollama); nothing leaves the house network.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Only two allow-listed Google accounts; tunnel behind Cloudflare Access; backups encrypted; nothing from this project is ever sent to outside AI providers or listed in public profiles.

## 8. Milestones
### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-home`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-home-private` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Home", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Rename folder to `SIR Home` with daemons stopped (script like `ahome-retire-old-path.ps1`), keep supervisor working, verify port 8090.
### M2 Parity with the old project
- [ ] Rebuild web app on the SIR UI kit; regenerate lockfile; fix CSP and lint.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Local assistant over notes with delete controls.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Rotate Telegram/Firebase/Gemini keys; purge secrets from history after rotation.

## 9. Risks and open decisions
- Private data: never use outside AI; never add to the public portfolio.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
