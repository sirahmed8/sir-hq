# PC cleanup dry run (Phase 2.4), 2026-10-29
Read-only. Nothing was deleted, moved or modified. Raw scripts and output: C:\Users\a7med\AppData\Local\Temp\claude\D--Projects\a88d4504-2da6-5bca-a167-e244d71ec42c\scratchpad\pc\
Free space at start: C: 14.47 GB, D: 14.60 GB. DISM could not run (error 740, needs elevation; not elevated per rules).
Sizes are GB (2^30 bytes), 3 decimals.

## 1. Temp folders
| Item | GB | Safe to clear automatically | Why |
|---|---|---|---|
| %TEMP% = %LOCALAPPDATA%\Temp (same folder, counted once) | 2.067 | yes, after closing apps | Regenerable temp data |
| - Temp\WinGet | 0.912 | no | WinGet staging; may hold an install in progress |
| - Temp\test-mcp | 0.105 | yes | 13,065 test files |
| - Temp\tmpeg8ef2tt, tmpymyvylml, tmpk4e9mko7 | 0.068 each | yes | Python temp dirs |
| C:\Windows\Temp | 1.232 | no (system path) | Windows-owned |
| - C:\Windows\Temp\ampe.iso | 0.870 | no, needs Ahmed | Unknown origin ISO |
| - C:\Windows\Temp\*.evtx | 0.02 each | no | Windows-owned event logs |

## 2. Package-manager caches
| Item | GB | Safe | Why |
|---|---|---|---|
| npm cache (C:\Users\a7med\AppData\Local\npm-cache) | 3.133 | yes (npm cache clean) | Regenerable; _npx is 2.768 GB, 181,098 files |
| - npm-cache\_cacache | 0.364 | yes | Regenerable |
| pnpm store (...\pnpm\store\v11) | 0 | n/a | Path does not exist |
| yarn cache | 0 | n/a | Yarn not installed |
| pip cache | 0.029 | yes | Regenerable |
| NuGet packages (C:\Users\a7med\.nuget\packages) | 0.532 | no | Restore cache needed by builds offline |
| NuGet http-cache | 0.134 | yes | Regenerable |
| Gradle, Cargo, rustup | 0 | n/a | Not present |
| Playwright browsers (AppData\Local\ms-playwright) | 0.701 | no, IN USE | chromium-1248 and chromium_headless_shell-1248 match Playwright 1.64.1 (npx cache and n8n nested copy). chromium-1234 (n8n top-level playwright-core 1.62.1) is not installed. Keep 1248, ffmpeg-1013, winldd-1007. |

## 3. node_modules outside the active list
| Item | GB | Safe | Why |
|---|---|---|---|
| D:\Projects\old projects\SIR Tele Gateway\node_modules | 0.278 | yes | Regenerable; retired project |
Only one node_modules exists outside the active list. Active-project node_modules total about 11.6 GB; not proposed.
Note: D:\Projects\AHome is a junction to AhmedAndHabiba; excluded from totals to avoid double counting.

## 4. Build output under D:\Projects
33 real folders, 4.951 GB total (false hits inside .venv and out\_next, 0 GB, excluded).
| Item | GB | Safe | Why |
|---|---|---|---|
| Obour Academic Hub\.next | 0.586 | yes, after dev servers stop | Regenerable |
| 11Players\.next | 0.582 | yes, after dev servers stop | Regenerable |
| Odysseus app\dist | 0.580 | no, check | Holds win-unpacked app and Installer.exe |
| AhmedAndHabiba\apps\web\.next (AHome is same folder) | 0.466 | yes, after dev servers stop | Counted once |
| EGFootball5\.next | 0.417 | yes, after dev servers stop | Regenerable |
| SIR Content Creation Studio\dist | 0.402 | no, check | Holds release installers |
| Negm Furniture\.next | 0.295 | yes, after dev servers stop | Regenerable |
| SIR Optimizer\PulseTools-Web\.next | 0.220 | yes | Regenerable |
| SIR ModPack\website-next\.next | 0.193 | yes | Regenerable |
| Merged sites\.next | 0.191 | yes | Regenerable |
| SIR Pharmacy\dist, SIR Library\dist | 0.161 each | no, check | May hold shipped installers |
| SIR Mods for GTA V\web-portal\.next | 0.139 | yes | Regenerable |
| SIR Controller\web\.next | 0.082 | yes | Regenerable |
| Other 16 folders | under 0.005 each | no, low value | Not worth the risk |

## 5. Crash dumps
| Item | GB | Safe | Why |
|---|---|---|---|
| C:\Windows\Minidump | 0 | no (system) | Empty |
| AppData\Local\CrashDumps | 0 | yes | Empty |
| C:\ProgramData\Microsoft\Windows\WER | 0.001 | no (ProgramData rule) | Not touched |

