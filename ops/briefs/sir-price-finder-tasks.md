# Build tasks for SIR Price Finder (round r61 refresh, planning-only)

Ready to queue for the free agents. Each task is one paragraph; the agent reads the plan `D:/Projects/_SIR/plans/sir-price-finder.md` (sections 10-14 are the r61 research refresh) and the competitor study `D:/Projects/_SIR/ops/competitors/sir-price-finder.md` first, then does only this task, runs the checks, commits, pushes and ticks the checklist. Version stays 1.0.0. Lawful data only: official APIs, approved feeds, or user-submitted snapshots; never scrape product pages, never imitate a browser to get around a block.

## Foundations

1. Monorepo scaffold with tokens, RTL, the health route and CI. Create the monorepo skeleton under `D:/Projects/SIR Price Finder` (apps/web, apps/api, packages/core, packages/data, packages/ui, packages/kit, docs, scripts) with strict TypeScript, Tailwind v4 tokens, RTL-first styles, an `/api/health` route returning JSON, and a `pnpm verify` script that runs typecheck, lint, tests, build and gitleaks. Only a placeholder home page and the health route; no fake data. Exit check: `pnpm verify` runs and the output was seen green; the health route answers JSON. **Skills**: `modern-web-guidance`, `nextjs`, `react-best-practices`.

2. The product's own Firebase project and the `owner-auth` package with negative tests. Check first whether a Firebase project and a GitHub repo named `sir-price-finder` already exist; if not create the Firebase project `sir-price-finder` on the free Spark plan and the private GitHub repo `sirahmed8/sir-price-finder` as the only remote. Implement `owner-auth` (Google sign-in via Firebase Auth, ID token verified on the server with JWKS, owner/admin allow-list from env, HttpOnly Secure SameSite=Strict cookie, rate limits on sign-in, wishlist, alert, upload and AI calls, second-factor offer) with negative tests: forged token gets 403, client-side flag flip grants nothing, non-owner token on `/owner` gets 403. Write the Firebase project name and repo name in the project checkpoint. Exit check: tests pass; names written in the checkpoint. **Skills**: `firebase_basics`, `firebase_auth_basics`, `firestore_rules_creation`, `auth`.

3. The data model and the Firestore rules, with emulator tests. Implement domain types and zod schemas in `packages/core` (Product, Store, PricePoint, PriceHistory, WishlistItem, Alert, User, ManualPriceSnapshot, Lead) and Firestore repositories in `packages/data`, one interface per entity, deny-by-default rules, per-user claims. Emulator tests must include a cross-tenant read that fails. Exit check: emulator rules tests pass including the cross-tenant denial. **Skills**: `firebase_firestore`, `firestore_rules_creation`, `firebase_security_rules_auditor`.

4. Legacy parity matrix, read-only. Read the legacy `plans/sir-deals.md` price-comparison section (12 pages) and write `.sir/reports/parity.md` in the project folder listing every route with a keep/port/drop/drop-with-reason verdict and the file that proves it. Exit check: every legacy route has a verdict with proof; nothing is silently rebuilt thinner. **Skills**: `karpathy-skills`.

5. Design tokens and the three design directions. Write the token set (colour seed green `#16A34A`, spacing 4/8 grid, radii, shadows, type: IBM Plex Sans Arabic / Cairo or Tajawal, motion spring config stiffness 300-400 damping 28-30) and three explored directions with screenshots plus the chosen one in `docs/DESIGN.md`. Exit check: `docs/DESIGN.md` holds three directions with screenshots and the chosen one; tokens file exists and is used by the scaffold. **Skills**: `anti-vibecoded-design-system`, `modern-ui-ux-design-system`, `taste-design-engine`.

