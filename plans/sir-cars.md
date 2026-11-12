# PLAN: SIR Cars (Wave 9, GLOBAL product, rebuild from zero, small independent project)

## Vision (owner, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` sections 5, 6 and 8)

SIR Cars is its own small independent project with the same premium standard as every other product: everything for a car owner in Egypt, from buying through owning, maintaining, fuelling, licensing, insuring, repairing, comparing and selling. It is not a module of any other product. The old `plans/sir-cars.md` (r51) is superseded by this file; the git history keeps it.

**Version 1.0.0.** Audited and rewritten 2026-11-12 (round r54, HQ). Supersedes the r51 text of this file. The canonical competitor study is `D:/Projects/_SIR/ops/competitors/sir-cars.md` (dated 2026-11-12, with sourcing tasks still open). The first ten build tasks for the free agents are in `D:/Projects/_SIR/ops/briefs/sir-cars-tasks.md`.

**Truth rule for this plan.** Nothing here is called working unless a reviewer saw it today. The product has never been built: `D:\Projects\SIR Cars` does not exist yet, no Firebase project exists for it, and no GitHub repo exists for it. The old r51 note assumed a repo `sirahmed8/sir-cars`; that assumption is unverified and is re-checked in M0. Verified today: this plan and the competitor file were written in this round.

**Product class: GLOBAL.** Anyone in the world can use it, accounts and subscriptions exist, every platform is planned, the owner has an owner-only analytics page, the site is hosted twice (Firebase Hosting and Vercel), and a paid subscription gives the owner every permission inside the product. It is listed in `PRODUCT_DIRECTION_2026-11-12.md` section 8 among the small independent projects created from the unplanned ideas.

---

## 1. Who it is for, and the promise

**For the buyer.** The Egyptian who is about to buy a car, new or used, and wants to know what it is really worth, what it costs to own, and whether the listing is honest. The one-line promise, in the words a buyer would use:

> Know what a car is worth and what it will cost you, before you pay for it.

**For the owner.** The person who already owns a car and loses track of licence dates, insurance renewals, service intervals, fuel spend and workshop bills. The one-line promise for that side:

> Your car reminds you before it becomes a problem, and shows you what it costs.

**For the seller.** The private seller who wants a fair price and a serious buyer, without paying a dealer commission or posting on five sites. The one-line promise for that side:

> List once, reach real buyers, and sell at a fair price.

**The end state we sell.** A visitor opens the app, searches "Kia Sportage 2019", sees the real trim-level price range with its source, the cost-per-kilometre from real owner data, the spec comparison against two other cars, and three verified listings near them with inspection badges. They tap to contact a seller, the seller's phone is hidden until a declared-interest tap with a consent screen. The owner logs in, adds their car once, and from that moment the app tracks fuel, maintenance, licence and insurance dates, and shows the total cost of ownership and the cost per kilometre. A workshop finder shows rated workshops near them with prices, and a parts comparison shows where a part is cheapest. When it is time to sell, the listing is one tap, pre-filled from the car record.

**Not in v1:** no ads, no fake listings, no fake reviews, no invented prices, no invented ratings, no fake users. An empty area shows an empty state with one action (tell us your city and we will tell you when listings arrive there). No odometer fraud tolerance: every listing carries a declared odometer and a report flow.

---

## 2. The ten competitors, and where we win

Full table with sources, dates and the second ring: `D:/Projects/_SIR/ops/competitors/sir-cars.md` (dated 2026-11-12).

| Competitor | What it proves about the market | Our edge |
|---|---|---|
| Hatla2ee (Egypt) | One local brand owns car search intent; trim-level price lists and SEO landing pages are table stakes | Whole car life in one place, owner tracker, verified private sellers, inspection badge |
| OLX Egypt (cars) | Free posting and huge traffic are expected; trust is the gap | Car-specific data model, verified phone, inspection badge, price history from submitted listings |
| Contactcars (Egypt) | Specs and trim data are a real product on their own | Combine research, marketplace and owner tools; same specs data behind estimates |
| Syarah (Saudi, UAE) | Inspection, delivery and a finance calculator sell trust | Egyptian market, Egyptian Arabic, licence and insurance reminders, local workshops and parts |
| CarSwitch (GCC) | Inspection-first trust model with a fixed price works | Egyptian market first, plus the owner side no marketplace covers |
| YallaMotor (MENA) | Specs database plus comparison tool is a real draw | Owner tools as a first-class feature, not an afterthought |
| Motory (Egypt) | Local price lists and model pages matter | One product for the whole car life |
| DubiCars (UAE) | Premium listing UX and a verified dealer badge sell trust | Egyptian market, owner tools, Egyptian Arabic, local payment rails |
| Fuelio (global) | Fuel log with consumption chart and reminders is the retention hook | Combine the best fuel tracker with the whole car life, Arabic first, web plus mobile |
| Drivvo (global) | Expense and maintenance log with cost per km is the owner's number | One product for the whole car life, free core features, local workshops and parts |

