# First 10 Tasks to Hand to Free Agents: SIR Education Hub (sir-education-hub-tasks.md)

Tasks ready to queue for free CLI agents. Each task includes a title and one-paragraph brief. All tasks are designed to be completed in under 2 hours. Product folder: `D:\Projects\SIR Education Hub`. Product rules: read `AGENTS.md`, `.sir/PLAN.md`, `.sir/CHECKPOINT.md`, `D:\Projects\_SIR\plans\sir-education-hub.md` first. Never touch `D:\Projects\AHome`, never open AHome/Habiba material, never port `solve_*` graded-work code, version stays 1.0.0, no placeholders, no fake data, five states on every view, Arabic RTL + English, multi-tenant isolation proven by emulator tests.

## 1. Deep scan of legacy and plan upgrade
Scan the legacy application (`legacy/Obour Academic Hub/`, 344 TS/TSX files, ~62k lines) and `ops/inventory/Obour-Academic-Hub.md`. Write `.sir/reports/deep-scan.md`: every page and feature with a verdict (port / drop / rewrite), the data model to keep (subjects, exams, sections, questions, users, subscriptions), and the list of files that must never be ported (solve modes, fake fallbacks, credential scripts). Check: the report lists each of the 12+ pages with a verdict and names every file containing keys or graded-work logic (names only, no secret values), plus a mapping table from legacy feature to new module per plan section 5.

## 2. Secrets and quarantine report
Inside `legacy/Obour Academic Hub/`, list (names only, never contents) every file holding keys or credentials: the two Firebase admin JSON files, `new-service-account.json`, `.env.local`, Upstash/Cloudinary/Vercel Blob values. Confirm `git check-ignore` covers `legacy/` and the product `.gitignore` covers `.env*`. Append the key-rotation steps to `.sir/CHECKPOINT.md` open items. Check: report file exists with file names only, and `git status` shows nothing secret staged.

## 3. Scaffold the app shell
Create the Next.js (App Router, TypeScript, Tailwind v4) app skeleton in the product repo root per `plans/SHARED_PLATFORM_KIT.md` tokens: RTL logical CSS, light/dark/system/high-contrast themes, Cairo + Inter type pairing, `/api/health` route returning 200 JSON, root layout with bidi-safe input handling and five-state primitives, multi-tenant-aware routing (`/h/[slug]/...`). Check: `npm run build` exits 0, `npm run dev` serves `/api/health` 200, and a 390px screenshot shows no horizontal overflow.

## 4. Firestore deny-by-default rules + multi-tenant emulator tests
Write `firestore.rules` (deny by default; reads only for signed-in members of the Hub; writes owner/admin via custom claim only; cross-Hub read fails) and emulator tests under `tests/rules/` proving: anonymous read denied, cross-user read denied, cross-Hub read denied, owner write allowed, non-member write denied. Check: `firebase emulators:exec --only firestore 'npm run test:rules'` passes green.

## 5. Google sign-in with hardened session
Implement `src/server/auth/`: Firebase ID token verified server-side via JWKS, `OWNER_EMAILS`/`OWNER_UIDS` fail-closed owner check, HttpOnly+Secure+SameSite=Strict session cookie, rate limit on sign-in attempts, forged/expired token tests, Hub membership resolution. Check: unit tests prove forged token -> 403, expired token -> 401, valid token -> session cookie set; no token in localStorage anywhere; cross-Hub access denied.

## 6. Subject list + note viewer with five states
Build the Subject list and Lecture note viewer screens reading from Firestore/Storage: skeleton matching final geometry, empty state with one CTA, error state with Retry, populated state with keyset pagination, RTL/LTR and light/dark, scoped to the current Hub. Check: Playwright screenshots of all five states at 390px and 1280px archived in `.sir/evidence/`, zero console errors.

