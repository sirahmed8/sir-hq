# PLAN: SIR Education Hub

Version 1.0.0. Merged 2026-11-12 (round r53a) from the old SIR Obour Hub plan and the owner's 2026-11-12 direction (`plans/PRODUCT_DIRECTION_2026-11-12.md`, section 2). Supersedes the two-section file from r52 (vision + previous plan). The old competitor file `ops/competitors/sir-education-hub.md` is replaced by the 10-competitor matrix in section 13. Tasks are in `ops/briefs/sir-education-hub-tasks.md`.

## What changed vs. the previous plan (r52)

- **Scope**: from "Obour students only" to a global multi-tenant education platform: any institute, university, school, training center, teacher or organization creates its own Hub; people join the Hubs they belong to.
- **Obour Institute** becomes the first Hub, keeping every current Obour feature (mapped in section 5).
- **Absorbed modules**: language learning and study help (TickTick ideas 24/25/27) are now first-class modules (section 6), not side notes.
- **Multi-tenancy is the data model from line one**: Hub, members, roles/permissions, groups, classes, courses, schedules, materials, assignments/quizzes, practice/mock exams, chats/announcements, attendance, grades visibility, certificates, parent/guardian view, billing, settings, branding per Hub (section 4).
- **Onboarding wizard** with linear stepper where future steps stay locked until validated (section 8).
- **Owner-only analytics page** covering all Hubs, revenue, usage, AI cost and health (section 9).
- **Safety for minors and data protection** gets its own section (12): GDPR, Egyptian PDPL 151/2020, moderation, reporting, export and deletion.
- **Platform matrix expanded** to web, Windows, macOS, Linux, Android, iOS, tablets, TV, one account everywhere, offline reading (section 11). TV added vs. the old plan (which skipped it); wearables and car stay deferred with ADR.
- **Pricing reshaped**: free trial for a Hub, free tier for students, fair subscription per Hub or per seat in EGP and USD (section 14).
- **Competitor matrix** is now the 10 named by the owner (Google Classroom, Moodle, Canvas, Schoology, Microsoft Teams for Education, Classera, Teachable, Udemy for Business, Edmodo successors, local Egyptian platforms) in `ops/competitors/sir-education-hub.md`.
- **M0 now recreates the Desktop folder kit from scratch** (owner default 19): folder.ico, shortcuts, Versions.txt 1.0.0.
- **AI tutor** is now explicitly built on the free-model fallback chain with strict privacy and a hard refusal of graded work (section 7).
- **Still true and kept**: Firebase project `sir-education-hub`, dual hosting Firebase + Vercel, deny-by-default Firestore rules, owner-auth pattern, ai-proxy fallback chain, billing-fallback, legal-pack, owner-only `/owner`, five states, premium quality bar, version 1.0.0, no PRs, never delete `legacy/`, no fake data.

## 1. Who it is for and the promise

Students, teachers, admins and parents in any educational organization worldwide, starting with Obour Institute (Management & Informatics, Engineering & Technology) and Ahmed's classmates. One account works everywhere.

**One-sentence promise (sell the end state):** Open SIR Education Hub on any device and in one minute you know today's lectures and halls, the exact grade you need for your target GPA, you have every course's notes, past exams and a tutor that explains instead of doing your graded work for you, and you can join or run the Hub your organization uses.

## 2. Competitors

Full study with sources: `ops/competitors/sir-education-hub.md` (10 competitors: Google Classroom, Moodle, Canvas, Schoology, Microsoft Teams for Education, Classera, Teachable, Udemy for Business, Edmodo successors, local Egyptian platforms). Headline: the real competition is scattered chat groups plus a legacy portal; global note marketplaces are USD-priced and curriculum-generic. Our edge: multi-tenant Hub model (any organization creates its own), Obour-specific timetable/GPA/attendance tools, a free-first curated vault, Arabic-first UX, integrity-first tutor, fair EGP pricing.

## 3. Names and IDs

| Item | Value |
|---|---|
| Product | SIR Education Hub (renamed from SIR Obour Hub on 2026-11-12) |
| Folder | `D:\Projects\SIR Education Hub` |
| GitHub (private) | `sirahmed8/sir-education-hub` |
| Firebase project | `sir-education-hub` (own project per rule 13) |
| App id | `app.sir.education-hub` |
| Hosts | Firebase Hosting + Vercel (same build, same env vars, both curl-checked) |
| Version | 1.0.0 (stays) |
| Platforms | section 11 |