6. Desktop folder kit recreation. In `C:\Users\a7med\Desktop\SIR Projects\SIR Price Finder`, confirm `folder.ico` exists (named exactly that, never `icon.ico`) and the folder holds `folder.ico`, `SIR Price Finder.lnk`, `Start SIR Price Finder dev.lnk`, `Stop SIR Price Finder dev.lnk`, `Open project folder.lnk` and `Versions.txt` reading version 1.0.0 and a plain status; rebuild any missing piece from the project `assets/brand/` icons and `scripts/dev-*.ps1`. Exit check: every listed file exists and the shortcuts resolve. **Skills**: none (scripted file work).

## Lawful price sources

7. `PriceSource` interface and the price-point write path. Define the interface every store implements (`fetch(productRef) -> PricePoint[]` with source, currency, amount, listPrice, lastCheckedAt, raw evidence ref) in `packages/core`, plus the repository write path that stores points idempotently (same product+store+minute does not duplicate). Exit check: unit tests prove idempotent writes and that a point without source or timestamp is rejected. **Skills**: `database-reliability-transactions`, `production-engineering-standards`.

8. Amazon Creators API client with fixture fallback. Implement the Amazon **Creators API** client (OAuth 2.0 Credential ID + Secret, bearer token cached 1 hour, `creatorsapi.amazon/catalog/v1`, `x-marketplace` header, lowerCamelCase, Offers V2) behind `PriceSource`, reading credentials only from the ignored env file. If credentials or Associates eligibility are missing, the client reports "blocked on Associates approval" and returns fixtures in tests only. Offline fixture test with a recorded sample response; never store fake prices in any user-visible path. Exit check: fixture test passes; a missing-credential run exits cleanly with the blocked message and writes nothing. **Skills**: `gemini-api-dev` (HTTP client patterns), `env-vars`, `mimic-api-extractor`.

9. Jumia Egypt source via JForce/affiliate path. Implement the Jumia price source using the official JForce affiliate product/link API (beta) once the owner enrolls; until then the source is marked "pending enrollment" and products enter via manual snapshots. Tracked links must carry the affiliate tag only after enrollment; no commission logic in v1. Exit check: with a fixture, a Jumia product resolves to price + product URL; without enrollment the source reports its pending state honestly. **Skills**: `env-vars`, `production-engineering-standards`.

10. Manual price snapshot flow (covers Noon and any store without an approved feed). Implement `POST /api/products/manual-price`: a signed-in user (or the owner) pastes a store URL and the price they saw; the system stores a `ManualPriceSnapshot` with source="manual", the submitter, timestamp, and optional screenshot reference; it feeds the same price-history pipeline as API sources but is always labelled "reported by a user". Exit check: a manual snapshot appears in the product's history labelled as user-reported, and the API rejects unauthenticated writes. **Skills**: `firebase_auth_basics`, `firebase_firestore`, `vibe-auth-hardening`.

11. Price refresh scheduler job. Implement the `price-refresh` cron job (Firebase scheduled function or Vercel cron) that iterates tracked products, calls each enabled `PriceSource` with per-source rate limits and timeouts, writes new `PricePoint`s, and records per-source health (last success, consecutive failures, latency). A failing source degrades to stale-marked data, never an error page. Exit check: a dry run over fixtures writes points and a health record; a forced source failure is recorded and the run completes. **Skills**: `firebase_basics`, `firebase_app_hosting_basics`, `database-reliability-transactions`.

12. Stale-price marking and source transparency. Implement the rule that every price row and chart point shows source name + last-checked timestamp, and prices older than the source's refresh window render with a visible stale marker. Exit check: a fixture with a 3-day-old Noon manual price shows the stale badge and its real timestamp at 390 px and 1280 px, Arabic and English, light and dark. **Skills**: `modern-web-guidance`, `a11y-debugging`.

## Core product UX

13. Search route `/` with five states. The home/search screen: search box, recent searches (local), today's tracked drops for signed-in users. Idle, loading skeleton, empty with exactly one action, error with retry, populated. Exit check: all five states render at 320/390/1280 px in Arabic and English, light and dark; no horizontal scroll. **Skills**: `modern-web-guidance`, `emil-motion-impeccable`, `a11y-debugging`.