**Category truth from the sources (2026-11-12):** the marketplace is split between one big local brand and generic classifieds; trust is the real problem; price data is public but scattered; owner tools are a separate app category; workshops and parts are offline; licence and insurance reminders are a daily pain; Arabic is badly served; nobody owns the whole car life. Our product plan follows that truth instead of fighting it.

---

## 3. Features

### 3.1 Parity with the best in the category (must ship)

| Feature | Why it is in the list | Source of the requirement |
|---|---|---|
| Trim-level price list and price range by model, year and trim | Base expectation for any car buyer | Hatla2ee, Contactcars, Motory |
| Price estimate for a specific car with its source and range | The buyer's first question | Hatla2ee price lists |
| Specs comparison of two or three cars side by side | Research is half the purchase | Contactcars, YallaMotor, Auto-Data.net |
| Used-car listings with photos, trim, year, mileage, city, price | Base expectation for any marketplace | Hatla2ee, OLX Egypt, Syarah |
| Verified phone on every listing | Trust is the gap | Syarah, CarSwitch inspection badge |
| Inspection badge and referral flow | Trust layer wired into the listing | CarSwitch, Syarah |
| Report-a-listing flow on every card | Legal and trust baseline | Shared kit security baseline |
| Fuel log with consumption and cost per kilometre | The retention hook for owners | Fuelio, Drivvo |
| Maintenance log with service intervals and reminders | The owner's second question | Drivvo, AutoCare, MyCar Tracks |
| Licence, insurance and periodic inspection reminders | The daily pain | Fuelio, Drivvo |
| Cost of ownership dashboard (fuel, maintenance, insurance, tax, fees) | The owner's number | Drivvo cost per km |
| Workshop finder with ratings and prices | Offline today, real gap | None found in Egypt |
| Parts price comparison across shops | Offline today, real gap | RockAuto pattern, global |
| Car record: one record per car, reused across listings, fuel, maintenance and reminders | The spine of the whole product | Our design |
| Sell flow pre-filled from the car record | The seller's last step | Our design |
| Web app that works offline (PWA) | The garage has bad signal | Nobody claims it (our gap) |
| Arabic Egyptian first, English second | The clearest local gap | Fuelio and Drivvo are English-first |
| Support assistant grounded in the help source | Cuts support time | Shared kit help-center |
| Data export and one-tap account deletion | Legal and trust baseline | Shared kit security baseline |

### 3.2 The owner's own ideas, carried forward from legacy and TickTick

Every line says where it came from, so nothing gets silently rebuilt thinner than what he already asked for.

| Idea | Source | Status in this plan |
|---|---|---|
| Specs, pros and cons, spare-parts locations, owner opinions | TickTick "oğرت برامج ومشاريع" idea 23 (core/06-portfolio.md SIR Cars row) | Build as the research core of M2 (specs and price) and M4 (workshops and parts) |
| Compare cars in plain words | TickTick idea 23 | M2, AI explains a comparison in plain words, the comparison itself is data |
| Summaries of owner opinions | TickTick idea 23 | M4, AI summarises real submitted reviews only, never invented |
| Find a spare part from a photo | TickTick idea 23 | M5, AI identifies the part and searches the parts catalogue, advisory only |
| Price estimate with the source shown | r51 legacy note | M2, every estimate shows its source and range |
| Maintenance log and reminders | Brief scope (licence, insurance, service) | M3 |
| Fuel and cost tracking | Brief scope | M3 |
| Workshop finder | Brief scope | M4 |
| Parts price comparison | Brief scope | M4 |
| Specs comparison | Brief scope | M2 |

**Explicitly dropped from the legacy note:** the assumption that the product is "planning only" waiting for wave approval; the three-milestone roadmap that stopped at M3; the claim that no code is written until a wave is approved (the owner decided on 2026-11-12 that this is now its own project). Nothing else is dropped: every feature in the r51 note is carried into sections 3.1 and 3.2 above.

### 3.3 Explicitly out of scope for v1

Betting or any money on a car outcome, drone or video inspections, anything that needs a hardware sensor in the car, odometer verification by a third party beyond the declared value and the report flow, and any feature that requires a government data feed we do not have a lawful source for. Those wait for a sourced data agreement.

