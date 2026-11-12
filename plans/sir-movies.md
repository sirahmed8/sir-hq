# PLAN: SIR Movies (small independent project, planning only)

Created 2026-11-12 (r51-backlog-projects). Idea 29 from the owner's "أفكار برامج ومشاريع" note. **Rewritten 2026-11-12 (r54) into the full premium plan.** Supersedes the r51 text; git history keeps it. Canonical competitor study: `D:/Projects/_SIR/ops/competitors/sir-movies.md` (opened sources dated 2026-11-12). First ten build tasks: `D:/Projects/_SIR/ops/briefs/sir-movies-tasks.md`.

**Truth rule for this plan.** Nothing here is called working unless a reviewer saw it today. This is a plan-only round: no folder, no repo, no code, no keys were created in this round. Verified today: the old plan file existed in git (`b3cc6a1` is the tip at time of writing); `D:\Projects\SIR Movies` does not exist; `sirahmed8/sir-movies` was not checked or created. Everything about competitors is "what their own pages showed on 2026-11-12", never an audited fact.

**Product class: GLOBAL.** Anyone in Egypt, the Arab world and globally can use it; accounts, subscriptions, dual hosting, owner-only analytics, all platforms planned.

**The decision behind this project.** The reason SIR Movies is its own product and not a module of another one, the lawful-content rules that apply to it and the exact folder, repository, Firebase and Desktop names are in `D:/Projects/_SIR/plans/BACKLOG_IDEAS_DECISIONS.md` (2026-11-12, round r53c).

---

## 1. Who it is for, and the promise

**For the Egyptian and Arab viewer.** The person who finishes a film and wants to know what to watch next, where it streams legally, what is on at the cinema this week, and to keep a list with friends, all in Arabic without wading through English-first sites.

**For Ahmed and his circle.** A private watchlist, ratings and shared lists that work over a weekend group chat, in RTL, on a phone, for free.

The one-sentence promise, in the words a user would use:

> Say what you watched and how you felt; SIR Movies tells you what is worth watching next, where to watch it legally right now, and what is playing at your cinema on Thursday.

**The end state we sell.** A user opens the app, sees a calm discovery surface (trending in Egypt, new on services, coming soon to cinemas), searches any title, reads the where-to-watch panel for their region, taps once to add it to their watchlist, rates and optionally reviews what they saw, gets "why you might like this" from their taste profile, shares a list with friends, and gets pinged when a watchlisted title arrives on a service they use. A backend event (affiliate click, showtime view) never breaks the user experience.

**Not in v1:** no piracy links ever, no scraping cinémas without written agreement, no invented ratings or showtimes, no ads inside the tracking flow, no selling watch history, and no AI text that presents itself as a human critic.

---

## 2. Names, IDs and current state

| Item | Value |
|---|---|
| Product folder | `D:\Projects\SIR Movies` (**not created this round**; created at M0) |
| Private GitHub repo | `sirahmed8/sir-movies` (**not created this round**; created at M0) |
| Stack default | `apps/web` Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens; `apps/mobile` Expo (M4/M5); shared `packages/core`, `packages/data`, `packages/ui`, `packages/kit`; Firebase Auth + Firestore; hosted on Firebase and Vercel |
| Metadata source | TMDB API (free tier; commercial terms re-read before monetisation) with IMDb IDs as external aliases only |
| Version | `1.0.0` everywhere, never bumped while under development |
| Domain candidates | `sirmovies.app` or an `.eg` name; owner checks availability and price "(unsourced, verify)". Until then Firebase and Vercel default URLs |
| Firebase project | `sir-movies`, created at M1, separate from every other SIR product. Not verified today |
| Payment | Paymob and Fawry in test mode first (EGP), Stripe later (USD); until keys exist: "Subscriptions launching soon" plus email capture |
| Wave | 9 (after current GLOBAL products); build starts only when HQ assigns it |
| Desktop kit | M0 recreates it per OWNER_DEFAULTS item 19 |

