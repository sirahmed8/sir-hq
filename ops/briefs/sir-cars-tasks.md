# First 40+ build tasks for SIR Cars (round r61, HQ, planning-only)

Ready to queue for the free agents. Each task is one paragraph; the agent reads the plan `D:/Projects/_SIR/plans/sir-cars.md` and the competitor study `D:/Projects/_SIR/ops/competitors/sir-cars.md` first, then does only this task, runs the checks, commits, pushes and ticks the checklist. Version stays 1.0.0.

## Monorepo & Infrastructure

1. Monorepo scaffold with tokens, RTL, the health route and CI. Create the monorepo skeleton under `D:/Projects/SIR Cars` (apps/web, apps/api, packages/core, packages/data, packages/ui, packages/kit, apps/mobile, apps/desktop, docs, scripts) with strict TypeScript, Tailwind v4 tokens, RTL-first styles, an `/api/health` route returning JSON, and a `pnpm verify` script that runs typecheck, lint, tests, build and gitleaks. No UI beyond the health route and a placeholder home page with the five states. Exit check: `pnpm verify` runs and the output was seen green, and the health route answers on both hosts later. **Skills**: `modern-web-guidance`, `nextjs`, `react-best-practices`.

2. The product's own Firebase project and the `owner-auth` package with negative tests. Verify whether a Firebase project and a GitHub repo named `sir-cars` already exist; if not, create the Firebase project `sir-cars` on the free Spark plan and the GitHub repo `sirahmed8/sir-cars` (private) as the only remote. Implement `owner-auth` (Google sign-in via Firebase Auth, ID token verified on the server with JWKS, allow-list for owner and admin, HttpOnly Secure SameSite=Strict cookie, rate limits on sign-in, listing creation, contact, uploads, AI calls and price-estimate calls, second factor offer) with negative tests: forged token returns 403, client-side flag flip grants nothing, non-owner token on `/owner` returns 403. Write the Firebase project name and GitHub repo name in the project checkpoint. Exit check: the tests pass and the Firebase project and repo names are written in the project checkpoint. **Skills**: `firestore_rules_creation`, `firebase_security_rules_auditor`, `auth`.

3. The data model and the Firestore rules, with emulator tests. Implement the domain types and zod schemas in `packages/core` (Car, Trim, PriceEstimate, Specs, Listing, FuelEntry, MaintenanceEntry, Reminder, Workshop, Part, Review, User) and the Firestore repositories in `packages/data`, one interface per entity, with deny-by-default rules and per-user and per-listing-owner claims. Emulator tests must include a cross-tenant read that fails. Exit check: the emulator rules tests pass, including the cross-tenant read that must fail. **Skills**: `firestore_rules_creation`, `firebase_firestore`.

4. The price-estimate engine with a cited source and range. Implement the price-estimate engine that reads trim price lists and submitted listings and returns a range plus the source and its last-checked date. Every estimate shown on screen must display its source and range; a stale source is flagged, never silently used. Exit check: a price estimate for a known trim returns a range and a source, and the source is shown on screen, with an automated test. **Skills**: `gemini-api-dev`, `ai-gateway`.

5. The specs comparison view with highlight of differences. Implement the specs comparison of two or three cars side by side, with the differences highlighted, at 390 px and 1280 px, in Arabic and English, in light and dark, with the five states (idle, loading skeleton, empty with one action, error with retry, populated). Exit check: the comparison renders correctly in all four combinations and a Playwright test covers the happy path. **Skills**: `anti-vibecoded-design-system`, `taste-design-engine`, `emil-motion-impeccable`.

6. The listing creation flow with photos and phone verification. Implement the listing model, the creation flow with photos, trim, year, mileage, city and price, phone verification by OTP before publish, and size- and type-checked photo uploads with signed URLs. Exit check: a listing cannot be published without phone verification (e2e test blocked), a wrong-type or too-large photo is refused, and a stored photo is reachable only with a valid signed URL. **Skills**: `firebase_firestore`, `webhook-testing`.

7. The listing page, the contact flow and the consent disclosure screen. Implement the listing page with the inspection badge and the report-a-listing flow, the contact flow that hides the seller's phone until a declared-interest tap, and the consent disclosure screen shown before the phone is revealed. Exit check: the buyer's phone is hidden until the declared-interest tap and the consent screen is shown before the seller's phone is revealed, with an e2e test. **Skills**: `vibe-auth-hardening`, `legal-compliance-shield`.

