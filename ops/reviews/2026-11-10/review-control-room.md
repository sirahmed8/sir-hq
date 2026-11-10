# Review: SIR Control Room (2026-11-10, independent reviewer)

Code: `_SIR/plans/generate_dashboard.py` (1,282 lines) + `plans/dashboard_template.html` (2,827 lines), `scripts/serve-control-room.py` (port 8899), `scripts/refresh-control-room.py`, `ops/artifact/`, `scripts/deliver/`, `scripts/hq_autopilot.py`. HEAD at review start `5ed479b`, then `d176c93` (HQ commit, did not touch the generator, server or refresh script, so every finding below still stands). Reviewed by running the tools, calling the live server, rendering the page at 320, 390 and 1920 px, and reading code. Nothing was edited, stopped or restarted. (`python -m py_compile` created `__pycache__` folders; that is all.)

## Verdict
1. The server answers, the page renders without horizontal scroll at 320, 390 and 1920 px, there is no emoji, the Telegram sender and the small test suites pass, and the page honestly prints "artifact is waiting for republish". That is the good part.
2. The dashboard's main message is not true: the "Verified today 4 of 16" headline, the per-project "verified" texts and the 10-item "ready" checklist are typed into `generate_dashboard.py`, not read from evidence. They include invented or stale numbers and private AHome feature names, and they are already published to a claude.ai artifact.
3. The service layer is unsafe: the server hands out the whole `_SIR/ops` folder (including a private person's email, owner actions and AHome reports) with no identity check, and 4 to 9 copies of the server run at once and refresh the page every 1 to 2 minutes. The local site and the published page differ and can never match with the current hash design.

## Commands run (exact) and results
| Command | Result |
|---|---|
| `curl http://127.0.0.1:8899/` | 302 to `/dashboard.html`, 200, 298 KB. `/health` 200 JSON. |
| `curl` of `/OWNER_ACTIONS.md`, `/bus/sir-hq.md`, `/control-room-server.log`, `/ACCOUNT_LEDGER.md`, `/PORTFOLIO.md`, `/agy-runs/`, `/locks/` | all 200 (directory listings on). `Host: evil.example` also 200. `..%2f` traversal 404. |
| `python -m py_compile` of serve, refresh, generate, autopilot, queue-add | ok |
| `python scripts/test_agy_chooser.py` | 8 tests OK |
| `python scripts/test_sync_quota_ledger.py` | 5 tests OK |
| `node --test scripts/deliver/send-telegram.test.mjs` | 6 of 6 pass (mock server) |
| `node scripts/deliver/test-format-briefing.mjs` | "All 3 test suites passed" |
| `python scripts/audit_control_numbers.py` | exit 0, but prints 19 `!=` lines (see M2, H5) |
| `test_purge_locks.py`, `test_backup_offsite_encrypted.py` | not run (they touch locks and backups; I did not want any side effect) |
| ruff, mypy, tsc, eslint | none defined for `_SIR`. No tests exist for `generate_dashboard.py`, `serve-control-room.py` or `refresh-control-room.py`. |
| Browser checks | 390 px: no horizontal scroll (`scrollX` stays 0 after `scrollTo(300,0)`), 22 of 73 controls under 44 px. 320 and 1920: no horizontal scroll, content max width 1240 at 1920. 0 emoji, 10 em-dashes in the rendered HTML. |
| `Get-CimInstance Win32_Process` for `serve-control-room.py` | 4 processes at 04:30, 9 later in the session. |
| `Get-ScheduledTask` | see H6 and H7. |

## Claims table
| # | Claim (source) | Result | Evidence |
|---|---|---|---|
| 1 | Page shows true per-project status, "Verified today 4/16" (page, plan) | not working | Statuses come from the `PROJECT_TRUTH` dict (`generate_dashboard.py:69-137`), with `verified_today: True`, dated 2026-11-09, "verified by Control Room auditor (Round 9)". Nothing reads an evidence file. |
| 2 | Local site and published page show the same content | not working | `ops/artifact/PUBLISHED.txt` = `735c2a2d` (written 2026-11-09 09:06); current hash differs; 101 "OUT OF SYNC" and 0 "IN SYNC" lines in `control-room-refresh.log`. I did not download the 300 KB artifact; the hash comparison is the evidence. |
| 3 | Refresh every 15 minutes (server, task) | not working as stated | Log shows runs every 1 to 2 minutes (04:24, 04:26, 04:27, 04:28) because several server copies and the scheduled task each refresh. |
| 4 | Detached daemon survives without any AI tool (round 13) | partly | Runs from Task Scheduler at logon (no IDE needed), but no restart on failure and duplicates (H1, H6). |
| 5 | `/health` reports health (plan, health JSON) | partly | Always returns the string "healthy" (`serve-control-room.py:140`). |
| 6 | Models on page are current (owner complaint) | cannot verify | `ops/MODELS.json` is typed by hand ("checked 2026-11-09", no source); generator only blocks a short list of old names (`generate_dashboard.py:1239-1254`) and contains a second hard-coded fallback (`:679-682`). I have no live source to compare "Gemini 3.8 Flash High". |
| 7 | AHome shown as counts and status only (plan rule 1) | not working | Page contains "partner summary consent switch", "12 Arabic notification channels", "941 tests", "944 files" (`:110-116`) and a 10-line private task list including "Friends Mode camouflage cloak wording" (`:830-841`). No string "habiba" appears (the guard at `:1256-1263` works for that one word only). |
| 8 | Handover checklist 7 of 10 ready (page) | not working | Hard-coded statuses (`:877-978`). "Silent subprocesses: zero console popup" is false (H7). "Tailscale endpoints verified from iPhone" while `tailscale status` shows the iPhone offline 16 h. "countdown 14 days" is a literal (`:992`). |
| 9 | Telegram sender works | verified | 6 of 6 mock-server tests today. I did not send a real message. |
| 10 | Briefing formatter | verified | test suites pass. |
| 11 | Telegram approvals: once, within 24 h, created by the system (plan rule 4) | partly | `telegram-inbox.mjs` accepts only the owner chat id and removes the buttons after a press; `approval.py` has no expiry and does not check that the id was system-made. |
| 12 | Print stylesheet, high contrast, content-visibility (cycle 3) | partly | Present in the template (`@media print` 1, high-contrast 2, `content-visibility` 1); not rendered or tested by me. |
| 13 | Autopilot queue and runners (HQ commit) | partly | `SIR_HQ_Autopilot` task is running; code uses `CREATE_NO_WINDOW` on every child; queue file valid. I did not wait for a runner. |
| 14 | Server binds loopback only; phone via tailnet (plan rule 6) | verified (bind) | `HOST = "127.0.0.1"`; `tailscale serve status` proxies 8899. The proxy makes the folder listing reachable by every tailnet device (C1). |
| 15 | No emoji, no private word "habiba" in the page | partly | 0 emoji, 0 "habiba". 10 em-dashes (copy rule says none). |
| 16 | Dashboard numbers traced to files (plan M1) | not working | `audit_control_numbers.py` exits 0 with 19 mismatches and compares equal strings as different; task counts for Laptop Manager (44/42 vs 34/32) and AHome (158/110 vs 92/72) disagree between tools. |
| 17 | Works at every screen size | partly | 320, 390, 1920 no horizontal scroll. 768 and 1280 not rendered by me. 22 of 73 controls under 44 px at 390. |

## Defects

### Critical
**C1. The whole `_SIR/ops` folder is public to the tailnet and to any local web page.**
`scripts/serve-control-room.py:106` serves `directory=OPS_DIR`; the handler (`:104-173`) has no Host check, no IP check, no use of the `Tailscale-User-Login` header, and directory listing is on. Reproduce: `curl http://127.0.0.1:8899/OWNER_ACTIONS.md` (200), `/bus/sir-hq.md` (37 KB), `/control-room-server.log`, `/agy-runs/` (listing), and with `-H "Host: evil.example"` (200, so DNS rebinding works from any browser tab). `tailscale serve` proxies `https://ahmed.tail9e9aa7.ts.net:8899` to it, so every device in the tailnet can read it. 184 files in `ops/` mention AHome or the private repo name, and `ops/agy-accounts-usage.md:63` holds another person's personal email address (the file is also tracked in the `sir-hq` repo). `ops/agy-runs/cli-r14-ahome.log:745` contains an AHome source line with a Firebase web key. Fix: serve a whitelist of exactly 4 files (`dashboard.html`, `favicon.*`, `manifest.json`, `health`) from a separate `ops/public/` folder; disable listing; require loopback IP and a Host in an allow-list; move private folders out of the served root; remove the email from `agy-accounts-usage.md` and from git history of `sir-hq`.

**C2. The headline "verified today" and the AHome detail on the page are typed in, and already published outside.**
`plans/generate_dashboard.py:69-342` (`PROJECT_TRUTH`) sets `status: "verified"`, `verified_today: True` for Study, Jobs, AHome and Laptop Manager with texts such as "38 pytest tests passing, GitHub Actions CI passing" (Laptop Manager), "941 test suite passing 100%", "0 leaks across 944 files", "Verified live in browser on port 3300 (sad.html)". The same page shows CI "failure" for AHome and Laptop Manager (from `gh run list`), and the Laptop Manager reviewer found 20 of 207 tests failing. Dates are 2026-11-09, not today. Lines `:830-841` print a hard-coded list of private AHome tasks ("Friends Mode camouflage cloak wording refinement", "voice recording", "messaging UI"). The rule says AHome appears as counts and status only and nothing private goes to an artifact; `ops/artifact/control-room.html` carries all of it. Fix: delete `PROJECT_TRUTH`; derive status from an evidence file per project (`.sir/evidence/verified-YYYY-MM-DD.json` written by a reviewer with command, exit code, date); "verified" only if the file is dated today; AHome row = name, status word, task counts, nothing else; add a test that renders the page from a fixture and fails on any AHome task or note string.

### High
**H1. Several copies of the server run at once.** 4 `pythonw.exe serve-control-room.py` processes at 04:30 (PIDs 34548, 17676, 29260, 4756), 9 later; the server log shows each one printing "listening successfully" on 127.0.0.1:8899. On Windows `HTTPServer` sets `SO_REUSEADDR`, which lets several processes bind one port, so requests go to whichever copy the OS picks. Each copy also runs its own refresh loop (`:198-209`) and heartbeat writer (`:212-216`), so the health file shows only the last writer's pid, `dashboard.html` is rewritten by competing processes, and the page regenerates every 1 to 2 minutes. Cause: no single-instance guard; `dev-start.vbs` and the task spawn a new copy every time. Fix: take an exclusive lock (`msvcrt.locking` on `ops/control-room.lock` or a named mutex) at start and exit if held; set `allow_reuse_address = False` on the server class; kill nothing by hand, let the next start fix it.

**H2. The published page can never match the local page.** The content hash (`generate_dashboard.py:1223-1231`) includes `git_hash`, the log and `active`, so it changes every few minutes; `PUBLISHED.txt` is a manual step and still holds `735c2a2d` from yesterday 09:06. Result: 101 "OUT OF SYNC", 0 "IN SYNC" in the log, and `notify_hq_artifact_outdated` keeps writing to the HQ bus. Fix: hash only the rendered owner-visible text without git hash and timestamps; write `PUBLISHED.txt` from the publish step itself; show "published N hours ago" on the page; or drop the artifact and make the tailnet page the single view.

**H3. Invented or stale numbers and states on the page.**
- "Working now" comes from `ops/active.json` (last written 2026-11-09 00:33): Study shows "Cycle 4 complete", the repo is at cycle 8.
- `remote_access` (`:1174-1211`) says "SAD Exam Cram Capsule (Today 11:30 AM Cairo)" with a `sad.html` link; the SAD exam was 09/11.
- `handover_countdown_days: 14` (`:992`), `archived_count()` fallback `31` (`:552`), checklist statuses (`:877-978`), `chk-model` text naming one model, are literals.
- `ops/MODELS.json` is hand-typed ("checked 2026-11-09"); nothing refreshes it, which is how the owner saw old model names.
Fix: every number must name its source file and age; if the source is older than 24 h show "stale, N h" in amber text; delete literals or move them to `ops/config.json` with a `checked` date and a visible age.

**H4. `/health` and the refresh loop lie.** `serve-control-room.py:140` returns `"status": "healthy"` unconditionally; `:205-206` ignores the return code and logs "Successfully executed" even when the generator crashes; no timeout on `subprocess.run`, so a hung generator stops refreshes forever with a green health file. Fix: record `last_refresh_ok`, `last_refresh_time`, `last_error` and make `/health` return 503 when the last good refresh is older than 30 min.

**H5. No tests for the thing that matters.** No test covers the generator, privacy fence, "verified needs evidence", server whitelist or refresh. Plan tasks 2 to 4 and 8 are not done. `audit_control_numbers.py` exits 0 on 19 mismatches and flags equal states as different ("in sync" vs "in sync (dirty: 1 files)"). Fix: `tests/test_dashboard.py` (privacy fixture, verified-needs-evidence, stale source marker), `tests/test_server.py` (whitelist, Host, listing off), make the audit script exit 1 on a real mismatch.

**H6. Server and refresh tasks do not recover.** `SIR_ControlRoom_Server`: logon trigger only, `RestartCount=0`, action is `wscript dev-start.vbs` which exits at once, so the task is "done" and nothing restarts a dead server; Interactive logon type. `SIR_ControlRoom_Refresh` repeats every 15 minutes in addition to the loop inside the server (double work). `dev-start.vbs` prefers `C:\msys64\ucrt64\bin\pythonw.exe` over the user Python 3.14. Fix: add a 5-minute repeat trigger to the server task that runs the launcher with the lock from H1; delete the refresh task or the in-server loop; pick one interpreter path from a config file.

**H7. Console windows still flash.** Scheduled tasks run console programs directly: `SIR_Reminder_Claude_Reset` runs `node.exe ...send-telegram.mjs`, and `AgentsRoom Wake` runs `cmd.exe /c exit` (AgentsRoom was retired on 2026-11-08). The checklist item "zero console popup" (`:898-907`) is therefore false. `check_ci_runs.py`, `check_git_hashes.py`, `audit_control_numbers.py`, `agy-worker.py:30` call `subprocess.run` without `CREATE_NO_WINDOW` (manual scripts, but they flash when launched from a task). Fix: wrap the two tasks with `wscript //B run-hidden.vbs`, delete `AgentsRoom Wake`, add `creationflags` to the four scripts.

### Medium
**M1. Single-threaded server.** `RobustHTTPServer(HTTPServer)` (`:188`) is not threaded: one stalled connection blocks every other request. Use `ThreadingHTTPServer` with `daemon_threads = True` and a socket timeout.

**M2. Number tracing is unreliable.** Task counts differ between the dashboard and the audit tool (Laptop Manager 44/42 vs parsed 34/32; AHome 158/110 vs 92/72). `parse_tasks` (`:396-416`) only counts headings it knows; the audit script counts differently. Pick one parser, put it in a module, test it on a fixture.

**M3. Size and structure.** `generate_dashboard.py` 1,282 lines, template 2,827 lines (298 KB output, three copies tracked in git: `dashboard.html`, `artifact/control-room.html`, `CHANGED.txt` show as modified in `git status` every few minutes). One-shot patch scripts remain (`update_dashboard_js_r11.py` 376, `update_dashboard_r11.py` 259, `polish_r11_ui.py` 151, `make-r10.py`, `make-r11.py`). Split into `data/`, `render/`, `privacy/`; untrack generated files; archive the patch scripts.

**M4. Silent fallbacks hide failures.** `git_sync_status` returns "in sync" on any exception (`:392-393`); `get_ci_status` shows `none` when `gh` times out after 5 s (`:610-629`), which reads as "no CI"; `json.load(status.json)` (`:1021`) is unguarded, so one bad project file stops the whole refresh (and the old page stays up without any sign). Return "unknown", show it, and skip only the broken project.

**M5. Invented status by substring.** `translate_log_entry` (`:633-669`) maps any log line containing "SIR Laptop Manager" to "all Python tests passed 100 percent, hardware monitor stable", and "SIR Jobs" to "automated checks stable". A log line saying a test failed would still print that. Remove the substring rules; show the log line as written.

**M6. Unlocked write to the HQ bus.** `notify_hq_artifact_outdated` (`:713-736`) reads and rewrites `ops/bus/sir-hq.md` while other agents append to it. Use append mode or a lock, and stop adding the notice every run.

**M7. Small touch targets and hidden drawer width.** 22 of 73 controls are under 44 px at 390 px. The closed settings drawer extends to x=439 at a 390 px viewport, so `document.scrollWidth` reads 474; use `inert`, `visibility:hidden` or `display:none` when closed.

**M8. Approval flow gaps.** `scripts/deliver/approval.py` has no 24 h expiry and no check that an approval id was created by the system; `telegram-inbox.mjs` ties answers to the owner chat id and removes the buttons (good) but never rejects an old id. Plan rule 4 asks for both.

### Low
**L1.** Tailnet hostname and IP are hard-coded in 15 places (`ahmed.tail9e9aa7.ts.net`, `100.85.112.10`); read them from one config.
**L2.** 10 em-dashes in the rendered page (copy rule: none), for example the Arabic name "غرفة التحكم — المقر".
**L3.** `control-room-server.log` and `control-room-refresh.log` have no rotation; every refresh adds 3 lines.
**L4.** `restore-finish.ps1` and `restore-misplaced.ps1` refer to `$L\AI_Models_Hub` under `SIR Controller\legacy\SIR Optimizer`; no `D:\AI_Models_Hub` literal exists anywhere in `_SIR` (good), but archive these one-shot scripts.
**L5.** `ops/briefs/PASTE_AHOME_4.txt` is untracked and named after the private project; make sure it holds no private text before the next commit.
**L6.** Plan item "older Control Room mod does not exist" is still a documentation gap (`plans/sir-control-room.md` section 2).

## What works (keep)
Windowless launchers and `CREATE_NO_WINDOW` in the generator, refresh script and autopilot; Telegram sender and briefing tests; owner-chat-only inbox; no emoji; no horizontal overflow at 320, 390 and 1920 px; the page prints its own out-of-sync state; the forbidden-string guard for "habiba" and for old model names.
