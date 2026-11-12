# PLAN: SIR Handyman (small independent GLOBAL product, rebuild from zero)

## Vision (owner, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` sections 5, 6 and 8)

SIR Handyman is its own small independent project with the same premium standard as every other product: on-demand home services in Egypt, Uber for craftsmen. The customer posts a request with photos and location, nearby verified workers accept or send a quote, the price is agreed before the visit, the visit is tracked live, the work is paid after it is done, and both sides rate the completed job. It is not a module of SIR Hagoozat (decided 2026-11-12, `BACKLOG_IDEAS_DECISIONS.md` section 3.5): the supply side is individual craftsmen with their own days, tools and quotes, so the entities, the economics and the legal duties are not a court slot. The old `plans/sir-handyman.md` (r51, thin first draft) is superseded by this file; the git history keeps it.

**Version 1.0.0.** Rewritten 2026-11-12 (round r54, HQ). The canonical competitor study is `D:/Projects/_SIR/ops/competitors/sir-handyman.md` (dated 2026-11-12, with sourcing tasks still open). The first ten build tasks for the free agents are in `D:/Projects/_SIR/ops/briefs/sir-handyman-tasks.md`.

**Truth rule for this plan.** Nothing here is called working unless a reviewer saw it today. The product has never been built: `D:\Projects\SIR Handyman` does not exist yet, no Firebase project exists for it, and no GitHub repo exists for it. Verified today (2026-11-12): this plan, the competitor file and the tasks file were written in this round; nothing else exists.

**Product class: GLOBAL.** Anyone in the world can use it once the two-sided model is proven in Egypt; accounts and subscriptions exist; every platform is planned; the owner has an owner-only analytics page; the site is hosted twice (Firebase Hosting and Vercel). It is listed in `PRODUCT_DIRECTION_2026-11-12.md` section 8 among the small independent projects created from the unplanned ideas (idea 28).

---

## 1. Who it is for, and the promise

**For the homeowner.** The Egyptian家庭 head who discovers a leak at 10pm, or needs the AC serviced before summer, and does not know which craftsman to trust, what a fair price is, or whether the person who arrives is safe. The one-line promise, in the words a homeowner would use:

> Describe the job with photos, agree the price, and watch the worker come to you.

**For the worker (craftsman).** The plumber, electrician, carpenter, painter or AC technician who loses half his week to phone calls that go nowhere, undercutting apps that take a hidden cut, and no-show customers. The one-line promise for that side:

> Real jobs near you, an agreed price, paid after you finish.

**For the building or property manager (later).** A landlord or compound manager who needs a vetted vendor pool for recurring maintenance across many units. The one-line promise for that side:

> One dashboard for every unit's maintenance, with verified workers and an audit trail.

**The end state we sell.** A visitor opens the app, taps "AC is not cooling", describes the problem in one line and attaches two photos, drops a pin or uses GPS, and picks a time window. Within minutes, verified AC technicians nearby send quotes. The homeowner compares quotes side by side (price, worker rating, jobs completed, distance), accepts one, sees the worker's name, photo and rating, shares the visit with a trusted contact, tracks the worker en route with a live ETA, and confirms arrival with a 4-digit visit code. The worker does the job, the homeowner confirms completion, the agreed price is charged through the app (or in test mode until launch), and both sides rate the completed job. The owner logs in at `/owner` and sees real metrics: requests per day, quotes per request, time-to-accept, completion rate, dispute rate, revenue from service fees, worker funnel, AI cost and error rate.

**Not in v1:** no ads, no fake workers, no fake ratings, no invented prices, no invented availability. An empty area shows an empty state with one action (tell us your city and we will tell you when workers arrive there). No worker is dispatched without identity verification. No job is paid before completion is confirmed by the homeowner (or auto-released after the dispute window closes).

---

## 2. The ten competitors, and where we win

Full table with sources, dates and the second ring: `D:/Projects/_SIR/ops/competitors/sir-handyman.md` (dated 2026-11-12).

| Competitor | What it proves about the market | Our edge |
|---|---|---|
| FilKhedma (Egypt) | A real app-first Egyptian home services product exists with a 1-month maintenance guarantee and B2B lane | Agreed price before work, worker identity shown, live tracking, chat, ratings on completed jobs, free for homeowners |
| Khidhma (Egypt) | Fixed online prices and booking on the web work today (EGP 99 cleaning, EGP 150 plumber, their prices) | Quote-then-agree for open-ended jobs, broader coverage, live tracking, worker ID, honest numbers |
| Mahlola (Egypt) | Home and commercial HVAC positioning for Egypt | Full request-quote-visit loop in one product, Egyptian Arabic first |
| Mu'een (Egypt, Giza) | 25+ categories and a live app on both stores prove demand in Giza/Cairo | Agreed price, wider hours, Egyptian Arabic, ratings tied to completed jobs |
| YalaFix (Egypt) | Membership EGP 299/month with priority and discounts is a real (paywalled) model | Free for homeowners, no paywall on any core action, transparent quotes |
| Taskty (Egypt) | An Arabic-first Play Store home services market proves store presence matters | Same store presence, plus tracking, chat, ID verification and ratings |
| Fixawy (Egypt) | Vetted-pro interviews and safety tests are a proven trust story in Egypt | Safety-test onboarding as a core trust badge, revived for the current market |
| SAADK (Egypt) | "Compare offers from approved companies" is a real App Store proposition | Compare offers from individual verified craftsmen and companies, Egyptian Arabic |
| ServiceMarket (UAE) | A 150k-customer (their claim) aggregator with AMC contracts works in the Gulf | Egypt-first, own verified network, agreed price, no partner-handoff surprises |
| Urban Company (India, UAE/KSA via noon) | A trained-network model at scale works globally | Egypt-first market, local rails (Paymob, Fawry), fair worker take rate, Egyptian Arabic |

