# PLAN: SIR Life (Wave 6, GLOBAL product, Part A already partly built)

## Vision (owner, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` final product list)

SIR Life is one calm daily life OS for people who want their day to make sense: prayer times that shape the plan, habits that forgive a missed day, reminders for water, medicine, food and gym, money and expenses in one place, and a daily brief that tells the truth about what happened. Arabic first, English second, private by default, and useful offline.

- Part A is Ahmed's private life organiser: calendar bridge, Telegram reminders, daily brief, read-only Gmail triage and approval-gated drafts, local JSON under ignored `data/`. It stays personal, unlisted and never mixed with AHome or Habiba data.
- Part B is the global consumer product: accounts, subscriptions, owner-only analytics, encrypted optional sync, Arabic and English, web plus mobile, all planned platforms, and the same premium standard as every SIR product.
- The accessibility map idea (TickTick idea 26) is a module of Part B, not a separate product, per `plans/accessibility-map-module-note.md`.

**Version 1.0.0.** Audited and rewritten 2026-11-12 (round r52, HQ). Supersedes the r44 text of this file, which the git history keeps. The canonical competitor study is `D:/Projects/_SIR/ops/competitors/sir-life.md` (opened sources dated 2026-11-12). The first ten build tasks for the free agents are in `D:/Projects/_SIR/ops/briefs/sir-life-tasks.md`.

**Truth rule for this plan.** Nothing here is called working unless a reviewer saw it today. Verified today in `D:\Projects\SIR Life`: `pnpm install` completed with TypeScript 5.9.3, `pnpm run typecheck` passed, `pnpm run build` passed, and `node --test dist/tests/**/*.test.js` passed 65 tests in 18 suites with 0 failures. The private repo `sirahmed8/sir-life` exists and `main` tracks `origin/main`. Not verified today: the Firebase project for this product, the public domain, payment keys, store accounts and any Part B screen. The product folder also has uncommitted `.sir` documentation changes that revert the checkpoint text toward the pre-build state; code and tests are unaffected and the working tree was left untouched because this round is scoped to `_SIR`.

**Product class: GLOBAL for Part B.** Anyone in the world can use it, accounts and subscriptions exist, every platform is planned, the owner has an owner-only analytics page, the site is hosted twice (Firebase and Vercel), and a paid subscription gives the owner every permission inside the product. Part A remains PERSONAL and is not a public product.

---

## 1. Who it is for, and the promise

**For the daily user.** The person who wants prayer times, habits, water, medicine, food, gym, expenses and a little calm in one place, without five subscriptions and without handing daily health data to an ad-supported feed.

**For Ahmed.** The same engine, run privately, keeps his calendar honest, sends Cairo-time Telegram reminders, triages Gmail read-only and drafts replies only after approval.

The one-sentence promise, in the words a user would use:

> Open SIR Life and see your whole day already arranged around prayer, with habits that forgive you and reminders that respect your quiet hours.

**The end state we sell.** A user opens the app in the morning and sees today's prayer times for their chosen method and city, the tasks that matter, habits due, water and medicine reminders, yesterday's food and gym entries, and one honest line about what is unfinished. They tap once to log water, check in a habit, mark a medicine taken, add an expense or start a focus block. The day bends around prayer instead of competing with it. If they miss a habit, the streak pauses gently and offers a rest day, not a lecture. Their data stays on the device until they choose encrypted sync.

**Not in v1:** no ads, no fake streaks, no invented religious rulings, no medical dosing advice, no public leaderboards of private health data, and no paywall on the core daily organiser.

---

## 2. Names, IDs and current state

| Item | Value |
|---|---|
| Product folder | `D:\Projects\SIR Life` |
| Private GitHub repo | `sirahmed8/sir-life`, default branch `main` |
| Stack today | Node.js + TypeScript 5.9.3, pnpm, `engine/`, `cli/`, `packages/core`, `packages/data`, `tests/` |
| Verified today | `pnpm run verify` equivalent: install, typecheck, build and 65/65 tests green on 2026-11-12 |
| Part B stack default | `apps/web` Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4; `apps/mobile` Expo for Android and iOS; shared `packages/core`, `packages/data`, `packages/ui`, `packages/kit`; Firebase Auth + Firestore; hosting on Firebase and Vercel |
| Domain candidates | `sirlife.app` or an `.eg` name, owner checks availability and price "(unsourced, verify)". Until then Firebase and Vercel default URLs |
| Firebase project | To be created and named `sir-life`, separate from every other SIR product. Not verified today |
| Payment | Paymob and Fawry in test mode first, Stripe later if needed; keys are owner actions. "Subscriptions launching soon" + email capture until keys exist |
| Version | Required `1.0.0` everywhere. Current `package.json` still shows `0.1.0`; T1 in `ops/briefs/sir-life-tasks.md` must set and verify it |

