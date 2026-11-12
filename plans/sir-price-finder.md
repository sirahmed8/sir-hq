# PLAN: SIR Price Finder (Wave 6, independent product, rebuild from zero)

## Vision (owner, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` section 5)

SIR Price Finder compares the price of any product across stores (Egypt first: Amazon.eg, Noon, Jumia, local stores, then global), shows price history, detects fake discounts, supports wishlists and alerts when it drops. Only public data and official APIs or feeds; respects each site's terms. This is an independent small product with the same premium standard as every other SIR product.

**Version 1.0.0.** Audited and rewritten 2026-11-12 (round r54, HQ). Supersedes the old `plans/sir-deals.md` price section, which is now split: Price Finder and Game Deals are separate projects. The canonical competitor study is `D:/Projects/_SIR/ops/competitors/sir-price-finder.md` (opened sources dated 2026-11-12). The first ten build tasks for the free agents are in `D:/Projects/_SIR/ops/briefs/sir-price-finder-tasks.md`.

**Product class: SMALL INDEPENDENT.** Anyone can use it to compare prices, accounts and subscriptions are not required (free tier unlimited, paid tier optional for advanced alerts), every platform is planned from one codebase, the owner has an owner-only analytics page, the site is hosted twice (Firebase Hosting and Vercel), and a free tier gives the owner every basic feature. A paid tier gives extra alert slots and deeper history.

---

## 1. Who it is for, and the promise

**For the bargain hunter.** The person who wants to buy a product (headphones, coffee maker, phone case, etc.) at the best price without checking ten websites. The one-line promise, in the words a user would use:

> Find the best price for any product across Amazon.eg, Noon, Jumia and global stores, see its price history, and get alerted when it drops.

**For the gift shopper.** The person buying a gift who wants to make sure they are not overpaying. The one-line promise for that side:

> Compare prices across stores, see if the "discount" is real, and get notified the moment the price falls.

**The end state we sell.** A user opens the app, searches for a product, sees a table with the price at each store, a small history sparkline, and a "real discount" badge. They add it to a wishlist, set an alert, and get a Telegram notification the moment the price falls below their target. The owner opens the same product on their phone, sees which items have price drops, the cash collected from alerts, and one tap to publish the find to a friend.

**Not in v1:** no fake "discount from X EGP" claims that are actually the regular price; no paid tier required to see price history; no ads in any tier, ever.

---

## 2. The ten competitors, and where we win

Full table with sources, dates and the second ring of competitors: `D:/Projects/_SIR/ops/competitors/sir-price-finder.md` (read on 2026-11-12).

| Competitor | What it proves about the market | Our edge |
|---|---|---|
| Google Shopping | Covers the widest retailer network globally; price history and "track price" feature; heavy ads and sponsored products cloud organic results; no deep Arabic/Egyptian store coverage | Local Arabic store coverage (Amazon.eg, Noon, Jumia) with the same track-price UX; zero ads in the product; all data stays on the owner's device |
| CamelCamelCamel | Deep Amazon price history going years back; email alerts when price drops below target; Amazon-only — no other retailers; US/UK Amazon stores only; no Egypt/MENA Amazon support | Tracks Amazon.eg price history with the same chart UX; adds price history for Noon, Jumia, and local Egyptian stores; multi-store wishlist in one place |
| Keepa | Extremely deep historical data (up to several years); advanced alerts (price drop, stock, Buy Box change); paid plans required for full history and many alerts; UI is complex and overwhelming for casual users | Simpler UX than Keepa; free tier with essential price history; no account needed to view history; Arabic Amazon.eg support added |
| Idealo | Covers 15+ European countries and many retailers; price history and price drop alerts; browser extension and app; weak or no coverage of Middle Eastern stores; EUR pricing focus, less relevant for EGP shoppers | Covers Egypt and Arab world stores (Noon, Jumia, Souq archive, Amazon.eg) alongside European/Global retailers; EGP currency auto-detection; free tier with all core features |
| ShopSavvy | Barcode scanner works in-store to find cheaper online prices; broad retailer coverage via scan; heavy ad-supported free tier; scanner experience varies by region; limited price history beyond the current scan | Barcode scanning integrated with cross-store history; no ads; Egyptian store barcodes (Noon, Jumia) recognized; price history saved locally |
| Slickdeals | Community-vetted deals with hotness voting; real-time price drop alerts for tracked items; quality varies; not all deals are genuine; no structured price history charts; US-centric; limited Arabic/EGP coverage | Curated deals filtered for Egyptian and Arab stores; price history charts built-in; honest fake-discount detection (our rubric, not community voting) |
| PriceSpy | Covers 30+ countries and many product categories; user reviews alongside prices; price history and wishlist; Middle Eastern store coverage is thin (Noon present, Amazon.eg absent); UI feels dated in some regions; wishlist limited to registered accounts | Wishlist works without an account; Egyptian stores (Noon, Jumia, Amazon.eg) are first-class; fake-discount detection rubric built-in; EGP auto-detection from visitor locale |
| Honey (Capital One) | Automatically applies promo codes at checkout; tracks price history on supported sites; closes tab after applying; no persistent price history view; US-centric; limited Arabic store support | Persistent wishlist and price history view; fake-discount detection (compares claimed "discount" vs historical price); Arabic store (Noon, Jumia, Souq) code support; all data local to owner |
| Noon Store | Largest online retailer in Egypt; wide product catalog across many categories; cash on delivery available; no price comparison across stores — only Noon prices; no price history or alerts for past prices; limited global retailer coverage | Price comparison across Noon vs Amazon.eg vs Jumia vs global; price history for Noon products; local store focus built-in |
| Amazon.eg | Egypt Amazon store with product pricing; trusted global brand with Egypt localization; wide product selection; no price comparison — only Amazon.eg prices; no price history or alerts for past prices; limited to Amazon's own inventory only | Compare Amazon.eg prices vs Noon, Jumia, and global retailers; price history tracking; wishlist across stores |

