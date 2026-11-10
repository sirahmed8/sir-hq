# PLAN: SIR Life (Wave 6, partly built)
Audited 2026-11-10. Two parts, kept apart on purpose:
- Part A, Life Organiser: Ahmed's private daily organiser (schedule bridge, Telegram reminders, daily brief, read-only mail triage). Personal tool: not sold, unlisted, exempt from commercial items.
- Part B, Life app: the public consumer app from the old plan (prayer-aware routine, habits, water and medicine reminders, food, gym, expenses). Commercial items below apply to Part B only and it starts only after Part A is verified.
SIR Life is separate from AHome: zero couple data in either direction.

## 1. Purpose (plain words)
Part A tells Ahmed each morning and evening what is on his schedule, reminds him on Telegram at the right time (never at night), and helps him plan study blocks. Part B is a calm Arabic-first app that does the same kind of daily planning plus prayer times, habits and reminders for anyone.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Life` |
| GitHub (private) | `sirahmed8/sir-life` |
| Part A runtime | Node + TypeScript (`engine/`, `cli/`, `packages/core`, `packages/data`), CLI commands `sync`, `brief`, `remind`, `listen`; local JSON store in git-ignored `data/` |
| Part B stack (default) | Expo (Android, iOS) + PWA, local-first storage, optional encrypted cloud sync (Pro). Next.js is not used (the master plan says Next.js; default is Expo + PWA from `_SIR` plan; ADR to confirm) |
| Domain | none for Part A. Part B: candidate `sirlife.app`, owner checks and buys |
| Platforms | A: Windows scheduled CLI, phone via Telegram: built, unverified. B: Android, iOS, PWA: not started. Wear OS and watchOS for prayer and water reminders: skipped in v1, listed for M6+. Desktop, TV, car: skipped |
| Money | Part A none. Part B: core modules free; Pro in EGP only for cloud sync and backup (price to test, "(unsourced, verify)"); "launching soon" fallback until keys |

## 3. Current state
Claimed (README): T-100 to T-104 done: calendar and timetable bridge with `.ics` export, Telegram reminder engine with Cairo quiet hours and DST, snooze and escalation, daily brief, read-only Gmail triage with approval-gated drafts, one outbound-text privacy chokepoint (`sanitizeOutbound`). PORTFOLIO.md: 7 of 24 tasks, 15 commits, 65 tests.
Verified today: `node --test dist/tests/*.test.js` = **65 passed, 0 failed** (18 suites). Caveat: `tsc` is not installed in the folder (the build step failed: "tsc is not recognized"), so these ran on the previously built `dist/` and may not match current source. Built, unverified: everything else.
Stale files: `.sir/CHECKPOINT.md` still says "nothing is built yet" (2026-10-30). `package.json` version is `0.1.0`; the version rule says 1.0.0. Part A mission in the project's `.sir/MASTER_PLAN.md` (prayer sentinel, journal, Next.js) differs from this plan: this plan wins until the manager rules.
Not started: Part B screens, prayer-time engine validation, habits, reminders for medicine and water, food, gym, expenses, sync, billing, legal, store builds.

## 4. Security and privacy rules
1. All outbound text (Telegram, mail drafts) passes `sanitizeOutbound` (exists; keep the 65 tests). Test: a message containing a mail body or phone pattern is cut.
2. Gmail is read-only plus drafts that need an explicit approval; never auto-send; token in Credential Manager. Test: sending without approval fails (exists: `gmail-approval.test.ts`).
3. Health data (medicine, food, gym, expenses) stays on the device by default; cloud sync is opt-in, end-to-end encrypted before upload; health text never goes to an outside AI provider without a per-feature consent switch.
4. `data/` is git-ignored (verified: `git check-ignore data` returns the path).
5. No AHome or couple data, ever; a grep test in CI for the AHome project name and private folder paths.
6. Part B: account deletion and export, cookie/tracker rules, sessions in HttpOnly cookies on the web side, rate limits on sync endpoints.

## 5. Shared pieces
Telegram sender from `_SIR/scripts/deliver/` (the reminder engine sends through the SIR AI bot; keep one bot). Part B uses Platform `ui/styles/hooks`, `i18n`, `billing-fallback`, `legal-pack`, `ai-proxy`. Prayer-time math stays in `packages/core` and may move to Platform if a second product needs it (none yet).

## 6. Screens (Part B) and entities
Today, Prayer times, Tasks, Habits, Water and medicine, Food, Gym, Expenses, Skills, Settings and Profile. Entities: PrayerDay, Task, Habit, Reminder, FoodEntry, Workout, Expense, SkillPlan. Part A has no screens (CLI, Telegram, `.ics`, HTML brief).
Five states, Arabic RTL first and English, light/dark/contrast, 44 px targets, 320 px to 4K, WCAG 2.2 AA, own logo.

## 7. AI
Part A: none required. Part B: optional meal and routine suggestions, off by default, local-first; evals for safety (no medical advice: the app tells the user to ask a doctor for medicine or diet changes). Support assistant for Part B grounded in docs.

## 8. Operations
Part A: scheduled task health line, Telegram quiet hours test, backup of `data/` weekly to `D:\Projects\Backups`. Part B: standard 26 set (crash reports with consent, weekly Telegram report, status JSON) after launch.

## 9. Visibility and legal (Part B only)
Arabic queries ("تطبيق مواعيد الصلاة والعادات"), store listings (ASO) in Arabic and English, `llms.txt`, facts page, JSON-LD `MobileApplication`. Health-adjacent data means a stricter privacy page; Egypt PDPL 151/2020 and GDPR special-category rules as tasks "(unsourced, verify)"; lawyer review before any paid launch. Prayer times: show the calculation method used and a note that local mosque times may differ.

## 10. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Honest base | `tsc` installed, `npm run verify` builds fresh and passes; version set to 1.0.0; checkpoint rewritten; CI green URL |
| M1 | Part A verified | one real morning brief and one reminder sent to Telegram with API ok; quiet-hours test around the DST change |
| M2 | Prayer engine | Cairo times match a published official timetable for 7 sample days within 1 minute (source named) |
| M3 | Part B core slice | Today screen with prayer times, tasks, habit checks, water counter, offline; unit tests |
| M4 | Security, legal, billing | consent switches, deletion flow, legal pages, billing fallback |
| M5 | Quality | 5 states, RTL/LTR, screenshots at 390 and 1280 |
| M6 | Stores | Android build on a device or emulator; store listing drafts for the owner |

## 11. Next 10 tasks (each under 2 hours)
1. Install dev dependencies, rebuild, run `npm run verify`, record counts. Files: `package.json`. Check: fresh `dist/` and 65 or more passing, saved in `.sir/evidence/`.
2. Set version to 1.0.0 and rewrite `.sir/CHECKPOINT.md` to the real state. Check: checkpoint lists T-100..T-104 with test evidence.
3. CI workflow (typecheck, test, gitleaks). Files: `.github/workflows/verify.yml`. Check: green Actions URL.
4. Run a real morning brief through the shared Telegram sender with no private mail content. Check: API ok printed; sanitize test passes.
5. DST boundary test for reminders (Egypt DST dates, `Intl`) with a fixed clock. Files: `tests/schedule-dst.test.ts` (extend). Check: passes for both transition days.
6. Prayer-time engine: Cairo method function with fixtures from an official timetable. Files: `packages/core/src/prayer/`, tests. Check: 7 days within 1 minute; source URL in the test header.
7. Expo app scaffold for Part B with tokens and RTL. Files: `apps/mobile/`. Check: runs on an emulator, screenshot of an empty Today screen with an honest empty state.
8. Habit model and streak logic with a forgiving rule (one miss does not reset) and tests. Check: unit tests green.
9. Local storage layer (SQLite on device) with migrations. Check: migration test opens, writes, reopens.
10. Privacy grep test: no AHome strings or couple paths in the repo. Files: `tests/no-private-strings.test.ts`. Check: passes; fails on an injected string.

## 12. Risks and open questions (defaults)
- Two products in one folder: default is Part A stays a private engine package and Part B imports `packages/core` only.
- Health data liability: default is no diagnosis, no dosing advice, clear disclaimers, medicine reminders are user-defined text.
- Prayer-time accuracy and method differences: default Egyptian General Authority of Survey method, shown to the user, user can change.
- Gmail scopes: default is the narrowest read-only scope; if verification is needed for public use, Part B does not ship Gmail features.

## 13. Only the owner can do
Sign in to Google to authorize Calendar and Gmail read scopes; sign in to Telegram if the bot token changes; store developer accounts and domain for Part B; lawyer review for health-data terms.

## 14. Market-grade note
Competitors (Muslim Pro, Todoist, TickTick and similar) in `plans/competitors/sir-life.md`: user counts and prices there need links or "(unsourced, verify)". Part A has no market section; it is personal.
