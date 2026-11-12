# Report: r61-plan-sir-mods-gta-v (planning-only refresh, rule 20/22)

Date: 2026-11-12. Worker: devin. Scope honoured: wrote ONLY under `D:/Projects/_SIR` (plans/, ops/competitors/, ops/briefs/, ops/bus/). No code, no edits inside `D:/Projects/SIR Mods for GTA V`, no repos, no Firebase projects created.

## What was done

1. Read the required inputs: `ops/WORKER_PREAMBLE.md`, `.sir/CHECKPOINT.md`, the brief `ops/briefs/r61-plan-sir-mods-gta-v.prompt.txt`, `git status`/`git diff --stat`/`git log`, `plans/PRODUCT_DIRECTION_2026-11-12.md`, `plans/sir-mods-for-gta-v.md`, `plans/sir-mods-for-gta-v-DEEP.md`, `ops/briefs/sir-mods-gta-v-tasks.md`, `ops/competitors/sir-mods-for-gta-v.md`, the product folder read-only (`AGENTS.md`, `.sir/CHECKPOINT.md`, `legacy/README.md`), `ops/TICKTICK_MAP.md` row, `ops/bus/team.md` tail, `ops/SKILLS_INDEX.md`.
2. Uncommitted state found at start: `ops/READ_LOG.md` (auto log line), `ops/briefs/sir-access-map-tasks.md` (another worker's parallel task - left untouched, not committed by me), and an untracked report for a sibling task. Nothing of mine was broken; nothing needed repair.
3. Web research (second pass) - findings written to `ops/competitors/sir-mods-for-gta-v.md` new section 5:
   - GTA V now has TWO PC editions: Legacy (Gen8, `GTA5.exe`) and Enhanced (Gen9, `GTA5_Enhanced.exe`, released 2025-03-25, builds 1.0.811/812). ScriptHookV supports Enhanced since 2025-03-23 (`dev-c.com/post/scripthookv-enhanced`); most Legacy `.asi` scripts are broken on Enhanced (SHVDN issue #1558); SHVDNE community fork supports both. Loaders differ: `OpenIV.asi` (Legacy) vs `OpenRPF.asi` (Enhanced); Gen8 assets crash Gen9, CodeWalker converts.
   - Rockstar official single-player mod support page updated 2026-09-15 (`support.rockstargames.com/articles/5NVOAYjcTomO8v6SX2k76k/pc-single-player-mods`) linking ToS, Creator Platform License Agreement and Mod Guidelines. Secondary coverage (allthings.how): monetized mods only via Rockstar-approved storefronts (reported Cfx Marketplace). The plan's old "49 EGP curated pack" is now HIGH RISK -> recommended: mods free forever, sell services/supporter perks only.
   - Installer space crowded: ModDrop V (Legacy+Enhanced, 13 languages, profiles, load order, check-and-repair), ModsHub (Electron, FiveM sync), LSPDFRManager (MIT, .NET 8 WPF+React), Nexus ModMaster Fluent (.oiv/.oivs/.nexus), OIV Package Installer (CodeWalker core, .oivs wizard, dlc.rpf/dlclist.xml). "One-click installer" alone is no longer a differentiator; surviving edges: AI NPC mod (unique), licence-gated pack, Egyptian Arabic guide, free forever, policy-safe, owner analytics.
   - Also noted: GTA 6 launched Nov 2026 (market risk, out of v1 scope).
4. Plan updated: `plans/sir-mods-for-gta-v.md` gained section 23 "Refresh delta (2026-11-12, round r61)": edition reality + detection decision, monetisation correction, competitive reality, full Firestore data model (10 collections with fields), API list (10 endpoints), AI features (4), security/privacy additions (signed manifests, telemetry minimisation, 24h NPC text retention), launch/marketing additions, risks R1-R6 each with recommended answer, open questions Q1-Q5 each with recommended answer.
5. Tasks file rewritten: `ops/briefs/sir-mods-gta-v-tasks.md` expanded from 10 to 45 tasks (T1-T45) grouped by milestone (M0-M1 gate/scaffold/core, M2 installer depth+safety+NPC AI, M3-M4 portal/quality/owner tools, M5-M6 polish/launch/release). Every task has an acceptance test and skill names from `ops/SKILLS_INDEX.md`. Includes dependency map and "deliberately not in this queue" list. First 10 remain the queue-ready slice.
6. `plans/sir-mods-for-gta-v-REFRESH-LOG.md` created documenting the rescan, research, plan changes, decisions, and owner-open items.
7. Bus updated: START + DONE lines in `ops/bus/team.md`, one summary line in `ops/bus/sir-hq.md`.

## Commits and push

- `b305a0f` "r61: expand SIR Mods for GTA V planning - 45 tasks, edition+legal research, REFRESH-LOG" - pushed to `main` (`385d762..b305a0f`).
- Note: a parallel HQ sweep commit `4a181dd` (20:00:12) had already swept my in-progress edits to `plans/sir-mods-for-gta-v.md` and `ops/competitors/sir-mods-for-gta-v.md` into its commit; verified `git show HEAD:` contains all my content (section 23 including Q5, competitor section 5) and `git diff HEAD` is clean for those files. `b305a0f` carried the tasks file, REFRESH-LOG and bus lines. Final state: `git status -sb` = `main...origin/main` in sync; `git log origin/main` top = `b305a0f` (plus a sibling worker's `c7f59e4` price-finder commit already on remote).
- Left uncommitted (not mine): `ops/AUTOPILOT_QUEUE.json`, `ops/READ_LOG.md`, `ops/artifact/*`, `ops/dashboard.html`, `ops/public/dashboard.html` - runtime/dashboard outputs and the other worker's `sir-access-map-tasks.md` edit (the latter was committed by its own worker's sweep, no longer in status).

## Verification

- Changes are documentation/markdown only; no code, no build, no tests applicable. `ops/ci-quota-exhausted.flag` EXISTS, so per WORKER_PREAMBLE rule 18 the CI-green requirement is replaced by local verification - there is nothing executable to verify; markdown files were checked by re-reading committed content (`git show HEAD:` greps confirmed section 23.10/Q5 and competitor section 5 present).
- `git push origin main` succeeded; `git status -sb` shows `main...origin/main` with no ahead/behind.

## What is unsure / open

- Whether Rockstar's September 2026 Mod Guidelines PDF is fetchable verbatim (task T10 owns it).
- Whether Cfx Marketplace accepts non-FiveM single-player mods (unsourced, verify) - decides if any paid-mod path exists.
- Exact ScriptHookV/loader redistribution licences - unresolved until T10's CSV work.
- Domain choice `.com` vs `.app` - owner picks at purchase (Q3).

## Recommended next

Queue T1-T3 first (parity matrix, scaffold, Firebase/auth) when the owner lifts the planning-only order; T10 (licence CSV + publisher policy) can run in parallel since it is read-only research plus docs.
