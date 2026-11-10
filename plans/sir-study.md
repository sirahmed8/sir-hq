# PLAN: SIR Study (Wave 2, private study helper)
Audited 2026-11-10. Replaces: the legitimate parts of the old Obour Institute scripts. Private tool for one owner: not sold, not listed, `noindex`. Commercial items are n/a with the reason below.
Hard rule that never changes: SIR Study never takes graded work for Ahmed. It never submits, never solves a live graded quiz or assignment, never writes a submission, never logs in to submit. It explains, summarizes, quizzes him for practice and plans his week. Ahmed writes every final answer.

## 1. Purpose (plain words)
It turns Ahmed's lecture files into readable study guides, flashcards and practice questions, shows what is due and when exams are, and reminds him on his phone. It teaches; it does not do the work for him.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Study` |
| GitHub (private) | `sirahmed8/sir-study` |
| Runtime | offline HTML study guides in `guides/` (one per subject, PWA with `sw.js`), Python scripts in `scripts/`, local server `scripts/serve.py` on port 3300, scheduled logon task |
| Platforms | local web and PWA on laptop and phone (tailnet): built, unverified. Android/iOS stores, macOS, Linux, TV, watch, extension: skipped, private tool |
| Money | none. Subscription, EGP pricing, legal pack, marketing, SEO: n/a. Default: never sold |

## 3. Current state
Claimed in `.sir/CHECKPOINT.md` (2026-11-10): M0 to M5 closed, 8 audit cycles, study guides for 7 subjects, Telegram exam briefing sent, local explainer with a graded-work refusal eval (10 of 10 refused, 5 of 5 concept questions answered with citations), CI run green. PORTFOLIO.md (2026-11-08): 16 of 33 tasks, 58 commits.
Verified by this audit today: `python scripts/verify_all_buttons_wired.py` on the last guide it prints: all 73 buttons and 37 inline handlers resolve (one guide only). Nothing else re-run; refusal eval and CI are claims, built, unverified.
Built, unverified: 7 subject guides plus `index.html`/`START_HERE.html` with live exam countdown, interactive solver tools for the operations-research guide, print layouts, material index (`scripts/index_materials.py`, `.sir/evidence/materials-index.json`), converters/extractors, sanitized export, backup drill (`scripts/backup_drill.py`), destructive-action dry-run and undo, local AI explainer (`scripts/study_ai_explainer.py`), daily briefing sender (`scripts/send_exam_briefing.py`, uses the shared Telegram sender).
Not started: the app-style screens in the old plan (Courses, Calendar with deadlines from an official iCal feed, Flashcards with spaced repetition, Practice questions with scoring, Notes viewer as one app); a read-only deadline feed; flashcard review scheduling; per-subject coverage proof against the syllabus beyond `guides/COVERAGE.md`; Chinese and Hindi text; auth design beyond the tailnet ADR.

## 4. Security and integrity rules
1. Loopback plus Tailscale identity; no public ingress (`docs/ADR-001-AUTHENTICATION.md`, `docs/THREAT_MODEL.md` exist). Test: a request from a non-allowed host is refused.
2. Read-only institute access only through an official feed (iCal link or a personal read-only token in Credential Manager). A test asserts the code has no HTTP POST to any submit, attempt or quiz endpoint.
3. Integrity guard: the explainer refuses graded work in Arabic and English. Eval set in `.sir/evidence/t-020-t-021-ai-integrity-eval.md`; it must stay at 100 percent refusals and is re-run after any prompt change.
4. Study material and notes never go to an outside AI provider. Local models only.
5. Secrets in Credential Manager or untracked `.env`; gitleaks in CI.
6. Every delete has dry run and undo (done, unverified, `.sir/evidence/t-019-destructive-actions.md`).
7. Telegram reminders contain dates and subject names only, no material text.

## 5. Shared pieces
- Telegram sender: `scripts/deliver/send-telegram.mjs` (shared). Do not build another.
- AI: local models through `_SIR/scripts/ai/ask.ps1` private mode. No SIR Platform ai-proxy needed.
- Design family: share look with Jobs and Laptop Manager until Platform extracts tokens (last wave).
- Auth/billing/legal: not needed.