**Category truth from the sources (2026-11-12):** the Egyptian market is active but nobody combines an agreed price before the visit, live tracking, worker identity, chat and ratings tied to completed jobs in one RTL Egyptian-Arabic product; web-first Egyptian competitors still have an app gap; guarantees are the only trust instrument in real use; the Gulf aggregator model proves breadth works but not at Egyptian price points; Urban Company proves the trained-network model but has not entered Egypt. Our product plan follows that truth instead of fighting it.

---

## 3. Features

### 3.1 Parity with the best in the category (must ship)

| Feature | Why it is in the list | Source of the requirement |
|---|---|---|
| Service catalog (plumbing, electricity, carpentry, painting, AC, cleaning, pest control, appliances, aluminium/alumetal, gas water heaters, moving) | Base expectation; FilKhedma and Mu'een cover 20+ categories | FilKhedma, Mu'een, YalaFix, Khidhma |
| Request with photos, description and GPS/pin location | Core of the model; Mu'een and FilKhedma flow this way | Mu'een, FilKhedma |
| Fixed-price menu for known jobs (cleaning, AC service) and free quotes for open-ended jobs | Khidhma proves fixed prices convert; open-ended needs quotes | Khidhma, Thumbtack |
| Nearby verified workers see the request and quote or accept | Core of the model | TaskRabbit, FilKhedma |
| Worker profile: photo, name, verified badge, rating, jobs completed, distance, response time | Trust layer; every serious competitor shows it | All ten |
| Agreed price locked in the booking before the visit | The differentiator; nobody in Egypt does it transparently | Our design (Thumbtack quotes, closest global analog) |
| Live en-route map with ETA for the worker visit | Mu'een claims real-time tracking; not demonstrably shipped in Egypt | Mu'een (claim), Uber pattern |
| 4-digit visit code on arrival, confirmed by the homeowner | Safety for home entry; nobody in Egypt has it | Our design |
| In-app chat (text + photos) tied to the booking | Base expectation; ServiceMarket and Urban Company have it | ServiceMarket, Urban Company |
| Rating after completion, one rating per booking, no rating without a completed job | Trust baseline; fake reviews are rampant | Shared kit security baseline |
| Push and Telegram notifications: quote received, quote accepted, worker en route, arrived, completed, reminder | Retention and safety | Shared kit notifications |
| Dispute flow: report a problem, freeze the payment, owner-arbitrated | Needed for home entry trust; nobody ships it in Egypt | Our design |
| Data export and one-tap account deletion | Legal and trust baseline | Shared kit security baseline |
| Arabic Egyptian first, English second, RTL designed first | The clearest local gap | OWNER_DEFAULTS items 15 and 16 |
| Web app that works offline (PWA) | Install gap of Egyptian web-first competitors | Khidhma "app coming soon" |
| Support assistant grounded in the help source | Cuts support time | Shared kit help-center |
| 1-month maintenance guarantee on eligible jobs, tied to the completed booking | FilKhedma proves guarantees differentiate in Egypt | FilKhedma |

### 3.2 The owner's own ideas, carried forward from legacy and TickTick

Every line says where it came from, so nothing gets silently rebuilt thinner than what he already asked for.

| Idea | Source | Status in this plan |
|---|---|---|
| On-demand home services, nearest worker accepts, live tracking, rating, payment later | TickTick "أفكار برامج ومشاريع" idea 28 (mapped in `ops/TICKTICK_MAP.md`), r51 legacy note `plans/sir-handyman.md` | M2 (request/quote/accept), M3 (tracking, payment), M4 (mobile) |
| Photos with the request | Brief scope (r54) | M2 |
| Price quote and agreed price | Brief scope (r54) | M2 |
| Worker verification and safety | Brief scope (r54) | M2 (ID flag), M3 (visit code), safety playbook |
| In-app chat | Brief scope (r54) | M3 |
| Live tracking | Brief scope (r54) | M3 |
| Two apps in one codebase (customer, worker) plus owner dashboard | Brief scope (r54) | M2 onward (role-based, one repo) |
| Absorption of the booking-type ideas Hagoozat decided to leave out | `BACKLOG_IDEAS_DECISIONS.md` section 3.5; `sir-hagoozat.md` section 3.4 | The request-quote-visit model; Hagoozat keeps slot-bound bookings (match add-ons, venue services). SIR Handyman imports the shared slot/kit pieces only where they fit (notifications, wallet, chat), never the pitch data model |
| Safety tests for gas/electrical work before dispatch | Fixawy's historic model (Cairo360 2017) | M2 worker onboarding: safety questionnaire + skill QA per category |
| Request tracking stepper (describe, location, schedule, done) | Mu'een's own flow | M2 UX |
| Membership household plan (optional, later) | YalaFix EGP 299/month | M6 optional, never blocks core, price set with the owner |
| Annual maintenance contract (AMC) for compounds and landlords | ServiceMarket AMC | M6 B2B lane, written agreements only |
| Compare offers before choosing | SAADK | M2 quote comparison screen |

**Explicitly dropped from the r51 note:** "planning only, build starts when Ahmed decides the wave order" (the owner decided on 2026-11-12 this is its own project), the three-milestone roadmap that stopped at M3 (now M0 to M6), and the claim that the market is "proven by Taskday, Khidmeh, Handyman.com.eg" (those names are stale; the real field is in the competitor file). Nothing else is dropped: the r51 scope (plumbing, electrician, carpenter, painter, AC technician, cleaner and more, request with photos and location, nearest worker accepts, live tracking, quote and agreed price, chat, ratings, verification, later payments) is fully carried into sections 3.1 and 3.2 above.

### 3.3 Explicitly out of scope for v1

Beauty/salon-at-home (Urban Company's lane, not ours), moving and freight (Mahlola's lane, a separate vertical if ever), healthcare at home, vehicle repair (Khidhma bundles it; we do not), insurance claims processing, and any government-data feed we do not have a lawful source for. Emergency 24/7 dispatch is a toggle per city, launched only when worker density supports it.

