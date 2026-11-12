# PLAN: SIR Game Deals (Wave 9, GLOBAL product, rebuild from zero, small independent project)

## Vision (owner, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` sections 5, 6 and 8)

SIR Game Deals is its own small independent project with the same premium standard as every other product: every game discount and every free game across the stores an Egyptian player actually uses, with the price in pounds, the price history, the lowest price ever, and an alert before the offer ends. It is not a module of any other product. The old `plans/sir-deals.md` (r51, the games half, which also held a general price finder) is superseded by this file; the git history keeps it. The price finder half of that old note becomes SIR Price Finder, its own project, per `PRODUCT_DIRECTION_2026-11-12.md` section 8.

**Version 1.0.0.** Audited and rewritten 2026-11-12 (round r54, HQ). The canonical competitor study is `D:/Projects/_SIR/ops/competitors/sir-game-deals.md` (dated 2026-11-12, sources opened or indexed on that date, with sourcing tasks still open). The first ten build tasks for the free agents are in `D:/Projects/_SIR/ops/briefs/sir-game-deals-tasks.md`.

**Truth rule for this plan.** Nothing here is called working unless a reviewer saw it today. The product has never been built: `D:\Projects\SIR Game Deals` does not exist yet, no Firebase project exists for it, and no GitHub repo exists for it. This round wrote the plan, the competitor study and the task briefs only, and it created no folder, no repo, no code and no key. Verified today by our own probes: Steam's public store endpoint returns `$39.99 USD` for Elden Ring with `cc=EG` while the same call returns `249.00 SR` for `cc=SA` and `249.00 AED` for `cc=AE`, so Steam has no Egyptian pound price and the Egypt row of the competitor study rests on a measurement, not on an assumption.

**Product class: GLOBAL.** Anyone in the world can use it, accounts and subscriptions exist, every platform is planned, the owner has an owner-only analytics page, the site is hosted twice (Firebase Hosting and Vercel), and a paid subscription gives the owner every permission inside the product. It is listed in `PRODUCT_DIRECTION_2026-11-12.md` section 8 among the small independent projects created from the unplanned ideas.

---

## 1. Who it is for, and the promise

**For the Egyptian player.** The person who has a wishlist on Steam, a limited budget in pounds, and a dollar rate that moves every week. They want to know which game is at its lowest price right now, whether it was ever cheaper, and which free game they can still claim today before it is gone. The one-line promise, in the words a player would use:

> See every discount and every free game for the games you play, in pounds, before the offer ends.

**For the player outside Egypt.** The same tracker with the currency and the region of their own store: a Steam, Epic, GOG, Xbox or PlayStation discount with a real history, a lowest-ever flag, a wishlist and an alert channel.

**The end state we sell.** A player opens the app and sees three things in one screen: the free games that can be claimed right now with the hour they end and the store giving them away, the discounts on the games in their watchlist with the price in pounds next to the price in dollars, and a clear flag on the ones that are at their lowest price ever. They import their Steam wishlist once and never type a game name again. When a game they watch drops under their number, they get a Telegram message with the store, the price in pounds, the expiry time and one tap to the page. Every number on screen says where it came from and when it was seen.

**Not in v1:** no ads, no invented prices, no fake users, no fake "lowest ever" line, no scraping of stores that forbid it, no selling of keys, no key reseller ranking, no invented countdown, no dark-pattern urgency and no paywall on browsing, history or the free game tracker.

---

## 2. The ten competitors, and where we win

Full table with sources, dates and the second ring: `D:/Projects/_SIR/ops/competitors/sir-game-deals.md` (dated 2026-11-12).

| Competitor | What it proves about the market | Our edge |
|---|---|---|
| HalfLoot (Egypt) | Egyptian players want the final price in pounds, paid by mobile wallet, with a human answer | Every store in one place (not PlayStation only), price history, lowest-ever flag, free games, wishlist and alerts, and neutrality because we never sell |
| PSprices (global, Arabic, no Egypt region) | History, lowest-price collections and Telegram alerts are the proven core of this category | Egypt and the Arab market as a first class region, EGP pricing, local shops and wallets, free game tracker, Arabic Egyptian copy |
| Games2Egypt (Egypt) | Regional gift cards and instalment payment are how Egyptians buy games | We stay a neutral tracker and show the region and the activation type on every offer so the buyer is not caught |
| NileShopper (Egypt) | The freshness rule (only prices seen in the last two days) is the trust feature | The same honesty, plus history curves, the lowest-ever flag, alerts and the free game tracker |
| Games4Egypt (Egypt) | A browsable catalogue by platform, genre, rating and year is the right browse shape | The same browse filters over live prices, with history, alerts and giveaways |
| IsThereAnyDeal (global, has an EG region) | The market is global and already expects a country and currency switcher | Arabic first, EGP by default, our own observed history, local shops, the giveaway calendar and a trust tier per store |
| GG.deals (global) | The historical low is the number players chase | The same history, built from our own lawful observations, plus the Egypt layer it cannot see |
| CheapShark (global) | A free documented API and a simple alert flow are enough for a useful tracker | Same API-first discipline with a written source ledger, plus the stores it does not cover, history and giveaways |
| GamerPower (global) | The free game side of the market has its own audience and its own API and RSS | Deals and free games in one list, the countdown next to the price history, the Egypt region |
| SteamDB (global) | Price history per app is possible and is what players want | We own our observations instead of copying a community scrape, and we add alerts, the lowest-ever flag, free games and Arabic |