**Current state, honestly:** Part A is real and tested. Part B is planned, not built. The old `.sir/MASTER_PLAN.md` describes a Next.js personal app, the older `plans/sir-life-DEEP.md` describes a more personal "Cairo Prayer Sentinel" vision, and `plans/sir-life.md` before this rewrite described an Expo-first Part B. This file is now the source of truth: Part A stays private and Part B is the global product on the shared kit.

---

## 3. Competitors and our edge

Full study: `D:/Projects/_SIR/ops/competitors/sir-life.md` (read on 2026-11-12).

| Competitor | What it proves | Our edge |
|---|---|---|
| Muslim Pro | Prayer times, Qibla, Quran, dhikr, widgets and verified times are table stakes | A calmer daily routine, local-first private data, no ads, prayer-aware habits |
| Athan | Native prayer apps can feel polished and personal | One daily screen for the whole life, not only prayer alerts |
| AlAdhan API | Prayer calculation methods and data quality are solvable | We validate against it but keep an offline local engine so users are not locked to one API |
| Habitica | Habits can carry XP, parties and history | Forgiving streaks, no shame mechanics, private by default |
| Streaks | A small habit set can feel premium | Cross-platform, Arabic-first, broader life modules |
| Fabulous | Routine structure and coaching retain users | Free core routines offline, no dark-pattern paywall, EGP pricing |
| Todoist | Task speed and reminders are expected | Habits, prayer, water, medicine, food and expenses in one calm place |
| TickTick | All-in-one breadth is possible | More core habits free, prayer-aware planning, local-first privacy |
| Headspace | Calm content has value | Calm tools that work offline without a required content subscription |
| MyFitnessPal | Food logging is worth paying for | One fair subscription for the whole day, local-first, no medical claims |

**Category truth from the sources:** Muslim apps are feature-dense, habit apps sell streaks, food and wellness are separate subscriptions, and Arabic-first local privacy is still under-served. SIR Life wins by being quieter, more private and more complete for daily life.

---

## 4. Features

### 4.1 Parity with the best in the category, must ship

| Feature | Why it is in the list | Source of the requirement |
|---|---|---|
| Prayer times for a chosen city and method, Cairo and Egyptian General Authority defaults | Table stakes for the audience | Muslim Pro, Athan, AlAdhan API |
| Prayer alerts with quiet hours, snooze and DST-safe Cairo handling | Daily usefulness without annoyance | Athan, Muslim Pro; existing Part A tests |
| Qibla direction | Expected in a prayer-aware app | Muslim Pro, Athan |
| Adhkar and dhikr counter with cited text only | Core daily spiritual routine | Athan, Muslim Pro; `prompts/PRODUCT_PROMPT.md` |
| Fasting countdown for Suhoor and Iftar when relevant | Seasonal daily need | Muslim Pro features page |
| Habits with forgiving streaks, rest days, freezes and history | Retention without shame | Habitica, Streaks, Todoist, TickTick |
| Tasks and routines with reminders, recurring items and quick add | Daily organiser baseline | Todoist, TickTick |
| Water reminders and intake log | Common health habit | MyFitnessPal, WaterMinder second ring |
| Medicine reminders with snooze and "taken" log, no dosing advice | Elderly and chronic-care usefulness | Owner ideas; medical safety boundary |
| Food log with calories, macros and water later, local-first | Parity with food trackers | MyFitnessPal |
| Gym and workout log with weight history | Owner idea and common tracker | TickTick legacy ideas; owner notes |
| Expense tracker with categories and monthly review | Life admin baseline | Owner ideas; common finance apps |
| Mood and energy check-in plus evening reflection | Calm daily close | Daylio second ring; Headspace prompts |
| Focus timer and breathing/meditation timer | Calm productivity | Fabulous, Headspace, TickTick pomodoro |
| Sleep and eye-rest reminders | Screen-time health | Headspace sleep page |
| Calendar bridge and .ics export for the user's own calendar | Interop without lock-in | Part A already has sync; Todoist/TickTick parity |
| Widgets, complications and watch surfaces later | Native feel | Athan, Streaks, TickTick |
| Arabic RTL and English shipped together | Market gap and owner rule | All competitors are global-first |
| Five UI states on every screen | Premium floor | `standard/23-premium-code-bar.md` |
| Data export and one-tap deletion | Trust and legal baseline | MyFitnessPal account model; privacy promise |
| Accessibility map module for accessible places | Owner idea 26, decided as Part B module | `plans/accessibility-map-module-note.md` |

