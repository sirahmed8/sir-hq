# PLAN: SIR Obour Hub (Wave 5, public product, not started)
Audited 2026-11-10. Replaces `Obour Academic Hub` (now in `legacy/`, kept until M6). Public product with a free tier and a paid tier in EGP.

## 1. Purpose (plain words)
A study site for students of the Obour Higher Institutes. They find lecture notes, past exam questions and quizzes, see their timetable and lecture hall, work out what grade they need to reach a target GPA, and ask an AI tutor that explains and quizzes but never does graded work. First users: Ahmed's classmates.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Obour Hub` |
| GitHub (private) | `sirahmed8/sir-obour-hub` |
| Stack (default) | Next.js App Router on Cloudflare Pages/Workers, Firebase Auth (Google sign-in, ID token verified on the server with JWKS), Firestore with deny-by-default rules, Cloudflare R2 for files. Note: `.sir/MASTER_PLAN.md` says D1/Supabase; this plan keeps Firebase because the old data is in Firestore and the import is a dry run copy. Manager may overrule; record in an ADR |
| Domain | candidates: `obourhub.com`, `obour-hub.app` (check and buy by owner; price "(unsourced, verify)"). Until then `sir-obour-hub.pages.dev` |
| Platforms | Web and PWA: planned. Android/iOS via Expo: M6+, only after web has real users. Windows, macOS, Linux, TV, watch, car: skipped, no reason. Browser extension: skipped |
| Money | Free: notes, exams, timetable, GPA tool, 5 AI questions per 24 hours. Pro in EGP (price to test, not a fact: start the test at 49 EGP/month and 399 EGP/year, "(unsourced, verify)" with 10 student interviews); shown with USD/SAR toggle. Until Paymob keys exist the button reads "Subscriptions launching soon" with email capture |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is the HQ setup note (2026-10-30, "nothing is built yet"); 40 tracked files, all setup. The project's own `.sir/MASTER_PLAN.md` (a 25-task backlog) exists and describes a different shape (timetable, GPA simulator, grade mirror, book marketplace, D1). Claims in it such as "over 15,000 enrolled students" have no source: "(unsourced, verify)".
Legacy facts (from `ops/inventory/Obour-Academic-Hub.md`, 2026-10-29, nothing re-run): Next 16, React 19, about 344 files / 62k lines, 47 test files not run, `allow read: if true` on 5 collections, CSP with unsafe-inline/eval, analytics loaded before consent, graded-work modes (`solve_assignment`, `solve_quiz`) to be deleted, payments were manual. Two Firebase admin service-account JSON files sit inside `legacy/Obour Academic Hub/` (the folder is git-ignored; both keys must be rotated at launch).

## 4. Security and conduct rules
1. Owner/admin only from a server-verified ID token plus `OWNER_EMAILS`/`OWNER_UIDS`, email verified, fail closed (use `owner-auth` copy). Test: forged token returns 403.
2. Firestore rules deny by default; reads only for signed-in users and published content; tested with the emulator (cross-user read fails).
3. Sessions: HttpOnly, Secure, SameSite=Strict cookie; no localStorage tokens; rate limit on sign-in and AI; 2FA offer for admin.
4. No graded work: the tutor gives hints and explanations only. Eval: 30 prompts in Arabic and English (live quiz, assignment, exam answers), 100 percent refused with a hint offered. `solve_*` code is not ported.
5. No grade-portal scraping and no stored institute passwords. A "grade mirror" is allowed only as a manual entry or a file the student uploads, kept on their account. Default decision: not built in v1.
6. Content: only notes that Ahmed or classmates own and agree to publish; no copied course PDFs; a takedown form exists (DMCA-style).
7. Analytics and trackers load only after consent; Reject All as prominent as Accept.
8. Secrets in env only; gitleaks; keys in `legacy/` rotated.
9. User data deletion and export in one tap each.

## 5. Shared pieces (SIR Platform; do not rebuild)
`owner-auth`, `signed-webhook`, `billing-fallback`, `ai-proxy`, `legal-pack`, `i18n`, `ui/styles/hooks`, Telegram sender. Per MAIN_PLAN these are built as internal `packages/*` here first, with the Platform names and interfaces, then swapped. Obour Hub is the planned first real consumer of the Platform (old plan M6).

## 6. Screens and entities
Landing, Sign in, Home (today plan), Subject, Notes viewer, Exams, Quiz runner, Q&A, Timetable, GPA planner, Study planner, AI tutor, Pricing, Profile, Settings, Owner dashboard, Help center, Legal. Entities: User, Subject, Lecture, Note, Exam, Question, QuizAttempt, Thread, Reply, StudyTask, Subscription, AiUsage, Lead.
Five states everywhere, 1,000+ items paginated, Arabic RTL first (Egyptian student tone) and English, light/dark/system/contrast, 320 px to 4K, WCAG 2.2 AA, own logo.