### 3.4 Lawful data

No scraping of existing marketplaces. All listings are user-submitted. For price benchmarks: public government data (Egyptian customs duty tables, Traffic Authority fee schedules, public press releases) and published price lists on Hatla2ee, Contactcars and Motory, cited with a link and a date, never copied verbatim. Price history is built from submitted listings only. Workshop and parts data is user-submitted and verified by a community report flow. Inspection service integration requires a signed referral agreement. Every data source is listed in `docs/DATA_SOURCES.md` with its licence and its last-checked date.

---

## 4. Platform matrix

Standing rule (owner, 2026-11-12): every product ships on all platforms, so web, Windows, macOS, Linux, Android and iOS are all required for SIR Cars. Wear OS, watchOS, TV and car are not in that list, so they are skipped in v1 with a written reason, not left in silence.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required | The whole product: search, estimate, compare, listings, contact, owner record, fuel, maintenance, reminders, workshops, parts, sell | Nothing pending |
| PWA (installable, offline) | Required | Install from the browser, offline car record, offline fuel and maintenance log, offline licence and insurance reminders, background sync | Native shell if the PWA proves weak on low-end Android |
| Windows | Required (M5) | Installable PWA from day one, then a real NSIS installer with the same Google sign-in and self-update | Signed installer (owner buys the certificate) |
| macOS | Required (M5) | Installable PWA from day one, then an unsigned DMG from the same Electron build | Signed build when the owner has an Apple account |
| Linux | Required (M5) | Installable PWA from day one, then AppImage and .deb from the same Electron build with a .desktop entry | Signed package |
| Android phone and tablet | Required (M4) | Expo app: the same account, car record, fuel, maintenance, reminders, listings, workshops, parts | Play Store when the reinvestment ladder allows |
| iPhone and iPad | Required (M4) | Expo app, same account and data, tablet layouts | App Store or SideStore (needs a paid Apple account, the owner decides) |
| Wear OS | Skipped in v1 | Nothing | A licence and insurance countdown complication, decided with an ADR |
| watchOS | Skipped in v1 | Nothing | Same ADR as Wear OS |
| TV (Android TV and Apple TV) | Skipped in v1 | Nothing | A workshop and parts search screen only if a real workshop asks |
| Car (Android Auto and CarPlay) | Skipped in v1 | Nothing | A fuel and maintenance log voice entry only if a paid tier needs it |
| Widgets and live activities | Part of M5 | Android Glance and iOS WidgetKit: the next reminder and the cost per kilometre | Richer surfaces later |
| Browser extension | Skipped | Nothing | A price checker on Hatla2ee and OLX pages only if users ask |
| Docker and self-host | Skipped | Nothing | Not a product need here |

**Rule:** every platform shares one Firebase project, one account and one dataset. No platform ever carries its own copy of the rules. The Windows, macOS and Linux builds come from one Electron shell and one release feed, so an update reaches all three at once.

---

## 5. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. That file is the shared standards kit every product builds against; SIR Platform was cancelled as a project on 2026-11-12, so there is no extraction target any more. SIR Cars is a GLOBAL product, so it adopts all twenty sections of the kit as internal `packages/*` with the kit names and interfaces, and when it hardens a piece that other products need, that piece goes back into the kit file and HQ queues the adaptation for the others.

### 5.1 Shape

```
apps/web        Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens
apps/api        Route handlers that need secrets and long tasks (webhooks, cron, AI proxy, price estimate)
packages/core   Domain types and zod schemas: Car, Trim, Listing, PriceEstimate, FuelEntry, MaintenanceEntry, Reminder, Workshop, Part, Review, User
packages/data   Firestore repositories, one interface per entity, emulator tests
packages/ui     The shared UI kit from the kit: InputBox, TabBar, BottomSheet, Card, Chip, Modal, Toast
packages/kit    owner-auth, signed-webhook, billing-fallback, ai-proxy, legal-pack, i18n, help-center, notifications
apps/mobile     Expo app for Android and iOS (M4)
apps/desktop    Electron shell for Windows, macOS and Linux (M5)
docs/           Help centre source, legal source, env names, decisions, DATA_SOURCES.md
scripts/        Seed-free checks, emulator tests, Lighthouse, AI evals
```

Layers depend inward only: presentation, domain (no I/O), data, core. Files under 300 lines, no `any`, no god components, absolute imports.

### 5.2 Accounts (`owner-auth`)

