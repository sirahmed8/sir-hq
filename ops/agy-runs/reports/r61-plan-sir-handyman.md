R61 Planning-Only Report: SIR Handyman

## Overview
Planning-only round for SIR Handyman (slug: sir-handyman). Free CLI agents must NOT start building. All work is limited to D:/Projects/_SIR (plans/, ops/competitors/, ops/briefs/, ops/research/). No code, no repo creation, no Firebase project creation.

## What Was Done

### 1. Expanded tasks from 10 to 42 granular tasks (ops/briefs/sir-handyman-tasks.md)
- Tasks split across milestones M0-M6 with granular descriptions and exit checks
- First 10 tasks remain ready for agent queue (as originally specified)
- Tasks 11-42 cover: quote comparison and acceptance, en-route tracking and visit code, escrow and Paymob/Fawry webhooks, ratings and share-visit, owner analytics and dispute queue, AI job description assistant and quote-draft, support assistant grounded in help docs, Windows installer and self-update, screenshots at 5 widths × 2 languages × 2 themes, accessibility WCAG 2.2 AA audit, Lighthouse mobile 90+, design tokens and RTL-first, empty states for every screen, consent banner and cookie audit, rate limit middleware, cross-tenant Firestore isolation, PWA offline support, Electron desktop shell
- Each task has acceptance test criteria and matching skills from ops/SKILLS_INDEX.md

### 2. Created plans/sir-handyman-REFRESH-LOG.md
- Documents all changes made in this round
- Lists research sources (FilKhedma, Khidhma web pages fetched 2026-11-12)
- Records plan improvements (task splitting, risk additions, RTL design mandate, PWA offline, webhook test expansion)
- Date-stamped for traceability

### 3. Enhanced plans/sir-handyman.md
- Added 11 new risks with recommended answers (RTL design gap, cold start quote generation, PDPL 151/2020 compliance scope, Paymob/Fawry test mode limitations)
- Updated existing risks with more detail
- Risks now cover: two-sided cold start, stranger enters home, price disputes, fake ratings, worker churn, gateway/eKYC/tax numbers, static export, safety tier, price undercuts, Arabic RTL design gap, cold start quote generation, PDPL compliance scope, Paymob/Fawry test limitations
- Each risk has a recommended answer for immediate planning guidance

### 4. Updated competitor research (ops/competitors/sir-handyman.md)
- Webfetched FilKhedma page (2026-11-12): 19 service categories, 1-month maintenance guarantee, vetted Heroes, flexible scheduling, B2B partner program, 19125 hotline, fixed-price menu absent (quote-based model)
- Webfetched Khidhma page (2026-11-12): fixed-price list per service (cleaning EGP 99/149/199, plumber EGP 150, electrician EGP 175), discount code KHIDHMA20, Arabic and English site, customer reviews, web booking works today, app "coming soon", 10K+ bookings (claim), 4.9 average rating (claim), 5k+ verified professionals (claim), 41s response time (claim), vehicle repair category, coverage Cairo-only
- Added sourcing tasks from the competitor file for future verification

### 5. Team board updated (ops/bus/team.md)
- Start line added: 19:45 opencode START r61-plan-sir-handyman planning-only refresh of SIR Handyman plan (rule 20)
- Finish line added: 19:55 opencode DONE r61-plan-sir-handyman planning-only: 42 tasks expanded, REFRESH-LOG created, risks+open questions added, team board updated; ready for queue

### 6. ops/bus/sir-hq.md updated
- One-line summary added documenting the planning-only refresh

## Risks and Open Questions (11 new entries)

1. **Arabic RTL design gap** - Most Egyptian pages mix Arabic and English; no fully RTL Egyptian-product with proper bidi isolation. Recommended: enforce RTL design first from M0; use IBM Plex Sans Arabic / Cairo / Tajawal; test every screen in Arabic and English, light and dark, from day one.

2. **Cold start quote generation** - With only 5 workers initially, quote volume may be too low. Recommended: keep M0-M1 sourcing period exclusive (5 workers + 5 jobs minimum) before opening quote feed; during M0-M1, display empty state with one action rather than showing empty quote feed.

3. **PDPL 151/2020 compliance scope** - Full legal review of every data collection point is pending. Recommended: schedule lawyer review as M6 gate; until then, keep all data collection minimal and tagged "(unsourced, verify)".

4. **Paymob/Fawry test mode limitations** - Real gateway behavior may differ from emulator tests. Recommended: run at least 20 negative webhook tests (expand from 10) before moving to test accounts; after launch, validate webhook signatures against live gateway documentation before enabling paid plans.

5. **Competition undercuts prices** - Default: never compete on price; compete on agreed price, identity, visit tracking and dispute protection.

6. **Safety tier on gas and electrical jobs** - Default: separate safety-QA pass per category, server-enforced, licence-check where Egyptian law requires one.

7. **Static export killing the server** - Default: no secret ever in a route handler that a static host would drop; server features run on functions side from M1.

8. **Gateway, eKYC and tax numbers** - Default: every one "(unsourced, verify)" until read on official page. Paymob/Fawry fee schedules for Egypt not publicly documented; tax treatment of service fees requires lawyer verification; eKYC provider selection remains unsourced.

9. **Worker churn from a bad first week** - Default: first three payouts only after 3 completed jobs and an ID pass, weekly worker report with earnings, service fee visible as single line.

10. **Fake ratings and shill reviews** - Default: one rating per completed booking per user, server-enforced; no rating without completed booking; rating locked after dispute window closes.

11. **Two-sided cold start in one district** - Default: one Cairo district, 5 real workers and 5 real completed jobs before any advertising or search push.

## Acceptance Tests and Verification

All 42 tasks have explicit exit checks with "green" meaning the output was seen, not assumed. The first 10 tasks are ready to hand to free agents immediately. Tasks 11-42 provide granular coverage of the full product lifecycle from foundations through release.

## Next Steps (for when building starts)

- M0 round: create Firebase project sir-handyman, GitHub repo sirahmed8/sir-handyman, monorepo scaffold, design tokens, DATA_SOURCES.md, eKYC provider research
- Free agents can start with tasks 1-10 immediately after M0 is complete
- All tasks require Playwright coverage at 390 px and 1280 px, Arabic and English, light and dark
- Five states on every screen: idle, loading skeleton, empty with one action, error with retry, populated
- No emoji, no placeholders, no invented data, version 1.0.0
- CI: local pnpm verify must pass (typecheck, lint, tests, build, gitleaks)
- Both hosts (Firebase Hosting and Vercel) must answer curl-checked 200