### 4.2 The owner's own ideas, carried forward

There is no `legacy/` folder in `D:\Projects\SIR Life`; the product folder was created after the legacy consolidation pattern and the source material is the current engine plus the TickTick note mapped in `plans/PROJECT_MERGE_RECORD.md` and `prompts/PRODUCT_PROMPT.md`. Every line says where it came from.

| Idea | Source | Status in this plan |
|---|---|---|
| Prayer-aware routine and daily brief | `prompts/PRODUCT_PROMPT.md`, current Part A daily brief | Part A now, Part B M2 |
| Adhkar, wird and Quran reminders with cited sources | `prompts/PRODUCT_PROMPT.md` | Part B M3, text only from verified sources |
| Habit tracking with forgiving streaks | TickTick ideas via merge record, `PRODUCT_PROMPT.md` | Part B M2 |
| Medication and water reminders | `PRODUCT_PROMPT.md`, owner daily-life need | Part B M2/M3 |
| Food, calorie and gym tracking | `PRODUCT_PROMPT.md`, TickTick-style life admin | Part B M3/M4 |
| Expense tracking | `PRODUCT_PROMPT.md`, owner ideas | Part B M3 |
| Skill plans and personal development | `PRODUCT_PROMPT.md` | Part B M4 |
| Forgetting reminders for bills, exams, renewals | TickTick countdown idea, owner note | Part B M3 |
| Calm breathing, meditation and focus | `PRODUCT_PROMPT.md`, competitor parity | Part B M3/M4 |
| Accessibility map of accessible places | TickTick idea 26, `plans/accessibility-map-module-note.md` | Part B M5 module |
| Telegram quick logger and daily brief delivery | Current Part A Telegram client and listener | Part A now, Part B M4 as opt-in bot link |
| Read-only Gmail triage with approval-gated drafts | Current Part A `engine/` Gmail path | Part A only; never in the global product without a separate privacy review |
| Web-to-app wrappers and desktop folder kit | Workspace standard and owner defaults | M0 and M5/M6, not a user feature |

**Explicitly dropped or deferred:** no medical diagnosis, no dosing suggestions, no Quran text that is not verified against a cited source, no health claims, no ads, no selling of health data, no fake prayer times for unverified cities, and no copying competitor assets or wording.

---

## 5. Platform matrix

Standing rule (owner, 2026-11-12): every product ships on all platforms, so web, Windows, macOS, Linux, Android and iOS are all required for SIR Life. Wear OS, watchOS, TV and car are not in that list for v1, so they are planned later with a written reason, not left in silence.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required | Marketing site, legal pages, pricing, web app, owner dashboard, help centre, PWA install | Nothing pending |
| PWA (installable, offline) | Required | Install from browser, offline Today screen, prayer times, local data, background sync when online | Native shell only if PWA proves weak on low-end Android |
| Android phone and tablet | Required (M4) | Expo app: same account, Today screen, habits, reminders, local storage, optional sync | Play Store when the reinvestment ladder allows; Wear OS after that |
| iPhone and iPad | Required (M4) | Expo app, same account and data, tablet layouts, iOS widgets later | App Store or SideStore when the owner has a paid Apple account |
| Windows | Required (M5) | Installable PWA from day one, then an Electron or Tauri shell decision in an ADR, same sign-in and self-update | Signed installer when the owner buys a certificate |
| macOS | Required (M5) | Installable PWA from day one, then the same desktop shell as Windows | Signed build when the owner has an Apple account |
| Linux | Required (M5) | Installable PWA from day one, then AppImage and .deb from the same desktop shell | Signed package |
| Wear OS | Planned (M6) | Nothing in v1 | Prayer countdown, habit check-in and water reminder complications |
| watchOS | Planned (M6) | Nothing in v1 | Same surfaces as Wear OS, decided with the same ADR |
| TV (Android TV and Apple TV) | Skipped in v1 | Nothing | A family/kiosk prayer-times screen only if users ask |
| Car (Android Auto and CarPlay) | Skipped in v1 | Nothing | Audio adhkar or prayer-time announcements only if a paid tier needs it |
| Browser extension | Skipped | Nothing | No browser use case that justifies the review |
| Docker and self-host | Skipped for consumers | Nothing | Part A remains local-first for Ahmed; Part B sync is hosted |