---

## 3. Features

### 3.1 Parity with the best in the category (must ship)

| Feature | Why it is in the list | Source of the requirement |
|---|---|---|
| Product search across stores | User searches for a product name and sees prices at each store | Google Shopping, CamelCamelCamel |
| Price history sparkline | User sees price over time (days/weeks/months) | Keepa, Idealo |
| "Real discount" badge | Every "discount from X EGP" claim is verified against the product's own price history; if the "original price" never existed, the badge shows "inflated" with a one-line explanation | Our rubric (research needed) |
| Wishlist save | User saves a product to a personal list | Google Shopping, Slickdeals |
| Price-drop alert | User sets a target price; gets notified (Telegram) when the price falls below it | Slickdeals, PriceSpy |
| Currency auto-detection | From the visitor locale and IP, shows EGP for Egypt, SAR for KSA, etc., with manual override on top | Idealo |
| Store filter | User can show/hide stores (Amazon.eg, Noon, Jumia, global) | Our design |
| Product page URL link | Each price entry links to the original product page on the source store | All competitors |
| Compare two or more products | User selects two products and sees a side-by-side price comparison | Our design (gap in category) |

### 3.2 The owner's own ideas, carried forward from legacy and TickTick

Every line says where it came from, so nothing gets silently rebuilt thinner than what he already asked for.

| Idea | Source | Status in this plan |
|---|---|---|
| Barcode scanner to add a product to track | TickTick note "أفكار برامج ومشاريع" idea 15 (price and game-deal finder) | M2, uses device camera or manual search |
| Price history export as CSV | TickTick note idea 15 | M3, user can export their tracked items |
| Fake-discount detection rubric with one-line explanation | TickTick note idea 15; research needed for the category | M2, the core trust feature |
| Multi-currency wishlist (EGP, SAR, USD) | TickTick note idea 15 | M3, auto-detected from locale |
| Telegram alert when price drops | TickTick note idea 15 | M2, the core alert mechanism |
| Browser extension one-click track | TickTick idea 15 | M3, add any product from any browser page |
| Seasonal sales calendar | TickTick "30-Day Projects Sprint" | M4, shows when stores typically discount |
| Historical lowest price badge | TickTick note idea 15 | M2, shows the all-time low |
| Price per unit (EGP/kg, EGP/ml) auto-calc | TickTick idea 15 | M3, helps compare similar products |

### 3.3 Explicitly out of scope for v1

- Scraping product pages that break a retailer's Terms of Service
- Paying for a subscription to get historical data
- Real-time stock availability (price only)
- Integration with checkout/purchase flow

---

