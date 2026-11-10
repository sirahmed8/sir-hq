# PLAN: SIR Hagoozat (Wave 5, public product, not started)
Audited 2026-11-10. Replaces `Hagoozat Elite` (Merged sites), `11Players` and `EGFootball5` (all in `legacy/`, kept until M6). Public product, free for players, paid tier in EGP, pitch owners pay a monthly fee.

## 1. Purpose (plain words)
Book a five-a-side football pitch in Egypt in a few taps, split the price between the players, and get balanced teams. Players find a game and a pitch; pitch owners fill empty hours and see who booked.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Hagoozat` |
| GitHub (private) | `sirahmed8/sir-hagoozat` |
| Stack (default) | Next.js App Router on Cloudflare Pages/Workers, Firebase Auth (Google) with server-verified ID token, Firestore with deny-by-default rules and transactions, R2 for private receipt images |
| Domain | candidates `hagoozat.app`, `hagoozat.com` (owner checks and buys; price "(unsourced, verify)"). Until then `sir-hagoozat.pages.dev` |
| Platforms | Web + PWA: planned (first). Android and iOS via Expo: M6+ after web has real bookings. Owner dashboard: web. Windows, macOS, Linux, watch, TV: skipped (no need). Widgets: skipped for v1 |
| Money | Free for players. Pro (priority booking, stats, player cards, no ads) at 59 EGP/month is the old plan's number: treat as a test price, "(unsourced, verify)". Pitch owners pay a monthly fee (amount decided after talking to 3 real owners). EGP first, USD/SAR/AED toggle. "Subscriptions launching soon" + email capture until Paymob/Fawry keys exist |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is the HQ setup note (2026-10-30, "nothing is built yet"); commits are setup and plan only (10).
Legacy facts (from `ops/inventory/Merged-sites.md`, 2026-10-29, nothing re-run): the merged app has 29 pages and 7 API routes against 55 and 36 pages in the originals, so it is not a complete merge; admin gate is client-side; a `dev_signature` payment bypass existed in an original (stopgap separate); 11Players has 62 files over 300 lines and a fake-players generator in admin; EGFootball5 API routes are dead on static hosting; README claims such as "281/281 tests" were not verified.
Real data status: no real pitches, owners or players are loaded anywhere. A marketplace with no real pitches is empty, so seeding is a growth task (section 10), never fake rows.

## 4. Security and conduct rules
1. Owner/admin from a server-verified token plus allow-list, fail closed. Test: client-side flag change grants nothing.
2. Payments: webhook signature with timestamp inside the signed body, idempotent activation. Test: tampered, replayed and unsigned events are rejected. No `dev_signature` or any bypass flag in any build.
3. Booking and deposits are Firestore transactions with idempotency keys and a 15 minute slot lock. Test: 20 parallel requests for one slot produce exactly one booking.
4. Receipt images (InstaPay, Vodafone Cash screenshots) are private files in R2 with signed URLs, size and type checked, auto-deleted 90 days after verification (default, adjust with lawyer). Players' phone numbers are visible to a pitch owner only after a booking.
5. Rules deny by default, per-user and per-pitch-owner claims, emulator tests (cross-tenant read fails).
6. Sessions in HttpOnly SameSite=Strict cookies, rate limits on auth, booking and AI, zod validation.
7. Merge old accounts by verified email only, never by display name.
8. No fake players, ratings or bookings in any non-test path.

## 5. Shared pieces (SIR Platform; build as internal packages first)
`owner-auth`, `signed-webhook`, `billing-fallback`, `ai-proxy`, `legal-pack`, `i18n`, `ui/styles/hooks` (the first kit already has the spring tab bar and Paymob test modal; Platform checkpoint names Hagoozat as the first consumer), Telegram sender. Pitch-owner dashboard analytics reuse the common owner-dashboard pattern from SIR Business.

## 6. Screens and entities
Landing, Sign in, Find a pitch (map or list, filters), Pitch page, Booking wizard (linear, steps unlock in order), Deposit and receipt upload, My bookings, Match page (squad balance, split bill, ratings), Communities, Notifications, Profile (player card), Pricing, Support, Owner dashboard (bookings, revenue, schedule, verification queue), Admin, Legal. Entities: User, Pitch, Slot, Booking, Deposit, Match, Squad, Rating, Community, Notification, Ticket, Subscription, Lead.
Five states, Arabic RTL first (Egyptian dialect copy) and English, themes, 320 px to 4K, WCAG 2.2 AA, own logo.

## 7. AI and support
Squad balancer with a plain-words explanation ("why these teams"), position coach, support assistant grounded in `docs/help`. Chain via `ai-proxy` with fallback, quota 5 per day free, owner unmetered, kill switch, eval sets in Arabic and English (balance fairness test: rating-sum difference within a set bound). Balancer itself must work without AI (pure algorithm); AI only explains.

## 8. Operations
Booking-failure alerts, payment reconciliation job (daily compare of gateway records to bookings), nightly Firestore export, weekly Telegram report (bookings, revenue in EGP, no-shows, errors), support triage by assistant, status JSON, emergency alerts (payment mismatch, outage). Ad spend: none until the owner sets a cap.

## 9. Launch package, legal, visibility
Owner buys domain, Paymob and Fawry business accounts (test mode in code), Play Console later. Legal pack from data inventory (privacy, terms, refunds and cancellation of bookings, cookies, DPA for pitch owners, sub-processors); Egypt PDPL 151/2020 and consumer rules as tasks, exact text "(unsourced, verify)", lawyer review before paid launch. Tax and e-invoicing for pitch-owner fees: "(unsourced, verify)" with the accountant step in the owner list.
Visibility: Arabic queries by area ("حجز ملعب خماسي في ..."), one landing page per city/area that has real pitches, pitch pages with `LocalBusiness`/`SportsActivityLocation` JSON-LD only for real, consenting owners, `llms.txt`, facts page, Google Business Profile guidance for owners, weekly AI-answer check. App store listing text drafted for later.

## 10. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Deep scan, setup, CI | deep-scan report; parity matrix of 55+36+29 pages; green Actions URL |
| M1 | Core slice | pitch list and page from Firestore emulator, booking wizard, parallel-booking test passes |
| M2 | Parity | deposit queue, matches, balancer, communities, owner dashboard with real counts; parity checklist ticked per route |
| M3 | Security, legal, billing | webhook tests, rules tests, billing fallback render test, legal pages generated |
| M4 | AI | balancer explanation eval, support assistant eval |
| M5 | Quality | screenshots 390/1280, LTR/RTL, Lighthouse mobile 90+ |
| M6 | Release | import dry run counts, 301 redirects from the three old hosts, keys rotated, first 3 real pitches onboarded |

## 11. Next 10 tasks (each under 2 hours)
1. Deep scan of the three legacy apps into a parity matrix (route, owner app, keep/drop). Files: `.sir/reports/parity.md`. Check: every route listed in the inventory has a row.
2. Scaffold app, tokens, RTL, health route, CI. Check: build green and Actions URL.
3. Data model and Firestore rules for Pitch, Slot, Booking, Deposit. Files: `firestore.rules`, `docs/data-model.md`. Check: rules compile in the emulator.
4. Emulator rules tests (own booking readable, other player's not, owner sees only own pitch). Check: tests green.
5. Slot lock plus booking transaction with idempotency key. Files: `apps/web/src/server/booking/`. Check: parallel test of 20 requests yields 1 booking.
6. Pitch list and pitch page with five states. Check: screenshots at 390 px.
7. Booking wizard: step 2 not reachable before step 1 validates. Check: e2e test tries to jump and is blocked.
8. Squad balancer pure function with tests (no AI). Files: `packages/balancer/`. Check: property test, rating-sum difference below the stated bound.
9. `billing-fallback` page with lead capture. Check: lead doc created; invalid email rejected.
10. Owner list file `docs/OWNER_STEPS.md` plus pitch-owner onboarding one-pager (Arabic) to approach 3 real pitches. Check: file exists; no invented partner names.

## 12. Risks and open questions (defaults)
- Two-sided cold start: default is launch in one area with 3 to 5 real pitches before any ad or SEO push.
- Manual payment methods (InstaPay, wallets) mean receipt fraud: default is manual verification queue plus owner confirmation, no auto-approval.
- Gateway terms and fees for Paymob/Fawry: "(unsourced, verify)" at build time from official docs.
- Port volume (three apps): default is port by feature behind the parity matrix, never copy files.
- Existing Egyptian competitors found by search on 2026-11-10: Hareefa (`https://hareefa.com/`) and Yalla Hagz (`https://www.yallahagz-eg.com/`). The cold start is harder than the old study assumed; the sourcing tasks at the end of `plans/competitors/sir-hagoozat.md` come before any marketing.
- Market size claims: none in this plan; the competitor study (`plans/competitors/sir-hagoozat.md`) must carry links or the "(unsourced, verify)" tag.

## 13. Only the owner can do
Buy the domain; create Firebase, Cloudflare, Paymob and Fawry accounts and paste keys into one `.env`; sign in for Google OAuth screen branding; talk to real pitch owners (or approve outreach text); accountant and lawyer review; store developer accounts later.