**Category truth from the sources (2026-11-12):** the Egyptian market already has good narrow products (a PlayStation deal site, a shop, a comparison site) and the global market has good aggregators, but nobody joins the discount history, the free game calendar and the Egyptian price in one Arabic-first product. Steam itself has no Egyptian pound price, so the conversion, the rate and the date are the product, not a detail. Our plan follows that truth instead of fighting it.

---

## 3. Features

### 3.1 Parity with the best in the category (must ship)

| Feature | Why it is in the list | Source of the requirement |
|---|---|---|
| One deals feed across Steam, Epic, GOG, Xbox, PlayStation and Egyptian shops | The aggregator baseline | IsThereAnyDeal, CheapShark, HalfLoot |
| Price history curve per game and per store | What players actually come back for | GG.deals, SteamDB, PSprices |
| Lowest price ever flag, with the date and the store that had it | The chasing number | GG.deals, PSprices |
| Freshness on every price (seen at, plus a stale badge after two days) | The Egyptian trust feature | NileShopper |
| Free game tracker with the end time and the claim link | A separate product today, merged here | GamerPower, Epic |
| Giveaway reminder before the claim window closes | The reason a free tracker keeps a user | GamerPower expires-soon list |
| Wishlist import from the user's own Steam account | The shortest path from nothing to useful | PSprices PSN sync, our design for Steam |
| Watchlist with a target price in the user's currency | The retention loop | PSprices, IsThereAnyDeal waitlist |
| Alerts by Telegram, email and push, with quiet hours | The category standard | PSprices (Telegram, email, browser), GamerPower alerts |
| Filters: store, platform, genre, discount depth, price range, DRM free, region, activation type | Browsing without noise | Games4Egypt, PSprices |
| Sort by discount, by absolute saving in the user's currency, by lowest ever | The right sort for a tight budget | Our design from the Egypt finding |
| Every offer shows the region the key unlocks, the activation type and the store trust tier | The number one complaint about key shops | TechBites Store notes, GamerPower |
| Price in the visitor's currency with the original price, the rate used and the date | Steam prices Egyptians in dollars | Our Steam probe, HalfLoot |
| Egyptian shops and wallet payment marked clearly | How Egyptians actually buy | HalfLoot, TechBites Store |
| Subscription tracker: what PS Plus, EA Play, Ubisoft+ and Game Pass cost and what they include | A big part of the player's real spend | HalfLoot subscription prices, IsThereAnyDeal subscription tracking |
| Arabic Egyptian first, English second | The clearest local gap | Every global competitor is English first |
| Support assistant grounded in the help source | Cuts support time | Shared kit help centre |
| Data export and one-tap account deletion | Legal and trust baseline | Shared kit security baseline |

### 3.2 The owner's own ideas, carried forward from legacy and TickTick

Every line says where it came from, so nothing gets silently rebuilt thinner than what he already asked for.

| Idea | Source | Status in this plan |
|---|---|---|
| Game discounts across stores | TickTick "أفكار برامج ومشاريع" idea 16 (mapped in `ops/TICKTICK_MAP.md` row "price and game-deal finder") | The core of M1 and M2 |
| Free games across stores | Same idea 16, read as the games half | M4, first class content with a countdown |
| Price history and lowest ever | Brief scope | M1 engine, M2 UI |
| Alerts | Brief scope | M3 |
| Wishlist import | Brief scope | M3 |
| Regional pricing for Egypt | Brief scope, and confirmed by our own Steam probe | M1 data model, M2 display, M3 alerts |
| Split the old deals note into a price finder and a game deals product | `PRODUCT_DIRECTION_2026-11-12.md` section 8 | Done: this file is the games half, SIR Price Finder is the other half |
| Key shops and Egyptian stores as sources | Brief scope | M1 source ledger, with a trust tier per store |

**Explicitly dropped from the legacy note:** the r51 note treated games and general product price comparison as one product and stopped at a three-milestone placeholder gated on retailer affiliate programmes. The owner decided on 2026-11-12 that each idea is its own project, so this plan covers games only and runs on the M0 to M6 ladder. The lawful-data gate survives and gets stronger in section 3.4.

### 3.3 Explicitly out of scope for v1

Selling keys or gift cards, ranking or recommending any key reseller, any scraping of a store whose terms forbid it, price prediction or "deal score" invented by a model, notification of a discount that we did not observe ourselves, console pricing from an unofficial scrape, a marketplace of user sellers, and any feature that needs a government or store feed we have no lawful source for. Those wait for a signed agreement.

### 3.4 Lawful data

The rule from the old note still stands and it is the reason the data model is built around our own observations.

1. **Tier A, public endpoints we may call.** Steam's public store endpoint (verified on 2026-11-12 to answer a country code and return the price), the Steam Web API with a key for the app catalogue, and a public giveaway API. Each one is checked against the vendor's terms before it is used, and the check is written in `docs/DATA_SOURCES.md` with the date.
2. **Tier B, partner and affiliate feeds.** GOG, Xbox, and key shop and retailer affiliate programmes. These give a lawful price feed and a revenue link, and they are how the commercial model works.
3. **Tier C, our own observations and user-owned data.** The price history is built from the offers we observe ourselves through Tier A and Tier B, with the observation time and the source stored on every point. A user can import their own wishlist from their own account, and a user can report a price they saw in an Egyptian shop; a user-reported price is marked as reported, moderated, and never mixed into the lowest-ever calculation without the same source rules.
4. **Never:** scraping a store that forbids it, copying a community price database, using a scraped feed as our own, or presenting a stale price as current.
5. Every data source is listed in `docs/DATA_SOURCES.md` with its licence, its terms status, its last-checked date and the trust tier we assign it. Every price on screen cites one of them.