## 4. Platform matrix

Standing rule (owner, 2026-11-12): every product ships on all platforms, so web, Windows, macOS, Linux, Android and iOS are all required for SIR Price Finder.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required | The whole product: search, price table, history sparkline, wishlist, alerts, currency auto-detect | Nothing pending |
| PWA (installable, offline) | Required | Install from the browser, offline wishlist, offline price history sparkline, background sync for alerts | Native shell if the PWA proves weak on low-end Android |
| Windows | Required (M5) | Installable PWA from day one, then a real NSIS installer with the same Google sign-in and self-update | Signed installer (owner buys the certificate) |
| macOS | Required (M5) | Installable PWA from day one, then an unsigned DMG from the same Electron build | Signed build when the owner has an Apple account |
| Linux | Required (M5) | Installable PWA from day one, then AppImage and .deb from the same Electron build with a .desktop entry | Signed package |
| Android phone and tablet | Required (M4) | Expo app: the same account, search, price history, wishlist, alerts | Play Store when the reinvestment ladder allows |
| iPhone and iPad | Required (M4) | Expo app, same account and data, tablet layouts | App Store or SideStore (needs a paid Apple account, the owner decides) |
| Wear OS | Skipped in v1 | Nothing | A kickoff countdown widget, decided with an ADR |
| watchOS | Skipped in v1 | Nothing | Same ADR as Wear OS |
| TV (Android TV and Apple TV) | Skipped in v1 | Nothing | A screen with today's price drops and the wishlist, only if a real use case appears |
| Car (Android Auto and CarPlay) | Skipped in v1 | Nothing | Navigation to the product page only if a paid tier needs it |
| Widgets and live activities | Part of M5 | Android Glance and iOS WidgetKit: the next price drop and the target price | Richer surfaces later |
| Browser extension | Skipped | Nothing | No browser use case that justifies the review in v1 |
| Docker and self-host | Skipped | Nothing | Not a product need here |

**Rule:** every platform shares one Firebase project, one account and one dataset. No platform ever carries its own copy of the rules. The Windows, macOS and Linux builds come from one Electron shell and one release feed, so an update reaches all three at once.

---

## 5. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. That file is the shared standards kit every product builds against; SIR Platform was cancelled as a project on 2026-11-12, so there is no extraction target any more. SIR Price Finder is a SMALL INDEPENDENT product, so it adopts the essential sections of the kit as internal `packages/*` with the kit names and interfaces, and when it hardens a piece that other products need, that piece goes back into the kit file and HQ queues the adaptation for the others.

### 5.1 Shape

```
apps/web        Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens
apps/api        Route handlers that need secrets and long tasks (webhooks, cron, AI proxy)
packages/core   Domain types and zod schemas: Product, Store, Price, Wishlist, Alert, User
packages/data   Firestore repositories, one interface per entity, emulator tests
packages/ui     The shared UI kit from the kit: InputBox, TabBar, BottomSheet, Card, Chip, Modal, Toast
packages/kit    owner-auth, billing-fallback, ai-proxy, legal-pack, i18n, help-center, notifications
apps/mobile     Expo app for Android and iOS (M4)
apps/desktop    Electron shell for Windows, macOS and Linux (M5)
docs/           Help centre source, legal source, env names, decisions
scripts/        Seed-free checks, emulator tests, Lighthouse, AI evals
```

Layers depend inward only: presentation, domain (no I/O), data, core. Files under 300 lines, no `any`, no god components, absolute imports.

### 5.2 Accounts (`owner-auth`)

- Google sign-in through Firebase Auth on the product's own Firebase project, ID token verified on the server with JWKS.
- Owner and admin rights come from an allow-list (`OWNER_EMAILS`, `OWNER_UIDS`), fail closed. Nothing in the client decides a privilege.
- Session in an HttpOnly, Secure, SameSite=Strict cookie. No tokens in localStorage.
- Rate limits on sign-in, alert, wallet requests, uploads and AI calls.
- Owner accounts get a second factor offer.
- Test: a forged token gets 403, a client-side flag flip gets nothing, a non-owner token on `/owner` gets 403.

### 5.3 Owner-only analytics page

- Route `/owner`, server-verified owner token, 403 for everyone else.
- Real metrics only, read from aggregates not raw collections: number of tracked products, alerts fired, price drops detected, users who clicked, average price saving in EGP.
- No invented numbers anywhere: an empty metric shows a dash and the reason, never a zero dressed as a fact.