## 7. AI and support assistant
Tutor: explains a lecture, makes practice questions, hint ladder (hint 1, 2, 3, then explanation), citations to the uploaded note. Support assistant: floating drawer grounded in `docs/help/*.md` only. Provider chain via `ai-proxy`: Gemini free tier, OpenRouter free models, Groq, local fallback for tests; fallback order and daily cost cap in config; kill switch `AI_ENABLED`. Free users: 5 per rolling 24 hours with the badge "3 / 5 free questions remaining today"; owners unmetered. Newest suitable model chosen from `ops/MODELS.json`.

## 8. Operations (standard 26)
Health check endpoint, error digest, nightly Firestore export to R2 with a monthly restore test, weekly dependency update with tests, status page (static JSON), support inbox triaged by the assistant, weekly Telegram report (new users, active users, AI cost, errors, subscriptions) in simple Arabic, emergency alerts (outage, leaked key, cost over cap). Owner contact only for emergencies and sign-in/payment steps. AI daily cost cap and ad spend cap are set in `config/limits.json`; ads: none until the owner sets a cap.

## 9. Launch package (standard 24, prepared for the owner)
Domain, Cloudflare project, Firebase project with a brand-clean Google sign-in screen, Paymob account (test mode in code), Play Console later. Legal pack (privacy, terms, refunds with auto-renewal text, cookies, DPA, sub-processors, AI-use note) generated from `data-inventory.yml`, marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch". Egypt PDPL 151/2020 and GDPR duties turned into tasks; exact article text "(unsourced, verify)" before the lawyer step.

## 10. Visibility (standard 27)
Arabic and Egyptian queries ("ملخصات مادة ... معهد العبور"), one landing page per subject and per tool (GPA calculator is the link magnet), `llms.txt`, facts page, JSON-LD (`WebApplication`, `FAQPage`, `BreadcrumbList`), Search Console and Bing steps for the owner, weekly AI-answer check script, YouTube short tutorials later. No fake reviews or student counts.

## 11. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Deep scan, setup, CI | `.sir/reports/deep-scan.md`; green Actions URL; secrets report |
| M1 | Core slice | sign in, subject list, note viewer, quiz attempt saved in Firestore (emulator e2e test) |
| M2 | Parity import | dry-run import prints counts equal to the old database |
| M3 | Security, legal, billing | rules tests, forged token test, `billing-fallback` render test, legal pages generated |
| M4 | AI | tutor refusal eval 100 percent; quota badge test |
| M5 | Quality | 390/1280 screenshots LTR+RTL, light+dark, Lighthouse mobile 90+ (saved JSON) |
| M6 | Release | domain connected (owner), old site redirects, keys rotated, classmates invited only when real content exists |

## 12. Next 10 tasks (each under 2 hours)
1. Deep scan of `legacy/Obour Academic Hub` against `ops/inventory/Obour-Academic-Hub.md`; write `.sir/reports/deep-scan.md` (features to port, to drop). Check: file lists each of the 12 pages with a verdict.
2. Secrets report: list files in legacy that hold keys (names only), confirm `legacy/` is git-ignored (`git check-ignore`), add rotation steps to the checkpoint. Check: report file, no key text inside.
3. Scaffold the app with Tailwind v4 tokens, RTL logical CSS, health route. Files: `apps/web/`. Check: `npm run build` exit 0; `/api/health` returns 200.
4. Firestore rules deny-by-default plus emulator tests (own data readable, others' not). Files: `firestore.rules`, `tests/rules/`. Check: tests green.
5. Google sign-in with server cookie session and JWKS verify. Files: `apps/web/src/server/auth/`. Check: forged and expired token tests green.
6. Subject list and note viewer reading from Firestore with skeleton, empty, error+Retry states. Check: screenshots of all 5 states at 390 px.
7. Import script with `--dry-run` counts. Files: `scripts/import-legacy.mjs`. Check: dry run prints counts and writes nothing.
8. Tutor refusal eval set (30 prompts) and runner. Files: `evals/tutor.jsonl`, `scripts/eval-tutor.mjs`. Check: runner exits non-zero below 100 percent refusal.
9. Pricing page with "Subscriptions launching soon" and lead capture stored in Firestore. Check: submitting an email creates one doc; invalid email shows an error.
10. CI: typecheck, lint, tests, build, gitleaks. Check: green Actions URL.

## 13. Risks and open questions (defaults)
- Institute rules or copyright on notes: publish only owned or agreed content; default is a takedown form and an upload agreement text.
- Paying capacity of students is unknown: default is test the price with interviews; keep Pro cheap; no dark patterns.
- Large legacy code (files over 530 lines): default is port by feature, never copy files wholesale.
- Backend choice conflict (Firestore vs D1): default Firestore; revisit only with an ADR.
- Competitor and market numbers: see `plans/competitors/sir-obour-hub.md`; it has no source links (0 URLs found), so every claim there is "(unsourced, verify)" until sourced.

## 14. Only the owner can do
Buy the domain; create the Firebase and Cloudflare projects (sign-in); create the Paymob account and paste keys into one `.env`; rotate the old Firebase keys; get consent from classmates who contribute notes; lawyer review before paid launch; Search Console sign-in.