## 6. Screens and entities
Screens: Today (lectures, deadlines, what to study), Calendar, Courses, Materials library, Notes viewer, Flashcards, Practice (self-test), Exam countdown, Settings and Profile. Entities: Course, Lecture, Material, Deadline, Note, Flashcard, PracticeQuestion, StudySession.
Five states on each, Arabic RTL and English, light/dark/system/contrast, 320 px to 4K, zoom 200 percent, WCAG 2.2 AA, own logo (`guides/logo.svg`, icons exist).

## 7. AI
Summaries, flashcards and practice questions from the lecture text with a citation to the file and page; step-by-step concept explanations; weekly plan. Fallback: local model A, local model B, plain keyword search over the index. Kill switch `STUDY_AI=off`. Support assistant: n/a (single user).

## 8. Operations
Daily briefing and exam reminders via Telegram in simple Arabic. Health line `.sir/health.txt`. Weekly backup via `scripts/backup_drill.py` with a restore check monthly. No public status page.

## 9. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Foundations | `scripts/verify.ps1` green; threat model and ADR exist (they do) |
| M1 | Materials index and deadlines | index lists all course folders; Today shows deadlines from the iCal feed (fixture test + one real read-only fetch) |
| M2 | Converters, flashcards, plan | PDF/DOCX to markdown test; flashcard schedule unit test; reminders fire in a dry run |
| M3 | Security | rules 1, 2, 7 have tests; brute-force n/a (no login) |
| M4 | AI | refusal eval 100 percent and citation eval at or above the stored score |
| M5 | Quality | screenshots at 320/390/768/1440, RTL and LTR; no horizontal scroll |
| M6 | Retirement | old Obour scripts folder moved to `old projects` keeping course materials; recorded |

## 10. Next 10 tasks (each under 2 hours)
1. Run `scripts/verify.ps1` and `scripts/audit_suite.py`, save output. Files: `.sir/evidence/verify-2026-11-10.md`. Check: file has the command and exit code.
2. Re-run the refusal eval from a script (not by hand) and store the score. Files: `scripts/eval_integrity.py`. Check: prints 10/10 refused, exits non-zero otherwise.
3. Test that no code path can POST to submit/attempt endpoints. Files: `tests/test_no_submit.py`. Check: test fails if a `requests.post` to such a path is added.
4. Read-only iCal deadline reader (feed URL in Credential Manager). Files: `scripts/deadlines.py`, `tests/fixtures/sample.ics`. Check: fixture test passes; Today screen lists deadlines.
5. Flashcard model plus spaced-repetition schedule (SM-2 style). Files: `scripts/flashcards.py`, tests. Check: unit tests for interval growth and lapse.
6. Flashcard review screen in `guides/` shell with keyboard answers 1 to 4. Check: screenshot 390 px and a keyboard-only run.
7. Coverage proof: for each subject, list syllabus topics vs guide sections, missing ones listed. Files: `guides/COVERAGE.md` generator. Check: file regenerated, gaps shown.
8. Phone check: open the guide over the tailnet and take a screenshot at 390 px; fix any horizontal scroll. Check: `scrollWidth <= innerWidth`.
9. Telegram reminder format test: no material text in message. Files: `tests/test_briefing_privacy.py`. Check: passes.
10. Push and record the GitHub Actions run URL. Check: green URL in checkpoint.

## 11. Risks and open questions (defaults)
- Institute rules on automated access: default is official feed only, read-only, otherwise manual import.
- Study guides built by AI can contain errors: default is each guide shows its source file and page for every claim, and `verify_accuracy.py` stays in the verify chain.
- Exam period urgency may tempt shortcuts: default is no feature may answer a live graded item; refusals are tested.
- Disk space: materials stay where they are, only an index is built.

## 12. Only the owner can do
Sign in to the institute site to copy his own iCal link or create a read-only token; sign in to Tailscale on his phone; click Submit on any assignment himself.

## 13. Market-grade note
Private study tool: no competitor study needed beyond inspiration (`plans/competitors/sir-study.md` exists; unsourced lines are tagged). No country legal pack. Data in the folder is the owner's course material: do not publish it, do not put it in a public repo.
