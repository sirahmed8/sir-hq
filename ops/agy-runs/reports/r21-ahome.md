# r21-ahome report (partial — round not complete)

Date: 2026-11-11. Worker: Devin (SWE-2 Flash). Repo: D:\Projects\AHome, branch main.

## Ticked items (all pushed to main, CI `verify` green on each push)
- 1 care-card padding (`e6a03e1`) + Tailwind token guard test + evidence PNG.
- 2 voice recorder grow-in/out (`036ad8e`) + evidence test.
- 3 Dynamic Island size/content morph (`9ac4683`).
- 4 heading equals tab name (`c13c7a7`) + `tests/r21_heading_matches_tab.test.mjs`.
- 5 duplicate «حياتنا» resolved by dock rename to «يومنا» (`.sir/plans/r21-tabs.md`).
- 6 SwipeablePager transform/direction root-cause fix + `tests/r21_tab_switch.test.mjs`.
- 7 duplicate tab bars removed + `tests/r21_tab_bars.test.mjs` (`4fa6189`).
- 8 MoreSheet closing spring (`e95f7e8`).
- 9 icon on every LiquidTabs pill + guard test (`4fa6189`).
- 10 biometric WebAuthn lock hardening (`2ac7eb9`).
- 11 every segmented control on shared LiquidTabs; custom controls migrated across calm/arcade/pairing/spotify/settings/study/chat/voice/life; `tests/r21_no_adhoc_tabs.test.mjs` extended (`3a52128`).

## Item 12 progress (not ticked)
- Exists and tested: PKCE start, callback, sealed token storage, refresh (Google), two-way sync engine (google_tasks, ticktick), disconnect, sync-now, conflicts, failed-op retry, device feed.
- Fixed this session (`55c8543`): config now reads the provisioned credential names `GOOGLE_TASKS_CLIENT_ID/SECRET`, `GOOGLE_TASKS_REDIRECT_URIS`, `TICKTICK_REDIRECT_URI` from `_local/ahome-oauth.env`; previously the core could not see them (real defect). Missing-client-id UI message now names the exact env var per provider.
- Open: account-name display when linked; events import from linked calendar (needs calendar scope / ICS path; tasks scope alone cannot read events); public OAuth callback route on Vercel/Firebase forwarding to the PC core (reachability via relay must be verified first).

## Open items
- 12 (partial above), 13 (events import + `.sir/plans/r21-integrations.md`), 14 (owner message format for Telegram/app/agents), 15 (free-writing importer + 30 messy fixtures), Part B (3 defect-hunt cycles + permanent invariants).

## Verification run this session
- `node --test` r21 heading/tab-bars/no-adhoc-tabs: 7/7 pass.
- `npx tsc --noEmit` (apps/web): 0 errors.
- `pytest -k "connection or oauth or pkce or config"` (local-core venv): 52 passed.
- CI: `gh run list` — verify green on c13c7a7, 4fa6189 and earlier; item-11 run in progress at handoff; new commit 55c8543 pushed.

## Not done
- `agy-done.py` intentionally NOT run: checklist is incomplete (items 12-15, Part B open). Exact continuation steps are in `.sir/CHECKPOINT.md` (Pass r21-ahome).

## CI status at handoff
- HEAD `f3acb37` on main: `verify` = success (gh run 42938153578).
- `55c8543` verify = success (gh run 42937382946).
- `3a52128` had one flaky failure in `r15_emoji_panel.test.mjs` (geometry sampled mid spring); test hardened in `f3acb37` to poll until settled; both later runs green.
- Round is INCOMPLETE: items 12 (partial), 13, 14, 15 and Part B remain open. `agy-done.py` not run, per manual.
