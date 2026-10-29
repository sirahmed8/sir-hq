# HQ CHECKPOINT — updated 2026-10-29 15:09
## Phase and step
Phase 0 finished. Next: Phase 1 (`phases/01-workstation.md`), step 1.1. (Read the file first; it is about 19 KB, so read it in parts.)
## Now
Phase 0 deliverables are in `_SIR/ops/`: HQ_CHECKPOINT, MISSION_LOG, TOOLS, DISK, PORTFOLIO, OWNER_ACTIONS, IDEAS_INBOX, inventory/SECRETS.md. Memory hooks installed and script-tested. Safety net: `pre-sir-snapshot` branch + tag `pre-sir-2026-10-29` in 18 repos; zips + bundle in `D:\Backups\SIR-2026-10-29\`. Leak #1 (public SIR ModPack) fixed and verified. `_SIR` is being turned into the private repo `sirahmed8/sir-hq` (first push is the last Phase 0 act).
## Next step
1. If `git -C D:/Projects/_SIR log` shows no commit or `gh repo view sirahmed8/sir-hq` fails: `git init -b main`, commit, `gh repo create sirahmed8/sir-hq --private --source . --push` (`.gitignore` already written).
2. Read `phases/01-workstation.md` and start 1.1. Disk first: C: 14 GB and D: 16 GB free. Free the safe regenerables from `ops/DISK.md` (npm-cache 5.6 GB via `npm cache clean --force`, Temp) before any heavy install.
3. Install missing tools in Phase 1 only (pnpm, eas-cli, wrangler, Android SDK); set `OLLAMA_MODELS=D:\Projects\AI_Models_Hub\ollama`.
## Running in the background
- none
## Decisions since the last milestone
- Disk is tight (C: 14 GB, D: 16 GB free): full zips of repos skipped (GitHub + snapshot branches cover them); models not backed up (re-pullable); node_modules (12.6 GB) is the first safe win but untouched until Phase 2.4/Phase 1 needs space.
- Backups sit on D: only; Google Drive copy needs Ahmed (OWNER_ACTIONS).
- standard/ is committed into sir-hq for now (backup beats purity); split into its own repo when Phase 1/3 installs it. platform/ is ignored.
- Obour Institute scripts named `ba_quiz_live_solver.py`, `academic_submission_engine.py`, `check_ba_quiz.py`: do not run or extend (rule 14); study-coach reviews in Phase 8.6.
- Never print any substring of a credential line: only variable name and length.
## Open promises
- Confirm the hooks fire after the first real compaction: check `ops/memory.log` for a "compaction" line and that the reload block appeared.
- Leaks #2 (Gemini key, private GTA V repo), #3 (ADMIN_SECRET_KEY), #4 (Telegram bot token, history of AHome): Ahmed rotates (OWNER_ACTIONS); then the agent cleans history (Tier 1) on a backup branch. #3 the agent can regenerate itself once the deploy target is known.
- Check the 114 MB ModPack release asset `SIR_Apps_Suite.zip` for account files (Phase 5).
- Phase 5 security notes: restrict Firebase web keys; SIR Restaurant ZATCA pseudo-key is fake crypto (rule 16); SIR Market hard-coded super-admin licence keys.
- Run `claude doctor` in Phase 1.
## Owner actions listed (never blocking)
- 5 open: revoke AHome Telegram token; rotate Gemini key; Google Drive for Desktop sign-in; optional Vercel login; optional GitHub Support purge for the old ModPack commit
## Usage
Not read (`/usage` is a UI command; check at the start of Phase 1 and write the reading here).
## Re-read after a reset
- START_HERE.md · phases/01-workstation.md · ops/DISK.md · ops/OWNER_ACTIONS.md
