# Review: SIR Laptop Manager (2026-11-10, independent reviewer)

Repo `D:/Projects/SIR Laptop Manager`, HEAD `a0a0a41` (r13). Reviewed by running the project's own tools, calling the live service on 127.0.0.1:8765 (read calls and dry-run POSTs only) and reading code. Nothing was edited, stopped or committed.

## Verdict
1. The service runs and the Task Scheduler setup is real (verified: logon trigger, restart 3x/1min, detached from any IDE). But the checkpoint is wrong on its headline claims: "207/207 green" is false (20 of 207 fail, on my machine and on GitHub), CI has been red on `main` for the newest commit, and "all milestones complete" is false (threat model doc and RAG eval file do not exist, 12 PLAN boxes are unticked).
2. The owner's "unfinished" complaint is justified: the Startup Services panel throws on load, `/api/game-mode/undo` returns 405, Arabic covers about 14 strings out of hundreds, and Game Mode service restore can hang and sends a stray Telegram text.
3. Quality tools (ruff, ruff format, mypy strict) are clean; code is typed and mostly well structured. The problems are integration bugs that the tests miss because tests call internals directly or patch the wrong module.

## Commands run (exact) and results
| Command (in project root) | Result |
|---|---|
| `.venv/Scripts/ruff.exe check src tests` | All checks passed |
| `.venv/Scripts/ruff.exe format --check src tests` | 115 files already formatted |
| `.venv/Scripts/mypy.exe src tests` | Success, 96 source files |
| `.venv/Scripts/pytest.exe -q -p no:cacheprovider` | **20 failed, 187 passed** (125 s) |
| `gh run list` / `gh run view 42718467173 --log-failed` | Newest run (r13 commit) **failed**: 19 failed, 184 passed, 4 skipped on Windows runner; same `AttributeError` as local |
| `curl http://127.0.0.1:8765/` and `/api/health`, `/api/daemon/status` | 200, real data (pid 7904, parent pythonw, detached true) |

CI history: 4 of the last 8 runs failed (r13, the "fix(test)" and "fix(ci)" attempts, and r12). Two fix commits were spent patching tests for runner paths, which shows tests depend on `D:\` paths and the developer's machine.

## Claims table (checkpoint "Done" items and recent commits)
| # | Claim | Result | Evidence |
|---|---|---|---|
| 1 | 207/207 tests green, CI green | **Not working** | 20 fail locally and in CI run 42718467173 (tests patch `ops_ui.server.execute_cleanup` and `.WindhawkManager`, which r13 moved out of `server.py`) |
| 2 | Sovereign daemon `SIR_Laptop_Manager`, detached, restart on failure | **Verified working** | `Get-ScheduledTask`: AtLogOn trigger, RestartCount 3, interval PT1M; `/api/daemon/status` parent `pythonw.exe`, `is_detached_from_ide: true`, uptime 15211 s |
| 3 | Log rotation `.sir/daemon.log` at 5 MB | Verified (code `daemon_service.py:40-47`, log has live entries) | read |
| 4 | Health banner `#daemon-health-banner` with bilingual text | **Partly** | banner exists; Arabic mode only translates 14 i18n keys (see H3) |
| 5 | Game Mode pauses non-essential services, restores on exit | **Partly / not working** | pause path exists (dry-run `/api/game-mode/evaluate` ok); restore blocks on `ollama serve` (H1); Telegram "listener" does not exist (H2) |
| 6 | `/api/game-mode/undo` endpoint | **Not working** | `curl -X POST /api/game-mode/undo` with valid token returns 405: route missing from `VALID_POSTS` (`ops_ui/tailnet.py:27-43`); its test calls `dispatch_post` directly |
| 7 | Console window elimination | **Partly** | all 8 Python subprocess calls use `run_hidden`/hidden kwargs (verified); all SIR Laptop tasks run `pythonw`/`wscript`. Not fixed: `SIR_Reminder_Claude_Reset` runs `node.exe` directly (console subsystem, flashes); `send-telegram.mjs` calls `execFileSync('powershell')` without `windowsHide` (`_SIR/scripts/deliver/send-telegram.mjs:63`) |
| 8 | Weekly cleanup scheduled task `SIR_Laptop_DiskCleanup` | Verified registered (Ready, weekly trigger); run not executed (destructive) | `Get-ScheduledTask` |
| 9 | Dry-run cleanup via ops UI | **Partly** | `POST /api/care/clean-dry-run` takes 75 s standalone and over 150 s via the server (81,098 files); UI will look hung (M1) |
| 10 | Startup services panel / 11 services status | **Not working in UI** | API fine (`/api/startup/services` returns an object) but `index.html:6624` does `services.map` on the object: console error `services.map is not a function` on every load |
| 11 | RAG search bilingual | Verified (English) | `/api/rag/search?q=rules for agents` returns chunks; Ollama up. Arabic quality not verified; `.sir/evidence/rag-eval.md` (PLAN M4 exit check) does not exist |
| 12 | Security headers, Host allowlist, Origin+token on POST | **Verified working** | `Host: evil.com` gives 403; POST without Origin or token rejected; audit chain `/api/security/audit` intact |
| 13 | Zero emoji, zero em dashes, files under 300 lines | **Partly** | no emoji or em dash found in src; all Python under 300 lines, **but `index.html` is 6,981 lines / 196 KB** with 313 inline `style=` attributes |
| 14 | Disk cleanup freed 9.33 GB | Cannot verify | C: is now 14.16 GB free (93.3% used); D: 7.11 GB free (97.3%) |
| 15 | M0-M10 complete | **Not true** | `docs/THREAT_MODEL.md` missing, `.sir/evidence/rag-eval.md` missing, 12 unchecked boxes in `.sir/PLAN.md` section 8 |

