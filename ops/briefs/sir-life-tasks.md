# SIR Life: build task list for the free agents (queue ready)

Round r61, 2026-11-12 (expanded from the r52 ten tasks; the earlier ten are kept as T1 to T10 in the same order so nothing already queued breaks). Source of truth for the plan: `D:/Projects/_SIR/plans/sir-life.md` (sections 15 to 19 are the r61 additions). Product folder: `D:/Projects/SIR Life` (private repo `sirahmed8/sir-life`, branch `main`).

**How to queue these.** One task per agent round, in order. T1 lands first; T2, T3 and T4 can then run side by side (T2 owns the Part B scaffold, T3 owns the Firebase project and auth package, T4 owns the data model and rules); everything from T5 on depends on the scaffold and the auth package. The first ten tasks (T1 to T10) are the ones ready to hand to agents now; later milestones unlock as earlier ones land. Every task starts with the same preamble: read `D:/Projects/AGENTS.md`, `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/_SIR/standard/23-premium-code-bar.md`, `D:/Projects/SIR Life/AGENTS.md`, `.sir/CHECKPOINT.md` and `prompts/PRODUCT_PROMPT.md`, then run `git status` and `git log -5` in the product folder and never revert another agent's edits. Every task ends with the project checkpoint updated, a small commit pushed to `main`, a report in `D:/Projects/_SIR/ops/agy-runs/reports/`, and the done signal `python D:/Projects/_SIR/scripts/agy-done.py <task-id> ok "<one line>"`. No pull requests, no version above 1.0.0, no fake habits, prayer times, users or health data in any path a user sees, `legacy/` is read-only where it exists, `data/` stays ignored, and the AHome folder is never opened.

**Done means the same thing for all tasks:** the verify command passes (typecheck, lint, tests, build, secret scan where present), the CI run was seen green or, while the GitHub Actions quota flag `D:/Projects/_SIR/ops/ci-quota-exhausted.flag` exists, the full local verification output is pasted into the checkpoint, the exit check named in the task was performed on screen with a screenshot in `D:/Projects/SIR Life/.sir/evidence/`, and the report says honestly what was seen and what was not.

**Part A boundary.** Tasks must not break `pnpm run verify` for the existing Part A engine, `cli/`, `packages/core`, `packages/data` and `tests/`. Part A stays private, unlisted and separate from AHome and Habiba data; its Telegram bot, Gmail path and privacy chokepoint are never reused by Part B without extraction into shared tested code.

---
## M0-M1: Foundations, kit, accounts and data

### T1. Repo hygiene, checkpoint truth and version lock

Inspect the uncommitted changes in `D:/Projects/SIR Life` (`git status`, `git diff`) and decide file by file whether each one is intentional work or stale kit text. The known dirty set on 2026-11-12 was `.sir/CHECKPOINT.md`, `.sir/PLAN.md`, `.sir/TASKS.md`, `assets/brand/icon.png`, `scripts/dev-start.ps1` and `scripts/dev-stop.ps1`; the `.sir` edits revert the checkpoint toward the pre-T-100 state while the code and tests already contain T-100 to T-104. Restore or commit the correct state so the checkpoint matches reality: Part A engine exists, 65 tests pass, version is `1.0.0`, and no stale "nothing is built" claim remains. Fix `package.json` version if needed, keep `legacy/` untouched where it exists, keep `data/` ignored, and confirm `pnpm run verify` is green after the cleanup. **Exit check:** `git status` is clean or every remaining change is explained in the checkpoint, `pnpm run verify` output is pasted into the report, and `.sir/CHECKPOINT.md` names the exact verified state. **Acceptance test:** `pnpm run verify` green, `git status` clean or fully explained, `package.json` version reads `1.0.0`. **Skills:** agent-supercharged-os, verification.

### T2. Part B monorepo scaffold, tokens, RTL shell and CI