## 7. Legacy import script with dry run
Write `scripts/import-legacy.mjs`: connects to the old Firestore (service account from env only, never committed), exports subjects/exams/questions/notes/users/counts per collection, supports `--dry-run` printing per-collection counts and writing nothing, and `--apply` gated behind an explicit flag plus confirmation and a target Hub id. Check: `node scripts/import-legacy.mjs --dry-run` prints real counts (or a clear "no credentials configured" path) and creates zero writes; script has no embedded secrets; cross-Hub writes are rejected.

## 8. AI tutor refusal eval set and runner
Create `evals/tutor.jsonl` with 30 prompts (15 Arabic, 15 English) covering live-quiz answers, assignment solutions, exam leaks, plus hint/explanation requests that must pass, including prompts that try to leak another Hub's content. Write `scripts/eval-tutor.mjs` that calls the ai-proxy chain and exits non-zero below 100% correct behavior (refusal + hint offer on graded-work prompts; no cross-Hub leakage). Check: runner executes and reports per-prompt verdicts; CI step added.

## 9. Pricing page with launch fallback
Build `/pricing`: free vs Pro comparison in EGP with auto-detected USD/SAR/AED display, Hub trial vs subscription tiers, "Subscriptions launching soon" CTA opening an email-capture modal that writes one lead doc to Firestore via a validated server route, invalid email shows inline error. Check: submitting a valid email creates exactly one `leads` doc; invalid email rejected client and server side; no payment links anywhere; currency auto-detected from locale/IP.

## 10. CI pipeline green
Add `.github/workflows/ci.yml` (or fix existing): typecheck, lint, vitest, build, gitleaks, emulator rules tests on every push; deploy steps for Firebase Hosting and Vercel only after build passes. Check: latest `main` run is green (or, while `ops/ci-quota-exhausted.flag` exists, the full local verify output - typecheck, lint, test, build - is pasted into the checkpoint and report).

---

## Additional tasks (r61 refresh, planning-only; T11 onwards)

All tasks below follow the same rules as T1-T10: read plan + competitor study first, under 2 hours each, commit and push to `main` in `D:\Projects\SIR Education Hub`, version 1.0.0, no placeholders, no fake data, five states on every view, Arabic RTL + English, multi-tenant isolation proven by emulator tests. First 10 (T1-T10) remain queue-ready and unchanged.

### Infrastructure and auth

11. **Firebase project + Vercel import + dual-host check.** Verify/create Firebase project `sir-education-hub` on Spark and GitHub repo `sirahmed8/sir-education-hub` (private); import repo into Vercel via CLI; set identical env vars on both; add `/api/health` returning 200 JSON on both hosts; curl both URLs (retry once on timeout). Check: both URLs return 200 JSON and the Firebase project + repo names are written in the project checkpoint. **Skills**: `firebase_basics`, `firebase_hosting_basics`, `vercel-cli`, `deployments-cicd`.

12. **Desktop folder kit (rule 19).** Recreate from scratch: `folder.ico`, SIR Projects shortcuts, `Versions.txt` 1.0.0 for the Education Hub folder on the Desktop. Check: Desktop folder exists with real shortcuts and folder.ico; Versions.txt reads 1.0.0. **Skills**: `laptop-admin`.

13. **Design tokens + theme engine.** Implement Tailwind v4 tokens (campus emerald palette for Obour Hub, neutral default for others), light/dark/system/high-contrast, Cairo + Inter pairing, RTL logical CSS, bidi-safe inputs, five-state primitives, Dynamic Island tab bar (active tab label only). Check: 390px screenshot shows no horizontal overflow in both languages/themes; contrast 7:1+ in daylight mode. **Skills**: `modern-ui-ux-design-system`, `anti-vibecoded-design-system`, `emil-motion-impeccable`, `taste-design-engine`.

14. **Owner-auth package with negative tests.** Implement `src/server/auth/`: Firebase ID token verified via JWKS, `OWNER_EMAILS`/`OWNER_UIDS` fail-closed, HttpOnly+Secure+SameSite=Strict cookie, rate limit on sign-in, forged/expired token tests, Hub membership resolution. Check: forged token -> 403, expired -> 401, valid -> cookie set; no token in localStorage; cross-Hub access denied. **Skills**: `vibe-auth-hardening`, `zero-trust-security-hardening`, `firebase_auth_basics`, `auth`.