## 6. Recycle Bin (own SID)
| Item | GB | Safe | Why |
|---|---|---|---|
| C:\$Recycle.Bin\<own SID> | 0.016 | no, needs Ahmed | Personal |
| D:\$Recycle.Bin\<own SID> | 0.121 | no, needs Ahmed | Personal |

## 7. Windows Update leftovers
| Item | GB | Safe | Why |
|---|---|---|---|
| C:\Windows\SoftwareDistribution\Download | 0.040 | no (system, admin) | Needs elevated Disk Cleanup |
| DISM AnalyzeComponentStore | n/a | n/a | Error 740, not run |

## 8. Downloads installers
Downloads holds 3 files, 0.004 GB. Only installer: C:\Users\a7med\Downloads\android.exe (0.003 GB, 2026-10-28). Not proposed; needs Ahmed.

## 9. Exact duplicates over 50 MB (SHA-256)
143 files over 50 MB, 24 size groups, 107 hashed, 0 hash errors, 20 duplicate sets. Surplus copies total about 7.87 GB (approximate, from 3-decimal sizes).
Most sets sit in runtime paths (Minecraft instances, release and download folders). Removing them can break launchers and download links.
| Set | Copies | Each GB | Surplus GB | Where | Proposal |
|---|---|---|---|---|---|
| SIR Modern.zip (resource pack) | 33 | 0.072 | 2.304 | SIR ModPack instances and SIR Package | needs Ahmed |
| SIR Market Setup 1.0.0.exe | 3 | 0.630 | 1.260 | public\downloads, public_repo, release | needs Ahmed |
| SIR Restaurant Setup | 3 | 0.383 | 0.766 | public, public_repo, release | needs Ahmed |
| watermedia_binaries-3.0.0.6.jar | 5 | 0.134 | 0.536 | SIR ModPack instances | needs Ahmed |
| SIR_Apps_Suite.zip | 4 | 0.112 | 0.336 | SIR ModPack dist and website | needs Ahmed |
| SIR Launcher.exe | 7 | 0.054 | 0.324 | SIR ModPack copies | needs Ahmed |
| physics-mod, AmbientSounds, Essential jars | 5, 5, 4 | about 0.08 | about 0.80 | SIR ModPack instances | needs Ahmed |
| Other 9 sets (Library, Pharmacy, Content Studio, Odysseus, GTA V, White_Noise.wav, website zips) | 2 to 4 | 0.05 to 0.21 | about 1.1 | various | needs Ahmed |
| ctranslate2.dll in SIR AI and Content Studio .venv | 2 | 0.055 | 0.055 | venvs | do NOT touch (runtime) |
No duplicate is proposed for automatic quarantine.

## 10. Empty folders (user areas)
| Area | Count | Why not removed |
|---|---|---|
| Desktop | 0 | n/a |
| Documents | 49 | Mostly app-created (Rockstar Social Club, FIFA 19, Codex sessions) |
| Downloads | 0 | n/a |
| D:\Projects (outside .git, node_modules) | 269 | Structural (data, logs, out\_next, .remember\logs); apps create on demand |
Proposal: none removed. Per-project breakdown not produced.

## 11. Zero-byte junk
1,650 zero-byte files in total. Most are Chromium and Social Club lock or journal files under Documents\Rockstar Games; app state, must not be moved.
Quarantine candidates (temp-type junk):
| Folder | Files |
|---|---|
| D:\Projects\SIR AI\data\audio_cache | 63 |
| D:\Projects\old projects\SIR Tele Gateway\logs | 4 |
| D:\Projects\Laptop manager\.remember\tmp | 4 |

## 12. Antigravity and Gemini data on C:
Conversation history and settings are NOT clearable. Back up first.
| Path | GB | Class |
|---|---|---|
| .gemini\antigravity\brain | 2.668 | conversation history, KEEP |
| .gemini\antigravity\conversations | 1.497 | conversation history, KEEP |
| .gemini\antigravity-cli\conversations | 0.301 | conversation history, KEEP |
| .gemini\antigravity-browser-profile | 0.233 | browser profile with logins, KEEP |
| .gemini\antigravity (scratch, plugin_data, mcp, cache, bin) | about 0.07 | settings-adjacent, KEEP |
| .gemini\antigravity\browser_recordings | 0.012 | old recordings, clearable when Antigravity is closed |
| .gemini\antigravity-cli\log | 0.022 | logs, clearable |
| AppData\Roaming\Antigravity Cache, Code Cache, GPUCache, GrShaderCache, ShaderCache, logs | about 0.42 total | caches, clearable |
| AppData\Roaming\Antigravity\User | 0.253 | settings, KEEP |
| AppData\Roaming\Gemini and gemini (Cache, Code Cache) | 0.17 each | caches, clearable |
| AppData\Roaming\Antigravity IDE (Cache, CachedData) | about 0.05 | caches, clearable |
| AppData\Local\antigravity-updater (installer.exe, pending) | 0.311 | updater leftovers, needs Ahmed |
| .antigravity-ide\extensions | 0.205 | extensions, KEEP |
| .antigravity_cockpit | about 0 | holds a credentials file; not read, not touched |
Clearable caches total about 0.62 GB, only with Antigravity closed.