---

## 4. Platform matrix

Standing rule (owner, 2026-11-12): every product ships on all platforms, so web, Windows, macOS, Linux, Android and iOS are all required for SIR Game Deals. Wear OS, watchOS, TV and car are not in that list, so they are skipped in v1 with a written reason, not left in silence.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required | The whole product: deals feed, game detail with the history curve and the lowest-ever flag, free games with the countdown, watchlist, alerts, filters, owner console, pricing, help centre, legal | Nothing pending |
| PWA (installable, offline) | Required | Install from the browser, offline watchlist and last seen prices, offline giveaway list with the countdown, background sync | Native shell only if the PWA proves weak on low-end Android |
| Windows | Required (M5) | Installable PWA from day one, then a real installer with the same Google sign-in and self-update | Signed installer (the owner buys the certificate) |
| macOS | Required (M5) | Installable PWA from day one, then the same desktop shell as Windows | Signed build when the owner has an Apple account |
| Linux | Required (M5) | Installable PWA from day one, then AppImage and .deb from the same shell | Signed package |
| Android phone and tablet | Required (M4) | Expo app: the same account, the deals feed, the free games countdown, the watchlist, the alerts with quiet hours, offline last-seen prices | Play Store when the reinvestment ladder allows; Wear OS after that |
| iPhone and iPad | Required (M4) | Expo app, same account and data, tablet layouts, iOS widgets later | App Store or SideStore when the owner has a paid Apple account |
| Wear OS | Skipped in v1 | Nothing | A price-drop complication for the games on the watchlist, decided with an ADR |
| watchOS | Skipped in v1 | Nothing | Same ADR as Wear OS |
| TV (Android TV and Apple TV) | Skipped in v1 | Nothing | A deals wall screen only if a store or a partner asks |
| Car (Android Auto and CarPlay) | Skipped in v1 | Nothing | Voice "is my game cheaper today" only if a paid tier needs it |
| Telegram bot | Required (M3) | The alert channel for every user, one bot for the product, each user links their own account | Voice alerts and digest summaries |
| Browser extension | Skipped | Nothing | A price badge on a store page only if users ask |
| Docker and self-host | Skipped | Nothing | Not a product need here |

**Rule:** every platform shares one Firebase project, one account and one dataset. No platform ever carries its own copy of the rules. The Windows, macOS and Linux builds come from one desktop shell and one release feed.

---

## 5. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. That file is the shared standards kit every product builds against; SIR Platform was cancelled as a project on 2026-11-12, so there is no extraction target any more. SIR Game Deals is a GLOBAL product, so it adopts all twenty sections of the kit as internal `packages/*` with the kit names and interfaces, and when it hardens a piece that other products need, that piece goes back into the kit file and HQ queues the adaptation for the others.

### 5.1 Shape

```
apps/web        Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens
apps/api        Route handlers that need secrets and long tasks (cron ingestion, alerts, AI proxy, wishlist import)
packages/core   Domain types and zod schemas: Game, Store, Offer, PricePoint, PriceHistory, Giveaway, WatchItem, Alert, User
packages/data   Firestore repositories, one interface per entity, emulator tests
packages/ui     The shared UI kit from the kit: InputBox, TabBar, BottomSheet, Card, Chip, Modal, Toast, PriceChart
packages/kit    owner-auth, signed-webhook, billing-fallback, ai-proxy, legal-pack, i18n, help-center, notifications, bot-link
apps/mobile     Expo app for Android and iOS (M4)
apps/desktop    One shell for Windows, macOS and Linux (M5)
docs/           Help centre source, legal source, env names, decisions, DATA_SOURCES.md, PRICE_SOURCES.md
scripts/        Seed-free checks, emulator tests, Lighthouse, AI evals, the source probes
```

Layers depend inward only: presentation, domain (no I/O), data, core. Files under 300 lines, no `any`, no god components, absolute imports.

### 5.2 Accounts (`owner-auth`)

- Google sign-in through Firebase Auth on the product's own Firebase project, ID token verified on the server with JWKS.
- Owner and admin rights come from an allow-list (`OWNER_EMAILS`, `OWNER_UIDS`), fail closed. Nothing in the client decides a privilege.
- Session in an HttpOnly, Secure, SameSite=Strict cookie. No tokens in localStorage.
- Rate limits on sign-in, alert creation, watchlist writes, wishlist import, AI calls and notification sends.
- Owner accounts get a second factor offer.
- Test: a forged token gets 403, a client-side flag flip gets nothing, a non-owner token on `/owner` gets 403.

### 5.3 Owner-only analytics page

- Route `/owner`, server-verified owner token, 403 for everyone else.
- Real metrics only, read from aggregates and never from a raw collection: signups, active users by week, watchlist size, alerts created, alerts delivered and failed, giveaway claim reminders sent and clicked, the number of games tracked, the number of price points stored, the ingestion freshness per source (last successful run and last price age per store), the coverage of cheapest-known price per game, the free to Pro conversion, MRR in EGP and in the visitor currency, the AI cost, the error rate and the notification failure rate.
- A source health panel: every store with its last successful ingestion, its last observed price, its trust tier and a red badge when it goes stale. This is the page that keeps the truth rule alive.
- No invented numbers anywhere: an empty metric shows a dash and the reason, never a zero dressed as a fact.
- The subscription check grants the owner every Pro permission inside the product.