## Defects

### Critical
None found that destroy data today. The closest are H1 and H2 below.

### High
**H1. Game Mode restore can hang forever and never clears its snapshot.**
`care/game_services.py:247` (and `startup/logon_automation.py:216-218`) launch `ollama serve` through `run_hidden`, which is `subprocess.run` and waits for the process to exit. `ollama serve` never exits, so the thread that handles `/api/game-mode/*` (or the game-exit watcher) blocks, `clear_snapshot()` (line ~166) is never reached, and any service after Ollama in the list is not relaunched.
Reproduce: stop Ollama while a snapshot exists, call restore (`GameServicesManager().restore_services()`) in a venv shell; it does not return.
Fix: use `popen_hidden` (non-blocking, `start_new_session`/`DETACHED_PROCESS` flags) for daemons; clear the snapshot per service after a successful launch; add a test with a fake long-running binary.

**H2. "Telegram Delivery Listener" does not exist and the launch path messages the owner.**
`care/game_services.py:72-79` and `startup/logon_automation.py:88-94` run `node send-telegram.mjs --listen`. `send-telegram.mjs` has no `--listen` flag (`_SIR/scripts/deliver/send-telegram.mjs:70-85`): the first argument `--listen` is not a file, so it is sent as a plain text message to the owner's Telegram. Every live startup run or Game Mode restore would send the text "--listen". Dry-run `POST /api/startup/run` lists this entry as "will start". This is a likely source of stray Telegram messages. I did not run it live (it would message the owner).
Fix: delete the entry from both lists (there is no listener). Add a test that no service definition points at a script flag that the script does not parse.

**H3. Arabic is not really supported.**
`ops_ui/static/index.html:3803-3835` has 14 translated keys. With the language switch on, 153 of 228 visible leaf text nodes on the Security tab stay English; only `dir=rtl` flips. Checkpoint and plan promise Arabic and English everywhere.
Reproduce: open `/`, click the language button, look at any tab.
Fix: see brief task on extracting strings to `static/i18n/en.json` and `ar.json` with a `data-i18n` attribute on every static label, and a test that fails when a key exists in one file and not the other.

