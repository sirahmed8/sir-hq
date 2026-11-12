# PLAN: SIR Deals (concept backlog, planning only)
Created 2026-11-12 (r51-backlog-projects). Ideas 15 and 16 from the owner's "أفكار برامج ومشاريع" note.

## Decision
**Own product** (not a module). Price comparison and game-deal finding are two facets of the same user need: find the cheapest price for something in Egypt before buying. The same user who wants the lowest price on a PC game also wants the lowest price on a phone or pair of sneakers. One product covers both. The brief suggested Hagoozat as a home; Hagoozat is about booking pitches, not shopping; the audiences overlap loosely but the daily use case is entirely different. Keeping it separate avoids scope creep in Hagoozat.

**Status: concept backlog, planning only.** The critical gate is lawful data: price data from Egyptian retailers must come from an official API, an affiliate feed, or a data-sharing agreement. Web scraping without written permission from each retailer violates Egypt's Computer Crimes Law 175/2018. No build work starts until at least one lawful source is confirmed.

## 1. Purpose (plain words)
Show Egyptians the cheapest price for any product (electronics, games, clothes, books) across Egyptian online shops at the moment they want to buy. Alert the user when a watched item drops in price. Surface new game deals and limited-time offers.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder (when created) | `D:\Projects\SIR Deals` |
| GitHub (when created) | `sirahmed8/sir-deals` (private) |
| Wave | 9 (after current GLOBAL products) |
| Stack (default, when built) | Next.js 15+ App Router, Cloudflare Workers, Firestore, R2 for cached price snapshots |
| Domain (candidate) | `sirdeals.app` — owner checks and buys |
| Platforms | Web (PWA) first; Android and iOS via Expo M6+ |
| Money | Free for users; affiliate commission (Jumia, Amazon.eg affiliate programs when available); Pro: price alerts without ads (EGP, auto-detected locale) |

## 3. Gate: lawful data sources
No build starts without at least one of these confirmed in writing:
1. Jumia Egypt affiliate API (product search + price) — apply at affiliate.jumia.com.eg.
2. Amazon.eg affiliate / Product Advertising API — apply at affiliate-program.amazon.com (Egypt not listed yet as of 2026-11-12; check quarterly).
3. Noon affiliate feed.
4. A signed data-sharing agreement with an Egyptian retailer.
5. A price-aggregator data provider whose terms permit resale of prices (e.g. Pricespy, Prisjakt — not Egypt yet; check quarterly).

Owner action required: apply to the affiliate programs above and report back. Agent blocks: none until a source is approved.

## 4. Competitor matrix
| Competitor | Strengths | Weaknesses | Opportunity |
|---|---|---|---|
| Yaoota.com | Strong Egyptian price aggregation, established | Poor mobile UX, slow, no price alerts | Mobile-first, real-time alerts, Arabic-first |
| Pricespy (global) | Great UX, price history charts | Not Egypt | Localised equivalent |
| Comparison.com.eg | Some categories | Narrow catalogue | Wider catalogue |
| Jumia / Noon direct | Real prices, trusted | No cross-shop comparison | Cross-shop single view |

## 5. Platform matrix
| Platform | Plan | Note |
|---|---|---|
| Web (PWA) | M1 | First |
| Android | M6+ | Expo |
| iOS | M6+ | Expo |
| Windows | Via PWA | Installable |
| macOS | Via PWA | Installable |
| Linux | Via PWA | Installable |
| Wear OS | Skipped v1 | Price alert notification later |
| watchOS | Skipped v1 | Same |
| TV / Car | Skipped | No use case |

## 6. Free-tier plan
- Firebase Spark plan for auth and Firestore (up to 1 GB storage, 50k reads/day free).
- Cloudflare Workers free (100k requests/day).
- Price data from free affiliate API tier first; cache snapshots in R2 (10 GB free on Cloudflare R2).
- Vercel Hobby for the second host.
- Affiliate revenue covers costs before paid tier is introduced.

## 7. Security and conduct
1. No scraping without written permission.
2. Prices are shown with a timestamp; they may be stale. Clear disclaimer: "Price shown at time of check; click through to confirm."
3. User price alerts stored server-side, rate-limited (max 50 per user free, 500 Pro).
4. Affiliate links are disclosed to users (Egypt Consumer Protection Law).
5. No fake prices, reviews or availability.

## 8. Three-milestone roadmap (placeholder, subject to data-gate passing)
| Milestone | Goal |
|---|---|
| M0 (planning) | At least one lawful data source approved; this plan complete; competitor matrix verified; affiliate application submitted. Owner action: apply to affiliates. |
| M1 (core) | Scaffold, affiliate feed integration, search, price history chart, one category live. |
| M2 (alerts) | Price alert engine, notifications, Pro billing. |
| M3+ (quality, mobile) | Coverage growth, store builds, legal pages. |

## 9. Next step (planning phase)
Owner submits affiliate applications (Jumia, Noon). Agent monitors quarterly for Amazon.eg availability. No code written until gate passes.