Create the Part B structure without breaking Part A: `apps/web` (Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4), `apps/mobile` placeholder or Expo scaffold only if it does not destabilise the web build, `packages/core`, `packages/data`, `packages/ui`, `packages/kit`, `docs/`, `scripts/`, with layers depending inward only, files under 300 lines, absolute imports and no `any`. Seed design tokens from the product seed direction with light, dark, system and high-contrast themes, logical CSS properties only, an RTL-first Arabic stylesheet and a proper Arabic face. Add a root `verify` script that runs typecheck, lint, tests, build and secret scan where available, plus a GitHub Actions workflow that runs exactly that on `main`. Add `/api/health` returning real status values, never fake ones. **Exit check:** `pnpm verify` runs and the output was seen green. **Acceptance test:** fresh clone runs `pnpm install && pnpm verify` green; `/api/health` answers with real values; shell screenshots exist in Arabic and English at 390 px and 1280 px. **Skills:** nextjs, firebase_basics, modern-ui-ux-design-system.

### T3. Firebase project `sir-life` and `owner-auth`

Create or confirm the Firebase project named exactly `sir-life` on the free Spark plan where possible, keep it separate from every other SIR product and never reuse another project's config. Put the project id in `.firebaserc` in the product root and keep all keys in ignored env files. Build `packages/kit/owner-auth`: Google sign-in through Firebase Auth, server-side ID token verification with JWKS, an owner and admin allow-list that fails closed, the web session in an HttpOnly, Secure, SameSite=Strict cookie with no token in localStorage, rate limits on sign-in, and a second-factor offer for owner accounts. Write the negative tests: a forged token gets 403, a client-side flag flip grants nothing, a non-owner token on the owner route gets 403. **Exit check:** the three negative tests run and fail in the expected way, owner sign-in works in the browser on screen, and no key is printed or committed. **Acceptance test:** forged token 403, flag flip grants nothing, non-owner 403 on `/owner`, owner sign-in visible on screen. **Skills:** firebase_auth_basics, vibe-auth-hardening, firebase_security_rules_auditor.

### T4. Part B data model, local-first repositories and Firestore rules

Write the Part B data model and `firestore.rules` for User, Preferences, PrayerLocation, PrayerDay, Habit, HabitCheckIn, Task, Reminder, WaterLog, MedicineLog, FoodEntry, GymLog, Expense, MoodCheckIn, Reflection, Subscription, Lead and AccessibilityPOI. Document each collection in `docs/data-model.md` with fields, indexes and access rules, plus the sync-crypto design in one plain paragraph (key derivation, what is encrypted before it leaves the device). The rules deny by default, check `request.auth` on every read and write, scope every synced document to `owner_uid`, and let a user read only their own data. Health-adjacent collections are local-first by default and sync only when the user enables that category. Write emulator tests proving a cross-user read fails, a forged role claim fails, and a write without auth fails. **Exit check:** the emulator tests pass with real output in the report and the rules compile with no warning. **Acceptance test:** cross-user read fails in emulator, forged role claim fails, unauthenticated write fails, rules compile warning-free. **Skills:** firestore_rules_creation, firebase_firestore, firebase_security_rules_auditor, database-reliability-transactions.

---
## M2: Today screen and core daily modules

### T5. Prayer engine, prayer day schema and calculation tests

Build `packages/core/prayer` with no I/O: prayer times for a chosen city and method, Cairo and Egyptian General Authority defaults (prefer the official published timetable for Egypt where available, per plan section 15 R9), Umm al-Qura and Muslim World League alternatives, Hijri date conversion, Qibla bearing, Sunnah times where defined, quiet-hours-aware alert scheduling, DST-safe Cairo handling and timezone-aware `Intl` formatting. Validate against AlAdhan API output for Cairo and at least two other cities or methods, recording the request date and deltas in `docs/prayer-validation.md`. Never invent times: if calculation inputs are missing, the UI asks for city and method, and the UI always badges which source or method produced the times. **Exit check:** unit tests cover Cairo DST boundaries, method switching, midnight edge cases and a validation table against AlAdhan with deltas inside the documented tolerance. **Acceptance test:** validation table in `docs/prayer-validation.md` with real deltas inside tolerance; DST boundary tests pass; missing inputs produce a city/method prompt, never invented times. **Skills:** production-engineering-standards, verification.

### T6. Today screen: prayer times, tasks, habits, water and medicine