## 4. Multi-tenant model

Every piece of data belongs to exactly one Hub. A user can belong to many Hubs with different roles in each. Rules are enforced server-side and in Firestore security rules (cross-Hub read fails in emulator tests).

### 4.1 Hub
- `hubId`, `name`, `slug` (unique, used in URLs), `type` (university / institute / school / training_center / teacher_group / organization), `country`, `language`, `timezone`, `createdAt`, `ownerUid`.
- Branding: logo, primary color, accent, favicon, welcome text, custom domain (later), email sender name. Stored in `hubs/{hubId}/branding`.
- Settings: features toggled per Hub (language learning module, study help, attendance rule threshold, grading scale, certificate templates, parent view on/off, billing mode).
- Status: trial / active / suspended / archived.

### 4.2 Members and roles
Roles per Hub (a user can hold one role per Hub, plus global platform roles):
- **Owner**: created the Hub; full control; billing; delete Hub.
- **Admin**: manage members, roles, courses, schedules, settings, moderation.
- **Teacher**: create/manage courses, materials, assignments, quizzes, grades, attendance for their classes.
- **Teaching assistant**: grade, post announcements, moderate Q&A in assigned courses.
- **Student**: enroll in classes, submit work, view own grades/attendance, use study help and language modules.
- **Parent/Guardian**: read-only view of linked student(s): grades, attendance, assignments due, announcements. No access to other students. Enabled per Hub setting and per student opt-in.
- **Moderator**: community content moderation only.
- **Platform owner (Ahmed)**: global, cross-Hub analytics and support; never sees student content unless acting on a report with audit log.

Permissions are a capability matrix (`canManageMembers`, `canEditCourse`, `canGrade`, `canPostAnnouncement`, `canViewAllGrades`, `canManageBilling`, etc.) stored as role -> capability set, evaluated server-side. No client-side trust.

### 4.3 Groups, classes, courses
- **Group**: a cohort inside a Hub (e.g., "Year 2, Management & Informatics, Section A"). Has members, schedule, assigned teachers.
- **Class**: a teaching instance of a course for a group in a term/semester. Has teacher(s), enrolled students, sessions.
- **Course**: the subject itself (name, code, department, credit hours, description, materials). Reusable across classes/terms.
- **Term/Semester**: time window with start/end, exam periods.

### 4.4 Schedules, materials, assignments, quizzes
- **Schedule**: weekly recurring sessions (day, time, hall/room, teacher, type: lecture/lab/exam) plus one-off events and cancellations/urgent notices. ICS export. Offline cache for the whole term.
- **Materials**: files (PDF/DOCX/etc.) organized Course > Topic > Doctor/Teacher, with ownership/agreement confirmation on upload and a takedown form. Stored in Firebase Storage with per-Hub paths.
- **Assignment**: title, description, due date, attachments, submission (file/text), grading, feedback. No graded-work solving by AI.
- **Quiz**: question bank (MCQ, short answer, etc.), attempts with persisted scores, time limits, retake policy, shuffle. Auto-grading where objective.

### 4.5 Practice and mock exams
- Practice quizzes generated from the course's own notes with citations (AI tutor).
- Mock exam mode: timed, exam-style, no hints during the run, review after.
- Spaced repetition flashcards per subject.
- Never solves graded work: practice only.

### 4.6 Chats and announcements
- Per-Hub announcement channel (teachers/admins post; students read; optional comments).
- Per-course Q&A threads.
- Study-group board (students coordinate).
- Per-Hub chat rooms (moderated).
- All messages stored per Hub; moderation queue; report button.

### 4.7 Attendance
- Per-session attendance (present/absent/late/excused) recorded by teacher or TA.
- Absence tracker against the institute's rule (e.g., 25% deprivation rule) with a configurable threshold per Hub. Rule text must cite an official source before stated as fact.
- Student sees own attendance; parent sees linked student's.

### 4.8 Grades visible to the right people
- Gradebook per class: assignment/quiz/exam scores, weights, computed totals, GPA on the institute's scale.
- Visibility: student sees own; teacher sees their classes; admin sees Hub; parent sees linked student; platform owner sees aggregates only.
- Grade mirror: manual entry or student-uploaded file only, kept on their account (not built in v1, recorded decision).
- GPA simulator: "grade needed for target GPA" calculator, local in browser, no server grade truth.

