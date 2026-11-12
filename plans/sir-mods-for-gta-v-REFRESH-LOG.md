# PLAN REFRESH LOG: SIR Mods for GTA V

Rule 20 rescan, round r61, 2026-11-12. Planning only - no code, no folder changes inside `D:/Projects/SIR Mods for GTA V`, no repos created (owner order: free tools must NOT start building these projects).

## What was re-read

- `D:/Projects/AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `ops/bus/team.md` (last 40 lines), `ops/bus/sir-mods-for-gta-v.md` inbox
- `plans/PRODUCT_DIRECTION_2026-11-12.md` (product is in the final list, section 7)
- `plans/sir-mods-for-gta-v.md` and `plans/sir-mods-for-gta-v-DEEP.md` (full)
- `ops/briefs/sir-mods-gta-v-tasks.md` (was 10 tasks)
- `ops/competitors/sir-mods-for-gta-v.md` (was one research pass)
- `D:/Projects/SIR Mods for GTA V/` read-only: `AGENTS.md`, `.sir/CHECKPOINT.md`, `.sir/PLAN.md` header, `legacy/README.md`
- `ops/TICKTICK_MAP.md` row (secrets rotation line mentions GTA V)
- `ops/SKILLS_INDEX.md` for per-task skill names

## Research added (second pass, 2026-11-12 evening)

Written into `ops/competitors/sir-mods-for-gta-v.md` section 5:

1. GTA V has two PC editions now: Legacy (Gen8) and Enhanced (Gen9, released 2025-03-25). ScriptHookV supports Enhanced since 2025-03-23 but most Legacy `.asi` scripts are broken on it; loaders differ (`OpenIV.asi` vs `OpenRPF.asi`); assets are not interchangeable (CodeWalker converts). The installer must detect the edition - this is new task T11 and a catalogue `editions` field.
2. Rockstar's official single-player mod support page was updated 2026-09-15 and links the Rockstar Games Mod Guidelines. Secondary coverage says monetized mods are only allowed via Rockstar-approved storefronts (reported as Cfx Marketplace). The old "49 EGP curated pack" idea is now HIGH RISK; recommended answer: mods stay free forever, sell services/supporter perks only (plan section 23.2, open question Q1).
3. The one-click installer space crowded fast: ModDrop V, ModsHub, LSPDFRManager (MIT, open source), Nexus ModMaster Fluent, OIV Package Installer. Feature bar updated: profiles, load order/conflict resolution, check-and-repair, `.oivs`-style options, dlc.rpf registration. Surviving edges: AI NPC mod (unique), licence-gated pack, Egyptian Arabic guide, free forever, policy-safe design, owner analytics.

## Plan changes

- `plans/sir-mods-for-gta-v.md`: new section 23 "Refresh delta (2026-11-12, round r61)" with edition reality, monetisation correction, competitive reality, full Firestore data model (10 collections), API list (10 endpoints), AI features (4), security/privacy additions, launch/marketing additions, risks R1-R6 with recommended answers, open questions Q1-Q5 with recommended answers.
- `ops/competitors/sir-mods-for-gta-v.md`: new section 5 with the findings above plus sourcing tasks 11-13.
- `ops/briefs/sir-mods-gta-v-tasks.md`: rewritten from 10 tasks to 45 tasks (T1-T45) grouped M0-M1 / M2 / M3-M4 / M5-M6, each with acceptance test and skills from `ops/SKILLS_INDEX.md`, plus a dependency map and a "deliberately not in this queue" list. First 10 remain the queue-ready slice (T1-T10 cover the M0 gate, scaffold, auth, data model, installer core, UI kit, catalog, NPC skeleton, owner page, licence CSV/policy).

## Decisions taken (per preamble rule 7, no owner needed)

- Edition support: detect and gate per mod; ship Legacy-first, Enhanced-safe mods progressively (R2/Q2).
- Monetisation: services only, never mod files, until a Rockstar-approved storefront path is confirmed and lawyer-reviewed (Q1).
- Domain: plan default `.com`; owner picks at purchase (Q3).
- Loader binaries (ScriptHookV, dinput8, OpenIV.asi/OpenRPF.asi): require + verify + link to author unless the CSV proves redistribution is allowed (Q4).

## Still open for the owner

- Buy domain + code-signing cert only after the M0 gate stays green (T37 writes the steps).
- Rotate the secrets that were committed in legacy `.env` files (T38 produces the names-only list; rotation itself is an owner action).
- Lawyer review before any paid surface goes live.