- Google sign-in through Firebase Auth on the product's own Firebase project, ID token verified on the server with JWKS.
- Owner and admin rights come from an allow-list (`OWNER_EMAILS`, `OWNER_UIDS`), fail closed. Nothing in the client decides a privilege.
- Session in an HttpOnly, Secure, SameSite=Strict cookie. No tokens in localStorage.
- Rate limits on sign-in, listing creation, contact, uploads, AI calls and price-estimate calls.
- Owner accounts get a second factor offer.
- Test: a forged token gets 403, a client-side flag flip gets nothing, a non-owner token on `/owner` gets 403.

### 5.3 Owner-only analytics page

- Route `/owner`, server-verified owner token, 403 for everyone else.
- Real metrics only, read from aggregates not raw collections: users, listings, contacts, price-estimate calls, AI cost, error rate, workshops, parts, subscriptions, revenue in EGP and the visitor currency.
- A second section for the listing owner role: their listings, contacts received, views, report queue. Each listing owner sees only their own listings, enforced in Firestore rules and re-checked on the server.
- No invented numbers anywhere: an empty metric shows a dash and the reason, never a zero dressed as a fact.

### 5.4 AI with the fallback chain

Chain from `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`: Gemini `flash-lite-latest`, then `flash-latest`, then any Gemini text model, then OpenRouter free models, then other free providers, then the local model on this PC. One Gemini key and one OpenRouter key per product, created on this product's own project, stored only in the ignored env file and the Vercel environment, never printed, never committed.

What AI does in this product, and what it must never do:

| Feature | AI role | Hard rule |
|---|---|---|
| Price estimate explanation | Explain the range and why it moves, in plain words | The estimate itself is computed from real data (trim price lists, submitted listings, customs tables). No AI in the number, only in the sentence |
| Specs comparison explanation | Explain the difference in plain words | The comparison is data; AI only writes the sentence |
| Owner opinion summary | Summarise real submitted reviews | Uses only real submitted reviews, never invented opinions |
| Spare part identification from a photo | Identify the part and search the catalogue | Advisory only, never blocks a real part from being listed |
| Support assistant | Answer from `docs/help/*.md` only | Refuses anything not in the help source, and says so |
| Weekly owner report draft | Draft the summary the Telegram sender sends | Numbers come from the database, the model only writes the sentence |

Free users get 5 AI calls per rolling 24 hours with a visible badge, the owner is unmetered, `AI_ENABLED` is the kill switch, a daily cost cap lives in `config/limits.json`, and every call logs which provider answered (never the content). Arabic and English eval sets exist before the feature ships, and the runner exits non-zero below the threshold.

### 5.5 Data and money

- Firestore with deny-by-default rules, per-user and per-listing-owner claims, emulator tests including a cross-tenant read that must fail.
- A listing is a document with a status, a declared odometer, a price and an expiry. Creating and editing a listing is a Firestore transaction with an idempotency key. Test: 20 parallel creates from one verified phone produce exactly the allowed number of listings and 19 clean rejections.
- Photos are size- and type-checked before upload, stored with signed URLs, auto-deleted 90 days after listing expiry (default, the lawyer may change it).
- A seller's phone number is visible to a buyer only after a declared-interest tap with an explicit consent disclosure screen (PDPL 151/2020).
- Wallet and card payments through Paymob and Fawry in test mode. The webhook is HMAC-SHA256 signed with the timestamp inside the signed body, verification is server-side only, and tampered, replayed, unsigned and wrong-timestamp events are rejected.
- Refunds and cancellation follow one written policy for every listing, published on the listing page before payment.

### 5.6 Hosting and delivery

- **Firebase Hosting** is primary. **Vercel** is the second host, the same repository imported with the Vercel CLI, the same build, the same environment variables on both. Both addresses are curl-checked and written into the project checkpoint.
- Static hosting cannot run route handlers, so every secret, webhook, AI call and price-estimate call lives in the Firebase Functions or the Vercel function side, never in the client bundle. This is the exact defect that killed the legacy apps (`/api/ai/chat`, `/api/ai/tts`, `/api/admin/role` returned 404 in production because the apps were exported as static).
- A service worker caches the car record, the next reminder and the listing list. Background sync sends the queued actions when the connection returns.
- Daily Firestore export to a private bucket, a monthly restore test, a health endpoint at `/api/health`, a status JSON, a nightly error digest and a weekly Telegram report at a round hour.

### 5.7 Security baseline

Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI. A CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent, with Reject All as prominent as Accept. One-tap data export and one-tap deletion. Rate limits on auth, listing, contact, uploads, AI, price-estimate and webhook endpoints. No fake data in any path a user can see. Phone verification by OTP before a listing is published.

---

## 6. Premium quality bar

