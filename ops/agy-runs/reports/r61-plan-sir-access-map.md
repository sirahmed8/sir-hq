# Report: r61-plan-sir-access-map (round r61, devin, 2026-11-12)

Planning-only refresh of SIR Access Map per rule 20 (rescan) and rule 22 (no building; free tools must not start these projects). Nothing was written inside `D:/Projects/SIR Access Map`; it was read in read-only mode only.

## What I read

- `D:/Projects/AGENTS.md`, `_SIR/ops/WORKER_PREAMBLE.md`, `_SIR/standard/23-premium-code-bar.md` (via rules), `plans/PRODUCT_DIRECTION_2026-11-12.md`, `plans/sir-access-map.md` (full, 457 lines), `ops/competitors/sir-access-map.md`, `ops/briefs/sir-access-map-tasks.md` (had 10 tasks), `ops/TICKTICK_MAP.md` row 29, `ops/SKILLS_INDEX.md` (skill names for tagging), `ops/bus/team.md`, `ops/bus/telegram-outbox.md` (no owner message needed, none sent).
- Project folder read-only: `D:/Projects/SIR Access Map/AGENTS.md`, `.sir/CHECKPOINT.md` (M0 next step: create repo `sirahmed8/sir-access-map` + Desktop kit), `.sir/PLAN_REFRESH.md`, `README.md`, `scripts/dev-*.ps1/.vbs`, `folder.ico`, `.gitignore`. The folder exists with skeleton only; no code, no repo remote yet.

## Web research run this round (2026-11-12)

- Competitor sweep found five products not in the study: **Braillito Maps** (Spanish iPhone app, VoiceOver-first, 10-question checklist per place, score shown as number plus colour band never colour alone), **DisabledEnabled** (offline-first map, claims 170k+ places, 25 categories, 4 needs filters including cognitive, no account/ads/analytics), **Kimap** (App Store claims "patented" motor-disabled navigation and an AI assistant; unverified, treated as watch-only), **Ahoi** (Boston, founded 2022, venture-backed accessibility reviews), **RailsMaps** (Egypt train-station accessibility map built from OSM data; proves Egyptian transport demand, no community proof layer).
- Academic reference: Zenodo record "Mapping Mobility Barriers: A Comparative Evaluation of Five Accessibility Platforms" (SKI Canada 2026) comparing OSM, Project Sidewalk, Wheelmap, AXS Map, AccessNow.
- Map/routing API pricing from official pages: Google Maps Platform Essentials = 10,000 free Dynamic Maps loads + 100,000 free Map Tiles API 2D tiles per month, pay-as-you-go after, billing account required; Maps SDK mobile listed unlimited free. Mapbox = 50,000 free GL JS loads/month + 200k vector tiles. Geoapify = 3,000 credits/day free, commercial use allowed with attribution, routing included. MapTiler and Stadia free tiers = non-commercial only (rejected). Public OSM tile server = no SLA, dev/offline only.
- Egyptian legal baseline: Law No. 10 of 2018 Articles 39-46 (accessibility of built environment, transport, ICT); Egyptian Building Code for persons with disabilities (under Building Law 119/2008) with measurable thresholds: corridors/doorways >= 1.2 m, ramp slope <= ~5%, entrance curb <= 15 cm, designated accessible parking with markings.
- WheeLog figures re-read: 69,118 spots, 16,111 km logged, 200,000+ users claimed (their claim, July 2026 update).

## Files changed

1. `ops/competitors/sir-access-map.md` — WheeLog row updated with re-read numbers; new "Addendum 2026-11-12 (r61 plan refresh)" section: 5 new competitors, map API pricing facts, Egyptian legal baseline, academic reference.
2. `plans/sir-access-map.md` — publish rules now require every FeatureKey to trace to a written source (Egyptian Building Code thresholds, Law 10/2018) or be marked "(unsourced, verify)"; section 5.6 records the provider comparison and recommendation (Geoapify free recommended, Mapbox fallback, Google Maps Platform needs owner billing account, MapTiler/Stadia rejected, public OSM tiles dev-only); section 9 points to the 48-task list; new section 12 "Plan refresh r61" with what changed, 8 open questions each with a recommended answer, and 3 new risks.
3. `ops/briefs/sir-access-map-tasks.md` — rewritten: 48 tasks grouped M0-M6, each a one-paragraph brief with acceptance test (exit check) and named skills from `ops/SKILLS_INDEX.md`. First 10 remain ready to hand to agents; tasks 11-48 cover map provider decision, i18n/RTL, UI kit, offline PWA, evidence engine, moderation, claims, owner analytics, pricing/billing fallback, legal pack, route engine, notifications, Expo app, Electron, AI features, SEO/launch.
4. `plans/sir-access-map-REFRESH-LOG.md` — new file logging the rescan, research, changes and next rescan point.
5. `ops/bus/team.md` — START and DONE lines appended.
6. `ops/bus/sir-hq.md` — one-line note for HQ.

## Decisions taken (rule 7, logged)

- Recommended Geoapify free tier as v1 map provider with Mapbox fallback; the binding licence/cost decision stays in M0 task 4 writing `docs/DATA_SOURCES.md`.
- Build stays last per `PRODUCT_DIRECTION_2026-11-12.md` section 8; no build work done.

## Commands run and real output

- `git status --short`, `git log -5`, `git diff --stat` at start (parallel workers' uncommitted edits present; left untouched).
- `wc -l`/`ls`/`grep` reads of plan, brief, competitor, checkpoint files.
- `web_search` x4 (competitors, Egypt law, map API pricing, Google Maps Platform pricing) — all returned results quoted above.
- `git add <explicit paths>` then `git commit -m "r61: SIR Access Map planning refresh - 48 tasks, competitor+plan updates, REFRESH-LOG"` → `[main 76d1bbd]`, `git push origin main` → `90e7810..76d1bbd main -> main`.

## Notable event

A parallel worker's commit `23dd086` ("r61: add sir-content-creation-studio entry to HQ inbox", 19:55:47) swept my in-progress edits to `plans/sir-access-map.md` into its commit; commit `90e7810` (SIR Business refresh) likewise carried `ops/competitors/sir-access-map.md`. Verified via `git show HEAD:<file>` that both files' current content on main is exactly what I wrote — nothing lost, content correct, just attributed to earlier commits. My commit `76d1bbd` carries the tasks file (48 tasks), REFRESH-LOG, and bus lines.

## Verification

- Planning-only round: no code, no build, no tests applicable. `ops/ci-quota-exhausted.flag` exists so CI-green rule is replaced by local verification; there was nothing to run locally beyond file writes and git.
- `git status` after push shows only unrelated files modified by other workers (`ops/READ_LOG.md`, an untracked report from another task). My paths are clean and pushed.

## Still open / recommended next

- The competitor file's 7 original sourcing tasks remain open (each under 1 hour); none blocks planning. They belong to the M0 research batch.
- Next step for this project when its turn comes: M0 task 1 (create private repo `sirahmed8/sir-access-map`, push main, build Desktop kit), then task 2 (Firebase project + owner-auth).
- No owner action needed this round.