### 4.9 Certificates
- Templates per Hub (course completion, exam pass, participation).
- Issued to a student, downloadable PDF, verifiable by code/link.
- Admin manages templates; teacher issues.

### 4.10 Parent / guardian view
- Opt-in per student (student or admin links a guardian account).
- Read-only dashboard: linked students' grades, attendance, assignments due, announcements.
- No access to other students; no chat; no content upload.
- Disabled by default; Hub admin enables.

### 4.11 Billing
- Per Hub: free trial (time-limited) then subscription. Per seat option for larger orgs.
- Per student tier: free tier (full timetable, notes browsing, exams archive, quiz attempts, GPA, planner, attendance, 5 AI questions/day) + Pro (unlimited AI tutor, offline packs, exam simulator, priority storage).
- EGP primary, USD/SAR/AED auto-detected from visitor locale/IP with manual override.
- Until Paymob/Fawry keys exist: "Subscriptions launching soon" + email lead capture; never a broken checkout.
- Subscription grants the Hub owner all permissions; platform owner sees revenue in analytics.

### 4.12 Settings and branding per Hub
- All of 4.1 branding + feature toggles + language + timezone + grading scale + attendance threshold + certificate templates + legal contact + data retention.
- Export Hub data (admin) and delete Hub (owner, with confirmation and grace period).

## 5. Obour Institute as the first Hub

Obour Institute is created as a seeded Hub (`type: institute`, country: EG, language: ar-EG) with its current features mapped:

| Current Obour feature (legacy) | New home | Notes |
|---|---|---|
| Timetable (weekly per department/year/section) | Schedule module | ported |
| Today's-lecture card with live countdown | Schedule + home dashboard | ported |
| Hall directory | Schedule (rooms) | ported |
| Cancellation/urgent notice banner | Announcements | ported |
| .ics export to phone calendar | Schedule | ported |
| Offline PWA cache for the semester | Platform (offline reading) | ported |
| Notes vault (Year > Department > Subject > Doctor) | Materials module | ported |
| PDF/DOCX viewer, 1-click download | Materials | ported |
| Search | Materials + global search | ported |
| Upload with ownership/agreement + takedown | Materials | ported |
| Past exam archive | Materials (tagged exam) | ported |
| Quiz runner with persisted attempts | Quizzes module | ported |
| AI-generated practice quizzes from course notes with citations | Practice + AI tutor | ported |
| Egyptian credit-hour GPA simulator | Grades module | ported |
| "grade needed for target GPA" calculator | Grades module | ported |
| Transcript PDF parser (local in browser) | Grades module | ported |
| Study tasks, assignment board | Assignments + planner | ported |
| Exam countdown hero | Home dashboard | ported |
| Absence tracker vs 25% rule | Attendance module | ported, rule text cited before stated as fact |
| Q&A threads per subject | Chats module | ported |
| Course difficulty ratings | Courses (reviews) | ported |
| Study-group board | Chats module | ported |
| Anonymous feedback box | Chats (moderated) | ported |
| Used-book/tool marketplace with WhatsApp contact | Marketplace module (optional per Hub) | ported |
| Google sign-in, profile, notification prefs | Accounts + notifications | ported |
| Linked Telegram bot for schedule alerts | Bot link flow | ported |
| Legal pages (privacy, terms, refunds, cookies, DPA, sub-processors, AI-use) | Legal pack | ported |
| Data export and deletion in one tap | Privacy controls | ported |
| Owner-only analytics | Owner analytics page | ported |
| Campus event registration with QR pass | Events module | ported |
| Telegram daily schedule alert bot bridge | Bot link flow | ported |
| Grade-appeal runbook guide | Help center (docs) | ported |
| Library catalog checker | Help center / integrations | ported |
| Bus schedule tracker | Help center / integrations | ported |
| Peer study-group coordinator | Chats module | ported |
| Course review benchmark | Courses (reviews) | ported |
| Admin panel (subjects, users, analytics, errors, inbox, resources, settings, team, subscriptions, notifications) | Hub admin area | ported |
| AI tutor (Jarvis) | AI tutor module | rebuilt on fallback chain |
| Transcription | Study help module | ported |

Explicitly NOT ported: `solve_assignment` / `solve_quiz` modes, deterministic fake fallback solutions, Moodle automation scripts, stored institute passwords, any graded-work submission. All quarantined in `legacy/`; never ported.

