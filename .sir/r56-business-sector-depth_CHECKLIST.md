# r56-business-sector-depth checklist

Round r56 (HQ, 2026-11-12). Output under `D:/Projects/_SIR` only (`plans/`, `ops/briefs/`, `ops/bus/`). Never open `D:/Projects/AHome`.

Owner order (plans/PRODUCT_DIRECTION_2026-11-12.md section 8): SIR Business is the biggest project, 25 sectors or more, and EACH sector gets its own specialised software and site: own data model, screens, workflows, reports, onboarding, templates, terminology, sector integrations and its own landing page, all on the shared Business engine. Not one generic app with a different label.

Brief: `ops/briefs/r56-business-sector-depth.prompt.txt`. Sources read: `AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `standard/OWNER_DEFAULTS.md`, `plans/PRODUCT_DIRECTION_2026-11-12.md` (sections 3 and 8), `plans/sir-business.md`, `plans/sir-business-DEEP.md`, `ops/inventory/SIR-Restaurant.md`, `ops/inventory/SIR-Business-Library-Market-Pharmacy.md`, `ops/competitors/sir-business.md`.

## Items

- [x] 1. Read the manual, the checkpoint, the brief, the sources; `git status`, `git diff --stat`, last commits; take the `_SIR` lock (the old one from 2026-11-10 is stale).
- [ ] 2. Decide the final sector list with reasons (owner named 32 candidates plus "others worth supporting"; r53 catalogue had 30). Final list written with the reason each sector is in or out, and what was merged or split.
- [ ] 3. Write `plans/business-sectors/_ENGINE.md`: the shared engine (accounts, one owner with several businesses, teams, roles, billing and trial, inventory, finance, customers, analytics, privacy of businesses and employees) and how a sector template plugs into it (module registry, sector packs, feature flags).
- [ ] 4. Build the data and the generator: `plans/business-sectors/_data/<sector>.json` (one file per sector, specific content) plus `scripts/build_business_sectors.py` (renderer, under 300 lines, re-runnable, no fake data).
- [ ] 5. Generate one plan per sector at `plans/business-sectors/<sector>.md` with all eleven required parts: operator and daily pain, data model (entities, fields, units, batches, expiry, tables, appointments, prescriptions), screens and workflows, roles and permissions, reports and KPIs, integrations, onboarding wizard and ready template data, landing page outline (Arabic and English), pricing tier notes, competitors (3 to 5), first 10 tasks, risks and what we refuse to fake.
- [ ] 6. Generate the first 10 tasks per sector at `ops/briefs/business-<sector>-tasks.md` (Brief, Files, Done when, Check for each).
- [ ] 7. Update `plans/sir-business.md` to link the whole catalogue (engine, index, every sector file, every tasks file) and reconcile the 30 sectors of section 4 with the final list.
- [ ] 8. Local verification (rule 18 applies, the Actions quota flag is present): `python -m compileall plans scripts`, the generator run twice with a byte-identical result, a check that every sector has all eleven parts and ten tasks, a check that no file contains an em-dash or an emoji, a check that every link resolves, `python plans/generate_dashboard.py` still passes.
- [ ] 9. Commit and push each group to `main` on `sirahmed8/sir-hq`, update `.sir/CHECKPOINT.md` after every commit.
- [ ] 10. One line to `ops/bus/sir-hq.md`, the full report at `ops/agy-runs/reports/r56-business-sector-depth.md`, then `python D:/Projects/_SIR/scripts/agy-done.py r56-business-sector-depth ok "<one line>"`.

## Open (honest, not ticked)

- CI on `main`: GitHub Actions minutes are used up (`ops/ci-quota-exhausted.flag` present, expected reset around 2026-12-01). Rule 18 replaces "CI green" with the full local verification above. The last seen run on main before this round was green.
- Sector competitor names that are not in `ops/competitors/sir-business.md` are marked "(unsourced, verify)" in the sector files and listed as open research tasks in `_INDEX.md`. No competitor price was read for them.
- No product code was written: this round is plans only. The product folder `D:/Projects/SIR Business` was not touched.
