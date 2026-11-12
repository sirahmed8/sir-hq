# SIR Hagoozat Refresh Log

**Round:** r61-plan-sir-hagoozat
**Date:** 2026-11-12
**Status:** Planning-only refresh per rule 20; no code, no folder, no repo created (owner order: free tools must NOT start building these projects)

## What was re-read

- `D:/Projects/AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `standard/23-premium-code-bar.md` (via brief requirements)
- `plans/PRODUCT_DIRECTION_2026-11-12.md`, `plans/sir-hagoozat.md`, `plans/sir-hagoozat-DEEP.md`, `plans/BACKLOG_IDEAS_DECISIONS.md`
- `ops/briefs/sir-hagoozat-tasks.md`, `ops/briefs/r61-plan-sir-hagoozat.md` + `.prompt.txt`
- `ops/competitors/sir-hagoozat.md` (canonical) and `plans/competitors/sir-hagoozat.md` (superseded r44)
- `D:/Projects/SIR Hagoozat` read-only: `.sir/CHECKPOINT.md`, `.sir/PLAN_REFRESH.md`, `.sir/TASKS.md`, folder layout, `legacy/`
- `ops/TICKTICK_MAP.md`, `ops/SKILLS_INDEX.md`, `ops/bus/team.md`, `ops/bus/sir-hq.md`
- Git state: `git status`, `git log -5`, `git diff --stat` (other agents' uncommitted ops files left untouched)

## Research done this round (web, 2026-11-12)

1. Egyptian pitch-booking market re-check: Yalla Hagz's 2026 rebuild now includes Solo Kickoffs, Team Fillups, Squads with split booking, wallet and rewards, per-court ratings; App Store Sports #5 in Egypt, 4.9/1.4K ratings, Play 5.0/1.36K reviews.
2. Kourtiva pricing page opened: published owner tiers AED 75 / 185 / 369 per month, 15-day free trial, no card; read-only API on Growth, full REST API on Pro.
3. New competitors found and recorded: Courty (multi-sport, Greater Cairo + Alexandria) and Tahgzly (padel live in Cairo/Giza/Damietta/Ras El Bar, QR pass, clubs can list); Kickoff apps kept as unsourced.
4. Payment fees sourced: Paymob publishes 2.75% + 3 EGP per transaction, no monthly fee, weekly settlement; PayTabs 2.5% + 2-3 EGP by volume; Fawry contract-quoted (~1.5-3.5%, unsourced); 14% VAT on gateway fees.
5. Google Maps Platform pricing (post-2025-03-01): 10K free calls per Essentials SKU monthly, Maps SDK/Embed unlimited; key still needs a billing cap.
6. WhatsApp Business Platform Egypt rates (Oct 2026 card): utility/auth US$0.0036 per delivered message, marketing US$0.0644; service-window rules changed (utility billed inside window, first 1,000 service replies free/month).
7. Regulation: Egypt PDPL 151/2020 Executive Regulations effective 2025-11-01, grace until 2026-10-31; PDPC licences required incl. cross-border transfers and electronic marketing; financial data is sensitive; breach-notification duties and criminal penalties. Now a launch gate.
8. Category trends 2026: demand/weather-aware dynamic pricing, waitlist auto-promotion, hybrid membership + pay-and-play, venue-facing AI assistants (Thril MCP), layered reminders cutting no-shows.

## Changes made

1. `ops/competitors/sir-hagoozat.md`: rewrote the Yalla Hagz row with the 2026 feature set and store numbers; added published Kourtiva pricing to its row; added Courty, Tahgzly and Kickoff to the second ring; added new section 4 "Market facts found in the second research pass" (payments, maps, WhatsApp, PDPL, trends); renumbered sourcing tasks and marked items 1-2 done/partial.
2. `plans/sir-hagoozat.md`: added 8 parity rows to section 3.1 (Solo Kickoff, Team Fillup, Squad RSVP, waitlist auto-promotion, weather voucher, per-court proven reviews, WhatsApp opt-in updates, owner AI assistant); added WhatsApp opt-in rules to notifications; new section 5.5.2 (Firestore data model: 18 collections with key fields, access rules, day-one indexes); new section 5.9 (typed `/api/v1` REST surface, 30 routes with auth); new section 5.10 (PDPL 151/2020 gates + sourced payment-rail facts); added 5 new risks to section 11; new section 11.1 (8 open questions with recommended answers); new section 12 (launch and marketing phases L0-L3 with marketing rules); renumbered owner-actions and sources to 13 and 14; updated the version header.
3. `ops/briefs/sir-hagoozat-tasks.md`: expanded from 10 to 50 tasks. T1-T10 kept ready to hand to agents (each now also names its skills); T11-T50 added covering open matches, squads, waitlist, voucher, QR pass, calendar/notifications, reviews, owner console, offline ledger, analytics, tournaments (knockout/league/scoreboard), community/chat/tickets, achievements/passport/profile, notification delivery, WhatsApp, Paymob/Fawry/InstaPay, subscriptions, owner onboarding, multi-sport, add-ons, recurring bookings, AI trio, Expo Android/iOS, offline PWA, legal/PDPL, SEO/GEO, marketing site, a11y, performance, security audit, self-audit loop, dual hosting, launch readiness. Each task has an exit check and named skills from `ops/SKILLS_INDEX.md`. Milestone map, dependency notes and file-ownership map added.
4. `ops/bus/team.md`: START and DONE lines for this task.
5. Report: `ops/agy-runs/reports/r61-plan-sir-hagoozat.md`.

## Risks and open questions (summary; full list in plan section 11.1)

- Yalla Hagz is stronger than the r52 snapshot assumed; our edge narrowed to Egyptian dialect, join-time split payment, owner analytics/cash register, offline-first, proven reviews. Parity rows added so we do not lose on table stakes.
- Kourtiva's AED pricing is far above our EGP test price but they sell to UAE-facing operators via demo; we keep self-serve EGP pricing, never claim cheaper until FX verified.
- Gateway fees (~7% effective on a 100 EGP deposit) must be priced in or passed through; shown before launch.
- PDPL licensing is now a hard gate before real Egyptian personal data at scale (grace ends 2026-10-31).
- Still unsourced: Fawry exact rates, Matchiva/Riadi/Mal3bk feature detail, player-side subscription existence anywhere in Egypt.

## Open promises

- Build remains gated on owner authorization (rule 22); T1-T10 stay queue-ready but must not run until then.
- Firebase project `sir-hagoozat` still not created (no firebase CLI on this machine per r60 notes; owner action when build is authorized).
- Owner actions unchanged: domain, gateway accounts, lawyer, real venue outreach, Play/App Store accounts later.

## Next step

HQ queues T1-T4 (parallel-safe) only after the owner authorizes building SIR Hagoozat; until then the next planning round can re-verify the unsourced items in competitors section 5.