14. Product search results `/compare?q=`. Cross-store result list: per-store price rows (store name, price in visitor currency + original currency, source, last-checked, real-discount badge, sparkline thumbnail, product link). Store filter chips (Amazon.eg, Jumia, Noon/manual, others). Exit check: searching a fixture product shows all its store rows with correct currency formatting and the store filter narrows the list; five states hold. **Skills**: `react-best-practices`, `modern-ui-ux-design-system`.

15. Product detail `/product/[id]`. One product page: full price table across stores sorted cheapest first, history chart (30 days free, 365 days plus-gated), the real-discount badge with its one-line explanation, add-to-wishlist and set-alert actions. Exit check: page renders from fixture data with all five states; deep history is hidden for free tier and shown for plus; screenshot evidence at 390 and 1280 px both languages both themes. **Skills**: `nextjs`, `react-best-practices`, `chart` (none — use inline SVG sparkline, no chart lib).

16. Price history sparkline and chart component. A dependency-free SVG sparkline/chart component (30d/90d/365d ranges, min/max/avg labels, hover or tap detail, reduced-motion safe) fed by `PricePoint[]`. Exit check: renders correctly with 1 point, 30 points and 365 points; empty history shows the empty state, not a broken axis; works at 320 px width. **Skills**: `modern-web-guidance`, `emil-motion-impeccable`.

17. Real-discount badge and rubric. The deterministic rubric in `packages/core/real-discount`: given price history and a claimed "was" price, classify the discount "real" / "inflated" / "unverifiable" with a one-line explanation (Arabic and English strings). Badge component with icon + text, never colour alone. Unit tests cover: fake "was" price above all history = inflated; genuine drop = real; no history = unverifiable. Exit check: rubric tests pass; badge renders at 390/1280 px both languages both themes; `npm test` green. **Skills**: `production-engineering-standards`, `anti-vibecoded-design-system`.

18. Wishlist `/wishlist` with unlimited items. Save product (name, best price, store URL, image if lawful), list, edit target price, remove; persists in Firestore per user, syncs across devices when signed in, works anonymously via local storage until sign-in (then merges). Exit check: unlimited items save and persist across reloads; anonymous -> sign-in merge keeps items; five states at all breakpoints. **Skills**: `firebase_firestore`, `react-best-practices`, `modern-web-guidance`.

19. Compare view: side-by-side up to 3 products (plus tier). Select up to 3 tracked products and compare per-store prices, sparklines, badges and unit-price normalisation side by side. Exit check: 2- and 3-product comparisons render at 390 px (stacked) and 1280 px (columns); free tier is capped at 1 comparison with an upgrade prompt that is honest, not a dead end. **Skills**: `react-best-practices`, `modern-ui-ux-design-system`.

20. Unit-price normalisation (EGP/kg, EGP/ml, EGP/unit). Parse package size from product titles where a pattern is unambiguous, compute price-per-unit, show it as a secondary line on comparable rows; ambiguous parses show nothing rather than a guess. Exit check: fixture titles produce correct unit prices; ambiguous titles show no unit price; test covers Arabic and English unit words. **Skills**: `production-engineering-standards`.

21. Currency auto-detect with manual override. Detect visitor locale/IP -> EGP, SAR, AED, USD etc.; every price shows converted amount with the original currency next to it, rate source and date cited; manual override in `/settings` persists per user. Exit check: EG/SA/AE/US fixtures map to the right currencies; override wins; layout holds at 320 px both languages. **Skills**: `modern-web-guidance`, `i18n` patterns via `nextjs`.

22. Arabic-first bilingual UI. Egyptian Arabic first, English second, MSA only in legal pages; per-character direction detection with live caret movement, every mixed run isolated with `<bdi>`/`unicode-bidi: isolate`; logical CSS properties only; flipped directional icons. Exit check: mixed Arabic/English/price strings render correctly at 320-1920 px; no "RTL"/"LTR" words ever shown. **Skills**: `anti-vibecoded-design-system`, `modern-ui-ux-design-system`.

