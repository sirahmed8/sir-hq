# PLAN: SIR Hagoozat (Wave 5, GLOBAL product, rebuild from zero)

## Vision (owner, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` section 4)

SIR Hagoozat takes the whole booking family: football pitch booking and every other booking idea, such as a position coach, other service bookings and handymen (section 5 of the direction file). Each idea is decided one by one: a module of Hagoozat if it is a booking, a separate project if it is a different product. Every module meets the same premium standard.

- The decision for every booking idea is done in this round and written in section 3.4 below: every idea is marked "module of SIR Hagoozat" or "separate product", with the reason in one line.

**Version 1.0.0.** Audited and rewritten 2026-11-12 (round r52, HQ). Extended the same day by rounds r53c and r61: r61 added the second research pass (Yalla Hagz's 2026 rebuild, Kourtiva's published AED pricing, Courty and Tahgzly, sourced Paymob/Maps/WhatsApp rates, PDPL Executive Regulations), the parity rows for Kickoffs, Team Fillups, Squads, waitlist, weather voucher, WhatsApp updates and the owner AI assistant, the Firestore data model (5.5.2), the API surface (5.9), the PDPL and payment-rail gates (5.10), the open-questions table (11.1), the launch and marketing phases (12), and the task list grew to 50 in `D:/Projects/_SIR/ops/briefs/sir-hagoozat-tasks.md`. Supersedes the r44 text of this file, which the git history keeps. Extended the same day by round r53c: the two sides side by side (3.5), the payments readiness ladder (5.5.1), the calendar, notifications and reviews rules (5.8), and the final decision for every unplanned idea, which now lives in `D:/Projects/_SIR/plans/BACKLOG_IDEAS_DECISIONS.md`. The canonical competitor study is `D:/Projects/_SIR/ops/competitors/sir-hagoozat.md` (opened sources dated 2026-11-12). The first ten build tasks for the free agents are in `D:/Projects/_SIR/ops/briefs/sir-hagoozat-tasks.md`.

**Truth rule for this plan.** Nothing here is called working unless a reviewer saw it today. The product has never been built: `D:\Projects\SIR Hagoozat` holds the kit files, three legacy apps and nothing that runs. Verified today: the private GitHub repo `sirahmed8/sir-hagoozat` exists, default branch `main`, last update 2026-11-09 (checked with `gh repo view`). Not verified: the Firebase project for this product does not exist yet (no `.firebaserc` in the product folder, and the Firebase CLI was not on the PATH in the round that wrote this plan).

**Product class: GLOBAL.** Anyone in the world can use it, accounts and subscriptions exist, every platform is planned, the owner has an owner-only analytics page, the site is hosted twice (Firebase Hosting and Vercel), and a paid subscription gives the owner every permission inside the product.

---

## 1. Who it is for, and the promise

**For the player.** The amateur footballer in Cairo, Giza, Alexandria or anywhere else who has a WhatsApp group, no pitch, no goalkeeper, and a bill to split. The one-line promise, in the words a player would use:

> Book a five-a-side pitch in under a minute, pay only your share, and arrive with a balanced team.

**For the pitch owner.** The person who owns one or more pitches and loses money on empty Tuesday afternoons. The one-line promise for that side:

> Your empty slots fill with players who arrive on time and pay you on the night.

**The end state we sell.** A player opens the app, sees three real pitches near them with real prices and real free slots, books one for tonight at 9 pm, shares the link to the squad, each person taps and pays their own share with a wallet, the app balances the two teams and sends a QR pass that works with no signal. The owner opens the same product on their phone, sees tomorrow's bookings, the cash they will collect, which slot is still empty, and one tap to publish it to the nearby players who need a game.

**Not in v1:** no ads, no fake pitches, no fake players, no invented ratings, no fake reviews. An empty area shows an empty state with one action (say where you are and we will tell you when a pitch opens there).

---

## 2. The ten competitors, and where we win

Full table with sources, dates and the second ring of competitors: `D:/Projects/_SIR/ops/competitors/sir-hagoozat.md` (read on 2026-11-12).

| Competitor | What it proves about the market | Our edge |
|---|---|---|
| Yalla Hagz (Egypt) | Players expect a free app, a small deposit and the rest at the venue; tournaments and a player passport are already table stakes | Egyptian Arabic copy, per-player collection at join time, open matches that fill an empty slot |
| Hareefa (Egypt) | One tap to rebook the weekly match is the retention habit to copy | The squad, the money and the match stay in one flow, and the owner gets analytics |
| Kourtiva (Egypt) | Split payment, open matches, QR entry, staff roles, tournaments and per-period pricing are all proven, and eight languages are possible | A player-first free tier, self-serve owner sign-up, wallet payment, offline-first, Egyptian speech |
| Matchiva (Egypt) | Booking a referee and a paid extra player is an open category | Real venue relationships, stats and tournaments, a published price list |
| Riadi (Egypt) | A multi-sport catalogue sells volume, and a client-rendered site leaves the AI answer engines nothing to read | One sport done properly, with a readable page and API surface for search and AI answers |
| Hagz Kora (Egypt) | InstaPay as the deposit is the expected Egyptian payment | Every wallet, plus the social layer nobody else has |
| Playtomic (global) | Four owner tiers, POS, wallet, API and support response times are the depth a venue product can reach | Football first, Egypt first, owner self-serve, fair and published fees |
| MATCHi (Nordics) | Matching players by level is the right way to fill a match | Level matching for 5-a-side football on local pitches, with money and community around it |
| Spond (global) | Availability requests, money collection and reminders are the team layer every club app needs | Those features on top of a real booking market with real venues and real prices |
| Pitchbooking (international) | Operators buy software, not apps, and want less admin | One product for both sides of the market, priced in EGP |

**Category truth from the sources (2026-11-12):** the Egyptian player app is expected to be free, the money comes from the venue side, the deposit pattern is established, the squad problem is already solved by Kourtiva, Arabic is badly served, and offline is claimed by nobody. Our product plan follows that truth instead of fighting it.

---

## 3. Features

### 3.1 Parity with the best in the category (must ship)

