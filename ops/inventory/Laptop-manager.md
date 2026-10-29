# Inventory: Laptop manager (Phase 3.1)
Scanned 2026-10-29. Read-only on the project. Evidence: git commands, ast parse, `laptop_admin.py --help` (exit 0). Nothing installed, nothing run beyond that.

## What it is and who for
Ahmed's "Personal OS": PC cleanup, Telegram bridge, TickTick sync, Moodle/Obour academic scripts, social/video generators, agent-config and local RAG (branches). Only Ahmed. Windows only, D:\ paths hard-coded.

## Build and run
- No package.json, pyproject, requirements file, or CI (no .github). 80 tracked .py files all parse (ast, no syntax errors). `python -I laptop_admin.py --help` lists 15 subcommands, exit 0.
- Not run: tests (3 files under tests/), any side-effect subcommand.

## Stack
Python 3 (CLI, bridge, scripts), PowerShell (.ps1), VBS/CMD launchers, one .mjs sync script (branch). Only stdlib sqlite3 seen among common libs. Ollama + bge-m3 for RAG (branch worktree-agent-config-and-rag, local-ai/rag.py, 104 lines).

## Repo health
- origin: github.com/sirahmed8/laptop-manager, PRIVATE (gh), pushed 2026-10-29.
- main b6b62f7 (2026-10-28). 345 tracked files.
- worktree-personal-os-charter 9a3107a: +27 lines (AGENTS.md, docs/PERSONAL_OPS.md), 1 commit ahead of main, worktree clean.
- worktree-agent-config-and-rag 8bd4340: +385 lines in 23 files (agent-config/ 18 agents, rules, skill, sync script; local-ai/rag.py), 1 commit ahead, worktree clean.
- pre-sir-snapshot 6e4e8b1: local branch only.
- Main has untracked: .claude/ (holds both worktrees), archive/, tools/sync_all_public_repos.{bat,py}.
- No stash entries. README.md is the only top-level doc with a clear purpose line.

## Structure
Flat root with about 60 ad-hoc scripts (analyze_*, drilldown_*, inspect_*, check_*), plus scripts/ (46 files), tools/ (23 tracked), social_outputs/ (86 JSON/MD), public/ (42, incl. 2.3 MB MP4), n8n_workflows/ (3), tests/ (3), assets/.
Duplicates: tools/pc_cleaner.py and pc_cleaner_v2.py.

## Platforms, data, auth, AI
- Platform: Windows 11 only. Desktop launchers: no .lnk on C:\Users\a7med\Desktop points here. Scripts that reference the project: setup_desktop_launchers.ps1:188-194, deploy_all_desktop_shortcuts.ps1:7, start_telegram_bridge.cmd:4, run_telegram_bridge_hidden.vbs:2, scripts/start-web.ps1:1.
- Data: JSON files, sqlite (TickTick DB), social_outputs/, academic_outputs/attendance_sync_20261023.json (tracked, personal).
- Auth: Telegram bot token, TickTick, Moodle login (14 "password" keyword hits in moodle scripts; no literal credential assignment found in .py/.ps1).
- AI: Gemini (34 keyword hits), Ollama (RAG), Telegram (162), TickTick (27), WhatsApp (13), n8n (11), Firebase (2). Call volume not measured.
- Legal: PRIVACY_POLICY.md 59 lines, TERMS_OF_SERVICE.md 57, COOKIE_POLICY.md 40, REFUND_POLICY.md 32, EULA.md 20. No placeholder markers. No LICENSE file.
- Icons: assets/laptop_manager.ico and assets/icons/ (4 .ico).
- Tests: 3 files (test_adversarial_challenger_2.py has 17 test functions). Not run.
- Docs: README.md uses emojis and hype ("AUTONOMOUS JARVIS OS", "Executive AI co-founder"), which breaks the no-hype rule.

## Red flags
1. SECRET (high): Telegram bot token-shaped value hard-coded in 5 tracked files (antigravity_telegram_bridge.py:44, scripts/configure_telegram_bot_info.py:6, scripts/telegram_helpers/send_executive_update_tg.py:8, test_clean_html.py:86, test_send_photo.py:9). Value matches bot_token in telegram_config.json (gitignored, on disk). Also present on origin/main, so it is in remote history. Value not printed.
2. Token-like fixtures in tests/test_adversarial_challenger_2.py (9 hits, lengths 22 and 34, likely fake; unverified).
3. Deletes without quarantine, against PERSONAL_OPS rule: tools/pc_cleaner.py:56, tools/pc_cleaner_v2.py:28, tools/storage_watchdog.py:95, archive_old_conversations.py:47,52, scripts/moodle/clean_academic_duplicates.py:19. Setup script removes Desktop .lnk/.url (setup_desktop_launchers.ps1:92-93).
4. Academic automation: tools/academic_jarvis_automator.py:74 run_attendance_sync, plus 9 "submit" and 15 "attendance" hits in tools/ and scripts/moodle/. Needs review against "never take graded work" and "no 2FA or platform bypass". Not proven either way.
5. Social/browser automation names: scripts/generate_brand_assets.py (6 hits for playwright/selenium/x.com keywords), scripts/generate_ai_brand.py (2). X scripting not confirmed or ruled out.

## Overlap (concrete, from names only; other projects not read)
- SIR Optimizer: PC cleanup (clean-pc, pc_cleaner*.py, storage_watchdog.py). Unverified overlap.
- SIR AI: Ollama/RAG (rag.py), AI routing. Unverified.
- SIR Controller: Telegram/status and launchers. Unverified.
PORTFOLIO.md rows: Laptop manager, SIR AI, SIR Controller, SIR Optimizer (lines 11, 16, 18, 23).

## Scores (0-5)
- Architecture 2: flat script pile, no package boundaries.
- Code quality 2: parses; duplicate cleaners; no tests run or in CI.
- Security 1: committed bot token; personal PDFs and academic data in repo.
- UX/design 1: CLI and emoji README; no UI.
- Performance 2: not measured.
- Completeness 2: branches hold the new work, main lacks it.
- Store readiness 0: personal Windows tool, no store target.

## Upgrade and business ops
Size: M.
Top 5 fixes:
1. Remove the hard-coded token (5 files), read from telegram_config.json or env, rotate token (owner), purge history.
2. Merge both branches into main; move .claude/worktrees out; commit or drop archive/ and tools/sync_all_public_repos.*.
3. Group root scripts into packages (pc/, academic/, social/, bridge/) with a requirements file, then run the 3 tests in CI.
4. Make all deletes move to quarantine first (pc_cleaner*.py, storage_watchdog.py, archive_old_conversations.py).
5. Review academic submit/attendance automation and X scripting against rules; rewrite README without hype.

Business ops: partly. Social posting prep, TickTick, Obour study tools are present. No income, billing or client tracking code found by names.
