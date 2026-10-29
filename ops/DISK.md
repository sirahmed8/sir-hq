# DISK report (2026-10-29, Phase 0.2, read-only)

| Drive | Size | Used | Free |
|---|---|---|---|
| C: | 210 GB | 197 GB (94%) | 14 GB |
| D: | 266 GB | 251 GB (95%) | 15 GB |

Rule 10: check free space before anything over 1 GB; never free space by deleting personal files (quarantine instead, Phase 2.4).

## Largest folders (GB)
**D:\ (251 GB used)**
| GB | Folder | Note |
|---|---|---|
| 198.97 | D:\Games | 79% of D:. Personal games/launchers. Phase 2.4 decides with Ahmed's list; nothing touched |
| 55.84 | D:\Projects | breakdown below |
| 0.12 | D:\$RECYCLE.BIN | |

**D:\Projects**
| GB | Folder | Reclaimable? |
|---|---|---|
| 16.86 | SIR ModPack | payload files; check what is regenerable in Phase 3 |
| 9.22 | AI_Models_Hub | Ollama models (re-pullable); keep, but point Ollama at it |
| 4.71 | SIR Market | includes node_modules 0.87 |
| 3.19 | SIR Mods for GTA V | |
| 2.90 | SIR Content Creation Studio | |
| 2.74 | SIR Restaurant | |
| 2.26 | Laptop manager | |
| 1.55 / 1.50 / 1.46 / 1.24 / 1.23 | Odysseus app / Obour Academic Hub / 11Players / EGFootball5 / AhmedAndHabiba (AHome is a symlink to it) | |

**`node_modules` under D:\Projects: about 12.6 GB in 20 folders** (largest: SIR Market 0.87, Merged sites 0.80, SIR Pharmacy / Restaurant / Library about 0.79 each, Obour Academic Hub 0.78, 11Players 0.72). Fully regenerable with `pnpm install`; deleting them in inactive projects is the first safe win (Tier 1, after snapshots, which exist).

**C:\Users\a7med**
| GB | Folder | Note |
|---|---|---|
| 44.37 | AppData\Local | children below |
| 17.63 | AppData\Roaming | children not yet measured |
| 4.92 | .gemini | Antigravity/Gemini data |
| 2.32 | .cache | |
| 0.59 | Documents · 0.58 .claude · 0.23 .android · 0.23 .bun · 0.16 .npm | |

**C:\Users\a7med\AppData\Local children**
7.99 Programs · 5.6 Google · **5.6 npm-cache (regenerable: `npm cache clean --force`)** · 4.82 Microsoft · 3.41 hermes · 3.07 Packages · 2.06 Temp (regenerable) · 1.8 uv (cache) · 1.48 Claude-Data · 0.85 Discord · 0.83 OpenAI · 0.81 Bytedance · 0.67 ms-playwright · 0.65 Python · 0.49 electron.

**Other C:** 14.35 ProgramData · 1.23 Windows\Temp (regenerable).

## Safe, regenerable candidates (nothing deleted yet)
npm-cache 5.6 + AppData Local\Temp 2.06 + Windows\Temp 1.23 + uv 1.8 + node_modules of inactive projects up to 12.6 ≈ 23 GB. Phase 2.4 (`pc-janitor`, dry run first) does the actual cleanup.

## Not yet measured (do in Phase 2.4)
AppData\Roaming children (17.6 GB), ProgramData children (14.35 GB), `C:\Users\a7med\.gradle` (path missing), build outputs (`dist`, `.next`, `build`, Android outputs) inside projects, and caches under `D:\Games`.

## Warning
Both drives are above 94% full. A build that creates a few GB (Android Gradle, emulator images, EAS local builds) can fail for lack of space. Prefer cloud builds (rule 10) and clear the safe candidates above before the first heavy build.
