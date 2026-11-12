# Report: r54-plan-sir-access-map

## What this task was

HQ brief `ops/briefs/r54-plan-sir-access-map.prompt.txt` (round r54, 2026-11-12): write the premium plan for **SIR Access Map**, one of the small independent projects decided in `plans/PRODUCT_DIRECTION_2026-11-12.md` section 8 and `plans/BACKLOG_IDEAS_DECISIONS.md` section 3.4. Build last. Output only under `D:/Projects/_SIR`: `plans/sir-access-map.md`, `ops/competitors/sir-access-map.md`, `ops/briefs/sir-access-map-tasks.md`, plus one line to `ops/bus/sir-hq.md`. Do NOT create the project folder or repo this round.

## State found at start

- `git status`: clean for this task's files; many unrelated unstaged changes from other workers (dashboard artifacts, queue, reports). No prior work on sir-access-map existed: `plans/sir-access-map.md`, `ops/competitors/sir-access-map.md`, `ops/briefs/sir-access-map-tasks.md` did not exist and no commits touched them.
- The legacy note `plans/accessibility-map-module-note.md` exists and is marked SUPERSEDED; it made the idea a module of SIR Life Part B. The owner's later decision (direction file section 8) makes it its own project. The plan carries that decision forward and cites it.
- `.sir/CHECKPOINT.md` has no r54-access-map section; this round's work is recorded here and in the bus line.

## What was done

