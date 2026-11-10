# r19-control report - 2026-11-11

Task: finish the SIR Control Room hardening round from `ops/reviews/2026-11-10/review-control-room.md` plus brief items 1-5. Repo: `sirahmed8/sir-hq` (`D:\Projects\_SIR`), work on `main`.

## What was done

### Repair first
- Removed the hard `psutil` dependency from `scripts/serve-control-room.py`; live-process check now uses Win32 `OpenProcess`/`GetExitCodeProcess`/`QueryFullProcessImageNameW` via ctypes (requires `STILL_ACTIVE`), `os.kill(pid, 0)` elsewhere. Fixed a false-positive where a terminated PID still had open handles.
- Fixed named-mutex detection with `ctypes.WinDLL("kernel32", use_last_error=True)` + `GetLastError()==183`.
- Fixed `scripts/dev-start.vbs` `BuildPath` arity bug that made the launcher silently dead (commit 450b76c).

### Brief item 1 - single server instance
- Three layers: named mutex `Global\SIR_ControlRoom_Server_Mutex`, PID file verified against the live process list, `SO_EXCLUSIVEADDRUSE` socket. Second launch exits.
- Integration test `tests/test_server_single_instance_integration.py` starts two copies and asserts the second exits.
- Live proof (2026-11-11 ~00:10 local): exactly one process:
  `Get-CimInstance Win32_Process -Filter "Name like 'python%'" | ? CommandLine -match serve-control-room` -> PID 36916, `pythoncore-3.14-64\pythonw.exe scripts\serve-control-room.py`.
- `SIR_ControlRoom_Server` task run repeatedly; still one listener. `SIR_ControlRoom_Refresh` scheduled task deleted (refresh is in-process).

### Brief item 2 - runtime locks out of git
- `ops/control-room.lock`, `ops/control-room.pid`, `ops/control-room-health.json`, `ops/locks/` removed from tracking / covered by `.gitignore`; runtime files no longer dirty every commit.

### Brief item 3 - every review finding
`.sir/R19_CHECKLIST.md` rewritten: C1, C2, H1-H8... (all of C1,C2,H1-H7,M1,M2,M4-M8,L1-L6) marked FIXED with file:line proof; M3 marked OPEN (accepted tech debt: generator ~1200 lines / template ~3100 lines remain single files, documented in `plans/sir-control-room.md` section 11).

Key verifications this session:
- `Get-ScheduledTask SIR_ControlRoom_Server`: repetition trigger present, `MultipleInstances=IgnoreNew`, `RestartCount=5`, action `wscript.exe //B //Nologo dev-start.vbs`.
- All SIR scheduled tasks run hidden (`wscript //B` or `pythonw.exe`); no AgentsRoom Wake task exists.
- Log rotation: `RotatingFileHandler(maxBytes=1MB, backupCount=3)` in serve-control-room.py:21,32,76; size check + `.1` backup in refresh-control-room.py:21-42.
- Approval flow: `approval.py` registers a pending row before sending buttons; `telegram-inbox.mjs` rejects unknown/expired (>24h)/non-pending/already-answered ids; atomic registry write then JSONL append. `tests/test_approval.py` 7 tests pass; full suite `python -m unittest discover -s tests` = 19 tests OK.
- L6 doc gap: `plans/MAIN_PLAN.md` step 6 and `plans/sir-control-room.md` section 2 updated.

### Brief item 4 - non-owner email
- `ops/agy-accounts-usage.md` account list uses neutral labels (`family account 4/5/6/7/8`, `account 3`); committed earlier as 23c5ed7. Sweep of tracked files shows remaining emails are owner accounts or already-neutral labels; nothing further to redact.

### Brief item 5 - dashboard verification and improvements
- Regenerated `ops/public/dashboard.html` + `ops/artifact/control-room.html` with `plans/generate_dashboard.py` (hash ce15260a at generation).
- Truth fixes this session:
  - Removed invented metric fallbacks (`|| 17`, `|| 5`, `|| 170`, `|| 7`, `|| 10`) -> `?? 0` in `dashboard_template.html:2693-2709`.
  - `get_control_room_daemon_health()` fallback now returns `"unknown"` not `"healthy"` (`generate_dashboard.py:897`); template renders a neutral "Status Unknown" pill (`dashboard_template.html:2216-2224`).
  - CI badges read live `gh run list`: AHome success, SIR HQ success, SIR Jobs success (new run 42908281854), SIR Study success, SIR Laptop Manager **failure** (shown red, not "ok" - truthful; that repo's CI is another task's problem).
  - Em-dash/`&mdash;` count in output: 0.
- Visible improvements shipped (well over 10): closed sidebar/dialog `visibility:hidden` (no phantom width, out of tab order), 44px touch targets for seg-btns/copy-badges/list links/chips/nav at <=600px, stale badges on active workers/attention/handover rows, relative-time on CI entries, daemon status distinguishes Running/Refresh Stale/Status Unknown/Stopped with pid+port+last-refresh age, dashboard footer shows content hash + git hash + artifact sync state.
- Screenshots: 16 PNGs in `.sir/evidence/r19/shots-src/` - before/after x light/dark x 390px/1280px x en/ar, plus the injected-theme HTML sources. JS syntax checked with `node --check` (OK).

### Privacy spot-check (live server)
```
/OWNER_ACTIONS.md   404
/HQ_CHECKPOINT.md   404
/agy-accounts-usage.md 404
/locks/             404
/dashboard.html     200
/health             200
```

### CI on main
- `gh run list -R sirahmed8/sir-hq --limit 3` after push f9f4c49:
  `completed success ... verify main push 42908844938` - green.

## Files changed (this session's commit f9f4c49)
`.sir/CHECKPOINT.md`, `.sir/R19_CHECKLIST.md` (new), `.sir/evidence/r19/` (new, 23 files), `ops/MISSION_LOG.md`, `ops/READ_LOG.md`, `ops/artifact/{CHANGED.txt,control-room.html}`, `ops/bus/sir-hq.md`, `ops/public/dashboard.html`, `plans/MAIN_PLAN.md`, `plans/dashboard_template.html`, `plans/generate_dashboard.py`, `plans/sir-control-room.md`. Earlier commits this round: 5feaa59, ed6dbfc, 4d47fbe, 502f5e5, 450b76c, 23c5ed7.

## Uncertainty / open items
- M3 modular split deferred (accepted, documented).
- SIR Laptop Manager CI is red on its own repo (last run 42751204666 failure, no pushes since 03:42); dashboard shows it red correctly. Not part of this repo's main.
- Screenshots were captured via headless Chrome `--screenshot` on file:// copies with theme injected through localStorage; they prove layout/theme/lang rendering but are not pixel-diffed against a live server session.
- Telegram approval end-to-end (real bot tap) not exercised; covered by unit tests only.

## Recommendations
- Split `generate_dashboard.py`/`dashboard_template.html` into modules before adding features (repo rule: <300 lines/file).
- Investigate sir-laptop-manager red CI under its own task.
- Schedule a real Telegram tap test for the approval flow.