### 5.4 AI with the fallback chain

Chain from `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`: Gemini `flash-lite-latest`, then `flash-latest`, then any Gemini text model, then OpenRouter free models, then other free providers, then the local model on this PC. One Gemini key and one OpenRouter key per product, created on this product's own project, stored only in the ignored env file and the Vercel environment, never printed, never committed.

What AI does in this product, and what it must never do:

| Feature | AI role | Hard rule |
|---|---|---|
| Price history explanation | Explain why a price changed (seasonal, promotion, stock change) in plain words | The price history data itself is real; the model only writes the sentence |
| Wishlist note draft | Draft the note the user writes when saving a product | Numbers come from the database, the model only writes the sentence |
| Fake-discount rubric feedback | Tell the user in plain words why their "discount" flag is "real" or "inflated" | The rubric is a pure function with a test; the model only explains the result |

Free users get 5 AI calls per rolling 24 hours with a visible badge, the owner is unmetered, `AI_ENABLED` is the kill switch, a daily cost cap lives in `config/limits.json`, and every call logs which provider answered (never the content). Arabic and English eval sets exist before the feature ships, and the runner exits non-zero below the threshold.

### 5.5 Data and money

- Firestore with deny-by-default rules, per-user claims, emulator tests including a cross-tenant read that must fail.
- A tracked product is a document with a status, current price, last-seen price, and an alert target.
- Wishlist items are user-owned; each has a target alert price and a last-notified timestamp.
- Alerts are firestore documents with a target price, a source store, and a notification status.
- Price data is fetched from official APIs or approved feeds only; no anonymous scraping.
- A user's phone number is visible only after a booking exists (if the product adds that feature later).
- Wallet and card payments through Paymob and Fawry in test mode only. The webhook is HMAC-SHA256 signed with the timestamp inside the signed body, verification is server-side only, and tampered, replayed, unsigned and wrong-timestamp events are rejected.
- Refunds and cancellation follow one written policy for every venue, published on the pitch page before payment.

### 5.6 Hosting and delivery

- **Firebase Hosting** is primary. **Vercel** is the second host, the same repository imported with the Vercel CLI, the same build, the same environment variables on both. Both addresses are curl-checked and written into the project checkpoint.
- Static hosting cannot run route handlers, so every secret, webhook and AI call lives in the Firebase Functions or the Vercel function side, never in the client bundle. This is the exact defect that killed the legacy apps (`/api/ai/chat`, `/api/ai/tts`, `/api/admin/role` returned 404 in production because the apps were exported as static).
- A service worker caches the pitch list, the next booking and the pass. Background sync sends the queued actions when the connection returns.
- Daily Firestore export to a private bucket, a monthly restore test, a health endpoint at `/api/health`, a status JSON, a nightly error digest and a weekly Telegram report at a round hour.

### 5.7 Security baseline

Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI. A CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent, with Reject All as prominent as Accept. One-tap data export and one-tap deletion. Rate limits on auth, booking, uploads, AI and webhooks. No fake data in any path a user can see.

---

## 6. Premium quality bar

This is the floor from `D:/Projects/_SIR/standard/23-premium-code-bar.md` and `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`, written for this product.

**Motion, Apple level.**

- One shared spring config across the app: stiffness 300 to 400, damping 28 to 30, transform and opacity only, no layout thrashing, 120 Hz safe.
- Every sheet, drawer, modal and panel opens and closes with the same spring. An open-only animation is a defect.
- Skeletons match the final geometry, optimistic feedback lands under 100 ms, and no white flash on theme change.

**Two languages, one layout.**

- Egyptian Arabic first for players and owners, English second for the international market, MSA only in legal pages. Both shipped together, never one as a partial translation.
- RTL designed first: logical CSS properties only, flipped directional icons, Arabic line heights, never a mirrored afterthought.
- Every text input detects Arabic or Latin per character as the user types and moves the caret and the direction live. Every mixed run is isolated with `<bdi>` or `unicode-bidi: isolate`. The words "RTL" and "LTR" never appear to the user.
- Currency auto-detected from the visitor locale and IP, with a manual override on top. Dates and times formatted with `Intl`.

