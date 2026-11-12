# Report: r54-plan-sir-movies (2026-11-12)

Worker: free-models router (OpenCode). Brief: `D:/Projects/_SIR/ops/briefs/r54-plan-sir-movies.md`. One small independent project, plans and ops only. The brief forbids creating the project folder or repo this round, and nothing was created outside `plans/` and `ops/`.

## Files written (absolute paths)

1. `D:/Projects/_SIR/plans/sir-movies.md` — full rewrite of the r51 note into the premium plan (14 sections): vision, who/promise, names/IDs, competitors and our edge, features (parity + owner's carried-forward ideas), platform matrix, architecture on the shared kit (shape, owner-auth, owner-only `/owner` analytics, AI fallback chain with hard rules, Firestore data model with 15 collections, hosting/data sources/money, security baseline), lawful content rules, free tier and fair pricing in EGP and USD (owner free forever, prices tagged `(unsourced, verify)`), milestones M0–M6 with acceptance tests, skills used, risks, owner-only actions, visibility checklist, definition of done.
2. `D:/Projects/_SIR/ops/competitors/sir-movies.md` — 10 competitors (Egypt/Arab first, then global) with strengths, flaws, our edge, ideas to steal and source links, all pages opened 2026-11-12; plus a second ring and seven open sourcing tasks.
3. `D:/Projects/_SIR/ops/briefs/sir-movies-tasks.md` — the first 10 tasks for the free agents, title plus one-paragraph brief each, with queue order and per-task file ownership.

Bus line appended to `D:/Projects/_SIR/ops/bus/sir-hq.md` (2026-11-12 | r54-plan-sir-movies | ...).

## Git state

`main` at `f126eb6` "r54: premium plan for SIR Movies (plan, competitors, first 10 tasks)". Pushed to `origin/main` (`dd50628..f126eb6`). Explicit paths committed only: `plans/sir-movies.md` (modified), `ops/competitors/sir-movies.md` (new), `ops/briefs/sir-movies-tasks.md` (new). Unrelated untracked files in the tree were not staged. GitHub Actions quota flag (`ops/ci-quota-exhausted.flag`) is present per the worker preamble, so local verification is the recorded signal for this round; there is no build to run because this round wrote documents only.

## What the rescan found (read before writing)

- `plans/sir-movies.md` (r51, idea 29 "movies"): own product, Arabic-first, TMDB backend, Egypt cinema via chain agreements, legal-only where-to-watch, affiliate model, waves "after current GLOBAL products". Kept as the backbone; expanded with data model, owner analytics, M0–M6, platform matrix and ten queued tasks.
- `ops/TICKTICK_MAP.md`: ideas 23/26/28/29 were "concept backlog"; 29 is the movie list. `plans/PRODUCT_DIRECTION_2026-11-12.md` section 8 decides each unplanned idea is its own small project, including `SIR Movies` explicitly; section 6 sets the standard (Arabic+English, all platforms, owner analytics, free tier + subscriptions, Firebase+Vercel, competitor matrix, M0–M6, first 10 tasks). Section 5 lists movies under the unplanned ideas.
- `ops/IDEAS_INBOX.md`: no movie entries (empty inbox).
- `plans/PROJECT_MERGE_RECORD.md` and `plans/sir-hagoozat.md` / `plans/sir-laptop-manager.md`: consistent — movies is its own product, not a Hagoozat booking module, not a laptop-manager module. No conflict found.
- `plans/SHARED_PLATFORM_KIT.md` (all 20 sections) and `standard/OWNER_DEFAULTS.md` (incl. items 11, 14–19) were applied: own Firebase project `sir-movies`, own repo `sirahmed8/sir-movies`, dual hosting, owner-only analytics fail-closed, AI fallback chain with per-product keys, EGP-first pricing auto-detected with manual override, PDPL export/delete, Desktop folder kit defined as M0, no SIR Platform references.
- `ops/SKILLS_INDEX.md` scanned; skills listed in plan section 10.
- `D:\Projects\AHome` was not opened.
- No `.sir/PLAN_REFRESH.md` exists yet because the project folder does not exist; the plan and tasks instruct T1 to create it and log this r54 rescan there (rescan repeats at every milestone start per the rescan rule).

## Market research (web, 2026-11-12) — summary of the ten

Opened directly: elCinema (Arabic cinema editorial: now/coming-soon for Egypt+Gulf+Levant+Maghreb, booking deep links, weekly Egyptian box office quoted at 9,140,822 EGP for ولا كان عالبال week of 10 Nov 2026, TV guide, Ramadan 2027 rails), JustWatch (`/` and `/eg`: full Arabic UI for Egypt listing Netflix, Prime, Apple TV+, Disney+, STARZPLAY, Shahid VIP, TOD, Zee5, with one-search and watchlist+notify), Letterboxd (`/about/`, `/about/pro/`: free tier forever, annual Pro/Patron, JustWatch-powered service filter + watchlist arrival alerts, film data from TMDB, apps iOS/Android/Apple TV), Trakt (`/`: free web/iOS/Android tracking + "where it's streaming"), Shahid (`/ar`: free tier with ads + Shahid VIP, live channels, series/movies/kids). Not parseable/blocked today and marked `(unsourced, verify)` in the study: Watch iT (HTTP 200, body not readable by fetch), IMDb (empty body), TMDB (HTTP 403), Reelgood (HTTP 403), `developers.justwatch.com` (transport error), `cinemaclub.co` (HTTP 000 — grey-area piracy site, excluded by hard rule, kept only as demand evidence). Second ring recorded: Rotten Tomatoes, Metacritic, Yango Play, TOD, Flixster/Google TV.

Category truth: Egypt splits into cinema editorial (elCinema) and streaming catalogs (Shahid, Watch iT, Yango Play, TOD); aggregation exists (JustWatch /eg) but stops at the poster — no personal diary, no Arabic social lists, no cinema showtimes, no EGP pricing; tracking is English-first (Letterboxd, Trakt). The gap SIR Movies fills: one Arabic-first, account-based product combining discovery, watch/rate/review, legal where-to-watch per region (Egypt first), Egyptian cinema showtimes under written chain permission, friend shared lists, seen-together social proof, and fair EGP-first pricing.

## Truth rule: what is verified vs not

Verified today: the three output files exist in git (`f126eb6`), push succeeded, bus line appended, competitor pages opened as dated, old plan read. **Not verified and must not be claimed:** any code, any build, any deployment, `D:\Projects\SIR Movies` (does not exist), repo `sirahmed8/sir-movies` (not checked — created at M0 by T1), Firebase project `sir-movies`, TMDB commercial eligibility, JustWatch partner program, any cinema chain's written permission, Watch iT/WeTV plan prices, Letterboxd Pro/Patron exact prices, Egyptian copyright clearance for any showtime feed (all flagged `(unsourced, verify)` in the study).

## What is unsure / open decisions

1. Cinema data path: no chain has granted permission yet. Default in the plan: curated from chain-published pages with `source` + `checkedAt`, labelled in the UI; booking deep links only under written agreement; otherwise "احجز من موقع السينما" to the chain's official page. Escalate: owner or HQ contacts VOX / Cairo Festival City / Galaxy / Plaza / Americana.
2. TMDB commercial licence must be re-read before M3 monetisation; plan blocks paid launch until read.
3. Domain choice (`sirmovies.app` vs `.eg`) and all payment keys are owner actions (list in plan section 12).
4. Version stays 1.0.0; no store submission without owner accounts.

## Recommended next steps (in order)

1. HQ/owner approve the wave placement (plan says wave 9, after current GLOBAL products) and run T1 (M0: folder, `.sir/`, repo, Desktop kit) as its own round.
2. T2+T3+T4 in parallel after T1; T5 after T2/T4; T6 after T2/T3/T5.
3. Owner actions: buy domain; read TMDB commercial terms; contact one cinema chain for written permission; open Paymob test account. Each is one tiny step in `D:/Projects/_SIR/ops/OWNER_ACTIONS.md` if HQ queues it.
4. Before any public comparison page or marketing claim, re-run the competitor study (it is dated 2026-11-12) and close the seven sourcing tasks in the competitor file section 4.

## Commands run and their real output (key lines)

- `git status --short` / `git log -5 --oneline` — tree had pre-existing unrelated untracked files (r52/r53 leftovers); none staged.
- `wc -l` on read files; `cat`/`sed -n` on the read list.
- `webfetch` on: letterboxd.com/about/, letterboxd.com/about/pro/, justwatch.com, justwatch.com/eg, shahid.net, trakt.tv, elcinema.com, watchit.com (200, unparseable), reelgood.com (403), themoviedb.org (403), developers.justwatch.com (transport error); `curl` status checks: watchit 200, cinemaclub.co 000, justwatch.com/eg 200.
- `git add plans/sir-movies.md ops/competitors/sir-movies.md ops/briefs/sir-movies-tasks.md` → `git commit -m "r54: premium plan for SIR Movies (plan, competitors, first 10 tasks)"` → `[main f126eb6] ... 3 files changed, 438 insertions(+), 68 deletions(-)` → `git push origin main` → `dd50628..f126eb6  main -> main`. LF→CRLF warnings only, no errors.
- `tail -5 ops/bus/sir-hq.md` (format reference) then one-line append via heredoc.
- No code was built; no browser tests were needed (documents only); no secrets were read, printed or committed.