### 5.4 AI with the fallback chain

Chain from `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`: Gemini `flash-lite-latest`, then `flash-latest`, then any Gemini text model, then OpenRouter free models, then other free providers, then the local model on this PC. One Gemini key and one OpenRouter key per product, created on this product's own project, stored only in the ignored env file and the hosting environment, never printed and never committed.

What AI does in this product, and what it must never do:

| Feature | AI role | Hard rule |
|---|---|---|
| Deal digest | Write the daily summary of what dropped for the games a user watches | The prices and the history are data. The model writes the sentence and never a price, a percentage or a lowest-ever number |
| Price explanation | Explain in plain words why a price moved | Only from the observed history, never a prediction and never a forecast |
| Store and region help | Answer "can I buy this key on my Egyptian account" from the help source and the store policy table | Never guesses a region rule, and refuses when the policy is not on file |
| Support assistant | Answer from `docs/help/*.md` only | Refuses anything not in the help source and says so |
| Weekly owner report draft | Draft the summary the Telegram sender sends | Numbers come from the database, the model only writes the sentence |

Free users get a small visible AI quota for the deal digest, the owner is unmetered, `AI_ENABLED` is the kill switch, a daily cost cap lives in `config/limits.json`, and every call logs which provider answered, never the content. Arabic and English eval sets exist before any AI feature ships, and the runner exits non-zero below the threshold.

### 5.5 Data model

Collections, fields and access rules. The full version with indexes lives in `docs/data-model.md` from M1.

| Collection | Key fields | Notes |
|---|---|---|
| `games` | `id`, `title`, `slug`, `storeIds{steam,epic,gog,xbox,playstation}`, `releaseDate`, `genres[]`, `drmFree`, `thumbnailUrl` (store CDN link only, never a copy) | The canonical title we join every store onto. One document per game |
| `stores` | `id`, `name`, `kind` (storefront, keyshop, local_egypt, subscription), `regionRules`, `paymentMethods[]`, `activationType`, `trustTier`, `termsUrl`, `lastCheckedAt` | Our trust tier decides the badge a store's offers carry |
| `offers` | `gameId`, `storeId`, `region`, `currency`, `priceMinor`, `basePriceMinor`, `discountPercent`, `url`, `availability`, `observedAt`, `sourceKind` (api, partner, user_reported), `sourceId` | One live offer per game and store and region. `priceMinor` is an integer in the smallest unit |
| `pricePoints` | `gameId`, `storeId`, `region`, `currency`, `priceMinor`, `observedAt`, `sourceKind` | Append only. This is the history, and it is ours because we observed it |
| `priceHistory` | `gameId`, `storeId`, `region`, `lowestEverMinor`, `lowestEverAt`, `lowestEverStoreId`, `average30dMinor`, `points[]` (downsampled curve) | Derived and rebuilt from `pricePoints`; the lowest-ever flag reads from here |
| `giveaways` | `id`, `gameId`, `storeId`, `kind` (free_keep, free_weekend, dlc, key), `startsAt`, `endsAt`, `claimUrl`, `regionEligible`, `lastSeenAt` | The free game calendar, with the end time the user needs |
| `giveawayClaims` | `userId`, `giveawayId`, `claimedAt`, `reminderSentAt` | Reminders fire from here |
| `watchlists` | `userId`, `gameId`, `targetPriceMinor`, `currency`, `notifyChannels[]`, `createdAt` | One per user and game |
| `alerts` | `userId`, `gameId`, `storeId`, `type` (price_below, any_discount, giveaway_start, giveaway_ending), `thresholdMinor`, `channels[]`, `active`, `lastFiredAt` | Rate limited per user |
| `wishlistImports` | `userId`, `source` (steam, epic, gog), `externalId`, `status`, `importedAt`, `itemsCount` | The user's own account only, never another user's |
| `notifications` | `userId`, `channel`, `payload`, `sentAt`, `status`, `errorCode` | Delivery truth for the owner page |
| `storesEgypt` | `storeId`, `paymentMethods[]` (instapay, vodafone_cash, card, cash), `deliveryCities[]`, `phone`, `notes` | The Egyptian specifics: how the player pays and where it delivers |
| `users` | `uid`, `email`, `locale`, `region`, `currency`, `role`, `createdAt` | Role comes from the server allow-list, never from the client |
| `preferences` | `userId`, `theme`, `language`, `quietHours`, `defaultRegion`, `displayCurrency` | Locale defaults, auto-detected with a manual override |
| `subscriptions` | `userId`, `plan`, `status`, `startedAt`, `renewsAt`, `provider`, `providerRef` | Server-side only; the client flag grants nothing |
| `leads` | `email`, `source`, `createdAt` | The pricing page capture before payment exists |
| `ingestionRuns` | `sourceId`, `startedAt`, `finishedAt`, `status`, `itemsSeen`, `itemsChanged`, `errors[]` | The freshness and health evidence for the owner page |
| `fxRates` | `base`, `quote`, `rate`, `observedAt`, `source` | The rate behind every EGP number, with its date |

**Money and numbers.** Every price is an integer in the smallest currency unit. Every converted number carries the rate and the observation time. A price older than two days is shown with a stale badge, and the lowest-ever flag is only computed from points we observed ourselves, with the store and the date shown.

**Access rules.** `pricePoints`, `priceHistory`, `games`, `stores` and `giveaways` are public reads with no personal data. `watchlists`, `alerts`, `wishlistImports`, `notifications` and `giveawayClaims` are owner-scoped. `subscriptions` and `leads` are server-only. `users` is owner-scoped with an admin role. Firestore rules deny by default and emulator tests must include a cross-user read that fails.

