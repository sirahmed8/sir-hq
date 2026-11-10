# Brief r16-laptop: SIR Laptop Manager, fix what the review found, then improve it

You work only in `D:/Projects/SIR Laptop Manager`. Python, local web UI on port 8765. An independent reviewer ran everything and found that several "done" claims are false. Full evidence: `D:/Projects/_SIR/ops/reviews/2026-11-10/review-laptop-manager.md` (read it first, 5 minutes).

## Rules
- Never ask the owner anything; decide, log it in `.sir/CHECKPOINT.md`, continue.
- After EVERY numbered task: run `powershell -File scripts/verify.ps1` (ruff format, ruff check, mypy, pytest must all pass), then `git add -A`, `git commit`, `git push origin main` (straight to main, never a pull request), then add one line to `.sir/CHECKPOINT.md` "Done" with the commit hash.
- Version stays 1.0.0 everywhere (set `pyproject.toml` version to `1.0.0` in task 1). No emoji, no em dashes, no placeholder text, no invented data or numbers anywhere in the UI.
- Never run anything destructive: no real cleanup, no stopping services, no uninstall. Use dry-run endpoints only. Do not stop or restart the running server on port 8765 except through its Task Scheduler task `SIR_Laptop_Manager` after all tests pass, and then check `curl http://127.0.0.1:8765/api/daemon/status`.
- Python files stay under 300 lines. Absolute imports. Never write the old path `D:\AI_Models_Hub`; the correct one is `D:\Projects\AI_Models_Hub`.
- Do not claim anything is done until the acceptance command in the task prints what is asked. Paste the real output in `.sir/evidence/r16-laptop.md`.
- Never read anything under `D:/Projects/AHome`.

## Read first (in this order)
1. `D:/Projects/_SIR/ops/reviews/2026-11-10/review-laptop-manager.md`
2. `.sir/CHECKPOINT.md`, `.sir/DESIGN.md`
3. `D:/Projects/_SIR/standard/23-premium-code-bar.md` and `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`
4. `src/sir_laptop_manager/ops_ui/tailnet.py`, `routes_cycle8.py`, `routes_cycle10.py`, `care/game_services.py`

## Part A: bug fixes (do in this order)

**1. Make CI green again.**
Files: `tests/test_ops_ui_server.py` (lines about 114, 188-212), `tests/test_tailnet_allowlist.py`, `tests/test_ops_ui_endpoints.py`, `pyproject.toml`.
Change: the tests patch `sir_laptop_manager.ops_ui.server.execute_cleanup` and `...server.WindhawkManager`, which no longer exist there. Patch the names where they are used: `sir_laptop_manager.care.cleaner.execute_cleanup` (imported inside `routes_extended.post_clean_dry_run`) and `sir_laptop_manager.look.windhawk_manager.WindhawkManager`. Add a pytest fixture in `tests/conftest.py` (autouse) that resets `GLOBAL_RATE_LIMITER` before each test so `test_read_endpoints_reject_foreign_host[/]` stops failing in the full run. Set version `1.0.0` in `pyproject.toml`.
Acceptance: `.venv/Scripts/pytest.exe -q -p no:cacheprovider` prints `0 failed`; after push, `gh run list --limit 1` shows `completed success` (wait with `gh run watch`). If CI still fails, run `gh run view --log-failed`, fix, push again until green.

**2. Add the missing undo route and test every route over HTTP.**
Files: `src/sir_laptop_manager/ops_ui/tailnet.py` (`VALID_POSTS`), new `tests/test_every_post_route.py`.
Change: add `"/api/game-mode/undo"` to `VALID_POSTS`. Write one test that imports `dispatch_post` source routes (parse `routes_cycle8.py` for `url == "..."` strings or keep a single route table module shared by both) and asserts every route handled by `dispatch_post` is in `VALID_POSTS`, and that a real HTTP POST with Origin and token to `/api/game-mode/undo` body `{"dry_run": true}` returns 200.
Acceptance: `curl` flow: get token from `/api/session`, POST `/api/game-mode/undo` with `{"dry_run":true}` and `Origin: http://127.0.0.1:8765` returns JSON, not 405. The new test passes.