## 13. Largest folders (depth 2)
C:\Users\a7med and D:\ were scanned at depth 2; no partial results.
| Rank | Folder | GB |
|---|---|---|
| 1 | D:\Games\GTAVEnhanced | 104.916 |
| 2 | D:\Games\FIFA 19 | 73.910 |
| 3 | D:\Games\Pro Evolution Soccer 2019 | 29.496 |
| 4 | D:\Games\Mortal.Kombat.Komplete.Edition | 9.248 |
| 5 | D:\Projects\AI_Models_Hub | 9.220 |
| 6 | C:\Users\a7med\.lunarclient\profiles | 7.979 |
| 7 | D:\Games\Blur | 7.315 |
| 8 | D:\Games\FrostyModManager | 5.808 |
| 9 | C:\Users\a7med\AppData\Local | 5.338 |
| 10 | C:\Users\a7med\.gemini\antigravity | 4.279 |
| 11 | C:\Users\a7med\AppData\Roaming | 4.243 |
| 12 | D:\Projects\Laptop manager | 2.319 |
| 13 | D:\Projects\AhmedAndHabiba (same as AHome) | 1.709 |
| 14 | D:\Projects\11Players | 1.458 |
| 15 | C:\Users\a7med\.lunarclient\shared | 1.389 |
Other: D:\Projects\SIR ModPack 16.4 GB; D:\Projects\AI_Models_Hub holds Ollama blobs (4.9, 1.1, 1.0, 0.9, 0.9 GB); D:\Backups 0.668; D:\Android 0.760. Laptop manager\backups\antigravity_conversations_archive_oct2026.zip is 2.208 GB (keep).

## Totals
| Category | Auto-safe reclaimable GB |
|---|---|
| 1 Temp (excl. WinGet, Windows, ISO) | 1.155 |
| 2 npm cache, pip, NuGet http-cache | 3.166 |
| 3 node_modules (old projects) | 0.278 |
| 4 build output (after dev servers stop) | 4.95 (upper bound) |
| 5 crash dumps | 0 |
| 6 Recycle Bin | 0 (needs Ahmed) |
| 7 Windows Update | 0 (needs admin) |
| 8 Installers | 0 |
| 9 duplicates | 0 auto (7.87 needs Ahmed) |
| 10 empty folders | 0 |
| 11 Antigravity caches | 0.62 |
Reclaimable without touching personal files: about 10.1 GB (1.155 + 3.166 + 0.278 + 4.95 + 0.62). The build figure is an upper bound.

## Proposed quarantine list
Zero-byte temp-type junk only (no bytes move):
- D:\Projects\SIR AI\data\audio_cache (63 files)
- D:\Projects\old projects\SIR Tele Gateway\logs (4 files)
- D:\Projects\Laptop manager\.remember\tmp (4 files)
Exact duplicates: none proposed automatically; see section 9.

## Needs Ahmed
1. Empty the Recycle Bin (0.137 GB)?
2. Decide on the 20 duplicate sets (about 7.87 GB) and whether ModPack instances and download links can share one copy.
3. C:\Windows\Temp\ampe.iso (0.87 GB): keep or delete?
4. Antigravity conversation history (brain 2.67, conversations 1.50, CLI 0.30 GB): back up before any cleanup.
5. D:\Games (about 220 GB) and .lunarclient profiles (8 GB): personal, not proposed.
6. Ollama models in AI_Models_Hub (9.2 GB) and release builds: keep or prune.
7. DISM and Windows Update cleanup: need an elevated run (not done).
8. antigravity-updater installer.exe and pending (0.31 GB): confirm.
9. Empty folders (49 Documents, 269 D:\Projects): confirm before any removal.

## Limits
- DISM not run (error 740, not elevated).
- First D:\ walk hit the 170 s budget; re-scanned by top-level folder with no partials.
- The first duplicate run was invalid (Get-FileHash missing, errors hidden). Re-run with .NET SHA-256 gave 0 hash errors; that result replaces the earlier one.
- Per-project empty-folder breakdown was not produced.