**Current state, honestly:** a plan exists (this file), a competitor study exists, ten tasks are queued. No code, no folder, no repo, no deployment, no keys. Egyptian cinema data sources are unbuilt and unlicensed. JustWatch developer program status is unknown (their developers site did not resolve on 2026-11-12). TMDB licensing for a monetised product is unverified. Every public claim must wait on those three checks.

---

## 3. Competitors and our edge

Full study: `D:/Projects/_SIR/ops/competitors/sir-movies.md` (10 competitors, opened 2026-11-12).

| Competitor | What it proves | Our edge |
|---|---|---|
| elCinema | Egypt's cinema conversation (showtimes, box office, booking links) is huge and editorial | Personal account-based tracking + where-to-watch + showtimes in a calm Arabic app |
| Watch iT | Legal Egyptian catalog with Arabic originals exists and can be linked | Cross-service aggregation including Watch iT, not one catalog |
| Shahid | Arabic streaming at scale (free + VIP), plus live channels | One watchlist and one answer across Shahid and every other legal service |
| JustWatch | Aggregation works, /eg exists in Arabic | Aggregation inside a tracking product with social lists and cinema |
| Letterboxd | Social tracking is loved; free tier with annual Pro/Patron works | Arabic-first, RTL, EGP pricing, showtimes, shared lists without the gatekeeping feel |
| IMDb | ID interoperability backbone | Calm premium UX; we key on TMDB IDs |
| Trakt | Scrobbling and API openness are sticky | Optional power-user scrobble in a consumer Arabic app |
| Reelgood | "Where to watch" is a product category | Egypt-first provider coverage, not US-centric |
| TMDB | Metadata is free and rich | We build the product on it legally with attribution |
| CimaClub | Pirate demand is real; product is illegal and ephemeral | The legal, safe, durable alternative for new releases and cinema |

---

## 4. Features

### 4.1 Parity with the best in the category, must ship