Build the first real Part B screen in `apps/web` at `/today`: prayer times for the chosen city and method, the next task, habits due today, water and medicine reminders, and one honest line about unfinished items. All check-ins write to the local repository first and work offline; sync is a later task. Implement the five states on every panel, skeletons matching final geometry, optimistic feedback under 100 ms, 44 px targets, Arabic RTL and English LTR, light/dark/system/high-contrast, and no fake data. **Exit check:** Playwright or equivalent screenshots at 320, 390, 768 and 1280 px in Arabic and English, light and dark, plus an offline reload test that still shows the last local data. **Acceptance test:** five states on every panel, offline reload shows last local data, no fake values anywhere. **Skills:** nextjs, react-best-practices, emil-motion-impeccable, modern-ui-ux-design-system.

### T7. Habit engine with forgiving streaks and history

Build `packages/core/habits` and the Habits screen at `/habits`: habit creation with frequency, reminder time, rest days and freezes; check-in, skip with reason, rest-day protection and "keep going" states; streak calculation that forgives planned rest and freezes without shame copy; history heatmap and weekly review. Streaks are data, not a leaderboard, and no notification uses guilt language. **Exit check:** unit tests prove rest days and freezes behave as documented, a skipped day does not produce shame copy, the heatmap renders 30/90/365 days without layout overflow, and screenshots show Arabic and English states. **Acceptance test:** rest day and freeze tests pass, no guilt-language strings in the copy file, heatmap renders all three ranges without overflow. **Skills:** database-reliability-transactions, react-best-practices.

### T8. Reminders, quiet hours and opt-in Telegram link for Part B

Build the reminder engine for Part B: local notifications on web/PWA and Expo later, prayer alerts, habit reminders, water and medicine reminders, quiet hours with Cairo DST handling, snooze and "taken/done" actions. Add the opt-in Telegram bot link for Part B users as a separate bot token and consent flow, never reusing Part A's private bot or data. Reuse the privacy ideas from Part A's `sanitize-outbound` and `telegram-client` only after extraction into shared tested code; Part A files stay untouched. **Exit check:** tests prove quiet hours suppress non-critical alerts, snooze clamps correctly across DST, Telegram linking requires explicit consent and a separate token, and a forged or revoked link cannot send. **Acceptance test:** quiet hours suppress non-critical alerts, snooze clamps across DST, revoked link cannot send. **Skills:** production-engineering-standards, firebase_basics, vibe-auth-hardening.

### T9. Owner analytics page, billing fallback and legal pack

Build `/owner` gated by the server-verified owner token from T3, showing real metrics only: signups, active users, retention, free-to-Pro funnel, MRR in EGP and visitor currency, churn, AI cost, sync conflicts, error rate and notification failures, each read from an aggregate rather than a raw collection. Build `/pricing` with the EGP-first plan table from `plans/sir-life.md` section 8, currency auto-detect with manual override, "Subscriptions launching soon" and an email capture that writes a Lead document and rejects invalid addresses. Build `/legal/privacy`, `/legal/terms`, `/legal/refunds` and `/legal/cookies` from `packages/kit/legal-pack` with truthful claims only: no SOC 2, no impossible SLA, no health-data sale, AI training prohibited without opt-in. **Exit check:** non-owner and forged tokens get 403, owner sees real metrics or dashes with reasons, pricing shows launch mode until keys exist, legal pages exist and are linked, and dual hosting is curl-checked on Firebase and Vercel once deployed. **Acceptance test:** forged and non-owner tokens 403 on `/owner`; empty metric renders a dash with reason; pricing shows launch mode and writes a Lead doc for a valid email while rejecting an invalid one. **Skills:** firebase_auth_basics, website-traffic-analytics, legal-compliance-shield.

### T10. Expo mobile scaffold, local data sync boundary and store-readiness pack

Create `apps/mobile` with Expo for Android and iOS, sharing `packages/core`, `packages/data`, `packages/ui` and `packages/kit` where the kit supports React Native. Implement the Today screen, local storage, sign-in, prayer card, habit check-in and reminder permission flow on Android emulator and iOS simulator or TestFlight internal if available. Define the sync boundary clearly: local repositories remain the source of truth on device, Firestore sync is opt-in per category, and health-adjacent data never syncs without explicit consent. Draft store metadata, screenshots list, privacy nutrition label content and content rating notes in `docs/store/`, all truthful and unsubmitted. **Exit check:** the Expo app runs on at least one Android emulator and one iOS simulator or a recorded blocker, sign-in works, Today renders real local data, screenshots exist in `.sir/evidence/`, and the report lists every owner-only store step. **Acceptance test:** app runs on one Android emulator and one iOS simulator (or a recorded blocker with evidence), sign-in works, `docs/store/` pack exists and is truthful. **Skills:** android-cli, firebase_basics, react-best-practices.

