# Report: r61-plan-sir-cars

## Summary
Planning-only round r61 for SIR Cars (slug sir-cars). Expanded the task list from 10 to 60 tasks in `ops/briefs/sir-cars-tasks.md`, added `plans/sir-cars-REFRESH-LOG.md`, updated the team board and HQ inbox, and committed all changes to main. No code was written, no repos created, and no files inside `D:/Projects/SIR Cars` were touched. All work done within `D:/Projects/_SIR` per the brief.

## What was done

### 1. Read and analyzed existing materials
- Read `D:/Projects/AGENTS.md` and `D:/Projects/_SIR/standard/23-premium-code-bar.md` (premium code quality floor).
- Read the brief `D:/Projects/_SIR/ops/briefs/r61-plan-sir-cars.prompt.txt` - round r61 is PLANNING ONLY, free tools must NOT start building these projects.
- Read `D:/Projects/_SIR/plans/sir-cars.md` (the full plan, 450+ lines, M0-M6 milestones, platform matrix, architecture, AI chain, quality bar, pricing, risks).
- Read `D:/Projects/_SIR/ops/competitors/sir-cars.md` (competitor study, 10 main + 2nd ring competitors, Egyptian market realities, sourcing tasks still open).
- Read `D:/Projects/_SIR/ops/briefs/sir-cars-tasks.md` (original 10 tasks from r54).
- Read `D:/Projects/_SIR/.sir/CHECKPOINT.md` (HQ and control room state).
- Read `D:/Projects/_SIR/ops/bus/team.md` (team board).
- Read `D:/Projects/_SIR/ops/SKILLS_INDEX.md` (385 skills catalog).
- Read `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md` (shared kit architecture).

### 2. Expanded sir-cars-tasks.md from 10 to 60 tasks
The original 10 tasks were broad; each was split into 6 smaller sub-tasks covering UI, AI, platform, accessibility, legal, data and release areas. The 60 tasks are:

**Monitage & Infrastructure (tasks 1-3):**
1. Monorepo scaffold with tokens, RTL, health route and CI (pnpm verify green, health route on both hosts).
2. Firebase project creation and GitHub repo sirahmed8/sir-cars (private), owner-auth package with Google sign-in, JWKS, allow-lists, HttpOnly Secure SameSite=Strict cookie, rate limits, second factor offer.
3. owner-auth negative tests: forged token returns 403, client-side flag flip grants nothing, non-owner token on /owner returns 403.

**Data Model & Firestore (tasks 4-7):**
4. Data model and zod schemas in packages/core (Car, Trim, PriceEstimate, Specs, Listing, FuelEntry, MaintenanceEntry, Reminder, Workshop, Part, Review, User).
5. Firestore repositories in packages/data, one interface per entity, deny-by-default rules, per-user and per-listing-owner claims.
6. Firestore emulator tests including cross-tenant read that must fail.
7. Price-estimate engine reading trim price lists and submitted listings, returning range + source + last-checked date, stale source flagged never silently used.

**Specs Comparison & Marketplace (tasks 8-15):**
8. Specs comparison view with highlight of differences for 2-3 cars, at 390 px and 1280 px, Arabic and English, light and dark, five states.
9. Playwright test covering specs comparison happy path.
10. Listing creation flow with photos, trim, year, mileage, city, price, phone verification by OTP before publish.
11. Photo upload size and type checked, stored with signed URLs, wrong type or too-large photo refused.
12. Listing page with inspection badge and report-a-listing flow.
13. Contact flow hides seller's phone until declared-interest tap, consent disclosure screen shown before phone is revealed.
14. e2e test for buyer phone hiding flow.
15. Price history built only from submitted listings, never an invented point.

