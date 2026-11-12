# PLAN: SIR Access Map (small independent project, GLOBAL product, rebuild from zero)

## Vision (owner, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` sections 5, 6 and 8)

SIR Access Map is its own small independent project with the same premium standard as every other product: a crowd-checked map of the places that are really usable by people with disabilities, for Egypt and the Arab world first and the world second. It is not a module of any other product. The old `plans/accessibility-map-module-note.md` (r51, which made it a module of SIR Life Part B) is superseded by this file; the git history keeps it, and `plans/BACKLOG_IDEAS_DECISIONS.md` section 3.4 records the owner's decision and the honest cost of it.

**Version 1.0.0.** Written 2026-11-12 (round r54, HQ). The canonical competitor study is `D:/Projects/_SIR/ops/competitors/sir-access-map.md` (dated 2026-11-12, with sourcing tasks still open). The first ten build tasks for the free agents are in `D:/Projects/_SIR/ops/briefs/sir-access-map-tasks.md`.

**Truth rule for this plan.** Nothing here is called working unless a reviewer saw it today. The product has never been built: `D:\Projects\SIR Access Map` does not exist yet, no Firebase project exists for it, and no GitHub repo exists for it. The decision file assumes the repo `sirahmed8/sir-access-map`; that assumption is unverified and is re-checked in M0. Verified today: this plan and the competitor file were written in this round.

**Product class: GLOBAL.** Anyone in the world can use it, accounts and subscriptions exist, every platform is planned, the owner has an owner-only analytics page, the site is hosted twice (Firebase Hosting and Vercel), and a paid subscription gives the owner every permission inside the product. It is listed in `PRODUCT_DIRECTION_2026-11-12.md` section 8 among the small independent projects created from the unplanned ideas. **It is built last**, after the other small projects, per `BACKLOG_IDEAS_DECISIONS.md` section 7; the owner may drop it at any time because nothing else depends on it.

**Build-order honesty (carried from the decision file).** A separate project means a separate Firebase project, a separate repository, a separate domain and a separate store listing for a small audience. To keep that cost honest this plan reuses the shared kit map layer and the shared map provider account wherever the kit allows, keeps the codebase deliberately small, and ships the map, the evidence flow and the claims before any paid feature.

---

## 1. Who it is for, and the promise

**For the person with a disability.** The wheelchair user, the person with low vision, the person who is hard of hearing, the older adult, the parent with a stroller, the tourist who cannot climb stairs, who needs to know before leaving home whether a place can actually be used. The one-line promise:

> Know before you go: is this place really usable for me, and how do I get there without a barrier?

**For the family member or caregiver.** The person planning an outing for someone else, who needs the same answer plus a route that avoids barriers. Same promise, same app, a "planning for someone" view that hides nothing and adds nothing private.

**For the place owner.** The clinic, restaurant, mosque, shop, station or park that wants its accessibility information to be correct, because wrong information costs them customers and, worse, strands a visitor at a door. The one-line promise for that side:

> Claim your place, prove your accessibility, and keep the record true.

**For the contributor.** The wheelchair user, the parent, the nurse, the delivery driver who sees a ramp, a broken lift or a blocked entrance every day and can fix the map in two minutes with a photo. The promise:

> See a barrier or an access feature? Two minutes and a photo fixes the map for everyone.

**The end state we sell.** A visitor opens the app in Cairo, searches "pharmacy near Tahrir" or drops a pin, and sees each place with its accessibility profile: entrance (step-free, door width, ramp), interior (lift, wide aisles), toilet (accessible, changing table, baby change), parking (designated bays, drop-off curb), help features (braille signage, audio announcements, staff assistance, quiet hours), each feature with a verified-on date, a photo and a confirmation count. They tap "route me there" and get a route that avoids known barriers, with each avoided barrier named and dated ("lift at this station reported out of service on 3 Nov"). A place owner taps "claim this place", proves ownership (a document or a callback to a business number), uploads photos and keeps the entry correct. A moderator queue holds every new or changed claim until it passes the evidence rules.

**Not in v1:** no ads, no fake places, no fake reviews, no invented accessibility ratings, no invented users or counts. An empty area shows an empty state with one action (drop a pin and add the first verified place). No place publishes from a single untested report: photo plus feature list plus a second-user confirmation or an owner claim. The submitter is never named publicly.

---

## 2. The ten competitors, and where we win

Full table with sources, dates and the second ring: `D:/Projects/_SIR/ops/competitors/sir-access-map.md` (dated 2026-11-12).

| Competitor | What it proves about the market | Our edge |
|---|---|---|
| Wheelmap.org | Crowdsourced accessibility ratings at scale work; traffic-light ratings are understood | Egypt/Arab-first coverage, full feature set per place, photo-evidence moderation, owner claim, route planning, dated claims |
| AccessNow (AXSMap) | Deep accessibility taxonomy and B2B partnerships are real | Consumer crowd layer with photo proof, Egypt first, place owners self-serve |
| iAccessLife | Feature-level ratings and company feedback channels exist | Arab-market coverage, owner claim and correction, route planning, photo evidence as publish gate |
| Wheelmate | Focused "nearest accessible X" works | A whole place map, not two categories, confirmations and claims, route planning |
| WheeLog! | Real routes users took are valuable data | Route planning guided by verified features, works without a pre-logged crowd |
| HandicapX | Granular ratings beyond yes/no matter (cleanliness, findability) | Every place type, feature-level ratings, owner corrections |
| Mapp4All | Per-disability filters and business self-listing are proven ideas | Egypt-first density, free claim flow, confirmations instead of pay-to-list |
| Entaleq (انطلق, Egypt) | The idea resonates locally; a 4-point entrance audit is a real checklist | Scale, photo evidence, second-user confirmation, owner claims, route planning, maintained releases |
| أماكني (Amakiny, Egypt) | Egyptian owners once wanted to list their own places | A maintained, cross-platform, evidence-checked version of exactly that |
| Google Maps / Apple Maps accessibility layers | Platform base maps are the substrate everyone expects | A dedicated verified layer on top: photo proof, owner claims, dated features, barrier-avoiding routes with reasons |