8. The car record, the fuel log and the maintenance log. Implement the car record (one record per car, reused across listings, fuel, maintenance and reminders), the fuel log with consumption and cost per kilometre, and the maintenance log with service intervals and reminders. Exit check: a user can add a car, log fuel and maintenance, and see consumption and cost per kilometre computed from real entries, with a test. **Skills**: `database-reliability-transactions`.

9. The licence, insurance and service reminders with the cost-of-ownership dashboard. Implement the licence, insurance and periodic inspection reminders that fire at a round hour through the Telegram sender, plus the cost-of-ownership dashboard (fuel, maintenance, insurance, tax, fees) and the weekly Telegram report with numbers and their meaning. Exit check: a reminder fires at a round hour and the weekly report arrives with the numbers and their meaning, with a test. **Skills**: `chat-sdk`, `telegram-bot`.

10. The owner-only analytics page and the billing fallback page. Implement `/owner` with server-verified owner token and 403 for everyone else, showing real metrics only (users, listings, contacts, price-estimate calls, AI cost, error rate, workshops, parts, subscriptions, revenue), and the billing fallback page with "Subscriptions launching soon" and an email capture that creates a lead document and rejects an invalid address. Exit check: a non-owner token on `/owner` gets 403, a forged token gets 403, the pricing page shows the test prices with auto-detected currency, and the email capture creates a lead document and rejects an invalid address. **Skills**: `routing-middleware`, `env-vars`.

## Marketplace & Listings

11. The listing listing view with five states everywhere. Implement the car listing grid/search view with idle, loading skeleton, empty with one action ("tell us your city and we will tell you when listings arrive"), error with retry, and populated states. At 390 px and 1280 px, in Arabic and English, light and dark. Exit check: the listing grid renders correctly in all four combinations with five states visible. **Skills**: `modern-web-guidance`, `a11y-debugging`.

12. Search and filter for cars by make, model, year, trim and city. Implement the search input and filter chips that work across all platforms. Exit check: searching "Kia Sportage 2019 Cairo" returns real listings with trim levels. **Skills**: `modern-web-guidance`.

13. Workshop finder with ratings and prices from submitted data. Implement the workshop finder user interface showing real workshops from submitted data, and an empty area shows an empty state with one action. At 390 px and 1280 px, in Arabic and English, light and dark. Exit check: the workshop finder displays submitted workshops with ratings and prices. **Skills**: `modern-app-engineering`, `mobile-ergonomics-polish`.

14. Parts price comparison across shops. Implement the parts price comparison showing prices from more than one shop, sorted, with the source of each price. Exit check: a part search returns prices from multiple shops sorted cheapest first. **Skills**: `modern-app-engineering`.

15. Review and rating system for workshops and listings. Implement the review model, submission flow (refuses a review from a user who has not used the workshop), and editing by author only. Exit check: a user can submit a review for a workshop they've used, and edit/delete their own review. **Skills**: `firestore_rules_creation`.

## AI & Arabic

16. AI price estimate explanation in plain words. Implement the AI that explains the range and why it moves, in plain words, grounded in real data (trim price lists, submitted listings, customs tables). No AI in the number, only in the sentence. Exit check: a price estimate explanation renders correctly and attributes the range to its source. **Skills**: `gemini-api-dev`, `ai-gateway`.

17. AI specs comparison explanation in plain words. Implement the AI that explains the difference in plain words between two cars, based on data only. The comparison is data; AI only writes the sentence. Exit check: an specs comparison explanation renders correctly without invented differences. **Skills**: `gemini-api-dev`.

18. AI owner opinion summary from real submitted reviews only. Implement the AI that summarises real submitted reviews only, never invented opinions. Uses only real submitted reviews from the database. Exit check: an opinion summary renders using only real submitted reviews. **Skills**: `gemini-api-dev`.

19. Spare part identification from a photo (advisory only). Implement the AI that identifies the part from a photo and searches the parts catalogue, advisory only, never blocks a real part from being listed. Exit check: the part identification returns advisory results with part name and search links. **Skills**: `gemini-api-dev`.

20. Support assistant grounded in the help source. Implement the support assistant that answers from `docs/help/*.md` only and refuses anything not in the help source, and says so. Exit check: the support assistant refuses an ungrounded question and points to the help source. **Skills**: `gemini-api-dev`, `a11y-debugging`.

21. Arabic Egyptian first, English second on all screens. Implement per-character Arabic detection and live caret direction movement, and every mixed run isolated with `<bdi>` or `unicode-bidi: isolate`. The words "RTL" and "LTR" never appear to the user. Exit check: Arabic and English text renders correctly with proper bidi layout on all screens. **Skills**: `anti-vibecoded-design-system`, `modern-ui-ux-design-system`.

