# r73-laptop-ollama-single-instance — Report

Date: 2026-11-13. Worker: Devin (SWE-2 Flash). Repo: `D:\Projects\SIR Laptop Manager` (github.com/sirahmed8/sir-laptop-manager).

## Problem

Two Ollama servers were listening on the same port area: the owner's normal user server plus a second `ollama serve` spawned by SIR Laptop Manager's ops_ui (pythonw pid 7548, spotted by the local-ai teammate). The duplicate loaded a second copy of the model in RAM (~3 GB) and made local AI slower and riskier on a 24 GB laptop.

## What I found

I audited every place in the project that can start `ollama serve` or the Ollama app:

1. `src/sir_laptop_manager/startup/logon_automation.py` — `_build_services_catalog()` had an "Ollama LLM Engine" `ServiceTarget` with `launcher_type="cmd"`, `target_path="ollama"`, `args=["serve"]`. `LogonAutomationEngine._launch_service()` spawned it via `popen_hidden` with no liveness check. Note: `run_startup_sequence()` already skips services whose port is in use, but the port check is a bare TCP connect — it does not verify the listener is actually Ollama, and `_launch_service` itself had no guard.
2. `src/sir_laptop_manager/care/game_services.py` — `NON_ESSENTIAL_SERVICES` contains the same Ollama record (`launcher_type="cmd"`, `target_path="ollama"`, `args=["serve"]`). `_relaunch_service()` (game-mode resume path) spawned `ollama serve` via `popen_hidden` whenever the paused service was restored — this is the most likely source of the duplicate: game mode pauses the Ollama PID, resume spawns a fresh `ollama serve` even if the owner's own server came back in the meantime.
3. `src/sir_laptop_manager/care/console_watcher.py` only lists `ollama.exe` in a suppression set — no spawn.
4. `src/sir_laptop_manager/ops_ui/` contains no `popen`/`subprocess`/`Popen` usage at all — no hidden spawn site there.
5. `rag/` and the rest of `src/` only *call* the Ollama HTTP API; nothing else spawns the binary.

## What I changed

### New: `src/sir_laptop_manager/care/ollama_manager.py`

`OllamaServerManager.ensure_server()` implements the single-instance contract:

- Probes TCP `127.0.0.1:11434` (`is_port_listening`, 0.5 s timeout) and then `GET http://127.0.0.1:11434/api/tags` (`is_ollama_api_responding`, 1 s timeout).
- If the port is listening AND the API answers 200 → returns `OllamaServerHandle(already_running=True, started=False)`. Zero spawns.
- If the port is occupied but the API does NOT answer → logs a warning and refuses to spawn (a foreign or hung listener would make a second `ollama serve` either fail to bind or duplicate the daemon).
- If nothing answers → resolves `ollama` via `shutil.which`, spawns `[ollama, "serve"]` through `popen_hidden` (zero console window), and registers `atexit.register(self.stop_server, handle)` so a server this manager started cannot outlive the owning process.
- `stop_server(handle)` terminates only handles with `started=True` (terminate → 5 s wait → kill fallback); foreign/user-owned servers are never touched.
- `_build_ollama_env()` + `OLLAMA_ENV_KEYS` explicitly forward the owner's knobs (`OLLAMA_MAX_LOADED_MODELS`, `OLLAMA_NUM_PARALLEL`, `OLLAMA_CONTEXT_LENGTH`, `OLLAMA_FLASH_ATTENTION`, `OLLAMA_KV_CACHE_TYPE`) on top of the inherited `os.environ`. The user environment is never modified — values are only read.

### `src/sir_laptop_manager/startup/logon_automation.py`

- Ollama `ServiceTarget.launcher_type` changed `"cmd"` → `"ollama"` (comment updated to list the new type).
- `_launch_service()` handles `"ollama"` first: calls `OllamaServerManager().ensure_server()`; tracks started handles in `self._ollama_handles`.
- New `shutdown()` stops every Ollama server this engine started (foreign servers untouched). `atexit` in the manager is the backstop for process exit.

### `src/sir_laptop_manager/care/game_services.py`

- `_relaunch_service()` `"cmd"` branch: when `target_path == "ollama"` and `args == ["serve"]`, routes through `OllamaServerManager().ensure_server()` instead of a blind `popen_hidden`. Returns True when the server was reused or started; the spawned process is covered by the manager's `atexit` stop.

### New tests: `tests/test_ollama_manager.py` (9 tests)

- `test_ensure_server_reuses_running_instance_no_spawn` — the brief's required "already running → no second spawn" assertion.
- `test_ensure_server_starts_once_when_nothing_answers` — exactly one `ollama serve` spawn + atexit registration.
- `test_ensure_server_never_spawns_when_port_occupied_but_api_dead` — hung/foreign listener → no spawn.
- `test_ensure_server_no_binary_no_spawn`.
- `test_spawned_env_preserves_owner_ollama_knobs` — all five `OLLAMA_*` vars verified in the spawned env.
- `test_stop_server_terminates_only_servers_it_started`.
- `test_game_services_relaunch_reuses_running_ollama` — game-mode resume path.
- `test_logon_launch_ollama_reuses_running_instance` and `test_logon_launch_ollama_starts_and_shutdown_stops` — logon path incl. `shutdown()`.

One fix during verification: the autouse `atexit` fixture needed an `Iterator[MagicMock]` return annotation for mypy's generator check (commit d599cd6).

## Commands run and real output

```
$ uv run pytest tests/test_ollama_manager.py tests/test_logon_automation.py tests/test_round13_game_services.py -x -q
collected 23 items
23 passed in 2.31s
```

```
$ powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
[1/4] ruff format: 143 files already formatted
[2/4] ruff check: All checks passed!
[3/4] mypy: Success: no issues found in 124 source files
[4/4] pytest: 347 passed, 1 skipped in 448.44s (0:07:28)
[OK] All verification checks passed with zero errors!
```

```
$ gh run list --limit 3
completed failure "r73: single-instance Ollama server guard" Verify Quality Bar main push 43458697839 4s
```

CI fails in ~4 s with zero steps — `D:/Projects/_SIR/ops/ci-quota-exhausted.flag` is present, so per WORKER_PREAMBLE rule 18 the local verification above is the gate. Flag still present at report time.

## Commits pushed to main

- `c9f800f` r73: single-instance Ollama server guard (manager + both call sites + 9 tests)
- `d599cd6` r73: annotate atexit fixture for mypy generator check
- `76d9bde` r73: checkpoint single-instance Ollama guard
- (also `git add .sir/evidence` screenshots refreshed by earlier audit runs, committed separately before the code commit)

## Notes / recommendations

- The duplicate-server scenario is now structurally impossible from this codebase: every spawn path funnels through `ensure_server()`, which never spawns when the API answers and never spawns when the port is occupied.
- The already-running duplicate `ollama serve` (pythonw pid 7548) observed on 2026-11-13 may still be alive on the host; the fix prevents recurrence but does not kill the existing stray process. If it is still running, the owner (or an ops pass) can stop it — the new code will reuse whichever server answers on 11434.
- `run_startup_sequence()`'s bare `is_port_in_use` pre-check remains as a fast path; correctness now lives in `ensure_server()`.
- No browser was opened this round; no owner action required.