15. **CI pipeline.** Add `.github/workflows/ci.yml`: typecheck, lint, vitest, build, gitleaks, emulator rules tests; deploy steps for Firebase Hosting + Vercel only after build passes. Check: local verify (typecheck, lint, test, build) runs green and output pasted into checkpoint while CI quota flag exists. **Skills**: `deployments-cicd`, `vercel-cli`.

### Data model and rules

16. **Domain types + zod schemas + Firestore repositories.** Implement `packages/core` types (Hub, Member, Role, Group, Class, Course, Term, Session, Material, Assignment, Quiz, Attempt, Grade, Attendance, Announcement, Thread, Message, Certificate, Event, MarketplaceListing, Review, Lead) and `packages/data` repositories, one interface per entity, with deny-by-default rules and per-Hub claims. Check: typecheck passes; cross-Hub read fails in emulator tests. **Skills**: `firebase_firestore`, `firestore_rules_creation`, `database-reliability-transactions`.

17. **Firestore rules + emulator tests (expanded).** Rules: anonymous read denied, cross-user read denied, cross-Hub read denied, owner write allowed, non-member write denied, parent read-only scoped to linked student. Check: `firebase emulators:exec --only firestore 'npm run test:rules'` green. **Skills**: `firestore_rules_creation`, `firebase_security_rules_auditor`.

18. **Storage rules + signed URLs for materials.** Per-Hub storage paths, size/type checks, signed download URLs, takedown flow. Check: wrong-type/too-large file refused; signed URL expires; takedown removes public access. **Skills**: `firebase_security_rules_auditor`, `owasp-vulnerability-shield`.

### Onboarding

19. **Create-Hub wizard (steps 1-4).** Account, Hub basics, branding (skippable with defaults), first group/class. Linear stepper, future steps locked until validated, progress saved/resumable. Check: cannot advance without required fields; back always allowed; progress indicator shows step X of N; state persists on reload. **Skills**: `react-best-practices`, `modern-web-guidance`, `cognitive-product-intuition`.

20. **Create-Hub wizard (steps 5-8).** First course + materials upload (optional), invite members (optional), plan selection (trial default), done -> open Hub dashboard. Check: same validation rules; completing lands on Hub dashboard; trial granted. **Skills**: `react-best-practices`, `commercial-app-blueprint`.

21. **Join-Hub flow.** Account, find Hub (search by name/slug or invite link), request to join / enter code, pick group/class, done. Check: invite link resolves to Hub; request creates pending membership; admin approval flow works. **Skills**: `react-best-practices`, `firebase_firestore`.

### Core features

22. **Home dashboard.** Today's lectures with live countdown, exam countdown hero, urgent notice banner, quick actions, offline readiness indicator. Check: screenshot at 390/1280 LTR/RTL light/dark; countdown updates each second; works offline from cache. **Skills**: `modern-ui-ux-design-system`, `emil-motion-impeccable`, `mobile-ergonomics-polish`.

23. **Schedule module + .ics export.** Weekly recurring sessions (day, time, hall, teacher, type), one-off events, cancellations/urgent notices, ICS export, offline cache for the term. Check: timetable query <5ms; .ics imports into phone calendar; offline works. **Skills**: `modern-web-guidance`, `database-reliability-transactions`.

24. **Hall directory.** Searchable halls/rooms with building/floor. Check: typing a hall number shows building/floor; no horizontal overflow at 390px. **Skills**: `modern-web-guidance`, `a11y-debugging`.

25. **Materials vault.** Course > Topic > Teacher organization, PDF/DOCX viewer, 1-click download, search, upload with ownership/agreement + takedown, Storage per-Hub paths. Check: upload requires agreement checkbox; takedown removes file; five states present. **Skills**: `firebase_firestore`, `firebase_storage` (via hosting), `modern-web-guidance`.

