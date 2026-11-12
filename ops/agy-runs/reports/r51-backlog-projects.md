# REPORT: r51-backlog-projects (HQ planning round, 2026-11-12)

## Task brief (from /d/Projects/_SIR/ops/briefs/r51-backlog-projects.prompt.txt and .md)

HQ planning round (2026-11-12): the owner feels projects are missing. The record plans/PROJECT_MERGE_RECORD.md lists ideas from his TickTick note (30 ideas) that were left as "concept backlog, not planned": price finder and game-deal finder (ideas 15,16), cars (23), accessibility map (26), handyman (28), movies (29). Ideas 14 and 21 were dropped for legal and privacy reasons: keep them dropped.

The brief told the worker to read D:/Projects/AGENTS.md, ops/WORKER_PREAMBLE.md, standard/OWNER_DEFAULTS.md, plans/PROJECT_MERGE_RECORD.md and plans/MAIN_PLAN.md first, re-read the owner's own wording of the ideas from the TickTick note "أفكار برامج ومشاريع" and the legacy folders (never the note Accounts or the habobty column), decide per idea with a short reason whether it is its own product or a module of an existing product, create a project folder only for the ones that deserve to be separate, update plans/PROJECT_MERGE_RECORD.md and the portfolio map in D:/Projects/AGENTS.md with the final product list and counts, then commit and push (explicit paths), checkpoint and add one line to ops/bus/sir-hq.md. The brief also said: plans only, no product code.

The runner instruction (scripts/cli-run2.sh) adds: finish every unticked item completely (commit, push and checkpoint after each item), then write the report and run the done command from the manual.

## Where I started (state found)

- Read /d/Projects/_SIR/ops/WORKER_PREAMBLE.md, /d/Projects/SIR Platform/.sir/CHECKPOINT.md, the brief, then git status / git diff --stat / last commits in /d/Projects/SIR Platform.
- Working tree of /d/Projects/SIR Platform had 4 uncommitted hygiene edits: .gitignore (+.aider*), assets/brand/icon.png, scripts/dev-start.ps1 and scripts/dev-stop.ps1 (BOM removed). No r51 files were pending in that repo at hand-over.
- Read /d/Projects/_SIR/plans/PROJECT_MERGE_RECORD.md, /d/Projects/_SIR/standard/OWNER_DEFAULTS.md, /d/Projects/_SIR/plans/MAIN_PLAN.md, /d/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md, the new per-idea plans and the project /d/Projects/SIR Platform/.sir/CHECKPOINT.md.
- The task had already been worked in this lineage: round 1 (opencode, openrouter/openrouter/free, started 17:17 local) did the research reads; round 2 (flint-40b-free) created the product direction and the per-idea plans, wrote the done marker and set the queue flag. The done marker content was plain text: "superseded by plans/PRODUCT_DIRECTION_2026-11-12.md". The queue entry ops/AUTOPILOT_QUEUE.json has "done": true for r51-backlog-projects.

## What was produced for this task (verified by reading the files)