### 3.4 Lawful data

No scraping of competitor apps, listings, reviews or catalogs. All service categories are our own taxonomy. Worker verification uses a third-party KYC provider (Egyptian eKYC vendors are researched in M0; never stored raw by us, only a pass/fail flag and a provider reference). Job photos live in R2/Storage with signed URLs and are deleted 90 days after completion. The homeowner's address is shared with the worker only after an accepted quote; it is deleted from the active store after the retention window (1 year default). PDPL 151/2020 applies end to end. Payments are Paymob/Fawry in test mode until the merchant account and the legal pack exist. Every source is listed in `docs/DATA_SOURCES.md` with its licence and last-checked date.

---

## 4. Platform matrix

Standing rule (owner, 2026-11-12): every product ships on all platforms. Web, Windows, macOS, Linux, Android and iOS are all required for SIR Handyman. Wear OS, watchOS, TV and car are not in that list, so they are skipped in v1 with a written reason, not left in silence. Two role-based apps (customer and worker) ship from one codebase; the owner dashboard is a route inside the same web app.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required | The whole product: request with photos, quote comparison, booking, chat, visit tracking, ratings, worker cabinet, /owner | Nothing pending |
| PWA (installable, offline) | Required | Install from browser, offline request drafts, offline job history, background sync of queued messages | Native shell if PWA proves weak on low-end Android |
| Windows | Required (M5) | Installable PWA from day one, then NSIS installer with the same Google sign-in and self-update | Signed installer (owner buys the certificate) |
| macOS | Required (M5) | Installable PWA from day one, then unsigned DMG from the same Electron build | Signed build when the owner has an Apple account |
| Linux | Required (M5) | Installable PWA from day one, then AppImage and .deb from the same Electron build with a .desktop entry | Signed package |
| Android phone and tablet | Required (M4) | Expo app: same account, customer flow and worker flow by role, GPS en-route, camera for photos, visit code | Play Store when the reinvestment ladder allows |
| iPhone and iPad | Required (M4) | Expo app, same account and data, tablet layouts | App Store or SideStore (paid Apple account, the owner decides) |
| Wear OS | Skipped in v1 | Nothing | Arrival-notification complication only if workers ask |
| watchOS | Skipped in v1 | Nothing | Same ADR as Wear OS |
| TV (Android TV and Apple TV) | Skipped in v1 | Nothing | No use case; a worker never uses a TV to accept a job |
| Car (Android Auto and CarPlay) | Skipped in v1 | Nothing | Turn-by-turn en-route is a phone job; no car surface in v1 |
| Widgets and live activities | Part of M5 | Android Glance and iOS WidgetKit: next visit countdown and en-route ETA | Richer surfaces later |
| Browser extension | Skipped | Nothing | No counterpart surface; skipped by design |
| Docker and self-host | Skipped | Nothing | Not a product need here |

**Rule:** every platform shares one Firebase project, one account and one dataset. No platform ever carries its own copy of the rules. The Windows, macOS and Linux builds come from one Electron shell and one release feed, so an update reaches all three at once.

---

## 5. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. That file is the shared standards kit every product builds against; SIR Platform was cancelled as a project on 2026-11-12. SIR Handyman is a GLOBAL product, so it adopts all twenty sections of the kit as internal `packages/*` with the kit names and interfaces; when it hardens a piece that other products need, that piece goes back into the kit file and HQ queues the adaptation for the others.

### 5.1 Shape

```
apps/web        Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens
                Routes: / (customer), /worker (worker cabinet), /owner (owner console)
apps/api        Route handlers that need secrets and long tasks (webhooks, cron, AI proxy, geo queries, payouts)
packages/core   Domain types and zod schemas (see 5.3)
packages/data   Firestore repositories, one interface per entity, emulator tests
packages/ui     The shared UI kit from the kit: InputBox, TabBar, BottomSheet, Card, Chip, Modal, Toast
packages/kit    owner-auth, signed-webhook, billing-fallback, ai-proxy, legal-pack, i18n, help-center, notifications, wallet
apps/mobile     Expo app for Android and iOS (M4), role-based (customer / worker)
apps/desktop    Electron shell for Windows, macOS and Linux (M5)
docs/           Help centre source, legal source, env names, decisions, DATA_SOURCES.md
scripts/        Seed-free checks, emulator tests, Lighthouse, AI evals, KYC sandbox checks
```

Layers depend inward only: presentation, domain (no I/O), data, core. Files under 300 lines, no `any`, no god components, absolute imports. Two apps in one codebase means one `apps/web` with route groups `(customer)` and `(worker)` plus a shared component layer, not two repos.

### 5.2 Accounts (`owner-auth`)

- Google sign-in through Firebase Auth on the product's own Firebase project, ID token verified on the server with JWKS. Phone OTP as a second factor for workers (Firebase Auth phone provider, test numbers in emulator).
- Owner and admin rights come from an allow-list (`OWNER_EMAILS`, `OWNER_UIDS`), fail closed. Nothing in the client decides a privilege.
- Session in an HttpOnly, Secure, SameSite=Strict cookie. No tokens in localStorage.
- Rate limits on sign-in, OTP sends, request creation, quote submission, uploads, AI calls, chat messages and webhooks.
- Owner accounts get a second factor offer; worker accounts must complete phone OTP before the first accepted job.
- Test: a forged token gets 403, a client-side flag flip gets nothing, a non-owner token on `/owner` gets 403, a non-worker token on `/worker` gets 403.

### 5.3 Data model (`packages/core`)

