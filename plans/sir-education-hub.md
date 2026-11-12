# PLAN: SIR Education Hub

Version 1.0.0. Renamed from SIR Obour Hub on 2026-11-12 by owner direction (`plans/PRODUCT_DIRECTION_2026-11-12.md`, section 2). The old plan is kept below under "Previous plan"; the next round merges both into one bigger plan.

## Vision (owner, 2026-11-12)

A single education platform for the world, not one institute. Anyone can create their own Hub: a university, an institute, a school, a training center, a teacher's group or another educational organization. Each Hub has its own members, roles, courses, schedules, materials, quizzes and practice, chats, announcements, billing and settings. People join the Hubs they belong to and get every feature there.

- Obour Institute is the first Hub: the owner's own, with the current Obour features.
- The product absorbs the older ideas: study help, language learning and the teaching platform.
- Platforms: web, Android, iOS, Windows and the other platforms, with one account everywhere.
- Money: a free trial for each Hub, then a subscription priced fairly in EGP and USD, with a free tier for students.
- Data: multi-tenant from the first line of code. Owner-only analytics page.
- Next round: merge the old Obour plan below with this vision into one plan (milestones M0 to M6, acceptance tests, first 10 tasks for the agents).

## Previous plan (merge into the new one in the next round)

Version 1.0.0. Rewritten 2026-11-12 (r52). Replaces the old 89-line plan; keeps what is still true (names, security rules, legacy facts, AI-tutor integrity rules). Supersedes stack notes that said Cloudflare Pages or D1: the standing owner rule (OWNER_DEFAULTS item 2, WORKER_PREAMBLE item 15) requires Firebase Hosting AND Vercel dual hosting, and rule 13 requires its own Firebase project `sir-education-hub`. Decisions recorded in section 5.

## 1. Who it is for and the promise
Students of Obour Higher Institutes (Management & Informatics, Engineering & Technology) and, later, other Egyptian institutes. First users: Ahmed's classmates. Global: any student anywhere can use the same tools for their own curriculum.

**One-sentence promise (sell the end state):** Open SIR Education Hub on any device and in one minute you know today's lectures and halls, the exact grade you need for your target GPA, and you have every course's notes, past exams and a tutor that explains instead of doing your graded work for you.

## 2. Competitors
Full study with sources: `ops/competitors/sir-education-hub.md` (10 competitors: official MyU portal, official Moodle, OUST portal, Facebook/Telegram groups, Course Hero, Studocu, Chegg, Quizlet, Keep/Notion setups, campus book market). Headline: the real competition is scattered chat groups plus a legacy portal; the global note marketplaces are USD-priced and curriculum-generic. Our edge: Obour-specific timetable/GPA/attendance tools, a free-first curated vault, Arabic-first UX, and an integrity-first tutor.

## 3. Features
**On par with best-in-category:**
- Timetable: weekly schedule per department/year/section, today's-lecture card with live countdown, hall directory, cancellation/urgent notice banner, .ics export to phone calendar, offline PWA cache for the whole semester.
- Notes vault: organized Year > Department > Subject > Doctor; PDF/DOCX viewer; 1-click download; search; upload with ownership/agreement confirmation; takedown form.
- Exams and practice: past exam archive, quiz runner with persisted attempts, AI-generated practice quizzes built from the course's own notes with citations.
- GPA tools: Egyptian credit-hour GPA simulator, "grade needed for target GPA" calculator, transcript PDF parser that auto-populates history locally in the browser.
- Planner: study tasks, assignment board, exam countdown hero, absence tracker against the 25% deprivation rule ("(unsourced, verify)" until the official regulation is cited).
- Community: Q&A threads per subject, course difficulty ratings, study-group board, anonymous feedback box, used-book/tool marketplace with direct WhatsApp contact.
- Accounts and settings: Google sign-in, profile, notification preferences, linked Telegram bot for schedule alerts and reminders.
- Legal and trust: privacy, terms, refunds, cookies, DPA, sub-processors, AI-use note; data export and deletion in one tap.

**Owner's own ideas (ported from TickTick `30-Day Projects Sprint` / `أفكار برامج ومشاريع` and legacy, per PROJECT_MERGE_RECORD):**
- Study-help modules from ideas 24/25/27: hints, practice sets, worked examples, flashcards, mock quizzes (never graded-work solving).
- Campus event registration with QR pass (legacy MASTER_PLAN task 17).
- Telegram daily schedule alert bot bridge (DEEP plan OH-118).
- Grade-appeal runbook guide (DEEP plan OH-120), library catalog checker (OH-119), bus schedule tracker (MASTER_PLAN task 22), peer study-group coordinator (OH-121), course review benchmark (OH-113).
- Grade mirror: manual entry or student-uploaded file only, kept on their account. Default: not built in v1 (recorded decision, same as old plan).

**Explicitly NOT built:** `solve_assignment` / `solve_quiz` modes, deterministic fake fallback solutions, Moodle automation scripts, stored institute passwords, any graded-work submission. All quarantined in legacy; never ported.