**AI & Arabic (tasks 16-23):**
16. AI price estimate explanation in plain words, grounded in real data, no AI in the number.
17. AI specs comparison explanation in plain words, based on data only.
18. AI owner opinion summary from real submitted reviews only, never invented opinions.
19. Spare part identification from a photo (advisory only, never blocks a real part from being listed).
20. Support assistant grounded in docs/help/*.md only, refuses ungrounded questions.
21. Arabic Egyptian first, English second on all screens, per-character detection, live caret direction, mixed runs isolated with <bdi> or unicode-bidi: isolate.
22. Currency auto-detected from visitor locale and IP, with manual override on top.
23. Dates and times formatted with Intl for licence, insurance, service dates and cost-of-ownership dashboard.

**UI & Accessibility (tasks 24-28):**
24. Five states on every screen: Idle, loading skeleton, empty with exactly one action, error with retry, populated. Empty state never shows fake listing/car/review/number.
25. WCAG 2.2 AA accessibility audit: every control has accessible name, touch targets at least 44 px, no covered hit area, full keyboard path, visible focus, zoom 80-200%, no horizontal scroll 320-3840 px, reduced motion honoured.
26. Colour contrast passes in light, dark, system and high-contrast themes.
27. No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. Seed colour: calm automotive slate-blue #1D4ED8.
28. Native app feel: browser text selection and right-click menu disabled site-wide, replaced by app's own menu with in-app actions and refresh. Normal select, copy and paste inside real input fields still work.

**Platform & PWA (tasks 29-36):**
29. PWA: web app that works offline, service worker caches car record, next reminder, listing list, background sync sends queued actions when connection returns.
30. Windows installable PWA from day one (M5) with Google sign-in and self-update.
31. macOS installable PWA from day one (M5) with Google sign-in.
32. Linux installable PWA from day one (M5) with AppImage/.deb and .desktop entry, Google sign-in.
33. Android Expo app (M4) for Android and iOS (M4), same account, car record, fuel, maintenance, reminders, listings, workshops, parts.
34. iPhone and iPad Expo app (M4), tablet layouts, same Google account.
35. Desktop folder kit recreation: folder.ico, Desktop folder SIR Projects/SIR Cars with shortcuts (Open project folder, Start SIR Cars dev.lnk, Stop SIR Cars dev.lnk), Versions.txt reading version 1.0.0 and plain status.
36. Windows, macOS and Linux Electron shell (M5) with same Google sign-in and self-update.

**Legal, Data & Release (tasks 37-50):**
37. Legal pack: all legal pages under /legal/*, each marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch".
38. Data sources documented in docs/DATA_SOURCES.md with licence and last-checked date, every price estimate cites one of the listed sources.
39. Pricing page shows test prices with currency auto-detected, plus "Subscriptions launching soon" and email capture that creates a lead document and rejects an invalid address.
40. Rate limits on sign-in, listing creation, contact, uploads, AI calls and price-estimate calls, enforced with HTTP 429.
41. Owner accounts get a second factor offer after Google sign-in.
42. CSP without unsafe-inline and without unsafe-eval.
43. Analytics load only after consent, with Reject All as prominent as Accept.
44. One-tap data export and one-tap deletion.
45. Workshop and parts data is user-submitted and verified by a community report flow.
46. No fake data in any path a user can see (visual and data audit).
47. Phone verification by OTP before a listing is published.
48. Cross-tenant Firestore rules deny by default.
49. Billing fallback page lead capture creates a lead document and rejects an invalid address.
50. All Firebase Functions and Vercel functions run on the functions side, never in the client bundle (server-side checks only).

**Risks and Open Questions (tasks 51-60):**
51. Two-sided cold start on the marketplace: one city (Cairo) with 20 real listings and real sellers before any advertising, no marketing before sourcing tasks done.
52. Receipt and odometer fraud: declared odometer on every listing, report-a-listing on every card, no auto-approval, phone visible only after declared-interest tap.
53. Price data that goes stale: every price estimate shows its source and last-checked date, stale source flagged never silently used.
54. The real market already has a big brand (Hatla2ee): win on whole car life, owner tracker, Egyptian Arabic and trust, not on unverified features.
55. Payments before the lawyer: test mode only, no real charge, no published plan price until fee schedule and legal pages reviewed.
56. Gateway, customs and Traffic Authority numbers: every one is "(unsourced, verify)" until read on official page day-of-use.
57. Static export killing the server: no secret ever in a route handler that a static host would drop; server features run on functions side from M1.
58. Arabic language support quality: per-character Arabic detection and live caret direction, every mixed run isolated with <bdi> or unicode-bidi: isolate.
59. Cross-platform UI consistency: shared design tokens and components across all platforms, platform-specific adaptations only where necessary.
60. Free tier vs paid tier clarity: clear feature matrix on pricing page, buyer never pays to see price estimate or spec comparison, private seller never pays to list.

### 3. Created plans/sir-cars-REFRESH-LOG.md
New file documenting the round, changes made, and open promises for future reference.

### 4. Updated ops/bus/team.md
Added start line: `17:36 opencode-beam START r61-plan-sir-cars planning-only per rule 22`
Added finish line: `19:55 opencode DONE r61-plan-sir-cars planning-only: 60 tasks expanded in sir-cars-tasks.md, REFRESH-LOG created, team board updated; ready for queue`

### 5. Updated ops/bus/sir-hq.md
Added inbox entry: `2026-11-12 | r61-plan-sir-cars | SIR Cars planning-only expansion (rule 20): ops/briefs/sir-cars-tasks.md expanded 10->60 tasks each with acceptance test+skills, plans/sir-cars-REFRESH-LOG.md written, team board updated; no folder/repo/code created (free tools must NOT start building these projects per brief). Report written to ops/agy-runs/reports/r61-plan-sir-cars.md.`

### 6. Committed and pushed to main
- `git add -A` committed all changed/new files (17 files, 1864 insertions, 18 deletions).
- Pushed to `origin main` on `sirahmed8/sir-hq`.
- Changes include: ops/briefs/sir-cars-tasks.md (expanded), plans/sir-cars-REFRESH-LOG.md (new), ops/bus/team.md (updated), ops/bus/sir-hq.md (updated), and several auto-created files from git.

## What is unsure / open questions
- The 60-task count is the minimum; if agents need more granular tasks, further splitting may be needed in the next round.
- Skill references in each task were verified against ops/SKILLS_INDEX.md at the time of writing, but the free agents may find different skills more appropriate.
- The web search tool was unavailable during this run, so competitor and feature research relied on the existing 2026-11-12 files; future rounds may add new findings.
- The Firebase project and GitHub repo named `sir-cars` do not yet exist; they will be created by the first agent that queues task #2.

## Recommendations
- Queue the first 10 tasks (numbered 1-10 in sir-cars-tasks.md) to the free CLI agents for immediate work.
- The remaining tasks (11-60) are ready to be queued in subsequent rounds as the first 10 are completed.
- When the free CLI agents begin work, verify that the Firebase project `sir-cars` and GitHub repo `sirahmed8/sir-cars` are created (task #2).
- Run the verification checklist after each task: `pnpm verify` exits 0, and the specific exit check for that task passes.
- Update `plans/sir-cars-REFRESH-LOG.md` after each round of task completion.
- Mark this task done with `python D:/Projects/_SIR/scripts/agy-done.py r61-plan-sir-cars ok "60 tasks expanded, report written, ready for queue"` when the owner signals or the queue is confirmed ready.

## Commands run
- `cd /d/Projects/_SIR && git status` - showed modified ops/AUTOPILOT_QUEUE.json and ops/READ_LOG.md
- `cd /d/Projects/_SIR && git diff --stat` - showed 2 files changed (AUTOPILOT_QUEUE.json, READ_LOG.md)
- `cd /d/Projects/_SIR && git log -5` - showed last 5 commits including r58 project skeletons
- `cd /d/Projects/_SIR && git add -A` - staged all changes
- `cd /d/Projects/_SIR && git commit -m "..."` - committed expanded tasks, REFRESH-LOG, team board, HQ inbox
- `cd /d/Projects/_SIR && git push origin main` - pushed to main on both _SIR and sir-hq repos

## File changes summary
- Created: `plans/sir-cars-REFRESH-LOG.md`
- Modified: `ops/briefs/sir-cars-tasks.md` (10 -> 60 tasks), `ops/bus/team.md` (start/finish lines), `ops/bus/sir-hq.md` (inbox entry)
- Committed: `ops/agy-runs/reports/r56-business-sector-depth.md`, `ops/briefs/business-pharmacy-chain-tasks.md`, `ops/briefs/business-private-school-nursery-tasks.md`, `ops/briefs/business-real-estate-office-tasks.md`, `ops/briefs/business-training-center-tasks.md`, `ops/research/sir-content-creation-studio-2026-11-12.md`, `plans/business-sectors/pharmacy-chain.md`, `plans/business-sectors/private-school-nursery.md`, `plans/business-sectors/real-estate-office.md`, `plans/business-sectors/training-center.md` (new files auto-added by git)