**H4. Newest commit is red in CI and tests do not protect the real routes.**
20 tests patch names that do not exist (`ops_ui/server.py` no longer imports `execute_cleanup` or `WindhawkManager`): `tests/test_ops_ui_server.py:114,188-212`, `tests/test_tailnet_allowlist.py` (`test_post_guarded_with_allowed_tailnet_origin`). One more failed in the full run only (`tests/test_ops_ui_endpoints.py::test_read_endpoints_reject_foreign_host[/]`, passes alone): shared global rate limiter state (`GLOBAL_RATE_LIMITER`) leaks between tests.
Fix: patch where used (`sir_laptop_manager.ops_ui.routes_extended.*`), reset the limiter in a fixture, and make `verify.ps1` the only definition of "done".

**H5. Startup Services panel is broken on every page load.**
`index.html:6624` expects an array and fields `running`, `type`; the API returns `{services:[...]}` with `is_running`, `category` (`ops_ui/routes_cycle10.py:42-54`). Console error on each load; the panel stays empty and reports nothing.
Fix: read `data.services`, use `is_running` and `category`, add empty and error states.

**H6. `/api/game-mode/undo` unreachable (405).** `ops_ui/tailnet.py:27-43`: missing from `VALID_POSTS`. The owner-required undo button for Game Mode therefore cannot work. Fix: add it, and add an HTTP-level test (not `dispatch_post`) for every route in `dispatch_post`.

### Medium
**M1. Dry-run clean is very slow and the live clean differs from the dry run.** `POST /api/care/clean-dry-run` = 75 s alone (81,098 files, 2.14 GB) and over 150 s through the server; no progress, no timeout in the UI. `care/cleaner.py:57-80`: per-file `resolve()` and `stat()` twice. The dry-run uses no age filter, while the real run (`care/safe_clean_orchestrator.py:130-140`) skips files younger than 24 h, so the preview overstates what will be freed. Fix: cache the report for 5 min, make it a background job with `GET` status, apply the same age filter in both.

**M2. Live `/api/space/clean` permanently deletes caches, no undo.** `care/safe_clean_orchestrator.py:~120-150` "Step 1 direct purge" unlinks regenerable caches without quarantine, while the UI and checkpoint advertise dry-run plus undo. Only `.exe` files in Downloads are quarantined. Fix: say so in the UI text, or quarantine everything above 50 MB.

**M3. Tests write into real state.** Running the suite created new buckets in the live quarantine (`.quarantine/q_20261110_021212_3cb711`, `..._021216_41609f`, `..._021325_277cec`; each 1 file, 4 bytes) and there are 95 buckets now, many from tests. Part of this was caused by my own test runs; they are 4-byte test files in a gitignored folder and I left them in place. Fix: `tmp_path` quarantine root in `tests/test_care_cleaner.py` and `tests/test_quarantine_engine.py`, plus a conftest guard that fails when `PathsConfig.project_root` is not patched.

**M4. Hard-coded machine paths.** `ops_ui/routes_space.py:130` and `care/quarantine_cli.py:29` use `D:\Projects\_SIR\_quarantine`; `care/scheduled_cleanup.py:62`, `startup/logon_automation.py:234-241` (including `C:\msys64\ucrt64\bin\pythonw.exe`), `care/safe_clean_orchestrator.py:84` (`D:\Downloads`, `C:\Users\a7med\Downloads`), `core/paths.py:34`. Reason CI needed two fix commits. Good: the correct `D:\Projects\AI_Models_Hub` is derived from `workspace_root` (`core/paths.py:37`) and the old path appears nowhere in src. Fix: one `PathsConfig` field for each and env override.

**M5. Fail-open identity.** `ops_ui/server.py:_user_ok` passes when `Tailscale-User-Login` is absent. With a tailnet Host header and no identity header the server answers 200 (`curl -H "Host: ahmed.tail9e9aa7.ts.net:8765" http://127.0.0.1:8765/api/health`). Today this needs a local process (tailnet-only serve), so risk is low, but it turns off the owner check whenever Funnel is enabled by mistake. Fix: require the header whenever Host is not loopback. Also `/api/session` hands the CSRF token to any caller with a good Host (by design, but then the token adds nothing).