**3. Fix the Startup Services panel.**
File: `src/sir_laptop_manager/ops_ui/static/index.html`, function `loadStartupServices` (about line 6615).
Change: read `data.services` (the API returns an object), use `is_running` and `category`, show an empty state ("No services configured") and an error state with a Retry button.
Acceptance: open `http://127.0.0.1:8765/`, Startup tab; browser console shows no `services.map` error (check with chrome devtools `list_console_messages`); screenshot at 390 px saved to `docs/screenshots/r16/startup-390.png` shows 11 service cards with RUNNING or STOPPED.

**4. Remove the fake Telegram listener and make Game Mode restore non-blocking.**
Files: `care/game_services.py` (list at lines 36-80, `_relaunch_service` line 247), `startup/logon_automation.py` (lines 87-94, 216-218), `core/process_flags.py`.
Change: delete the "Telegram Delivery Listener" entry from both lists (the script has no `--listen`; it would send the text "--listen" to the owner). Launch daemons (Ollama and any `cmd` type) with `popen_hidden` (not `run_hidden`) so the call returns at once. Clear the snapshot record by record after each successful launch, not only at the end. Add tests in `tests/test_round13_game_services.py` using a fake long-running binary (`python -c "import time; time.sleep(60)"`) proving `restore_services()` returns in under 3 seconds.
Acceptance: `.venv/Scripts/pytest.exe tests/test_round13_game_services.py -q` passes; `grep -rn "listen" src/sir_laptop_manager/care/game_services.py src/sir_laptop_manager/startup/logon_automation.py` prints nothing.

**5. Stop tests from writing into real state.**
Files: `tests/test_care_cleaner.py`, `tests/test_quarantine_engine.py`, `tests/conftest.py`.
Change: every test that creates a quarantine bucket must use `tmp_path`. Add an autouse fixture that sets an env var `SIR_LM_STATE_DIR` to `tmp_path` and make `core/paths.py` honour it for `quarantine_dir` and `.sir` state files. Add a guard test: after the full suite, the number of directories in `.quarantine/` is unchanged (compare before and after in a session-scoped fixture).
Acceptance: run `ls .quarantine | wc -l` before and after `pytest`; the numbers are equal. (Do not delete the existing buckets.)

**6. Remove hard-coded machine paths.**
Files: `ops_ui/routes_space.py:130`, `care/quarantine_cli.py:29`, `care/scheduled_cleanup.py:62`, `startup/logon_automation.py:234-241`, `care/safe_clean_orchestrator.py:84`, `core/paths.py`.
Change: add `PathsConfig` fields `shared_quarantine_dir`, `pythonw_path`, `downloads_dirs` (derived from `USERPROFILE`, `sys.executable`, workspace root) with env overrides. Replace each literal. Remove `C:\msys64\...` and `C:\Users\a7med\...` literals.
Acceptance: `git grep -nE "C:\\\\Users\\\\a7med|msys64|D:\\\\Projects\\\\_SIR\\\\_quarantine" -- src` prints nothing; tests pass.

**7. Make the dry-run clean fast and honest.**
Files: `care/cleaner.py`, `care/safe_clean_orchestrator.py`, `ops_ui/routes_extended.py`, `ops_ui/routes_space.py`, `ops_ui/static/index.html` (the "Dry Run Clean" button).
Change: scan once (one `os.scandir` walk, one `stat` per file, resolve each root once), apply the same minimum-age rule in dry-run and live run, cache the dry-run report for 5 minutes, and run it as a background job: POST returns `{job_id}` in under 200 ms, `GET /api/jobs/<id>` returns progress and result. In the UI show a skeleton, a progress line ("scanned 41,000 files") and a Cancel button.
Acceptance: `time curl -X POST .../api/care/clean-dry-run` (with token) returns in under 1 s; the job finishes in under 40 s on this machine; screenshot of the progress state at 390 px in `docs/screenshots/r16/clean-progress-390.png`.

**8. Tell the truth about live clean.**
File: `care/safe_clean_orchestrator.py` (live "Step 1 direct purge"), UI text for Space Clean.
Change: either route files larger than 50 MB through quarantine, or show a plain line in the confirm sheet: "Caches are deleted for good. Installers in Downloads go to quarantine and can be restored." The Undo button must be disabled and labelled when nothing was quarantined.
Acceptance: a unit test with `tmp_path` proves a large file is quarantined and a small cache file is not; text appears in the UI (screenshot).

