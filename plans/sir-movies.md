# PLAN: SIR Movies (concept backlog → own product, planning only)
Created 2026-11-12 (r51-backlog-projects). Idea 29 from the owner's "أفكار برامج ومشاريع" note.

## Decision
**Own product.** Movie discovery, tracking and recommendations are well-defined and distinct from any existing SIR product. SIR Life is about personal routines and health; entertainment tracking belongs in a dedicated product. The commercial model (affiliate links to streaming services, event-cinema ticket affiliate, Pro watchlist features) is proven. **Status: planning only.** Build work starts when Ahmed decides the wave order.

## 1. Purpose (plain words)
Discover new films, track what you have watched, get personalised recommendations, and find where to watch them (streaming or cinema in Egypt). Arabic-first with Egyptian cinema listings.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Movies` |
| GitHub | `sirahmed8/sir-movies` (private, create when build starts) |
| Wave | 9 (after current GLOBAL products) |
| Stack (default) | Next.js 15+ App Router, Cloudflare Workers, Firestore, TMDB API (free, public licence for non-commercial use; switch to licensed feed for commercial) |
| Domain (candidate) | `sirmovies.app` — owner checks and buys |
| Platforms | Web (PWA) first; Android and iOS via Expo M6+ |
| Money | Free tier (discover, track up to 100 films); Pro: unlimited watchlist, offline cards, streaming link aggregation (EGP + USD auto-detected); affiliate commission from streaming service sign-up links |

## 3. Data sources
1. **TMDB (The Movie Database)**: free API for non-commercial and commercial use (read attribution terms). Covers movie metadata, trailers, cast, ratings. Apply for a commercial API key when the product monetises.
2. **Egyptian cinema listings**: no public API found as of 2026-11-12. Options: cinema chains (VOX, Cairo Festival City, Americana) have websites; a scraping agreement or manual curation is required. Owner action: contact cinema chains for a data-sharing or affiliate deal.
3. **Streaming availability**: JustWatch affiliate API (apply at developers.justwatch.com) or manual mapping for Egypt's streaming services (Shahid, Netflix, Disney+, WeTV).

## 4. Competitor matrix
| Competitor | Strengths | Weaknesses | Opportunity |
|---|---|---|---|
| IMDb | Massive database, global | No Egypt cinema focus, poor Arabic UX, no streaming aggregation | Egyptian-first, Arabic UX, local cinema listings |
| Letterboxd | Excellent community and UX | English-only, no Egypt, no streaming links | Arabic community, Egypt cinema, streaming links in one place |
| JustWatch | Streaming aggregation | Not a tracking or discovery app | Combine discovery + tracking + where-to-watch |
| Cimaclub | Egyptian content focus | Grey area legality (links to pirated content) | Legal streaming links only, legitimacy advantage |
| Shahid | Arabic streaming | Streaming service, not a discovery/tracking app | Cross-service aggregation on top |

## 5. Platform matrix
| Platform | Plan | Note |
|---|---|---|
| Web (PWA) | M1 | First |
| Android | M6+ | Expo |
| iOS | M6+ | Expo |
| Windows | Via PWA | Installable |
| macOS | Via PWA | Installable |
| Linux | Via PWA | Installable |
| Wear OS | Skipped v1 | Now Playing notification later |
| watchOS | Skipped v1 | Same |
| TV | M6+ consideration | Movie app on TV is natural use case |
| Car | Skipped | No use case |

## 6. Free-tier plan
- Firebase Spark plan (auth, Firestore, up to 1 GB).
- TMDB API: free.
- Cloudflare Workers free tier; R2 for cached posters (10 GB free).
- Vercel Hobby for second host.
- Revenue: affiliate links (streaming sign-ups, cinema tickets if partnership formed); Pro plan.

## 7. Lawful content rules
1. Only legal streaming services listed (no links to pirated content; no Cimaclub-style linking).
2. TMDB images served through TMDB CDN with proper attribution; not stored raw.
3. Egyptian cinema listings: only shown with the cinema chain's permission or from a licensed feed; no scraping without written agreement.
4. Affiliate links clearly disclosed to users.
5. No user-generated review text scraping from other sites.

## 8. Security and conduct
1. Watchlist is per authenticated user; no public leakage of private watchlists without explicit sharing opt-in.
2. Rate limit on TMDB calls: cache aggressively (1 hour TTL for metadata, 24 hours for images); stay inside free tier.
3. Owner dashboard: server-verified token; shows active users, searches, watchlist sizes, affiliate clicks.
4. PDPL 151/2020: watching-history data is personal; export and deletion flow on the profile page.

## 9. Three-milestone roadmap
| Milestone | Goal | Owner-visible exit check |
|---|---|---|
| M0 (planning) | This plan complete, TMDB API key registered, JustWatch application submitted, cinema data approach decided, domain registered. | Plan in `_SIR/plans/sir-movies.md`; TMDB key in .env.local. |
| M1 (core) | Movie search, detail page (cast, trailer, ratings), watchlist (add/remove, watched/want), where-to-watch (TMDB provider list). | Open URL → search a film → add to watchlist → see streaming links. Screenshot 390/1280 LTR/RTL. |
| M2 (Egypt, recommendations, billing) | Egyptian cinema listings (at least one chain), personalised recommendations, Pro billing (Paymob), owner-only analytics. | Egyptian cinema showings visible; recommendations shown; pricing page; legal pages at `/legal/*`; dual hosting verified. |
| M3+ (quality, AI, mobile) | AI recommendation explanation ("why this film"), store builds, Lighthouse 90+ mobile. | AI eval passes; Android build on emulator. |

## 10. Next step (planning phase)
Ahmed applies for TMDB commercial API key and contacts cinema chains. Agent monitors JustWatch developer program availability for Egypt. No code written until wave approved.