This is the floor from `D:/Projects/_SIR/standard/23-premium-code-bar.md` and `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`, written for this product.

**Motion, Apple level.**
- One shared spring config across the app: stiffness 300 to 400, damping 28 to 30, transform and opacity only, no layout thrashing, 120 Hz safe.
- Every sheet, drawer, modal and panel opens and closes with the same spring. An open-only animation is a defect.
- The price estimate reveal and the specs comparison settle with a spring; the cost-of-ownership chart animates on first view. Micro-interactions 100 to 150 ms, standard 200 to 300 ms, large 300 to 500 ms. Press scale 0.98. Reduced-motion path for every animation.
- The active tab shows its label and the others show an icon only, the active tab scrolls into view on load and on change, and the bottom bar never vanishes when the keyboard opens.
- Skeletons match the final geometry, optimistic feedback lands under 100 ms, and no white flash on theme change.

**Two languages, one layout.**
- Egyptian Arabic first for buyers, owners and sellers, English second for the international market, MSA only in legal pages. Both shipped together, never one as a partial translation.
- RTL designed first: logical CSS properties only, flipped directional icons, Arabic line heights, never a mirrored afterthought.
- Every text input detects Arabic or Latin per character as the user types and moves the caret and the direction live. Every mixed run is isolated with `<bdi>` or `unicode-bidi: isolate`. The words "RTL" and "LTR" never appear to the user.
- Currency auto-detected from the visitor locale and IP, with a manual override on top. Dates and times formatted with `Intl`.

**Five states on every screen.**
Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake listing, a fake car, a fake review or a fake number.

**Accessibility.**
WCAG 2.2 AA. Every control has an accessible name. Touch targets at least 44 px with no covered hit area. Full keyboard path on every screen, visible focus, zoom from 80 to 200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured, and a colour pair that passes contrast in light, dark, system and high-contrast themes.

**The look.**
One design system: tokens for colour, spacing on a 4 and 8 px grid, radii, shadows, type and motion. Seed colour a calm automotive slate-blue `#1D4ED8` for a car product, neutral canvas, accent only for primary actions and key numbers. No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. One component per control, never two. Arabic screen face: IBM Plex Sans Arabic, Cairo or Tajawal.

**Native app feel.**
The browser's text selection and the right-click menu are disabled site-wide and replaced by the app's own menu with in-app actions and a refresh. Normal select, copy and paste inside real input fields still work.

**Evidence before the word done.**
Screenshots at 320, 390, 768, 1280 and 1920 px, in Arabic and English, in light and dark, plus 3840 px once. Playwright on the critical journeys. Lighthouse mobile 90 or better. A click-target audit in CI. The self-audit loop runs until two clean cycles.

---

## 7. Free tier and fair pricing (EGP and USD)

These are **test prices**, not published prices. They are the outline the owner confirms with three real car owners and the official gateway fee schedule before anything is charged. The USD column uses 48 EGP per 1 USD, which is "(unsourced, verify)" and is recomputed from the live rate on the pricing page.

| Plan | Who | EGP | USD | What it includes | Rule |
|---|---|---|---|---|---|
| Buyer Free | Any visitor | 0 | 0 | Search, price estimate, specs comparison, browse listings, contact one seller per day, fuel and maintenance log for one car, licence and insurance reminders, workshop finder browse | The core actions are never behind a plan |
| Buyer Pro | Serious buyers and owners | 99 per month (test) | about 2.10 per month | Unlimited contacts, price history and trends, cost-of-ownership dashboard, multi-car record, parts price comparison, priority support | Cancel any time, the plan lapses at the end of the paid month |
| Seller Free | A private seller | 0 | 0 | List up to 3 cars per 30 days, photos, basic stats, contact management | A private seller is never charged to list |
| Seller Pro | A frequent seller or small dealer | 299 per month or 2,990 per year (test) | about 6.20 per month or about 62 per year | Unlimited listings, featured placement, WhatsApp lead badge, lead analytics, bulk upload, inspection referral priority | One fee only: the plan replaces any per-listing fee; the transaction fee is the published gateway cost |
| Workshop Partner | A workshop or parts shop | price set with the owner | | Listed workshop page, price list, booking requests, verified badge | Later milestone, decided with the first real workshop |

**Fairness rules written into the product.**
1. A buyer never pays to see a price estimate or a spec comparison.
2. A private seller never pays to list. A dealer pays one subscription, never a per-listing fee hidden in a small line.
3. Every price on screen is in the visitor's currency, auto-detected, with the original EGP amount next to it.
4. A listing deposit is refunded in full when the seller cancels. A buyer cancellation inside the published window is refunded minus what the seller already lost, and the rule is on the listing page before payment.
5. No ads, in any tier, ever. The owner sets an ad spend cap of 0 until he changes it.
6. The owner of the product gets every paid feature, free, and a subscription grants him all permissions inside the owner console.