| Entity | Key fields | Notes |
|---|---|---|
| User | uid, role (customer / worker / owner), displayName, phone (verified), createdAt | One auth identity, role claims in custom token |
| WorkerProfile | uid, categories[], hourlyRate?, travelRadiusKm, bio, photoURL, status (applied / in_review / verified / suspended), serviceArea (geo hash), workerScore | Status transitions are server-side only |
| WorkerVerification | workerUid, provider, providerRef, result (pass / fail), checkedAt, categoryApprovals (per category: pass / fail) | Pass/fail flag only, never a document image; providerRef for audit |
| ServiceCategory | id, slug (ar/en), parentId?, safetyTier (standard / gas_electrical), active | Own taxonomy, ours alone |
| JobRequest | id, customerUid, categoryId, description, photos[] (storage paths), location (geo, not street until accepted), address, timeWindow, status (open / quoted / accepted / en_route / arrived / in_progress / completed / disputed / cancelled), createdAt | Location (lat/lng or area) visible to workers before accept; full street address visible only after accepted |
| Quote | id, requestId, workerUid, amountEgp, etaMinutes, note, status (pending / accepted / rejected / withdrawn), createdAt | Unique (requestId, workerUid); one accepted quote per request via transaction |
| Booking | id, requestId, quoteId, customerUid, workerUid, agreedAmountEgp, status, idempotencyKey, visitCode (4-digit, hashed), enRouteAt, arrivedAt, completedAt, disputeDeadline | Created in a Firestore transaction from the accepted quote |
| JobMessage | id, bookingId, senderUid, kind (text / photo / system), body, createdAt, readAt | System messages for every state transition |
| Rating | id, bookingId, raterUid, ratedUid, stars (1-5), text?, createdAt | One rating per (bookingId, raterUid); written only when booking status is completed |
| Wallet | userId, balanceEgp (pending / available), heldInEscrowEgp, updatedAt, ledgerVersion | Server-side balance only; every movement is a ledger entry with idempotency key |
| WalletEntry | id, userId, kind (hold / release / fee / payout / refund / adjustment), amountEgp, refType, refId, createdAt | Append-only ledger |
| Payout | id, workerUid, amountEgp, method (Paymob transfer / Fawry payout), status, externalRef | First payout only after 3 completed jobs and ID pass |
| Dispute | id, bookingId, openedBy, reason, evidencePhotos[], status (open / customer_won / worker_won / split / withdrawn), resolution, resolvedAt | Opens freeze the escrow; owner resolves in /owner |
| PlatformFee | bookingId, feeEgp, feeRateSnapshot, collectedAt | Snapshot of the fee rate at acceptance time |
| SafetyFlag | id, workerUid, kind (no_show / unsafe_gas / harassment / theft), sourceBookingId, status, createdAt | Feeds workerScore and suspension |

Visit code: 4-digit, hashed at rest, shown to the customer at booking acceptance and verified by the worker on arrival. En-route location pings are ephemeral (kept 24h, then deleted); the booking stores only arrivedAt.

### 5.4 Owner-only analytics page

- Route `/owner`, server-verified owner token, 403 for everyone else.
- Real metrics only, read from aggregates not raw collections: DAU/WAU/MAU (customers and workers separately), open requests, quotes per request, median time-to-first-quote, time-to-accept, acceptance rate, completion rate, dispute rate, cancellation rate, average agreed price per category, platform fee revenue EGP, payout queue, worker funnel (applied / in_review / verified / active / suspended), ratings distribution, safety flags (1-star, gas/electrical), AI cost, error rate, per-city density.
- A second section for the support role: the dispute queue with evidence photos, the safety-flag queue, the worker verification queue. Each section enforced by the server, not hidden by CSS.
- No invented numbers anywhere: an empty metric shows a dash and the reason, never a zero dressed as a fact.

### 5.5 AI with the fallback chain

Chain from `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`: Gemini `flash-lite-latest`, then `flash-latest`, then any Gemini text model, then OpenRouter free models, then other free providers, then the local model on this PC. One Gemini key and one OpenRouter key per product, created on this product's own project, stored only in the ignored env file and the Vercel environment, never printed, never committed.

| Feature | AI role | Hard rule |
|---|---|---|
| Job description assistant | Customer describes the problem in messy words; AI proposes category, safety tier and a photo checklist | Advisory only; the customer confirms the category; AI never creates the request alone |
| Quote draft for workers | Worker writes the job in one line; AI drafts a quote note and a fair-range hint from completed jobs of the same category | The price is the worker's number, always; the range comes from real completed bookings, never invented |
| Support assistant | Answers from `docs/help/*.md` only | Refuses anything not in the help source, and says so |
| Weekly owner report draft | Draft the Telegram weekly summary | Numbers come from the database, the model only writes the sentence |
| Dispute summary for the owner | Summarise the two sides' messages for the /owner dispute queue | Advisory only; the owner decides; the summary quotes real messages |

Free users get 5 AI calls per rolling 24 hours with a visible badge, the owner is unmetered, `AI_ENABLED` is the kill switch, a daily cost cap lives in `config/limits.json`, and every call logs which provider answered (never the content). Arabic and English eval sets exist before the feature ships, and the runner exits non-zero below the threshold.

### 5.6 Data and money

- Firestore with deny-by-default rules, per-user and per-role claims, emulator tests including a cross-tenant read that must fail.
- Accepting a quote is a Firestore transaction with an idempotency key: (1) verifies the quote is pending and the request is open, (2) creates the booking with a hashed visit code, (3) moves the quoted amount into wallet escrow as a `hold` entry, (4) notifies both parties. Test: 20 parallel accepts of different quotes on one request produce exactly one booking and 19 clean rejections.
- Escrow release: customer confirms completion, then a `release` entry minus fee plus worker credit. If the customer does nothing for 72h after the worker marks the job done, the dispute window closes and the hold auto-releases. Never released before arrival is confirmed.
- Photos are size- and type-checked before upload, stored with signed URLs, auto-deleted 90 days after completion (default; the lawyer may change it).
- Jobs in the gas/electrical safety tier require the worker to hold that category's safety-QA pass; the server enforces it, the client never decides.
- Wallet and payouts are server-side only (Admin SDK). The client never sees or sends balances; it only reads its own ledger entries.
- Paymob and Fawry in test mode; webhooks HMAC-SHA256 signed with the timestamp inside the signed body, server-side verification only, tampered, replayed, unsigned and wrong-timestamp events rejected.
- Refunds and cancellation: one written policy on the request page before booking; cancellation before accept is free, after accept the agreed price is frozen until evidence settles, the fee is refunded to the platform only when cancellation was the worker's fault.

