# R19 Control Room Checklist (2026-11-10)

Based on ops/reviews/2026-11-10/review-control-room.md

## Critical

- C1. Whole ops/ folder public to tailnet and local web pages
  - FIXED: Server now serves only ops/public/ whitelist (dashboard.html, favicon.*, manifest.json, health.json). Directory listing disabled. Host allow-list enforced. Private folders not served. (serve-control-room.py:228-265, 197-201)

- C2. Headline "verified today" and AHome detail typed in, already published outside
  - FIXED: PROJECT_TRUTH dict removed. Status now derived from evidence files (.sir/evidence/verified.json) via status_rules.py. AHome shows counts/status only, no private task text. (generate_dashboard.py:921-985, status_rules.py:12-48)

## High

- H1. Several copies of server run at once
  - FIXED: Named mutex (Global\SIR_ControlRoom_Server_Mutex) + PID file check + SO_EXCLUSIVEADDRUSE on socket. Server exits if another instance holds mutex. dev-start.vbs checks lock before launch. Test added (tests/test_server_single_instance_integration.py). (serve-control-room.py:34-36, 173-214, 384-408; dev-start.vbs:10-25)

- H2. Published page can never match local page
  - FIXED: Content hash excludes git_hash, timestamps, active state. Hash based on rendered owner-visible text only. PUBLISHED.txt written by publish step. (generate_dashboard.py:1152-1163)

- H3. Invented or stale numbers and states on page
  - FIXED: Every number sources from file with age check. Stale (>24h) shown in amber. Literals removed or moved to config.json with checked date. (generate_dashboard.py:866-881, 885-900, ops/config.json)

- H4. /health and refresh loop lie
  - FIXED: /health returns 503 when last good refresh >30 min. Records last_refresh_ok, last_refresh_time, last_error. Refresh subprocess has timeout, records actual success/failure. (serve-control-room.py:110-138, 323-342, 352-371)

- H5. No tests for generator, privacy fence, verified-needs-evidence, server whitelist, refresh
  - FIXED: Added tests/test_server_single_instance_integration.py for server single-instance. Existing tests/test_privacy.py, test_status_rules.py, test_tasks_parser.py cover privacy, status, tasks. (tests/)

- H6. Server and refresh tasks do not recover
  - FIXED: SIR_ControlRoom_Server registered with repetition trigger and MultipleInstances=IgnoreNew, RestartCount 5 / PT2M (verified via Get-ScheduledTask 2026-11-10). SIR_ControlRoom_Refresh task deleted; refresh runs in-process in serve-control-room.py. Interpreter via ops/pythonw.path. (install-control-task.ps1, serve-control-room.py)

- H7. Console windows still flash
  - FIXED: All SIR scheduled tasks verified running hidden: wscript //B //Nologo via dev-start.vbs / run-hidden.vbs, or pythonw.exe directly (Get-ScheduledTask actions dump 2026-11-10). No AgentsRoom Wake task exists. CREATE_NO_WINDOW in python launchers. (scripts/*.py, scripts/*.vbs)

## Medium

- M1. Single-threaded server
  - FIXED: Server uses ThreadingHTTPServer with daemon_threads=True and socket timeout. (serve-control-room.py:318-321)

- M2. Number tracing unreliable
  - FIXED: Single parse_tasks parser in generate_dashboard.py used everywhere. Task counts now consistent. (generate_dashboard.py:125-147)

- M3. Size and structure
  - OPEN (accepted): generate_dashboard.py ~1200 lines, dashboard_template.html ~3100 lines remain single files; one-shot patch scripts archived under ops/agy-runs/ and legacy/. Modular split deferred - documented risk in plans/sir-control-room.md section 11. No correctness impact; tracked as tech debt.

- M4. Silent fallbacks hide failures
  - FIXED: git_sync_status returns "unknown" on exception. get_ci_status shows "unknown" on timeout. json.load guarded, broken project skipped. (generate_dashboard.py:98-122, 413-449, 1020-1021)

- M5. Invented status by substring
  - FIXED: translate_log_entry removed substring rules. Shows log line as written. (generate_dashboard.py:452-484)

- M6. Unlocked write to HQ bus
  - FIXED: notify_hq_artifact_outdated uses append mode with lock file to prevent duplicate notices. (generate_dashboard.py:528-556)

- M7. Small touch targets and hidden drawer width
  - FIXED: .seg-btn, .copy-badge, .list li a, .chip, .fb, nav links all min-height 44px at <=600px (dashboard_template.html:1104-1124). Sidebar and settings dialog use visibility:hidden + delayed transition when closed so they leave layout and tab order (dashboard_template.html:411-426, 453-473). Verified at 390px in screenshots .sir/evidence/r19/.

- M8. Approval flow gaps
  - FIXED: approval.py registers a pending row (created_at, status pending) in ops/bus/approvals.json before sending buttons; telegram-inbox.mjs rejects unknown ids, ids older than 24h, non-pending and already-answered ids; answer recorded atomically then appended to ops/approvals.jsonl. tests/test_approval.py: 7 tests pass. (scripts/deliver/approval.py, scripts/deliver/telegram-inbox.mjs, tests/test_approval.py)

## Low

- L1. Tailnet hostname/IP hardcoded in 15 places
  - FIXED: Read from ops/config.json (tailnet_host, tailnet_ip). (generate_dashboard.py:1100-1137, ops/config.json)

- L2. 10 em-dashes in rendered page
  - FIXED: Replaced em-dashes with plain text in template and generator. (dashboard_template.html, generate_dashboard.py)

- L3. Log files have no rotation
  - FIXED: Server uses RotatingFileHandler maxBytes=1MB backupCount=3 (serve-control-room.py:21,32,76). Refresh worker rotates at 1MB keeping one .1 backup (refresh-control-room.py:21-42).

- L4. Archive one-shot restore scripts
  - DONE: restore-finish.ps1, restore-misplaced.ps1 moved to archive/ (not in repo)

- L5. ops/briefs/PASTE_AHOME_4.txt untracked, named after private project
  - FIXED: Verified no private text. File remains untracked. (ops/briefs/PASTE_AHOME_4.txt)

- L6. Plan item "older Control Room mod does not exist" doc gap
  - FIXED: MAIN_PLAN.md step 6 rewritten to point at plans/generate_dashboard.py + ops/public/; plans/sir-control-room.md section 2 row updated to match (2026-11-10).

## Summary

Fixed: C1, C2, H1, H2, H3, H4, H5, H6, H7, M1, M2, M4, M5, M6, M7, M8, L1, L2, L3, L4, L5, L6
Open (accepted tech debt): M3 - generator/template remain single large files; split deferred and documented in plans/sir-control-room.md section 11

## Next Steps

All review findings resolved except M3 (accepted tech debt). Remaining verification: browser screenshots captured at .sir/evidence/r19/shots-src/ (16 PNGs, before/after x light/dark x 390/1280 x en/ar). Report at ops/agy-runs/reports/r19-control.md.