**Five states on every screen.**

Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake pitch, a fake player or a fake number.

**Accessibility.**

WCAG 2.2 AA. Every control has an accessible name. Touch targets at least 44 px with no covered hit area. Full keyboard path on every screen, visible focus, zoom from 80 to 200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured, and a colour pair that passes contrast in light, dark, system and high-contrast themes.

**The look.**

One design system: tokens for colour, spacing on a 4 and 8 px grid, radii, shadows, type and motion. Seed green `#16A34A` for a price-finder product, calm neutral canvas, accent only for primary actions and key numbers. No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. One component per control, never two. Arabic screen face: IBM Plex Sans Arabic, Cairo or Tajawal.

**Native app feel.**

The browser's text selection and the right-click menu are disabled site-wide and replaced by the app's own menu with in-app actions and a refresh. Normal select, copy and paste inside real input fields still work.

**Evidence before the word done.**

Screenshots at 320, 390, 768, 1280 and 1920 px, in Arabic and English, in light and dark, plus 3840 px once. Playwright on the critical journeys. Lighthouse mobile 90 or better. A click-target audit in CI. The self-audit loop runs until two clean cycles.

---

## 7. Free tier and fair pricing (EGP and USD)

These are **test prices**, not published prices. They are the outline the owner confirms with real users before anything is charged. The free tier is unlimited; the paid tier is optional for advanced alert slots and deeper history.

| Plan | Who | EGP | USD | What it includes | Rule |
|---|---|---|---|---|---|
| Free | Any user | 0 | 0 | Search any product, see price at Amazon.eg, Noon, Jumia, global stores, price history sparkline, real-discount badge, save unlimited items to wishlist, set 1 alert at a time, currency auto-detect | The core action is never behind a plan |
| Plus | Serious users | 29 per month or 290 per year (test) | about 0.60 per month or about 6 per year | Unlimited alerts (instead of 1), deeper price history (365 days instead of 30), compare up to 3 products side-by-side, export wishlist as CSV, email alert fallback (if Telegram unreachable) | Cancel any time, the plan lapses at the end of the paid month |
| Owner | The product owner | 0 | 0 | Every paid feature free, all permissions inside the owner console, can view all alerts across all users (aggregated only), can add custom alert targets | One-tap data export and one-tap deletion |

**Fairness rules written into the product.**

1. A user never pays to track a price, and the app never takes a cut of a user's share.
2. The free tier is truly free: no caps on searches, no caps on wishlist items, no caps on price history.
3. Every price on screen is in the visitor's currency, auto-detected, with the original EGP amount next to it.
4. An alert fires only once per price drop; no spam.
5. No ads, in any tier, ever. The owner sets an ad spend cap of 0 until he changes it.
6. The owner of the product gets every paid feature, free, and a subscription grants him all permissions inside the owner console.

**Still open and blocking publication:** the official Paymob and Fawry fee schedules for Egypt, the tax and invoicing treatment of venue fees in Egypt (if the paid tier is ever charged), the exact cancellation and refund wording, and the lawyer review of every legal page. Each is tagged "(unsourced, verify)" in `ops/competitors/sir-price-finder.md` section 4 and in `docs/ENV.md` when the project starts.

---

## 8. Milestones M0 to M6, with acceptance tests

Every exit check is something a reviewer can run or click. "Green" means the output was seen, not assumed.

### M0: Foundations, the kit and the honest map of the legacy

Work: create the product's own Firebase project named `sir-price-finder` (free Spark plan) and keep it separate from every other product; scaffold the monorepo (apps, packages, docs, scripts) with strict TypeScript, Tailwind v4 tokens, RTL-first styles and the shared `verify` script; write the legacy parity matrix; design the token set and the three design directions; recreate the Desktop folder kit from scratch for the new build.

Exit checks:

1. `D:/Projects/SIR Price Finder` contains `folder.ico` (named exactly that, never `icon.ico`) and the Desktop folder `SIR Projects/SIR Price Finder` holds `folder.ico`, `SIR Price Finder.lnk`, `Start SIR Price Finder dev.lnk`, `Stop SIR Price Finder dev.lnk`, `Open project folder.lnk` and `Versions.txt` reading version 1.0.0 and a plain status. The old kit belonged to the legacy build, so M0 rebuilds it.
2. `.sir/reports/parity.md` lists every route of the legacy `sir-deals.md` (the price comparison section merged, 12 pages with a keep, port, drop or drop-with-reason verdict and the file that proves it).
3. `pnpm verify` runs typecheck, lint, tests, build and gitleaks, and the output was seen green.
4. The Firebase project `sir-price-finder` exists and the GitHub repo `sirahmed8/sir-price-finder` is the only remote for it.
5. `docs/DESIGN.md` holds three explored directions with screenshots and the chosen one, plus the token file and the balancer prototype running at 120 Hz.

### M1: The price comparison core, proven under contention

Work: the data model and the Firestore rules for Product, Store, Price, Wishlist, Alert; the price fetch script for Amazon.eg (first product, offline fixture test); the price fetch script for Noon (first product, offline fixture test); the price history sparkline; the real-discount badge with the rubric; the wishlist save; the 1-alert-at-a-time limit; the currency auto-detect from visitor locale and IP; five states everywhere.

Exit checks:

1. The emulator rules tests pass, including a cross-tenant read that must fail.
2. Price history fetch for Amazon.eg produces a valid sparkline for a tracked product (offline fixture test passes).
3. Price history fetch for Noon produces a valid sparkline for a tracked product (offline fixture test passes).
4. The real-discount badge correctly flags an "inflated" price when the "original price" never existed in the history, and shows "real" when the discount is genuine, at 390 px and 1280 px, in Arabic and English, light and dark.
5. The wishlist save persists across reloads and stores the product name, price, and store URL.
6. The currency auto-detect shows EGP for Egypt visitors, with manual override widget.
7. The price table renders all five states (idle, loading skeleton, empty with one action, error with retry, populated) at 390 px and 1280 px, in Arabic and English, light and dark.

### M2: Alerts and wishlist, proven at scale

Work: the alert target price and the one-alert-at-a-time limit; the wishlist with unlimited items; the Telegram alert when price drops below target; the side-by-side product compare (up to 3 products); the fake-discount rubric applied to all tracked products; the CSV export of wishlist; five states everywhere.

Exit checks:

1. A user can set an alert target price for a tracked product; when the price drops below the target, a Telegram alert is sent (dry-run mode first, then real).
2. A user can save unlimited items to a wishlist; the wishlist persists across reloads and stores the product name, price, and store URL for each item.
3. The side-by-side product compare shows up to 3 products with their prices at different stores, the history sparklines, and the real-discount badges.
4. The CSV export of the wishlist downloads a file with the correct columns (product name, price, store, URL).
5. The fake-discount rubric is applied to all tracked products: if the "original price" never existed, the badge shows "inflated" with a one-line explanation; if the discount is genuine, it shows "real".
6. The Telegram alert fires exactly once when the price drops below the target, and the alert includes the product name, the new price, and a link to the product page.
7. 5 parallel alert checks for one product produce exactly one alert and 4 clean rejections (no duplicate alerts).

### M3: AI, deeper history, and the paid tier

Work: the AI explanation of price history changes; the deeper price history (365 days instead of 30) for Plus tier; the side-by-side product compare (up to 3 products); the CSV export of wishlist; the paid tier entitlements; five states everywhere.

Exit checks:

1. `npm run eval:ai` passes with Arabic and English eval sets, and the AI explains a price history change in plain words without inventing data.
2. The deeper price history (365 days) is available for Plus-tier users; Free-tier users see only 30 days.
3. The side-by-side product compare shows up to 3 products with their prices at different stores, the history sparklines, and the real-discount badges.
4. The CSV export of the wishlist downloads a file with the correct columns (product name, price, store, URL).
5. The Plus tier entitlements are enforced: a Free-tier user who tries to set a second alert gets a "upgrade to Plus" message; the entitlement check uses the Firebase token.
6. Lighthouse mobile is 90 or better and the JSON is saved in `.sir/evidence/`.

### M4: API, extensions, and the quality pass

Work: the browser extension one-click track; the API endpoints for price history and alerts; the Windows installer with the same sign-in and self-update; the macOS and Linux builds; the full self-audit; Lighthouse mobile 90 or better.

Exit checks:

1. The browser extension one-click track adds the current product to the user's wishlist (install from the store, verify it works).
2. The API endpoints for price history and alerts return valid JSON for a tracked product; the API uses the Firebase token for auth.
3. The Windows installer installs, starts, signs in with the same Google account, updates itself, and its entry is in `Projects-Hub.html` and on the Download page with the version and the size.
4. Screenshots exist at 320, 390, 768, 1280 and 1920 px in both languages and in light, dark and high contrast, with the five states visible.
5. The accessibility audit passes WCAG 2.2 AA with an accessible name on every control, no covered hit area, and no horizontal scroll from 320 px.
6. Each legacy folder moves from `legacy/` to `D:\Projects\old projects\` only after the parity matrix shows every kept feature is ported and verified, keeping the git history. `legacy/` is never deleted from the repository history.

### M5: Release, real products and the legacy handover

Work: the launch package (domain, accounts, legal review); the first real products onboarded with written consent; the legacy handover.

Exit checks:

1. Three real products are live with a written consent, a real price and a real owner, and no seeded or invented product exists in any path a user can see.
2. The 301 redirects from the three old hosts are verified by curl.
3. The legacy keys are rotated and the service-account file is out of the repository.
4. The lawyer has reviewed the legal pages and the tax question is answered, and only then can a paid plan go live.
5. Each legacy folder moves from `legacy/` to `D:\Projects\old projects\` only after the parity matrix shows every kept feature is ported and verified, keeping the git history. `legacy/` is never deleted from the repository history.

### M6: Release, real products and the legacy handover

(M6 is the same as M5 for this small independent product; the milestones merge at release.)

---

## 9. The first ten tasks for the free agents

Ready to queue, each with its own brief: `D:/Projects/_SIR/ops/briefs/sir-price-finder-tasks.md`.

1. Legacy parity matrix, read-only, into `.sir/reports/parity.md`. Read the legacy `sir-deals.md` price section, list every route with a keep/port/drop/drop-reason verdict, and write the verdict file with the file proof.

2. Monorepo scaffold with tokens, RTL, the price-compare route and CI. Scaffold the monorepo (apps/web, apps/api, packages/core, packages/data, packages/ui, packages/kit) with strict TypeScript, Tailwind v4 tokens, RTL-first styles and the shared `verify` script that runs typecheck, lint, tests, build and gitleaks.

3. The product's own Firebase project and the `owner-auth` package with negative tests. Create the Firebase project `sir-price-finder` (free Spark plan), set up Firestore deny-by-default rules, Google sign-in, owner allow-list, HttpOnly Secure cookie, and write the `owner-auth` package with negative tests (forged token 403, non-owner token on /owner 403, client-side flag flip gets nothing).

4. The data model and the Firestore rules, with emulator tests. Write the Firestore data model for Product, Store, Price, Wishlist, Alert; write the deny-by-default rules; run the emulator tests including a cross-tenant read that must fail.

5. The price fetch script for Amazon.eg (first product, offline fixture test). Write a script that fetches the price of a single tracked product from Amazon.eg, stores the result in Firestore, and has an offline fixture test that can run without network.

6. The price fetch script for Noon (first product, offline fixture test). Write a script that fetches the price of a single tracked product from Noon, stores the result in Firestore, and has an offline fixture test that can run without network.

7. The real-discount badge with the rubric. Implement the rubric: given a product's price history, determine if a "discount from X EGP" claim is "real" or "inflated"; display the badge with a one-line explanation; write the unit test for the rubric with Arabic and English eval sets.

8. The wishlist save and unlimited items. Implement the wishlist save (product name, price, store URL), unlimited items, persistence across reloads, and the UI for viewing and managing the wishlist.

9. The price-drop alert and Telegram notification. Implement the alert target price, the one-alert-at-a-time limit, the logic to check the price against the target, and the Telegram notification (dry-run first, then real). Write the test that a price drop below target fires exactly one Telegram alert.

10. The currency auto-detect from visitor locale and IP. Implement the locale/IP detection that shows EGP for Egypt, SAR for KSA, AED for UAE, etc., with a manual override widget on the settings page.

All tasks: after finishing, run the gates (`npm test`, `npm run lint`, `npm run typecheck`), update the project checkpoint, commit to `main` with a clear message. Do not push to `D:\Projects\_SIR` for project-code changes; push the SIR Price Finder repo. Reports go to `D:/Projects/_SIR/ops/agy-runs/reports\<task>.md`.