## 6. Language learning and study help as modules

Both are optional modules a Hub can enable.

### 6.1 Language learning module
- Per-Hub language courses (e.g., English, French, German, Arabic for non-natives) with levels, lessons, vocabulary, grammar, listening/reading exercises.
- Spaced repetition vocabulary cards with audio.
- Pronunciation practice (record + compare, local where possible).
- Placement test to set starting level.
- Progress per student; certificate on level completion.
- AI tutor helps explain grammar and gives examples; never writes graded essays for the student.

### 6.2 Study help module
- Hints, practice sets, worked examples, flashcards, mock quizzes (never graded-work solving).
- AI-generated practice quizzes from the course's own notes with citations.
- Study planner: tasks, assignment board, exam countdown, daily plan sized to 15/30/60 minutes.
- Weak-topic tracking and review scheduling.
- Transcript-to-notes (audio transcription) where a Hub enables it.
- Mind maps from course content.
- All AI help is hint-first and explains; refuses to solve graded work.

## 7. AI tutor and summaries

Built on the shared `ai-proxy` fallback chain (Gemini flash-lite -> flash -> any Gemini -> OpenRouter free -> other free -> local), per-project keys on the `sir-education-hub` Firebase/GCP project and its own OpenRouter key.

- Grounded strictly in uploaded notes + `docs/help/*.md` + course materials of the Hub the user belongs to. No cross-Hub data leakage.
- Capabilities: explain a concept, give a hint ladder, generate practice quizzes with citations, summarize a document, create flashcards, answer questions about course material.
- Refuses graded work: live-quiz answers, assignment solutions, exam leaks. Eval set of 30 Arabic + English prompts must pass 100% refusal before launch.
- Quotas: free users 5 questions per rolling 24h with quota badge; Pro unlimited; owner unmetered.
- `AI_ENABLED` kill switch and daily cost cap in `config/limits.json`.
- Privacy: Hub content is never used to train models; prompts are not logged with student identity beyond quota counting; `private=true` forces local models and fails closed if local unavailable.
- AI cost per Hub is tracked for the owner analytics page.
- Support assistant (floating drawer) grounded only in `docs/help/*.md`.

## 8. Onboarding wizard

Linear stepper. Future steps are not clickable until the current step validates. Progress is saved; a Hub can resume.

Steps for "Create a Hub":
1. Account (Google sign-in, profile).
2. Hub basics (name, type, country, language, timezone).
3. Branding (logo, colors) - skippable with defaults.
4. First group/class (name, year/section, term).
5. First course + materials upload (optional, skippable).
6. Invite members (email/links) - optional.
7. Plan selection (trial / Pro) - optional, defaults to trial.
8. Done: open the Hub dashboard.

Steps for "Join a Hub":
1. Account.
2. Find Hub (search by name/slug or invite link).
3. Request to join / enter code.
4. Pick group/class (if applicable).
5. Done.

Validation: each step's required fields are checked client and server side; the stepper disables forward navigation until valid; back navigation is always allowed; a progress indicator shows step X of N.

## 9. Owner-only analytics page

Route `/owner`, server-verified owner token only, fail closed, 403 for non-owner.

Content (real metrics only, no fake numbers):
- All Hubs: count by status (trial/active/suspended/archived), by type, by country, growth over time.
- Revenue: MRR, ARR, by plan, by currency, churn, failed payments.
- Usage: active users (DAU/WAU/MAU) per Hub and platform-wide, sessions, feature usage (materials views, quiz attempts, AI questions, attendance marks).
- AI cost: per Hub, per day, model breakdown, quota hits.
- Health: error rates, API latency, storage usage, backup status, CI status.
- Moderation: open reports, resolved, response time.
- Export: CSV/JSON for any metric.

## 10. Free tier and pricing (EGP primary, USD/SAR/AED auto-detected)