26. **Past exam archive.** Materials tagged "exam" with year/term/course, filterable. Check: filter by course+year returns tagged exams; empty state with one CTA. **Skills**: `firebase_firestore`, `modern-web-guidance`.

27. **Quiz runner with persisted attempts.** Question bank (MCQ, short answer), attempts with persisted scores, time limits, retake policy, shuffle, auto-grading where objective. Check: attempt persists across reload; score computed; retake policy enforced. **Skills**: `firebase_firestore`, `react-best-practices`.

28. **AI practice quiz generator from course notes.** Generates practice quizzes from the course's own notes with citations; never graded work. Check: generated quiz cites source note; refuses to generate answers for a live quiz. **Skills**: `gemini-api-dev`, `ai-gateway` (omniroute-resilience-gateway).

29. **Mock exam mode.** Timed, exam-style, no hints during run, review after. Check: timer counts down; hints disabled during run; review shows answers + explanations after. **Skills**: `react-best-practices`, `emil-motion-impeccable`.

30. **Spaced repetition flashcards per subject.** Cards with audio, review scheduling. Check: due cards surface; rating updates next review date. **Skills**: `modern-web-guidance`, `database-reliability-transactions`.

31. **Grades module.** Gradebook per class (assignment/quiz/exam scores, weights, computed totals, GPA on institute scale), visibility by role. Check: student sees own only; teacher sees own classes; admin sees Hub; parent sees linked student. **Skills**: `firebase_firestore`, `firestore_rules_creation`.

32. **GPA simulator (Egyptian credit-hour scale).** Local in browser, "grade needed for target GPA" calculator, transcript PDF parser (local). Check: computes required grades on test vectors; parser populates course history with 100% accuracy on sample transcript. **Skills**: `modern-web-guidance`, `react-best-practices`.
33. **Attendance module.** Per-session attendance (present/absent/late/excused), absence tracker vs configurable threshold (e.g. 25%), rule text cited before stated as fact. Check: warns when threshold reached; student/parent see own/linked only. **Skills**: `firebase_firestore`, `firestore_rules_creation`.

34. **Assignments module.** Title, description, due date, attachments, submission (file/text), grading, feedback. Check: submission persists; grading updates gradebook; feedback visible to student. **Skills**: `firebase_firestore`, `react-best-practices`.

35. **Planner / study tasks.** Tasks, assignment board, exam countdown, daily plan sized to 15/30/60 minutes, weak-topic tracking. Check: task CRUD persists; daily plan generates from due dates. **Skills**: `modern-web-guidance`, `database-reliability-transactions`.

36. **Chats & announcements.** Per-Hub announcement channel, per-course Q&A threads, study-group board, per-Hub chat rooms (moderated), report button, moderation queue. Check: post -> moderation -> visible flow e2e; report creates moderation doc. **Skills**: `firebase_firestore`, `chat-sdk`, `modern-web-guidance`.

37. **Course reviews / difficulty ratings.** Anonymous aggregated difficulty metrics (effort hours, math intensity, lab workload). Check: rating submits; aggregate recomputes; no individual exposed. **Skills**: `firebase_firestore`, `firestore_rules_creation`.

38. **Events module.** Campus event registration with QR pass. Check: registration creates doc; QR scans to verify; capacity enforced. **Skills**: `firebase_firestore`, `modern-web-guidance`.

39. **Certificates.** Templates per Hub, issuance to student, downloadable PDF, verifiable by code/link. Check: issued cert verifies by code; non-existent code returns 404. **Skills**: `firebase_firestore`, `modern-web-guidance`.

40. **Marketplace module (optional per Hub).** Used books/tools, WhatsApp contact, listing CRUD, report listing. Check: listing contact flow tested; report creates moderation doc. **Skills**: `firebase_firestore`, `modern-web-guidance`.

41. **Language learning module.** Levels, lessons, vocabulary, grammar, listening/reading exercises, spaced repetition cards with audio, pronunciation practice (record+compare, local), placement test, progress, certificate on level completion. Check: placement test sets starting level; card review scheduling works; cert issued on completion. **Skills**: `firebase_firestore`, `gemini-api-dev`, `modern-web-guidance`.

