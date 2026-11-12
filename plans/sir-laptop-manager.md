# PLAN: SIR Laptop Manager (Wave 2, PERSONAL tool, building)
Audited 2026-11-10. Replaces: `Laptop manager` and `antigravity-agent-suite` (both now under `legacy/`, kept until M6). Internal tool for one owner: not sold, not listed, `noindex`. **PERSONAL**: only Ahmed, never sold. Commercial items are marked "n/a" with the reason; nothing is silently dropped. Uses the same architecture and rules as GLOBAL products (SHARED_PLATFORM_KIT) where applicable.

## 1. Purpose (plain words)
It keeps Ahmed's Windows laptop healthy. It shows disk, memory, battery and startup items on one page, cleans junk safely (everything goes to a quarantine folder first and can be restored), pauses heavy background programs while he plays a game, and keeps one set of AI-agent rules in sync across all his coding tools.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Laptop Manager` |
| GitHub (private) | `sirahmed8/sir-laptop-manager` |
| Runtime | Python 3.14 (uv), `src/sir_laptop_manager/` (packages: agent_config, care, core, look, ops_ui, power, rag, startup, tray), ops page on `127.0.0.1:8765` |
| Platforms | **Platform Matrix (PERSONAL):** Windows ✅ built, unverified (ops page, tray, scheduled task `SIR_Laptop_Manager`). iPhone companion over Tailscale ✅ built, unverified. Web/PWA, Android, macOS, Linux, TV, watch, extension: ⏭️ skipped, a Windows-only tool. |
| Money | none (internal). Subscription, EGP pricing, checkout fallback: n/a. Default: if it is ever sold, move the generic parts to SIR Platform billing first. |

## 3. Current state
Claimed in `.sir/CHECKPOINT.md` (2026-11-10): milestones M0 to M10 and rounds 8 to 13 done, "207/207 tests green", 96 source files typed clean. PORTFOLIO.md (2026-11-08) said 12 of 27 tasks, 29 commits.
Verified by this audit on 2026-11-10 (command `uv run --offline pytest -q` in the project folder): **188 passed, 19 failed** out of 207. Failures are in `tests/test_ops_ui_server.py` and `tests/test_tailnet_allowlist.py`; first cause: tests patch `ops_ui.server.execute_cleanup`, which no longer exists. So "207/207" was not true today. Nothing else was re-run.
Built, unverified: dry-run cleanup with SHA-256 quarantine, desktop shortcut doctor, startup doctor with registry backup, game-mode service relief (`game_services.py`, `game_mode.py`), disk watcher, telemetry history, tray companion, agent-config sync (18 tools), local RAG over `AI_Models_Hub`, Dynamic-Island style tabs, Arabic RTL layout, scheduled-task daemon with log rotation.
Not started: Telegram report format per standard 26, evals for RAG (Arabic and English), licence audit of the 97 imported skills, restore drill evidence, phone/Tailscale threat test, CI proof (GitHub run link), Chinese and Hindi text.

## 4. Security rules (each needs a test or command)
1. Binds to 127.0.0.1; phone access only with `Tailscale-User-Login` header check plus CSRF HMAC token. Test: bad host and bad origin POSTs return 403 (the currently failing tests cover this; fix them first).
2. Every POST that changes anything defaults to dry run and needs explicit `confirm: true` (boolean, not a string).
3. Deletes always go to quarantine with a manifest; undo works. Sync never deletes.
4. Secrets only in Credential Manager or untracked `.env`. The old hard-coded Telegram token in 5 legacy files is rotated (M6) and gitleaks runs on history.
5. No graded-work automation of any kind (the legacy academic script stays in `legacy/` and is not ported).
6. Paths and subprocess arguments never from raw input (path traversal test).
7. Private text (notes, RAG corpus) goes only to local models.
8. Licence audit of the 97 skills before they leave `legacy/`: keep MIT/Apache/BSD, drop unknown.

## 5. Shared pieces (use SIR Platform, do not rebuild)
- Telegram reports and approvals: use the one shared sender `scripts/deliver/send-telegram.mjs` and the report format in section 8; do not write a second bot.
- Design tokens and settings/profile screens: copy from the first finished SIR web product; Platform extracts them last. Until then keep them as `src/.../look/` and mark them "extract to Platform".
- No auth, billing or AI proxy needed (single owner, loopback). The local RAG is the only AI feature and it stays local.
- **Reuses SHARED_PLATFORM_KIT design tokens, motion, i18n, legal-pack patterns; no auth/billing/ai-proxy needed for personal use.**

## 6. Screens and entities
Screens: Dashboard (disk, memory, battery, startup, health), Cleanup (dry run, quarantine, restore), Game mode, Shortcuts and startup doctor, Agent config sync, Local AI (RAG), Settings and Profile. Entities: CleanupPlan, QuarantineItem, Routine, AgentProfile, Skill, SyncRun, GameProfile.
Five states on every screen. Arabic RTL and English first; light, dark, system, high contrast; 320 px to 4K; spring motion with reduced-motion path; WCAG 2.2 AA; own logo in favicon, tray and top bar.

## 7. Support assistant and AI
In-product assistant = the RAG page grounded only in `docs/` and the runbook; answers in Arabic or English; no quota (one user). Fallback: local model A, local model B, plain search over docs. "Why is my laptop slow" explanation with a one-tap safe fix is the flagship; it must show the dry run first.

