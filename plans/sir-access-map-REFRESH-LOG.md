# SIR Access Map plan refresh log

## 2026-11-12 (round r61, devin, planning only per rule 22)

Rescan performed before touching the plan. Read:

- `D:/Projects/AGENTS.md` (workspace laws)
- `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md` (worker manual, rules 20 and 22)
- `D:/Projects/_SIR/standard/23-premium-code-bar.md` (premium bar)
- `D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md` (direction, sections 5, 6, 8)
- `D:/Projects/_SIR/plans/sir-access-map.md` (full plan, 457 lines)
- `D:/Projects/_SIR/ops/competitors/sir-access-map.md` (competitor study)
- `D:/Projects/_SIR/ops/briefs/sir-access-map-tasks.md` (had 10 tasks)
- `D:/Projects/_SIR/ops/TICKTICK_MAP.md` (TickTick row 29)
- `D:/Projects/_SIR/ops/SKILLS_INDEX.md` (skill names for task tagging)
- `D:/Projects/SIR Access Map/` read-only: `AGENTS.md`, `.sir/CHECKPOINT.md`, `.sir/PLAN_REFRESH.md`, `README.md`, `scripts/`, `folder.ico`, `.gitignore`
- `ops/bus/team.md`, `ops/bus/telegram-outbox.md` (no owner message needed)

Fresh web research run this round (searches on 2026-11-12):

- Accessibility-map competitor sweep: found Braillito Maps (Spanish, VoiceOver-first, 10-question checklist, score as number plus colour), DisabledEnabled (offline-first, 170k+ places claimed, 4 needs filters incl. cognitive), Kimap (unverified "patented" claims, watch only), Ahoi (Boston, venture-backed), RailsMaps Egypt train-station accessibility map (OSM-derived, proves Egyptian transport demand).
- Academic: Zenodo SKI Canada 2026 paper comparing OSM, Project Sidewalk, Wheelmap, AXS Map, AccessNow on tags, ratings, appearance, openness.
- Map/routing APIs official pricing: Google Maps Platform Essentials 10k free Dynamic Maps loads + 100k free Map Tiles API tiles monthly (billing account needed); Mapbox 50k free GL JS loads/month; Geoapify 3,000 credits/day free with commercial use allowed; MapTiler and Stadia free tiers non-commercial (rejected); public OSM tiles no SLA.
- Egyptian law: Law 10 of 2018 Articles 39-46 (built environment, transport, ICT accessibility) and the Egyptian Building Code for persons with disabilities with measurable thresholds (1.2 m corridors, ~5% ramp slope, 15 cm curb, designated parking).
- WheeLog updated figures re-read: 69,118 spots, 16,111 km, 200k+ users claimed (July 2026).

Changes written:

1. `ops/competitors/sir-access-map.md`: WheeLog row updated with re-read numbers; new addendum section with the five new competitors, the map API pricing facts and the Egyptian legal baseline.
2. `plans/sir-access-map.md`: publish rules now require every FeatureKey to trace to a source (Egyptian Building Code thresholds, Law 10/2018) or be marked "(unsourced, verify)"; section 5.6 records the provider decision (Geoapify recommended, Mapbox fallback, Google needs owner billing, MapTiler/Stadia rejected, public OSM tiles dev-only); section 9 now points at the 48-task list; new section 12 records this refresh, eight open questions each with a recommended answer, and three new risks.
3. `ops/briefs/sir-access-map-tasks.md`: expanded from 10 to 48 tasks grouped by milestone M0-M6, each with an acceptance test (exit check) and the matching skills from `ops/SKILLS_INDEX.md`. First 10 remain ready to hand to agents.

Decision taken without asking (rule 7): recommended Geoapify free tier as the v1 map provider with Mapbox fallback, recorded in plan 5.6 and task 4; the real licence/cost decision still happens in M0 with `docs/DATA_SOURCES.md` as the artefact.

Still open: the competitor file's seven original sourcing tasks remain open (each under one hour); none blocks planning. Build remains last per PRODUCT_DIRECTION section 8; this round wrote planning files only, nothing inside `D:/Projects/SIR Access Map` except reading it.

Next rescan: at M0 start (repo, Firebase project and scaffold do not exist yet; CHECKPOINT next step is M0 task 1: create repo `sirahmed8/sir-access-map` and the Desktop kit).
