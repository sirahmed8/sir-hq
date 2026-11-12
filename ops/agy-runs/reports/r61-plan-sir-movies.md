# Report: r61-plan-sir-movies (planning-only refresh, rule 20/22)

**Date:** 2026-11-12 · **Tool:** devin · **Result:** ok

## What the task was

Round r61 planning-only rescan of SIR Movies per `ops/briefs/r61-plan-sir-movies.prompt.txt`: re-read the project, improve `plans/sir-movies.md` with fresh research and more detail, expand `ops/briefs/sir-movies-tasks.md` to 40+ tasks with acceptance tests and skills, update `ops/competitors/sir-movies.md`, write `plans/sir-movies-REFRESH-LOG.md`, risks + open questions with recommended answers. No code, no writes inside `D:\Projects\SIR Movies`.

## What I did

1. Read `ops/WORKER_PREAMBLE.md`, `.sir/CHECKPOINT.md`, the brief, `git status`/`git log`/`git diff --stat`, `ops/bus/team.md` tail, `D:/Projects/AGENTS.md`, `plans/PRODUCT_DIRECTION_2026-11-12.md`, `ops/TICKTICK_MAP.md`, `plans/sir-movies.md` (full), `ops/briefs/sir-movies-tasks.md`, `ops/competitors/sir-movies.md`, and `D:/Projects/SIR Movies` read-only (skeleton, `.sir` files, AGENTS.md, README, git log).
2. Checked state: `ops/ci-quota-exhausted.flag` exists (rule 18: local verification replaces CI-green). `D:\Projects\SIR Movies` now exists (commit `009dd34`, remote `sirahmed8/sir-movies` configured) — the r54 plan's "does not exist" claim was stale and is corrected. `.sir/CHECKPOINT.md` inside the project is stale ("No commits yet"); fixing it is task 1 of the new queue, not this round's scope.
3. Web research (sources below), then wrote all deliverables.

## Files changed (all under `D:/Projects/_SIR`, explicit paths committed)

- `plans/sir-movies.md` — header/truth updated; new §3.1 r61 research refresh; new §4.0 screens/surfaces table (16 surfaces); data model extended (`alerts`, `notifications`, `smartLists`, `imports`, `moderation`, `aiThreads`); new §6.9 PDPL compliance; new §6.10 external API surface + cost map; monetisation unit-economics note; §11 risks/open questions rewritten with recommended answers; §12 owner list extended; §9.1 points to 48 tasks.
- `ops/briefs/sir-movies-tasks.md` — rewritten: **48 tasks** in M0-M6 groups, each with brief + exit check + verified skill names; first 10 ready to queue; dependency notes; exclusions.
- `ops/competitors/sir-movies.md` — new §4 second ring (7 competitors) + 6 category findings; sourcing tasks 1-2 resolved/partial; new tasks 8 (PDPL) and 9 (cinema feeds).
- `plans/sir-movies-REFRESH-LOG.md` — new.
- `ops/bus/team.md` — START + DONE lines. `ops/bus/sir-hq.md` — one DONE line.

## Research findings (all opened 2026-11-12)