| Feature | Why it is in the list | Source of the requirement |
|---|---|---|
| Live availability by pitch, date and hour | Base expectation for every player | Yalla Hagz, Hareefa, Kourtiva |
| Instant booking confirmation and a 15 minute hold on the slot | Stops the double booking that ruins a night | Legacy EGFootball5 slot lock; Kourtiva QR entry |
| Deposit first, settle at the venue | The established Egyptian pattern | Yalla Hagz, Hagz Kora |
| Split payment, each player pays their own share when joining | The number one owner complaint in Egypt | Kourtiva; legacy `PitchSplitBillCalculator` |
| Open matches with the missing places shown | Fills an under-booked slot instead of losing it | Kourtiva; legacy 11Players lobbies |
| QR entry pass per confirmed booking, with a scan log | Tells the owner which bookings actually happened | Kourtiva |
| Calendar sync: Apple Calendar and Google Calendar deep links plus an .ics download for every confirmed booking | Players and owners keep the slot in their own calendar; reminders fire even without the app | Our gap, zero competitors do it well |
| Reviews and ratings that carry proof: a venue is rated only by players with a finished booking, a player is rated only by a match that was played | Trust without invented reviews, the number one thing fake apps break | Kourtiva staff roles and player search; our gap on proven reviews |
| Notifications a person can switch off: booking confirmed, a squad member joined, the reminder before the slot, the deposit verdict, the owner's day digest | A booking nobody hears about is a booking that is lost | Yalla Hagz venue chat, Spond reminders |
| Tournaments (knockout, league, single round) | Retention for regular players | Kourtiva, Yalla Hagz, legacy EGFootball5 |
| Player passport: stats, badges, ratings, position | Keeps players inside the product | Yalla Hagz "passport and badges"; legacy 11Players |
| Pitch owner console: schedule, prices, cash register, utilisation, no-shows | What the owner is actually paid for | Playtomic, MATCHi, Pitchbooking |
| Off-peak and peak pricing per period | Fills the quiet afternoon | Kourtiva; legacy `dynamicPricing` idea |
| Wallet and card payments (Egyptian wallets, InstaPay, cards) | Cash only loses the market | Hagz Kora, Kourtiva (gap) |
| Web app that works offline (PWA) | The pitch has bad signal | Nobody claims it (our gap) |
| Arabic Egyptian first, English second | The clearest local gap | Kourtiva is formal, the rest are English-first |
| Support assistant grounded in the venue rules | Cuts owner support time | SHARED_PLATFORM_KIT help-center |
| Data export and one-tap account deletion | Legal and trust baseline | Yalla Hagz has a deletion page, we need both |
| Solo Kickoff: a host books a pitch and the app balances and invites solo players | Yalla Hagz made this table stakes in 2026; it converts browsers who have no squad | Parity row added 2026-11-12 |
| Team Fillup: post the open spots on a booking you already hold, players request to join with profile, position and level shown | Yalla Hagz Team Fillups; Kourtiva open matches | Parity row added 2026-11-12 |
| Squad (crew) with one-tap RSVP for the weekly match | Yalla Hagz Squads; Hareefa one-tap rebook | Parity row added 2026-11-12 |
| Waitlist with auto-promotion when a slot frees | Category trend 2026; nobody in Egypt does it visibly | Our gap |
| Weather or closure reschedule voucher | Pitch closures in rain are common in Cairo winter | Legacy idea HZ-115, now planned |
| Per-court ratings and reviews written by players who played there | Yalla Hagz shows court ratings; we add the proof rule | Section 5.8 already requires proof |
| WhatsApp booking updates as opt-in utility templates | Every Egyptian player lives in WhatsApp; Meta utility rate for Egypt is about US$0.0036 per message (sourced 2026-11-12) | Cheaper than SMS, opt-in only |
| Owner AI assistant that answers from the venue's own numbers | Thril and venue software trend 2026; must stay read-only plus draft actions | Section 5.4 scoped |

### 3.2 The owner's own ideas, carried forward from legacy and TickTick

Every line says where it came from, so nothing gets silently rebuilt thinner than what he already asked for.

| Idea | Source | Status in this plan |
|---|---|---|
| Squad balancer with a fairness meter (drag players, watch the balance settle with a spring) | `legacy/11Players` and `legacy/Hagoozat Elite` PES balancing | Build as the signature interaction of M2 (must be pure algorithm, AI only explains) |
| Position coach that suggests a role for a player | TickTick note "أفكار برامج ومشاريع" idea 30, mapped to a Hagoozat module | M5, AI with a free-quota cap and a local fallback |
| Player card (FUT style), kit builder and jersey designer | `legacy/Hagoozat Elite` (`Holographic3DFutCard`, `fut`), `legacy/EGFootball5` jersey designer | M5, the card is the passport surface |
| Post-match newspaper and season ceremony | `legacy/11Players` (`/newspaper`, `/season-ceremony`), `legacy/Hagoozat Elite` | M5, built from real match data only |
| Goal of the month, var highlights, derby pages | `legacy/Hagoozat Elite` (`/goal-of-the-month`, `/var-highlights`, `/stats/derby`) | M5, from real uploads and real votes |
| Captain draft room and scouting board | `legacy/11Players` (`/draft`, `/scouting`) | M6 (optional), needs a legal check on competitive integrity |
| Achievements, XP, leaderboards | `legacy/11Players` and `legacy/EGFootball5` | M4, driven by real matches |
| Communities, chat, announcements, support tickets | `legacy/11Players`, `legacy/EGFootball5` | M4 |
| Tactical board and live match scoreboard | `legacy/EGFootball5` (`PitchTacticalBoard`, live scoreboard) | M4, live score first, tactics after |
| Web-to-app wrappers for Hagoozat Elite, Education Hub and the player cards | TickTick "أفكار برامج ومشاريع" ideas 6, 7, 8 | M4 (Android and iOS) and M5 (Windows installer) |
| Owner cash register with offline ledger and walk-in bookings | `legacy/Hagoozat Elite` owner dashboard | M4 |
| Player passport with verified games played | `legacy/11Players` rating and karma engine | M2 to M4, never invented numbers |
| Announcements, onboarding, guide, unsubscribe, thank-you, data-deletion pages | `legacy/EGFootball5` and `legacy/11Players` routes | M3, with the legal pack |
| Embroidered jersey conflict check between two teams | `legacy/Hagoozat Elite` idea | M6, small, it is a real night saver |

**Explicitly dropped from legacy:** the `dev_signature` webhook bypass, the client-side admin gate, the fake player generator (`generateDummyPlayersForCommunity` in `legacy/11Players/src/lib/dummyData.ts`, called from `AdminTable.tsx:386`), the dead `FirestoreSeeder`, the SOC 2 and ISO 27001 claims in the old privacy policy, and the seeded placeholder API keys in `legacy/11Players/src/lib/firebase.ts`.

### 3.3 Explicitly out of scope for v1

Betting and any money-back-on-score, drone filming, and anything that needs a hardware sensor in the pitch.

### 3.4 The booking family: what is a Hagoozat module and what is another product

Decided in this round, one line of reason each, as the owner asked (`PRODUCT_DIRECTION_2026-11-12.md` sections 4 and 5). The rule used: if the thing is a booking of a time slot for a service, and the customer, the payment, the calendar and the rating are the same objects, it is a Hagoozat module. If the customer, the data and the day are a different business, it is its own product.

**Modules of SIR Hagoozat (same slot, same customer, same payment, same rating):**

This table is about product boundaries, not about release order. Only pitch slots, the split bill, open matches, tournaments, the QR entry and the owner console are in the first release; every other module below is M5 or later, and each one reuses the slot engine rather than adding a second booking system.

| Idea | Where it comes from | One-line reason |
|---|---|---|
| Padel and padbol courts | Yalla Hagz offers both today | Same venue, same slot, same booking engine, only the sport and the court differ |
| Indoor hall and small futsal court slots | Same venues, other surfaces | A hall is a pitch with walls, so it shares the slot, the price per period and the QR entry |
| Large football field slots (7-a-side and 11-a-side) | Courty lists 5, 7 and 11-a-side in Egypt | One pitch can hold more than one format, so it is a slot attribute and not a new product |
| Referee booking for a match | Matchiva offers it today | It is a booking attached to an existing match slot, paid in the same basket |
| Professional player booking for a match | Matchiva offers it today | Same, a service booked against a match the customer already has |
| Position coach booking (a training session) | TickTick idea 30, mapped to Hagoozat | A coach is booked for a slot, the same booking flow with a different provider type |
| Extra floodlight hour, ball, bibs and keeper gloves as add-ons | Legacy `dynamicPricing` and the venue extras in the legacy pitch pages | They are priced per slot and paid in the same transaction, so they are add-ons and not products |
| Equipment rental (balls, bibs, cones, pump) | Common in Egyptian venues, not offered by any competitor found | It rides on the same slot and the same payment, so it belongs in the basket |
| Match photographer or recorder booking | Legacy `broadcaster` and the live stream in EGFootball5 | The legacy app already had a broadcaster surface, and it is booked against a match |
| Tournament organisation service for a venue | Kourtiva and Yalla Hagz run tournaments for venues | The owner pays for running a bracket on their pitch, which is a service on the venue, not a separate product |
| Stadium or training-ground multi-day booking | Natural growth from hourly slots | The same slot model with a longer window and a different price, so it stays a slot |
| Venue add-on: extra hour after the slot | Every Egyptian venue sells it | It is the same slot engine with a different duration |