**Category truth from the sources (2026-11-12):** the global leaders are Europe/US-heavy with thin Arab coverage; the only Egyptian products are dormant or abandoned; nobody locally does photo evidence plus second-user confirmation; the place-owner claim flow is missing everywhere; route planning that avoids barriers does not exist locally; accessibility data expires and nobody dates it; Arabic is badly served. Our product plan follows that truth instead of fighting it.

---

## 3. Features

### 3.1 Parity with the best in the category (must ship)

| Feature | Why it is in the list | Source of the requirement |
|---|---|---|
| Map of places with an accessibility profile per place | The core promise | Wheelmap, AccessNow, Entaleq |
| Feature-level ratings, not just accessible yes/no (entrance, lift, toilet, parking, braille, audio, quiet hours, door width, aisle width) | Granularity is what users actually need | HandicapX, iAccessLife, Mapp4All |
| Photo evidence attached to each feature claim | Trust is the gap everywhere | Our design, informed by Wheelmap photo uploads |
| Second-user confirmation before a place or feature publishes | Nobody local does this | Our design (decision file rule) |
| Verified-on date and re-check window per feature; stale claims flagged | Accessibility data expires | Our design; competitor gap |
| Place search by name, category and "near me", filter by needed feature | Base expectation | All competitors |
| Category coverage: shops, clinics, pharmacies, restaurants, cafes, mosques, stations, parks, government offices, ATMs | The owner's stated scope | Brief scope |
| Arabic Egyptian first, English second, RTL-first | The clearest local gap | Entaleq proves Arabic demand |
| Accessibility of the app itself (WCAG 2.2 AA, screen-reader labels, large text, high contrast) | A product for disabled users must itself be usable | The product's own audience |
| Route planning that avoids known barriers and names each avoided barrier | The differentiator | WheeLog proves routes matter; nobody does barrier-avoidance locally |
| Place-owner claim flow: prove ownership, upload proof, correct the entry | The missing half everywhere | أماكني proved demand, then died |
| Report-a-place and report-a-feature on every entry | Legal and trust baseline | Shared kit security baseline |
| Data export and one-tap account deletion | Legal and trust baseline | Shared kit security baseline |
| Support assistant grounded in the help source | Cuts support time | Shared kit help-center |
| Offline-capable saved places and last-viewed map tiles (PWA) | Basements, old buildings and poor signal are the norm | Our design; nobody claims it locally |

### 3.2 The owner's own ideas, carried forward from legacy and TickTick

Every line says where it came from, so nothing gets silently rebuilt thinner than what he already asked for.

| Idea | Source | Status in this plan |
|---|---|---|
| Wheelchair access, ramps, lifts, accessible toilets, parking, braille or audio help, quiet hours | Brief scope (PRODUCT_DIRECTION section 8) | Feature checklist in 3.1 and the data model in 5.3 |
| Crowd-sourced with photo evidence and confirmations | Brief scope | M2 evidence and confirmation engine |
| Route planning that avoids barriers | Brief scope | M4 route engine |
| Place owner can claim and correct it | Brief scope | M3 claim flow |
| Shops, clinics, stations, restaurants, mosques named in scope | Brief scope | Category taxonomy in 5.3 |
| Users add and confirm entries | TickTick idea 26 / BACKLOG_IDEAS_DECISIONS 3.4 | M2 submission and confirmation flow |
| Accessibility info carries a date and an expiry for parts that change (a lift out of service) | BACKLOG_IDEAS_DECISIONS 3.4 rules | Verified-on date and re-check window in the data model |
| Submitter never named publicly | BACKLOG_IDEAS_DECISIONS 3.4 rules | Privacy rule in 5.7 |
| Module-of-SIR-Life idea (superseded) | plans/accessibility-map-module-note.md | Explicitly dropped: the owner decided own project; the shared map-layer lesson is kept in 5.6 |