- **Free for students**: full timetable, hall directory, notes browsing and downloads, exams archive, quiz attempts, GPA simulator, planner, attendance tracker, 5 AI questions per rolling 24h, marketplace browsing.
- **Pro for students** (test price, "(unsourced, verify)" until 10 student interviews): 49 EGP/month or 399 EGP/year (~$1 / ~$8 placeholder pending FX check) - unlimited AI tutor, offline note packs, exam simulator mode, priority upload storage.
- **Hub trial**: free trial for a Hub (time-limited, e.g. 30 days) with full features.
- **Hub subscription**: fair pricing per Hub or per seat, in EGP and USD, tiered by size (small teacher group / school / institute / university). Prices are "(unsourced, verify)" until 5 Hub-owner interviews; recorded in `config/pricing.json`.
- **Marketplace business listing**: 30 EGP/semester (from `.sir/MASTER_PLAN.md`, "(unsourced, verify)" as market rate).
- **Fallback**: until Paymob/Fawry keys exist, CTA reads "Subscriptions launching soon" with email capture; never a broken checkout.
- Owner gets all Pro features free; subscription grants the Hub owner all permissions.

## 11. Platform matrix

| Platform | v1 | Notes |
|---|---|---|
| Web (responsive, PWA installable) | in v1 | Next.js App Router; Arabic RTL first, English second; light/dark/system/high-contrast; offline reading of cached materials |
| Windows | in v1 via installable PWA + Tauri wrapper for desktop-only features | follows WINDOWS_APP_STANDARD when a desktop-only feature appears (ADR) |
| macOS | in v1 via installable PWA | same |
| Linux | in v1 via installable PWA | same |
| Android phone/tablet | M5-M6 | Capacitor wrapper; APK/AAB via EAS or local Gradle |
| iOS / iPad | M5-M6 | same Capacitor build; unsigned .ipa for SideStore until paid Apple account |
| Tablets (Android/iPad) | M5-M6 | responsive + Capacitor; larger layouts |
| TV (Android/Apple) | post-v1 (ADR) | big-screen dashboard for classroom display if requested |
| Wear OS / watchOS | post-v1 (ADR) | glanceable next-lecture reminder only if requested |
| Car (Android Auto/CarPlay) | skip | no allowed car category fits |
| Widgets / Live Activities | M6 | next-lecture and countdown widgets via Capacitor plugins |
| Browser extension | skip | no use case |

One account everywhere: Firebase Auth (Google sign-in) with server-verified ID token; session cookie HttpOnly/Secure/SameSite=Strict; no localStorage tokens.

Offline reading: service worker caches materials and timetable for the term; "check offline readiness" in settings; works on weak campus networks.

## 12. Safety for minors and data protection

- **Age and consent**: Hub owner declares the age range of their learners. For Hubs with minors, require parental/guardian consent flow before a student account is active; store consent record with timestamp and version of the terms accepted.
- **GDPR + Egyptian PDPL 151/2020**: data inventory (`data-inventory.yml`), legal pack generated and marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch"; country-specific tasks with "(unsourced, verify)" until sourced; Saudi PDPL etc. as tasks.
- **Data minimization**: collect only what the feature needs; no tracking beyond product analytics; no third-party ads.
- **Moderation**: report button on all user content; moderation queue for admins; platform owner sees only reported content with audit log; auto-hide after N reports pending review.
- **No graded-work solving by AI** (integrity): eval set 100% refusal before launch; this is also a child-safety and academic-integrity rule.
- **Data export and deletion**: one tap each, per user and per Hub (admin). Deletion has a grace period and confirmation; audit log entry.
- **Cross-Hub isolation**: Firestore rules deny cross-Hub reads; emulator tests prove it.
- **Secrets**: env only, gitleaks in CI, keys in `legacy/` rotated at launch.
- **CSP**: no unsafe-inline/eval; analytics load only after consent; Reject All as prominent as Accept.
- **Privacy of the people first**: AHome and Habiba data never leaves AHome; no private data in plans/logs/reports.

## 13. Competitor matrix

See `ops/competitors/sir-education-hub.md` for the full 10-competitor matrix (Google Classroom, Moodle, Canvas, Schoology, Microsoft Teams for Education, Classera, Teachable, Udemy for Business, Edmodo successors, local Egyptian platforms) with strengths, flaws and our edge, plus sourcing tasks. Every claim carries a source link or "(unsourced, verify)".

## 14. Architecture (Firebase + Vercel now)