**M6. `index.html` is a 6,981-line, 196 KB monolith** with inline JS and CSS. Violates the 300-line rule, makes the 20 tests and a11y checks fragile, and the checkpoint claims "strict <300-line ceiling across all files". Fix: split into `static/css/*.css`, `static/js/*.js` modules.

**M7. Stray startup-time test and doc gaps:** `docs/THREAT_MODEL.md` and `.sir/evidence/rag-eval.md` missing; `pyproject.toml` version is `0.1.0` (rule says 1.0.0); `.sir/disk_watcher_state.json` is untracked runtime state that should be in `.gitignore`.

**M8. Console flashes still possible outside Python.** `SIR_Reminder_Claude_Reset` task runs `node.exe` directly; `send-telegram.mjs:63` spawns `powershell` without `windowsHide: true` (only when env vars are missing, but the disk watcher calls this script from the hidden daemon). Fix: wrap with `wscript //B` hidden runner and add `windowsHide: true`.

### Low
- L1. `window.confirm` used three times (`index.html:5285, 6175, 6379`): blocking and unstyled; replace with an in-page confirm sheet (earlier cross-review flagged it, not fixed).
- L2. Route modules named by build round (`routes_cycle7.py`, `routes_cycle8.py`, `routes_cycle10.py`): rename by feature (`routes_telemetry`, `routes_dispatch`, `routes_gamemode`).
- L3. `dispatch_post` returns `{"error": ...}` with HTTP 200 for unknown routes (`routes_cycle8.py:142`) and many handlers return `success:false` with 200.
- L4. Brand: `.sir/DESIGN.md` seed colour is `#475569` slate; the UI uses emerald `#10b981`. Decide and write it down.
- L5. At 320 px the stat tiles stack with oversized labels and one `.btn-accent` on the RAG tab extends past the viewport (measured `right > innerWidth`); tables scroll inside their own wrapper (acceptable). No horizontal page scroll at 320, 390, 502, 1038.
- L6. `PytestUnraisableExceptionWarning` from unclosed HTTP responses in `test_ops_ui_endpoints.py`.
- L7. Hard-coded owner email in `ops_ui/server.py:30`.
- L8. `core/restore_point.py`, `power/battery_wear.py` not exercised against real Windows in CI (4 skipped tests).

## What I could not check
Live Game Mode pause/restore (would stop real services), the live clean, weekly task execution, Arabic RAG score, screenshots at 768/1280/1920 (checked overflow numerically at 320 and ~500/1038; one screenshot at 320 px was inspected), 5-state coverage of every tab.

## Status update (re-checked later on 2026-11-10, after r15 and during r16)
- Fixed since the review: the 20 broken tests (r15 commit `2cfcf2f`; full suite now 226 passed locally), `/api/game-mode/undo` is in `VALID_POSTS`, the Startup Services panel reads `payload.services`, the fake Telegram `--listen` entry is gone, Game Mode launches daemons with `popen_hidden`, `docs/THREAT_MODEL.md` exists, ruff, ruff format and mypy are clean (101 files).
- Caveat: several of these fixes are still uncommitted in the working tree (git status shows modified `.gitignore`, `.sir/DESIGN.md`, deleted `.sir/game_services_snapshot.json`). GitHub Actions on `main` was red again on the three r15 commits, failing at the "ruff format" step; the working tree formats clean, so pushing the r16 work should turn it green. Check `gh run list` after the push.
- Still open (not re-fixed when I looked): Arabic coverage (only 2 `i18n` hits in a now 7,765-line `index.html`), the monolithic `index.html`, hard-coded paths, slow dry-run clean, `rag-eval.md` evidence, route modules named by round. Treat the rest of this file as the open list except items listed as fixed above.
