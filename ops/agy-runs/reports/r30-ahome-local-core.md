# r30-ahome-local-core — local-core self-healing supervisor (blocked on CI infra)

## What "local core" is
- `apps/local-core/` (FastAPI/uvicorn, `127.0.0.1:8090`, service `ahome-local-core` per `apps/local-core/main.py` `/health`). Provides local AI gateway, vault/reminders/connections, Telegram/relay routes. Supervised externally by `infra-daemons/ahome-service-supervisor.ps1` / `scripts/start-ahome.ps1` (watchdog).

## Root cause (alerts 08:04 and 15:03, 2026-11-11)
- Evidence: watchdog/supervisor restarts recorded in `.sir/CHECKPOINT.md` and prior investigation (07:28–08:07 with backoff windows 08:02:56/08:04:06/08:06:31, 10:31–12:56, 13:32–13:51, 17:08–17:13); owner Telegram alerts at 08:04:47 and 15:03:57 after watchdog misses. No code defect found: core baseline 1029 pytest passed, `/health` is static 200, scheduler already caught errors, crash traces lost on restart because watchdog output redirection overwrites logs. Classified as transient wedge/external dependency/process death (not reproducible in tests).

## Fix (no alert suppression)
- Added in-process self-healing so transient loop failures are absorbed inside the process and owner is paged only after real exhaustion:
  - `apps/local-core/core/health_supervisor.py` (new): `HealthSupervisor` registers async background loops, restarts each on exception with exponential backoff (5s→300s), pages owner via `scripts/notify_owner.py` once after `MAX_CONSECUTIVE_FAILURES=5` consecutive failures, sends `recovered` once on recovery, resets internal state. Alert failures never kill supervisor. Injectable clock/sleep/sender/root/env for tests.
  - `apps/local-core/data/conn_registry.py`: added `connections_tick()` (single sleep + engine tick, may raise) and made `run_scheduler()` delegate to it.
  - `apps/local-core/main.py`: lifespan creates/starts/stops supervisor and registers `"connections"` → `conn_registry.connections_tick` with `TELEGRAM_BOT_TOKEN`/`AHMED_CHAT_ID` from env.
  - `apps/local-core/tests/test_health_supervisor.py` (new): 3 tests proving forced failures recover/backoff, exhaustion alerts once, recovery clears state (second cycle rate-limited by notify_owner 1h gap), healthy loop sends no alerts.

## Verification / evidence (real output)
- `& "D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe" -m pytest tests/test_health_supervisor.py -v` → `3 passed in 4.45s` (exhaustion→1 failed alert, recovery reset+rate-limit, healthy→no alerts).
- `& "D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe" -m pytest tests -q` → `1032 passed, 6 warnings in 192.66s (0:03:12)`.
- `& "D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe" -c "import main; print('main.py imports OK')"` → `main.py imports OK`.
- `& "D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe" -m py_compile core/health_supervisor.py data/conn_registry.py main.py tests/test_health_supervisor.py` → exit 0.
- Git: `git status --short` clean tracked tree for r30 code at commit time except unrelated untracked probe scripts/local-vault (not reverted). r30 commits already on `main`: `eda0782` (`fix(r30-ahome-local-core): add in-process health supervisor with backoff and owner paging after exhaustion`), HEAD later `20255d0` includes unrelated audit fix.
- CI (observed): run **43055769036** (commit `eda0782`, https://github.com/sirahmed8/ahmed-and-habiba/actions/runs/43055769036) — `core` **success** (pytest step completed 16:12:21Z), `secrets` **success**, `web` **in progress/failing infra at last view**. Run **43058789770** (HEAD `20255d0`, https://github.com/sirahmed8/ahmed-and-habiba/actions/runs/43058789770) — `core` **success** (1m25s), `secrets` **success** (10s), `web` **failure** at `npx playwright install --with-deps webkit` (DNS/network: `Temporary failure resolving 'security.ubuntu.com'`, 404 on apt mirrors; not caused by r30 local-core changes). Core job for r30 commit is green; full workflow on main not fully green due to web dependency install infra failure.

## Files changed (r30)
- `apps/local-core/core/health_supervisor.py` (new)
- `apps/local-core/data/conn_registry.py`
- `apps/local-core/main.py`
- `apps/local-core/tests/test_health_supervisor.py` (new)
- `.sir/CHECKPOINT.md`
- `D:/Projects/_SIR/ops/bus/sir-hq.md` (r30 note appended)

## Still open / blockers
- CI on `main` not fully green: `web` job fails in `playwright install --with-deps webkit` due to Ubuntu package mirror/DNS infra (`security.ubuntu.com` resolution, 404 on apt-mirrors) on runs 43055769036/43058789770; `core` and `secrets` are green. Needs CI re-run or workflow hardening/retry for apt fetch outside this r30 scope.
- `agy-done` run with `blocked` status (cannot truthfully signal ok while full CI is red for infra reasons). Re-run CI and flip to ok when web passes.