## 4. Platform matrix (what v1 includes)
| Platform | v1 state | Notes |
|---|---|---|
| Web (responsive, PWA installable) | in v1 | Next.js App Router; Arabic RTL first, English second; light/dark/system/high-contrast |
| Windows | in v1 via installable PWA | Windows app standard deferred: Tauri/Electron wrapper only if a desktop-only feature appears (ADR) |
| macOS | in v1 via installable PWA | same |
| Linux | in v1 via installable PWA | same |
| Android phone/tablet | M5-M6 | Capacitor wrapper of the web app (per `.sir/MASTER_PLAN.md` wrappers decision); APK/AAB via EAS or local Gradle |
| iOS / iPad | M5-M6 | same Capacitor build; unsigned .ipa for SideStore until paid Apple account |
| Wear OS | post-v1 (ADR) | glanceable next-lecture reminder only if requested |
| watchOS | post-v1 (ADR) | same |
| TV (Android/Apple) | skip v1 | no real big-screen use for a student timetable/notes product; revisit with evidence |
| Car (Android Auto/CarPlay) | skip | no allowed car category fits (per `.sir/PLATFORMS.md`) |
| Widgets / Live Activities | M6 | next-lecture and countdown widgets via Capacitor plugins |
| Browser extension | skip | no use case |

## 5. Architecture (on the shared kit, `plans/SHARED_PLATFORM_KIT.md`)
- **App**: Next.js (App Router) + TypeScript + Tailwind v4 tokens, deployed identically to **Firebase Hosting** and **Vercel** (Vercel imports the GitHub repo via Vercel CLI; same build, same env vars on both; both curl-checked per rule 15). Repo `sirahmed8/sir-education-hub` (private). App version stays 1.0.0.
- **Backend**: Firebase project `sir-education-hub` (own project per rule 13): Auth (Google sign-in, JWKS-verified ID token on server), Firestore (deny-by-default rules, emulator-tested), Firebase Storage for notes files, App Check where available. Decision recorded: older drafts mentioned Cloudflare Pages/D1/R2; superseded by the dual-host and own-Firebase rules. R2 remains a documented scale alternative behind an ADR if Storage egress costs bite.
- **Accounts**: `owner-auth` package pattern - server-verified token, `OWNER_EMAILS`/`OWNER_UIDS` allow-list, email_verified, fail closed; HttpOnly+Secure+SameSite=Strict session cookie; rate limits on auth and AI; no localStorage tokens.
- **Owner-only analytics page**: `/owner` route, server-verified owner token only, real metrics (users, AI cost, subscriptions, errors, content counts). Non-owner gets 403.
- **AI**: `ai-proxy` with the standing fallback chain (Gemini flash-lite -> flash -> any Gemini -> OpenRouter free -> other free -> local), per-project keys, `AI_ENABLED` kill switch, daily cost cap in `config/limits.json`, free users 5 questions per rolling 24h with quota badge, owner unmetered. Tutor is grounded in uploaded notes + `docs/help/*.md`; refuses graded work; eval set of 30 Arabic+English prompts must pass 100% refusal before launch.
- **Billing**: `billing-fallback` - "Subscriptions launching soon" + email lead capture until Paymob keys exist; EGP primary with auto-detected USD/SAR/AED; subscription grants owner all permissions.
- **Legal**: `legal-pack` generated from `data-inventory.yml`, marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch"; Egypt PDPL 151/2020 tasks.
- **Ops**: `/api/health`, nightly Firestore export, weekly dependency update, static status JSON, weekly Arabic Telegram report, emergency alerts; AI daily cost cap.
- **Support assistant**: floating drawer grounded only in `docs/help/*.md`.
- **Skills used for this plan** (from ops/SKILLS_INDEX.md + encyclopedia): sir-skill-library, taste-design-engine, anti-vibecoded-design-system, emil-motion-impeccable, cognitive-product-intuition, modern-ui-ux-design-system, high-conversion-copywriting, mobile-ergonomics-polish, firebase_auth_basics, firebase_firestore, firestore_rules_creation, firebase_security_rules_auditor, vibe-auth-hardening, zero-trust-security-hardening, legal-compliance-shield, omniroute-resilience-gateway, database-reliability-transactions, production-engineering-standards, react-best-practices, nextjs, verification, skills-discovery-engine.

## 6. Premium quality bar
- Apple-level motion: spring physics (stiffness 400/damping 30 micro, 300/28 layout), transform+opacity only, 120Hz-safe, reduced-motion path, matching open/close for every sheet/drawer.
- Arabic (Egyptian student tone) RTL-first and English; per-character bidi detection in inputs; `<bdi>` isolation for mixed text; Cairo/IBM Plex Sans Arabic + Inter pairing; `tabular-nums` on numbers.
- Five states on every view: idle, skeleton matching final geometry, empty with one CTA, error with Retry, populated with cursor/keyset pagination fine at 1,000+ items.
- Accessibility: WCAG 2.2 AA, 44px targets, full keyboard nav, focus visible, 320px to 4K, zoom 80-200%.
- No AI slop: no purple-blue gradients, no sparkle icons, no emoji headings, no pill-button spam, no hype words, no em-dashes in copy, no fake counts or reviews.
- Signature interaction (from `.sir/DESIGN.md`): "today plan" card turning the next exam into a countdown ring plus a three-step study path; Dynamic Island active-only tab bar.