**Own products, decided elsewhere on 2026-11-12 and kept here for the record (not modules):**

| Idea | Home | One-line reason |
|---|---|---|
| Handyman bookings (plumbers, electricians, painters) | `plans/sir-handyman.md`, own product, planning only | The customer, the entities and the flow are a service marketplace with its own supply of workers, so folding it into Hagoozat would bloat the scope |
| Car buying, selling and tracking | `plans/sir-cars.md`, own product, planning only | It is a marketplace with listings and price history, not a booking, and the competitors there are completely different |
| Price finder | `plans/sir-price-finder.md`, own product, planning only | It is price comparison and alerts with a lawful-feed gate, and a shopper is not a player |
| Game-deal finder | `plans/sir-game-deals.md`, own product, planning only | It shares the comparison engine with the price finder but not the audience, and the owner split it on purpose on 2026-11-12 |
| Movie discovery and tracking | `plans/sir-movies.md`, own product, planning only | It is entertainment tracking with affiliate links, a different daily use case from booking a pitch |
| Accessibility map | `plans/sir-access-map.md`, own product, built last | The owner decided every unplanned idea is its own project on 2026-11-12, and it is a crowd-moderated place-claim product, not a personal routine feature |

The full decision for every unplanned idea, with the reason and the lawful-data rules, is in `D:/Projects/_SIR/plans/BACKLOG_IDEAS_DECISIONS.md` (2026-11-12).

**Rule for any new booking idea that arrives later:** write one line here with the same shape ("module of SIR Hagoozat" or "own product") and the reason, before any code is planned. If the answer needs more than one line of reasoning, it is its own product.

### 3.5 The two sides, side by side

One product, two customers, two different days and two different definitions of success. Every screen belongs to one of these columns, and nothing is built for one side that hurts the other.

| | **Player and customer side** | **Owner and venue side** |
|---|---|---|
| Who they are | The amateur footballer, the organiser of the Saturday match, the parent who pays for the pitch | The person who owns one pitch or a hall, the receptionist, the operator with several venues |
| What they came for | A free slot tonight, a fair split of the bill, a balanced team | A filled Tuesday, fewer no-shows, the cash collected at the door without a spreadsheet |
| The screen they open first | The pitch list and the map, filtered by area, turf and price | The day view: today's bookings, the money due, the empty slots to publish |
| The action that matters | Book and share the link, then each person pays their own share | Publish the free slot to the players nearby, then confirm the deposit |
| What they must never see | Ads, a fake pitch, an invented player, a price that is not the real price | Another owner's pitches, another owner's money, another owner's players |
| How they pay | One share at join time, a wallet or a card, and the rest at the venue | A deposit collected in the app, the rest in cash at the venue, and a ledger that says which is which |
| What they are asked to give | A phone number, visible to the owner only after a booking exists | The pitch address, the prices per period, the house rules, the cancellation policy |
| What keeps them coming back | The pass in the phone, the calendar entry, the squad, the passport with real stats | The daily digest, the utilisation number, the no-show number, the review that means something |
| What "success" is | The match happened and everybody paid their share | The slot was filled, the player arrived, the money was collected |
| The plan that serves them | Sections 1, 3.1, 3.2, 4, 7 and the tasks T7, T8, T9 | Sections 1, 3.1, 5.3, 5.5, 7 and the tasks T10 and the M4 owner console |

---

## 4. Platform matrix

Standing rule (owner, 2026-11-12): every product ships on all platforms, so web, Windows, macOS, Linux, Android and iOS are all required for SIR Hagoozat. Wear OS, watchOS, TV and car are not in that list, so they are skipped in v1 with a written reason, not left in silence.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required | The whole product: browse, book, pay, squad, tournaments, owner console | Nothing pending |
| PWA (installable, offline) | Required | Install from the browser, offline pitch list, offline booking pass and QR, background sync | Native shell if the PWA proves weak on low-end Android |
| Windows | Required (M5) | Installable PWA from day one, then a real NSIS installer with the same Google sign-in and self-update | Signed installer (owner buys the certificate) |
| macOS | Required (M5) | Installable PWA from day one, then an unsigned DMG from the same Electron build | Signed build when the owner has an Apple account |
| Linux | Required (M5) | Installable PWA from day one, then AppImage and .deb from the same Electron build with a .desktop entry | Signed package |
| Android phone and tablet | Required (M4) | Expo app: the same account, bookings, pass, squad, owner console | Play Store when the reinvestment ladder allows |
| iPhone and iPad | Required (M4) | Expo app, same account and data, tablet layouts | App Store or SideStore (needs a paid Apple account, the owner decides) |
| Wear OS | Skipped in v1 | Nothing | A kickoff countdown widget, decided with an ADR |
| watchOS | Skipped in v1 | Nothing | Same ADR as Wear OS |
| TV (Android TV and Apple TV) | Skipped in v1 | Nothing | A venue screen with today's bookings and the queue, only if a real venue asks |
| Car (Android Auto and CarPlay) | Skipped in v1 | Nothing | Navigation to the pitch only if a paid tier needs it |
| Widgets and live activities | Part of M5 | Android Glance and iOS WidgetKit: the next booking and the kickoff time | Richer surfaces later |
| Browser extension | Skipped | Nothing | No browser use case that justifies the review |
| Docker and self-host | Skipped | Nothing | Not a product need here |

**Rule:** every platform shares one Firebase project, one account and one dataset. No platform ever carries its own copy of the rules. The Windows, macOS and Linux builds come from one Electron shell and one release feed, so an update reaches all three at once.

---

## 5. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. That file is the shared standards kit every product builds against; SIR Platform was cancelled as a project on 2026-11-12, so there is no extraction target any more. SIR Hagoozat is a GLOBAL product, so it adopts all twenty sections of the kit as internal `packages/*` with the kit names and interfaces, and when it hardens a piece that other products need, that piece goes back into the kit file and HQ queues the adaptation for the others.

### 5.1 Shape