### 5.7 Hosting and delivery

- **Firebase Hosting** is primary. **Vercel** is the second host, the same repository imported with the Vercel CLI, the same build, the same environment variables on both. Both addresses are curl-checked and written into the project checkpoint.
- Static hosting cannot run route handlers, so every secret, webhook, AI call, geo query and payout lives in the Firebase Functions or the Vercel function side, never in the client bundle.
- A service worker caches the catalog, the user's bookings and the visit code screen. Background sync sends queued chat messages when the connection returns.
- Daily Firestore export to a private bucket, a monthly restore test, a health endpoint at `/api/health`, a status JSON, a nightly error digest and a weekly Telegram report at a round hour.

### 5.8 Security baseline

Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI. A CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent, with Reject All as prominent as Accept. One-tap data export and one-tap deletion. Rate limits on auth, OTP, request, quote, upload, AI, chat and webhook endpoints. Phone verification by OTP before a worker's first accepted job and before a customer's first booking. No fake data in any path a user can see. En-route pings are ephemeral (24h), never sold, deleted by the nightly job.

---

## 6. Premium quality bar

This is the floor from `D:/Projects/_SIR/standard/23-premium-code-bar.md` and `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`, written for this product.

**Motion, Apple level.**
- One shared spring config across the app: stiffness 300 to 400, damping 28 to 30, transform and opacity only, no layout thrashing, 120 Hz safe.
- Every sheet, drawer, modal and panel opens and closes with the same spring. An open-only animation is a defect.
- The quote-comparison reveal, the route en-route map and the visit-code settle animation use springs; micro-interactions 100 to 150 ms, standard 200 to 300 ms, large 300 to 500 ms. Press scale 0.98. Reduced-motion path for every animation.
- The active tab shows its label and the others show an icon only, the active tab scrolls into view on load and on change, and the bottom bar never vanishes when the keyboard opens.
- Skeletons match the final geometry, optimistic feedback lands under 100 ms, and no white flash on theme change.

**Two languages, one layout.**
- Egyptian Arabic first for customers and workers, English second for the international market, MSA only in legal pages. Both shipped together, never one as a partial translation.
- RTL designed first: logical CSS properties only, flipped directional icons, Arabic line heights, never a mirrored afterthought.
- Every text input detects Arabic or Latin per character as the user types and moves the caret and the direction live. Every mixed run is isolated with `<bdi>` or `unicode-bidi: isolate`. The words "RTL" and "LTR" never appear to the user. The job-description composer and chat composer behave like WhatsApp.
- Currency auto-detected from the visitor locale and IP, with a manual override on top. Dates and times formatted with `Intl`.

**Five states on every screen.**
Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake worker, a fake quote, a fake review or a fake number.

**Accessibility.**
WCAG 2.2 AA. Every control has an accessible name. Touch targets at least 44 px with no covered hit area. Full keyboard path on every screen, visible focus, zoom from 80 to 200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured, and a colour pair that passes contrast in light, dark, system and high-contrast themes.

**The look.**
One design system: tokens for colour, spacing on a 4 and 8 px grid, radii, shadows, type and motion. Seed colour a calm trusted teal `#0F766E` for a home-services product, neutral canvas, accent only for primary actions and key numbers (agreed price, ETA). No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. One component per control, never two. Arabic screen face: IBM Plex Sans Arabic, Cairo or Tajawal.

**Native app feel.**
The browser's text selection and the right-click menu are disabled site-wide and replaced by the app's own menu with in-app actions and a refresh. Normal select, copy and paste inside real input fields still work.

**Safety and trust surfaces are part of quality, not an afterthought.**
Worker identity card (name, photo, verified badge, rating, jobs completed) is shown before the visit, share-visit with a trusted contact is one tap, the visit code is large and glanceable, the report button is reachable within one thumb-travel from any in-visit screen, and a gas/electrical job shows the worker's category safety-QA pass badge.

**Evidence before the word done.**
Screenshots at 320, 390, 768, 1280 and 1920 px, in Arabic and English, in light and dark, plus 3840 px once. Playwright on the critical journeys. Lighthouse mobile 90 or better. A click-target audit in CI. The self-audit loop runs until two clean cycles.

---

## 7. Free tier and fair pricing (EGP and USD)

These are **test prices**, not published prices. They are the outline the owner confirms with three real craftsmen and three real homeowners and the official gateway fee schedule before anything is charged. The USD column uses 48 EGP per 1 USD, which is "(unsourced, verify)" and is recomputed from the live rate on the pricing page.

| Plan | Who | EGP | USD | What it includes | Rule |
|---|---|---|---|---|---|
| Customer Free | Any visitor | 0 | 0 | Post requests with photos, receive and compare quotes, book, chat, visit tracking, rate completed jobs, dispute flow, data export | The core actions are never behind a plan |
| Worker Free | A verified craftsman | 0 per month + 12% service fee per completed job (test rate) | 0 + 12% | Unlimited bids, worker cabinet, wallet, payouts, ratings, safety-QA badge | A worker never pays to join or to bid |
| Worker Pro | A full-time craftsman | 249 per month or 2,490 per year (test) | about 5.20 per month or about 52 per year | 0% service fee, priority listing in quote feed, verified "Pro" badge, analytics (views, win rate, earnings), priority support | Cancel any time; the plan lapses at the end of the paid cycle; never both a fee and a subscription on the same job |
| Company / Compound | A property manager or landlord | price set with the owner | | Managed unit dashboard, AMC contracts, vetted vendor pool, consolidated invoicing | Later milestone, decided with the first real compound |