**Still open and blocking publication:** the official Paymob and Fawry fee schedules for Egypt, the tax and invoicing treatment of seller fees in Egypt, the exact cancellation and refund wording, the customs duty table source, the Traffic Authority fee schedule, and the lawyer review of every legal page. Each is tagged "(unsourced, verify)" in `ops/competitors/sir-cars.md` section 4 and in `docs/ENV.md` when the project starts.

---

## 8. Milestones M0 to M6, with acceptance tests

Every exit check is something a reviewer can run or click. "Green" means the output was seen, not assumed.

### M0: Foundations, the kit and the honest map of the market

Work: verify whether a Firebase project and a GitHub repo named `sir-cars` already exist; if not, create the Firebase project `sir-cars` on the free Spark plan and the GitHub repo `sirahmed8/sir-cars` (private) as the only remote; scaffold the monorepo (apps, packages, docs, scripts) with strict TypeScript, Tailwind v4 tokens, RTL-first styles and the shared `verify` script; design the token set and three design directions; recreate the Desktop folder kit from scratch for the new build; write `docs/DATA_SOURCES.md`.

Exit checks:
1. `D:/Projects/SIR Cars` contains `folder.ico` (named exactly that, never `icon.ico`) and the Desktop folder `SIR Projects/SIR Cars` holds `folder.ico`, `SIR Cars.lnk`, `Start SIR Cars dev.lnk`, `Stop SIR Cars dev.lnk`, `Open project folder.lnk` and `Versions.txt` reading version 1.0.0 and a plain status. The old kit belonged to no previous build, so M0 creates it.
2. `pnpm verify` runs typecheck, lint, tests, build and gitleaks, and the output was seen green.
3. The Firebase project `sir-cars` exists and the GitHub repo `sirahmed8/sir-cars` is the only remote for it.
4. `docs/DESIGN.md` holds three explored directions with screenshots and the chosen one, plus the token file.
5. `docs/DATA_SOURCES.md` lists every data source with its licence and its last-checked date, and every price estimate cites one of them.

### M1: Research core, proven under real data

Work: the data model and the Firestore rules for Car, Trim, PriceEstimate, Specs; the price-estimate engine reading trim price lists and submitted listings; the specs comparison view; the search and filter for cars by make, model, year, trim and city; five states everywhere.

Exit checks:
1. The emulator rules tests pass, including a cross-tenant read that must fail.
2. A price estimate for a known trim returns a range and a source, and the source is shown on screen.
3. The specs comparison of two cars shows the differences highlighted, at 390 px and 1280 px, in Arabic and English, light and dark.
4. The search and filter show idle, loading, empty with one action, error with retry and populated, at 390 px and 1280 px, in Arabic and English, light and dark.

### M2: Marketplace core, proven under contention

Work: the listing model and the Firestore rules; the listing creation flow with photos, trim, year, mileage, city, price; phone verification by OTP; the listing page with the inspection badge and the report flow; the contact flow with the consent disclosure screen; the price history built only from submitted listings.

Exit checks:
1. A listing cannot be published without phone verification, and the e2e test tries to publish without it and is blocked.
2. A photo upload is refused when it is the wrong type or too large, and a stored photo is reachable only with a valid signed URL.
3. 20 parallel listing-creates from one verified phone produce exactly the allowed number of listings and clean rejections.
4. The buyer's phone is hidden until a declared-interest tap, and the consent screen is shown before the seller's phone is revealed.
5. The price history for a trim shows only submitted listings, with their dates, never an invented point.

### M3: Owner core, security, billing, legal, and the owner page

Work: the car record; the fuel log; the maintenance log with service intervals; the licence, insurance and periodic inspection reminders; the cost-of-ownership dashboard; the signed webhook with negative tests; the billing fallback page with lead capture; the legal pack; the owner-only analytics page.

Exit checks:
1. Ten negative webhook tests pass (tampered, replayed, unsigned, wrong timestamp, wrong amount, and the rest), and no `dev_signature` or any other bypass exists in the code.
2. A non-owner token on `/owner` gets 403 and a forged token gets 403.
3. The pricing page shows the test prices with the currency auto-detected, plus "Subscriptions launching soon" and an email capture that creates a lead document and rejects an invalid address.
4. Every legal page exists under `/legal/*`, each marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch".
5. Both hosts answer: the Firebase URL and the Vercel URL were curl-checked, and the two addresses are written in the project checkpoint.
6. A reminder fires at a round hour, sends through the Telegram sender, and the owner's weekly report arrives with the numbers and their meaning.