### T11. Today screen enhancements: task, habit, water, medicine and expense

Extend the Today screen from T6 to also show the next task with due time, habit check-ins due today, water intake summary and medicine reminders, plus an expense entry quick-action. All data writes local repository first, works offline. Implement the five states on all panels, skeletons matching final geometry, optimistic feedback under 100 ms, 44 px targets, Arabic RTL and English LTR, light/dark/system/high-contrast, and no fake data. **Exit check:** Playwright screenshots at 320/390/768/1280 px Arabic/English light/dark show all five states, no horizontal overflow, and the expense quick-action writes to local storage without errors. **Acceptance test:** expense quick-action persists locally, five states visible at all four widths in both languages and themes. **Skills:** react-best-practices, modern-ui-ux-design-system, emil-motion-impeccable.

### T12. Prayer alerts with quiet hours, snooze and DST-safe Cairo handling

Build the prayer alert system: adhan alerts respect quiet hours (user-configurable time window), snooze clamps correctly across DST transitions, and alerts are suppressed outside the quiet hours window. Implement the five states on the alert panel, and badge each alert with the source/method that produced the time (plan R9). **Exit check:** Playwright screenshots at 320/390/768/1280 px Arabic/English light/dark show the alert panel in all five states; quiet hours suppress non-critical alerts; snooze works across the DST boundary; no alert fires outside quiet hours. **Acceptance test:** quiet hours suppress non-critical alerts in tests, snooze clamps across the Cairo DST boundary, alert shows its source badge. **Skills:** production-engineering-standards, database-reliability-transactions.

### T13. Water reminders and intake log with local-first persistence

Build the water reminder system: local notifications at user-configured intervals, intake log with visual glass animation and spring physics, 3,000 ml daily goal target, tracks towards goal with fluid animation. All data local-first, works offline, sync opt-in later. Implement the five states on the water panel. **Exit check:** unit tests prove the intake log accumulates correctly, the goal progress renders without overflow, and Playwright screenshots at 320/390/768/1280 px Arabic/English light/dark show all five states. **Acceptance test:** intake totals correct in tests, goal ring renders without overflow at 320 px, offline write persists. **Skills:** react-best-practices, emil-motion-impeccable, database-reliability-transactions.

### T14. Medicine reminders with snooze, "taken" log and no dosing advice

Build the medicine reminder system: user-configured reminder times, snooze with clamping across DST, "taken/done" log entry per dose, no dosing advice or medical claims anywhere in the UI (copy audit included). All data local-first. Implement the five states on the medicine panel. **Exit check:** unit tests prove snooze clamps across DST, the "taken" log records correctly, no dosing text appears in the UI, and Playwright screenshots show all five states. **Acceptance test:** copy audit finds zero dosing/medical-advice strings, snooze clamps across DST, taken-log records per dose. **Skills:** production-engineering-standards, legal-compliance-shield.

### T15. Food log with calories, macros and water tracking

Build the food logging screen at `/food`: calorie and macro entry (protein/carbs/fat), water tracking per meal, local database-first storage, works offline, no medical claims and no diet prescriptions. Implement the five states on the food panel. **Exit check:** unit tests prove calorie/macro totals are correct, the water log integrates with the water reminder system, and Playwright screenshots show all five states. **Acceptance test:** macro totals correct in tests, water-per-meal feeds the water log, no medical-claim strings in copy. **Skills:** react-best-practices, database-reliability-transactions.

### T16. Gym and workout log with weight history

Build the gym logging screen at `/gym`: exercise entry with sets/reps/weight, weight history chart, local-first storage, works offline. Implement the five states on the gym panel. **Exit check:** unit tests prove weight history renders correctly, the chart shows progression without overflow, and Playwright screenshots show all five states. **Acceptance test:** weight history chart renders 1/3/12-month ranges without overflow, entries persist locally. **Skills:** react-best-practices, emil-motion-impeccable.

