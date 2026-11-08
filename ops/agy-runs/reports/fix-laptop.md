# fix-laptop report (2026-11-08, Claude builder)

Repo: D:/Projects/SIR Laptop Manager. Commits 06a8e4d, f287ca5, 7844c0f, 6163c2b, pushed to origin/main (fast-forward b86e920..6163c2b).

## Fixes (file:line)
1. scripts/restore-look.ps1 (rewritten). Dry run by default (Invoke-RestoreLook :114); -Execute needs elevation (:123), aborts if .reg export fails (:168) or restore point cannot be verified (:175, sequence number must rise). Every write is read back with its registry type (Set-RegValue :74). Failures exit 1; no "Restored Successfully" line. dock.bottomGap = 4 DWord (:28). Numbers are DWord and text is String, as Windhawk stores them (checked read-only with reg query). Disabled is no longer force-set; only SettingsChangeTime is touched. Mods that are not installed are skipped (windows-animations is not installed on this machine).
2. src/sir_laptop_manager/ops_ui/server.py: SESSION_TOKEN :32, Host/Origin/token guard `_guard_post` :67, `/api/session` :119, fix-gap dry run unless JSON `confirm: true` :301. All POSTs guarded (clean-dry-run too). index.html postGuarded :723, fixDpiGap does dry run, native confirm, then execute (:739-750). Body capped at 4096 bytes.
3. src/sir_laptop_manager/look/windhawk_manager.py: pre_modification_guard :129 returns False when the restore point fails; set_mod_setting :147 (dry run default, DWORD/SZ, read-back); fix_dpi_bottom_gap :268 (dry run default, elevation check, range 0-64, blocked without restore point). cli.py look fix-gap has --execute.
4. scripts/dev-stop.ps1: Test-IsOurServer :9 / Stop-IfOurServer :15 kill only processes whose command line contains sir_laptop_manager.ops_ui.server (PID file and port 8765 owner).
5. .sir/reports/scan-2026-11-08.md: token line removed. `git rm --cached .sir/backups`; .gitignore now lists .sir/backups/windhawk/, .sir/backups/agent-pointers/, *.bak.

## Tests
tests/test_windhawk_manager.py (+10), tests/test_ops_ui_server.py (guard matrix, dry-run default, strict confirm, bad bodies), tests/test_powershell_scripts.py (9: dry run leaves HKLM unchanged, abort paths with mocked functions, typed writes, dev-stop skips a decoy process).
ruff format/check clean, mypy strict "no issues in 38 files", pytest 82 passed. restore-look.ps1 was never run with -Execute; the registry was only read.

## Open
- The old Telegram token id remains in git history of this repo (commits before 6163c2b) and in the legacy Laptop manager repo: rotate it (bot token rotation is allowed for agents; needs BotFather, i.e. Ahmed's sign-in).
- The two .reg and two .bak backups also remain in history.
- server.py is about 310 lines (over the 300 limit); split the GET handlers into a module next.
- The live registry still has dock.bottomGap = 2; run `uv run sir look fix-gap --execute` from an elevated shell to apply 4.
