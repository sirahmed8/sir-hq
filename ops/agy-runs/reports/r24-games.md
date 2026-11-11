# r24-games report - 2026-11-11

Task: games tune-up (owner-requested override of the no-touch-games rule) + game-mode automation pause rule + NVIDIA MCP registration.

## Commits

- `sir-laptop-manager` main:
  - `256da08` game mode: session marker kept for whole game, daemon auto-evaluates
  - `228cf75` chore: untrack runtime game-services snapshot, ignore it
  - `f25d822` r24: games tune-up log + checkpoint
- `sir-hq` (_SIR) main: `3ee25a9` game mode: pause every automation while a game runs
- CI: `gh run watch 42943334081` -> all steps green (ruff format, ruff check, mypy, pytest 243 passed). Earlier run 42942009631 failed on pytest because `.sir/game_services_snapshot.json` was accidentally committed; fixed by `228cf75`, subsequent runs green.

## Hardware baseline (real commands)

```
nvidia-smi --query-gpu=name,driver_version,temperature.gpu,clocks.sm,clocks.max.sm,power.limit,memory.total --format=csv
-> NVIDIA GeForce RTX 4050 Laptop GPU, 617.42, 50C, 2055/3105 MHz, 6141 MiB
WMI: i7-13650HX, 25534783488 bytes RAM (~24 GB)
Display: 1920x1080 @ 144 Hz (Win32_VideoController CurrentRefreshRate=144)
```

## Games found (D:\Games, ~199 GB)

Blur 7.4G, FIFA 19 42G, GTAVEnhanced 105G, Mortal.Kombat.Komplete.Edition 9.3G, Need For Speed Underground 1.3G, Pro Evolution Soccer 2019 30G. Launchers: Steam, Epic, Rockstar, PrismLauncher, Lunar Client. `.sir/games.json` already detects all of them for game mode.

## What changed per game

Full detail + undo in `.sir/GAMES_TUNING.md`. Summary:

- GTA V Enhanced: NVIDIA App MCP `set_game_optimization` -> `Recommended` then `Balanced` (final). settings.xml now: DLSS on (dlssQuality=1, ResScalingType=4), RT kept but cheaper (RTReflection_FullRes=false, second-bounce GI off), VSync=0, TextureQuality=0 (6 GB VRAM safe). Manual edit: `FrameLimit` 0->60 (vsync off + cap rule).
- PES 2019: NVIDIA preset `Recommended` (was UNOPTIMIZED); `sider.ini` fps.limit 0->144. Binary settings.dat NOT touched.
- FIFA 19: already OPTIMIZED in NVIDIA App; fifasetup.ini already 1080p/vsync off/quality 4; untouched.
- MKKE: already OPTIMIZED; options.ini already maxed sane; untouched.
- Blur: dxvk.conf `dxvk.maxFrameRate` 0->144 (was uncapped on a 144 Hz panel); settings.xml already 1080p/vsync off.
- NFSU: video options live inside save profiles -> deliberately untouched.

## Backups

`D:/Projects/Backups/games-2026-11-11/`: gta5-enhanced-settings.xml, blur-settings.xml, blur-dxvk.conf, mkke-options.ini, fifa19-fifasetup.ini, pes2019-sider.ini, pes2019-cpy.ini, nfsu-launcher.log, UserGpuPreferences.reg.txt.

## GPU preference + NVIDIA profiles

- `HKCU\Software\Microsoft\DirectX\UserGpuPreferences` `DirectXUserGlobalSettings`: appended 18 `<exe>;GpuPreference=2;` entries (all game exes, mod launchers, Steam/Epic/Rockstar/Prism/Lunar). Verified: re-read shows 18 `GpuPreference=2`. Original 75-byte value backed up.
- nvidia-smi cannot write per-app profiles; NVIDIA Profile Inspector is NOT installed (only empty `AppData/Local/nvidiaProfileInspector/Logs`). The NVIDIA App MCP `set_game_optimization` is the supported driver-level path and was used.

## NVIDIA MCP