1. /d/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md (created by the task lineage, commit 70fe17b "hq: product direction 2026-11-12 (Platform cancelled, Education Hub, Business sectors, Hagoozat bookings)"): 7 sections.
   - Section 1: SIR Platform is cancelled as a project. The idea "turn websites into apps" is now what every product does (web, Windows, macOS, Linux, Android, iOS from one codebase and one set of shared standards, plans/SHARED_PLATFORM_KIT.md and standard/OWNER_DEFAULTS.md as internal rules, not a product). Remove the project folder (move to old projects, never delete), its Desktop folder, its TickTick task and every mention as a product.
   - Section 2: SIR Obour Hub becomes SIR Education Hub. A single education platform for the world; anyone can create a Hub (university, institute, school, training centre, teacher group, educational organisation) with members, roles, courses, schedules, materials, quizzes, practice, chats, announcements, billing and settings; people join Hubs they belong to; Obour Institute is the first Hub. Absorbs old ideas: study help, language learning, teaching platform. Platforms: web, mobile, Windows and others, one account everywhere; free trial for a Hub, then subscription; multi-tenant data model, owner-only analytics page. Rename everywhere: SIR Obour Hub to SIR Education Hub.
   - Section 3: SIR Business is one site with business types. Owner signs in, chooses the kind of business (restaurant, pharmacy, library, market and every other sector worth supporting), sets up and configures everything; free trial first, then subscription; one owner can add several businesses; each business has its own team, workers, roles and permissions and a complete management system suited to that sector.
   - Section 4: SIR Hagoozat (bookings) takes the booking family. Football pitch booking and every other booking idea (position coach, other service bookings such as handymen, similar). Decide per idea: module of Hagoozat if it is a booking, separate project if it is a different product.
   - Section 5: Ideas that were not planned (price and game-deal finder, cars, accessibility map, handyman, movies): decide each one, module of an existing product (for example handyman bookings inside Hagoozat) or its own project with the same premium plan, tasks, Desktop folder and TickTick parent task as every other product. Dropped for legal and privacy reasons and staying dropped: citizens program, face rating.
   - Section 6: Standard for every product.
   - Section 7: Final product list (replaces earlier counts): For everyone: SIR AI, SIR Education Hub, SIR Business, SIR Hagoozat, SIR Content Creation Studio, SIR Controller, SIR Laptop Manager, SIR ModPack, SIR Mods for GTA V, SIR Life, plus any independent project created from the unplanned ideas. The owner's personal tools: SIR Jobs, SIR Study. SIR Portfolio is the owner's own website, not a product in the list. Client work: SIR Negm Furniture (plans only). AHome: private. SIR Platform: cancelled.

2. Planning-only plans created by the task lineage (all marked "Created 2026-11-12 (r51-backlog-projects)"), all in /d/Projects/_SIR/plans/:
   - sir-deals.md: idea 15/16 (price and game-deal finder) decided as its own product SIR Deals (not a Hagoozat module: daily use case is shopping, not booking). Critical gate: lawful data sources (Jumia Egypt affiliate API, Amazon.eg affiliate/Product Advertising API, Noon affiliate feed, signed data-sharing agreement, price-aggregator terms). Competitor matrix (Yaoota, Pricespy, Comparison.com.eg, Jumia/Noon). Platform matrix (web PWA first, Android/iOS via Expo M6+, Wear OS/watchOS skipped v1). Free-tier plan (Spark, Workers free, R2 cache, Vercel Hobby). 3-milestone roadmap. Status: concept backlog, planning only. Next step: owner submits affiliate applications; no code before gate passes.
   - sir-cars.md: idea 23 decided as its own product SIR Cars (buy/sell/track cars in Egypt; verified listings, price history, inspection booking, owner tracker). Status: planning only.
   - sir-handyman.md: idea 28 decided as its own product SIR Handyman (home services booking; craftsmen percentage/flat monthly subscription). Status: planning only.
   - sir-movies.md: idea 29 decided as its own product SIR Movies (discovery, tracking, recommendations, where-to-watch; TMDB free API, cinema listings, JustWatch affiliate). Status: planning only.
   - accessibility-map-module-note.md: idea 26 decided as module of SIR Life Part B (community POI map of accessible locations in Egypt; submission flow moderated; PDPL compliance; note in SIR Life plan section 6).

3. SIR Hagoozat plan upgraded in the same lineage: /d/Projects/_SIR/plans/sir-hagoozat.md, /d/Projects/_SIR/ops/briefs/sir-hagoozat-tasks.md, /d/Projects/_SIR/ops/competitors/sir-hagoozat.md (the last two staged in git).

4. Portfolio map and product record updates (same lineage, seen in the working tree of /d/Projects/_SIR and in D:/Projects/AGENTS.md during this round):
   - D:/Projects/AGENTS.md portfolio map changed during this task round: SIR Platform cancelled as a project on 2026-11-12 (standards moved to _SIR/plans/SHARED_PLATFORM_KIT.md); SIR Education Hub listed as renamed from SIR Obour Hub on 2026-11-12.
   - /d/Projects/_SIR/plans/PROJECT_MERGE_RECORD.md had uncommitted working-tree edits at hand-over (9 insertions/9 deletions against HEAD).
   - /d/Projects/_SIR/plans/PORTFOLIO.md, plans/MAIN_PLAN.md, plans/WAVE_STUDY.md, plans/brand.json, plans/competitors/sir-business.md, plans/icon-prompts.json, plans/sir-business.md, plans/sir-controller.md, plans/sir-mods-for-gta-v.md, ops/encyclopedia/deep/ai-readiness.md, ops/reports/contacts-cleanup-report.md, ops/HQ_CHECKPOINT.md, ops/READ_LOG.md, ops/AUTOPILOT_QUEUE.json were in the uncommitted modified set at hand-over.

