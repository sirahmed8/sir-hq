# Phase 2 — AHome fixes Ahmed asked for

> **Read first:** `START_HERE.md`, then `core/02-rules.md` (tiers: quarantine, never delete personal files). **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with `phases/03-inventory-and-merge.md`.

**2.1 Recover `.remember` in `D:\Projects\AHome`.** First identify what created it (which tool, plugin or agent uses a `.remember` folder). Then try, in order: the Recycle Bin; `D:\Projects\AhmedAndHabiba\.remember` (the old folder may still have a copy); git history (`git log --all --stat -- .remember`); Windows File History / Previous Versions / OneDrive. Restore it, or report that it's unrecoverable and whether its tool can rebuild it. If it holds private data, make sure it's gitignored and backed up.

**2.2 Retire `D:\Projects\AhmedAndHabiba`.** Ahmed has asked for this; AHome replaces it.

1. Diff it fully against `D:\Projects\AHome`: files, git remotes, branches and stashes, `.env` files, databases, assets, uncommitted changes.
2. Migrate anything unique into AHome and commit it.
3. Update everything that points to the old path: shortcuts, scripts, scheduled tasks, Claude/Antigravity settings, Remote Control.
4. Zip the old folder into `D:\Backups\` and send it to the Recycle Bin (not a permanent delete).
5. Report what was migrated. If you found unique content, migrate it first, then proceed.

**2.3 AHome folder icon.** Make the AHome folder show AHome's app icon (procedure in Standard module 15).

**2.4 PC cleanup, owned by Laptop Manager** (`pc-janitor`).

- Everything PC-related (cleanup, disk, health, startup apps, PC automations) belongs to `D:\Projects\Laptop Manager`. Clean and organize that project first. It may already have an `automations` folder; keep it as the home for automations that don't belong to any project.
- **Dry run first:** a report of what would be removed and the space it frees, by category: temp folders, package-manager caches (npm, `pnpm store prune`, Gradle, pip), old build output, crash dumps, the Recycle Bin, Windows Update leftovers (built-in Disk Cleanup/DISM), installers sitting in Downloads, duplicate files, empty folders.
- Clean regenerable categories automatically (Tier 1). Personal files are never deleted: exact duplicates and obvious junk (zero-byte files, temp copies) move to `D:\Quarantine\<date>\` with a manifest (original path → new path) so anything can be restored. All other personal files stay where they are. The report lists what moved; Ahmed empties the quarantine whenever he likes.
- **Empty folders:** remove them only in user areas (Desktop, Documents, Downloads, `D:\Projects` outside git internals). Never in `Windows`, `Program Files`, `ProgramData` or `AppData`; apps expect those.
- **Antigravity's folder on C:** locate it (for example `%USERPROFILE%\.gemini\` and the app's data folders). First back up settings, skills, rules and anything that looks like conversation history. Then clear only caches, logs, old browser recordings and temp files. Report sizes before and after.
- Never touch restore points, drivers, BitLocker or security software. Report the space reclaimed.