**9. Identity check fails closed off-loopback.**
File: `ops_ui/server.py` `_user_ok`.
Change: if the Host header is not loopback (`127.0.0.1`, `localhost`) and `Tailscale-User-Login` is missing, return 403. Keep loopback working without the header. Add tests for both.
Acceptance: `curl -s -o /dev/null -w "%{http_code}" -H "Host: ahmed.tail9e9aa7.ts.net:8765" http://127.0.0.1:8765/api/health` prints `403`; the same with header `Tailscale-User-Login: a7medorabe7@gmail.com` prints `200`; plain `http://127.0.0.1:8765/api/health` prints `200`.

**10. Console windows: the two leftovers.**
Files: `D:/Projects/_SIR/scripts/deliver/send-telegram.mjs` line 63 (`execFileSync('powershell', ...)`): add `windowsHide: true`. Create `D:/Projects/_SIR/scripts/run-node-hidden.vbs` (copy the pattern of `D:/Projects/_SIR/scripts/run-refresh-hidden.vbs`) and re-register the Task Scheduler task `SIR_Reminder_Claude_Reset` so its action is `wscript.exe //B //Nologo run-node-hidden.vbs <args>` instead of `node.exe` (use `schtasks /Change` or `Set-ScheduledTask`; keep trigger and arguments the same).
Acceptance: `Get-ScheduledTask SIR_Reminder_Claude_Reset | % { $_.Actions.Execute }` prints `wscript.exe`; `git grep -n "execFileSync" -- D:/Projects/_SIR/scripts/deliver` shows `windowsHide: true` on every call. Run `schtasks /Run /TN SIR_Reminder_Claude_Reset` only if the message text is harmless; otherwise skip and say so.

**11. Write the two missing documents.**
Files: `docs/THREAT_MODEL.md`, `.sir/evidence/rag-eval.md`, `.gitignore`.
Change: threat model with real content from this code (assets, trust boundaries: loopback, Tailscale serve, Host/Origin/token checks, quarantine, game mode kills processes; what may leave the machine: nothing private; top 8 threats with mitigation and test name). RAG eval: 20 Arabic and 20 English questions with expected source file, run by `tests/test_rag_bilingual_eval.py` logic, record real scores (do not invent; if Ollama is down, say "not run" with the reason). Add `.sir/disk_watcher_state.json` to `.gitignore`.
Acceptance: both files exist and are linked from `README.md`; `git status --short` is clean after commit.

## Part B: at least 10 visible improvements (each with a screenshot or command as proof)

**B1. Real Arabic.** Extract every static UI string from `index.html` into `static/i18n/en.json` and `static/i18n/ar.json`; use `data-i18n="key"` on each label; `toggleLanguage()` loads the JSON and swaps text. Test: `tests/test_i18n_parity.py` fails if a key is missing in either file or if any `data-i18n` key is unknown. Proof: screenshot of Health and Startup tabs in Arabic at 390 px, `docs/screenshots/r16/ar-health-390.png`, with fewer than 10 visible English labels (technical names such as CPU and file paths are fine).

**B2. Split the monolith.** Move CSS to `static/css/{tokens,layout,components,rtl}.css` and JS to `static/js/{api,state,views-*.js,i18n}.js` (ES modules), each file under 300 lines, `index.html` under 300 lines. `static_serving.py` must serve them with correct types and ETag. Proof: `wc -l src/sir_laptop_manager/ops_ui/static/index.html` prints under 300; all tabs still load with no console errors.

**B3. Replace `window.confirm` with an in-page confirm sheet** (lines about 5285, 6175, 6379): a `<dialog>` that opens from the clicked button (scale from the trigger, 180 ms spring), names the exact action and target, has a Cancel button focused by default and a red confirm button apart from it. Proof: `grep -c "window.confirm" index.html js/*.js` prints 0; screenshot of the sheet at 390 px.

**B4. Five states on every tab.** Each tab shows a skeleton that matches the final layout while loading, an empty state with one action, an error state with Retry that re-runs the failing request, and the populated state. Proof: a Playwright or devtools script `scripts/states_check.mjs` forces each state by intercepting fetch and saves 4 screenshots per tab at 390 px into `docs/screenshots/r16/states/`.