- **App**: Next.js (App Router) + TypeScript + Tailwind v4 tokens, deployed identically to Firebase Hosting and Vercel (Vercel imports the GitHub repo via Vercel CLI; same build, same env vars on both; both curl-checked per rule 15). Repo `sirahmed8/sir-education-hub` (private). App version stays 1.0.0.
- **Backend**: Firebase project `sir-education-hub` (own project per rule 13): Auth (Google sign-in, JWKS-verified ID token on server), Firestore (deny-by-default rules, emulator-tested, multi-tenant by Hub), Firebase Storage for materials/files, App Check where available. Older drafts mentioned Cloudflare Pages/D1/R2; superseded by the dual-host and own-Firebase rules. R2 remains a documented scale alternative behind an ADR if Storage egress costs bite.
- **Accounts**: `owner-auth` package pattern - server-verified token, `OWNER_EMAILS`/`OWNER_UIDS` allow-list, email_verified, fail closed; HttpOnly+Secure+SameSite=Strict session cookie; rate limits on auth and AI; no localStorage tokens.
- **Owner-only analytics page**: `/owner` route, server-verified owner token only, real metrics (section 9). Non-owner gets 403.
- **AI**: `ai-proxy` with the standing fallback chain, per-project keys, `AI_ENABLED` kill switch, daily cost cap in `config/limits.json`, free users 5 questions per rolling 24h with quota badge, owner unmetered, Hub-scoped context. Tutor eval set of 30 Arabic+English prompts must pass 100% refusal before launch.
- **Billing**: `billing-fallback` - "Subscriptions launching soon" + email lead capture until Paymob keys exist; EGP primary with auto-detected USD/SAR/AED; subscription grants owner all permissions.
- **Legal**: `legal-pack` generated from `data-inventory.yml`, marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch"; Egypt PDPL 151/2020 and GDPR tasks.
- **Ops**: `/api/health`, nightly Firestore export, weekly dependency update, static status JSON, weekly Arabic Telegram report, emergency alerts; AI daily cost cap.
- **Support assistant**: floating drawer grounded only in `docs/help/*.md`.
- **Skills used for this plan** (from ops/SKILLS_INDEX.md + encyclopedia): sir-skill-library, taste-design-engine, anti-vibecoded-design-system, emil-motion-impeccable, cognitive-product-intuition, modern-ui-ux-design-system, high-conversion-copywriting, mobile-ergonomics-polish, firebase_auth_basics, firebase_firestore, firestore_rules_creation, firebase_security_rules_auditor, vibe-auth-hardening, zero-trust-security-hardening, legal-compliance-shield, omniroute-resilience-gateway, database-reliability-transactions, production-engineering-standards, react-best-practices, nextjs, verification, skills-discovery-engine, modern-web-guidance, a11y-debugging, chrome-devtools.

## 15. Premium quality bar (Apple-level)

- Apple-level motion: spring physics (stiffness 400/damping 30 micro, 300/28 layout), transform+opacity only, 120Hz-safe, reduced-motion path, matching open/close for every sheet/drawer.
- Arabic (Egyptian student tone) RTL-first and English; per-character bidi detection in inputs; `<bdi>` isolation for mixed text; Cairo/IBM Plex Sans Arabic + Inter pairing; `tabular-nums` on numbers.
- Five states on every view: idle, skeleton matching final geometry, empty with one CTA, error with retry, populated with cursor/keyset pagination fine at 1,000+ items.
- Accessibility: WCAG 2.2 AA, 44px targets, full keyboard nav, focus visible, 320px to 4K, zoom 80-200%.
- No AI slop: no purple-blue gradients, no sparkle icons, no emoji headings, no pill-button spam, no hype words, no em-dashes in copy, no fake counts or reviews.
- Native-app feel (owner default 14): disable default selection/context menu, own context menu.
- Self-audit loops until two clean cycles; browser tests for layout invariants at 320/390/768/1280/1920 in both languages/themes.

## 16. Milestones M0-M6 (acceptance tests)