- `NvAppMcpServer.exe` registered as `nvidia-app` (type local) in `~/.config/kilo/kilo.jsonc` and `~/.config/opencode/opencode.jsonc`.
- Verified over stdio JSON-RPC: initialize OK (serverInfo nvidia-app 1.0.0), tools/list = 12 tools; `nvapp_client_get_applications` returned 11 apps with OPS state; `set_game_optimization` applied successfully to GTA V, Minecraft: Windows 10 Edition, PES 2019.
- npm survey (`registry.npmjs.org/-/v1/search?text=nvidia mcp`): only unrelated packages (@purplesquirrel/nvidia-mcp = NIM AI pipelines, nimgen = FLUX image). No other trusted/free NVIDIA GPU-control MCP; recorded, nothing else installed.

## Junk cleaned (regenerable only, ~303 MB)

NVIDIA DXCache 31 MB, GLCache 27 MB, D3DSCache 128 KB, Epic `webcache_4430` 245 MB. No saves/profiles/mods/game files touched.

## Automation pause rule - implemented + verified

Project repo:
- `game_mode.py`: snapshot file now written for the whole session (even empty `[]`), `_session_active()` checks file existence, `is_game_session_active()` helper added.
- `daemon_service.py`: new `sir-game-mode` thread evaluates every 20 s -> marker no longer needs dashboard open.
- `scheduled_cleanup_runner.py`: skips while game session active.
- tests: +3 cases; 243/243 pytest green, ruff/mypy clean.

_SIR repo:
- `hq_autopilot.py`: during game mode also kills the Telegram inbox poller (pid file removed; `ensure_listener` restarts on resume). Alerts via send-telegram.mjs unaffected.
- `cli-run2.sh`: exits immediately when marker exists; whole runner tree set to BelowNormal priority via winpid.
- `telegram-inbox.mjs`: skips getUpdates while marker exists.
- `hq_manager_tick.py`, `hq_watchdog.py`, `hq_duties.py`: log `skip: game mode active`.

Verification (fake `.sir/game_mode_snapshot.json` containing `[]`):
- `python hq_manager_tick.py` -> manager_tick.log `2026-11-11 03:52:56 skip: game mode active`
- `python hq_watchdog.py` -> watchdog.log `2026-11-11 03:52:56 skip: game mode active`
- `python hq_duties.py` -> duties.log `2026-11-11 03:52:56 skip: game mode active`
- autopilot `step()`: autopilot.log `game mode active: paused`, then after marker removal `game ended: resumed`
- `bash cli-run2.sh fakegame-test ...` -> `cli-fakegame-test.log: === game mode active: runner paused 03:53`, exit 0
- Live daemon after restart: `.sir/daemon.log` `Game mode: restored` (cleared a stale services snapshot) then `Game mode: idle`; marker confirmed absent afterwards.

Side effect cleaned up: the resume test spawned two untracked runner pids and a duplicate telegram listener; both killed (taskkill /T /F on 40148, 19632; node 18700). One listener remains, pid file consistent (20516).

## Performance numbers - honest status

No game was launched this round (interactive titles; PresentMon not installed). Measurable deltas delivered instead: ~303 MB cache reclaimed, 18 GPU pins, 4 driver-level game optimizations, 3 FPS caps (GTA V 60, Blur 144, PES2019 144). To capture FPS: `nvidia-smi dmon -s pucm -d 1` while playing, or install PresentMon (`PresentMon.exe -process_name GTA5_Enhanced.exe`), or use installed Special K overlay. Documented in GAMES_TUNING.md section 11.

## Disk warning

D: 4.9 GB free (99%), C: 9.3 GB free. Moving games to external storage already sits in OWNER_ACTIONS; flagged again in checkpoint.

## Still open / unsure

- In-game FPS before/after numbers pending an actual play session.
- PES 2019 binary settings.dat and NFSU save-profile configs intentionally untouched (crash/save risk); in-game Settings.exe is the path.
- `nvapp_client_set_laptop_feature` (Battery Boost/Whisper Mode per game) exists but was not changed - left at owner defaults.