**Rule:** every platform shares one Firebase project, one account and one dataset for Part B. Local-first storage is the default on every client; cloud sync is opt-in and encrypted. Part A stays separate and local.

---

## 6. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. SIR Platform was cancelled as a project on 2026-11-12, so there is no extraction target; SIR Life adopts the kit sections as internal `packages/*` with the kit names and interfaces. Part B is GLOBAL, so it adopts accounts, owner analytics, AI fallback, legal pack, dual hosting and all-platform planning. Part A stays a private Node/TS engine and only shares proven pure modules after they are extracted and tested.

### 6.1 Shape

```
apps/web        Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens
apps/mobile     Expo app for Android and iOS (M4)
apps/desktop    Desktop shell decision in an ADR at M5, same web bundle where possible
packages/core   Domain types and zod schemas: PrayerDay, Habit, Task, Reminder, WaterLog,
                MedicineLog, FoodEntry, Expense, MoodCheckIn, User, Subscription
packages/data   Local repositories first (IndexedDB/local SQLite on mobile, JSON/SQLite on desktop),
                optional encrypted Firestore sync repositories, emulator tests
packages/ui     Shared UI kit: InputBox, TabBar, BottomSheet, Card, Chip, Modal, Toast, Skeleton
packages/kit    owner-auth, signed-webhook, billing-fallback, ai-proxy, legal-pack, i18n,
                help-center, notifications, privacy-chokout reuse from Part A
engine/         Part A private life organiser (calendar bridge, Telegram, Gmail triage, daily brief)
cli/            Part A operator commands
packages/core   Shared pure domain code; Part A modules stay private and unlisted
tests/          Part A and shared package tests
docs/           Help centre source, legal source, env names, decisions, ADRs
scripts/        Verify, seed-free checks, emulator tests, Lighthouse, AI evals, icon/desktop kit
```

Layers depend inward only: presentation, domain (no I/O), data, core. Files under 300 lines, no `any`, no god components, absolute imports. Part A code is never imported by Part B screens; shared pure functions move only after extraction and tests.

### 6.2 Accounts (`owner-auth`)

- Firebase project named `sir-life`, created and verified before any Part B code depends on it. Never reuse another product's project.
- Google sign-in through Firebase Auth on web and mobile; email and password later if needed. ID token verified on the server with JWKS for sensitive routes.
- Owner and admin rights come from `OWNER_EMAILS` and `OWNER_UIDS`, fail closed. Nothing in the client decides a privilege.
- Web session in an HttpOnly, Secure, SameSite=Strict cookie. No tokens in localStorage. Mobile uses the Firebase SDK session plus Firestore rules.
- Rate limits on sign-in, sync writes, uploads, AI calls and webhooks.
- Owner accounts get a second-factor offer.
- Tests: a forged token gets 403, a client-side flag flip gets nothing, a non-owner token on `/owner` gets 403, and a revoked session cannot write.

### 6.3 Owner-only analytics page

- Route `/owner`, server-verified owner token, 403 for everyone else.
- Real metrics only, read from aggregates not raw collections: signups, active users, retention curve, free-to-Pro conversion, MRR in EGP and visitor currency, churn, AI cost, sync conflicts, error rate, notification delivery failures.
- No invented numbers anywhere: an empty metric shows a dash and the reason, never a zero dressed as a fact.
- Owner sees every permission inside the product because the subscription check grants owner all Pro features.

### 6.4 AI with the fallback chain

Chain from `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`: Gemini `flash-lite-latest`, then `flash-latest`, then any Gemini text model, then OpenRouter free models, then other free providers, then the local model on this PC. One Gemini key and one OpenRouter key for this product, created on the `sir-life` Firebase/Google project or the product's own provider accounts, stored only in the ignored env file and the hosting environment, never printed and never committed.