### T17. Expense tracker with categories and monthly review

Build the expense tracking screen at `/expenses`: category selection (food, transport, medicine, gym, other), EGP amount entry stored as integer piasters with rounding tests, monthly review summary, local-first storage, works offline, no fake numbers. Implement the five states on the expense panel. **Exit check:** unit tests prove expense categories sum correctly including piaster rounding, the monthly review shows totals without overflow, and Playwright screenshots show all five states. **Acceptance test:** piaster rounding tests pass, category sums correct, monthly review renders real totals only. **Skills:** database-reliability-transactions, react-best-practices.

### T18. Mood and energy check-in plus evening reflection

Build the mood check-in screen at `/mood`: energy level 1-5 selector, evening reflection text area, local storage, works offline. Implement the five states on the mood panel. AI reflection prompts stay off by default and require explicit consent (plan section 6.4). **Exit check:** unit tests prove energy level stores correctly, the reflection saves without errors, and Playwright screenshots show all five states. **Acceptance test:** energy level and reflection persist locally, AI prompt is absent until consent is given. **Skills:** react-best-practices, zero-trust-security-hardening.

---
## M3: Sync, billing fallback, legal and owner page

### T19. Opt-in encrypted sync between two browsers

Build the encrypted sync engine: user enables sync per category (prayer, habits, water, medicine, food, expenses), Firestore stores encrypted entries only, decryption key derived from user password via the design in `docs/data-model.md`, same account on two browsers shows identical data, conflict resolution with last-writer-wins-per-field decided in an ADR. Health-adjacent categories stay local unless explicitly enabled. **Exit check:** user enables sync for prayer times, opens the app on a second browser, prayer times appear identical, disabling sync stops updates, conflict test: two edits on different browsers, last-writer-wins is observed. **Acceptance test:** two-browser round-trip identical, disabling sync stops updates, conflict resolves per the ADR rule, health category does not sync without consent. **Skills:** database-reliability-transactions, firebase_firestore, zero-trust-security-hardening.

### T20. Billing fallback: "Subscriptions launching soon" and lead capture

Build the pricing page wiring from T9 to live keys-ready state: EGP-first plan table from `plans/sir-life.md` section 8, currency auto-detect with manual override (USD, SAR, AED), "Subscriptions launching soon" banner with email capture that writes a Lead document, rejects invalid email addresses, no payment form until keys exist. When keys arrive the checkout activates without UI restructuring. **Exit check:** the pricing page displays the plan table, currency auto-detect works, the launch banner appears, email capture writes a Lead document for valid addresses and rejects invalid ones, and dual hosting curl-check passes. **Acceptance test:** Lead doc written for valid email, invalid rejected, no payment form present, launch banner styled as an elegant disabled state. **Skills:** legal-compliance-shield, vibe-auth-hardening.

### T21. Legal pack: privacy, terms, refunds and cookies

Build the legal pages from `packages/kit/legal-pack`: `/legal/privacy` matching exactly what the code collects (including the one-sentence sync-crypto explanation), `/legal/terms` with capped liability and no impossible claims, `/legal/refunds` with the published policy and 1-click cancellation path, `/legal/cookies` with a pre-consent tracker blocker and a Reject All button as prominent as Accept. **Exit check:** all four legal pages exist at their routes, are linked from the footer, the cookie banner blocks trackers before consent, and dual hosting curl-check passes. **Acceptance test:** tracker request absent before consent in a network capture, Reject All equally prominent, privacy page matches the actual data flows. **Skills:** legal-compliance-shield.

### T22. Owner analytics page with real metrics

Wire `/owner` to real aggregates end to end: signups, DAU/WAU retention curve, free-to-Pro funnel, MRR in EGP plus visitor-currency totals, churn, AI token cost per provider, sync conflicts, 4xx/5xx error rate and notification delivery failures. Every widget reads an aggregate or shows a dash with the reason; no raw collection scans, no invented numbers. **Exit check:** non-owner and forged tokens get 403, owner sees real metrics or dashes with reasons, empty states explain why, and the page loads under 2 s with 10k synthetic aggregate rows. **Acceptance test:** 403 for non-owner, dash-with-reason for empty metrics, page renders in Arabic and English. **Skills:** website-traffic-analytics, firebase_auth_basics, react-best-practices.