### M4: Workshops, parts, community and the two platforms

Work: the workshop finder with ratings and prices; the parts price comparison across shops; the review and rating system for workshops and listings; the AI opinion summary; the Expo app for Android and iOS; the Telegram notifications and the scheduled reminders.

Exit checks:
1. The workshop finder shows real workshops from submitted data, and an empty area shows an empty state with one action.
2. A part search returns prices from more than one shop, sorted, with the source of each price.
3. The review system refuses a review from a user who has not used the workshop, and a review is editable by its author only.
4. The Android APK builds and installs on a device, and the same Google account sees the same car record on the web app.

### M5: AI, the Windows app and the quality pass

Work: the spare-part identification from a photo; the price estimate explanation; the specs comparison explanation; the support assistant; the Windows installer with the same sign-in and self-update; the macOS and Linux builds; the widget and live activity surfaces; the full self-audit.

Exit checks:
1. `npm run eval:estimate` and `npm run eval:support` pass with Arabic and English sets, and the support assistant refuses an ungrounded question.
2. The Windows installer installs, starts, signs in with the same Google account, updates itself, and its entry is in `Projects-Hub.html` and on the Download page with the version and the size.
3. Screenshots exist at 320, 390, 768, 1280 and 1920 px in both languages and in light, dark and high contrast, with the five states visible.
4. The accessibility audit passes WCAG 2.2 AA with an accessible name on every control, no covered hit area, and no horizontal scroll from 320 px.
5. Lighthouse mobile is 90 or better and the JSON is saved in `.sir/evidence/`.

### M6: Release, real listings and the legacy handover

Work: the launch package (domain, accounts, legal review); the old hosts redirected with 301; the keys rotated; the first real listings onboarded with written consent; the first real workshops onboarded with written consent.

Exit checks:
1. Three real listings are live with a written consent, a real price and a real seller, and no seeded or invented listing exists in any path a user can see.
2. Three real workshops are live with a written consent, a real price list and a real owner.
3. The 301 redirects from any old hosts are verified by curl.
4. The legacy keys are rotated and the service-account file is out of the repository.
5. The lawyer has reviewed the legal pages and the tax question is answered, and only then can a paid plan go live.

---

## 9. The first ten tasks for the free agents

Ready to queue, each with its own brief: `D:/Projects/_SIR/ops/briefs/sir-cars-tasks.md`.

1. Monorepo scaffold with tokens, RTL, the health route and CI.
2. The product's own Firebase project and the `owner-auth` package with negative tests.
3. The data model and the Firestore rules, with emulator tests.
4. The price-estimate engine with a cited source and range.
5. The specs comparison view with highlight of differences.
6. The listing creation flow with photos and phone verification.
7. The listing page, the contact flow and the consent disclosure screen.
8. The car record, the fuel log and the maintenance log.
9. The licence, insurance and service reminders with the cost-of-ownership dashboard.
10. The owner-only analytics page and the billing fallback page.

---

## 10. Skills from the library that this build uses

Picked from `D:/Projects/_SIR/ops/SKILLS_INDEX.md` and the digests in `D:/Projects/_SIR/ops/encyclopedia/`. Digests live under `ops/encyclopedia/<tool>/<skill>.md`; the paths below are the real files found on 2026-11-12.

**Design and UI**
- `anti-vibecoded-design-system` (claude) - keeps the car product away from generic AI styling and purple gradients.
- `taste-design-engine` (claude) - the self-audit against AI patterns before the screens ship.
- `emil-motion-impeccable` (claude) - the spring physics for the sheets, the tab bar and the estimate reveal.
- `modern-ui-ux-design-system` (claude) - tokens, micro-interactions and hierarchy for one design system.
- `cognitive-product-intuition` (claude) - the listing and contact flow step order and the empty states.
- `high-conversion-copywriting` (claude) - the promise line and the listing copy that sell the end state without hype.
- `commercial-app-blueprint` (claude) - llms.txt, the trust signals and the sticky call to action on the site.
- `a11y-debugging` (codex) - the accessibility audit with Chrome DevTools against WCAG 2.2 AA.
- `mobile-ergonomics-polish` (claude) - touch targets, no horizontal scroll, tap feedback on the phone screens.
- `modern-web-guidance` (claude) - the current web APIs, container queries and dialog behaviour, run before any client-side work.
- `react-best-practices` (claude) and `nextjs` (claude) - App Router structure, Server Components, rendering and performance rules.

