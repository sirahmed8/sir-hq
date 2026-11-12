# Backlog ideas: the decision for every unplanned idea (round r53c, 2026-11-12)

Source of the ideas: the owner's TickTick note "أفكار برامج ومشاريع" (30 ideas), mapped into the portfolio in `D:/Projects/_SIR/ops/TICKTICK_MAP.md` (2026-10-29) and `D:/Projects/_SIR/plans/PROJECT_MERGE_RECORD.md`. The note text itself is not copied into this repository, only its mapping, so the wording of each idea below is the scope line from the round brief for that project (`D:/Projects/_SIR/ops/briefs/r54-plan-sir-*.md`, 2026-11-12), not a quotation of the owner's private note.

The question the owner asked (`D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md` section 5): for each idea that was never planned, decide whether it is a module of an existing product or its own project with the same premium standard, its own plan, its own tasks, its own Desktop folder and its own TickTick parent task.

**Truth rule for this file.** Nothing here was built, deployed or tested. Every market fact below is either taken from a file in this repository that says where it came from, or tagged "(unsourced, verify)". No price, revenue number, user count or review of any competitor is stated as fact. Nothing in this file is called working.

---

## 1. The decision table

| Idea | The idea (plain words) | Decision | Home | One-line reason |
|---|---|---|---|---|
| 15 | Price finder: compare the price of any product across stores, warn me when it drops | **Own project** | `plans/sir-price-finder.md` | The customer, the data and the moment are a purchase, not a booking, so retailer feeds never enter the venue product |
| 16 | Game-deal finder: game discounts and free games across stores | **Own project** | `plans/sir-game-deals.md` | Publisher price feeds have their own currency, their own freshness and their own audience, so it is a separate product that reuses the shared price engine |
| 23 | Cars: buy, sell, compare and track cars | **Own project** | `plans/sir-cars.md` | It is a listings marketplace with price history and inspection partners, a different business from booking a court |
| 26 | Accessibility map: which places are usable by people with disabilities, users add and confirm entries | **Own project, built last** | `plans/sir-access-map.md` | The owner decided every unplanned idea is its own project, and crowd-sourced place claims with photo evidence are a moderation product, not a personal routine feature |
| 28 | Handyman: on-demand home services, the nearest worker accepts, live tracking, rating, payment later | **Own project** | `plans/sir-handyman.md` | The supply side is individual craftsmen with their own availability and quotes, so the entities, the economics and the legal duties are not a court slot |
| 29 | Movies: discover films, track what you watched, find where to watch in Egypt | **Own project** | `plans/sir-movies.md` | Entertainment tracking and where-to-watch have no customer, data or daily habit in common with any other SIR product |
| 14 | Citizens program | **Dropped** | none | Government scope: it needs a state contract, identity verification at scale and procurement we cannot carry |
| 21 | Face rating | **Dropped** | none | Face templates are special category personal data under Egypt's PDPL 151/2020, and the risk is far larger than the value |

**What stays a module (for contrast, not up for decision).** The position coach (idea 30) is a module of SIR Hagoozat: it is a booked slot for a service provider at a booked time, paid in the same basket, rated the same way. That decision is written in `plans/sir-hagoozat.md` section 3.4 and is not changed by this file.

**Old notes that this file supersedes.** `plans/accessibility-map-module-note.md` made the accessibility map a module of SIR Life Part B. The owner's later message (direction file section 8) turns every unplanned idea into its own project, so that note is superseded and `plans/sir-access-map.md` replaces it. The old notes `plans/sir-cars.md`, `plans/sir-deals.md`, `plans/sir-handyman.md` and `plans/sir-movies.md` were thin first drafts; each was rewritten as a premium plan on 2026-11-12 (see section 6 for who wrote what and when).

---

## 2. The rule that produced these decisions

The same rule the owner wrote for the booking family (`plans/sir-hagoozat.md` section 3.4), applied to every idea here:

> A thing is a **module of an existing product** when the customer, the paid object, the calendar and the rating are the same objects as that product already has. A thing is its **own project** when the customer, the data or the daily habit is different, and the honest cost of merging would be paid by both products.

Three checks were applied in order:

1. **Same customer?** The buyer of a phone in a shop is not the amateur footballer booking a court. If the customer changes, the onboarding, the notifications and the retention story change with it.
2. **Same paid object?** A slot with a price per period, a deposit and a split bill is a Hagoozat object. A product price, a car, a job quote, a cinema ticket and a place accessibility record are not.
3. **Same day?** A booking is a weekly habit. A price check is a monthly event. A car purchase happens twice in a lifetime. A movie is a night.

