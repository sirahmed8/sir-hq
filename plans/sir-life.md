# PLAN: SIR Life
Status: planned, not started. Wave 4. Replaces: nothing (new, from Ahmed's TickTick ideas). Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 1. Mission and audience
A calm daily-life app for a Muslim student, Arabic first and local-first: prayer-aware routine and tasks, adhkar and Quran wird, habits, medication and water reminders, diet and calories, gym log, expenses, skill plans.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Life` |
| GitHub (private) | `sirahmed8/sir-life` |
| Firebase project / OAuth app name | `sir-life` / "SIR Life" |
| Cloudflare project | `sir-life` (`sir-life.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-life` (Android, iOS, Windows) |
| Platforms | Expo (Android, iOS), PWA |
| Money | All core modules free; Pro in EGP only for cloud sync and backup; Launching Soon fallback |

## 3. Why rebuild (evidence from the Phase 3 inventories)
New product; the 30 TickTick ideas collapse into modules of this app and of SIR Obour Hub / SIR Business (see `ops/TICKTICK_MAP.md`).

## 4. What to port from the old project
nothing; prayer data from verified sources (UmmahAPI, Tarteel, quranmajeed connectors).

## 5. Screens and entities
**Screens:** Today, Prayer times, Tasks, Habits, Water/Meds, Food, Gym, Expenses, Skills, Settings
**Entities:** PrayerDay, Task, Habit, Reminder, FoodEntry, Workout, Expense, SkillPlan
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Optional meal and routine suggestions, local first; health data never leaves the device without consent.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Health data encrypted on device; export and delete everything in one tap.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-life`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-life` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Life", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Today screen with prayer times, tasks, habit checks, water counter; offline; tests for prayer-time and habit logic.
### M2 Parity with the old project
- [ ] Remaining modules one at a time.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Suggestions with evals; off by default.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Store builds when accounts exist (free stores first).

## 9. Risks and open decisions
- Religious content accuracy: cite sources, no invented rulings.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