### 5.6 Data and money

- Firestore with deny-by-default rules, per-user claims, emulator tests including a cross-tenant read that must fail.
- The ingestion pipeline is a scheduled job, not a request handler: it runs at a round time, writes an `ingestionRuns` record, is idempotent on the same observation, and never overwrites a price point.
- A new lowest price is a transaction: write the point, then update the derived history, so two stores dropping at the same minute cannot produce two "lowest ever" flags.
- Alerts are queued, de-duplicated per user and per game inside a window, and rate limited. A user never receives the same offer twice in one window.
- Wallet and card payments through Paymob and Fawry in test mode. The webhook is HMAC-SHA256 signed with the timestamp inside the signed body, verification is server-side only, and tampered, replayed, unsigned and wrong-timestamp events are rejected.
- Price alerts for free users are capped at a published limit, and the Pro limit is higher. The cap is part of the pricing page, not a surprise.

### 5.7 Hosting and delivery

- **Firebase Hosting** is primary. **Vercel** is the second host, the same repository imported with the Vercel CLI, the same build, the same environment variables on both. Both addresses are curl-checked and written into the project checkpoint.
- Static hosting cannot run route handlers, so the cron ingestion, the AI proxy, the wishlist import and the notification sender live on the functions side, never in the client bundle.
- A service worker caches the watchlist, the last seen prices and the giveaway list with their countdowns. Background sync queues the writes when the connection returns.
- Daily Firestore export to a private bucket, a monthly restore test, a health endpoint at `/api/health`, a status JSON, a nightly error digest and a weekly Telegram report at a round hour.

### 5.8 Security baseline

Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI. A CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent, with Reject All as prominent as Accept. One-tap data export and one-tap deletion. Rate limits on auth, alerts, wishlist import, AI and webhook endpoints. No fake data in any path a user can see. A wishlist import never reads another user's account and never stores the user's store credentials: the token lives server-side, encrypted, and is deleted on unlink.

---

## 6. Premium quality bar

This is the floor from `D:/Projects/_SIR/standard/23-premium-code-bar.md` and `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`, written for this product.

**Motion, Apple level.**
- One shared spring config across the app: stiffness 300 to 400, damping 28 to 30, transform and opacity only, no layout thrashing, 120 Hz safe.
- Every sheet, drawer, modal and panel opens and closes with the same spring. An open-only animation is a defect.
- The price curve draws on first view with a spring, the lowest-ever flag lands with a short settle, and the giveaway countdown ticks without a layout jump. Micro-interactions 100 to 150 ms, standard 200 to 300 ms, large 300 to 500 ms. Press scale 0.98. Reduced-motion path for every animation.
- The active tab shows its label and the others show an icon only, the active tab scrolls into view on load and on change, and the bottom bar never vanishes when the keyboard opens.
- Skeletons match the final geometry, optimistic feedback lands under 100 ms, and no white flash on theme change.

**Two languages, one layout.**
- Egyptian Arabic first for players, English second for the international market, MSA only in legal pages. Both shipped together, never one as a partial translation.
- RTL designed first: logical CSS properties only, flipped directional icons, Arabic line heights, never a mirrored afterthought.
- Every text input detects Arabic or Latin per character as the user types and moves the caret and the direction live. Every mixed run is isolated with `<bdi>` or `unicode-bidi: isolate`. The words "RTL" and "LTR" never appear to the user.
- Currency auto-detected from the visitor locale and IP, with a manual override on top. Dates and times formatted with `Intl`, and the giveaway countdown uses the user's timezone.

**Five states on every screen.**
Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake deal, a fake game, a fake price or a fake countdown. A store that has no data yet says so with its last check time.

**Accessibility.**
WCAG 2.2 AA. Every control has an accessible name. Touch targets at least 44 px with no covered hit area. Full keyboard path on every screen, visible focus, zoom from 80 to 200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured, and a colour pair that passes contrast in light, dark, system and high-contrast themes. The lowest-ever flag and the stale badge are never colour alone; each carries a word and an icon.

**The look.**
One design system: tokens for colour, spacing on a 4 and 8 px grid, radii, shadows, type and motion. Seed colour a deep teal `#0F766E` for a price product with a dark neutral canvas, accent only for primary actions and key numbers, and a second accent reserved for the lowest-ever flag so it reads as a fact, not as marketing. No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. One component per control, never two. Arabic screen face: IBM Plex Sans Arabic, Cairo or Tajawal.

**Native app feel.**
The browser's text selection and the right-click menu are disabled site-wide and replaced by the app's own menu with in-app actions and a refresh. Normal select, copy and paste inside real input fields still work.

**Evidence before the word done.**
Screenshots at 320, 390, 768, 1280 and 1920 px, in Arabic and English, in light and dark, plus 3840 px once. Playwright on the critical journeys. Lighthouse mobile 90 or better. A click-target audit in CI. The self-audit loop runs until two clean cycles.

---

## 7. Free tier and fair pricing (EGP and USD)

These are **test prices**, not published prices. They are the outline the owner confirms with real players and the official gateway fee schedule before anything is charged. The USD column uses 48 EGP per 1 USD, which is "(unsourced, verify)" and is recomputed from the live rate on the pricing page. For context, the closest global comparable lists $5 per month and $24 per year on its own pricing page (read 2026-11-12), which is about 268 EGP per month and about 1,285 EGP per year at that rate, so our price sits below the category.