- **PDPL now enforced** — Executive Regulations Decree 816/2025 grace period ended 2026-10-31; PDPC licence + registered DPO (exam) + 72h breach notification + cross-border consent + criminal sanctions. Biggest new launch blocker; owner/legal action. Sources: Baker McKenzie insight 2026-10, LegalIn English PDF of Decree 816/2025, Kluwer/Amereller analyses.
- **TMDB commercial API = $149 USD/month** — TMDB staff forum answer 2026-10-14; free tier non-commercial w/ attribution; no AI training on TMDB content; 6-month cache cap. Source: themoviedb.org/api-terms-of-use, developer FAQ, forum thread.
- **JustWatch Partner API is real** — `apis.justwatch.com` content-partner API + widget + data dump; contract + partner token; branded JustWatch link mandatory; 500+ providers/120+ countries/daily updates. Source: apis.justwatch.com docs, justwatch.com API page.
- **Watchmode API pricing public** — Developer free 2,500 credits/mo (non-commercial, 3 countries, attribution); Startup $349/mo, Business $599/mo commercial; 436 services/54 countries; "leaving soon" data. Source: api.watchmode.com/pricing.
- **Cinema data options** — International Showtimes API v5 (120+ countries, free trial), The Boxoffice Company Source (70+ countries), elCinema licensed web service (SOAP/REST, weekly), VOX Egypt showtimes page verified live. Sources: respective sites opened today.
- **New competitors** — ReelRifter (AI chat over watchlist, MCP server, extension scrobble, spoiler-free catch-up, year-in-review; Pro-gated AI), Moviebase (Trakt two-way sync), Movie Paradise (multi-source ratings, Jellyfin/Plex scrobble, smart lists, AI chat), Simkl (scrobble hub, PRO/VIP recs), Omniphile, Logfolio, Limelight. Category findings: AI-over-watchlist and multi-source ratings are now expected; Trakt free tier tightened (1 community app, VIP $59.99/yr); Letterboxd Pro $18.99/yr, still no TV.

## Commands run (real)

- `git status -sb`, `git log --oneline -8`, `git diff --stat` — tree had only generated dashboard/READ_LOG/team.md churn from other agents; nothing broken, nothing of mine reverted.
- `git -C "D:\Projects\SIR Movies" status/log/remote -v` — skeleton healthy, remote configured.
- `wc -l`/`grep` on plan/tasks/competitors/SKILLS_INDEX — verified all cited skill names exist (`nextjs`, `firebase_*`, `firestore_rules_creation`, `database-reliability-transactions`, `legal-compliance-shield`, `ai-gateway`, `open-seo-auditor`, `a11y-debugging`, `emil-motion-impeccable`, `anti-vibecoded-design-system`, `taste-design-engine`, `modern-ui-ux-design-system`, `mobile-ergonomics-polish`, `production-engineering-standards`, `zero-trust-security-hardening`, `vibe-auth-hardening`, `owasp-vulnerability-shield`, `verification`, `agent-supercharged-os`, `karpathy-skills`, `high-conversion-copywriting`, `commercial-app-blueprint`, `cookie-debugging`, `env-vars`, `routing-middleware`, `deployments-cicd`, `firebase_hosting_basics`, `firebase_app_hosting_basics`, `firebase_auth_basics`, `firebase_firestore`, `firebase_security_rules_auditor`, `auth`, `chat-sdk`, `android-cli`, `modern-app-engineering`, `modern-web-guidance`, `react-best-practices`, `turbopack`, `shadcn`-adjacent, `sir-ecosystem-orchestrator`, `agent-reach`, `debug-optimize-lcp`, `application-testing`, `api-engineer`, `internet-skill-finder` — `notifications`, `telegram-bot`, `bot` do NOT exist in the index and were not cited).
- 5 web searches (competitors 2026, JustWatch API, TMDB terms, cinema APIs, tracking-app features, Watchmode pricing, Egypt PDPL) — outputs summarized above.

## What is unsure / open

- JustWatch/Watchmode/elCinema/International-Showtimes commercial terms all require outreach — queued as sourcing tasks and plan outreach items; none blocks the build.
- PDPL licence cost and DPO category unknown until owner engages PDPC — flagged as top owner action in plan §11/§12.
- Arabic title coverage in TMDB unmeasured — task queue includes a measurement step (recommendation in §11).
- The uncommitted `assets/brand/icon.png` change and stale `.sir/CHECKPOINT.md` inside `D:\Projects\SIR Movies` belong to the earlier r58/r60 folder work; left untouched per planning-only scope (task 1 of the queue fixes the checkpoint).

## Recommendation next

Queue tasks 1-10 of `ops/briefs/sir-movies-tasks.md` when HQ assigns build rounds (an r60 build brief already exists). Before public launch: PDPL licence + DPO (owner), TMDB commercial decision, cinema data agreement or licensed feed, legal review.