| Feature | Why | Source |
|---|---|---|
| Search across movies and series with Arabic and English titles, cast, crew, year, poster | Table stakes | elCinema, Letterboxd, TMDB |
| Title detail: synopsis, cast, ratings (TMDB + user), runtime, genres, trailers (YouTube embed) | Table stakes | All |
| Watchlist with watched / watching / want-to-watch states, per user | Core loop | Letterboxd, IMDb, Trakt |
| Episode-level progress for series (season/episode counter) | Series parity | Trakt, elCinema seasonals |
| Ratings (0.5 to 5 or 1 to 10) and optional text reviews with spoiler tag | Community | Letterboxd, elCinema |
| Where-to-watch panel per region (Egypt first): subscription, rent, buy, free, with deep links out | The JustWatch gap | JustWatch; TMDB watch providers for EG |
| Egyptian cinema showtimes by city and chain, now showing and coming soon | The elCinema gap, done as structured data | elCinema (only with written permission or licensed feed) |
| Shared lists with friends: create, invite link, public/unlisted/private, who-watched tracking | Social gap | Letterboxd lists; owner demand |
| Personalised recommendations by taste (genre/cast/decade weights from the user's ratings) | Retention | Letterboxd, JustWatch |
| Notifications: "now on a service you use", "new episode of a tracked series", "cinema premiere this week" | JustWatch watchlist alerts | JustWatch |
| Arabic RTL and English shipped together, five states everywhere | Premium floor | standard/23-premium-code-bar.md |
| Data export and one-tap account deletion (PDPL 151/2020) | Legal baseline | Privacy promise |
| Offline PWA reading of the watchlist and cached title cards | Native feel | OWNER_DEFAULTS item 14 |

### 4.2 The owner's own ideas, carried forward

| Idea | Source | Status |
|---|---|---|
| Movie discovery and tracking, Arabic support | TickTick ideas note, idea 29; `plans/sir-movies.md` r51 | This product |
| Where to watch (legal only), watchlist, ratings, recommendations, trailers, Egypt cinema showtimes, shared lists | r54 brief scope | This plan, sections 4 and 5 |
| Affiliate links to streaming and cinema booking | r51 plan money model | M3 (streaming sign-up) and M3/M5 (cinema booking, only under agreement) |
| No piracy links, ever | r51 plan lawful content rules | Section 7, hard rule |
| Movie list as concept backlog | `ops/TICKTICK_MAP.md`, ideas 23/26/28/29 | Decided: own project (PRODUCT_DIRECTION section 8) |

**Explicitly dropped or deferred:** no piracy linking, no scraping elCinema or cinema sites without written agreement, no fake ratings/reviews/user counts, no scraping user text from other sites, no medical or age-appropriateness claims beyond TMDB content ratings, no gambling/betting integrations, no copying competitor branding, posters stored raw (TMDB CDN with attribution only), and no AI fabricating "critic" reviews.

---

## 5. Platform matrix

Standing rule: every product ships on all platforms. v1 below; the rest with a written reason.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required (M1) | Marketing site, search, detail pages, auth, legal, pricing | Nothing pending |
| PWA (installable, offline) | Required (M1) | Install, offline watchlist cache, title cards cached via SW | Nothing pending |
| Android phone and tablet | Required (M4/M5) | Expo app: same account, discovery, watchlist, push for alerts | Play Store with owner's account |
| iPhone and iPad | Required (M4/M5) | Expo app, same account and data, tablet layouts | App Store or owner's preferred distribution |
| Windows | Required (M5) | Installable PWA day one; Electron/Tauri shell decision by ADR at M5 | Signed installer when owner has a certificate |
| macOS | Required (M5) | Installable PWA day one; same shell as Windows | Signed build when owner has Apple account |
| Linux | Required (M5) | Installable PWA day one; AppImage/deb from same shell | Signed package |
| Wear OS | Skipped in v1 | Nothing | "Now playing" reminder complication only if M6 decides |
| watchOS | Skipped in v1 | Nothing | Same ADR as Wear OS |
| TV (Android TV / Apple TV) | Decision at M6 | Nothing in v1 | Natural use case (couch + discovery); M6 ADR decides |
| Car (Android Auto / CarPlay) | Skipped | Nothing | No use case |
| Browser extension | Skipped | Nothing | No use case justifies the review burden |

**Rule:** all platforms share one Firebase project, one account and one dataset. Client storage local-first where it makes sense; watchlist syncs via Firestore with per-user security rules.

---

## 6. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. SIR Movies is GLOBAL, so it adopts accounts, owner analytics, AI fallback, legal pack, dual hosting and all-platform planning.

### 6.1 Shape

```
apps/web        Next.js 15+ App Router, React 19, TS strict, Tailwind v4 tokens
apps/mobile     Expo app for Android and iOS (M4/M5)
apps/desktop    Desktop shell ADR at M5 (installable PWA first)
packages/core   Domain types and zod schemas: Title, WatchlistEntry, Rating, Review,
                SharedList, ListMember, Cinema, CinemaShowtime, RecommendationProfile,
                StreamingProviderMapping, AffiliateClick, User, Subscription, Lead, AnalyticsEvent
packages/data   TMDB client (search, detail, watch providers, recommendations) with
                server-side cache (1h TTL metadata, 24h images), Firestore repositories,
                emulator tests
packages/ui     Shared kit: InputBox (search), TabBar, BottomSheet, Card (title poster),
                Chip (genre), Modal, Toast, Skeletons, Five-state wrappers
packages/kit    owner-auth, billing-fallback, signed-webhook, ai-proxy, legal-pack,
                i18n, help-center, notifications, analytics-aggregates
docs/           help source, legal source, data-model.md, ADR decisions, env names
scripts/        verify, TMDB cache warmer (dev only), Lighthouse, eval runner, desktop kit
```

Layers depend inward only. Files under 300 lines, no `any`, absolute imports, RTL-first logical CSS.

### 6.2 Accounts (`owner-auth`)

- Firebase project `sir-movies`, created at M1, never reused from another product.
- Google sign-in via Firebase Auth (web + mobile). ID token verified server-side with JWKS. Owner and admin rights from `OWNER_EMAILS`/`OWNER_UIDS`, fail closed. Web session in HttpOnly, Secure, SameSite=Strict cookie; mobile via Firebase SDK + Firestore rules. Rate limits on sign-in, sync, AI, webhooks; 2FA offer for owner.
- Tests: forged token 403; client-side flag flip grants nothing; non-owner on `/owner` 403.

### 6.3 Owner-only analytics page

Route `/owner`, server-verified owner token, everyone else 403. Real metrics read from aggregates, never raw per-user content: signups per day, WAU/MAU, new titles logged, top searched titles (aggregate), where-to-watch outbound clicks, affiliate clicks (per provider, aggregate), showtime views per cinema chain, free→Pro conversion, MRR in EGP and USD, churn, AI cost, error rate, notification delivery failures. Empty metric shows a dash and the reason, never a fake zero.

### 6.4 AI with the fallback chain

Chain: Gemini `flash-lite-latest` → `flash` → any Gemini → OpenRouter free → other free providers (Groq) → local Ollama (`AI_ENABLED` kill switch). Keys on this product's own accounts only, never printed, never committed.

AI roles and hard rules:

| Feature | AI role | Hard rule |
|---|---|---|
| "Why this film" | One-sentence taste explanation from the user's own ratings/genres | User's own data only; explanation shown as suggestion, not fact |
| Recommendation seed | Re-rank TMDB similar/recommended by taste profile | Deterministic scoring first; AI only phrases the why |
| Natural-language search later | Parse "a calm 90s Egyptian comedy" into filters | Parses to filters; if unsure, asks one clarifying question |
| Support assistant | Answer from `docs/help/*.md` only | Refuses ungrounded answers |
| Review summaries | Aggregate themes across reviews (opt-in display) | Never invents a consensus; shows "not enough reviews yet" under a threshold |
| Weekly owner report | Draft summary from DB aggregates | Numbers from DB; model only writes the sentence |

Free users get a small visible AI quota; owner unmetered; daily cost cap in `config/limits.json`; Arabic and English eval sets before any AI ships; runner exits non-zero below threshold; evals never train on private reviews.

### 6.5 Data model (Firestore, collections)

```
users/{uid}                      profile: displayName, locale, region (auto from IP/locale),
                                 tier (free|pro), createdAt, settings{notifications, aiWhy}
titles/{tmdbId}                  cached TMDB metadata snapshot: title, titleAr, year, posterPath
                                 (CDN path only, never raw bytes), genres, runtime, synopsis,
                                 synopsisAr, imdbId (alias), cachedAt, ttl
watchlistEntries/{entryId}       uid, tmdbId, kind (movie|tv), state (watched|watching|want),
                                 episodeProgress {season, episode}, addedAt, watchedAt, rating (0.5-5),
                                 reviewId | null, tags[]
ratings/{uid_tmdbId}             uid, tmdbId, kind, value, createdAt   (aggregate source for title scores)
reviews/{reviewId}               uid, tmdbId, kind, body (markdown), spoiler:bool, createdAt,
                                 helpfulCount, status (published|hidden)
sharedLists/{listId}             ownerUid, name, nameAr?, kind (watchlist|custom), visibility
                                 (public|unlisted|private), memberUids[], itemTmdbIds[], createdAt
listInvites/{token}              listId, createdBy, expiresAt, maxUses
cinemas/{cinemaId}              chain, city, branch, lat, lng, partnerStatus (permission|licensed|pending|none)
showtimes/{showtimeId}           cinemaId, tmdbId, kind, screen, startsAt, language, format,
                                 bookingUrl (only under agreement), source (manual|partner)
streamingProviders/{region_tmdbId_provider}  region (eg|sa|ae|...), tmdbId, providerId (TMDB watch providers),
                                 type (flatrate|rent|buy|free), url, verifiedAt
affiliateClicks/{clickId}        uid | null (anon allowed), provider, tmdbId, surface, ts  (aggregate only)
leads/{leadId}                   email, source: pricing, createdAt, consent:true     (PDPL: consent first)
subscriptions/{uid}              tier, status, gateway (paymob|fawry|stripe), renewsAt, cancelledAt
analyticsDaily/{yyyy-mm-dd}      signups, wau, titlesLogged, searches, whereClicks, affiliateClicks,
                                 showtimeViews, mrrEgpCents, mrrUsdCents, aiCalls, aiCostMicros, errors
events/{eventId}                 short-lived raw events, TTL 30 days, then aggregates only
```

Rules: deny by default; every user reads/writes only their own docs; sharedLists enforce membership and visibility server-side; titles collection world-readable (public TMDB data) but writable only by server; analyticsEvents write-only from clients, read never. Emulator tests prove cross-user read fails and list-membership enforcement.

### 6.6 Hosting, data sources and money

- Firebase project `sir-movies`: Auth, Firestore, Functions if needed, Hosting. Vercel second host, same repo via CLI, same build, same env vars on both. Both curl-checked, written in checkpoint.
- TMDB: server-side key; metadata cached 1h TTL, images referenced by CDN path with attribution link; no raw images in git or Firestore. Re-read commercial terms before M3 monetisation.
- Where-to-watch: TMDB watch-providers endpoint (region `eg`) + manual curation for Egypt-only services (Watch iT, Yango Play, TOD) until/unless a JustWatch-style partnership exists. Every outbound link verified monthly by a script, never by hand-editing copy.
- Egyptian cinema: written agreement with at least one chain (VOX / Cairo Festival City / Galaxy / Plaza / Americana) OR manual admin-curated schedule fed by the chain's own published listings under their permission; no scraping without agreement; booking deep links only under agreement. Until then, M3 ships "Coming soon to Egyptian cinemas" as curated editorial with source links, clearly dated.
- PDPL 151/2020: watch history is personal data; export and one-tap deletion on the profile page; analytics keep aggregates and TTL raw events; no selling data; privacy page matches code.
- Money: integer piasters/cents; Paymob + Fawry test mode first; signed webhooks, timestamped, idempotent; subscription state server-side only; "Subscriptions launching soon" + Lead capture until keys exist.

### 6.7 Security baseline

Firestore rules deny by default; zod at every boundary; no secrets in git; gitleaks in CI; CSP without unsafe-inline/eval; analytics after consent with Reject All as prominent as Accept; rate limits on auth, sync, AI, webhooks; affiliate links disclosed next to the button; no fake data anywhere a user can see.

### 6.8 The premium quality bar for this product

This is the floor from `D:/Projects/_SIR/standard/23-premium-code-bar.md`, written for this product. It is not a wish list: each line is checked by the self-audit before a milestone is called done.

**Motion, Apple level.** One shared spring config across the app (stiffness 300 to 400, damping 28 to 30), transform and opacity only, 120 Hz safe. Every sheet, drawer, modal and panel opens and closes with the same spring; an open-only animation is a defect. Micro-interactions 100 to 150 ms, standard 200 to 300 ms, large 300 to 500 ms, press scale 0.98, and a reduced-motion path for every animation. The poster grid uses a spring on insert and on remove, never a jump.

**Two languages, one layout.** Egyptian Arabic first for the catalogue and the Egyptian cinemas, English second, both shipped together and never one as a partial translation. RTL designed first with logical CSS properties only and flipped directional icons. Every text input detects Arabic or Latin per character as the user types and moves the caret and the direction live; every mixed run is isolated with `<bdi>` or `unicode-bidi: isolate`; the words "RTL" and "LTR" never reach the user. Currency and date and time are auto-detected from the visitor locale with a manual override on top, and formatted with `Intl`.

**Five states on every screen.** Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake film, a fake rating, a fake poster or a fake showtime; a title with no aggregate rating shows a dash, not a zero.

**Accessibility.** WCAG 2.2 AA. Every control has an accessible name, touch targets at least 44 px with no covered hit area, a full keyboard path on every screen, visible focus, zoom from 80 to 200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured, and a colour pair that passes contrast in light, dark, system and high-contrast themes. Trailers never autoplay with sound, and every one of them has a caption or a text alternative.

**The look.** One design system: tokens for colour, spacing on a 4 and 8 px grid, radii, shadows, type and motion. A calm dark canvas with one accent for the primary action, no purple-blue gradients, no emoji headings, no pill buttons on data inputs, no hype words, and no em dashes in the copy. One component per control, never two. Arabic screen face: IBM Plex Sans Arabic, Cairo or Tajawal.

**Native app feel.** The browser's text selection and the right-click menu are disabled site-wide and replaced by the app's own menu with in-app actions and a refresh, while normal select, copy and paste keep working inside real input fields.

**Evidence before the word done.** Screenshots at 320, 390, 768, 1280 and 1920 px in Arabic and English in light and dark, plus 3840 px once. Playwright on the critical journeys (search, detail, add to watchlist, offline sync). Lighthouse mobile 85 or better on the detail route. A click-target audit in CI. The self-audit loop runs until two clean cycles in a row.

---

## 7. Lawful content rules (hard)

1. Only licensed streaming services are listed (Netflix, Disney+, Prime Video, Apple TV+, Shahid, Watch iT, STARZPLAY, TOD, Zee5, Yango Play, and regional equivalents). No CimaClub-style pirate linking. Ever.
2. TMDB images served from TMDB CDN with attribution; never stored raw; never re-hosted.
3. Cinema showtimes appear only with the chain's written permission or a licensed data feed; booking deep links only under agreement; otherwise "source: chain official page, checked <date>" with a dated link.
4. Affiliate links are labelled "sponsored"/"إعلان" in context; eligibility and payout terms published in legal pages.
5. No user-generated review scraping; reviews are written in-app by signed-in users and are moderatable (report / hide) with an audit trail.
6. AI never writes "critic" copy; AI "why this film" labels itself and cites the taste dimensions it used.
7. Egyptian copyright law and platform ToS govern; when in doubt, the content does not ship.

---

## 8. Free tier and fair pricing (proposals, validate before publishing)

Every public price page carries a source link and date, or "(unsourced, verify)". Owner account gets every Pro permission inside the product, free forever.

| Tier | Price proposal | Includes |
|---|---|---|
| Free | 0 EGP | Discovery, search, title detail, trailers, watchlist up to 100 titles, ratings, reviews, episode progress, 1 shared list up to 3 members, Egyptian cinema showtimes (curated), legal where-to-watch panel, offline PWA reading, Arabic + English, export and delete |
| Pro monthly | 59 EGP/month "(unsourced, verify)" | Unlimited watchlist and lists, unlimited list members, AI "why this film" (fair-use daily cap), availability alerts for watchlist titles, episode air-date reminders, advanced stats (year in review, taste DNA), priority support, ad-free |
| Pro yearly | 499 EGP/year "(unsourced, verify)" (~2 months free) | Same as monthly, billed yearly, launch price for early users |
| USD fallback | $1.99/month or $19.99/year "(unsourced, verify)" | Same Pro features, auto-detected from locale/IP with manual override, never manual-only |
| Owner | Free forever | Every Pro permission; `/owner` analytics |

**Fairness:** no ads in the tracking flow; no selling watch history; cancel as easy as sign-up; refunds per published policy; until keys exist, "Subscriptions launching soon" plus email capture writing a Lead.

**Revenue (secondary):** affiliate commission from streaming sign-ups and cinema ticket bookings, disclosed. Affiliate never gates a free feature; it only earns when a user chooses to subscribe/book through us.

---

## 9. Milestones M0 to M6 with acceptance tests

| Milestone | Goal | Acceptance test |
|---|---|---|
| M0 | Project kit is real and honest; this round does **not** do it | `D:\Projects\SIR Movies` exists with `.sir/` (CHECKPOINT, PLAN_REFRESH.md logging this r54 rewrite), `AGENTS.md`, `.gitignore`, `legacy/` untouched-if-any, version 1.0.0 in package.json; `sirahmed8/sir-movies` created private and `main` tracks `origin/main`; Desktop folder `SIR Projects\SIR Movies` with `folder.ico` (project root), Versions.txt (1.0.0, plain status), `Open project folder` shortcut; TickTick parent task created; checkpoint lists exactly what exists. Do **not** claim anything works at M0 |
| M1 | Foundation: monorepo, Firebase, auth, TMDB search/detail | `apps/web` builds; `pnpm run verify` (typecheck, lint, tests, build, gitleaks) green; Firebase project `sir-movies` exists and is recorded; forged token → 403 (3 negative tests); `/api/health` returns real status; search "dune" returns real TMDB results; detail page renders poster/synopsis/cast with attribution; screenshots 320/390/768/1280 px Arabic+English light/dark; CI seen green or quota flag recorded with local output |
| M2 | Tracking core: watchlist, ratings, reviews, where-to-watch | User adds a title to watchlist offline-first, goes online, syncs; rating persists; review posts with spoiler flag; where-to-watch panel shows EG options with prices from TMDB watch providers + manual Egypt curation, every link checked by script; five states on all panels; export and one-tap delete work |
| M3 | Egypt push: cinema showtimes, AI "why this film", billing fallback | At least one cinema chain surfaces showtimes under written permission OR curated "source: chain page, checked <date>" clearly marked; "why this film" passes Arabic and English eval set; pricing page shows launch mode until keys exist; `/owner` 403 for non-owner with real metrics or dashes-with-reasons; legal pages live at `/legal/*`; dual hosting curl-checked on Firebase and Vercel |
| M4 | Mobile apps | Expo Android and iOS builds run on emulator/simulator; same account and data; push notification for watchlist availability and episode reminders with quiet hours; App Store / Play assets drafted truthfully, unsubmitted |
| M5 | Desktop shells, shared lists polish, billing live | Windows/macOS/Linux installable PWA verified; desktop shell ADR (Electron vs Tauri vs stay-PWA) recorded and built if chosen; Paymob live in EGP (owner buys keys) with signed webhook tests; shared lists invite links work end-to-end with per-list membership enforcement covered by emulator tests |
| M6 | TV decision, store readiness, visibility, launch | Android TV / Apple TV ADR decided; store listings drafted with truthful screenshots (no fake users); `llms.txt`, JSON-LD, Arabic visibility pages for "أين أشاهد" queries verified; notification delivery failure rate under agreed threshold for 30 days; accessibility pass (WCAG 2.2 AA); legacy untouched; launch checklist complete |

**Exit rule for every milestone:** verify passes, CI seen green or quota flag recorded with local output, checkpoint updated, report in `ops/agy-runs/reports/`, nothing called working unless seen that day.

### 9.1 The first ten build tasks

The ten tasks are ready to queue, each with a title and a one-paragraph brief: `D:/Projects/_SIR/ops/briefs/sir-movies-tasks.md` (round r54). The order is the dependency order: the scaffold, the Firebase project and auth, the data model and rules, the TMDB source, the where-to-watch source, the first screens, the showtimes, the tracking core, the owner page and billing, and the quality pass. Tasks 1 to 4 can run side by side; everything from 5 on needs the scaffold and the rules to be green first.

---

## 10. Skills used for this plan

Selected from `ops/SKILLS_INDEX.md`; no new skill installed.

- `sir-ecosystem-orchestrator` for product boundaries and portfolio placement.
- `sir-skill-library` for finding specialists before writing architecture and tasks.
- `agent-supercharged-os` for the plan-test-implement-review loop.
- `firebase_auth_basics`, `firebase_firestore`, `firestore_rules_creation`, `firebase_security_rules_auditor`, `firebase_hosting_basics`, `firebase_app_hosting_basics` for accounts, rules, hosting, owner analytics.
- `modern-app-engineering`, `modern-ui-ux-design-system`, `emil-motion-impeccable`, `anti-vibecoded-design-system`, `a11y-debugging`, `mobile-ergonomics-polish`, `shadcn` for the premium bar.
- `database-reliability-transactions` for sync, idempotency, webhooks.
- `high-conversion-copywriting` and `open-seo-auditor` for pricing page and Arabic visibility later.
- `agent-reach` for read-only market research (used this round for competitors).
- `verification` for "nothing is working unless seen today".
- `video-digest` / `youtube-video-research` later for trailer-embedding UX research, never for piracy sources.

---

## 11. Risks and open questions

- **TMDB commercial terms:** free tier covers non-commercial and development; before M3 monetisation the owner or an agent must read TMDB's commercial/API terms and either switch to a licensed feed or confirm eligibility. Default: do not monetise until terms read; until then, launch gate is blocked, not faked.
- **Egyptian cinema data:** no public licence found as of 2026-11-12. Default: manual curation from chain-published pages, dated and sourced, only for chains that grant written permission or whose pages allow it; otherwise only "coming soon" editorial with links. Never scrape behind a prohibition.
- **JustWatch partnership:** developer program status unknown; rely on TMDB watch providers + manual Egypt curation. If a partner feed appears, swap the source behind the same `StreamingProviderMapping` interface.
- **Watch iT / WeTV / Yango Play terms:** link-out only (we never embed); terms re-read before listing logos or prices.
- **AI hallucinated "why":** eval gate; if Arabic quality is below threshold, the feature ships hidden, not shipped weak.
- **Affiliate disclosure:** plain-language "إعلان قد نربح منه" near every affiliate link; owner legal review before launch.
- **Competitor drift:** this study is dated; re-run before any public comparison page.
- **Store accounts and certificates:** owner actions; nothing assumes they exist.

---

## 12. Only the owner can do

Buy `sirmovies.app` or choose an `.eg` name after checking rules and price; create the Firebase project `sir-movies` (or approve an agent to); open Vercel, Paymob, Fawry, and later Stripe accounts; TMDB commercial eligibility decision; cinema chain agreements (VOX, Cairo Festival City, Galaxy, Plaza, Americana); Apple Developer and Google Play accounts when ready; code-signing certificates; legal review of privacy, terms, refunds and PDPL pages; recruit beta testers.

---

## 13. Market-grade and visibility checklist

- Landing page says the end state in five seconds: what to watch next, legally, in Arabic, with tonight's cinema.
- `llms.txt`, facts page, help centre, legal pages, pricing, comparison pages only after competitor sources are current.
- Arabic queries to target: "أين أشاهد", "مواعيد عرض السينما اليوم", "قائمة مسلسلات", "ترشيح أفلام", "فيلم عربي". Claims verified before publishing.
- YouTube demos of real use only after M2; no fake screens or invented users.
- Weekly AI-answer check for "best movie tracking app Arabic", "where to watch in Egypt", "سينمات القاهرة" after launch.

---

## 14. Definition of done for this plan

Complete when `plans/sir-movies.md`, `ops/competitors/sir-movies.md` and `ops/briefs/sir-movies-tasks.md` exist, the bus line is sent, the explicit paths are committed and pushed to `main`, and the report states what was verified today versus what remains unverified. The project folder and repo are M0 work and are deliberately not part of this round.