23. Dates, numbers and prices formatted with `Intl`. All dates/times via `Intl` in the active locale; prices via `Intl.NumberFormat` with the detected currency; Arabic-Indic numerals option respected. Exit check: a fixture timestamp renders correctly in ar-EG and en-US; no hard-coded date formats in components. **Skills**: `modern-web-guidance`.

## Alerts and notifications

24. Alert model and free-tier entitlement. One active alert per product on free, unlimited on plus; alert = product + target price + channel + quiet hours + status; entitlement enforced server-side from the Firebase token, never client flags. Exit check: a free user setting a second alert gets the honest upgrade prompt; a forged entitlement claim is rejected (test). **Skills**: `firebase_auth_basics`, `vibe-auth-hardening`, `firestore_rules_creation`.

25. Alert check job and exactly-once firing. The `alert-check` cron compares fresh `PricePoint`s to targets and fires at most one alert per product per drop (idempotency key = product+drop-event); 5 parallel checks produce exactly one alert and 4 clean rejections. Alert record stores fired/dismissed/acted-on for the owner analytics. Exit check: the parallel-check test passes; re-running the job does not re-fire. **Skills**: `database-reliability-transactions`, `firebase_basics`.

26. Telegram alert delivery with dry-run. Telegram sender for price-drop alerts (product name, new price, store, product link, badge verdict), dry-run mode that prints the message, real mode behind env config; quiet hours and digest mode honoured. Exit check: dry-run output shows the exact message; a real send (when owner configures the bot) arrives once; failures retry with backoff and are logged without message content secrets. **Skills**: `chat-sdk`.

27. Email fallback channel for alerts. Optional email channel when Telegram is unreachable or user prefers it; uses the transactional email path already in the kit if present, else a documented provider env slot; unsubscribe link in every alert email. Exit check: an alert can be delivered by email in test mode; unsubscribe works. **Skills**: `legal-compliance-shield`, `env-vars`.

28. Alert management UI `/alerts`. List active and fired alerts, edit target/channel/quiet hours, pause/resume, delete; fired-alert log with outcome marking (acted/dismissed). Five states everywhere. Exit check: all CRUD works against Firestore with entitlement checks; 390/1280 px both languages both themes. **Skills**: `react-best-practices`, `firebase_firestore`.

## AI features (metered, grounded)

29. AI price-history explanation. `POST /api/ai/explain` writes one plain-words sentence about why a price moved, grounded strictly in the real `PricePoint` series and event flags (season, sale campaign if known); the model never supplies numbers. Free users: 5 calls per rolling 24h with a visible badge; owner unmetered; `AI_ENABLED` kill switch; daily cost cap in `config/limits.json`. Exit check: eval set (ar+en) passes threshold; a response containing an invented number fails the truth check; quota badge counts down correctly. **Skills**: `gemini-api-dev`, `ai-gateway`, `omniroute-resilience-gateway`.

30. AI fallback chain wiring. Implement/verify the chain from `plans/AI_FALLBACK_CHAIN.md` (Gemini flash-lite -> flash -> any Gemini -> OpenRouter free -> other free -> local Ollama), one key per provider in env only, provider-that-answered logged per call (never content). Exit check: a forced 429 on the primary falls over to the secondary and the log records which provider answered; kill switch returns the non-AI fallback UI. **Skills**: `omniroute-resilience-gateway`, `ai-gateway`, `env-vars`.

31. Support assistant grounded in help docs. Floating assistant answering only from `docs/help/*.md` (price sources, alerts, currency, privacy), refusing ungrounded questions with a pointer to the help page; free-tier daily cap with visible badge, owner unmetered. Exit check: an off-topic question gets a refusal that names the help source; quota exhaustion shows the upgrade/email fallback. **Skills**: `gemini-api-dev`, `legal-compliance-shield`.