## 7. Free tier and pricing (EGP primary, USD/SAR/AED auto-detected)
- **Free**: full timetable, hall directory, notes browsing and downloads, exams archive, quiz attempts, GPA simulator, planner, attendance tracker, 5 AI questions per rolling 24h, marketplace browsing.
- **Pro** (test price, "(unsourced, verify)" until 10 student interviews): 49 EGP/month or 399 EGP/year (~$1 / $8 placeholder pending FX check) - unlimited AI tutor, offline note packs, exam simulator mode, priority upload storage. Marketplace business listing: 30 EGP/semester (from `.sir/MASTER_PLAN.md`, unsourced).
- **Fallback**: until Paymob/Fawry keys exist, CTA reads "Subscriptions launching soon" with email capture; never a broken checkout.
- Owner gets all Pro features free; subscription grants owner all permissions.

## 8. Milestones M0-M6 (acceptance tests)
| Milestone | Scope | Acceptance test |
|---|---|---|
| **M0 Foundations + Desktop kit** | Repo scaffold (exists), `.sir/` kit (exists), Firebase project `sir-education-hub` + Vercel import, CI green, **recreate the Desktop folder kit from scratch** (`folder.ico`, SIR Projects shortcuts, Versions.txt 1.0.0) | `npm run build` exit 0; `/api/health` 200; `gh run list` green or local verify pasted (CI quota flag rule); Desktop folder exists with real shortcuts and folder.ico; sign-in brand check screenshot shows no Firebase project id |
| **M1 Core slice** | Google sign-in, subject list, note viewer, quiz runner with persisted attempts; deploy to both hosts | Sign in -> subject -> note -> quiz attempt saved in Firestore (emulator e2e); both Firebase and Vercel URLs curl 200 |
| **M2 Content parity** | Import script `--dry-run` for legacy Firestore data; timetable + GPA simulator + hall directory from DEEP plan OH-101..105 | Dry run prints counts matching legacy; timetable query <5ms; GPA calculator computes required grades correctly on test vectors |
| **M3 Security, legal, billing, owner page** | Deny-by-default rules + emulator tests, forged-token 403, billing fallback, legal pages, `/owner` analytics | Forged token 403 in CI; `/owner` 403 for non-owner; pricing shows "Subscriptions launching soon" + lead capture creates one Firestore doc |
| **M4 AI tutor + quality** | ai-proxy chain, quota badge, tutor eval, support assistant, five-state audit, Lighthouse | `npm run eval:tutor` 100% refusal on 30 prompts; badge shows "3 / 5" correctly; Lighthouse mobile 90+; screenshots 390/1280 LTR/RTL light/dark archived |
| **M5 Community + marketplace** | Q&A, course reviews, study groups, book marketplace, Telegram schedule bot | Post -> moderation -> visible flow e2e; marketplace listing contact flow tested; bot sends daily schedule at 07:30 Cairo time |
| **M6 Mobile + release** | Capacitor Android/iOS builds, widgets, domain + dual-host cutover, legacy keys rotated, `legacy/` moved to old projects per merge record | APK installs and signs in on a real device; both hosts serve the domain; old Firebase admin keys rotated; checkpoint records both live URLs |

## 9. First 10 tasks for free agents
Written and queue-ready in `ops/briefs/sir-education-hub-tasks.md` (T1-T10: deep scan, secrets report, scaffold, Firestore rules, auth, notes viewer five states, import dry-run, tutor eval, pricing fallback, CI).

## 10. Risks and open questions (defaults)
- Content rights: only notes classmates own and agree to publish; takedown form + upload agreement; default conservative.
- Paying capacity unknown: test price with interviews; keep Pro cheap; no dark patterns.
- Large legacy (62k lines, 24+ files >530 lines): port by feature, never copy wholesale.
- Unverified market claims: every competitor number without a link stays "(unsourced, verify)"; sourcing tasks listed in the competitor file.
- Result-day traffic spikes: static/edge-cached public pages (timetable, hall directory, grade-lookup-free design) so the portal stays up when the official SIS falls over.

## 11. Only the owner can do
Buy the domain; create/confirm Firebase project `sir-education-hub` sign-in and OAuth consent screen; create Paymob/Fawry accounts and paste keys into `.env` (never git); rotate the two legacy Firebase admin keys found in `legacy/Obour Academic Hub/`; consent from classmates contributing notes; lawyer review before paid launch; Search Console/Bing sign-in; Apple Developer account when iOS store submission is wanted.
