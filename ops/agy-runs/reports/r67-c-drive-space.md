# r67-c-drive-space — Drive C: fill investigation, fix and watchdog

Date: 2026-11-12, worker: devin (continued after autopilot CLI rounds all failed on model rate limits).

## Space numbers (real readings)

| Time | C: free |
|---|---|
| 18:30 (HQ) | 9.2 GB |
| 20:40 (HQ) | 4.6 GB |
| 21:20 (HQ / watchdog) | 0.24 GB |
| 21:34 task start | ~1.3 GB (brief said ~0.25 GB; watchdog cleanup had already freed a little) |
| 22:52 watchdog | 1.2 GB |
| 23:25 after fixes | **5.30 GB** |

D: free after moving caches: 7.42 GB (was ~10 GB; D: is also tight, see Open items).

## Cause (what filled C: by ~3-4 GB/hour between 18:30 and 21:20)

Not one runaway file — a combination, all "ours" (the SIR autopilot fleet):

1. **Pagefile growth.** `C:\pagefile.sys` is 21.05 GB, system-managed (left untouched per AGENTS.md). `Win32_PageFileUsage` showed PeakUsage 7955 MB. The PC has ~24 GB RAM; `MAX_PARALLEL = 22` in `scripts/hq_autopilot.py` lets up to 22 CLI agents (node/python/kilo/cline/claude/devin) run at once. Tonight's process list showed 5+ agent runtimes plus Chrome plus games-adjacent apps; free physical memory was ~1.9 GB. Memory pressure pushed the system-managed pagefile to grow on C: — the single largest consumer and the reason free space kept dropping even after caches were cleaned.
2. **Worker caches/downloads on C:.** Every CLI worker downloaded toolchains into the user profile on C:: Playwright browsers (~0.9 GB in `AppData\Local\ms-playwright`, written 22:24-22:25), uv cache (1.0 GiB, cleaned), npm `_npx` payloads incl. workerd (~0.7 GB `npm-cache`), pnpm metadata cache, `Roaming\npm\node_modules` 7.45 GB of global CLIs, Devin `sessions.db` 1.25 GB.
3. **Transient recovery.** Free space jumped 0.0 -> 3+ GB around 22:45-22:55 while nothing was deleted by hand: the pagefile shrank back when memory pressure eased (pagefile.sys LastWriteTime 22:44) and some workers exited. Confirms pagefile + transient worker footprint as the mechanism.

Timeline proof from `ops/watchdog.log`: C: was 4.4 GB at 20:31, 3.2 GB at 21:02, 0.0-0.3 GB from 21:12 to 22:41, recovering after 22:52.

## What was checked and deliberately NOT touched

- `vssadmin list shadowstorage` — needs admin, could not run (noted).
- `C:\Users\a7med\.gemini\antigravity\conversations` (2.39 GB), `brain` (0.84 GB), `.claude` (2.06 GB), `.claude\projects` — conversation history / personal data: never touched.
- `Roaming\npm\node_modules` (7.45 GB) — installed global CLIs (kilo, opencode, etc.): deleting would break the tools; not a cache.
- `iCloud Photos Archive` (36 GB), `.lunarclient` (10 GB), games, `Windows\Installer`, `ProgramData\Package Cache` (1.13 GB, installer cache — needs admin judgment): untouched.
- `C:\Windows\SoftwareDistribution\Download` (0.77 GB): DISM `StartComponentCleanup` failed with error 740 (needs elevation). Left for owner/IT.
- Pagefile: system-managed, off limits per brief.

## Changes made

1. **Caches moved to D: (user-level env vars, current user only):**
   - `npm_config_cache=D:\Caches\npm`
   - `PIP_CACHE_DIR=D:\Caches\pip`
   - `UV_CACHE_DIR=D:\Caches\uv`
   - `PLAYWRIGHT_BROWSERS_PATH=D:\Caches\ms-playwright`
   - `npm_config_store_dir=D:\Caches\pnpm-store`
   - Set via `[Environment]::SetEnvironmentVariable(...,'User')`; verified. New processes pick them up automatically.
2. **Playwright browsers moved** `C:\...\ms-playwright` -> `D:\Caches\ms-playwright` via robocopy /MOVE (0.89 GB; source dir gone, verified).
3. **Regenerable space freed on C::** `uv cache clean --force` removed 35,679 files / 1.0 GiB; `npm-cache` (~0.67 GB incl. `_npx`), `pnpm-cache`, `uv\cache`, temp files older than 1 day, `CrashDumps` cleaned. Net C: free: 0.24 GB -> 5.30 GB.
4. **`scripts/cli-run2.sh`**: exports `TMP`/`TEMP=D:\Caches\tmp` plus the same cache env vars inside the runner, so every CLI worker round writes temp and downloads to D: even when launched by an old parent process.
5. **`scripts/hq_autopilot.py`**: `MAX_PARALLEL` 22 -> 12 (comment explains: 22 agents exhausted RAM, grew pagefile on C: to 0 bytes free). Still covers every active project.
6. **`scripts/hq_watchdog.py`**: cleanup now also purges uv and pnpm caches; Telegram warning now fires once per episode only when C: free drops **under 2 GB** (was: warned at <4.5 GB), message updated; cleanup still auto-runs under 4.5 GB every 10 min. `python -m py_compile` passes.

## Commands run (real output highlights)

- `Get-PSDrive C` series: 1.30 -> 3.44 -> 0.0-0.3 (watchdog log) -> 4.79 -> 5.30 GB.
- `Win32_PageFileUsage`: AllocatedBaseSize 21552 MB, PeakUsage 7955 MB.
- `uv cache clean --force`: "Removed 35679 files (1.0GiB)".
- robocopy ms-playwright: source `Test-Path` = False, dest 0.89 GB.
- `python -m py_compile scripts/hq_watchdog.py scripts/hq_autopilot.py`: OK; `bash -n scripts/cli-run2.sh`: OK.
- `Dism.exe /online /Cleanup-Image /StartComponentCleanup`: Error 740 (elevation required) — not done.

## Still open / risks

- **D: is also tight (7.4 GB free).** Caches now land there; if D: keeps shrinking the same problem moves. Owner decision needed on what to offload (games are his call).
- **Windows Update cache (0.77 GB) and `ProgramData\Package Cache` (1.13 GB)** need an elevated cleanup — one owner tap: run `cleanmgr` as admin or approve a maintenance window.
- **npm global CLIs (7.45 GB) and Devin sessions.db (1.25 GB)** live on C: by design of those tools; moving them means reinstalling tools — not done.
- Chrome cache (~0.6 GB) skipped while the browser is running; watchdog temp pass covers the rest.
- If C: drops under 2 GB again the watchdog now warns Ahmed once and auto-cleans; pagefile will still grow under heavy parallel load — MAX_PARALLEL=12 is the mitigation, raise only if disk stays healthy.

## Recommendation for HQ

- Consider a scheduled weekly `cleanmgr`/Storage Sense pass (needs one elevated run by the owner).
- If agents keep needing more parallelism, the durable fix is moving the pagefile or user profile caches off C: — owner decision (system settings are off-limits to agents).