The rule exists to keep each product honest, not to keep the portfolio small: the owner asked on 2026-11-12 for small focused projects, each with the same premium standard, its own plan, its own folder, its own Desktop kit and its own TickTick parent task.

---

## 3. The decision for each idea

### 3.1 SIR Price Finder (idea 15)

**What it is.** The user searches for a product, sees what the Egyptian stores actually charge right now, watches the price, and gets a warning when it drops. Egypt first: Amazon.eg, Noon, Jumia and local stores, then the global stores.

**Why its own project.** The customer buys things, the data is retailer catalogues and prices, and the moment is the moment of purchase. Nothing in the pitch-booking product needs a price feed. Putting retailer feeds and affiliate links inside the venue product would damage the trust of both sides: a player would see ads next to the pitch list, and a venue owner would see marketplace noise next to the booking console.

**The hard gate, stated honestly.** There is no build without at least one lawful price source, confirmed in writing. The candidate sources, all of which need an application or an agreement:

- Jumia Egypt affiliate programme (product search and price feed).
- Noon affiliate feed.
- Amazon Product Advertising API, where the Egyptian market is served (availability checked again before the build, it was not open for Egypt on 2026-11-12 according to the first planning note, "(unsourced, verify)").
- A direct data-sharing agreement with one Egyptian retailer.
- A licensed price-aggregator feed whose terms permit the use we intend.
- User-submitted price reports, each with a timestamp, a store name and a photo, used as a supplement and never as the only source.

**Not allowed:** scraping a store's pages or its API against its terms. The first planning note cited Egyptian law on unauthorised data collection (Computer Crimes Law 175/2018); that citation is carried over from the 2026-11-12 r51 note and is tagged "(unsourced, verify)" until a lawyer or the official text is read.

**Product rules written into the plan.** Every price carries the store, the time it was checked and the link to the store. Fake discount detection is honest: a "was" price is only shown when a real earlier price was recorded by us. Affiliate links are disclosed. No invented prices, no invented reviews, no invented stock.

### 3.2 SIR Game Deals (idea 16)

**What it is.** The games a person owns or wants, the price of each one in every store, the free games that are actually free this week, and one place to see the whole list.

**Why its own project, even though it looks like the price finder.** The data is different: publisher and platform price feeds, region locks, own-licence keys, free-to-keep promotions, and a currency that is usually not the EGP the shopper thinks in. The buyer is a gamer with a wishlist of titles. If the two lived in one product, the price finder would carry Steam and PlayStation vocabulary and the game product would carry supermarket vocabulary, and both would be worse for their own user.

**What is shared.** The comparison engine (fetch, normalise, timestamp, cache, history, alert) belongs in the shared kit (`plans/SHARED_PLATFORM_KIT.md`) and is used by both products. Two products, one engine. No shared database, no shared account, no shared repo.

**The gate.** The same lawful sources rule applies, plus one extra: a free game that we cannot verify with the store is not published. Steam and the console stores expose price information for the products we sell nothing of; each store's own terms and any store API that requires a key are read before the feed is used.

### 3.3 SIR Cars (idea 23)

**What it is.** A trustworthy car marketplace for Egypt: real listings with real photos, a price history for each model, a booking for an inspection, and a maintenance tracker for the owner of a car.

**Why its own project.** A car is not a slot. The product needs seller identity, phone verification, a listing lifecycle, a price history per model and per year, inspection partners and the legal duty that follows a private phone number (PDPL 151/2020). None of that exists in any SIR product, and none of it belongs to a pitch booking app.

**Lawful data.** No scraping of Hatla2ee, OLX or any other marketplace. Listings are submitted by their owners. Benchmark numbers come from public official sources, and each one is tagged with its date and its publisher. An inspection referral needs a signed agreement with the inspection company, so the referral is a link and a partner agreement, not a copy of their report.

### 3.4 SIR Access Map (idea 26)

**What it is.** A map of places that shows how usable they are for people with disabilities: a ramp, a lift, an accessible toilet, a parking space, braille or audio help, quiet hours. Users add a place, users confirm it, the owner of the place can claim the entry and correct it.

**Why its own project (and the honest counter-argument).** The earlier note (2026-11-12, r51) made this a module of SIR Life Part B, and its reason was sound: the market is small, accessibility maps rarely earn money on their own, and the map layer would be shared with the other SIR Life location features. The owner then decided that every unplanned idea is its own small project with the same premium standard, and that is the decision that stands.