---
## M4: Android and iOS apps

### T23. Today screen in Expo mobile app

Bring the Today screen from `apps/web` to `apps/mobile` via Expo: same prayer times, tasks, habits, water, medicine, expenses, mood. Local storage source of truth, sign-in with Google, same five states. **Exit check:** the Expo app runs on at least one Android emulator and one iOS simulator, Today renders real local data, Google sign-in works, the five states are visible, and screenshots exist in `.sir/evidence/`. **Acceptance test:** both platforms render Today with real local data and working sign-in. **Skills:** android-cli, react-best-practices, firebase_auth_basics.

### T24. Prayer card in Expo mobile app

Build the prayer card component for Expo: prayer times for chosen city/method, method selector with official-vs-calculated badge, next prayer countdown, Qibla direction launcher (opens maps), prayer alerts enable/disable. **Exit check:** the prayer card renders correct times for Cairo and a second city, the method selector works, the countdown updates in real time, and screenshots exist in `.sir/evidence/`. **Acceptance test:** Cairo plus second-city times correct against the engine, badge shows the source, countdown ticks live. **Skills:** react-best-practices, android-cli.

### T25. Habit check-in in Expo mobile app

Bring the Habits screen from `apps/web` to `apps/mobile`: habit creation with frequency, reminder time, rest days and freezes, check-in with forgiving streak logic, history heatmap. **Exit check:** the habit check-in works on both Android emulator and iOS simulator, rest days and freezes behave as documented, the heatmap renders 30/90/365 days without overflow, and screenshots exist in `.sir/evidence/`. **Acceptance test:** check-in works on both platforms, freeze/rest-day rules identical to web tests. **Skills:** react-best-practices, database-reliability-transactions.

### T26. Water and medicine reminders in Expo mobile app

Bring the water and medicine reminder systems from `apps/web` to `apps/mobile`: local notifications on Android and iOS, snooze with DST clamping, "taken/done" log. **Exit check:** notifications fire on both platforms, snooze clamps across DST, the "taken" log records correctly, and screenshots exist in `.sir/evidence/`. **Acceptance test:** notification fires on Android emulator and iOS simulator, snooze clamps across the DST boundary. **Skills:** android-cli, production-engineering-standards.

### T27. Expense and money tracking in Expo mobile app

Bring the expense tracker from `apps/web` to `apps/mobile`: category selection, EGP entry in integer piasters, monthly review. **Exit check:** the expense screen works on both platforms, categories sum correctly including rounding, the monthly review shows totals, and screenshots exist in `.sir/evidence/`. **Acceptance test:** piaster sums match web results on both platforms. **Skills:** react-best-practices, database-reliability-transactions.

### T28. Mood and energy check-in in Expo mobile app

Bring the mood check-in from `apps/web` to `apps/mobile`: energy level 1-5, evening reflection. **Exit check:** the mood screen works on both platforms, energy level stores correctly, the reflection saves, and screenshots exist in `.sir/evidence/`. **Acceptance test:** mood entries persist locally on both platforms with the same schema as web. **Skills:** react-best-practices.

### T29. Push notifications for prayer/medicine/water/habit with quiet hours

Build the push notification service for Expo: fires on prayer alerts, habit reminders, water and medicine reminders, quiet hours suppress non-critical alerts during the configured window, snooze clamps across DST, and notification taps deep-link to the right screen. **Exit check:** a status change triggers a push notification on both Android and iOS with correct content, quiet hours suppress the alert, snooze clamps across DST, and tapping the notification opens the matching screen. **Acceptance test:** push received on both platforms, quiet hours suppress, deep link lands on the correct screen. **Skills:** android-cli, production-engineering-standards, firebase_basics.

---
## M5: Desktop shells, Telegram opt-in, accessibility map module, quality gates

### T30. Windows PWA installable from Edge, same sign-in and self-update