22. Currency auto-detected from visitor locale and IP, with manual override. Implement currency display in visitor's currency with the original EGP amount next to it. Exit check: a visitor from Saudi Arabia sees prices in SAR, with EGP equivalent shown. **Skills**: `modern-web-guidance`.

23. Dates and times formatted with `Intl`. Implement date/time formatting for licence renewals, insurance dates, service intervals, and cost-of-ownership dashboard. Exit check: dates display correctly in Egyptian format (e.g., 12/1/2024) and in MSA for international. **Skills**: `modern-web-guidance`.

## UI & Accessibility

24. Five states on every screen: Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake listing, a fake car, a fake review or a fake number. Exit check: every screen in the app has all five states implemented and working. **Skills**: `emil-motion-impeccable`, `modern-ui-ux-design-system`.

25. WCAG 2.2 AA accessibility audit. Every control has an accessible name. Touch targets at least 44 px with no covered hit area. Full keyboard path on every screen, visible focus, zoom from 80 to 200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured. Exit check: the accessibility audit passes with no violations on the critical journeys. **Skills**: `a11y-debugging`.

26. Colour contrast passes in light, dark, system and high-contrast themes. Implement the design token set with contrast ratios that meet WCAG AA. Exit check: the colour palette passes contrast checks in all four themes. **Skills**: `anti-vibecoded-design-system`.

27. No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. Implement the design system with calm automotive slate-blue `#1D4ED8` as seed colour. Exit check: a visual audit finds no styling violations of the forbidden patterns. **Skills**: `anti-vibecoded-design-system`.

28. Native app feel: browser text selection and right-click menu disabled site-wide and replaced by the app's own menu with in-app actions and a refresh. Normal select, copy and paste inside real input fields still work. Exit check: right-click opens the app menu, not the browser context menu. **Skills**: `modern-ui-ux-design-system`.

29. Font: IBM Plex Sans Arabic for Arabic, Cairo or Tajawal for display, for all screens. Exit check: all Arabic text uses the designated Arabic font. **Skills**: `modern-ui-ux-design-system`.

## Platform & PWA

30. PWA: web app that works offline (PWA). Implement service worker that caches the car record, the next reminder and the listing list. Background sync sends the queued actions when the connection returns. Offline car record, offline fuel and maintenance log, offline licence and insurance reminders. Exit check: the PWA can be installed and works offline with core features available. **Skills**: `vercel-cli`, `firebase_hosting_basics`.

31. Windows installable PWA from day one (M5). Implement the PWA installed as a Windows app with the same Google sign-in and self-update. Exit check: the Windows app installs and runs with Google sign-in. **Skills**: `modern-app-engineering`.

32. macOS installable PWA from day one (M5). Same as Windows but DMG build. Exit check: the macOS app installs and runs with Google sign-in. **Skills**: `modern-app-engineering`.

33. Linux installable PWA from day one (M5). Same as Windows but AppImage/.deb with .desktop entry. Exit check: the Linux package installs and runs with Google sign-in. **Skills**: `modern-app-engineering`.

34. Android Expo app (M4) for Android and iOS (M4). Same account, car record, fuel, maintenance, reminders, listings, workshops, parts. Exit check: the Android APK builds and installs on a device, and the same Google account sees the same car record on the web app. **Skills**: `android-cli`, `device-hub`.

35. iPhone and iPad Expo app (M4). Same account and data, tablet layouts. Exit check: the iOS build installs and shows tablet layouts with the same Google account. **Skills**: `android-cli`.

36. Desktop folder kit recreation. In `C:\Users\a7med\Desktop\SIR Projects\SIR Cars`, confirm `folder.ico` exists (named exactly that, never `icon.ico`), and the Desktop folder `SIR Projects/SIR Cars` holds `folder.ico`, `SIR Cars.lnk`, `Start SIR Cars dev.lnk`, `Stop SIR Cars dev.lnk`, `Open project folder.lnk` and `Versions.txt` reading version 1.0.0 and a plain status. Exit check: the Desktop folder kit is complete and all shortcuts work or are deliberately skipped. **Skills**: `make-icons-and-desktop` (via script).

37. Windows, macOS and Linux Electron shell (M5). Implement the Electron shell for Windows, macOS and Linux with the same Google sign-in and self-update. Exit check: the Electron app builds and runs on all three platforms. **Skills**: `modern-app-engineering`.

## Legal, Data & Release