1. Read all required inputs: `D:/Projects/AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `standard/OWNER_DEFAULTS.md`, `plans/PRODUCT_DIRECTION_2026-11-12.md` (sections 6 and 8 binding), `ops/briefs/r52-product-premium-plan.md`, `plans/SHARED_PLATFORM_KIT.md`, `plans/accessibility-map-module-note.md`, `plans/BACKLOG_IDEAS_DECISIONS.md` (section 3.4 and the build order), `ops/TICKTICK_MAP.md` (idea 26 row), and the sibling deliverables `plans/sir-cars.md`, `ops/competitors/sir-cars.md`, `ops/briefs/sir-cars-tasks.md` for format.
2. Rescanned for existing notes: grep over `ops/IDEAS_INBOX.md`, `ops/TICKTICK_MAP.md`, `plans/BACKLOG_IDEAS_DECISIONS.md` and `plans/` found the module note, the decision file entry and the TickTick backlog row. Nothing else existed.
3. Market research on the web (2026-11-12): searches for wheelchair/accessibility map apps and for the Egyptian/Arab market. Found the real Egyptian players: **Entaleq (انطلق)** by HELM nonprofit (~200 places, 9 categories, 4-point entrance audit, Arabic+English, last Play update Oct 2024), **أماكني (Amakiny)** iOS app from 2018 billed as first in Egypt/Middle East with place-owner self-listing, and the **Acsibility** student project. Global: Wheelmap (claimed ~3.2M places per WIRED), AccessNow/AXSMap, iAccessLife, Wheelmate, WheeLog!, HandicapX, Mapp4All.
4. Wrote `ops/competitors/sir-access-map.md`: 10 competitors with market, strengths, flaws, our edge, ideas to steal and sources; a second ring (Acsibility, Access Earth, Flush Toilet Finder, Access Guide, platform step-free transit); an "Egypt and Arab market" section; five stated edges; seven open sourcing tasks. Unsourced claims are tagged "(unsourced, verify)" per the truth rules.
5. Wrote `plans/sir-access-map.md` (~330 lines) with every required section: vision and three promises (user, caregiver/place-owner, contributor), the end state, competitor summary table, features (parity table, owner-idea traceability table citing the brief scope, decision file rules and the superseded module note, explicit out-of-scope, lawful-data rules), platform matrix (web/PWA required, Windows/macOS/Linux M5, Android/iOS M4, Wear OS/watchOS/TV/car skipped with reasons), architecture on the shared kit (monorepo shape, owner-auth, the full data model Place/FeatureClaim/PhotoEvidence/Confirmation/Claim/RoutePlan/SavedPlace/ModerationItem with the publish rules, owner-only `/owner` analytics, AI fallback chain with a hard-rules table, data/map-provider/money, security and privacy baseline, dual hosting), premium quality bar (motion, RTL/bidi, five states, WCAG 2.2 AA plus large-text/high-contrast toggle because the audience needs it), free tier and EGP/USD test pricing (Explorer Free/Pro, Contributor free, Place Owner Free/Verified) with fairness rules, milestones M0-M6 each with runnable acceptance tests, the first ten tasks, the skills list, and risks with defaults.
6. Wrote `ops/briefs/sir-access-map-tasks.md`: ten ready-to-queue task briefs, each one paragraph with an exit check, covering scaffold, Firebase+folder+auth, data model+rules, map view, place profile, submission flow, photo upload+moderation queue, confirmation+publish engine, owner claim flow, owner analytics+billing fallback.
7. Appended one line to `ops/bus/sir-hq.md`.
8. Committed and pushed. First push was rejected because `origin/main` had moved (another worker pushed `2c2b2ae` r54-plan-sir-handyman meanwhile); `git pull --rebase` was blocked by unrelated unstaged files, but a re-check showed local and remote had converged: final state is commit `f7d2f82` "r54: premium plan for SIR Access Map (crowd-checked accessibility map, built last)" on `origin/main`, containing exactly the three deliverable files plus the bus line.

## Commands run and real output (key lines)

- `git status` / `git log --oneline -10` / `git diff --stat` at start: showed unrelated unstaged worker files; no sir-access-map files.
- `ls plans/ | grep -i access` -> only `accessibility-map-module-note.md`; `ls ops/competitors/` and `ops/briefs/` had no sir-access-map files.
- `git commit -m "r54: premium plan for SIR Access Map ..."` -> created `f7d2f82` with `ops/briefs/sir-access-map-tasks.md`, `ops/competitors/sir-access-map.md`, `plans/sir-access-map.md` (and the accumulated `ops/bus/sir-hq.md` lines).
- First `git push origin main` -> `! [remote rejected] main -> main (cannot lock ref ... is at f7d2f82 but expected bda2855)`; after fetch/re-check, `git status -sb` showed `main...origin/main` in sync and `git ls-tree origin/main` lists all three files at `f7d2f8255de8222e6def4ee10eebda29b8c9d9ce`.
- `gh run list --limit 3` -> both runs on the push commit succeeded:
  - `completed success r54: premium plan for SIR Access Map ... verify main push 43259639968 16s`
  - `completed success r54: premium plan for SIR Access Map ... test main push 43259639932 9s`
- Note: `ops/ci-quota-exhausted.flag` still exists, but the Actions runs on this commit actually executed and passed (16s and 9s), so CI on main is genuinely green for this push, not just locally substituted.

## What is in the plan (summary for HQ)

- Promise: "Know before you go: is this place really usable for me, and how do I get there without a barrier?"
- Differentiators vs the field: photo evidence + second-user confirmation publish gate, dated/re-check-windowed feature claims, place-owner claim flow, barrier-avoiding route that names each avoided barrier, Egypt/Arab-first Egyptian-Arabic coverage.
- Honest cost kept from the decision file: separate Firebase project, repo, domain and store listing for a small audience; built last; reuses shared kit map layer; owner may drop it.
- M0 explicitly creates `D:/Projects/SIR Access Map` with `.sir/`, `AGENTS.md`, repo `sirahmed8/sir-access-map` and the Desktop folder kit per OWNER_DEFAULTS item 19 — and this round did NOT create any of it.

## What is still open / unsure

- Sourcing tasks in the competitor file section 4 remain open (each under one hour): Wheelmap Egypt coverage counts, Entaleq full listing, store ratings for the five global apps, AccessNow/iAccessLife feature pages, Egyptian accessibility standards baseline, OSM/map-provider licence check for Egypt, Egyptian municipality/NGO lists.
- The repo name `sirahmed8/sir-access-map` is assumed from the decision file and is unverified until M0.
- Map provider choice (OSM/OSRM vs licensed) is an M0 decision recorded in `docs/DATA_SOURCES.md`.
- The plan is built-last by owner decision; nothing here schedules it before the other small projects.

## Recommendation next

Queue nothing for this product until the earlier small projects (Price Finder, Game Deals, Cars, Movies, Handyman) are further along; when its turn comes, start with task 1 (scaffold) then task 2 (M0: folder, Firebase project, repo, owner-auth).