| Plan | Who | EGP | USD | What it includes | Rule |
|---|---|---|---|---|---|
| Free | Any player | 0 | 0 | The whole deals feed, every store we cover, price history curves, the lowest-ever flag, the free game tracker with the countdown, filters, up to 5 watchlist items, up to 10 alerts, email alerts, Arabic and English, export and deletion | Browsing, history and free games are never behind a plan |
| Pro monthly | A player who watches a list | 39 per month (test) | about 0.80 per month | Unlimited watchlist, unlimited alerts, Telegram and push alerts with quiet hours, wishlist auto import, price alerts on every store, the store trust tier view, the subscription tracker, the AI deal digest, CSV export | Cancel any time, the plan lapses at the end of the paid month |
| Pro yearly | The same player | 349 per year (test) | about 7.30 per year | Everything in Pro monthly, two months free, priority alerts | One click to cancel, the same rules |
| Lifetime | Decided with the owner later | not set | | | Not in v1, and only if the owner wants it |
| Owner | Ahmed | 0 | 0 | Every Pro permission inside the product, the owner console with every metric | Never charged |

**Fairness rules written into the product.**
1. A player never pays to see a price, a price history or a free game.
2. The free tier keeps working after the trial of any paid feature ends, with the same published limits.
3. Every price on screen is in the visitor's currency, auto-detected, with the original currency, the rate and the date next to it.
4. No ads, in any tier, ever. The ad spend cap is 0 until the owner changes it.
5. No urgency tricks: no fake countdowns, no fake "only 2 left" on a digital good, no fake low-stock lines on a deal.
6. The owner of the product gets every paid feature, free, and a subscription grants him all permissions inside the owner console.

**Still open and blocking publication:** the official Paymob and Fawry fee schedules for Egypt, the tax treatment of a subscription in Egypt, the exact cancellation and refund wording, the exchange rate source and the moment it is read, the terms of every store we call, and the lawyer review of every legal page. Each is tagged "(unsourced, verify)" in `ops/competitors/sir-game-deals.md` section 4 and in `docs/ENV.md` when the project starts.

---

## 8. Milestones M0 to M6, with acceptance tests

Every exit check is something a reviewer can run or click. "Green" means the output was seen, not assumed.

### M0: Foundations, the kit and the honest map of the market

Work: create the product folder `D:\Projects\SIR Game Deals` with the `.sir` file set (CHECKPOINT, PLAN, TASKS, PREMIUM, PLAN_REFRESH), an `AGENTS.md` that points at the workspace laws, and a `folder.ico` named exactly that (never `icon.ico`, never under `assets/brand`); create the GitHub repo `sirahmed8/sir-game-deals` (private) as the only remote and the Firebase project `sir-game-deals` on the free Spark plan; recreate the Desktop folder kit from scratch for this new build; scaffold the monorepo (apps, packages, docs, scripts) with strict TypeScript, Tailwind v4 tokens, RTL-first styles and the shared `verify` script; design the token set; write `docs/DATA_SOURCES.md` with every source, its terms status and its last-checked date.

Exit checks:
1. `D:\Projects\SIR Game Deals` exists with the `.sir` set, `AGENTS.md` and `folder.ico`; the Desktop folder `SIR Projects/SIR Game Deals` holds `folder.ico`, `SIR Games.lnk` (web links for both hosts), `Start SIR Game Deals dev.lnk`, `Stop SIR Game Deals dev.lnk`, `Windows app.lnk` and `Android APK.lnk` where those exist, `Open project folder.lnk`, and `Versions.txt` reading version 1.0.0 and a plain status.
2. `pnpm verify` runs typecheck, lint, tests, build and gitleaks, and the output was seen green.
3. The Firebase project `sir-game-deals` exists and the repo `sirahmed8/sir-game-deals` is its only remote; the app id is in `.firebaserc` and every key is in an ignored env file.
4. `docs/DESIGN.md` holds the explored directions with screenshots and the chosen one, plus the token file.
5. `docs/DATA_SOURCES.md` lists every source with its licence, its terms status and its last-checked date, and the source probe script output is pasted into the report.

### M1: The price data core, proven under real data

Work: the data model and the Firestore rules for Game, Store, Offer, PricePoint, PriceHistory and FxRate; the scheduled ingestion pipeline for the sources cleared in M0 with an `ingestionRuns` record per run; the price history engine and the lowest-ever calculation; the freshness rule and the currency conversion with the rate and its date.

Exit checks:
1. The emulator rules tests pass, including a cross-user read that must fail.
2. A live ingestion run produces real `pricePoints` from at least two cleared sources, and the report shows the run record with the item counts.
3. A game that has been observed at two different prices shows a history curve with two real points, and the lowest-ever flag names the store and the date.
4. The same game queried with the Egypt region shows the dollar price and the converted pound price with the rate and the date on screen, and the source is named.
5. A stale price (older than two days) shows the stale badge, and the count of stale offers is visible on the owner source health panel.

### M2: The browse experience

Work: the deals feed with the filters and the sorts; the game detail page with the history curve, the lowest-ever flag, every store offer with its region, activation type and trust tier; the free game list with the end time; the five states everywhere; Arabic Egyptian first.

Exit checks:
1. The feed, the detail page and the free game list each show idle, loading skeleton, empty with one action, error with retry and populated, at 390 px and 1280 px, in Arabic and English, in light and dark.
2. Every offer on screen shows the price in the visitor's currency, the original currency, the rate used and the time it was seen.
3. A store with a trust tier below the top shows its tier badge and its region warning.
4. Screenshots exist at 320, 390, 768, 1280 and 1920 px in both languages and in light and dark, with no horizontal overflow and no clipped text.
5. No fake game, price, discount or countdown appears anywhere in the app, including the empty states.

