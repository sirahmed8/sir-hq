# PLAN: SIR Obour Hub
Status: planned, not started. Wave 5. Replaces: Obour Academic Hub. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- Obour Academic Hub
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
A study platform for Obour Higher Institutes computer science students: notes, past exams, quizzes, Q&A, study planner and an AI tutor that explains and quizzes but never does graded work. Audience: Ahmed's classmates first, then other Egyptian institutes.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Obour Hub` |
| GitHub (private) | `sirahmed8/sir-obour-hub` |
| Firebase project / OAuth app name | `sir-obour-hub` / "SIR Obour Hub" |
| Cloudflare project | `sir-obour-hub` (`sir-obour-hub.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-obour-hub` (Android, iOS, Windows) |
| Platforms | Web + PWA (Cloudflare), later Android/iOS via Expo |
| Money | Free tier covers notes, exams and 5 AI questions a day; Pro in EGP for unlimited AI, offline packs and exam simulator (Launching Soon fallback until Paymob keys exist) |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- Old app is the closest to shippable (CI, 47 tests, httpOnly session) but has `allow read: if true` on 5 Firestore collections, CSP unsafe-inline/eval, 24+ files over 530 lines and analytics before consent.
- It ships `solve_assignment` and `solve_quiz` modes plus fabricated fallback solutions: graded work, removed in the rebuild.
- Firebase ids `obourinstitutes1` show on login today.

## 4. What to port from the old project
- Content model and subjects/exams/sections data (export from Firestore, dry-run import with counts).
- Rate-limit design (Upstash) as Workers KV limiter; CI backup workflow idea (daily Firestore export).
- Pages: main, subject, exams, quiz, qa, todo, market, alumni, pricing, admin.

## 5. Screens and entities
**Screens:** Landing, Sign in, Home (today plan), Subject, Lecture notes viewer, Exams, Quiz runner, Q&A, Study planner, AI tutor, Pricing, Profile, Settings, Admin/Owner dashboard, Help center, Legal
**Entities:** User, Subject, Lecture, Note, Exam, Question, QuizAttempt, Thread, Reply, StudyTask, Subscription, AiUsage
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Flagship: AI tutor that explains a lecture, makes practice questions and gives hints with sources from the uploaded notes. Hard rule: no full solutions to graded assignments or live quizzes; refuses and offers hints instead. Assistant: grounded support bot. Free provider chain via SIR Platform.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Firestore read rules per collection (signed-in, published only); admin only by custom claim.
- Analytics only after consent.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-obour-hub`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-obour-hub` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Obour Hub", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Sign in with Google (brand check), Subject list, Lecture notes viewer, Quiz runner with real persisted attempts.
- [ ] Cloudflare deploy at `sir-obour-hub.pages.dev` with preview per branch.
### M2 Parity with the old project
- [ ] Import subjects/exams/notes with a dry run and record counts matching the old DB.
- [ ] Q&A, study planner, alumni and market pages; admin dashboard with real counts only (no simulated data).
- [ ] Pricing page with EGP plans and the Launching Soon fallback.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] AI tutor with source citations, hint ladder (hint 1/2/3 then explanation), quota badge '3 / 5 free questions today'; eval set proving it refuses to write a submission.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Redirect old `obourinstitutes1.web.app` to the new domain after parity; export old data once more; move `Obour Academic Hub` to `old projects`.
- [ ] Announce to classmates only when real content exists.

## 9. Risks and open decisions
- Content copyright: only publish notes Ahmed or classmates own; no copied course PDFs.
- Paymob needs a business account (owner action); fallback covers the gap.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
