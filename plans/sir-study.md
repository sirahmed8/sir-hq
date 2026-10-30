# PLAN: SIR Study
Status: planned, not started. Wave 5. Replaces: the legitimate parts of the Obour Institute scripts (materials download, convert, study portal, briefings). Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

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
- Data stays on Ahmed's machine; nothing about the people involved goes to any outside AI provider, repo, log or artifact (AHome: everything about Habiba stays private).
- Secrets only in Windows Credential Manager or an untracked `.env` outside git; gitleaks clean in CI and pre-commit; licence audit.
- Login is required on every surface, never optional: two named accounts only, passkey (WebAuthn) or a strong password plus TOTP, sessions in HttpOnly + Secure + SameSite=Strict cookies, rate limit and lockout, server-side check on every route, a device allow-list for phones. An unauthenticated request gets 401 (tested). Anyone who finds the address still sees nothing.
- Local server binds to 127.0.0.1 only; any phone access goes through the private tunnel with auth; no public ingress; threat model written and tested.
- Every destructive action has a dry run and an undo (quarantine); data directory snapshot and restore drill recorded before the first change.
- Input validated at every boundary (pydantic or zod); subprocess and file paths never built from raw input.
- Credentials never stored in scripts: Moodle access by an official feature only (calendar iCal feed or a personal web-service token kept in Windows Credential Manager); read-only scopes; no form posts to submit/attempt endpoints (test asserts none exist).
- Data local; no study material sent to outside AI providers.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-study`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] Data and secrets layout: data directory and `.env` outside git, backup copy to `D:/Projects/Backups`, snapshot and restore drill saved in `.sir/evidence/`.
- [ ] Threat model and privacy data map (what may leave the machine: nothing private) written in `docs/`.
- [ ] Authentication design: two named accounts, passkey or password plus TOTP, sessions, lockout, device allow-list, phone access only through a private tunnel with its own identity check (Cloudflare Access limited to the two accounts, or Tailscale; verify current terms first); written as an ADR before any code.
- [ ] Local verify: lint, typecheck, tests, gitleaks in one command and in CI; first green run.
### M1 Core slice
- [ ] Materials index of the existing course folders; deadline calendar from the iCal feed; Today screen; tests.
### M2 Parity with the old project
- [ ] Converters (PDF/DOCX to markdown), flashcards and practice questions, weekly plan, reminders to phone (Telegram or push) without private content.
### M3 Security and reliability
- [ ] Security checklist above is green with tests (no public bind, no route answers without a valid session, brute force locks out, bad input, path traversal, secret scan).
- [ ] Backup, restore and rollback runbook tested once; `doctor` command prints health in one screen.
- [ ] Dry-run and undo for every destructive action, tested.
### M4 AI
- [ ] Local summarizer and explainer with source citations; eval set where the correct behavior is to refuse graded work.
### M5 Quality sweep
- [ ] Every screen or command has first-use, loading, empty, error and populated states; Arabic and English text correct; keyboard use complete; accessibility checked where there is a UI; performance budget recorded.
### M6 Release and retirement
- [ ] Move the study portal scripts here; retire the old Obour Institute scripts folder to `old projects` keeping the course materials.

## 9. Risks and open decisions
- Institute rules on automated access: read-only, official feeds only.
- Disk space: materials stay where they are, index only.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