## Platform surfaces

32. PWA: installable, offline wishlist and history. Service worker caches app shell, wishlist and recently-viewed price charts; background sync queues alert-setting and manual snapshots; install prompt on supported browsers. Exit check: Lighthouse PWA checks pass; airplane-mode shows cached wishlist and charts with a stale-data banner. **Skills**: `firebase_hosting_basics`, `modern-web-guidance`.

33. Windows/macOS/Linux desktop builds (M5). One Electron shell (or installable-PWA path per plan section 4) producing NSIS installer, unsigned DMG and AppImage/.deb with .desktop entry, same Google sign-in and self-update feed; entry added to `Projects-Hub.html` and the Download page with version and size. Exit check: each build installs and signs in with the same account on the owner's machine or CI artifact. **Skills**: `modern-app-engineering`.

34. Android and iOS Expo app (M4). Same account, search, product detail, wishlist, alerts; push notifications for alerts as the mobile channel; tablet layouts. Exit check: Android APK builds and installs; same Google account sees the same wishlist on web and mobile. **Skills**: `android-cli`, `device-hub`, `mobile-ergonomics-polish`.

35. Widgets and live activities (M5/M6 per ADR). Android Glance widget and iOS WidgetKit surface showing next price drop and target price; decided by the M6 ADR, built only if approved. Exit check: widget renders real alert data; absent data shows an honest empty state. **Skills**: `modern-app-engineering`.

## Legal, monetisation and release

36. Legal pack under `/legal/*`. privacy (matches exact data collected, sub-processor list, DPA note, AI-training prohibition clause), terms (liability cap, AS-IS, arbitration), refunds (auto-renewal disclosure, 1-click cancel), cookies (pre-consent tracker blocker, Reject All as prominent as Accept); every page tagged "AI-drafted, to be reviewed by a qualified lawyer before paid launch". Exit check: all four pages exist with the tag and the tracker-block test passes. **Skills**: `legal-compliance-shield`.

37. Pricing page with fair fallback. `/pricing` shows Free and Plus test prices (29 EGP/mo or 290 EGP/yr, ~USD equivalents) with auto-detected currency and original EGP amount; payment CTAs show "Subscriptions launching soon" and open a lead-capture modal storing email in Firestore with validation. Exit check: no broken checkout link exists; lead capture creates a document and rejects invalid emails; prices render in visitor currency. **Skills**: `env-vars`, `routing-middleware`, `high-conversion-copywriting`.

38. Billing webhook readiness (test mode only). Paymob/Fawry webhook endpoint with HMAC-SHA256 verification (timestamp inside signed body), server-side only, rejecting tampered/replayed/unsigned/wrong-timestamp events; stays in test mode until the lawyer review. Exit check: the four rejection cases each return the correct error and a valid test event is accepted once. **Skills**: `vibe-auth-hardening`, `webhook-testing`, `zero-trust-security-hardening`.

39. One-tap data export and deletion. User can export all their data (wishlist, alerts, snapshots they submitted) as a file and delete their account + data in one tap, with a written confirmation and a 30-day recovery window note. Exit check: export produces a complete file; deletion removes user docs and is verified by rules test. **Skills**: `legal-compliance-shield`, `firebase_firestore`.

40. CSP, headers and consent-gated analytics. CSP without `unsafe-inline`/`unsafe-eval`; analytics load only after consent with Reject All equal-prominence; cookie banner pre-blocks trackers. Exit check: header audit passes; a fresh visit shows zero tracker requests before consent. **Skills**: `modern-web-guidance`, `cookie-debugging`.

41. Rate limits everywhere they matter. Sliding-window limits on sign-in, search, manual-price submit, alert CRUD, AI calls and webhooks; 429 with Retry-After; per-IP and per-user buckets. Exit check: burst tests hit 429 correctly and legitimate use is unaffected. **Skills**: `auth`, `zero-trust-security-hardening`.

