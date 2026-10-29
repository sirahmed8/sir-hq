# NEXT (read this, nothing else, to know where we are) - updated 2026-10-29 23:50
Everything below is done by the agents; only the last section needs Ahmed.

## Done today
- AHome renamed (old name gone), 5.9 GB freed, 3 routines registered in Task Scheduler (morning, nightly, weekly: Ready).
- All 16 projects inventoried and scored (`ops/inventory/`, `ops/PORTFOLIO.md`), TickTick read and backed up.
- Five security fixes written, tested and pushed as PRs. Four ready to merge (script ready; the Optimizer's review fixes are done, 35/35 tests); SIR AI's blocking fix is still being written.
- Moodle automation: 75 files moved to `D:\Quarantine\2026-10-29\moodle-automation` (nothing deleted, manifest inside), scheduled task `Obour_HCI_Quiz_Sentinel` disabled.
- `Merged sites` renamed to `Hagoozat Elite`; `11Players` and `EGFootball5` moved to `old projects` (backups tested). Their live sites stay online.
- New folders with prompts: `SIR Platform`, `SIR Business`, `SIR Life`.

## Next, in this order (agents run all of it)
1. Finish the two PR fixes (sir-optimizer, SIR-AI), re-run tests, push. Then merge all five (script `scripts/merge-approved-prs.ps1` for the first three).
2. Rotate the leaked keys in the browser (Google AI Studio, OpenRouter): create new, put them only in local untracked env files, delete the old. Needs Ahmed's logged-in Chrome.
3. Fix GitHub Actions failures: SIR-Controller `build`, sir-content-creation-studio `CI`, odysseus `CI` and `Container scan`, antigravity-agent-suite `CI` (oldest run). The other repos have no workflows: add the standard CI (typecheck, lint, test, build, gitleaks).
4. SIR Platform: extract owner-auth, signed-webhook, ai-proxy from the reviewed code; Obour Academic Hub is the first consumer (remove its solve modes, tighten Firestore reads).
5. Port Hagoozat Elite features from `old projects\11Players` and `EGFootball5` (list in `ops/inventory/Merged-sites.md`).
6. SIR Business core, Restaurant first.
7. Smaller merges: Optimizer into Controller, agent suite into Laptop manager.
8. Not yet done at all: the benchmark against the best apps (Phase 3.6), the parity test of the SIR setup in Antigravity/OpenCode/Kilo, testing the agent-config sync script on a temp workspace.

## Only Ahmed can do (the classifier or his accounts)
- Run `pwsh -NoProfile -File D:\Projects\_SIR\scripts\merge-approved-prs.ps1` (4 merges: merged-sites, SIR-Controller, sir-mods-for-gta-v, sir-optimizer).
- Move the passwords out of the TickTick notes into a password manager; change the Moodle password.
- Log in to Chrome sessions for Google AI Studio and OpenRouter if asked.