What AI does in Part B, and what it must never do:

| Feature | AI role | Hard rule |
|---|---|---|
| Daily plan suggestion | Draft a calm day plan from the user's own tasks and prayer times | Uses only the user's own data, never another user's data |
| Reflection prompt | Suggest one question for the evening check-in | Optional, off by default for health-adjacent notes until consent is explicit |
| Support assistant | Answer from `docs/help/*.md` only | Refuses anything not in the help source and says so |
| Food photo estimate later | Estimate portion size from a photo | Advisory only, user confirms, no medical or diet prescription |
| Weekly owner report draft | Draft the summary the Telegram sender sends | Numbers come from the database; the model only writes the sentence |
| Religious text | None in v1 | No AI-generated Quran, hadith, fatwa or ruling text. Cited sources only |

Free users get a small visible AI quota for support and plan suggestions, the owner is unmetered, `AI_ENABLED` is the kill switch, a daily cost cap lives in `config/limits.json`, and every call logs which provider answered, never the content. Arabic and English eval sets exist before any AI feature ships, and the runner exits non-zero below the threshold.

### 6.5 Data, privacy and money

- Local-first storage is the default on every client. Cloud sync is opt-in, end-to-end encrypted where the shared kit defines it, and never required for the core daily organiser.
- Firestore rules deny by default for Part B synced collections, check `request.auth` on every read and write, scope every document to `owner_uid`, and are tested in the emulator including a cross-user read that must fail.
- Health-adjacent data (medicine, food, mood, water) stays local unless the user enables sync for that category. The privacy page states exactly what leaves the device.
- Part A keeps its existing privacy chokepoint: `packages/core/src/sanitize-outbound.ts`, `packages/data/src/telegram-client.ts` as the only Telegram Bot API caller, and `packages/data/src/outbound-files.ts` for outbound files. These remain Part A private and are not exposed to Part B.
- Money is stored in integer piasters/cents for expenses and subscriptions, with rounding tests. Subscription state is checked server-side; client flags grant nothing.
- Payments through Paymob and Fawry in test mode first, Stripe later if needed. The webhook is signature-verified server-side only, and tampered, replayed, unsigned and wrong-timestamp events are rejected. Until keys exist, pricing shows "Subscriptions launching soon" and captures a lead.
- Currency is EGP-first with USD, SAR and AED support, auto-detected from locale/IP with a manual override. Dates and times use `Intl` and the user's chosen timezone, with Cairo DST handled by the existing tested engine.

### 6.6 Hosting and delivery

- Firebase project `sir-life` is primary for Auth, Firestore, Functions if needed and Hosting/App Hosting. Vercel is the second host for `apps/web`, same repository imported with the Vercel CLI, same build and same environment variables on both.
- Both addresses are curl-checked and written into the project checkpoint. While `ops/ci-quota-exhausted.flag` exists, local verification is the recorded signal.
- Secrets, webhooks, AI calls and owner analytics live server-side only. The client bundle never contains provider keys.
- A service worker caches the Today shell, prayer times and local data. Background sync queues writes when the connection returns and resolves conflicts with the documented last-writer-wins-per-field or server-order rule decided in an ADR.
- Daily Firestore export to a private bucket for Part B synced data, monthly restore test, `/api/health`, status JSON, nightly error digest and weekly Telegram report at a round hour.

### 6.7 Security baseline

Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI. CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent, with Reject All as prominent as Accept. One-tap data export and one-tap deletion for Part B accounts. Rate limits on auth, sync, uploads, AI and webhooks. No fake data in any path a user can see.

---

## 7. Premium quality bar

This is the floor from `standard/23-premium-code-bar.md`, `plans/GEMINI_QUALITY_CHARTER.md` and the master production directive, written for this product.

**Motion, Apple level.**

- One shared spring config across the app: stiffness 300 to 400, damping 28 to 30, transform and opacity only, no layout thrashing, 120 Hz safe.
- Every sheet, drawer, modal and panel opens and closes with the same spring. An open-only animation is a defect.
- The Today screen is the signature surface: prayer times settle into the day plan with a soft reorder, habit check-ins land under 100 ms, and streak changes use a gentle count rather than a explosion.
- Micro-interactions 100 to 150 ms, standard 200 to 300 ms, large 300 to 500 ms. Press scale 0.98. Reduced-motion path for every animation.
- The active tab shows its label and the others show an icon only, the active tab scrolls into view on load and on change, and the bottom bar never vanishes when the keyboard opens.
- Skeletons match the final geometry, optimistic feedback lands under 100 ms, and no white flash on theme change.