**Fairness rules written into the product.**
1. A homeowner never pays to post, quote, book, chat, track or rate.
2. A worker never pays to join or to bid. The fee is on completion only, one model or the other per job (the Worker Pro subscription replaces the per-job fee, never stacks).
3. Every price on screen is in the visitor's currency, auto-detected, with the original EGP amount next to it.
4. An agreed price is frozen at acceptance. It can only move with both sides tapping "agree to new amount" in the booking, and the app records who proposed and who agreed.
5. The escrow holds the agreed amount only. The platform fee is taken from the worker's side, never added on top of the customer's agreed price.
6. No ads, in any tier, ever. The owner sets an ad spend cap of 0 until he changes it.
7. The owner of the product gets every paid feature, free, and a subscription grants him all permissions inside the owner console.

**Still open and blocking publication:** the official Paymob and Fawry fee schedules for Egypt, the tax and invoicing treatment of service fees in Egypt, the exact cancellation and refund wording, the eKYC provider for Egypt (Veriff, Onfido, Shuftipro, or an Egyptian local vendor), and the lawyer review of every legal page. Each is tagged "(unsourced, verify)" in `ops/competitors/sir-handyman.md` section 4 and in `docs/ENV.md` when the project starts.

---

## 8. Milestones M0 to M6, with acceptance tests

Every exit check is something a reviewer can run or click. "Green" means the output was seen, not assumed.

### M0: Foundations, the kit and the honest map of the market

Work: verify whether a Firebase project and a GitHub repo named `sir-handyman` already exist (they do not today); if not, create the Firebase project `sir-handyman` on the free Spark plan and the GitHub repo `sirahmed8/sir-handyman` (private) as the only remote; **create the project folder `D:\Projects\SIR Handyman` with `.sir/`, `AGENTS.md`, `folder.ico` in the project root, `.gitignore`, and the Desktop folder kit** (`Desktop\SIR Projects\SIR Handyman` holding `folder.ico`, `SIR Handyman.lnk`, `Start SIR Handyman dev.lnk`, `Stop SIR Handyman dev.lnk`, `Open project folder.lnk` and `Versions.txt` reading version 1.0.0 and a plain status); scaffold the monorepo (apps, packages, docs, scripts) with strict TypeScript, Tailwind v4 tokens, RTL-first styles and the shared `verify` script; design the token set and three design directions; write `docs/DATA_SOURCES.md`; research Egyptian eKYC providers and pick one sandbox.

Do **not** create any of the above in round r54. M0 runs as its own round after HQ approves the plan.

Exit checks:
1. `D:/Projects/SIR Handyman` contains `folder.ico` (named exactly that, never `icon.ico`) and the Desktop folder `SIR Projects/SIR Handyman` holds the six kit items from item 19 of OWNER_DEFAULTS, verified by listing the folder.
2. `pnpm verify` runs typecheck, lint, tests, build and gitleaks, and the output was seen green.
3. The Firebase project `sir-handyman` exists and the GitHub repo `sirahmed8/sir-handyman` is the only remote for it.
4. `docs/DESIGN.md` holds three explored directions with screenshots and the chosen one, plus the token file.
5. `docs/DATA_SOURCES.md` lists every data source with its licence and its last-checked date.
6. A one-page eKYC comparison (providers, per-check cost in EGP/USD, Egypt coverage, Arabic support, sandbox availability) is written in `docs/EKYC.md`, each claim tagged with its source or "(unsourced, verify)".

### M1: Catalog and worker onboarding, proven offline

Work: the service taxonomy (own, never copied); the worker application flow (categories, photo, bio, service area, phone OTP, safety-QA questionnaire for gas/electrical categories); the KYC pass/fail flag integration in sandbox mode; the seed of zero (empty states rendered, never sample workers).

Exit checks:
1. A worker can apply, upload a photo, pass phone OTP, answer the safety questionnaire for electrical and see "in review" with the five states everywhere.
2. A forged client-side "verified" flag gives the worker nothing: the server only reads the KYC flag, proven by a test that flips the client flag and expects 403 on the worker cabinet.
3. Empty catalog areas show the empty state with one action at 390 px and 1280 px, in Arabic and English, light and dark.
4. The safety-QA questionnaire blocks a gas job assignment to a worker without the pass, enforced server-side, with a test.

### M2: Request, quote and acceptance under contention

Work: the request flow (category, description, photos, GPS/pin, time window); the worker quote feed (nearby verified workers, filters); the quote comparison screen; the accept transaction (idempotency key, escrow hold, booking creation, visit code); the customer booking screen and the worker job screen.

Exit checks:
1. 20 parallel accepts of different quotes on one request produce exactly one booking and 19 clean rejections, emulator test.
2. A quote from a worker outside the request's service area is refused by the server.
3. A request created with a photo of the wrong type or over size is refused before upload.
4. The agreed price is frozen in the booking; an attempt to change it without both-side consent is rejected by the server, with a test.
5. Arabic and English, light and dark, 390 px and 1280 px, the five states on the request, quote-comparison and booking screens, verified by Playwright.

### M3: The live visit, money and the owner page

Work: en-route pings with 24h TTL; arrival confirmation with the visit code; in-app chat with photo and system messages; escrow release (customer confirm or 72h auto-release); Paymob/Fawry webhook in test mode with the ten negative tests; the owner-only analytics page; the dispute flow (open, evidence photos, freeze, resolve); the 1-month maintenance guarantee tracking for eligible categories.