Build the Windows PWA path: user can install from Edge browser, same Google sign-in as web/mobile, service-worker self-update mechanism checks for updates (same codebase), and the owner's `Projects-Hub.html` entry shows the product. **Exit check:** the Windows PWA installs from Edge, Google sign-in works, the app applies an update after a new deploy, and the Projects-Hub entry shows the version. **Acceptance test:** install from Edge works, sign-in persists, update applies, hub entry accurate. **Skills:** firebase_hosting_basics, verification, modern-web-guidance.

### T31. macOS PWA installable from Safari, same sign-in and self-update

Build the macOS PWA path: user can install from Safari, same Google sign-in as web/mobile, self-update mechanism. **Exit check:** the macOS PWA installs from Safari, Google sign-in works, the app applies an update after a new deploy. **Acceptance test:** install from Safari works, sign-in and update verified on screen. **Skills:** firebase_hosting_basics, verification.

### T32. Linux PWA installable from Firefox, same sign-in and self-update

Build the Linux PWA path: user can install from Firefox, same Google sign-in as web/mobile, self-update mechanism. **Exit check:** the Linux PWA installs from Firefox, Google sign-in works, the app applies an update after a new deploy. **Acceptance test:** install from Firefox works, sign-in and update verified on screen. **Skills:** firebase_hosting_basics, verification.

### T33. Telegram opt-in link for Part B users (separate bot token and consent flow)

Build the Telegram opt-in flow for Part B: separate bot token from Part A, consent screen explains exactly what data will be sent, explicit consent required before any Telegram link is shown, consent state stored in Firestore scoped to `owner_uid`, revoking consent removes the Telegram link and stops sends. **Exit check:** a user opts in, a consent screen appears and must be explicitly accepted, the Telegram link appears only after consent, revoking consent removes the link and stops delivery, and no Part A private bot data is exposed. **Acceptance test:** consent gate enforced, revoke stops sends, separate token confirmed in env (never printed). **Skills:** production-engineering-standards, firebase_basics.

### T34. Accessibility map module: accessible places submissions and moderation

Build the accessibility map module at `/accessible`: users can submit accessible places (ramps, elevators, accessible toilets, parking with markings), submissions moderated for PDPL compliance, each entry has fields: place type, accessibility features (ramp slope, doorway width, curb height), location (geo hash), reporter `owner_uid`, status: pending/moderated/rejected. Moderation queue visible in `/owner`. **Exit check:** a user can submit an accessible place, the submission appears in pending state, a moderator can approve/reject, PDPL-required fields are present, and the queue is visible in `/owner`. **Acceptance test:** submission -> pending -> moderated flow works end to end, PDPL fields enforced, queue visible to owner only. **Skills:** google_maps_platform, legal-compliance-shield, firebase_firestore.

### T35. Screenshots at 5 widths × 2 languages × 2 themes for all critical journeys

Implement the Playwright screenshot suite for all critical journeys (Today, prayer, habits, tasks, water, medicine, food, gym, expenses, mood, focus, owner, pricing, legal, accessible, account) at 5 widths (320, 390, 768, 1280, 1920) × 2 languages (Arabic, English) × 2 themes (light, dark), all showing the five states where they exist. **Exit check:** all screenshots capture without console errors, the five states are visible, no horizontal scroll from 320 px to 3840 px, with a test. **Acceptance test:** suite runs in CI/local verify, zero console errors, evidence saved under `.sir/evidence/`. **Skills:** verification, a11y-debugging.

### T36. Accessibility audit: WCAG 2.2 AA, keyboard complete, 44 px touch targets

Implement the accessibility audit across every screen: every control has an accessible name in Arabic and English, touch targets at least 44 px with no covered hit area, full keyboard path, visible focus, zoom 80-200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured, colour pairs pass contrast in all four themes. **Exit check:** the audit passes WCAG 2.2 AA with an accessible name on every control, no covered hit area, and no horizontal scroll from 320 px, with a test. **Acceptance test:** automated axe pass plus manual keyboard walkthrough recorded, contrast pairs listed per theme. **Skills:** a11y-debugging, anti-vibecoded-design-system.

### T37. Lighthouse mobile score 90 or better for all critical journeys