### M3: Watchlists, wishlist import and alerts

Work: the watchlist with a target price; the Steam wishlist import from the user's own account; the alert engine (price below, any discount, giveaway start, giveaway ending) with quiet hours; the Telegram bot link (one bot for the product, each user links their own account); email and push channels; the rate limits and the de-duplication window.

Exit checks:
1. A user imports their own Steam wishlist and the games appear on the watchlist; the import never reads another user's account and the stored token is deleted on unlink.
2. A price that crosses a user's target price sends exactly one alert inside the window and none on a repeat of the same offer.
3. Quiet hours suppress a non-critical alert and the test proves it.
4. The Telegram link flow has the five states (not linked, linking, linked, syncing, failed with retry), a wrong chat id is ignored and an unapproved destructive command is refused.
5. The free tier limits (5 watchlist items, 10 alerts) are enforced on the server, not only in the client, and the pricing page states them.

### M4: Free games tracker and the two mobile apps

Work: the giveaway ingestion from the cleared free game sources; the free game page with the claim link, the end time and the region eligibility; the claim reminder before the window closes; the Expo app for Android and iOS with the same account, the offline last-seen prices and the local notifications.

Exit checks:
1. The free game list shows real giveaways from the cleared sources with the end time, and a giveaway that ends shows a countdown that reaches zero and then marks it as ended rather than counting below zero.
2. A reminder is sent before the end time, once per giveaway, and the delivery is recorded.
3. The Android APK builds and installs on a device, and the same Google account sees the same watchlist on the web app.
4. The app works offline with the last seen prices and the watchlist, and the background sync queues the writes when the connection returns.

### M5: Owner console, pricing, legal, the two hosts and the desktop shells

Work: the owner-only analytics page with the source health panel; the pricing page with the test prices, the currency auto-detect and the lead capture; the signed webhook with negative tests; the legal pack; dual hosting; the Windows, macOS and Linux builds; the full self-audit.

Exit checks:
1. A non-owner token on `/owner` gets 403 and a forged token gets 403, and every metric on the page comes from an aggregate with a real value or a dash with a reason.
2. The pricing page shows the test prices with the currency auto-detected, plus "Subscriptions launching soon" and an email capture that creates a lead document and rejects an invalid address.
3. Ten negative webhook tests pass (tampered, replayed, unsigned, wrong timestamp and the rest) and no bypass exists in the code.
4. Every legal page exists under `/legal/*`, each marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch".
5. Both hosts answer: the Firebase URL and the Vercel URL were curl-checked, and the two addresses are written in the project checkpoint.
6. The Windows, macOS and Linux builds come from one shell and one release feed, the installable PWA is signed in with the same Google account, and the Download page shows the version and the size.
7. The accessibility audit passes WCAG 2.2 AA and Lighthouse mobile is 90 or better, with the JSON saved in `.sir/evidence/`.

### M6: Release, the market layer and the AI layer

Work: the launch package (domain, accounts, legal review); the AI deal digest with the fallback chain and the Arabic and English eval sets; the store listings for the mobile apps; the first real store partnerships; the keys rotated; the old hosts redirected.

Exit checks:
1. The AI eval runner passes with the Arabic and English sets, and the support assistant refuses an ungrounded question.
2. A deal digest for a real watchlist contains no price that is not in the database.
3. Store metadata and screenshots are drafted and truthful, and nothing is submitted without the owner.
4. The 301 redirects from any old hosts are verified by curl, and the legacy keys are rotated.
5. At least three stores are live from cleared sources with a named trust tier and a last-checked date, and the owner source health panel shows them green.
6. The lawyer has reviewed the legal pages before any paid plan goes live.

---

## 9. The first ten tasks for the free agents

Ready to queue, each with its own brief: `D:/Projects/_SIR/ops/briefs/sir-game-deals-tasks.md`.

1. The M0 kit: project folder, `.sir` set, `AGENTS.md`, `folder.ico`, the GitHub repo, the Firebase project, the Desktop folder kit and the verify script.
2. The data source ledger and the source probes, with the terms status of every source.
3. The monorepo scaffold with the design tokens, the RTL shell, the health route and CI.
4. The product's own Firebase project and the `owner-auth` package with negative tests.
5. The data model, the Firestore rules and the emulator tests.
6. The scheduled ingestion pipeline, the price history engine and the lowest-ever calculation.
7. The deals feed, the game detail page with the history curve and the five states.
8. The watchlist, the Steam wishlist import, the alert engine and the Telegram bot link.
9. The free game tracker, the countdown and the claim reminder.
10. The owner analytics page with the source health panel, the pricing page, the legal pack and the two hosts.

---

## 10. Skills from the library that this build uses

Picked from `D:/Projects/_SIR/ops/SKILLS_INDEX.md` and the digests in `D:/Projects/_SIR/ops/encyclopedia/`. Digests live under `ops/encyclopedia/<tool>/<skill>.md`; the paths below are the real files found on 2026-11-12.