**Two languages, one layout.**

- Arabic first for the product voice, English second for the international market. Both shipped together, never one as a partial translation. MSA only in legal pages; Egyptian Arabic can appear in onboarding and help where it sounds natural.
- RTL designed first: logical CSS properties only, flipped directional icons, Arabic line heights, never a mirrored afterthought.
- Every text input detects Arabic or Latin per character as the user types and moves the caret and the direction live. Every mixed run is isolated with `<bdi>` or `unicode-bidi: isolate`. The words "RTL" and "LTR" never appear to the user.
- Currency auto-detected from the visitor locale and IP, with a manual override on top. Dates and times formatted with `Intl`.
- Arabic typography uses a proper Arabic face with correct line height; numerals can be Latin or Arabic-Indic by user preference.

**Five states on every screen.**

Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake habit, a fake prayer time or a fake number. A missing prayer calculation shows the method and city controls, not invented times.

**Accessibility.**

- WCAG 2.2 AA target, keyboard complete, focus visible, 44 px touch targets, high-contrast theme, reduced motion, screen-reader labels in Arabic and English.
- Color is never the only signal for prayer state, habit status or errors.
- The accessibility map module inherits the same rules and adds accessible-POI filters.

**Responsive.**

- 320 px to 4K, no horizontal overflow, foldables and tablets included. Desktop uses the same design tokens as web and mobile.

---

## 8. Free tier and fair pricing

Prices are proposals to validate with real users, not final public claims. Every public price page must carry a link to the pricing source and a date, or "(unsourced, verify)" until checked.

| Tier | Price proposal | What it includes |
|---|---|---|
| Free | 0 | Full local-first daily organiser: prayer times, habits, tasks, water, medicine, food log basics, expenses, mood check-in, breathing/focus timers, widgets where supported, Arabic and English, export and deletion. No ads. |
| Pro monthly | 79 EGP/month proposal "(unsourced, verify)" | Encrypted multi-device sync, cloud backup, Telegram quick logger for Part B users who opt in, priority support, advanced reports, accessibility map contributions at higher limits |
| Pro yearly | 699 EGP/year proposal "(unsourced, verify)" | Same as monthly, billed yearly, launch price for early users |
| USD fallback | $2.99/month or $24.99/year proposal "(unsourced, verify)" | Same Pro features for non-EGP visitors, auto-detected with manual override |
| Owner | Free forever | Owner account gets every Pro permission inside the product |

**Fairness rules:** no ads, no selling health data, no dark-pattern countdowns, cancel is as easy as sign-up, refunds follow the published policy, and until payment keys exist the pricing page shows "Subscriptions launching soon" plus an email capture that writes a Lead document.

---

## 9. Milestones M0 to M6 with acceptance tests

| Milestone | Goal | Acceptance test |
|---|---|---|
| M0 | Product folder kit is real and honest | `D:\Projects\SIR Life` has the full `.sir` file set, `assets/brand` icon, `scripts/dev-start.ps1` and `dev-stop.ps1`, Desktop shortcuts under `Desktop/SIR Projects/SIR Life` open/start/stop correctly, `pnpm run verify` is green, checkpoint says exactly what exists, version is `1.0.0` |
| M1 | Part B foundation: monorepo, Firebase project, auth, rules | `apps/web` builds, `apps/mobile` scaffolds, `packages/*` compile, Firebase project `sir-life` exists and is recorded, `owner-auth` fails closed, emulator tests prove cross-user reads fail, `/api/health` returns real status |
| M2 | Today screen and core daily modules | Prayer times render for Cairo and a second city with the chosen method, habits/tasks/water/medicine check-ins persist locally, five states verified at 320/390/768/1280 px in Arabic and English, offline reload works, no fake data |
| M3 | Sync, billing fallback, legal and owner page | Opt-in encrypted sync round-trips between two browsers, Firestore rules tested, pricing page shows launch mode until keys exist, legal pages exist at `/legal/*`, `/owner` returns 403 for non-owner and real metrics for owner, dual hosting curl-checked on Firebase and Vercel |
| M4 | Android and iOS apps | Expo apps install on test devices or emulators, same account and local data, push notifications for prayer/medicine/water with quiet hours, app-store assets drafted, no health data leaves device without consent |
| M5 | Desktop shells, Telegram opt-in, accessibility map module | Windows/macOS/Linux installable PWA verified, desktop shell ADR decided and built if chosen, Telegram bot link works for opted-in users only, accessibility map submissions are moderated and PDPL-safe |
| M6 | Wear OS/watchOS decision, store readiness, launch polish | Watch surfaces decided by ADR, store listings drafted with truthful screenshots, support assistant evals pass in Arabic and English, restore test passes, launch checklist complete, legacy review confirms `legacy/` still intact where it exists |