**Security and legal**
- `firestore_rules_creation` (claude) - the deny-by-default rules for every collection.
- `firebase_security_rules_auditor` (claude) - the audit that finds a cross-tenant read before a user does.
- `zero-trust-security-hardening` (claude) - server-side role checks, secure cookies and rate limiting.
- `owasp-vulnerability-shield` (claude) - the OWASP pass over uploads, webhooks, contact flow and auth.
- `vibe-auth-hardening` (claude) - the five auth flaws that a fast build introduces.
- `legal-compliance-shield` (claude) - the legal pack that matches what is actually collected, including PDPL 151/2020.
- `cookie-debugging` (codex) - the consent banner behaviour and the cookie audit.

**Mobile and desktop**
- `modern-app-engineering` (claude) - the shared architecture for the Expo app and the Electron shell.
- `android-cli` (claude) and `device-hub` (codex) - the Android build, the emulator and the device checks.

**AI**
- `gemini-api-dev` (codex) - the Gemini calls and the structured output.
- `ai-gateway` (codex) and `omniroute-resilience-gateway` (claude) - the fallback chain and the failover on quota errors.
- `firebase_ai_logic_basics` (claude) - Firebase AI Logic when it becomes cheaper than a direct call.

**Automation and operations**
- `chat-sdk` (codex) - the Telegram bot for reminders and the weekly report.
- `webhook-testing` (deep) - capturing, replaying and validating the gateway webhooks.
- `verification` (codex) and `verification-before-completion` (deep) - the end-to-end check before the word done.

**Data, hosting and growth**
- `firebase_firestore` (claude) - queries, indexes and the data model.
- `database-reliability-transactions` (claude) - the atomic listing creation and idempotency keys.
- `firebase_hosting_basics` (claude), `vercel-cli` (codex), `deployments-cicd` (codex) and `env-vars` (codex) - the two hosts with the same build and the same variables.
- `google_maps_platform` (codex) - the workshop finder map, the geocoding and the distance search.
- `open-seo-auditor` (claude) - Arabic search visibility, JSON-LD and the AI answer check.
- `system-design-architect` (claude) and `production-engineering-standards` (claude) - the zero-mock persistence and the production bar.

---

## 11. Risks and the defaults we take

- **Two-sided cold start on the marketplace.** Default: one city (Cairo) with 20 real listings and real sellers before any advertising or search push. No marketing before the sourcing tasks in the competitor file are done.
- **Receipt and odometer fraud.** Default: declared odometer on every listing, report-a-listing on every card, no auto-approval of anything, phone visible to the buyer only after a declared-interest tap.
- **Price data that goes stale.** Default: every price estimate shows its source and its last-checked date; a stale source is flagged, never silently used.
- **The real market already has a big brand.** Hatla2ee owns car search intent. Default: win on the whole car life, the owner tracker, Egyptian Arabic and trust, not on features we cannot verify.
- **Payments before the lawyer.** Default: test mode only, no real charge, no published plan price until the fee schedule and the legal pages are reviewed.
- **Gateway, customs and Traffic Authority numbers.** Default: every one of them is "(unsourced, verify)" until read on the official page on the day it is used.
- **Static export killing the server.** Default: no secret ever in a route handler that a static host would drop; the server features run on the functions side from M1.

---

## 12. Only the owner can do

Buy the domain and point it at both hosts. Create and fund the Paymob and Fawry business accounts and paste the keys into the project's ignored env file. Sign in once on the Google OAuth screen so the branding is right. Talk to three real car sellers and three real workshops, or approve the outreach text. Lawyer and accountant. Buy the code-signing certificate later. Create the Play Console and Apple developer accounts when the reinvestment ladder allows.

Everything else is an agent's job.

---

## 13. Sources and files

- Canonical competitor study with dated links: `D:/Projects/_SIR/ops/competitors/sir-cars.md`
- The ten build briefs: `D:/Projects/_SIR/ops/briefs/sir-cars-tasks.md`
- Shared kit: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`
- AI chain: `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`
- Quality charter: `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`
- Desktop and Windows standard: `D:/Projects/_SIR/plans/WINDOWS_APP_STANDARD.md`
- Legacy source and notes: `D:/Projects/_SIR/plans/sir-cars.md` (r51, superseded) and TickTick "oğرت برامج ومشاريع" idea 23
- Owner ideas: `D:/Projects/_SIR/ops/TICKTICK_MAP.md` and `plans/PROJECT_MERGE_RECORD.md`