**What the cost of that decision is, stated plainly.** A separate project means a separate Firebase project, a separate repository, a separate domain and a separate store listing for a small audience. To keep that cost honest, the Access Map plan reuses the shared kit map layer and the shared map provider account, and it is built **last**, after the other small projects. The owner may drop it at any time without touching another product, because nothing else depends on it.

**Rules.** A place is not published from one untested report: it needs a photo, a feature list and a confirmation from a second user or a claim by the place owner. The submitter is never named publicly. Accessibility information about a place is a factual claim about a physical place, so it carries a date and an expiry for the parts that change (a lift that is out of service).

### 3.5 SIR Handyman (idea 28)

**What it is.** The owner of a home describes the job, chooses a time, sees a fixed price or a quote, and follows the worker to the door. The worker accepts nearby jobs, gets rated and is paid.

**Why its own project (and the honest counter-argument).** This is the idea that most looks like a Hagoozat module: it has a slot, a price, a payment, a rating and a customer. The counter-argument is real, and the plan keeps it: Hagoozat already has a slot engine with holds, idempotency keys, split payment, a QR pass and ratings, and a "visit slot" model would reuse it.

**Why it is still its own project.** The supply side is the difference. A pitch has a fixed set of slots, a published price per period and a venue that owns the whole facility; a craftsman has his own day, his own tools, his own travel radius, and a job whose price is a quote rather than a slot price. The acceptance criteria differ (the work is done and the price agreed), the legal duties differ (who is liable for damage, insurance, the craftsman's identity check), and the customer of the two products never overlaps. Merging them would put a quote flow inside a court-slot flow and make both harder to reason about.

**What the decision costs.** The slot engine ideas stay in the shared kit, so if the handyman product later wants a visit-slot model, it imports the same tested component instead of writing a second one. The two products share no account and no data.

**Rules.** No fake craftsmen, no fake ratings, no shill reviews: a rating requires a completed job reference. The craftsman's identity check result is a pass or fail flag, never a copy of the identity document. The homeowner's address is shared with the worker only after a confirmed booking, and it is deleted from the active store after the retention window. Payment stays in test mode until the merchant account and the legal pages exist.

### 3.6 SIR Movies (idea 29)

**What it is.** Find a film, see what it is really about, keep a watchlist, mark what was watched, and find where to watch it in Egypt, on a streaming service or in a cinema.

**Why its own project.** The daily habit of an entertainment tracker (what to watch tonight, what was on that list) has no customer, no data and no notification in common with a pitch booking, a car marketplace or a price finder. It also has the cleanest legal position of the six ideas, because the data has proper owners: a film metadata API with attribution rules, and a cinema schedule that needs a written agreement with the chain.

**Lawful content.** Only legal streaming services are listed. No links to pirated content and no clone of the sites that provide them. Film metadata and images come from the licensed API and are served through its CDN with the required attribution. Cinema showings appear only with the chain's permission or from a licensed feed. User review text is never copied from another site; the product's own ratings are the user's own.

### 3.7 The two that stay dropped

**Idea 14, citizens program.** Dropped on 2026-11-12 and it stays dropped: it needs a government contract, identity verification at a scale the company cannot carry, and procurement we do not do. No plan, no folder, no task.

**Idea 21, face rating.** Dropped on 2026-11-12 and it stays dropped: a face template is special category personal data under Egypt's PDPL 151/2020, it needs an explicit legal basis and a data protection impact assessment, and the product value is small next to that risk. No biometric matching, no face scoring, no upload of a face photo for any purpose in any SIR product. If the owner ever asks again, the answer is the same until a lawyer says otherwise in writing.

---

## 4. Rules that apply to every finder (price finder, game deals)

These are the laws-of-the-product rules, and they are the reason the two finders are planned behind a data gate rather than built immediately:

1. **A price is only shown with its source, its store and the minute it was checked.** A stale price is a stale price, and the screen says so.
2. **No source without permission.** An official API, an affiliate feed, a signed agreement, or a licence that permits our use. Nothing else.
3. **No scraping that breaks a site's terms, and no scraping of a site that forbids it in its robots or terms file.** The plan names the licence for every feed it uses.
4. **The user can always leave for the store with one tap**, and the affiliate relationship is disclosed on the page.
5. **A discount is only a discount when we recorded the earlier price ourselves.** A crossed-out number with no history behind it is not shown.
6. **Alerts are opt-in, rate-limited and deletable**, and the free tier caps the number of watched items so the free tier stays usable for everyone.
7. **When no lawful feed is available for a category, that category is empty with one action** ("tell us when a store joins"), never full of invented prices.

---

## 5. The exact folders and files HQ creates next

HQ creates the folders in this order. No folder is created by this round, by design: the r54 rounds write the plans first, then M0 of each project creates its own folder, its own repository and its own Desktop kit.

| Product | Folder (exact name) | Private repository | Firebase project (Spark) | Desktop folder | Plan | Competitors | First 10 tasks |
|---|---|---|---|---|---|---|---|
| SIR Price Finder | `D:\Projects\SIR Price Finder` | `sirahmed8/sir-price-finder` | `sir-price-finder` | `Desktop\SIR Projects\SIR Price Finder` | `plans/sir-price-finder.md` | `ops/competitors/sir-price-finder.md` | `ops/briefs/sir-price-finder-tasks.md` |
| SIR Game Deals | `D:\Projects\SIR Game Deals` | `sirahmed8/sir-game-deals` | `sir-game-deals` | `Desktop\SIR Projects\SIR Game Deals` | `plans/sir-game-deals.md` | `ops/competitors/sir-game-deals.md` | `ops/briefs/sir-game-deals-tasks.md` |
| SIR Cars | `D:\Projects\SIR Cars` | `sirahmed8/sir-cars` | `sir-cars` | `Desktop\SIR Projects\SIR Cars` | `plans/sir-cars.md` | `ops/competitors/sir-cars.md` | `ops/briefs/sir-cars-tasks.md` |
| SIR Handyman | `D:\Projects\SIR Handyman` | `sirahmed8/sir-handyman` | `sir-handyman` | `Desktop\SIR Projects\SIR Handyman` | `plans/sir-handyman.md` | `ops/competitors/sir-handyman.md` | `ops/briefs/sir-handyman-tasks.md` |
| SIR Movies | `D:\Projects\SIR Movies` | `sirahmed8/sir-movies` | `sir-movies` | `Desktop\SIR Projects\SIR Movies` | `plans/sir-movies.md` | `ops/competitors/sir-movies.md` | `ops/briefs/sir-movies-tasks.md` |
| SIR Access Map | `D:\Projects\SIR Access Map` | `sirahmed8/sir-access-map` | `sir-access-map` | `Desktop\SIR Projects\SIR Access Map` | `plans/sir-access-map.md` | `ops/competitors/sir-access-map.md` | `ops/briefs/sir-access-map-tasks.md` |

One-line description of each product, for the folder, the repo description and the TickTick parent task:

- **SIR Price Finder:** compare what a product costs in the Egyptian stores right now, watch it, and get told when the price drops.
- **SIR Game Deals:** every game price across the stores, plus the games that are genuinely free this week, in one list.
- **SIR Cars:** buy, sell and compare cars in Egypt with real listings, a price history and inspection booking.
- **SIR Handyman:** book a trusted craftsman near you for a home job, track the visit and pay after it is done.
- **SIR Movies:** find a film, track what you watched, and see where it is showing in Egypt.
- **SIR Access Map:** a crowd-checked map of the places that are really usable for people with disabilities, with photo evidence.

Each folder is created with `.sir/`, its own `AGENTS.md`, `folder.ico` in the project root (named exactly that), the Desktop kit of OWNER_DEFAULTS item 19, a TickTick parent task, and its own repository named exactly after the product. No product reuses another product's Firebase project or repository.

---

## 6. Build order, dependencies and what each project owes the others

**Order of the build:** SIR Price Finder and SIR Game Deals first (smallest, one shared engine, the data gate can be worked in parallel with the build), then SIR Cars, then SIR Movies, then SIR Handyman, and SIR Access Map last. The order is not a value judgement on the ideas; it is the order in which the external dependencies arrive.

**What each project depends on, and what it gives back to the shared kit:**

| Project | Depends on | Gives back to the kit |
|---|---|---|
| SIR Price Finder | A lawful price source (affiliate or agreement) | The price comparison engine: fetch, normalise, timestamp, cache, history, alert |
| SIR Game Deals | The same engine, plus a game price feed | The same engine extended for region and currency, and the free-game promotion model |
| SIR Cars | Inspection and data partners | A listing lifecycle model with a price history per model |
| SIR Movies | A film metadata key, a cinema agreement | A watchlist and where-to-watch model |
| SIR Handyman | A craftsman identity check provider | A quote-based booking model and the wallet and payout pattern |
| SIR Access Map | Nothing (build last) | A place-claim and evidence model |

**Every one of the six also owes the standard**: owner-only analytics page, an Arabic and English interface with RTL first, all platforms in the matrix with a written reason for every skipped one, a free tier with fair EGP and USD pricing, M0 to M6 with acceptance tests, an owner-only admin, and no fake data in any path a user can see.

**Owner-only actions** (these stay with the owner, the agent does everything around them):

- Apply for the affiliate and developer programmes (Jumia, Noon, the film metadata API, the cinema chain contact, the inspection company, the identity check provider).
- Buy the domains when the owner chooses to.
- Create the business payment accounts when a product is ready to take money.

---

## 7. Files read for this decision

- `D:/Projects/AGENTS.md`, `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/_SIR/standard/OWNER_DEFAULTS.md`, `D:/Projects/_SIR/standard/23-premium-code-bar.md`
- `D:/Projects/_SIR/ops/LESSONS.md`, `D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md` (sections 4, 5 and 8), `D:/Projects/_SIR/plans/PROJECT_MERGE_RECORD.md`
- `D:/Projects/_SIR/ops/TICKTICK_MAP.md` (the 30 ideas mapping and the two dropped ones)
- `D:/Projects/_SIR/plans/sir-hagoozat.md` (the booking family rule, section 3.4) and `D:/Projects/_SIR/ops/competitors/sir-hagoozat.md`
- The first planning notes of the six ideas: `plans/sir-cars.md`, `plans/sir-deals.md`, `plans/sir-handyman.md`, `plans/sir-movies.md`, `plans/accessibility-map-module-note.md` (all written 2026-11-12 by round r51)
- The per-project briefs written by HQ on 2026-11-12: `D:/Projects/_SIR/ops/briefs/r54-plan-sir-price-finder.md`, `r54-plan-sir-game-deals.md`, `r54-plan-sir-cars.md`, `r54-plan-sir-handyman.md`, `r54-plan-sir-movies.md`, `r54-plan-sir-access-map.md`

The AHome folder was never opened. The TickTick note "Accounts" was never opened. Nothing private from the owner was copied into this file.

---

## 8. Status of the six plans (read this before working on any of them)

| Project | Plan file | Competitors file | Tasks file | Written by | Verified by this round |
|---|---|---|---|---|---|
| SIR Price Finder | `plans/sir-price-finder.md` | `ops/competitors/sir-price-finder.md` | `ops/briefs/sir-price-finder-tasks.md` | round r54 (HQ brief) | see section 8 note below |
| SIR Game Deals | `plans/sir-game-deals.md` | `ops/competitors/sir-game-deals.md` | `ops/briefs/sir-game-deals-tasks.md` | round r54 (HQ brief) | see section 8 note below |
| SIR Cars | `plans/sir-cars.md` | `ops/competitors/sir-cars.md` | `ops/briefs/sir-cars-tasks.md` | round r54 (HQ brief) | see section 8 note below |
| SIR Handyman | `plans/sir-handyman.md` | `ops/competitors/sir-handyman.md` | `ops/briefs/sir-handyman-tasks.md` | round r54 (HQ brief) | see section 8 note below |
| SIR Movies | `plans/sir-movies.md` | `ops/competitors/sir-movies.md` | `ops/briefs/sir-movies-tasks.md` | round r54 (HQ brief) | see section 8 note below |
| SIR Access Map | `plans/sir-access-map.md` | `ops/competitors/sir-access-map.md` | `ops/briefs/sir-access-map-tasks.md` | round r54 (HQ brief) | see section 8 note below |

**Note on who writes what.** The decision file (this file) and the SIR Hagoozat merged plan are the work of round r53c. The six premium plans, their competitor files and their task files are the work of the six r54 rounds that HQ queued at 18:17 on 2026-11-12, one round per project, so that each plan is researched and written by its own round without two rounds writing the same file. This file is the contract those six rounds answer to: the decision, the reason, the lawful-data rules and the folder names are already fixed here, so a plan that disagrees with this file has to change, not this file.

Each of the six rounds must still produce a plan that meets the house structure (`D:/Projects/_SIR/ops/briefs/r52-product-premium-plan.md`): the promise, the ten competitors with dated sources, the features, the platform matrix, the architecture on the shared kit, the premium quality bar, the free tier and the EGP and USD pricing, M0 to M6 with acceptance tests, and the first ten tasks ready to queue.

**Open and honest:** none of the six products exists as a folder, a repository, a Firebase project or a line of code. The only thing that exists today is a plan per product. M0 of each product creates the folder, the repository and the Desktop kit.
