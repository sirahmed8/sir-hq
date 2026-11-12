# PLAN: SIR Cars (concept backlog → own product, planning only)
Created 2026-11-12 (r51-backlog-projects). Idea 23 from the owner's "أفكار برامج ومشاريع" note.

## Decision
**Own product.** Car buying, selling and tracking in Egypt is a large, clearly distinct market (Hatla2ee, CarSwitch, OLX Egypt Cars are established players). No existing SIR product serves this. The commercial model (listing fees, featured ads, inspection service referrals) is proven. This deserves its own folder, Firebase project and repo. **Status: planning only.** Build work starts when Ahmed decides the wave order.

## 1. Purpose (plain words)
Let Egyptians buy, sell and compare cars in a trustworthy marketplace: verified listings, price history, inspection booking, and an owner tracker for maintenance reminders. Arabic first, Egyptian dialect copy.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Cars` |
| GitHub | `sirahmed8/sir-cars` (private, create when build starts) |
| Wave | 9 (after current GLOBAL products) |
| Stack (default) | Next.js 15+ App Router, Cloudflare Workers, Firestore, R2 for car photos |
| Domain (candidate) | `sircars.app` or `sir-cars.com` — owner checks and buys |
| Platforms | Web (PWA) first; Android and iOS via Expo M6+ |
| Money | Free for private sellers (up to 3 listings); Pro seller: unlimited listings + featured + WhatsApp lead badge (EGP, auto-detected locale); inspection referral partnership |

## 3. Competitor matrix
| Competitor | Strengths | Weaknesses | Opportunity |
|---|---|---|---|
| Hatla2ee.com | Largest Egyptian car marketplace, SEO, big brand | Outdated UX, slow mobile, no inspection integration | Modern mobile-first UX, integrated inspection flow |
| OLX Egypt (cars) | High traffic | Generic (not car-specific), low trust, scam listings | Verified listings, inspection badge, ownership history |
| CarSwitch | GCC focus, inspection model | Not Egypt yet | Egyptian market, local payment (Paymob/Fawry) |
| Contactcars.com | Research-focused | No marketplace | Combine research + marketplace |
| Syarah (Saudi) | Great UX | Saudi only | Egyptian equivalent |

## 4. Platform matrix
| Platform | Plan | Note |
|---|---|---|
| Web (PWA) | M1 | First |
| Android | M6+ | Expo |
| iOS | M6+ | Expo |
| Windows | Via PWA | Installable |
| macOS | Via PWA | Installable |
| Linux | Via PWA | Installable |
| Wear OS | Skipped v1 | Maintenance reminder later |
| watchOS | Skipped v1 | Same |
| TV / Car | Skipped | No use case |

## 5. Free-tier plan
- Firebase Spark plan (auth, Firestore, up to 1 GB storage).
- Cloudflare Workers free tier for API, R2 for car photos (10 GB free tier covers hundreds of listings at launch).
- Vercel Hobby for second host.
- Revenue: featured listing fee from Pro sellers; inspection referral commission.
- No paid infra needed until real listings require scale.

## 6. Lawful data
No scraping existing marketplaces. All listings are user-submitted. For price benchmarks: use public government data (Motor Vehicles Authority Egypt, customs duty tables — public domain) and published press releases. Price history is built from submitted listings only. Inspection service integration requires a signed referral agreement.

## 7. Security and conduct
1. Listings require phone number verification (OTP via Vonage/Twilio free tier).
2. Photos are size- and type-checked before upload; R2 signed URLs; auto-deleted 90 days after listing expiry.
3. No fake listings, bots, or shill bids. Rate limit: 3 free listings per verified phone per 30 days.
4. PDPL 151/2020: seller phone visible to buyer only after a declared-interest tap with explicit consent disclosure.
5. Owner dashboard: server-verified token, shows all metrics (listings, leads, revenue, verification queue).
6. Report-a-listing flow in every listing card.

## 8. Three-milestone roadmap
| Milestone | Goal | Owner-visible exit check |
|---|---|---|
| M0 (planning) | This plan complete, competitor matrix verified, inspection partner scoped, domain registered. | Owner registers domain; plan in `_SIR/plans/sir-cars.md`. |
| M1 (core) | List, search and filter cars; seller upload with photo; buyer contact flow with consent disclosure; Firestore emulator tests (concurrent listing updates). | Open URL → see listings → contact seller → consent screen shown. |
| M2 (Pro, verification, legal) | Pro seller billing (Paymob), phone OTP, inspection referral flow, legal pages (PDPL, terms), owner-only analytics. | Pro listing live; legal pages at `/legal/*`; dual hosting verified. |
| M3+ (quality, mobile) | Store builds, SEO (city-level landing pages for real listings), maintenance tracker for owners, price benchmark widget. | Lighthouse 90+ mobile; Android build on emulator. |

## 9. Next step (planning phase)
Ahmed decides the wave order. Agent monitors for Egyptian auto-data APIs (Motor Vehicles Authority public portal). No code written until wave approved.