**Explicitly dropped from the legacy note:** the decision to make it a module of SIR Life Part B (the owner's later message supersedes it); the single `AccessibilityPOI` model with only `features[]` and `photos[]` (replaced by the richer evidence and expiry model in 5.3); the assumption that no commercial model is possible (kept honest in section 7 as a test-price outline the owner confirms); the "no owner action" line (M0 now has real founder steps).

### 3.3 Explicitly out of scope for v1

Turn-by-turn voice navigation inside the app (we hand off to the platform map app with the route), indoor mapping of specific venues, accessibility certification or legal verification services, any feature that needs a government data feed we do not have a lawful source for, and payment for place owners beyond the optional verified badge in the pricing outline. Those wait for a sourced data agreement or a milestone decision.

### 3.4 Lawful data and sources

No scraping of Google Maps, Wheelmap or any competitor. All place and feature data is user-submitted and owner-claimed. The base map is OpenStreetMap or the licensed map provider decided in M0 (`docs/DATA_SOURCES.md` records the licence and last-checked date). Published government accessibility standards and any official Egyptian accessibility lists are cited with a link and a date as a checklist baseline, never copied verbatim. Every data source is listed in `docs/DATA_SOURCES.md`.

---

## 4. Platform matrix

Standing rule (owner, 2026-11-12): every product ships on all platforms, so web, Windows, macOS, Linux, Android and iOS are all required for SIR Access Map. Wear OS, watchOS, TV and car are not in that list, so they are skipped in v1 with a written reason, not left in silence.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required | The whole product: map, search, place profile, submit, confirm, claim, route plan, saved places, owner console | Nothing pending |
| PWA (installable, offline) | Required | Install from the browser, offline saved places and last-viewed tiles, offline feature checklist for submission drafts | Native shell if the PWA proves weak on low-end Android |
| Windows | Required (M5) | Installable PWA from day one, then a real NSIS installer with the same Google sign-in and self-update | Signed installer (owner buys the certificate) |
| macOS | Required (M5) | Installable PWA from day one, then an unsigned DMG from the same Electron build | Signed build when the owner has an Apple account |
| Linux | Required (M5) | Installable PWA from day one, then AppImage and .deb from the same Electron build with a .desktop entry | Signed package |
| Android phone and tablet | Required (M4) | Expo app: the same account, map, submit with camera, confirm, claim, route, saved places | Play Store when the reinvestment ladder allows |
| iPhone and iPad | Required (M4) | Expo app, same account and data, tablet layouts | App Store or SideStore (needs a paid Apple account, the owner decides) |
| Wear OS | Skipped in v1 | Nothing | A "nearest accessible place" complication, decided with an ADR |
| watchOS | Skipped in v1 | Nothing | Same ADR as Wear OS |
| TV (Android TV and Apple TV) | Skipped in v1 | Nothing | Nothing planned; no use case found |
| Car (Android Auto and CarPlay) | Skipped in v1 | Nothing | A "find accessible parking near me" action only if users ask |
| Widgets and live activities | Part of M5 | Android Glance and iOS WidgetKit: saved places and "accessible X near me" | Richer surfaces later |
| Browser extension | Skipped | Nothing | Nothing planned |
| Docker and self-host | Skipped | Nothing | Not a product need here |

**Rule:** every platform shares one Firebase project, one account and one dataset. No platform ever carries its own copy of the rules. The Windows, macOS and Linux builds come from one Electron shell and one release feed, so an update reaches all three at once.

---

## 5. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. That file is the shared standards kit every product builds against; SIR Platform was cancelled as a project on 2026-11-12, so there is no extraction target any more. SIR Access Map is a GLOBAL product, so it adopts all twenty sections of the kit as internal `packages/*` with the kit names and interfaces, and when it hardens a piece that other products need, that piece goes back into the kit file and HQ queues the adaptation for the others.

### 5.1 Shape

```
apps/web        Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens
apps/api        Route handlers that need secrets and long tasks (webhooks, cron, AI proxy, photo moderation, claim verification)
packages/core   Domain types and zod schemas: Place, PlaceCategory, FeatureClaim, FeatureKey, PhotoEvidence, Confirmation, Claim, RoutePlan, SavedPlace, User, ModerationItem
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
- Rate limits on sign-in, place submission, photo upload, claim creation, confirmation, route planning and AI calls.
- A contributor account is a normal account; no phone verification is required to confirm a place (the confirmation itself is the trust signal), but a claim by a place owner requires proof of ownership.
- Owner accounts get a second factor offer.
- Test: a forged token gets 403, a client-side flag flip gets nothing, a non-owner token on `/owner` gets 403.

### 5.3 The data model (the heart of this product)

```
Place            id, name, category, lat/lng, address_text, city, osm_ref?, status, created_by_uid (never public), created_at
PlaceCategory    enum: shop, clinic, pharmacy, restaurant, cafe, mosque, station, park, office, atm, hotel, other
FeatureKey       enum: step_free_entrance, ramp, door_width_ok, lift, wide_aisles, accessible_toilet,
                 baby_change, designated_parking, drop_off_curb, braille_signage, audio_announcement,
                 staff_assistance, quiet_hours, hearing_loop, guide_dog_welcome
FeatureClaim     id, place_id, feature_key, state (yes/no/partial/unknown), note, photo_ids[],
                 claimed_by_uid, claimed_at, verified_on, recheck_after, status
PhotoEvidence    id, place_id, feature_claim_id?, storage_path, content_type, size, uploaded_by_uid,
                 created_at, moderation_state
Confirmation     id, place_id or feature_claim_id, user_uid, agrees (yes/no), note, created_at
Claim            id, place_id, claimant_uid, proof_type (document|callback|domain), proof_ref,
                 status (pending|verified|rejected), reviewed_by, created_at
RoutePlan        id, user_uid, from, to, waypoints[], avoided_barriers[{place_id, feature_key, reason, since}],
                 created_at, expires_at
SavedPlace       id, user_uid, place_id, note, created_at
ModerationItem   id, type (place|claim|photo|feature), target_id, reason, state, created_at, resolved_at
User             uid, display_name (public contributor name or "anonymous"), role, created_at
```

**Publish rules (the truth engine):**
- A `Place` is `published` only when it has a name, a category, coordinates and at least one `FeatureClaim` that is `confirmed` (two distinct users agree) or `owner_verified`.
- A `FeatureClaim` becomes `confirmed` when a second distinct user confirms it; a single report shows as `reported` (visible with a "reported, unconfirmed" badge, never as fact).
- A `Claim` verified by the owner marks its `FeatureClaim`s as `owner_verified`, which counts as a confirmation but is labelled "claimed by the place".
- `verified_on` is set when a claim is confirmed; `recheck_after` is 180 days by default for stable features (entrance, parking) and 90 days for changeable ones (lift, accessible toilet, quiet hours). Past `recheck_after` the feature shows a "needs re-check" badge, and the owner of the product sees it in the moderation queue.
- Every `FeatureKey` traces to a written source in `docs/DATA_SOURCES.md`: the Egyptian Building Code for persons with disabilities gives measurable thresholds (corridors and doorways at least 1.2 m, ramp slope at most about 5 percent, entrance curb height at most 15 cm, designated parking bays with markings), and Law No. 10 of 2018 Articles 39 to 46 give the legal hook. A feature that cannot be traced to a source or marked "(unsourced, verify)" does not ship.
- Photo upload is size- and type-checked before storage, stored with signed URLs, auto-deleted 90 days after the place or claim is removed.
- A place owner sees only their own claimed places in their console; enforced in Firestore rules and re-checked on the server.

### 5.4 Owner-only analytics page

- Route `/owner`, server-verified owner token, 403 for everyone else.
- Real metrics only, read from aggregates not raw collections: users, published places, pending moderation items, claims pending verification, confirmations per day, photos uploaded, route plans created, feature staleness count (claims past `recheck_after`), AI cost, error rate, subscriptions, revenue in EGP and the visitor currency.
- A second section for the place-owner role: their claimed places, pending corrections, verification status. Each owner sees only their own places, enforced in Firestore rules and re-checked on the server.
- No invented numbers anywhere: an empty metric shows a dash and the reason, never a zero dressed as a fact.

### 5.5 AI with the fallback chain

Chain from `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`: Gemini `flash-lite-latest`, then `flash-latest`, then any Gemini text model, then OpenRouter free models, then other free providers, then the local model on this PC. One Gemini key and one OpenRouter key per product, created on this product's own project, stored only in the ignored env file and the Vercel environment, never printed, never committed.

What AI does in this product, and what it must never do:

| Feature | AI role | Hard rule |
|---|---|---|
| Place-name and category suggestion | Suggest a category and normalise a name on submission | Suggestion only; the user confirms before save |
| Photo moderation assist | Flag a photo that does not show the claimed feature (blur, wrong subject, screenshot) | Advisory only; a human moderator decides; never auto-publishes or auto-deletes |
| Claim proof assist | Read an uploaded ownership document and extract the business name for the reviewer | Extracts fields for a human reviewer only; never verifies on its own |
| Route explanation | Write the plain-words reason a route avoids a barrier | The route and the barrier data are computed from real claims; AI only writes the sentence |
| Support assistant | Answer from `docs/help/*.md` only | Refuses anything not in the help source, and says so |
| Weekly owner report draft | Draft the summary the Telegram sender sends | Numbers come from the database, the model only writes the sentence |

Free users get 5 AI calls per rolling 24 hours with a visible badge, the owner is unmetered, `AI_ENABLED` is the kill switch, a daily cost cap lives in `config/limits.json`, and every call logs which provider answered (never the content). Arabic and English eval sets exist before the feature ships, and the runner exits non-zero below the threshold.

### 5.6 Data, map provider and money

- Firestore with deny-by-default rules, per-user and per-place-owner claims, emulator tests including a cross-tenant read that must fail.
- A place submission, a feature claim and a confirmation are Firestore transactions with idempotency keys. Test: 20 parallel confirmations from distinct users on one claim produce exactly one confirmed state and clean rejections for duplicates.
- The base map provider is decided in M0 and recorded in `docs/DATA_SOURCES.md`. The r61 refresh (2026-11-12) compared the official pricing pages: Geoapify free plan (3,000 credits per day, commercial use allowed with attribution, routing plus geocoding plus isochrones) is the recommended v1 provider; Mapbox free tier (50,000 GL JS loads per month) is the fallback; Google Maps Platform Essentials (10,000 free Dynamic Maps loads and 100,000 free Map Tiles API tiles per month) is viable but needs a billing account, which is an owner step; MapTiler and Stadia free tiers are non-commercial and rejected; the public OSM tile server has no SLA and is for development and offline tiles only, never the production host. Route planning in v1 uses the provider's routing or OSRM on OSM data; the "avoids barriers" layer is ours on top.
- Signed webhook for any future payment provider (HMAC-SHA256, timestamp inside the signed body, server-side verification, idempotent activation). Test: tampered, replayed, unsigned and wrong-timestamp events are rejected.
- No wallet or card payment is required for v1 publishing; the billing fallback page collects leads for the paid tiers in section 7.

### 5.7 Security and privacy baseline

Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI. A CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent, with Reject All as prominent as Accept. One-tap data export and one-tap deletion. Rate limits on auth, submission, upload, claim, confirmation, route and webhook endpoints. No fake data in any path a user can see. The submitter of a place or feature is never shown publicly: the public record shows "community verified" or "claimed by the place", never a name tied to a submission unless the contributor opts in to a public profile.

### 5.8 Hosting and delivery

- **Firebase Hosting** is primary. **Vercel** is the second host, the same repository imported with the Vercel CLI, the same build, the same environment variables on both. Both addresses are curl-checked and written into the project checkpoint.
- Static hosting cannot run route handlers, so every secret, webhook, AI call and photo-moderation call lives in the Firebase Functions or the Vercel function side, never in the client bundle.
- A service worker caches saved places, last-viewed tiles and submission drafts. Background sync sends queued actions when the connection returns.
- Daily Firestore export to a private bucket, a monthly restore test, a health endpoint at `/api/health`, a status JSON, a nightly error digest and a weekly Telegram report at a round hour.

---

## 6. Premium quality bar

This is the floor from `D:/Projects/_SIR/standard/23-premium-code-bar.md` and `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`, written for this product.

**Motion, Apple level.**
- One shared spring config across the app: stiffness 300 to 400, damping 28 to 30, transform and opacity only, no layout thrashing, 120 Hz safe.
- Every sheet, drawer, modal and panel opens and closes with the same spring. An open-only animation is a defect.
- The place-profile expansion and the route reveal settle with a spring; the feature checklist animates on first view. Micro-interactions 100 to 150 ms, standard 200 to 300 ms, large 300 to 500 ms. Press scale 0.98. Reduced-motion path for every animation.
- The active tab shows its label and the others show an icon only, the active tab scrolls into view on load and on change, and the bottom bar never vanishes when the keyboard opens.
- Skeletons match the final geometry, optimistic feedback lands under 100 ms, and no white flash on theme change.

**Two languages, one layout.**
- Egyptian Arabic first for the Egyptian and Arab audience, English second for the international market, MSA only in legal pages. Both shipped together, never one as a partial translation.
- RTL designed first: logical CSS properties only, flipped directional icons, Arabic line heights, never a mirrored afterthought. The map itself is direction-neutral; all chrome, lists and sheets are RTL-correct.
- Every text input detects Arabic or Latin per character as the user types and moves the caret and the direction live. Every mixed run is isolated with `<bdi>` or `unicode-bidi: isolate`. The words "RTL" and "LTR" never appear to the user.
- Currency auto-detected from the visitor locale and IP, with a manual override on top. Dates and times formatted with `Intl`.

**Five states on every screen.**
Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake place, a fake rating, a fake photo or a fake number.

**Accessibility (the product must practice what it maps).**
WCAG 2.2 AA, and stricter where the audience demands it: every control has an accessible name in both languages, touch targets at least 44 px with no covered hit area, full keyboard path on every screen, visible focus, zoom from 80 to 200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured, and a colour pair that passes contrast in light, dark, system and high-contrast themes. Screen-reader labels describe accessibility features in plain words ("step-free entrance, confirmed by 3 visitors"), not raw enum names. A "large text and high contrast" quick toggle lives in settings because the audience needs it.

**The look.**
One design system: tokens for colour, spacing on a 4 and 8 px grid, radii, shadows, type and motion. Seed colour a calm accessible teal `#0F766E` for a public-good map product, neutral canvas, accent only for primary actions and key status. No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. One component per control, never two. Arabic screen face: IBM Plex Sans Arabic, Cairo or Tajawal.

**Native app feel.**
The browser's text selection and the right-click menu are disabled site-wide and replaced by the app's own menu with in-app actions and a refresh. Normal select, copy and paste inside real input fields still work.

**Evidence before the word done.**
Screenshots at 320, 390, 768, 1280 and 1920 px, in Arabic and English, in light and dark, plus 3840 px once. Playwright on the critical journeys (search, place profile, submit, confirm, claim, route). Lighthouse mobile 90 or better. A click-target audit in CI. The self-audit loop runs until two clean cycles.

---

## 7. Free tier and fair pricing (EGP and USD)

These are **test prices**, not published prices. They are the outline the owner confirms with real users and the official gateway fee schedule before anything is charged. The USD column uses 48 EGP per 1 USD, which is "(unsourced, verify)" and is recomputed from the live rate on the pricing page. This product's audience includes people with disabilities and low-income families, so the free tier is deliberately generous and the paid tier sells convenience and power, never access to safety information.

| Plan | Who | EGP | USD | What it includes | Rule |
|---|---|---|---|---|---|
| Explorer Free | Any visitor | 0 | 0 | Full map, search, place profiles, feature ratings with dates, route planning (limited to 10 per day), submit and confirm places, save up to 10 places, offline saved places | The core safety information is never behind a plan |
| Explorer Pro | Frequent users, caregivers, tourists | 49 per month or 399 per year (test) | about 1.00 per month or about 8.30 per year | Unlimited route plans, unlimited saved places, offline map tiles for saved areas, "alert me when a saved place's accessibility changes", priority support | Cancel any time, the plan lapses at the end of the paid month |
| Contributor | Anyone who adds places | 0 | 0 | Unlimited submissions and confirmations, contributor stats on own profile (opt-in) | Contribution is never charged; the map depends on it |
| Place Owner Free | A place owner | 0 | 0 | Claim one place, correct its entry, respond to reports, see basic view counts | A place owner is never charged to be correct |
| Place Owner Verified | A business that wants the badge | 199 per month or 1,990 per year (test) | about 4.15 per month or about 41.50 per year | Verified badge, priority in "near me" results for users filtering by its features, analytics on profile views and route plans through the place, multi-location claim for a small chain | One fee only; the badge is the product, never pay-to-rank beyond the published priority rule |

**Fairness rules written into the product.**
1. A user never pays to see whether a place is accessible. Safety information is free, always.
2. A contributor is never paid and never charged; a place owner is never charged to claim and correct.
3. Every price on screen is in the visitor's currency, auto-detected, with the original EGP amount next to it.
4. The verified badge buys visibility within the published rule, never the ability to mark a false feature as true: owner claims still pass the same evidence and moderation rules as everyone else.
5. No ads, in any tier, ever. The owner sets an ad spend cap of 0 until he changes it.
6. The owner of the product gets every paid feature, free, and a subscription grants him all permissions inside the owner console.

**Still open and blocking publication:** the official Paymob and Fawry fee schedules for Egypt, the tax and invoicing treatment of subscriptions in Egypt, the exact cancellation and refund wording, the map provider licence and cost tier, the Egyptian accessibility standards baseline, and the lawyer review of every legal page. Each is tagged "(unsourced, verify)" in `ops/competitors/sir-access-map.md` section 4 and in `docs/ENV.md` when the project starts.

---

## 8. Milestones M0 to M6, with acceptance tests

Every exit check is something a reviewer can run or click. "Green" means the output was seen, not assumed.

### M0: Foundations, the kit and the honest map of the market

Work: verify whether a Firebase project and a GitHub repo named `sir-access-map` already exist; if not, create the Firebase project `sir-access-map` on the free Spark plan and the GitHub repo `sirahmed8/sir-access-map` (private) as the only remote; create the project folder `D:/Projects/SIR Access Map` with `.sir/`, `AGENTS.md`, the plan pointer and the checkpoint; scaffold the monorepo (apps, packages, docs, scripts) with strict TypeScript, Tailwind v4 tokens, RTL-first styles and the shared `verify` script; design the token set and three design directions; recreate the Desktop folder kit from scratch for the new build; write `docs/DATA_SOURCES.md` including the map-provider decision.

Exit checks:
1. `D:/Projects/SIR Access Map` exists with `.sir/CHECKPOINT.md`, `AGENTS.md` and the repo remote set to `sirahmed8/sir-access-map` only.
2. `D:/Projects/SIR Access Map` contains `folder.ico` (named exactly that, never `icon.ico`) and the Desktop folder `SIR Projects/SIR Access Map` holds `folder.ico`, `SIR Access Map.lnk`, `Start SIR Access Map dev.lnk`, `Stop SIR Access Map dev.lnk`, `Open project folder.lnk` and `Versions.txt` reading version 1.0.0 and a plain status. The old kit belonged to no previous build, so M0 creates it.
3. `pnpm verify` runs typecheck, lint, tests, build and gitleaks, and the output was seen green.
4. `docs/DESIGN.md` holds three explored directions with screenshots and the chosen one, plus the token file.
5. `docs/DATA_SOURCES.md` lists every data source with its licence and its last-checked date, the map-provider decision with its licence and cost tier, and every feature checklist item traces to a source or is marked "(unsourced, verify)".

### M1: Map and place core, proven under real data

Work: the data model and the Firestore rules for Place, PlaceCategory, FeatureClaim, PhotoEvidence, Confirmation, Claim, RoutePlan, SavedPlace; the map view with search, category filter and "near me"; the place profile with the feature checklist, dates and badges; the category taxonomy and the feature enum; five states everywhere.

Exit checks:
1. The emulator rules tests pass, including a cross-tenant read that must fail and a place-owner read of another owner's place that must fail.
2. The map renders real published places only; an unpublished place never appears, and an empty city shows an empty state with one action.
3. The place profile shows each feature with its state, verified-on date, photo count and confirmation count, at 390 px and 1280 px, in Arabic and English, light and dark.
4. Search and filters show idle, loading, empty with one action, error with retry and populated, at 390 px and 1280 px, in Arabic and English, light and dark.

### M2: Evidence engine: submit, photo, confirm, moderate

Work: the submission flow (place or feature, with the feature checklist and note); photo upload with size and type checks and signed URLs; the confirmation flow (second distinct user); the moderation queue for new places, claims, photos and stale features; the publish rules from 5.3 implemented and tested.

Exit checks:
1. A place with one unconfirmed report shows as "reported, unconfirmed" and never as a confirmed feature; a second distinct user's confirmation flips it to confirmed.
2. A photo upload is refused when it is the wrong type or too large, and a stored photo is reachable only with a valid signed URL.
3. 20 parallel confirmations on one claim produce exactly one confirmed state and clean rejections for duplicate confirmers.
4. The moderation queue holds every new place and every owner claim until a moderator resolves it, and the queue shows the evidence (photos, confirmations, proof) in one view.
5. A feature past `recheck_after` shows the "needs re-check" badge and appears in the owner analytics staleness count.

### M3: Place-owner claims and the owner page

Work: the claim flow (proof types: document, callback to a business number, domain); the claimant console (claimed places, pending corrections, verification status); the owner-only analytics page; the billing fallback page with lead capture; the legal pack.

Exit checks:
1. A claim cannot be verified without proof, and the e2e test tries to verify without proof and is blocked.
2. A non-owner token on `/owner` gets 403 and a forged token gets 403.
3. A place owner sees only their own claimed places; an emulator test proves a read of another owner's place fails.
4. The pricing page shows the test prices with the currency auto-detected, plus "Subscriptions launching soon" and an email capture that creates a lead document and rejects an invalid address.
5. Every legal page exists under `/legal/*`, each marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch".
6. Both hosts answer: the Firebase URL and the Vercel URL were curl-checked, and the two addresses are written in the project checkpoint.

### M4: Route planning, community features and the two platforms

Work: the route engine (provider routing plus the barrier-avoidance layer that names each avoided barrier with its reason and date); saved places; the "accessible X near me" quick action; the Expo app for Android and iOS; the Telegram notifications and the scheduled reminders (re-check prompts, weekly digest).

Exit checks:
1. A route between two points in a seeded test area avoids a known barrier and the result names the avoided barrier, its feature and its since-date.
2. With no barrier data, the route falls back to the plain provider route and says so honestly ("no accessibility data on this route yet").
3. The Android APK builds and installs on a device, and the same Google account sees the same saved places on the web app.
4. A re-check reminder fires at a round hour for a stale feature and reaches the contributor through the Telegram sender.

### M5: AI, the Windows app and the quality pass

Work: the place-name and category suggestion; the photo moderation assist; the route explanation; the support assistant; the Windows installer with the same sign-in and self-update; the macOS and Linux builds; the widget and live activity surfaces; the full self-audit.

Exit checks:
1. `npm run eval:support` passes with Arabic and English sets, and the support assistant refuses an ungrounded question.
2. The photo moderation assist flags an off-subject photo for a human reviewer and never deletes or publishes anything by itself (test proves no auto-action).
3. The Windows installer installs, starts, signs in with the same Google account, updates itself, and its entry is in `Projects-Hub.html` and on the Download page with the version and the size.
4. Screenshots exist at 320, 390, 768, 1280 and 1920 px in both languages and in light, dark and high contrast, with the five states visible.
5. The accessibility audit passes WCAG 2.2 AA with an accessible name on every control, no covered hit area, no horizontal scroll from 320 px, and the large-text and high-contrast toggle works.
6. Lighthouse mobile is 90 or better and the JSON is saved in `.sir/evidence/`.

### M6: Release, real places and the legacy handover

Work: the launch package (domain, accounts, legal review); the first real places onboarded with written consent from their owners or confirmed by real visitors; the first real claims verified; the old hosts redirected with 301; the keys rotated.

Exit checks:
1. Ten real places are live in one Egyptian city, each with a photo, a feature list and either two confirmations or a verified owner claim, and no seeded or invented place exists in any path a user can see.
2. Three real place owners have claimed and verified their entries with proof on file.
3. The 301 redirects from any old hosts are verified by curl.
4. The legacy keys are rotated and the service-account file is out of the repository.
5. The lawyer has reviewed the legal pages and the tax question is answered, and only then can a paid plan go live.

---

## 9. The task list for the free agents

The full ordered task list is `D:/Projects/_SIR/ops/briefs/sir-access-map-tasks.md` (48 tasks after the r61 refresh, each with an acceptance test and the skills that fit). The first ten stay ready to hand to agents at any time; tasks 11 and beyond queue behind them in order. The first ten:

1. Monorepo scaffold with tokens, RTL, the health route and CI.
2. The product's own Firebase project, the project folder and `owner-auth` with negative tests.
3. The data model and the Firestore rules, with emulator tests.
4. The map view with search, category filter and "near me".
5. The place profile with the feature checklist, dates and badges.
6. The submission flow with the feature checklist and note.
7. Photo upload with checks, signed URLs and the moderation queue.
8. The confirmation flow and the publish rules engine.
9. The place-owner claim flow with proof types.
10. The owner-only analytics page and the billing fallback page.

---

## 10. Skills from the library that this build uses

Picked from `D:/Projects/_SIR/ops/SKILLS_INDEX.md` and the digests in `D:/Projects/_SIR/ops/encyclopedia/`. Digests live under `ops/encyclopedia/<tool>/<skill>.md`.

**Design and UI**
- `anti-vibecoded-design-system` (claude) - keeps the map product away from generic AI styling and purple gradients.
- `taste-design-engine` (claude) - the self-audit against AI patterns before the screens ship.
- `emil-motion-impeccable` (claude) - the spring physics for the sheets, the tab bar and the route reveal.
- `modern-ui-ux-design-system` (claude) - tokens, micro-interactions and hierarchy for one design system.
- `cognitive-product-intuition` (claude) - the submission and claim flow step order and the empty states.
- `high-conversion-copywriting` (claude) - the promise line and the place copy that sell the end state without hype.
- `commercial-app-blueprint` (claude) - llms.txt, the trust signals and the sticky call to action on the site.
- `a11y-debugging` (codex) - the accessibility audit with Chrome DevTools against WCAG 2.2 AA.
- `mobile-ergonomics-polish` (claude) - touch targets, no horizontal scroll, tap feedback on the phone screens.
- `modern-web-guidance` (claude) - the current web APIs, container queries and dialog behaviour, run before any client-side work.
- `react-best-practices` (claude) and `nextjs` (claude) - App Router structure, Server Components, rendering and performance rules.

**Security and legal**
- `firestore_rules_creation` (claude) - the deny-by-default rules for every collection.
- `firebase_security_rules_auditor` (claude) - the audit that finds a cross-tenant read before a user does.
- `zero-trust-security-hardening` (claude) - server-side role checks, secure cookies and rate limiting.
- `owasp-vulnerability-shield` (claude) - the OWASP pass over uploads, claims, confirmations and auth.
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
- `chat-sdk` (codex) - the Telegram bot for re-check reminders and the weekly report.
- `webhook-testing` (deep) - capturing, replaying and validating the gateway webhooks.
- `verification` (codex) and `verification-before-completion` (deep) - the end-to-end check before the word done.

**Data, hosting, maps and growth**
- `firebase_firestore` (claude) - queries, indexes and the data model.
- `database-reliability-transactions` (claude) - the atomic submission, confirmation and claim flows and idempotency keys.
- `firebase_hosting_basics` (claude), `vercel-cli` (codex), `deployments-cicd` (codex) and `env-vars` (codex) - the two hosts with the same build and the same variables.
- `google_maps_platform` (codex) - evaluated in M0 for the base map, geocoding, routing and "near me"; OSM/OSRM is the fallback if the licence or cost fails.
- `open-seo-auditor` (claude) - Arabic search visibility, JSON-LD and the AI answer check.
- `system-design-architect` (claude) and `production-engineering-standards` (claude) - the zero-mock persistence and the production bar.

---

## 11. Risks and the defaults we take

- **Crowd cold start: nobody submits in a new city.** Default: launch in one city (Cairo) with a seeded contributor drive: the owner, family and volunteers submit and confirm 50 real places in the first month before any marketing. No marketing before the sourcing tasks in the competitor file are done.
- **Stale or wrong accessibility data harms a user.** Default: the publish rules in 5.3 (photo + second confirmation or owner claim), the verified-on date and re-check window on every feature, the "needs re-check" badge, and the report flow on every entry. A place with only unconfirmed reports is labelled as such, never as fact.
- **Abuse: fake places, fake photos, fake confirmations.** Default: rate limits on every mutation, one confirmation per user per claim, photo moderation assist plus human review, moderator queue before publish, ban flow for repeat abuse, and no public naming of submitters.
- **Owner-claim fraud: a business claims a place it does not own.** Default: proof required (document, callback to a listed business number, or domain), human review, and a verified badge that never overrides the evidence rules.
- **The map provider cost or licence fails.** Default: the M0 decision records the licence and cost tier; OSM/OSRM is the fallback; if both fail, the product ships list-and-profile first and the map second, never a broken map.
- **The audience cannot afford any subscription.** Default: the free tier covers every safety feature; paid tiers sell convenience (offline tiles, unlimited routes, alerts) and business visibility, never access to accessibility information. If real users say even that is too much, the plan drops to a donation/NGO model and the owner decides.
- **Privacy: a submitter's identity leaks.** Default: submitter UID is stored but never shown publicly; public records show "community verified" or "claimed by the place"; one-tap deletion removes the account and its submissions per the retention policy the lawyer confirms.

---

## 12. Plan refresh r61 (2026-11-12): what the rescan changed

Rescan per rule 20: re-read the project folder (`.sir/CHECKPOINT.md`, `PLAN_REFRESH.md`, `AGENTS.md`, README), this plan, the competitor file, the tasks file, the TickTick row and `PRODUCT_DIRECTION_2026-11-12.md`, then ran fresh web research. Findings and where they landed:

1. **Five more competitors found** (Braillito Maps, DisabledEnabled, Kimap, Ahoi, RailsMaps Egypt stations) plus an academic platform comparison (Zenodo SKI Canada 2026). Added to `ops/competitors/sir-access-map.md` addendum. Braillito validates the checklist-per-place model and the "number plus colour, never colour alone" accessibility rule, which this plan already had in spirit; DisabledEnabled validates the offline-first no-account posture and adds a fourth needs filter (cognitive) worth keeping in the filter design. Kimap's "patented navigation" claim is unverified and treated as marketing, not a model.
2. **Map provider decided with real numbers.** Official pricing pages checked 2026-11-12: Geoapify free (3,000 credits/day, commercial OK) recommended for v1, Mapbox free (50k GL JS loads/month) fallback, Google Maps Platform Essentials (10k loads + 100k tiles free monthly) viable but needs an owner billing account, MapTiler and Stadia free tiers rejected as non-commercial, public OSM tiles rejected for production. Written into 5.6.
3. **Egyptian legal baseline found and mapped to the checklist.** Law 10 of 2018 Articles 39 to 46 plus the Egyptian Building Code for persons with disabilities give measurable thresholds (1.2 m corridors, 5 percent ramp slope, 15 cm curb, designated parking). Every FeatureKey now must trace to a source in `docs/DATA_SOURCES.md`. Written into 5.3.
4. **Task list expanded from 10 to 48** with acceptance tests and skills per task in `ops/briefs/sir-access-map-tasks.md`.

### Open questions and the recommended answer for each

| Question | Recommended answer |
|---|---|
| Which map provider for v1? | Geoapify free tier first (commercial use allowed, routing included), Mapbox as fallback, Google Maps Platform only if the owner opens a billing account. Decide for real in M0 and record licence plus cost tier in `docs/DATA_SOURCES.md`. |
| How to seed the first city without fake data? | Owner, family and volunteers submit and confirm 50 real places in Cairo in month one; no seeded or invented places ever. NGOs and disability communities are outreach targets, not data sources we copy. |
| Should contributors get a public profile? | No in v1. Public records show "community verified" or "claimed by the place"; opt-in public profiles wait for a moderation and abuse review. |
| Indoor accessibility (malls, metro stations)? | Out of v1 as indoor mapping, but station and mosque entrance features are in scope. Metro station step-free status can be sourced from RATP-style official lists where they exist; otherwise crowd-sourced like everything else. |
| Paid place-owner badge: is it ethical here? | Keep it, with the published priority rule and the same evidence bar as everyone. If real owners say it feels pay-to-rank, drop to a flat "verified" badge with no ranking effect. |
| Egypt data protection law (Law 151 of 2020) for health-adjacent submissions? | Treat all submissions as personal data: no health details requested, submitter UID never public, one-tap export and deletion, lawyer review before paid launch. The legal pack task covers this. |
| What if Geoapify free quota is too small at launch? | The provider sits behind one adapter interface; switching to Mapbox or Google is a config change, not a rewrite. Quota alerts live in owner analytics. |
| Should route planning include public transport step-free info? | Not in v1 (no lawful structured feed). v2 candidate: ingest official metro/RER accessibility lists as citations, not scraped data. |

### Risks added by the r61 research

- **Provider dependency.** A free-tier map provider can change terms or quotas; mitigated by the adapter interface and the two-host rule.
- **Legal exposure if we cite the building code wrong.** Mitigated by quoting thresholds with source links and dates, and marking anything unverified.
- **Braillito-style screen-reader-first competition.** Mitigated by the plan's own WCAG 2.2 AA bar plus VoiceOver/TalkBack testing tasks added in M5.
