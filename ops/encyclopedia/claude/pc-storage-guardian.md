# pc-storage-guardian

Tools: claude, codex, cursor, gemini-plugin, kilo, opencode, windsurf (kilo copy used; identical across tools).
Source: C:\Users\a7med\.config\kilo\skills\pc-storage-guardian\SKILL.md (76 lines, read in full)

## Summary
A Windows workstation hygiene skill: disk telemetry thresholds (C: critical <12 GB free, healthy >25 GB), a whitelist of safe prune targets (npm/pip caches, %TEMP% files older than 24h, Windows Temp, crash dumps, pytest/eslint caches), non-destructive execution rules (skip locked files, batch operations for SSD wear, never defrag NVMe), and a dry-run-first workflow pointing at `D:\Projects\Laptop manager\tools\pc_cleaner.py`.

## When to use / not use
Use when a Windows dev machine's system drive is filling up or caches need periodic pruning. Not a backup tool, not for deleting user files/repos/.env — the whitelist is explicit and anything outside it is off-limits.

## Inputs, outputs, dependencies
Input: PowerShell access on the owner's machine. Output: reclaimed disk space via cache/temp purges. Needs: the `pc_cleaner.py` tool at the hardcoded path, `npm`/`pip` CLIs for their cache commands, PowerShell for telemetry.

## Key rules
1. Measure first: `Get-PSDrive C, D` free/used GB before and after; dry-run the cleaner before real purge.
2. Only approved targets: npm `_cacache`, %TEMP% (>24h old), C:\Windows\Temp remnants, CrashDumps .dmp files, pip cache, project `.pytest_cache`/`__pycache__`/`.eslintcache`.
3. Never delete user files, desktop files, git repos, or .env configs; wrap every unlink in try/except and skip locked files.
4. SSD preservation: batch prunes on intervals (e.g. 6h cron or manual), no micro-deletions, never defragment NVMe (TRIM is native).
5. Sequence: dry-run → real purge → npm cache clean → verify with Get-PSDrive.

## Risks / owner items
- Hardcodes user-specific paths (`C:\Users\a7med`, `D:\Projects\Laptop manager`) — portable only on Ahmed's machine; other users need path edits.
- %TEMP% deletion can break apps mid-write; the 24h age rule and lock-skipping mitigate but don't eliminate risk.
- References an external script that must exist; if `pc_cleaner.py` is missing the skill degrades to manual commands.

## Category and tags
ops — windows, disk-cleanup, storage, ssd, maintenance, powershell.

## Revision note
Identical across tools; owner-machine-specific tooling baked into a "skill".
