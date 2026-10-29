# PLAN: SIR Study
Status: planned, not started. Wave 4. Replaces: the legitimate parts of the Obour Institute scripts (materials download, convert, study portal, briefings). Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- materials/obour-year2-term1 (the old Obour Institute study folder)
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
Ahmed's private study organizer: pulls his own lecture materials and deadlines (read-only), converts them to readable notes, builds a weekly plan, reminds him of lectures, quizzes and exam dates, and helps him learn with summaries, flashcards and practice questions. It never logs in to submit anything, never solves graded quizzes or assignments, never writes a submission.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Study` |
| GitHub (private) | `sirahmed8/sir-study` |
| Firebase project / OAuth app name | `sir-study-private` / "SIR Study" |
| Cloudflare project | `sir-study` (`sir-study.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-study` (Android, iOS, Windows) |
| Platforms | Python local engine + small web UI (local) + phone reminders; private |
| Money | none (personal) |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- The old automation mixed legitimate organizing with quiz solving and assignment submission, which is graded work done by a tool and a risk for Ahmed; those files are quarantined in `D:\Quarantine\2026-10-29\moodle-automation`.
- Study materials, notes and the portal scripts are scattered in one big folder.

## 4. What to port from the old project
- From `Obour Institute Second Year 1st term`: download/convert materials scripts, study portal generator, morning briefing, NotebookLM prompt files, course folders structure. Nothing from the quarantine folder.

## 5. Screens and entities
**Screens:** Today (lectures, deadlines, what to study), Calendar, Courses, Materials library, Notes viewer, Flashcards, Practice questions (self-test), Exam countdown, Settings
**Entities:** Course, Lecture, Material, Deadline, Note, Flashcard, PracticeQuestion, StudySession
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Local models first (private): summarize a lecture, make flashcards and practice questions with sources, explain a concept step by step, plan the week. Rule: explanations and hints only; refuses to produce a submission or answer a live graded quiz, and says why.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Credentials never stored in scripts: Moodle access by an official feature only (calendar iCal feed or a personal web-service token kept in Windows Credential Manager); read-only scopes; no form posts to submit/attempt endpoints (test asserts none exist).
- Data local; no study material sent to outside AI providers.

## 8. Milestones
### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-study`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-study-private` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Study", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Materials index of the existing course folders; deadline calendar from the iCal feed; Today screen; tests.
### M2 Parity with the old project
- [ ] Converters (PDF/DOCX to markdown), flashcards and practice questions, weekly plan, reminders to phone (Telegram or push) without private content.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Local summarizer and explainer with source citations; eval set where the correct behavior is to refuse graded work.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Move the study portal scripts here; retire the old Obour Institute scripts folder to `old projects` keeping the course materials.

## 9. Risks and open decisions
- Institute rules on automated access: read-only, official feeds only.
- Disk space: materials stay where they are, index only.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