42. Owner analytics `/owner`. Server-verified owner route showing real aggregates only: tracked products, alerts fired/dismissed/acted, price drops detected, estimated user savings in EGP, source health panel, AI cost per call, error rate; empty metrics show a dash and reason. Exit check: non-owner and forged tokens get 403; every number traces to a real aggregate query. **Skills**: `firebase_auth_basics`, `firebase_firestore`, `routing-middleware`.

43. Dual hosting: Firebase Hosting + Vercel. Deploy the same build to the product's Firebase Hosting and import the repo into Vercel with the CLI; identical env on both; curl-check both addresses and write them in the project checkpoint. Exit check: both URLs return 200 and `/api/health` is green on both. **Skills**: `firebase_hosting_basics`, `vercel-cli`, `deployments-cicd`.

44. Evidence pack and self-audit loop. Screenshots at 320/390/768/1280/1920 px in ar+en, light+dark+high-contrast, five states visible; Playwright on critical journeys (search -> product -> wishlist -> alert); Lighthouse mobile >= 90; click-target audit in CI; self-audit loop until two clean cycles. Exit check: evidence files exist under `.sir/evidence/` and the audit report shows two clean cycles. **Skills**: `a11y-debugging`, `chrome-devtools`, `verification`.

45. Launch package (owner-gated). Domain, OAuth branding review, legal review status, first tracked products list, Telegram bot setup, and the "public or stay personal" decision recorded as an ADR. Exit check: `docs/LAUNCH.md` lists every item with owner/not-owner and its status; nothing public-facing ships before the owner's go. **Skills**: `commercial-app-blueprint`, `legal-compliance-shield`.

46. Seasonal sales calendar (M4+). Show per-store typical sale windows (from observed history only, labelled as observed patterns not promises) and a "likely sale soon" hint on tracked products. Exit check: hints derive only from real history; a product with thin history shows no hint. **Skills**: `production-engineering-standards`.

47. Browser extension one-click track (M4+, ADR-gated). Manifest V3 extension adding the current product page to the wishlist via the manual-snapshot/lookup flow; store review checklist documented. Exit check: extension installs, adds a product, and the item appears in the web wishlist; deferred if the M6 ADR says no. **Skills**: `chrome-extensions`, `modern-web-guidance`.

48. Performance and scale pass at 1,000+ tracked products. Index review, query plans, pagination on history endpoints, load script proving the latency budget, bundle-size budget enforced in CI. Exit check: load script output saved in `.sir/evidence/`; CI fails on budget regression. **Skills**: `debug-optimize-lcp`, `production-engineering-standards`.

## Risks and open questions for the build agents

49. R1 thin lawful coverage -> never imply coverage we lack; every price row names its source. Recommended default already in plan section 14.

50. R2 Amazon Associates eligibility (10 sales/30d) -> fixture fallback from day one; report "blocked on Associates approval" honestly. Owner action if wanted: enroll in Amazon.eg Associates (free) — listed in OWNER_ACTIONS when the time comes.

51. R3 third-party scrape APIs -> banned for stored price data in v1; revisit only with written terms.

52. R4 stale prices -> source + last-checked always visible; stale marker beyond the refresh window.

53. R5 alert fatigue -> one alert per drop, quiet hours, digest mode; exactly-once enforced by idempotency key.

54. R6 currency accuracy -> original currency + rate source/date on every converted price.

55. R7 paid tier before legal -> test prices only, fallback capture, no real charge before lawyer review.

56. Q1 Noon official feed -> re-check quarterly; manual snapshots meanwhile.

57. Q2 Google Shopping paid API -> no until revenue exists.

58. Q3 browser extension timing -> M4+ behind the M6 ADR.

59. Q4 personal vs public -> personal-first; launch is the owner's call.

60. Open: which store categories to seed first for the owner (recommend: the owner's own frequent purchases — headphones, phone accessories, home goods) so the first real history is useful on day one.