**Design and UI**
- `anti-vibecoded-design-system` (claude) - keeps the price product away from generic AI styling and purple gradients.
- `taste-design-engine` (claude) - the self-audit against AI patterns before the screens ship.
- `emil-motion-impeccable` (claude) - the spring physics for the sheets, the tab bar and the price curve draw.
- `modern-ui-ux-design-system` (claude) - tokens, micro-interactions and hierarchy for one design system.
- `cognitive-product-intuition` (claude) - the deal card and the alert flow step order and the empty states.
- `high-conversion-copywriting` (claude) - the promise line and the deal copy that sell the end state without hype.
- `commercial-app-blueprint` (claude) - llms.txt, the trust signals and the sticky call to action on the site.
- `a11y-debugging` (codex) - the accessibility audit with Chrome DevTools against WCAG 2.2 AA.
- `mobile-ergonomics-polish` (claude) - touch targets, no horizontal scroll and tap feedback on the phone screens.
- `modern-web-guidance` (claude) - the current web APIs, container queries and dialog behaviour, run before any client-side work.
- `react-best-practices` (claude) and `nextjs` (claude) - App Router structure, Server Components, rendering and performance rules.

**Data and price correctness**
- `database-reliability-transactions` (claude) - the atomic lowest-ever write and the idempotent ingestion.
- `firebase_firestore` (claude) - queries, indexes and the data model.
- `production-engineering-standards` (claude) and `system-design-architect` (claude) - the zero-mock persistence and the ingestion shape.
- `mimic-api-extractor` (claude) - when a store has a public endpoint worth wrapping properly.

**Security and legal**
- `firestore_rules_creation` (claude) - the deny-by-default rules for every collection.
- `firebase_security_rules_auditor` (claude) - the audit that finds a cross-user read before a user does.
- `zero-trust-security-hardening` (claude) - server-side role checks, secure cookies and rate limiting.
- `owasp-vulnerability-shield` (claude) - the OWASP pass over the webhooks, the imports and the auth.
- `vibe-auth-hardening` (claude) - the five auth flaws that a fast build introduces.
- `legal-compliance-shield` (claude) - the legal pack that matches what is actually collected, including PDPL 151/2020.
- `cookie-debugging` (codex) - the consent banner behaviour and the cookie audit.

**Mobile and desktop**
- `modern-app-engineering` (claude) - the shared architecture for the Expo app and the desktop shell.
- `android-cli` (claude) and `device-hub` (codex) - the Android build, the emulator and the device checks.

**AI**
- `gemini-api-dev` (codex) - the Gemini calls and the structured output.
- `ai-gateway` (codex) and `omniroute-resilience-gateway` (claude) - the fallback chain and the failover on quota errors.

**Automation and operations**
- `chat-sdk` (codex) - the Telegram bot for the alerts and the weekly report.
- `bot` architecture from `plans/BOT_ARCHITECTURE.md` - one bot for the product, every user links their own account.
- `verification` (codex) and `verification-before-completion` (deep) - the end-to-end check before the word done.

**Hosting and growth**
- `firebase_hosting_basics` (claude), `vercel-cli` (codex), `deployments-cicd` (codex) and `env-vars` (codex) - the two hosts with the same build and the same variables.
- `open-seo-auditor` (claude) - Arabic search visibility, JSON-LD and the AI answer check.
- `pc-storage-guardian` (claude) - disk hygiene for the growing price point archive.

---

## 11. Risks and the defaults we take

- **Price data that goes stale.** Default: every price shows its observation time, the freshness rule is two days, a stale price carries a badge, and the owner source health panel goes red when a source stops.
- **Store terms.** Default: a source enters the pipeline only after its terms status is written in `docs/DATA_SOURCES.md`; no scraping of a store that forbids it, no copy of a community price database, and our history comes only from what we observed ourselves.
- **The region and activation trap.** Default: every offer shows the region the key unlocks and the activation type, key shops sit in a lower trust tier, and the product never sells a key.
- **The free game feed is volatile.** Default: a giveaway we can no longer see is marked as unverified instead of being hidden, and the reminder is sent once.
- **A crowded global market.** Default: we win on Egypt and the Arab market, on Arabic Egyptian copy, on EGP and on wallet payment, and on the one thing nobody joins: the discount and the free game in one list.
- **Payments before the lawyer.** Default: test mode only, no real charge, no published plan price until the fee schedule and the legal pages are reviewed.
- **Static export killing the server.** Default: no secret ever in a route handler that a static host would drop; the ingestion, the alerts and the AI proxy run on the functions side from M1.

---

## 12. Only the owner can do

Buy the domain and point it at both hosts. Create and fund the Paymob and Fawry business accounts and paste the keys into the project's ignored env file. Sign in once on the Google OAuth screen so the branding is right. Approve the pricing test prices after checking them with three real players. Lawyer and accountant. Buy the code-signing certificate later. Create the Play Console and Apple developer accounts when the reinvestment ladder allows. Apply for the store affiliate and partner programmes that need a company, and sign the agreements.

Everything else is an agent's job.

---

## 13. Sources and files

- Canonical competitor study with dated links: `D:/Projects/_SIR/ops/competitors/sir-game-deals.md`
- The ten build briefs: `D:/Projects/_SIR/ops/briefs/sir-game-deals-tasks.md`
- Shared kit: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`
- AI chain: `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`
- Quality charter: `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`
- Desktop and Windows standard: `D:/Projects/_SIR/plans/WINDOWS_APP_STANDARD.md`
- Product direction: `D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md`
- Legacy source and notes: `D:/Projects/_SIR/plans/sir-deals.md` (r51, superseded) and the TickTick "أفكار برامج ومشاريع" idea 16
- Owner ideas map: `D:/Projects/_SIR/ops/TICKTICK_MAP.md` and `D:/Projects/_SIR/plans/PROJECT_MERGE_RECORD.md`