**B5. Health tab: real sparklines, no decoration.** CPU, RAM, disk free as 24-hour sparklines drawn from the stored telemetry in `/api/telemetry/history` (or the existing history endpoint); show min, max and last value as text; if there are fewer than 12 points show "Collecting data, N of 12 samples" instead of a fake line. Proof: screenshot at 1280 px.

**B6. Disk space card with a runway estimate.** From the stored C: and D: free-space samples compute GB per day (linear fit over the last 7 days) and show "At this rate C: is full in N days" only when at least 3 days of samples exist; otherwise show "Not enough history yet". Add a unit test with synthetic samples. Proof: unit test output plus screenshot.

**B7. Game Mode card.** Show the state in plain words (Idle, Playing: <game>, Services paused: list), the list of services that will be paused with a per-service toggle saved to `.sir/game_mode_config.json`, a "Preview what would be paused" button (dry-run) and a visible Undo button wired to `/api/game-mode/undo`. Proof: screenshots in idle and in dry-run preview state at 390 px and 1280 px.

**B8. Command palette (Ctrl+K).** A dialog listing every tab and every safe action (refresh, dry-run clean, verify backups, language, theme); arrow keys and Enter work; opens with a 160 ms scale and fade; respects `prefers-reduced-motion`. Proof: screenshot at 1280 px; `tests/test_ops_ui_a11y.py` extended to assert the dialog has `aria-modal` and a labelled input.

**B9. Touch targets and 320 px layout.** Every button and link at least 44 by 44 px on widths under 768; stat tiles use a 2-column grid at 320 px with a value-over-label layout; fix the `.btn-accent` on the RAG tab that extends past the viewport. Proof: a script measures all `button, a, [role=tab]` rects at 320 px and prints `0 under 44`, and `document.documentElement.scrollWidth == innerWidth` on every tab at 320, 390, 768, 1280 and 1920; screenshots at all five widths of the Health tab in `docs/screenshots/r16/widths/`.

**B10. Daemon health banner shows facts that can change.** Show uptime as a live counter, last 3 log lines from `/api/daemon/log?tail=3` (new read-only route, last 3 lines of `.sir/daemon.log`), and the time of the last successful disk check. Remove any line that is a constant string. Proof: screenshot at 1280 px and a test for the route.

**B11. Brand token decision.** `.sir/DESIGN.md` says seed `#475569`, the UI uses emerald `#10b981`. Pick one, write it in `DESIGN.md` as named CSS custom properties (`--brand`, `--brand-hover`, `--on-brand`), and make the CSS use only those tokens for primary buttons and active tab; check WCAG AA contrast of text on the brand colour in light, dark and high-contrast themes. Proof: a table of the three contrast ratios in `.sir/evidence/r16-laptop.md`.

**B12. Quarantine screen: batch actions.** Table with search, sort by size and age, multi-select with "Restore selected (dry run first)" and "Purge older than N days (dry run first)", showing the exact byte total before confirming. Proof: screenshot at 1280 px with 3 rows selected.

**B13. Route modules renamed by feature.** `routes_cycle7.py` to `routes_telemetry.py`, `routes_cycle8.py` to `routes_dispatch.py`, `routes_cycle10.py` to `routes_gamemode.py`, updating imports and tests. Proof: `ls src/sir_laptop_manager/ops_ui | grep cycle` prints nothing; verify passes.

**B14. Unknown routes return real status codes.** `dispatch_post` unknown route returns 404 and handler failures return 4xx/5xx with `{"error": ...}`, not HTTP 200 with `success:false`; UI shows the error text in a toast. Proof: tests for 404 and for one failing handler.

## Last step
When every task above is done (or a task is impossible: write why in `.sir/CHECKPOINT.md` and skip it), update `.sir/CHECKPOINT.md` with the real numbers (tests passed/failed, latest CI run id and result), then run:

`python D:/Projects/_SIR/scripts/agy-done.py r16-laptop ok "<one line: tasks done, tests passed, CI run id and result>"`

If CI is red or any acceptance command failed, use `fail` instead of `ok` and say which.