Exit checks:
1. Ten negative webhook tests pass (tampered, replayed, unsigned, wrong timestamp, wrong amount, and the rest), and no `dev_signature` or any other bypass exists in the code.
2. A non-owner token on `/owner` gets 403 and a forged token gets 403.
3. The visit code is required before the worker can mark arrival; a wrong code fails, a correct code moves the booking to `arrived`, with a test.
4. Escrow: customer confirms completion and the worker's ledger shows `release` minus fee; or 72h passes after in_progress and the hold releases automatically, with time-travel tests in the emulator.
5. A dispute opened by either side freezes the escrow; the /owner dispute queue shows both sides' messages and the evidence photos; resolving it writes the resolution to the booking.
6. Both hosts answer: the Firebase URL and the Vercel URL were curl-checked, and the two addresses are written in the project checkpoint.
7. A reminder fires at a round hour, sends through the Telegram sender, and the owner's weekly report arrives with the numbers and their meaning.

### M4: Ratings, notifications, the Expo app and the safety playbook

Work: ratings (one per booking, completed only); push and Telegram notifications; the worker score recomputed from completed jobs; share-visit with a trusted contact; the safety playbook screen (share visit, emergency call, report button, arrival code); the Expo Android and iOS apps with the full customer and worker flows.

Exit checks:
1. A rating without a completed booking is refused by the server, with a test; a second rating on the same booking by the same user is refused.
2. The Android APK builds and installs on a device, and the same Google account sees the same bookings on the web app and the Expo app.
3. The share-visit link opens a read-only page for the trusted contact showing the worker's name, photo, ETA and visit code status, and expires when the booking completes.
4. A gas/electrical booking surfaces the worker's safety-QA pass badge; a worker without it cannot be assigned, emulator test.

### M5: AI, the desktop apps and the quality pass

Work: the job description assistant and the quote-draft AI (advisory only); the support assistant grounded in help docs; the Windows installer with the same sign-in and self-update; the macOS and Linux builds; widgets and live activities; the full self-audit.

Exit checks:
1. `npm run eval:assistant` and `npm run eval:support` pass with Arabic and English sets, and the support assistant refuses an ungrounded question.
2. The Windows installer installs, starts, signs in with the same Google account, updates itself, and its entry is in `Projects-Hub.html` and on the Download page with the version and the size.
3. Screenshots exist at 320, 390, 768, 1280 and 1920 px in both languages and in light, dark and high contrast, with the five states visible.
4. The accessibility audit passes WCAG 2.2 AA with an accessible name on every control, no covered hit area, and no horizontal scroll from 320 px.
5. Lighthouse mobile is 90 or better and the JSON is saved in `.sir/evidence/`.

### M6: Release, first real jobs and the legacy handover

Work: the launch package (domain, accounts, legal review); the first real workers onboarded with written consent in one Cairo district; the first real jobs with written consent; the B2B AMC lane decision with the first compound; the optional membership plan only if the owner wants it after three months of real data.

Exit checks:
1. Five real workers in one Cairo district are live with written consent, verified IDs and at least one completed job each with a real customer, and no seeded or invented worker exists in any path a user can see.
2. Five real completed jobs exist in production with agreed prices, escrow releases and ratings both ways.
3. The 301 redirects from any old hosts are verified by curl.
4. The lawyer has reviewed the legal pages and the eKYC contract is signed, and only then can a paid plan go live.
5. The first dispute (if any) was resolved in /owner with the evidence trail intact, or the report says there were none.

---

## 9. The first ten tasks for the free agents

Ready to queue, each with its own brief: `D:/Projects/_SIR/ops/briefs/sir-handyman-tasks.md`.

1. Monorepo scaffold with tokens, RTL, the health route and CI.
2. The product's own Firebase project and the `owner-auth` package with negative tests.
3. The data model (`packages/core`) and the Firestore rules, with emulator tests.
4. The service taxonomy and the worker application flow with phone OTP and safety-QA.
5. The request flow with photos, GPS/pin and time window.
6. The worker quote feed, the quote comparison screen and the accept transaction.
7. En-route tracking, the visit code and the in-app chat.
8. Escrow release, Paymob/Fawry webhook (test mode) and the wallet ledger.
9. The ratings system (completed jobs only) and share-visit with a trusted contact.
10. The owner-only analytics page and the dispute queue.

---

## 10. Skills from the library that this build uses

Picked from `D:/Projects/_SIR/ops/SKILLS_INDEX.md` and the digests in `D:/Projects/_SIR/ops/encyclopedia/`. Digests live under `ops/encyclopedia/<tool>/<skill>.md`; the paths below are the real files found on 2026-11-12.

**Design and UI**
- `anti-vibecoded-design-system` (claude) - keeps the product away from generic AI styling and purple gradients.
- `taste-design-engine` (claude) - the self-audit against AI patterns before the screens ship.
- `emil-motion-impeccable` (claude) - the spring physics for the sheets, the tab bar and the visit-code settle.
- `modern-ui-ux-design-system` (claude) - tokens, micro-interactions and hierarchy for one design system.
- `cognitive-product-intuition` (claude) - the request-quote-accept step order and the empty states.
- `high-conversion-copywriting` (claude) - the promise line and the request copy that sell the end state without hype.
- `commercial-app-blueprint` (claude) - llms.txt, the trust signals and the sticky call to action on the site.
- `a11y-debugging` (codex) - the accessibility audit with Chrome DevTools against WCAG 2.2 AA.
- `mobile-ergonomics-polish` (claude) - touch targets, no horizontal scroll, tap feedback on the phone screens.
- `modern-web-guidance` (claude) - the current web APIs, container queries and dialog behaviour, run before any client-side work.
- `react-best-practices` (claude) and `nextjs` (claude) - App Router structure, Server Components, rendering and performance rules.

**Security and legal**
- `firestore_rules_creation` (claude) - the deny-by-default rules for every collection.
- `firebase_security_rules_auditor` (claude) - the audit that finds a cross-tenant read before a user does.
- `zero-trust-security-hardening` (claude) - server-side role checks, secure cookies and rate limiting.
- `owasp-vulnerability-shield` (claude) - the OWASP pass over uploads, webhooks, chat and auth.
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
- `chat-sdk` (codex) - the Telegram bot for the weekly report and booking notifications.
- `webhook-testing` (deep) - capturing, replaying and validating the gateway webhooks.
- `verification` (codex) and `verification-before-completion` (deep) - the end-to-end check before the word done.

