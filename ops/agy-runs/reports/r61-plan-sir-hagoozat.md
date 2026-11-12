# Report: r61-plan-sir-hagoozat (planning-only refresh, rule 20)

Date: 2026-11-12. Worker: devin (SWE-2 Flash Medium). Scope honored: wrote only under `D:/Projects/_SIR` (`plans/`, `ops/competitors/`, `ops/briefs/`, `ops/bus/`, report). Nothing written inside `D:/Projects/SIR Hagoozat`, no repos created, no code written.

## What the previous round left

The earlier r61 attempt (cli log `ops/agy-runs/cli-r61-plan-sir-hagoozat.log`) died on a model token limit before doing any work — its final output was a request for files it could not see. Nothing was broken in the tree; `git status` showed only other agents' uncommitted ops files, which were left untouched. No checklist file exists for this task; the brief `.md`/`.prompt.txt` is the checklist and was followed item by item.

## Inputs read

`ops/WORKER_PREAMBLE.md`, `.sir/CHECKPOINT.md`, `ops/briefs/r61-plan-sir-hagoozat.md` + `.prompt.txt`, `plans/PRODUCT_DIRECTION_2026-11-12.md`, `plans/sir-hagoozat.md` (full), `plans/sir-hagoozat-DEEP.md`, `plans/BACKLOG_IDEAS_DECISIONS.md`, `ops/briefs/sir-hagoozat-tasks.md`, `ops/competitors/sir-hagoozat.md`, `ops/TICKTICK_MAP.md`, `ops/SKILLS_INDEX.md`, `ops/bus/team.md` (tail), `ops/bus/sir-hq.md` (tail), product folder read-only (`.sir/CHECKPOINT.md`, `.sir/PLAN_REFRESH.md`, `.sir/TASKS.md`), `git status`, `git log -5`, `git diff --stat`.

## Research performed (web, all dated 2026-11-12)

- Yalla Hagz site, Google Play and App Store listings: their 2026 rebuild added Solo Kickoffs, Team Fillups, Squads (split booking + RSVP), wallet/rewards, per-court ratings; claims 75K players / 250+ venues / 100K hours; App Store Sports #5 in Egypt, 4.9 from 1.4K ratings; Play 5.0 from 1.36K reviews; "Contains ads" label.
- Kourtiva pricing page opened: Starter AED 75/mo (4 pitches, 3 staff), Growth AED 185/mo (15 pitches, 10 staff, read-only API), Pro AED 369/mo (30+ pitches, unlimited staff, full REST API), 15-day free trial no card, prices excl. VAT.
- New competitors recorded: Courty (multi-sport, Greater Cairo + Alexandria, live slots, venue dashboard) and Tahgzly (padel live in Cairo/Giza/New Damietta/Ras El Bar, QR pass, club listing, AR+EN); Kickoff kept as unsourced.
- Payment fees: Paymob published 2.75% + 3 EGP/txn, no monthly fee, weekly settlement; PayTabs 2.5% + 2-3 EGP by volume; Fawry contract-quoted (~1.5-3.5%, unsourced); 14% VAT on gateway fees.
- Google Maps Platform post-2025-03-01 pricing: 10K free calls per Essentials SKU monthly, Maps SDK/Embed unlimited.
- WhatsApp Business Platform Egypt rates (Oct 2026 card): utility/auth US$0.0036 per delivered message, marketing US$0.0644; service window rules changed.
- Regulation: Egypt PDPL 151/2020 Executive Regulations effective 2025-11-01, grace until 2026-10-31; PDPC licences incl. cross-border transfers and e-marketing; financial data sensitive; breach-notification duties.
- Category trends: demand/weather-aware dynamic pricing, waitlist auto-promotion, hybrid membership + pay-and-play, venue AI assistants (Thril MCP), layered reminders (~48% no-show reduction claims).

## Files changed

1. `ops/competitors/sir-hagoozat.md` — Yalla Hagz row rewritten for the 2026 feature set; Kourtiva row gained published AED pricing; Courty, Tahgzly, Kickoff added to second ring; new section 4 "Market facts found in the second research pass"; sourcing tasks renumbered with items 1-2 done/partial.
2. `plans/sir-hagoozat.md` — 8 new parity rows in 3.1; WhatsApp opt-in rules in notifications; new 5.5.2 Firestore data model (18 collections, access rules, day-one indexes); new 5.9 `/api/v1` REST surface (30 routes with auth); new 5.10 PDPL + payment-rail gates; 5 new risks in section 11; new 11.1 open-questions table (8 questions with recommended answers); new section 12 launch & marketing (phases L0-L3, marketing rules); sections renumbered; version header updated.
3. `ops/briefs/sir-hagoozat-tasks.md` — expanded 10 → 50 tasks. T1-T10 kept queue-ready (each now names skills); T11-T50 cover open matches, squads, waitlist, voucher, QR pass, calendar/notifications, reviews, owner console, offline ledger, analytics, tournaments, community/chat/tickets, achievements/passport/profile, notification delivery, WhatsApp, Paymob/Fawry/InstaPay, subscriptions, owner onboarding, multi-sport, add-ons, recurring bookings, AI trio, Expo Android/iOS, offline PWA, legal/PDPL, SEO/GEO, marketing site, a11y, performance, security audit, self-audit loop, dual hosting, launch readiness. Each task has an exit check and named skills from `ops/SKILLS_INDEX.md`. Added milestone map, dependency notes, file-ownership map.
4. `plans/sir-hagoozat-REFRESH-LOG.md` — created; documents inputs, research, changes, risks, open promises.
5. `ops/bus/team.md` — START and DONE lines. `ops/bus/sir-hq.md` — one summary line.

## Commands run and real output (key ones)

- `git status -sb`, `git log -5 --oneline`, `git diff --stat` — baseline; other agents' uncommitted files noted and left alone.
- `grep -c "^## T"` on committed tasks file → `50` (verified in HEAD after push).
- `git show HEAD:plans/sir-hagoozat-REFRESH-LOG.md | head -5` → file present in HEAD.
- `git log origin/main..HEAD` → empty after push; `git status -sb` → `## main...origin/main` (not ahead).
- Commits: `2a1dd8f` (bus lines) plus earlier sweep `06937a9`/`0574fb8` which picked up the plan, competitors, tasks and refresh-log edits made earlier in this session — verified all content is in `origin/main` (a parallel worker's checkpoint commit swept the staged files; nothing lost, verified by `git show HEAD:` on each file).
- `git push origin main` → `06937a9..2a1dd8f main -> main`.

## CI status

`ops/ci-quota-exhausted.flag` exists, so per WORKER_PREAMBLE rule 18 "CI green" is replaced by local verification. These changes are Markdown documentation only — no code, no build artifacts — so there is nothing to compile or test; the verification performed was content checks (task count = 50 in committed file, refresh log present in HEAD, all four files on origin/main). No CI loop attempted.

## What is unsure / still open

- Fawry exact fee schedule remains contract-quoted ("(unsourced, verify)").
- Matchiva, Riadi, Mal3bk pages still snippet-level (sourcing task 3 in competitors section 5).
- Whether any Egyptian competitor sells a player subscription — still unconfirmed (sourcing task 5).
- AED→EGP conversion for Kourtiva price comparison is "(unsourced, verify)".
- Build remains gated: T1-T50 must not run until the owner authorizes building SIR Hagoozat (rule 22). Firebase project `sir-hagoozat` still not created.

## Recommended next

HQ queues T1-T4 (parallel-safe) only after owner authorization; a future planning round can close sourcing tasks 3-5 in `ops/competitors/sir-hagoozat.md` section 5.