**Exit rule for every milestone:** the verify command passes, the CI run is seen green or the quota flag is recorded with full local output, the checkpoint is updated, a report exists in `ops/agy-runs/reports/`, and nothing is called working unless it was seen that day.

---

## 10. Skills used for this plan

Selected from `ops/SKILLS_INDEX.md` and the deep digests; no new skill was installed.

- `sir-ecosystem-orchestrator` for product-family boundaries and the AHome separation rule.
- `sir-skill-library` for finding the right specialist skills before writing architecture and tasks.
- `agent-supercharged-os` for the plan-test-implement-review loop and carried lessons.
- `firebase_auth_basics`, `firebase_firestore`, `firestore_rules_creation`, `firebase_security_rules_auditor`, `firebase_hosting_basics`, `firebase_app_hosting_basics` for accounts, rules, hosting and owner analytics.
- `modern-app-engineering`, `modern-ui-ux-design-system`, `emil-motion-impeccable`, `anti-vibecoded-design-system`, `a11y-debugging` for the premium bar.
- `database-reliability-transactions` for sync, idempotency and local-first conflict rules.
- `verification` for "nothing is working unless seen today".
- `google_maps_platform` later for the accessibility map and mosque-nearby features.

---

## 11. Risks and open questions

- **Part A versus Part B confusion:** default is strict separation. Part A stays private under `engine/`, `cli/` and existing `packages/*`; Part B lives in `apps/*` and new shared packages. Shared code moves only as pure, tested functions.
- **Prayer calculation correctness:** default is local calculation engine validated against AlAdhan for Cairo and at least two other cities/methods, with the method shown to the user. No invented times.
- **Health-data privacy:** default is local-only for medicine, food, mood and water until the user opts into sync per category. The privacy page must match the code exactly.
- **Monetization timing:** default is free core plus Pro sync/backup. Prices above are proposals; validate with interviews before publishing.
- **Desktop shell choice:** default is installable PWA first, then an ADR between Electron and Tauri at M5 based on bundle size, signing and update needs.
- **Competitor claims:** every public comparison must use `ops/competitors/sir-life.md` sources or "(unsourced, verify)".
- **Store accounts and certificates:** owner actions; nothing here assumes they exist.

---

## 12. Only the owner can do

Buy `sirlife.app` or choose an `.eg` name after checking rules and price; create or confirm the Firebase project `sir-life`; create Vercel, Paymob, Fawry and later Stripe accounts; provide Apple Developer and Google Play accounts when ready; buy code-signing certificates; approve legal review for privacy, terms, refunds and PDPL; recruit beta users; and decide whether Part B gets a public Telegram bot token separate from Part A.

---

## 13. Market-grade and visibility checklist

- Landing page explains the end state in five seconds: prayer-aware day, forgiving habits, private by default.
- `llms.txt`, facts page, help centre, legal pages, pricing page and comparison pages only after competitor sources are current.
- Arabic queries to target later: "جدول صلوات", "تطبيق عادات", "تذكير صلاة", "تنظيم يومي", "تطبيق حياة يومية". Claims must be verified before publishing.
- YouTube demos of real use only after M2/M4; no fake screens or invented users.
- Weekly AI-answer check for "best prayer times app", "habit tracker Arabic", "Muslim daily planner" after launch.

---

## 14. Definition of done for this plan

This plan is complete when `plans/sir-life.md`, `ops/competitors/sir-life.md` and `ops/briefs/sir-life-tasks.md` exist, the bus line is sent, the explicit paths are committed and pushed to `main`, the checkpoint records the real verification output, and the report states what was verified today versus what remains unverified.