**Data, hosting and growth**
- `firebase_firestore` (claude) - queries, indexes and the data model.
- `database-reliability-transactions` (claude) - the atomic quote acceptance and the idempotency keys.
- `firebase_hosting_basics` (claude), `vercel-cli` (codex), `deployments-cicd` (codex) and `env-vars` (codex) - the two hosts with the same build and the same variables.
- `google_maps_platform` (codex) - the en-route map, the geocoding and the distance search.
- `open-seo-auditor` (claude) - Arabic search visibility, JSON-LD and the AI answer check.
- `system-design-architect` (claude) and `production-engineering-standards` (claude) - the zero-mock persistence and the production bar.

---

## 11. Risks and the defaults we take

- **Two-sided cold start in one district.** Default: one Cairo district, 5 real workers and 5 real completed jobs before any advertising or search push. No marketing before the sourcing tasks in the competitor file are done.
- **A stranger enters the home.** Default: identity pass/fail flag from a third-party eKYC before the first accepted job, worker photo and rating shown before the visit, share-visit with a trusted contact, 4-digit visit code, report button within one thumb-travel, gas/electrical safety-QA as a separate pass. Never document images stored.
- **Price disputes and "he said, she said".** Default: agreed price frozen in the booking, photos at request and at completion, both-side consent needed to change any amount, dispute freeze on the escrow, owner resolution in /owner with the evidence trail.
- **Fake ratings and shill reviews.** Default: one rating per completed booking per user, server-enforced; no rating without a completed booking; the rating is locked after the dispute window closes.
- **Worker churn from a bad first week.** Default: first three payouts only after 3 completed jobs and an ID pass, weekly worker report with earnings, service fee visible in the worker cabinet as a single line.
- **Gateway, eKYC and tax numbers.** Default: every one of them is "(unsourced, verify)" until read on the official page on the day it is used. Paymob and Fawry fee schedules for Egypt are not publicly documented; the exact percentage per transaction and the tax treatment of service fees require lawyer verification. eKYC provider selection (Veriff, Onfido, Shuftipro, or an Egyptian local vendor) remains unsourced.
- **Static export killing the server.** Default: no secret ever in a route handler that a static host would drop; the server features run on the functions side from M1.
- **Safety tier on gas and electrical jobs.** Default: a separate safety-QA pass per category, server-enforced, and a licence-check where Egyptian law requires one for that trade (owner to confirm with the lawyer before paid launch).
- **Competition undercuts prices.** Default: never compete on price; compete on agreed price, identity, visit tracking and dispute protection, and let the fee pay for support and safety.
- **Arabic RTL design gap.** Default: most Egyptian pages mix Arabic and English; nobody ships a fully RTL, Egyptian-speech product with proper bidi isolation. Risk: without deliberate RTL design first (logical CSS, bidi isolation, Arabic typefaces), the product will feel foreign to Egyptian users. Recommended answer: enforce RTL design first from M0; use IBM Plex Sans Arabic / Cairo / Tajawal; test every screen in Arabic and English, light and dark, from day one.
- **Cold start quote generation.** Default: with only 5 workers initially, quote volume may be too low to show meaningful comparison. Risk: homeowners see "no quotes available" and leave before the network effects kick in. Recommended answer: keep the M0-M1 sourcing period exclusive (5 workers + 5 jobs minimum) before opening the quote feed to new requests; during M0-M1, display an empty state with one action ("Tell us your city and we will tell you when workers arrive there") rather than showing an empty quote feed.
- **PDPL 151/2020 compliance scope.** Default: data minimization and consent tracking are implemented, but the full legal review of every data collection point is pending. Risk: non-compliant data collection could block the product launch or expose the owner to fines. Recommended answer: schedule the lawyer review of legal pages (privacy policy, terms, data processing addendum) as an M6 gate; until then, keep all data collection minimal and tagged "(unsourced, verify)".
- **Paymob/Fawry test mode limitations.** Default: webhook testing in emulator covers 10 negative tests, but real gateway behavior may differ. Risk: production webhooks may fail if the test mode signatures differ from live mode. Recommended answer: run at least 20 negative webhook tests (expand the emulator test set) before moving to test accounts; after launch, validate webhook signatures against the live gateway documentation before enabling paid plans.

---

## 12. Only the owner can do

Buy the domain and point it at both hosts. Create and fund the Paymob and Fawry business accounts and paste the keys into the project's ignored env file. Sign in once on the Google OAuth screen so the branding is right. Talk to five real craftsmen in one Cairo district, or approve the outreach text. Lawyer and accountant. Buy the eKYC contract (the owner signs; agents research and prepare). Buy the code-signing certificate later. Create the Play Console and Apple developer accounts when the reinvestment ladder allows. Approve the launch district.

Everything else is an agent's job.

---

## 13. Sources and files

- Canonical competitor study with dated links: `D:/Projects/_SIR/ops/competitors/sir-handyman.md`
- The ten build briefs: `D:/Projects/_SIR/ops/briefs/sir-handyman-tasks.md`
- Shared kit: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`
- AI chain: `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`
- Quality charter: `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`
- Desktop and Windows standard: `D:/Projects/_SIR/plans/WINDOWS_APP_STANDARD.md`
- Product direction (sections 5, 6, 8): `D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md`
- Legacy source and notes: `D:/Projects/_SIR/plans/sir-handyman.md` (r51, superseded), `D:/Projects/_SIR/ops/TICKTICK_MAP.md` idea 28, `D:/Projects/_SIR/plans/BACKLOG_IDEAS_DECISIONS.md` section 3.5, `D:/Projects/_SIR/plans/sir-hagoozat.md` section 3.4