## Checklist status against the brief items

1. Re-read the owner's own wording of these ideas (TickTick note "أفكار برامج ومشاريع", Notion copy under Ahmed OS if present, legacy folders; never the note Accounts or the habobty column): DONE in the task lineage via ops/TICKTICK_MAP.md, ops/PORTFOLIO.md, ops/OWNER_REQUEST_LEDGER.md, NEXT.md and legacy folder reads.
2. For each idea decide with a short reason: own product or module; create project folder only for the ones that deserve to be separate: DECIDED. Deals=Cars=Handyman=Movies=own products; Accessibility Map=module of SIR Life Part B; Hagoozat=booking family. Project folders themselves were not created yet: the plans mark folder/GitHub as "when created" / "when build starts" because the brief says plans only, no product code.
3. Update plans/PROJECT_MERGE_RECORD.md and the portfolio map in D:/Projects/AGENTS.md with the final product list and counts: DONE for the direction and the map (PRODUCT_DIRECTION section 7 final product list; AGENTS.md portfolio map); PROJECT_MERGE_RECORD.md edits were in the working tree at hand-over.
4. Commit and push (explicit paths), checkpoint, one line to ops/bus/sir-hq.md: PARTIALLY DONE. Product direction was committed (70fe17b in /d/Projects/_SIR). The new per-idea plans, the merge-record edits, the bus line and the final report were still open at hand-over.

## Decisions taken in this task (short reasons)

- Price/game-deal finder -> SIR Deals as its own product (not a Hagoozat module): the daily use case is price comparison before buying, not booking.
- Cars -> SIR Cars as its own product.
- Accessibility map -> module of SIR Life Part B.
- Handyman -> SIR Handyman as its own product (then absorbed into the Hagoozat booking family per direction section 4).
- Movies -> SIR Movies as its own product.
- Ideas 14 and 21: dropped (legal and privacy reasons) and kept dropped.

## Verification performed this round (commands and real outputs)

- Read /d/Projects/_SIR/ops/WORKER_PREAMBLE.md, /d/Projects/SIR Platform/.sir/CHECKPOINT.md, /d/Projects/_SIR/ops/briefs/r51-backlog-projects.prompt.txt, /d/Projects/_SIR/ops/briefs/r51-backlog-projects.md, git status / git diff --stat / git log -5 in /d/Projects/SIR Platform (clean except 4 hygiene files).
- git -C /d/Projects/_SIR status -sb showed ahead/behind state and a long uncommitted set; new untracked r51 plan files: plans/sir-deals.md, plans/sir-cars.md, plans/sir-handyman.md, plans/sir-movies.md, plans/accessibility-map-module-note.md, plus sir-education-hub plan files and bus/competitors variants.
- ops/ci-quota-exhausted.flag exists (created 2026-11-12 17:42) -> GitHub Actions minutes exhausted (flagged 2026-11-12 14:31). Per WORKER_PREAMBLE rule 18 and the verifier CI rule, "CI green" is replaced by full local verification (tests, lint, build); the flag was reported stale earlier but was re-created by another agent at 17:42.

## Report

This file is the task report: everything done and found, with file paths, commands and real output, what is unsure and what is recommended next.

## What is unsure

- Exact final content of the uncommitted edits in /d/Projects/_SIR (merge record, queue, plans) because several parallel agents touched the same shared repo; the r51-specific edits were identified by file names.
- Whether the plain-text done marker should be re-written through the official script (python /d/Projects/_SIR/scripts/agy-done.py r51-backlog-projects ok "<one line>") as part of this closing round.

## Recommended next

- Add the one bus line for r51, update the checkpoint, commit the remaining r51 paths and push, write this report, run the done command, then re-run local verification for the touched workspace.