```
apps/web        Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens
apps/api        Route handlers that need secrets and long tasks (webhooks, cron, AI proxy)
packages/core   Domain types and zod schemas: Pitch, Slot, Booking, Deposit, Squad, Match, Rating, User
packages/data   Firestore repositories, one interface per entity, emulator tests
packages/ui     The shared UI kit from the kit: InputBox, TabBar, BottomSheet, Card, Chip, Modal, Toast
packages/kit    owner-auth, signed-webhook, billing-fallback, ai-proxy, legal-pack, i18n, help-center, notifications
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
- Rate limits on sign-in, booking, wallet requests, uploads and AI calls.
- Owner accounts get a second factor offer.
- Test: a forged token gets 403, a client-side flag flip gets nothing, a non-owner token on `/owner` gets 403.

### 5.3 Owner-only analytics page

- Route `/owner`, server-verified owner token, 403 for everyone else.
- Real metrics only, read from aggregates not raw collections: bookings, revenue in EGP and the visitor currency, utilisation per hour, no-show rate, deposits waiting for verification, new players, repeat players, AI cost, error rate.
- A second section for the pitch owner role: the schedule, the cash ledger, the deposits queue and the export tools. Each pitch owner sees only their own pitches, enforced in Firestore rules and re-checked on the server.
- No invented numbers anywhere: an empty metric shows a dash and the reason, never a zero dressed as a fact.

### 5.4 AI with the fallback chain

Chain from `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`: Gemini `flash-lite-latest`, then `flash-latest`, then any Gemini text model, then OpenRouter free models, then other free providers, then the local model on this PC. One Gemini key and one OpenRouter key per product, created on this product's own project, stored only in the ignored env file and the Vercel environment, never printed, never committed.

What AI does in this product, and what it must never do:

| Feature | AI role | Hard rule |
|---|---|---|
| Squad balance explanation | Explain why these two teams are fair, in plain words | The balancer itself is a pure function with a test. No AI in the decision, only in the sentence |
| Position coach | Suggest a role from the player's own history | Uses only that player's own data, never a private player's data of anyone else |
| Support assistant | Answer from `docs/help/*.md` only | Refuses anything not in the help source, and says so |
| Photo quality check on a pitch photo | Warn about blur or darkness | Advisory, never blocks a real pitch from being listed |
| Weekly owner report draft | Draft the summary the Telegram sender sends | Numbers come from the database, the model only writes the sentence |

Free players get 5 AI calls per rolling 24 hours with a visible badge, the owner is unmetered, `AI_ENABLED` is the kill switch, a daily cost cap lives in `config/limits.json`, and every call logs which provider answered (never the content). Arabic and English eval sets exist before the feature ships, and the runner exits non-zero below the threshold.

### 5.5 Data and money

- Firestore with deny-by-default rules, per-user and per-pitch-owner claims, emulator tests including a cross-tenant read that must fail.
- A slot is a document with a status and a hold expiry. Booking is a Firestore transaction with an idempotency key. Test: 20 parallel requests for one slot produce exactly one booking.
- Deposits and receipts are private files with signed URLs, checked for size and type, deleted 90 days after verification (default, the lawyer may change it).
- A player's phone number is visible to a pitch owner only after a booking exists.
- Wallet and card payments through Paymob and Fawry in test mode. The webhook is HMAC-SHA256 signed with the timestamp inside the signed body, verification is server-side only, and tampered, replayed, unsigned and wrong-timestamp events are rejected.
- Refunds and cancellation follow one written policy for every venue, published on the pitch page before payment.

#### 5.5.1 Payments readiness

Money is the last thing that goes live and the first thing that must never be wrong. The ladder below is in order, and nothing moves up a step until the step below it is proven.

| Step | What it proves | Honest state on 2026-11-12 |
|---|---|---|
| 1. The money arithmetic is exact | The split bill divides the slot price to the piastre, and a player who joins late pays the same share | Not built yet: the rule is specified here, the test is task T8 |
| 2. The amount is shown before the payment | One screen with the total, the share, the deposit and what the venue receives | Not built yet: task T8 |
| 3. The gateway runs in test mode | Paymob and Fawry accept the test card, the webhook is signed, a replayed or tampered event is rejected | Not built yet: task T8 and the signed-webhook tests |
| 4. The owner's business account exists | The real merchant account, the tax treatment of the venue fee, the invoice | Owner only: listed in section 12 |
| 5. The legal pages exist | Terms, cancellation and refund wording, privacy, each reviewed by a lawyer | Not built yet: milestone M3 |
| 6. The first real charge | One venue with a written agreement, one real booking, one real refund, one real receipt | Not started: milestone M6, and only after steps 1 to 5 |

Rules: no real charge before step 5. Every amount is computed on the server and never in the client. A deposit is refunded in full when the venue cancels. The refund path is proven with the test card before a real card exists. The fee schedule of each gateway is read on the official page on the day it is used, and until then it is "(unsourced, verify)" and it never appears on a pricing page.

#### 5.5.2 Data model (Firestore collections)

One collection per aggregate, ids are Firestore document ids, every document carries `createdAt`, `updatedAt` and `schemaVersion`. Money is stored as integer piastres plus a currency code, never floats. Timestamps are server timestamps; slot times additionally store the venue IANA timezone.

| Collection | Key fields | Access rule |
|---|---|---|
| `users` | phone (private until booking), displayName, locale, skillLevel, positions, createdAt | self read/write of profile fields; stats computed, not stored raw |
| `venues` | ownerId, name, address, geo, phone, houseRules, cancellationPolicy, commissionPlan, status | owner writes; public reads only published fields |
| `pitches` | venueId, name, sport, surface, size, amenities[], photoUrls[], pricePeriods[] {days, startMin, endMin, pricePiastres}, status | public read when published; owner writes |
| `slots` | pitchId, startsAt, endsAt, status {open, held, booked, blocked}, holdExpiresAt, pricePiastres, waitlistCount | public read; writes only through booking transactions |
| `bookings` | slotId, venueId, organiserId, memberIds[], status {held, confirmed, played, cancelled, no_show}, depositPiastres, idempotencyKey, qrRef | members and venue owner read; organiser manages |
| `bookingMembers` | bookingId, userId, sharePiastres, paidPiastres, position, level, status | self + organiser + venue owner read |
| `deposits` | bookingId, userId, amountPiastres, gateway, status {pending, submitted, verified, rejected, refunded}, receiptPath (private) | self + venue owner; receipt via signed URL only |
| `openMatches` | bookingId or standalone, spotsNeeded, positionsNeeded, levelRange, expiresAt, status | public read when open; join requests are transactions |
| `squads` | ownerId, name, memberIds[], weeklySlotTemplate | members read/write own squad |
| `waitlist` | slotId, userId, position, notifiedAt, status | self + slot owner reads |
| `matches` | bookingId, score, scorers[], playedAt, status | participants read; organiser writes result |
| `ratings` | targetType {venue, pitch, player}, targetId, bookingId, score, text, repliedBy | public read aggregates; one per booking enforced |
| `tournaments` | venueId, format {knockout, league, round_robin}, teams[], status, bracketState | participants read; organiser writes |
| `ledger` | venueId, kind {cash, online, refund, fee}, amountPiastres, bookingId?, offlineId?, syncedAt | venue owner only; offlineId dedupes sync |
| `notifications` | userId, kind, channel, payloadRef, sentAt, status | self read; system writes |
| `subscriptions` | userId or venueId, plan, status, gatewaySubscriptionId, currentPeriodEnd | self + owner admin |
| `leads` | email, source, createdAt | write-only public; owner reads |
| `aiUsage` | userId, feature, provider, tokensIn, tokensOut, costMicroUsd, dayBucket | self summary; owner aggregate |

Indexes needed on day one: `slots(pitchId, startsAt)`, `slots(status, startsAt)`, `bookings(venueId, startsAt)`, `bookings(memberIds array-contains, status)`, `openMatches(status, expiresAt)`, `ledger(venueId, createdAt)`, `waitlist(slotId, status)`. Every query that filters on a second field gets a compound index, and the emulator test suite asserts the index list matches the queries in code.

### 5.6 Hosting and delivery

- **Firebase Hosting** is primary. **Vercel** is the second host, the same repository imported with the Vercel CLI, the same build, the same environment variables on both. Both addresses are curl-checked and written into the project checkpoint.
- Static hosting cannot run route handlers, so every secret, webhook and AI call lives in the Firebase Functions or the Vercel function side, never in the client bundle. This is the exact defect that killed the legacy apps (`/api/ai/chat`, `/api/ai/tts`, `/api/admin/role` returned 404 in production because the apps were exported as static).
- A service worker caches the pitch list, the next booking and the pass. Background sync sends the queued actions when the connection returns.
- Daily Firestore export to a private bucket, a monthly restore test, a health endpoint at `/api/health`, a status JSON, a nightly error digest and a weekly Telegram report at a round hour.

### 5.7 Security baseline

Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI. A CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent, with Reject All as prominent as Accept. One-tap data export and one-tap deletion. Rate limits on auth, booking, uploads, AI and webhooks. No fake data in any path a user can see.

### 5.8 Calendar, notifications and reviews

**Calendar.** Every confirmed booking produces one calendar event, and the event is the same everywhere.

- The event carries the venue name, the pitch size, the address, the amount paid, the booking reference and the QR pass. The start and the end are stored in UTC, and the venue timezone (Africa/Cairo, UTC+2 all year, Egypt has no daylight saving since 2023) is stored next to them, so a venue in another country stays correct.
- **Google Calendar:** a deep link that opens the add-event form pre-filled, plus the .ics download of the same booking. The deep link needs no OAuth, so it works on a phone that is not signed in.
- **Apple Calendar:** Apple publishes no add-event deep link, so the honest path is the .ics file and a subscribe URL per venue, offered from the same screen. The iPhone opens the .ics and lets the user add it to any calendar they own.
- The .ics download works with no signal and no account, because the pass has to work at the gate.
- The owner side gets the same two options, so a venue can publish its weekly slots to a shared calendar.
- Nothing is written to anyone's calendar without a tap, and the screen says plainly that the product does not keep syncing after that, because there is no server-side calendar account in v1.

**Notifications.** Every kind is opt-in, and every kind has its own switch in the settings.

| Kind | Channel | Who | When |
|---|---|---|---|
| Booking confirmed | Push and email | the player and the owner | the moment the slot is booked |
| A squad member joined | Push | the organiser | when someone joins an open match |
| The reminder before the slot | Push, three hours and one hour before | the player | only when the booking is confirmed |
| The deposit verdict | Push and email | the player and the owner | when the owner verifies or rejects the receipt |
| The owner's day digest | Email or Telegram, at a round time | the owner | once a day, and only when it has something in it |

Rules: quiet hours come from the venue's own rules, one message per event, no marketing messages in any tier, the same message in Arabic and English, a visible stop in every message, and a message that is never sent for a booking that no longer exists. WhatsApp is an opt-in channel: each player enables it per booking type, messages go out as Meta utility templates (booking confirmation, reminder, deposit verdict), the per-message cost is logged against the AI and ops cost budget, and push plus email remain the free default so no user is charged for a message they did not ask for.

**Reviews.** A review is a claim about a real event, so it needs a real event behind it.

- A venue is rated only by a player whose booking reached the "played" state, one review per booking.
- A player is rated only by a member of the opposite team in a match that was played.
- A rating is a number plus an optional sentence. The number is what the interface shows. The sentence is written by the person and is never generated, rewritten or translated by AI.
- The booking reference is checked on the server, not in the client, and no review is published without it.
- The venue can reply once per review. A review is never deleted silently: a removed review says why, and the history stays visible to the owner of the venue.
- No average rating is shown for an entity with fewer than three reviews, because two reviews are not a reputation. It shows "new on SIR" instead.
- AI never writes a review, never edits one and never answers with one.

### 5.9 API surface (v1)

One typed REST surface under `/api/v1`, the same one the Expo app, the PWA and the future owner integrations call. Every route validates input with zod, authenticates with the Firebase ID token, and is rate-limited. Server-only routes (webhooks, cron, AI proxy) live on the functions side and never ship in the static bundle.

| Route | Method | Purpose | Auth |
|---|---|---|---|
| `/api/v1/pitches` | GET | List pitches with filters (area, sport, price, availability window) | public, rate-limited |
| `/api/v1/pitches/:id` | GET | Pitch detail with photos, amenities, price periods, house rules | public |
| `/api/v1/pitches/:id/slots` | GET | Live slot availability for a date range | public |
| `/api/v1/pitches/:id/slots/:slotId/hold` | POST | Take the 15-minute hold before checkout | user |
| `/api/v1/bookings` | POST | Create a booking (idempotency key required) | user |
| `/api/v1/bookings/:id` | GET, PATCH | Booking detail, cancel inside the published window | owner of booking |
| `/api/v1/bookings/:id/split` | POST | Per-player share requests inside an open match | booking member |
| `/api/v1/bookings/:id/qr` | GET | Signed offline QR pass payload | booking member |
| `/api/v1/open-matches` | GET, POST | List and create Team Fillup / open match posts | user |
| `/api/v1/open-matches/:id/join` | POST | Request to join with position and level | user |
| `/api/v1/squads` | GET, POST, PATCH | Crew management and weekly RSVP | user |
| `/api/v1/waitlist` | POST, DELETE | Join or leave a slot waitlist | user |
| `/api/v1/deposits` | POST | Register a deposit intent and receipt upload URL | booking member |
| `/api/v1/deposits/:id/receipt` | POST | Upload the private receipt (signed URL flow) | booking member |
| `/api/v1/payments/webhook/:gateway` | POST | Paymob, Fawry, InstaPay callbacks, HMAC verified | gateway signature |
| `/api/v1/me` | GET, PATCH, DELETE | Profile, passport stats, data export, account deletion | user |
| `/api/v1/me/bookings` | GET | Own bookings and passes | user |
| `/api/v1/venues/:id/console` | GET | Owner day view: bookings, money due, empty slots | pitch owner |
| `/api/v1/venues/:id/slots` | POST, PATCH | Publish, price and block slots | pitch owner |
| `/api/v1/venues/:id/deposits` | GET, POST | Deposit verification queue | pitch owner |
| `/api/v1/venues/:id/ledger` | GET, POST | Cash register entries, offline sync endpoint | pitch owner |
| `/api/v1/tournaments` | GET, POST | Tournament list and creation | user / owner |
| `/api/v1/tournaments/:id/bracket` | GET | Bracket and standings | public |
| `/api/v1/tournaments/:id/results` | POST | Enter a result, advance the bracket | organiser |
| `/api/v1/notifications/prefs` | GET, PATCH | Per-kind, per-channel switches | user |
| `/api/v1/owner/analytics` | GET | Aggregate owner metrics | owner only |
| `/api/v1/leads` | POST | Pricing-page email capture | public, rate-limited |
| `/api/v1/ai/*` | POST | Position coach, balance explanation, support assistant (proxied, metered) | user, quota |
| `/api/health` | GET | Liveness and dependency status | public |

Rules for the surface: no route returns another tenant's data (enforced in rules and re-checked in handlers), money amounts are computed server-side only, every mutating route is idempotent or explicitly rejects a replay, and the OpenAPI description plus `llms.txt` ship with the site so search and AI answer engines can read the product.

### 5.10 Legal baseline, Egypt PDPL and launch gates

- Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI. A CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent, with Reject All as prominent as Accept. One-tap data export and one-tap deletion. Rate limits on auth, booking, uploads, AI and webhooks. No fake data in any path a user can see.
- **Egypt PDPL 151/2020 (updated 2026-11-12):** the Executive Regulations took effect 2025-11-01 with a grace period ending 2026-10-31. Before real Egyptian user data is collected the product needs: a licence from the Personal Data Protection Centre (including the cross-border transfer position, because Firestore stores data outside Egypt), an appointed data-protection contact, consent records for every marketing message, a breach-notification runbook with the law's timelines, and financial data treated as sensitive (deposit and payment records get the strictest handling and shortest retention that still serves the ledger). The legal pack must state all of this; the lawyer review covers it before M6.
- **Payment rails:** Paymob publishes 2.75% + 3 EGP per transaction with weekly settlement (sourced 2026-11-12); Fawry is contract-quoted ("(unsourced, verify)"). On a small deposit the fixed 3 EGP plus 14% VAT on the fee is material, so the pricing page shows the net math and the plan never silently absorbs gateway costs.

---

## 6. Premium quality bar

This is the floor from `D:/Projects/_SIR/standard/23-premium-code-bar.md` and `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`, written for this product.

**Motion, Apple level.**
- One shared spring config across the app: stiffness 300 to 400, damping 28 to 30, transform and opacity only, no layout thrashing, 120 Hz safe.
- Every sheet, drawer, modal and panel opens and closes with the same spring. An open-only animation is a defect.
- The squad balancer is the signature interaction: drag a player, and the fairness meter settles with a spring. Micro-interactions 100 to 150 ms, standard 200 to 300 ms, large 300 to 500 ms. Press scale 0.98. Reduced-motion path for every animation.
- The active tab shows its label and the others show an icon only, the active tab scrolls into view on load and on change, and the bottom bar never vanishes when the keyboard opens.
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
One design system: tokens for colour, spacing on a 4 and 8 px grid, radii, shadows, type and motion. Seed green `#16A34A` for a pitch product, calm neutral canvas, accent only for primary actions and key numbers. No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. One component per control, never two. Arabic screen face: IBM Plex Sans Arabic, Cairo or Tajawal.

**Native app feel.**
The browser's text selection and the right-click menu are disabled site-wide and replaced by the app's own menu with in-app actions and a refresh. Normal select, copy and paste inside real input fields still work.

**Evidence before the word done.**
Screenshots at 320, 390, 768, 1280 and 1920 px, in Arabic and English, in light and dark, plus 3840 px once. Playwright on the critical journeys. Lighthouse mobile 90 or better. A click-target audit in CI. The self-audit loop runs until two clean cycles.

---

## 7. Free tier and fair pricing (EGP and USD)

These are **test prices**, not published prices. They are the outline the owner confirms with three real pitch owners and the official gateway fee schedule before anything is charged. The legacy plan's own numbers are kept where they exist, because they are the owner's numbers: 59 EGP per month for the player Pro tier (`legacy/11Players` pricing copy) and 450 EGP per month or 4,500 EGP per year for the venue tier (the previous Hagoozat plan). The USD column uses 48 EGP per 1 USD, which is "(unsourced, verify)" and is recomputed from the live rate on the pricing page.

| Plan | Who | EGP | USD | What it includes | Rule |
|---|---|---|---|---|---|
| Player Free | Any player | 0 | 0 | Browse pitches and real free slots, book with a deposit, split the bill, join open matches, QR pass, player passport with real stats, WhatsApp share, offline pass | The core action is never behind a plan |
| Player Pro | Serious players | 59 per month (test) | about 1.20 per month | Priority alerts on new slots near their areas, unlimited open-match discovery, full position coach, card themes, create and enter tournaments, priority support | Cancel any time, the plan lapses at the end of the paid month |
| Venue Free | A pitch owner | 0 | 0 | List up to 3 pitches, publish free slots, take cash and manual bookings at the venue, basic schedule | A venue is never charged to be listed |
| Venue Pro | A pitch owner | 450 per month or 4,500 per year (test) | about 9.40 per month or about 94 per year | Unlimited pitches, online deposits with wallets and cards, dynamic off-peak pricing, open-match publishing to nearby players, QR entry with a scan log, utilisation and no-show analytics, cash register, automated reminders | One fee only: the plan replaces the commission, the transaction fee is the published gateway cost |
| Venue Partner | A multi-pitch operator | price set with the owner | | Staff roles, POS, invoices, API, multi-venue | Later milestone, decided with the first real operator |

**Fairness rules written into the product.**
1. A player never pays to book a pitch, and the app never takes a cut of a player's share.
2. A venue owner pays one thing only. If the venue is on Venue Pro, there is no commission on top. If the venue is on Venue Free, the commission is shown before the owner confirms, never hidden in a small line.
3. Every price on screen is in the visitor's currency, auto-detected, with the original EGP amount next to it.
4. A deposit is refunded in full when the venue cancels. A player cancellation inside the published window is refunded minus what the venue already lost, and the rule is on the pitch page before payment.
5. No ads, in any tier, ever. The owner sets an ad spend cap of 0 until he changes it.
6. The owner of the product gets every paid feature, free, and a subscription grants him all permissions inside the owner console.

**Still open and blocking publication:** the official Paymob and Fawry fee schedules for Egypt, the tax and invoicing treatment of venue fees in Egypt, the exact cancellation and refund wording, and the lawyer review of every legal page. Each is tagged "(unsourced, verify)" in `ops/competitors/sir-hagoozat.md` section 4 and in `docs/ENV.md` when the project starts.

---

## 8. Milestones M0 to M6, with acceptance tests

Every exit check is something a reviewer can run or click. "Green" means the output was seen, not assumed.

### M0: Foundations, the kit and the honest map of the legacy

Work: create the product's own Firebase project named `sir-hagoozat` (free Spark plan) and keep it separate from every other product; scaffold the monorepo (apps, packages, docs, scripts) with strict TypeScript, Tailwind v4 tokens, RTL-first styles and the shared `verify` script; write the legacy parity matrix; design the token set and the three design directions; recreate the Desktop folder kit from scratch for the new build.

Exit checks:
1. `D:/Projects/SIR Hagoozat` contains `folder.ico` (named exactly that, never `icon.ico`) and the Desktop folder `SIR Projects/SIR Hagoozat` holds `folder.ico`, `SIR Hagoozat.lnk`, `Start SIR Hagoozat dev.lnk`, `Stop SIR Hagoozat dev.lnk`, `Open project folder.lnk` and `Versions.txt` reading version 1.0.0 and a plain status. The old kit belonged to the legacy build, so M0 rebuilds it.
2. `.sir/reports/parity.md` lists every route of the three legacy apps (29 pages and 7 API routes merged, 55 pages in 11Players, 36 in EGFootball5) with a keep, port, drop or drop-with-reason verdict and the file that proves it.
3. `pnpm verify` runs typecheck, lint, tests, build and gitleaks, and the output was seen green.
4. The Firebase project `sir-hagoozat` exists and the GitHub repo `sirahmed8/sir-hagoozat` is the only remote for it.
5. `docs/DESIGN.md` holds three explored directions with screenshots and the chosen one, plus the token file and the balancer prototype running at 120 Hz.

### M1: The booking core, proven under contention

Work: the data model and the Firestore rules for Pitch, Slot, Booking, Deposit; the slot lock and the booking transaction with an idempotency key; the pitch list and the pitch page; five states everywhere.

Exit checks:
1. The emulator rules tests pass, including a cross-tenant read that must fail.
2. 20 parallel booking requests for one slot produce exactly one booking and 19 clean rejections.
3. The pitch list and the pitch page show idle, loading, empty with one action, error with retry and populated, at 390 px and 1280 px, in Arabic and English, light and dark.
4. The slot hold expires on its own and the slot becomes bookable again, with a test that says so.

### M2: Money and the squad

Work: the booking wizard with ordered steps that cannot be skipped; the deposit and the private receipt upload; the split bill with each player paying their share; the open match with the missing places; the squad balancer with the fairness meter; the WhatsApp share; the QR pass.

Exit checks:
1. Step 2 of the wizard cannot be reached before step 1 validates, and the e2e test tries to jump and is blocked.
2. A receipt upload is refused when it is the wrong type or too large, and a stored receipt is reachable only with a valid signed URL.
3. The split bill sums to the slot price exactly, and a player who joins late pays the same share.
4. The balancer is a pure function with a property test: the rating-sum difference between the two teams stays inside the stated bound, and the same input always gives the same teams.
5. The QR pass works offline and the pitch owner scan marks the booking as arrived.

### M3: Security, billing, legal, and the owner page

Work: the signed webhook with negative tests; the billing fallback page with lead capture; the legal pack; the owner-only analytics page.

Exit checks:
1. Ten negative webhook tests pass (tampered, replayed, unsigned, wrong timestamp, wrong amount, and the rest), and no `dev_signature` or any other bypass exists in the code.
2. A non-owner token on `/owner` gets 403 and a forged token gets 403.
3. The pricing page shows the test prices with the currency auto-detected, plus "Subscriptions launching soon" and an email capture that creates a lead document and rejects an invalid address.
4. Every legal page exists under `/legal/*`, each marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch".
5. Both hosts answer: the Firebase URL and the Vercel URL were curl-checked, and the two addresses are written in the project checkpoint.

### M4: The owner console, the community and the two platforms

Work: the owner console (schedule, utilisation, no-shows, cash register with an offline ledger, deposit verification queue, export); the tournaments engine (knockout, league, single round); communities, chat, announcements and support tickets; the achievements, XP and leaderboard layer; the Telegram notifications and the scheduled reminders; the Expo app for Android and iOS.

Exit checks:
1. The owner console shows real numbers from the database, and every metric is empty with a dash when there is no data.
2. A knockout bracket with 8, 16 and 32 teams generates correctly, a result advances the winner, and the standings recompute.
3. The offline ledger records a cash booking with no connection and syncs cleanly when the connection returns, with no duplicate.
4. The reminder job fires at a round hour, sends through the Telegram sender, and the owner's weekly report arrives with the numbers and their meaning.
5. The Android APK builds and installs on a device, and the same Google account sees the same booking on the web app.

### M5: AI, the Windows app and the quality pass

Work: the position coach, the balance explanation, the support assistant; the Windows installer with the same sign-in and self-update; the macOS and Linux builds; the widget and live activity surfaces; the full self-audit.

Exit checks:
1. `npm run eval:balancer` and `npm run eval:support` pass with Arabic and English sets, and the support assistant refuses an ungrounded question.
2. The Windows installer installs, starts, signs in with the same Google account, updates itself, and its entry is in `Projects-Hub.html` and on the Download page with the version and the size.
3. Screenshots exist at 320, 390, 768, 1280 and 1920 px in both languages and in light, dark and high contrast, with the five states visible.
4. The accessibility audit passes WCAG 2.2 AA with an accessible name on every control, no covered hit area, and no horizontal scroll from 320 px.
5. Lighthouse mobile is 90 or better and the JSON is saved in `.sir/evidence/`.

### M6: Release, real venues and the legacy handover

Work: the launch package (domain, accounts, legal review); the old hosts redirected with 301; the keys rotated; the first real pitches onboarded with written consent; the legacy handover.

Exit checks:
1. Three real pitches are live with a written consent, a real price and a real owner, and no seeded or invented pitch exists in any path a user can see.
2. The 301 redirects from the three old hosts are verified by curl.
3. The legacy keys are rotated and the service-account file is out of the repository.
4. The lawyer has reviewed the legal pages and the tax question is answered, and only then can a paid plan go live.
5. Each legacy folder moves from `legacy/` to `D:\Projects\old projects\` only after the parity matrix shows every kept feature is ported and verified, keeping the git history. `legacy/` is never deleted from the repository history.

---

## 9. The first ten tasks for the free agents

Ready to queue, each with its own brief: `D:/Projects/_SIR/ops/briefs/sir-hagoozat-tasks.md`.

1. Legacy parity matrix, read-only, into `.sir/reports/parity.md`.
2. Monorepo scaffold with tokens, RTL, the health route and CI.
3. The product's own Firebase project and the `owner-auth` package with negative tests.
4. The data model and the Firestore rules, with emulator tests.
5. The slot lock and the booking transaction with the 20 parallel test.
6. The shared UI kit: tokens, the four themes, the five states, the spring components.
7. The pitch list and the pitch page with the map and list views.
8. The booking wizard with the deposit and the private receipt upload.
9. The squad balancer as a pure function plus the fairness meter.
10. The owner-only analytics page and the billing fallback page.

---

## 10. Skills from the library that this build uses

Picked from `D:/Projects/_SIR/ops/SKILLS_INDEX.md` and the digests in `D:/Projects/_SIR/ops/encyclopedia/`. Digests live under `ops/encyclopedia/<tool>/<skill>.md`; the paths below are the real files found on 2026-11-12.

**Design and UI**
- `anti-vibecoded-design-system` (claude) - keeps the pitch product away from generic AI styling and purple gradients.
- `taste-design-engine` (claude) - the self-audit against AI patterns before the screens ship.
- `emil-motion-impeccable` (claude) - the spring physics for the balancer, the sheets and the tab bar.
- `modern-ui-ux-design-system` (claude) - tokens, micro-interactions and hierarchy for one design system.
- `cognitive-product-intuition` (claude) - the wizard step order and the empty states, so the flow matches how players think.
- `high-conversion-copywriting` (claude) - the promise line and the pitch page copy that sell the end state without hype.
- `commercial-app-blueprint` (claude) - llms.txt, the trust signals and the sticky call to action on the site.
- `a11y-debugging` (codex) - the accessibility audit with Chrome DevTools against WCAG 2.2 AA.
- `mobile-ergonomics-polish` (claude) - touch targets, no horizontal scroll, tap feedback on the phone screens.
- `modern-web-guidance` (claude) - the current web APIs, container queries and dialog behaviour, run before any client-side work.
- `react-best-practices` (claude) and `nextjs` (claude) - App Router structure, Server Components, rendering and performance rules.

**Security and legal**
- `firestore_rules_creation` (claude) - the deny-by-default rules for every collection.
- `firebase_security_rules_auditor` (claude) - the audit that finds a cross-tenant read before a user does.
- `zero-trust-security-hardening` (claude) - server-side role checks, secure cookies and rate limiting.
- `owasp-vulnerability-shield` (claude) - the OWASP pass over uploads, webhooks and auth.
- `vibe-auth-hardening` (claude) - the five auth flaws that a fast build introduces.
- `legal-compliance-shield` (claude) - the legal pack that matches what is actually collected.
- `cookie-debugging` (codex) - the consent banner behaviour and the cookie audit.

**Mobile and desktop**
- `modern-app-engineering` (claude) - the shared architecture for the Expo app and the Electron shell.
- `android-cli` (claude) and `device-hub` (codex) - the Android build, the emulator and the device checks.
- `compose-preview` (codex) - the Wear OS decision, when it is taken.

**AI**
- `gemini-api-dev` (codex) - the Gemini calls and the structured output.
- `ai-gateway` (codex) and `omniroute-resilience-gateway` (claude) - the fallback chain and the failover on quota errors.
- `firebase_ai_logic_basics` (claude) - Firebase AI Logic when it becomes cheaper than a direct call.

**Automation and operations**
- `chat-sdk` (codex) - the Telegram bot for confirmations and reminders.
- `webhook-testing` (deep) - capturing, replaying and validating the gateway webhooks.
- `verification` (codex) and `verification-before-completion` (deep) - the end-to-end check before the word done.
- `sir-browser` (deep) - the zero-prompt browser bridge for the visual audits.

**Data, hosting and growth**
- `firebase_firestore` (claude) - queries, indexes and the data model.
- `database-reliability-transactions` (claude) - the atomic booking transaction and idempotency keys.
- `firebase_hosting_basics` (claude), `vercel-cli` (codex), `deployments-cicd` (codex) and `env-vars` (codex) - the two hosts with the same build and the same variables.
- `google_maps_platform` (codex) - the map view, the geocoding and the distance search for nearby players.
- `open-seo-auditor` (claude) - Arabic search visibility, JSON-LD and the AI answer check.
- `system-design-architect` (claude) and `production-engineering-standards` (claude) - the zero-mock persistence and the production bar.

---

## 11. Risks and the defaults we take

- **Two-sided cold start.** Default: one area with 3 to 5 real pitches and real owners before any advertising or search push. No marketing before the sourcing tasks in the competitor file are done.
- **Yalla Hagz moved faster than planned.** Their 2026 rebuild added Kickoffs, Team Fillups, Squads, wallet and rewards, and they hold the App Store Sports chart in Egypt. Default: our differentiators narrow to what they structurally lack — Egyptian dialect, per-player split payment at join time, owner analytics and cash register, offline-first, and proven reviews — and the plan adds the parity rows (Kickoffs, Fillups, Squads) so we do not lose on table stakes.
- **Kourtiva published owner pricing.** AED 75 to 369 per month (about EGP 1,000 to 4,800 at the plan's test rate, "(unsourced, verify)" for the conversion) is far above our 450 EGP Venue Pro test price, but they are UAE-facing with a demo-request sales motion. Default: keep the EGP price, win on self-serve sign-up and Egyptian payment rails, and never claim we are cheaper until the exchange rate is verified on the day.
- **Gateway fees eat small deposits.** Paymob's published 2.75% + 3 EGP plus 14% VAT on the fee means a 100 EGP deposit loses about 7% to the gateway. Default: deposits are priced to cover the gateway cost or the venue absorbs it as a published plan benefit; the math is shown before launch, never hidden.
- **PDPL enforcement is live.** Executive Regulations effective 2025-11-01, grace until 2026-10-31, licences required for cross-border transfers and marketing. Default: treat licensing and the data-protection officer as M6 launch gates; do not collect real Egyptian personal data in production before the lawyer signs off.
- **Receipt fraud on manual payment.** Default: manual verification queue, no auto-approval, a phone number visible to the owner only after a booking.
- **Port volume.** Three apps, 3,014 files. Default: port by feature behind the parity matrix, never copy files across.
- **The real market already has good products.** Yalla Hagz, Hareefa and Kourtiva are live. Default: win on Egyptian Arabic, the split bill, the open match, offline and the owner numbers, not on features we cannot verify.
- **Payments before the lawyer.** Default: test mode only, no real charge, no published plan price until the fee schedule and the legal pages are reviewed.
- **Gateway and tax numbers.** Default: every one of them is "(unsourced, verify)" until read on the official page on the day it is used.
- **Static export killing the server.** Default: no secret ever in a route handler that a static host would drop; the server features run on the functions side from M1.

### 11.1 Open questions, and the answer we take

| Question | Recommended answer |
|---|---|
| Do we charge players anything in v1? | No. Player Free covers the whole core loop; Player Pro at the 59 EGP test price unlocks convenience features only after the venue side proves revenue. A player paywall before venues exist starves the marketplace. |
| Commission or subscription for venues? | Subscription only, per the fairness rules. Kourtiva sells subscriptions; Yalla Hagz takes commission. We take subscription so the owner never pays twice on the same booking. |
| WhatsApp or Telegram for the owner digest? | Telegram for the owner (free, already used by HQ tooling), WhatsApp utility templates for players who opt in (about US$0.0036 per message, sourced 2026-11-12). |
| PWA-only or native from day one? | PWA in M1-M3, Expo in M4. The PWA must be good enough that the native app is an upgrade, not a rescue. |
| One sport or multi-sport at launch? | Football 5-a-side first, padel and padbol as the same slot engine in M5. The slot model already carries `sport`; the UI does not pretend to be multi-sport before the venues exist. |
| Egyptian-only or international at launch? | Egypt first (Arabic dialect, EGP, Paymob/Fawry/InstaPay), English always present. The global claim stays honest: the product works anywhere a venue lists it, but marketing spends only where venues are. |
| PDPL licence before or after launch? | Before collecting real Egyptian personal data at scale. Development and emulator data are unaffected; the M6 gate requires the licence path answered by the lawyer. |
| Do we build the position coach before or after the booking core? | After. It is an M5 AI feature riding on real match data; shipping it early produces suggestions with no data behind them. |

---

## 12. Launch and marketing

The launch is a supply-side beachhead, not a billboard campaign. Order matters: venues first, players second, paid anything last.

**Phase L0 (before any public page):** 3 to 5 real pitches in one area (New Cairo or Maadi, decided by where the owner can physically visit), each with a written agreement, real photos, real prices and a named owner contact. The pitch pages go live only when the data is real.

**Phase L1 (quiet launch):** the site and the PWA go live on both hosts, Arabic first. The owner personally onboards the first venues (the owner-actions list in section 13 covers the accounts). No ads, no influencer spend. The first players arrive through the venues' own WhatsApp groups and the "book without calls" pitch to owners.

**Phase L2 (first community):** one area, one weekly recurring match per venue, the Squad feature doing the retention work. Owner testimonials with numbers (utilisation, no-shows) become the sales material for the next five venues.

**Phase L3 (paid and broader):** only after M6 gates pass (lawyer, PDPL path, real charge proven). Channels in order: venue-owner outreach (the buyer), player WhatsApp community seeding in the covered areas, Arabic SEO on the queries in the DEEP plan section 5.4 ("حجز ملاعب كرة قدم القاهرة" and the slang variants), `llms.txt` and structured `SportsApplication` JSON-LD for AI answer engines, and the 12-week calendar sketched in `plans/sir-hagoozat-DEEP.md` section 5.4.

**Marketing rules:** no fake players, fake pitches, fake ratings or invented counters anywhere a user can see (the "50K players" claims of competitors are exactly what we refuse to copy). Every published number is real and dated. Arabic copy is Egyptian dialect for players; MSA only in legal pages. No marketing messages to users who did not opt in (PDPL consent records). No ad spend until the owner approves a cap; the default cap is 0.

---

## 13. Only the owner can do

Buy the domain and point it at both hosts. Create and fund the Paymob and Fawry business accounts and paste the keys into the project's ignored env file. Sign in once on the Google OAuth screen so the branding is right. Talk to three real pitch owners, or approve the outreach text. Lawyer and accountant. Buy the code-signing certificate later. Create the Play Console and Apple developer accounts when the reinvestment ladder allows.

Everything else is an agent's job.

---

## 14. Sources and files

- Canonical competitor study with dated links: `D:/Projects/_SIR/ops/competitors/sir-hagoozat.md`
- The ten build briefs: `D:/Projects/_SIR/ops/briefs/sir-hagoozat-tasks.md`
- Shared kit: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`
- AI chain: `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`
- Quality charter: `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`
- Desktop and Windows standard: `D:/Projects/_SIR/plans/WINDOWS_APP_STANDARD.md`
- Legacy sources, read-only: `D:/Projects/SIR Hagoozat/legacy/11Players`, `legacy/EGFootball5`, `legacy/Hagoozat Elite`
- Legacy facts and red flags: `D:/Projects/_SIR/ops/inventory/11Players.md`, `EGFootball5.md`, `Merged-sites.md`
- Owner ideas: `D:/Projects/_SIR/ops/TICKTICK_MAP.md` and `plans/PROJECT_MERGE_RECORD.md`
- Decision for every unplanned idea (module or own project, with the reason and the lawful-data rules): `D:/Projects/_SIR/plans/BACKLOG_IDEAS_DECISIONS.md`