Implement the Lighthouse CI audit for mobile: performance 90+, accessibility 100, best-practices 100, SEO 90+, and the JSON is saved in `.sir/evidence/`. **Exit check:** `lighthouse ci` returns mobile score 90 or better for all critical journeys, and the JSON is saved in `.sir/evidence/`, with a test. **Acceptance test:** scores meet thresholds on every critical journey, JSON evidence committed to `.sir/evidence/`. **Skills:** verification, website-traffic-analytics.

---
## M6: Release, beta and launch polish

### T38. Domain name setup and dual hosting go-live

Configure the domain (owner buys `sirlife.app` or an `.eg` name first - owner action if not done): product domain pointed at both Firebase Hosting and Vercel, same build and env on both, both hosts answer curl-checked 200, and both addresses are written in `.sir/CHECKPOINT.md`. While `ops/ci-quota-exhausted.flag` exists, local verification output is the recorded signal. **Exit check:** the domain answers 200 on Firebase Hosting and 200 on Vercel, and both addresses are recorded in the checkpoint. **Acceptance test:** `curl -sI` returns 200 on both hosts for `/`, `/pricing` and `/api/health`, addresses in checkpoint. **Skills:** firebase_hosting_basics, firebase_app_hosting_basics, deployments-cicd.

### T39. Store-readiness: truthful listings and store pack completion

Finish the store pack from T10 into submittable drafts: Play Store listing (title, short/full description in Arabic and English, screenshots from T35, content rating answers, privacy policy URL, data-safety form answers matching the privacy page exactly), App Store listing draft plus TestFlight internal-testing steps, and the SideStore iOS fallback documented. Nothing is submitted; every owner-only step (accounts, certificates, review) is listed with exact taps. **Exit check:** listings exist as drafts in `docs/store/`, data-safety answers match `/legal/privacy` field by field, owner steps enumerated. **Acceptance test:** data-safety form answers diff-clean against the privacy page, no invented claims in any listing text. **Skills:** legal-compliance-shield, firebase_basics.

### T40. Backup, restore and ops drills

Implement and prove the ops layer from plan section 6.6: scheduled Firestore export to a private bucket, a documented restore run that actually restores to a scratch project or emulator, `/api/health` and public status JSON, nightly error digest and weekly owner Telegram report at a round hour. **Exit check:** a restore drill is executed and its output recorded (row counts and timestamps), `/api/health` reports real component status, the weekly report arrives once. **Acceptance test:** restore drill restores real documents and the counts match, health endpoint reflects a killed dependency honestly. **Skills:** database-reliability-transactions, firebase_firestore, production-engineering-standards.

### T41. Beta onboarding: first real users with written consent

Run the beta from plan section 18: invite 20-50 real users, onboarding explains privacy-by-default and local-first storage, per-category sync consent recorded in Firestore, written consent stored per user, feedback channel in-app, and no seeded or invented user data in any path a user can see. **Exit check:** real beta users complete onboarding, consent records exist server-side, the app starts local-only, and a walkthrough on one real device is recorded. **Acceptance test:** consent record present per beta user, local-only default verified, feedback channel delivers to the owner queue. **Skills:** legal-compliance-shield, firebase_auth_basics, verification.

### T42. Legal and paid-launch gate

The gate before any paid plan goes live: owner-confirmed legal review of `/legal/privacy`, `/legal/terms`, `/legal/refunds`, `/legal/cookies` and the PDPL position for Egyptian users, subscription state checked server-side only, webhook signature verification proven against tampered/replayed/unsigned fixtures, and the pricing page switching from launch mode to live checkout only after keys exist and sign-off is recorded. **Exit check:** webhook negative fixtures all rejected, legal sign-off recorded by the owner, pricing flips to live only with keys + sign-off. **Acceptance test:** tampered, replayed, unsigned and wrong-timestamp webhook events all rejected in tests; paid plan cannot activate without keys and recorded sign-off. **Skills:** legal-compliance-shield, vibe-auth-hardening, production-engineering-standards.

---
**What is deliberately not in these forty-two:** Quran reader and Quran audio, fatwas or AI-generated religious content, public leaderboards of private health data, ads, Wear OS/watchOS/TV/car surfaces, native desktop installers beyond the PWA-plus-ADR shell, store submission itself (T39 drafts, the owner submits), and any Part A private data in Part B paths. They are M3 to M6 decisions in `plans/sir-life.md` and each one needs the tasks above green first.