38. Legal pack: all legal pages under `/legal/*`, each marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch". Exit check: every legal page exists and has the AI-drafted tag. **Skills**: `legal-compliance-shield`.

39. Data sources documented in `docs/DATA_SOURCES.md` with licence and last-checked date. Every price estimate cites one of the listed sources. Exit check: `docs/DATA_SOURCES.md` lists every data source with its licence and its last-checked date, and every price estimate on screen cites one of them. **Skills**: `database-reliability-transactions`.

40. Pricing page shows test prices with currency auto-detected, plus "Subscriptions launching soon" and an email capture that creates a lead document and rejects an invalid address. Exit check: the pricing page renders test prices in the visitor's currency with the "Subscriptions launching soon" badge, and the email capture validates and creates a lead document. **Skills**: `env-vars`, `routing-middleware`.

41. Rate limits on sign-in, listing creation, contact, uploads, AI calls and price-estimate calls. Exit check: rate limits are enforced and return appropriate HTTP 429 responses. **Skills**: `auth`.

42. Owner accounts get a second factor offer. Exit check: the Google sign-in page offers a second factor (SMS or authenticator app) after initial sign-in. **Skills**: `auth`.

43. CSP without `unsafe-inline` and without `unsafe-eval`. Exit check: the Content Security Policy passes audit and has no `unsafe-inline` or `unsafe-eval`. **Skills**: `modern-web-guidance`.

44. Analytics load only after consent, with Reject All as prominent as Accept. Exit check: the analytics consent banner works and analytics do not load before consent. **Skills**: `cookie-debugging`.

45. One-tap data export and one-tap deletion. Exit check: the user can export their data and delete their account with one tap. **Skills**: `legal-compliance-shield`.

46. Workshop and parts data is user-submitted and verified by a community report flow. Exit check: submitted workshops and parts appear in the finder after community verification. **Skills**: `modern-app-engineering`.

47. No fake data in any path a user can see. Exit check: a visual and data audit finds no invented users, listings, prices or ratings. **Skills**: `anti-vibecoded-design-system`.

48. Phone verification by OTP before a listing is published. Exit check: a listing cannot be published without a verified phone via OTP. **Skills**: `auth`.

49. Cross-tenant Firestore rules deny by default. Exit check: the Firestore rules prevent a user from reading another user's data. **Skills**: `firestore_rules_creation`.

50. Billing fallback page lead capture creates a lead document and rejects an invalid address. Exit check: the lead capture form validates the email address and creates a lead document on success, rejects invalid addresses. **Skills**: `env-vars`.

## Risks and Open Questions

51. Two-sided cold start on the marketplace. Risk: launching with too few listings or sellers. Recommended default: one city (Cairo) with 20 real listings and real sellers before any advertising or search push. No marketing before the sourcing tasks in the competitor file are done.

52. Receipt and odometer fraud. Risk: fake odometer readings and fake receipts. Recommended default: declared odometer on every listing, report-a-listing on every card, no auto-approval of anything, phone visible to the buyer only after a declared-interest tap.

53. Price data that goes stale. Risk: price estimates using outdated price lists. Recommended default: every price estimate shows its source and its last-checked date; a stale source is flagged, never silently used.

54. The real market already has a big brand. Risk: Hatla2ee owns car search intent. Recommended default: win on the whole car life, the owner tracker, Egyptian Arabic and trust, not on features we cannot verify.

55. Payments before the lawyer. Risk: real charges before legal review. Recommended default: test mode only, no real charge, no published plan price until the fee schedule and the legal pages are reviewed.

56. Gateway, customs and Traffic Authority numbers. Risk: official fees change. Recommended default: every one of them is "(unsourced, verify)" until read on the official page on the day it is used.

57. Static export killing the server. Risk: secrets dropped in static host. Recommended default: no secret ever in a route handler that a static host would drop; the server features run on the functions side from M1.

58. Arabic language support quality. Risk: Arabic bidi layout issues across platforms. Recommended default: per-character Arabic detection and live caret direction movement, and every mixed run isolated with `<bdi>` or `unicode-bidi: isolate`.

59. Cross-platform UI consistency. Risk: UI looks different on web vs mobile vs desktop. Recommended default: shared design tokens and components across all platforms, with platform-specific adaptations only where necessary.

60. Free tier features vs paid tier clarity. Risk: users confused about what is free vs paid. Recommended default: clear feature matrix on the pricing page, buyer never pays to see a price estimate or spec comparison, private seller never pays to list.

Now let me save this file and continue with the other requirements.