| Milestone | Scope | Acceptance test |
|---|---|---|
| **M0 Foundations + Desktop kit** | Repo scaffold (exists), `.sir/` kit (exists), Firebase project `sir-education-hub` + Vercel import, CI green, **recreate the Desktop folder kit from scratch** (`folder.ico`, SIR Projects shortcuts, Versions.txt 1.0.0) | `npm run build` exit 0; `/api/health` 200; `gh run list` green or local verify pasted (CI quota flag rule); Desktop folder exists with real shortcuts and folder.ico; sign-in brand check screenshot shows no Firebase project id |
| **M1 Core slice** | Google sign-in, Hub creation wizard (steps 1-3), subject list, note viewer, quiz runner with persisted attempts; deploy to both hosts | Sign in -> create Hub -> subject -> note -> quiz attempt saved in Firestore (emulator e2e); both Firebase and Vercel URLs curl 200 |
| **M2 Content parity** | Import script `--dry-run` for legacy Firestore data; timetable + GPA simulator + hall directory; multi-tenant rules | Dry run prints counts matching legacy; timetable query <5ms; GPA calculator computes required grades correctly on test vectors; cross-Hub read fails in emulator tests |
| **M3 Security, legal, billing, owner page, onboarding** | Deny-by-default rules + emulator tests, forged-token 403, billing fallback, legal pages, `/owner` analytics, full onboarding wizard | Forged token 403 in CI; `/owner` 403 for non-owner; pricing shows "Subscriptions launching soon" + lead capture creates one Firestore doc; wizard blocks future steps until validated |
| **M4 AI tutor + quality + modules** | ai-proxy chain, quota badge, tutor eval, support assistant, five-state audit, Lighthouse, language-learning and study-help modules (v1) | `npm run eval:tutor` 100% refusal on 30 prompts; badge shows "3 / 5" correctly; Lighthouse mobile 90+; screenshots 390/1280 LTR/RTL light/dark archived; module enable/disable per Hub works |
| **M5 Community + marketplace + mobile** | Q&A, course reviews, study groups, book marketplace, Telegram schedule bot, Capacitor Android/iOS builds, widgets | Post -> moderation -> visible flow e2e; marketplace listing contact flow tested; bot sends daily schedule at 07:30 Cairo time; APK installs and signs in on a real device |
| **M6 Mobile + release + parent view + certificates** | Capacitor polish, parent/guardian view, certificates, domain + dual-host cutover, legacy keys rotated, `legacy/` moved to old projects per merge record, Desktop kit verified | Both hosts serve the domain; old Firebase admin keys rotated; parent view shows only linked student; certificate verifies by code; checkpoint records both live URLs |

## 17. First 10 tasks for free agents

Written and queue-ready in `ops/briefs/sir-education-hub-tasks.md` (T1-T10: deep scan, secrets report, scaffold, Firestore rules, auth, notes viewer five states, import dry-run, tutor eval, pricing fallback, CI). Each task is under ~2 hours, commits and pushes to `main` in `D:\Projects\SIR Education Hub`.

## 18. Risks and open questions (defaults)

- Content rights: only notes classmates own and agree to publish; takedown form + upload agreement; default conservative.
- Paying capacity unknown: test price with interviews; keep Pro cheap; no dark patterns.
- Large legacy (62k lines, 24+ files >530 lines): port by feature, never copy wholesale.
- Unverified market claims: every competitor number without a link stays "(unsourced, verify)"; sourcing tasks listed in the competitor file.
- Result-day traffic spikes: static/edge-cached public pages (timetable, hall directory) so the portal stays up when the official SIS falls over.
- Multi-tenant isolation must be proven by emulator tests before any real Hub data is stored.
- Parent/guardian view is privacy-sensitive: opt-in only, read-only, no cross-student access, audit-logged.
- AI cost can grow with many Hubs: per-Hub cost tracking and daily cap; alert owner if over.

## 19. Only the owner can do

Buy the domain; create/confirm Firebase project `sir-education-hub` sign-in and OAuth consent screen; create Paymob/Fawry accounts and paste keys into `.env` (never git); rotate the two legacy Firebase admin keys found in `legacy/Obour Academic Hub/`; consent from classmates contributing notes; lawyer review before paid launch; Search Console/Bing sign-in; Apple Developer account when iOS store submission is wanted; decide final Hub subscription prices after 5 Hub-owner interviews.

## 20. Skills and standards applied

Shared kit: owner-auth, billing-fallback, owner analytics, notifications, bot-link, ai-proxy, design-tokens, motion, changelog, help-center, signed-webhook, legal-pack, i18n, ui/styles/hooks, dual hosting, competitor matrix, security baseline, operations standard 26, launch package standard 24, visibility standard 27.

Premium code bar: `standard/23-premium-code-bar.md`. Owner defaults: `standard/OWNER_DEFAULTS.md`. Lessons: `ops/LESSONS.md` (L1-L51). Quality charter: `plans/GEMINI_QUALITY_CHARTER.md`. AI fallback chain: `plans/AI_FALLBACK_CHAIN.md`.