42. **Study help module.** Hints, practice sets, worked examples, flashcards, mock quizzes, study planner, weak-topic tracking, transcript-to-notes (audio, where enabled), mind maps from course content. Check: hint ladder refuses graded work; mock quiz timed. **Skills**: `gemini-api-dev`, `modern-web-guidance`.
43. **AI tutor refusal eval set + runner.** `evals/tutor.jsonl` with 30 prompts (15 ar, 15 en) covering live-quiz answers, assignment solutions, exam leaks, plus passing hint/explanation requests, including cross-Hub leakage prompts. `scripts/eval-tutor.mjs` calls ai-proxy chain, exits non-zero below 100%. Check: runner reports per-prompt verdicts; CI step added. **Skills**: `gemini-api-dev`, `omniroute-resilience-gateway`.

44. **AI tutor quota badge + cost tracking.** Free 5/24h badge "N / 5", Pro unlimited, owner unmetered, per-Hub cost tracking, daily cap, kill switch. Check: badge shows "3 / 5" correctly; quota blocks 6th free question; cost doc written per call. **Skills**: `firebase_firestore`, `omniroute-resilience-gateway`, `gemini-api-dev`.

45. **Support assistant drawer.** Floating drawer grounded only in docs/help/*.md; refuses ungrounded questions. Check: ungrounded question refused with pointer to help; grounded question answered with citation. **Skills**: `gemini-api-dev`, `modern-web-guidance`.

46. **Pricing page with launch fallback.** Free vs Pro comparison in EGP with auto-detected USD/SAR/AED, Hub trial vs subscription tiers, "Subscriptions launching soon" CTA -> email-capture modal -> one lead doc via validated server route, invalid email rejected client+server. Check: valid email creates exactly one leads doc; invalid rejected; no payment links; currency auto-detected. **Skills**: `commercial-app-blueprint`, `env-vars`, `modern-web-guidance`.

47. **Owner-only analytics page (/owner).** Server-verified owner token, 403 for non-owner; real metrics: Hubs by status/type/country, revenue MRR/ARR, usage DAU/WAU/MAU, AI cost per Hub, health, moderation, CSV/JSON export. Check: non-owner -> 403; forged token -> 403; metrics render from real data (no fake numbers). **Skills**: `routing-middleware`, `firebase_firestore`, `commercial-app-blueprint`.

48. **Parent/guardian view.** Opt-in per student, read-only dashboard (linked students' grades, attendance, assignments due, announcements), no cross-student access. Check: parent sees only linked student; disabled by default; audit log entry on access. **Skills**: `firebase_firestore`, `firestore_rules_creation`, `vibe-auth-hardening`.

49. **Minor consent flow.** Hub owner declares age range; parental/guardian consent before student account active for minor Hubs; consent record with timestamp + terms version. Check: minor account inactive until consent; consent record stored; audit log. **Skills**: `legal-compliance-shield`, `firebase_firestore`, `vibe-auth-hardening`.

50. **Legal pack generation.** Generate privacy, terms, refunds, cookies, DPA, sub-processors, AI-use from data-inventory.yml; marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch". Check: all 7 pages render; disclaimer banner present; data-inventory.yml committed. **Skills**: `legal-compliance-shield`, `commercial-app-blueprint`.

51. **Data export and deletion (one tap).** Per user and per Hub (admin); grace period + confirmation + audit log. Check: export produces JSON/CSV of user's data; deletion soft-deletes then hard-deletes after grace; audit log entry. **Skills**: `firebase_firestore`, `database-reliability-transactions`.

52. **Moderation + reporting.** Report button on all user content; moderation queue for admins; platform owner sees only reported content with audit log; auto-hide after N reports pending review. Check: report creates doc; queue lists; auto-hide triggers. **Skills**: `firebase_firestore`, `modern-web-guidance`.
53. **CSP + consent banner.** No unsafe-inline/eval; analytics load only after consent; Reject All as prominent as Accept. Check: CSP header present; banner blocks analytics until accept; reject persists. **Skills**: `owasp-vulnerability-shield`, `legal-compliance-shield`.

54. **PWA + offline reading.** Service worker caches materials + timetable for the term; "check offline readiness" in settings; works on weak campus networks. Check: airplane mode shows cached timetable/materials; readiness check reports status. **Skills**: `modern-web-guidance`, `react-best-practices`.

55. **Capacitor Android build (M5-M6).** APK/AAB via EAS or local Gradle; sign-in works on device. Check: APK installs and signs in on a real device. **Skills**: `mobile-ergonomics-polish`, `modern-app-engineering`.

56. **Capacitor iOS build (M5-M6).** Unsigned .ipa for SideStore until paid Apple account. Check: build succeeds; install via SideStore on test device. **Skills**: `mobile-ergonomics-polish`, `modern-app-engineering`.

57. **Widgets / Live Activities (M6).** Next-lecture and countdown widgets via Capacitor plugins. Check: widget shows next lecture + countdown on home screen. **Skills**: `mobile-ergonomics-polish`.

58. **Accessibility audit.** WCAG 2.2 AA: 44px targets, full keyboard nav, focus visible, 320px-4K, zoom 80-200%. Check: automated a11y checks pass; manual keyboard walkthrough documented. **Skills**: `a11y-debugging`, `chrome-devtools`.

59. **Five-state audit + Lighthouse.** Every view has idle/skeleton/empty/error/populated; Lighthouse mobile 90+. Check: screenshots of all five states at 390/1280 archived; Lighthouse report >=90. **Skills**: `verification`, `chrome-devtools`.

60. **Responsive layout verification.** Playwright tests for zero horizontal overflow across 320/390/768/1280/1920 in both languages/themes. Check: all viewports pass. **Skills**: `verification`, `a11y-debugging`.

61. **Ops endpoints + backups.** /api/health, nightly Firestore export, weekly dependency update, static status JSON, weekly Arabic Telegram report, emergency alerts, AI daily cost cap. Check: health 200; export runs; Telegram report delivered at scheduled time. **Skills**: `chat-sdk`, `modern-web-guidance`.

62. **Telegram schedule bot bridge.** Daily 07:30 Cairo schedule alert to linked students. Check: bot sends daily schedule at 07:30 Cairo time in test. **Skills**: `chat-sdk`, `telegram-bot`.
63. **Sourcing tasks (competitor matrix).** Verify Canvas/Schoology/Classera/Teachable/Udemy pricing pages with dates; record reuse/terms position of student.oi.edu.eg and elearning.oi.edu.eg; find 5 real student-run notes groups; find official enrolment figure; find official 25% absence rule + grade-appeal text; confirm Edmodo shutdown date. Check: each item has a source link or is tagged "(unsourced, verify)". **Skills**: `retrieving-developer-knowledge`, `skills-discovery-engine`.

64. **Self-audit loops + browser tests.** Two clean self-audit cycles; browser tests for layout invariants at 320/390/768/1280/1920 in both languages/themes. Check: audit log shows two clean cycles; tests green. **Skills**: `verification`, `chrome-devtools`.

65. **Legacy import script (expanded).** `scripts/import-legacy.mjs`: connects to old Firestore via env-only service account, exports subjects/exams/questions/notes/users/counts, `--dry-run` (prints counts, zero writes), `--apply` gated behind flag + confirmation + target Hub id, cross-Hub writes rejected. Check: dry run prints real counts or clear "no credentials configured"; zero writes; no embedded secrets. **Skills**: `firebase_firestore`, `database-reliability-transactions`.

66. **Milestone acceptance verification.** Per-milestone acceptance tests (M0-M6) run and evidence archived in .sir/evidence/. Check: each milestone's acceptance test passes with evidence file. **Skills**: `verification`.

---
Note: T1-T10 remain queue-ready and unchanged. T11-T66 are the expanded detailed tasks from the r61 refresh. Total 66 tasks.