## 8. Operations (standard 26, scaled to one user)
- Health: `doctor` command, daemon log rotation (done, unverified), weekly care routine registered in Task Scheduler.
- Telegram weekly report in simple Arabic: disk free C: and D:, bytes freed, quarantine size, last backup date, failed tests count. Alerts: disk below threshold, daemon down for more than 10 minutes. The sender never includes file names from private folders.
- Backups: weekly snapshot of `.sir/` state and config to `D:\Projects\Backups`, restore drill once per month.
- Updates: `uv lock --upgrade` weekly on a branch of work, tests must pass before push to main.

## 9. Three-Milestone Roadmap (owner-visible checks)
| Milestone | Goal | Owner-Visible Exit Check |
|---|---|---|
| **M1: Foundations & Security** | `scripts/verify.ps1` green; `docs/THREAT_MODEL.md` present; gitleaks 0 findings; 0 failing tests; path traversal and bad-origin tests for every POST route | 1. Run `scripts/verify.ps1` → all green, writes `.sir/evidence/verify-latest.md` with real counts. 2. `git check-ignore` confirms no secrets. 3. CI green badge URL in checkpoint. 4. All 207 tests pass. |
| **M2: Core Features Verified** | Dry-run cleanup and quarantine (clean, restore, hash compare test passes); agent config sync and routines (sync on temp workspace leaves no deletion; routines listed by `schtasks`); local AI RAG eval file with 20 Arabic and 20 English questions, score recorded | 1. Quarantine a temp file → restore → hashes equal (evidence). 2. Sync dry run on temp workspace → no deletions. 3. `schtasks /query` shows `SIR_Laptop_Manager` routine. 4. `.sir/evidence/rag-eval.md` has 20+20 scores. |
| **M3: Quality & Retirement** | 5-state screenshots at 320, 390, 768, 1440; RTL and LTR; zoom 200%; `legacy/*` moved to `D:\Projects\old projects\`, old repos archived, keys rotated | 1. Screenshots of Cleanup and Game mode at 320/390/768/1440, RTL/LTR, light/dark, zoom 200%. 2. `scrollWidth <= innerWidth` in capture output. 3. `legacy/*` moved to `old projects\`. 4. Old GitHub repos archived. 5. Keys rotated (names only in `docs/OWNER_STEPS.md`). |

## 10. Next 10 tasks (each under 2 hours)
1. Fix the 19 failing tests: restore or rename `execute_cleanup` in `src/sir_laptop_manager/ops_ui/server.py` or update the tests in `tests/test_ops_ui_server.py`. Check: `uv run --offline pytest -q` shows 0 failed.
2. Make `scripts/verify.ps1` fail on any failing test and write the date and result to `.sir/evidence/verify-latest.md`. Check: run it, file shows real counts.
3. Push to GitHub and record the Actions run URL; if red, fix. Files: `.github/workflows/`. Check: green badge URL in checkpoint.
4. Path traversal and bad-origin tests for every POST route. Files: `tests/test_ops_ui_security.py`. Check: pytest passes; a route without the guard makes it fail.
5. Restore drill: quarantine a temp file, restore, compare hashes. Files: `.sir/evidence/restore-drill.md`. Check: hashes equal.
6. Licence audit script for `legacy/antigravity-agent-suite` skills: output CSV of name and licence. Files: `scripts/license_audit.py`, `.sir/evidence/skills-licences.csv`. Check: every row has a licence or "unknown"; unknown ones are not imported.
7. Port the keepers from the audit into `src/.../agent_config/skills/` with a manifest. Check: sync dry run lists them, no deletions.
8. RAG eval set (20 Arabic, 20 English) and a runner. Files: `tests/rag_eval/`, `scripts/rag_eval.py`. Check: score printed, saved to evidence.
9. Telegram weekly report builder with a privacy filter (no paths outside project names). Files: `src/.../core/report.py`, test. Check: test proves a private path is redacted; real send returns ok from the API.
10. Five-state screenshots of Cleanup and Game mode at 320 and 390 px, fix overflow. Files: `scripts/capture_*.mjs`. Check: `scrollWidth <= innerWidth` in the capture script output.

## 11. Risks and open questions (defaults)
- The safety classifier blocks edits to global agent config: default is project-scope sync only, global writes go to OWNER_ACTIONS as one command.
- The "all green" claim was false today: default is no milestone is called done until section 10 task 1 and 2 are done.
- Python 3.14 is new: default is keep it, pin in `pyproject.toml`; fall back to 3.13 if a wheel is missing.
- Game mode pauses other local services (Jobs, Study, Control Room, Ollama): default is a visible banner and one-tap restore, tested.

## 12. Only the owner can do
Approve the Windows UAC prompt when installing the scheduled task; sign in to Tailscale on the phone; sign in to GitHub if the token expired.

## 13. Market-grade note
Competitor study exists at `plans/competitors/sir-laptop-manager.md` (dated 2026-11-09, some claims cite forums; any claim without a link there is "(unsourced, verify)"). Country law packs: n/a (single owner). Privacy: collects nothing off the machine.

## 14. Competitor Matrix (from plans/competitors/sir-laptop-manager.md)
| Competitor | Strengths | Flaws | Our Edge | Ideas to Steal |
|---|---|---|---|---|
| (to be sourced) | | | | |

*Every claim in competitor matrix must carry a source link or "(unsourced, verify)".*

## 15. Feature Parity Target (best-in-category)
Match or exceed the best laptop manager for: quarantine-based cleanup with undo, game-mode service relief, agent-config sync across 18 tools, local RAG with Arabic/English, scheduled daemon with log rotation, Dynamic-Island style tabs, Arabic RTL, spring motion.