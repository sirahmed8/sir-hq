# PLAN: SIR Handyman (concept backlog → own product, planning only)
Created 2026-11-12 (r51-backlog-projects). Idea 28 from the owner's "أفكار برامج ومشاريع" note.

## Decision
**Own product.** Home services booking (plumbers, electricians, carpenters, painters, AC technicians) in Egypt is a proven commercial market (Taskday, Khidmeh, Handyman.com.eg exist). The business model — service-fee percentage, featured craftsman, subscription for verified pros — is similar to Hagoozat but the domain, entities, and flow are entirely different. Merging into Hagoozat would bloat its scope. **Status: planning only.** Build work starts when Ahmed decides the wave order.

## 1. Purpose (plain words)
Book a trusted handyman in Egypt in a few taps: describe the job, pick a time, see a fixed price or an on-site quote, pay through the app. Craftsmen get more jobs; homeowners get verified, rated workers. Arabic first, Egyptian dialect copy.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Handyman` |
| GitHub | `sirahmed8/sir-handyman` (private, create when build starts) |
| Wave | 9 (after current GLOBAL products) |
| Stack (default) | Next.js 15+ App Router, Cloudflare Workers, Firestore with transactions (job slot locking), R2 for job photos |
| Domain (candidate) | `sirhandyman.app` — owner checks and buys |
| Platforms | Web (PWA) first; Android and iOS via Expo M6+ |
| Money | Free for homeowners; craftsman pays a percentage of each booked job or a flat monthly subscription (EGP, Paymob/Fawry, auto-detected locale) |

## 3. Competitor matrix
| Competitor | Strengths | Weaknesses | Opportunity |
|---|---|---|---|
| Taskday (Egypt) | Egyptian market, app store presence | Limited coverage, UX dated | Modern UX, real ratings, transparent pricing |
| Khidmeh (Egypt) | B2C model | Poor mobile | Mobile-first, instant booking |
| Handyman.com.eg | Established brand | Web only, no live booking | Native app feel, in-app payment |
| Homzmart | Furniture + services | Product-first, services secondary | Services-first, broader trades coverage |
| UrbanClap/Urban Company | Excellent UX, proven model | India/UAE focus | Egyptian market equivalent |

## 4. Platform matrix
| Platform | Plan | Note |
|---|---|---|
| Web (PWA) | M1 | First |
| Android | M6+ | Expo |
| iOS | M6+ | Expo |
| Windows | Via PWA | Installable |
| macOS | Via PWA | Installable |
| Linux | Via PWA | Installable |
| Wear OS | Skipped v1 | Job arrival notification later |
| watchOS | Skipped v1 | Same |
| TV / Car | Skipped | No use case |

## 5. Free-tier plan
- Firebase Spark plan (auth, Firestore).
- Cloudflare Workers free (100k req/day); R2 for job photos (10 GB free tier).
- Vercel Hobby for second host.
- Revenue: 10–15% job fee from craftsman, or flat monthly Pro plan — no paid infra needed until volume justifies it.
- Paymob test mode until business account approved.

## 6. Lawful data and compliance
1. Craftsman onboarding: ID check required (National ID scan and liveness check by third-party KYC provider — owner to research providers; never stored raw by the app beyond KYC pass/fail flag).
2. Job photos stored in R2 with signed URLs; deleted 90 days after job completion.
3. PDPL 151/2020: homeowner address shared with craftsman only after confirmed booking; deleted from active store after 1 year.
4. Insurance and liability: a legal disclaimer on every quote that neither SIR Handyman nor the owner are liable for damage (lawyer review before paid launch).
5. No fake craftsmen, fake ratings, or shill reviews. Each rating requires a completed booking reference.

## 7. Security and conduct
1. Booking is a Firestore transaction with idempotency key and 10-minute slot lock.
2. Craftsman wallet (pending, released, withdrawn) uses server-side balance with no client-side override.
3. Webhooks (payment gateway) are HMAC-SHA256 signed with timestamp check (5-minute replay window).
4. Owner dashboard: server-verified token, all metrics (bookings, revenue, craftsmen pipeline, payout queue).
5. Rate limit: 20 booking attempts per user per hour.

## 8. Three-milestone roadmap
| Milestone | Goal | Owner-visible exit check |
|---|---|---|
| M0 (planning) | This plan complete, competitor matrix verified, KYC provider researched, domain candidate registered. | Plan in `_SIR/plans/sir-handyman.md`; owner registers domain. |
| M1 (core) | Service categories, craftsman profiles, booking wizard (time, address, job description, photo), Firestore concurrent booking test. | Open URL → browse category → book a slot → 10 parallel requests yield 1 slot (test). |
| M2 (payments, verification, legal) | Craftsman wallet, Paymob payout flow, KYC pass/fail flag, legal pages, owner-only analytics. | Craftsman receives payout in test mode; legal pages at `/legal/*`; dual hosting verified. |
| M3+ (quality, AI, mobile) | AI job description assistant (describe in plain words → suggest category and price range); store builds; Lighthouse 90+ mobile. | AI suggestion eval passes; Android build on emulator; screenshot 390/1280 LTR/RTL. |

## 9. Next step (planning phase)
Ahmed decides wave order. Owner researches Egyptian KYC providers. No code written until wave approved.
