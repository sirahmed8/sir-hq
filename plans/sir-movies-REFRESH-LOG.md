# SIR Movies Refresh Log

**Round:** r61
**Date:** 2026-11-12
**Status:** Planning-only refresh per rule 20 (rescan before work); no product code written; nothing inside `D:\Projects\SIR Movies` was modified.

## What was re-read (rescan)

- `D:/Projects/AGENTS.md`, `_SIR/ops/WORKER_PREAMBLE.md`, `standard/OWNER_DEFAULTS.md` rules via preamble, `plans/PRODUCT_DIRECTION_2026-11-12.md` (SIR Movies = own small independent project, section 8), `ops/TICKTICK_MAP.md` (idea 29 -> SIR Movies), `ops/SKILLS_INDEX.md` (skill names verified before citing).
- `plans/sir-movies.md` (full 340-line r54 plan), `ops/briefs/sir-movies-tasks.md` (10 tasks), `ops/competitors/sir-movies.md` (10 competitors + second ring).
- `D:/Projects/SIR Movies` read-only: skeleton exists (commit `009dd34`, remote `sirahmed8/sir-movies` configured, `main` tracking `origin/main`); `.sir/CHECKPOINT.md` is stale (says "No commits yet"); `assets/brand/icon.png` has an uncommitted modification left by the earlier folder round; no product code.
- `ops/briefs/r60-build-sir-movies.md` exists (build round brief), `ops/ci-quota-exhausted.flag` exists (CI minutes exhausted; local verification is the gate).

## Changes made

1. **`plans/sir-movies.md`** — header/truth updated to r61 state (folder+repo exist, no code); new section 3.1 "r61 research refresh" (7 new competitors, verified pricing facts, concrete data-source map with costs, PDPL enforcement change, 2026 feature trends); new section 4.0 explicit screens/surfaces table (16 surfaces with routes and contents); data model extended with `alerts`, `notifications`, `smartLists`, `imports`, `moderation`, `aiThreads`; new section 6.9 Egypt PDPL compliance (licence, DPO, 72h breach, cross-border consent, children, criminal exposure); new section 6.10 external API surface and cost map (TMDB $149/mo commercial confirmed, JustWatch Partner API, Watchmode tiers, International Showtimes, elCinema licensing, Boxoffice Source, chains, FCM, Paymob/Fawry, AI providers); monetisation updated with unit-economics reality check; risks/open questions rewritten with recommended answers; owner-only list extended (PDPL licence+DPO flagged as biggest launch blocker); milestone task pointer updated to 48 tasks.

2. **`ops/briefs/sir-movies-tasks.md`** — rewritten from 10 to **48 tasks** grouped M0-M6, each with a concrete brief, exit check and verified skill names from `ops/SKILLS_INDEX.md`; first 10 ready to hand to free agents (task 1 = M0 tail since folder/repo already exist; tasks 2-10 = M1 foundation); dependency notes and deliberate exclusions at the end.

3. **`ops/competitors/sir-movies.md`** — new section 4 "Second ring added 2026-11-12 (r61 refresh)" with 7 competitors (ReelRifter, Moviebase, Movie Paradise, Simkl, Omniphile, Logfolio, Limelight) and 6 category-level findings; sourcing tasks 1-2 marked partially/fully answered; new sourcing tasks 8 (PDPL licence/DPO) and 9 (Egypt cinema feed evaluation).

4. **`ops/bus/team.md`** — START and DONE lines appended.

5. **Report** written to `ops/agy-runs/reports/r61-plan-sir-movies.md`; one line appended to `ops/bus/sir-hq.md`.

## Key research findings (all sourced 2026-11-12, dates kept)

- **PDPL is now enforced.** Executive Regulations (Decree 816/2025) grace period ended 2026-10-31; licence + registered DPO + 72h breach duty + cross-border consent + criminal sanctions. Biggest new launch blocker; owner/legal action.
- **TMDB commercial API = $149 USD/month** (TMDB staff forum answer 2026-10-14); free tier non-commercial with attribution; no AI training on TMDB content; 6-month cache cap.
- **JustWatch Partner API is real** (`apis.justwatch.com`, contract + token, branded link mandatory, 120+ countries); Watchmode has public pricing (free dev 2,500 credits/mo 3 countries; $349/mo commercial); International Showtimes API 120+ countries with free trial; elCinema sells licensed data; Boxoffice Source is enterprise.
- **Category moved:** AI-over-watchlist shipped (ReelRifter w/ MCP, Movie Paradise), multi-source ratings comparison is expected, Trakt tightened free tier (VIP $59.99/yr), Letterboxd Pro $18.99/yr still no TV.

## Open promises / next step

- Tasks 1-10 of `ops/briefs/sir-movies-tasks.md` are ready to queue when HQ decides (rule 22: free tools must NOT start building; an r60 build brief already exists).
- The stale `.sir/CHECKPOINT.md` inside `D:\Projects\SIR Movies` is fixed by task 1, not by this planning round (this round may not write outside `_SIR`).
- `assets/brand/icon.png` uncommitted change in the project repo belongs to the earlier folder round; left untouched.
- Before any public launch: PDPL licence + DPO (owner), TMDB commercial decision, cinema data agreement or licensed feed, legal review.
