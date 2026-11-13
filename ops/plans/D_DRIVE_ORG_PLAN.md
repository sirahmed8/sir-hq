# D: drive audit and organization plan

Date: 2026-11-13. Owner request (2026-11-13): Ahmed freed a lot of space on C: (deleted games and other things). D: must stay untouched for now. When the current build tasks finish, space will be moved from D: to C:. This document is the preparation, so that the move later is fast, safe and reversible.

Everything here is a measurement and a plan. Nothing on D: was deleted, moved, renamed or modified.

## 0. Method, guarantees and limits

- Read-only audit. The only files written by this round are this plan (`D:/Projects/_SIR/ops/plans/D_DRIVE_ORG_PLAN.md`) and the round report. Nothing else on D: was created, deleted, moved or renamed.
- C: was not touched. Its free space was only read.
- Inside `D:\Projects\AHome` only folder names and sizes were read. No file was opened and no content was printed.
- `D:\acc` (account recovery codes) and `D:\.remember` (agent memory logs) were listed by name only, never opened.
- Size method: `robocopy <folder> NUL /L /S /XJ /NJH /NDL /NC /NS /BYTES` (listing mode, nothing is copied), reading the `Bytes:` line of the summary. `/XJ` skips junctions, so no folder is counted twice through a link. Units are GiB (2^30 bytes), three decimals.
- Caveat on the folder table: robocopy counts a hard-linked file once per link, so the sum of the folder table is about 4.9 GB larger than the space the drive really uses. This is real and was confirmed on this machine: pnpm hard-links every package file from the store `D:\.pnpm-store\v11\files` into `node_modules\.pnpm` (`fsutil hardlink list` on a file in `SIR Life\node_modules\.pnpm` shows both links). Every folder number is therefore an upper bound, and the drive-level truth is the `Win32_LogicalDisk` reading in section 1.
- Earlier baselines used for comparison: `ops/DISK.md` (2026-10-29) and `ops/disk-plan-2026-11-12.md` (the cleanup that freed 14.81 GB on 2026-11-12).

## 1. Free space right now (measured 2026-11-13, 02:45 to 03:25)

| Drive | Size | Used | Free | Free share |
|---|---|---|---|---|
| C: | 210.00 GB | 192.49 GB | **17.51 GB** | 8.3% |
| D: | 265.01 GB | 212.77 GB | **52.23 GB** | 19.7% |

Source: `Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3"` and `Get-PSDrive`.

What changed since the last measurement:

| Date | C: free | D: free | Note |
|---|---|---|---|
| 2026-10-29 | 14 GB | 15 GB | `ops/DISK.md` |
| 2026-11-12 06:00 | 7.61 GB | 2.03 GB | `ops/disk-plan-2026-11-12.md`, D: was almost full |
| 2026-11-12 after the cleanup | 9.63 GB | 14.82 GB | 14.81 GB of regenerable data deleted |
| 2026-11-12 23:30 | 5.30 GB | 7.42 GB | worker caches moved from C: to D: (`ops/agy-runs/reports/r67-c-drive-space.md`) |
| 2026-11-13 02:45 (this round) | **17.51 GB** | **52.23 GB** | owner freed space on both drives |

The owner's numbers in the brief ("C: about 17.5 GB free, D: about 52 GB free") match the measurement exactly.

Two facts that decide any move:

- C: has 17.51 GB free, but the system pagefile `C:\pagefile.sys` is 13.13 GB right now and was 21 GB on 2026-11-12. Under memory pressure the pagefile grows into C:, which is how C: hit 0.24 GB free on the night of 2026-11-12. C: headroom is therefore not 17.5 GB of usable space. The safe usable budget is about **8 GB** (keep at least 9.5 GB free).
- D: also carries a system-managed pagefile (`d:\pagefile.sys` is listed in the paging-file registry), so D: free space moves with memory pressure too.

## 2. Top-level map of D:

Every top-level folder on D:, hidden ones included. `System Volume Information` and the recycle bin are listed because they exist, not because their contents were judged.

| Folder | GB | Files | Class | Verdict |
|---|---|---|---|---|
| `D:\Games` | 152.14 | 21340 | C. games, apps, media | owner decision, the biggest block on D: |
| `D:\Projects` | 62.70 (sum of children, upper bound) | about 700000 | A. SIR workspace | keep, section 3 |
| `D:\Caches` | 2.15 | 30311 | B. tool caches | keep on D: (they were moved here on purpose), clean only |
| `D:\AI_Models_Hub` | 0.41 | 16 | B. duplicate model store | owner decision, section 7 |
| `D:\$RECYCLE.BIN` | 0.12 | 43 | D. system | owner decision, personal |
| `D:\.pnpm-store` | 0.10 | 714 | B. tool cache | the live pnpm store, in use, do not touch |
| `D:\tmp-win` | 0.01 | 563 | B. temp | safe to remove later |
| `D:\temp-npm` | 0.005 | 696 | B. temp | safe to remove later |
| `D:\tmp` | 0.002 | 35 | B. temp scratch | safe to remove later |
| `D:\.sir` | 0.002 | 24 | D. unknown | evidence folder of a tool, leave alone |
| `D:\.remember` | 0.0001 | 10 | D. unknown | agent memory logs, in use |
| `D:\d` | 0.0002 | 2 | D. unknown | stray tree holding copies of two projects, owner decision |
| `D:\temp`, `D:\temp-verify`, `D:\tmp-npm` | 0.0003 | 100 | B. temp | safe to remove later |
| `D:\acc` | 0.00001 | 2 | D. sensitive | account recovery codes, never open |
| `D:\Downloads` | 0 | 0 | C. downloads target | keep, Chrome saves here |
| `D:\System Volume Information` | not readable | - | D. system | Windows owns it |

Sum of the measured folders: about 217.6 GB against 212.77 GB really used (hard-link double counting, section 0).

### 2.1 Two oddities worth a decision

- `D:\d\Projects` contains `AHome` and `SIR Hagoozat` as plain directories (not junctions, 2 files in the scan). It looks like a half-finished copy made by a script with a wrong root path. It is tiny, but it is AHome material, so it is listed and not touched.
- `D:\.pnpm-store\v11` is the real pnpm store on this machine (`pnpm store path` prints `D:\.pnpm-store\v11`). The user environment variable `npm_config_store_dir=D:\Caches\pnpm-store` set on 2026-11-12 does not control pnpm (`pnpm config get store-dir` prints `undefined`, there is no npmrc on the machine), and `D:\Caches\pnpm-store` is empty. The store that is actually in use is on D:, which is the right place, so nothing has to move. The misleading environment variable should be corrected by HQ later, not by this task.

## 3. Class A: the SIR workspace, keep it

`D:\Projects` is the working directory of every agent, every build and every repo. It is not a move candidate. Per-project sizes, measured with the same robocopy listing:

| Folder | GB | Files | Note |
|---|---|---|---|
| `SIR ModPack` | 14.98 | 73833 | 14.97 GB of it is `legacy\`, the mod payload |
| `AI_Models_Hub` | 11.68 | 81 | Ollama 11.40, whisper 0.14, `OLLAMA_MODELS` points here |
| `SIR Business` | 6.30 | 3368 | four sector apps plus legacy |
| `Android` | 5.92 | 33854 | SDK 3.85, Gradle caches 1.38, JDK 0.32 |
| `SIR Laptop Manager` | 5.38 | 93119 | active product, a pytest run was live during the scan |
| `SIR AI` | 4.30 | 127532 | active product, esbuild was running during the scan |
| `SIR Mods for GTA V` | 2.71 | 40110 | |
| `AHome` | 2.46 | 71232 | private, local only, round r71 was editing it |
| `ahome-audit-before` | 2.00 | 51636 | copy of AHome source kept for the audit |
| `Backups` | 1.64 | 2844 | protected, owner backups |
| `SIR Content Creation Studio` | 1.33 | 11088 | |
| `_SIR` | 0.90 | 7282 | this workspace and the whole HQ system |
| `SIR Controller` | 0.90 | 3507 | |
| `SIR Study` | 0.73 | 7195 | active product |
| `SIR Portfolio` | 0.59 | 14647 | active product |
| `SIR Jobs` | 0.26 | 6397 | active product |
| `SIR Hagoozat` | 0.22 | 3246 | |
| `sir-study-before-661a0d9` | 0.19 | 1891 | old copy of SIR Study at an earlier commit |
| `SIR Negm Furniture` | 0.09 | 1676 | friend project, planning only |
| `SIR Education Hub` | 0.06 | 1810 | |
| `SIR Life` | 0.03 | 812 | pnpm layout with hard links |
| `old projects` | 0.01 | 366 | never delete |
| `SIR Platform` | 0.01 | 308 | cancelled project |
| `SIR Movies`, `SIR Game Deals`, `SIR Cars`, `SIR Access Map`, `SIR Handyman`, `SIR Deals`, `SIR Price Finder` | under 0.01 each | under 100 each | planning only |
| `.agentsroom`, `.agents`, `.claude`, `.pytest_cache`, `.ruff_cache`, `.mypy_cache`, `.hypothesis`, `.remember`, `.sir`, `projects` | under 0.02 each | - | tool state, small |

Working sets that must stay in place because something points at them by name:

| Path | Pinned by | If it moves |
|---|---|---|
| `D:\Projects\AI_Models_Hub` | user env `OLLAMA_MODELS` | Ollama serves no model, the local fallback dies |
| `D:\Caches\npm`, `pip`, `uv`, `ms-playwright`, `pnpm-store`, `tmp` | user env vars plus `scripts/cli-run2.sh` | every worker round writes caches to C: again, which is what filled C: on 2026-11-12 |
| `D:\Projects\Android\jdk21` and `D:\Projects\Android\Sdk` | Java and adb processes were running during the scan | Android build breaks |
| `D:\Projects\Backups` | AGENTS.md rule (allowed location) | owner backups are lost |
| `D:\Downloads` | `SIR Laptop Manager` `care/safe_clean_orchestrator.py` | the cleanup job misses a folder |
| `D:\Projects\_SIR\_quarantine` | `SIR Laptop Manager` `ops_ui/routes_space.py`, `care/quarantine_cli.py` | the quarantine path breaks |
| `D:\.pnpm-store\v11` | hard links from `node_modules\.pnpm` in the pnpm projects | packages break until every install is repeated |

## 4. Class B: tool caches and regenerable data

| Folder | GB | What it is | Move to C: | Clean |
|---|---|---|---|---|
| `D:\Caches\ms-playwright` | 1.58 | Chromium build for the browser tests | no, it was moved off C: on purpose | safe, re-downloads |
| `D:\Caches\npm` | 0.44 | npm cache | no | safe, `npm cache clean --force` |
| `D:\Caches\tmp` | 0.13 | temp of every worker round | no | safe, temp |
| `D:\Caches\pnpm-store`, `pip`, `uv` | about 0 | empty now | no | safe |
| `D:\.pnpm-store\v11` | 0.10 | the live pnpm content store | no | no, it is in use |
| `D:\AI_Models_Hub` | 0.41 | faster-whisper model, a copy of what already sits in `D:\Projects\AI_Models_Hub` | no | owner decision, section 7 |
| `D:\Projects\Android\gradle-home` + `Android\.gradle` | 1.38 | Gradle caches | possible, needs `GRADLE_USER_HOME` repointed | safe, re-downloads |
| `D:\temp*`, `D:\tmp*` | under 0.02 | stale temp and test scratch | no | safe |

Rule from the 2026-11-12 incident: caches that the agents write to stay on D:. D: has the room (52 GB free), C: does not.

## 5. Class C: games, apps and media

| Folder | GB | Files | Note |
|---|---|---|---|
| `D:\Games\GTAVEnhanced` | 104.78 | 13033 | the single biggest thing on D: |
| `D:\Games\Pro Evolution Soccer 2019` | 29.50 | 6277 | |
| `D:\Games\Mortal.Kombat.Komplete.Edition` | 9.25 | 1314 | |
| `D:\Games\Blur` | 7.32 | 152 | |
| `D:\Games\Need For Speed Underground` | 1.29 | 563 | the only game that fits the C: budget |
| `D:\Games\Havoc.exe` | file at the folder root | - | |
| `D:\Downloads` | 0 | 0 | Chrome download target |

Since 2026-10-29 the games folder fell from 198.97 GB to 152.14 GB: `FIFA 19` (73.9 GB) and `FrostyModManager` (5.8 GB) are gone, `Need For Speed Underground` is new. The owner is already reorganizing games by hand, so nothing here is proposed without his word.

## 6. Junk inside D:\Projects (sizes only, nothing deleted in this round)

The cleanup of 2026-11-12 already removed the legacy `node_modules` (about 9.3 GB) and the legacy build outputs (about 2.4 GB). What is left is measured here so the next cleanup round starts from facts.

Regenerable, in the projects:

| Path | GB | Kind | Note |
|---|---|---|---|
| `ahome-audit-before\node_modules` | 1.70 | node_modules | part of the audit copy, goes with it |
| `AHome\apps\web\.next` | 1.09 | build output | regenerable, needs the AHome round to stop first |
| `SIR AI\node_modules` | 0.70 | node_modules | active product, a build was running, do not touch now |
| `AHome\node_modules` | 0.74 | node_modules | private, active |
| `SIR AI\legacy\SIR AI (v1)\.venv` | 0.43 | Python env | regenerable, slow to rebuild |
| `SIR Content Creation Studio\legacy\SIR Content Creation Studio (v1)\.venv` | 0.42 | Python env | regenerable, slow to rebuild |
| `AHome\apps\local-core\.venv` | 0.39 | Python env | live, four processes were running on it |
| `SIR AI\legacy\Odysseus app\.venv` | 0.38 | Python env | regenerable, slow to rebuild |
| `SIR Portfolio\node_modules` | 0.39 | node_modules | active |
| `SIR Jobs\node_modules` | 0.03 | node_modules | active |
| `SIR Laptop Manager\node_modules` | 0.02 | node_modules | active |
| `SIR Life\node_modules` | 0.02 | node_modules | pnpm layout, hard-linked to the store |
| `SIR Portfolio\.next` | 0.09 | build output | regenerable |
| `SIR AI\legacy\SIR Tele Gateway\.venv` | 0.04 | Python env | regenerable, slow to rebuild |
| `SIR Hagoozat\legacy\EGFootball5\out` and `11Players\out` | 0.04 | build output | regenerable |
| `SIR Negm Furniture\apps\web\out` and `legacy\Negm Furniture\out` | 0.02 | build output | friend project, planning only |
| `SIR Education Hub\legacy\Obour Academic Hub\out` | 0.01 | build output | regenerable |
| `SIR AI\apps\web\dist`, `SIR AI\apps\desktop\build`, `SIR Business\legacy\...\build` | 0.001 | build output | already empty |
| `SIR Study\dist`, `SIR ModPack\dist`, `SIR ModPack\website-next` | 0 | - | do not exist |

Sums that matter:

- **node_modules in the two copies that are not live projects**: about 1.70 GB (`ahome-audit-before`).
- **build output in projects nobody is working on**: about 0.16 GB (small, the 2026-11-12 cleanup already took the big ones).
- **AHome build output**: 1.09 GB, regenerable but only after the AHome round stops.
- **Python envs in finished legacy products**: 1.27 GB, regenerable but each rebuild costs minutes.
- **Gradle caches**: 1.38 GB, regenerable.
- **node_modules of the six live products** (SIR AI, AHome, SIR Portfolio, SIR Jobs, SIR Laptop Manager, SIR Study): about 1.9 GB, they stay, every build round needs them and a reinstall costs more time than the space is worth.

## 7. Ranked move plan

The owner's goal: move space from D: to C: once the build rounds are done. Two things must be true at the same time for that to be safe, so the ranking is split into two tracks.

- Track 1 frees D: without spending any C: space. Free wins first.
- Track 2 moves data from D: to C:, limited by the C: budget of about 8 GB.

### Track 1: free D: without touching C: (ranked by GB, lowest risk first)

| Rank | Folder | GB freed on D: | Risk | How |
|---|---|---|---|---|
| 1 | `D:\Projects\ahome-audit-before` | 2.00 | low | snapshot copy of AHome source made for the audit, the live repo has the same history; the owner confirms before it goes |
| 2 | `D:\Caches\ms-playwright` | 1.58 | low | regenerable, it re-downloads on the next browser test |
| 3 | `D:\Projects\Android\gradle-home` + `Android\.gradle` | 1.38 | low | regenerable Gradle cache |
| 4 | `D:\Projects\AHome\apps\web\.next` and `out` | 1.09 | low, private project | regenerable, only after the AHome round stops |
| 5 | legacy Python envs (SIR AI x3, SIR Content Creation Studio) | 1.27 | medium, slow rebuild | regenerable, last in the batch |
| 6 | `D:\Caches\npm` | 0.44 | low | regenerable, `npm cache clean --force` |
| 7 | `D:\Projects\sir-study-before-661a0d9` | 0.19 | low | old copy of SIR Study, the repo and GitHub hold the history |
| 8 | build outputs of projects nobody works on | 0.16 | low | regenerable |
| 9 | `D:\$RECYCLE.BIN` (own SID) | 0.12 | personal | owner decision only |
| 10 | `D:\AI_Models_Hub` | 0.41 | medium | duplicate of the whisper model in `D:\Projects\AI_Models_Hub`; confirm the voice pipeline first |
| 11 | `D:\temp*`, `D:\tmp*`, `D:\temp-verify` | 0.03 | low | stale temp |
| 12 | `D:\d\Projects` (stray copy) | 0.0002 | medium | AHome material, owner decision |

Track 1 without the owner-decision rows (9, 10, 12): **about 8.2 GB** of D: freed, **0 GB** of C: used. With them: about 8.7 GB.

Track 1 is not urgent, D: has 52 GB free. It is listed so the owner can run it in one pass whenever he wants D: tidier.

### Track 2: move data from D: to C: (the actual request)

C: budget: 17.51 GB free now, minus a safety floor of 9.5 GB, leaves **about 8 GB of usable space on C:**. The pagefile on C: (13.13 GB today, 21 GB under pressure) and the watchdog threshold (4.5 GB) are the reasons for that floor.

| Rank | Folder | GB | Fits the 8 GB budget? | Risk | Verdict |
|---|---|---|---|---|---|
| 1 | `D:\Games\Need For Speed Underground` | 1.29 | yes | low, one game, no save data touched | move to C: if the owner wants it back |
| 2 | `D:\Projects\Backups` | 1.64 | yes | low, the copies inside stay on the workspace drive | possible, D: keeps the working set and C: keeps the spare copy |
| 3 | `D:\Games\Blur` | 7.32 | no, it alone eats the whole budget | low | keep on D: or an external drive |
| 4 | `D:\Games\Mortal.Kombat.Komplete.Edition` | 9.25 | no | low | keep on D: or an external drive |
| 5 | `D:\Games\Pro Evolution Soccer 2019` | 29.50 | no | low | keep on D: or an external drive |
| 6 | `D:\Games\GTAVEnhanced` | 104.78 | no | medium, mods and saves live inside it | keep on D:, an external drive is the answer |
| 7 | `D:\Projects\AI_Models_Hub` | 11.68 | no | high, `OLLAMA_MODELS` points at it | do not move |
| 8 | `D:\Projects\SIR ModPack` | 14.98 | no | high, product payload in `legacy\` | do not move |
| 9 | `D:\Projects\Android` | 5.92 | yes, but no | high, the JDK and SDK paths are pinned | do not move |

Reality check on track 2: of the 152.14 GB of games, only `Need For Speed Underground` (1.29 GB) fits inside the safe C: budget. `Blur` alone would take the whole budget. So the honest answer is that **C: cannot take the games back**. The two things that really free D: are deleting what is regenerable (track 1, about 8.2 GB) and the owner's decision on the games (up to 152 GB, to an external drive or into the bin).

### The top three moves

1. **Run track 1 in one pass** (about 8.2 GB of D: freed, nothing touches C:): drop `ahome-audit-before` after the owner confirms, clear `ms-playwright` and the npm cache, clear the Gradle caches, clear the AHome build output once the AHome round stops, drop `sir-study-before-661a0d9` and the small build outputs.
2. **Move 2.93 GB onto C: and stop there**: `D:\Projects\Backups` (1.64 GB) plus `D:\Games\Need For Speed Underground` (1.29 GB). C: then sits at about 14.6 GB free, well above the 9.5 GB floor, and D: gains the same 2.93 GB for the build rounds.
3. **Decide the games once, in one pass**, with the owner naming the folders to keep, to delete or to put on an external drive. That is the only move big enough to matter, up to 152 GB. A 64 GB or bigger USB drive is the only thing that can take `GTAVEnhanced` (104.78 GB).

## 8. Do not touch list

1. `D:\Projects\AHome` and everything in it. Private, local only, round r71 was editing `apps/web` during this scan, four `local-core` Python processes were running.
2. `D:\Projects\AI_Models_Hub`. `OLLAMA_MODELS` points at it, and the whisper transcribe reads it.
3. `D:\Caches\` (all of it). The user env vars and `scripts/cli-run2.sh` point there. Moving it back to C: re-creates the 2026-11-12 C: emergency.
4. `D:\.pnpm-store\v11`. The live pnpm store, hard-linked into the pnpm projects.
5. `D:\Projects\Android\jdk21` and `D:\Projects\Android\Sdk`. Java and adb were running.
6. `D:\Projects\Backups`. Owner backups, protected by AGENTS.md. (Moving a copy to C: is a track 2 option, deleting is not.)
7. `D:\Projects\old projects` and every `legacy\` folder, including `SIR ModPack\legacy` (14.97 GB, the mod payload). Never deleted, only read.
8. `D:\Projects\_SIR` and its `.sir`, `ops`, `plans`, `scripts` trees. The HQ system runs from it.
9. The root of D: itself. `d:\pagefile.sys` is a system-managed pagefile and the paging-file registry lists both C: and D:. The root must not be restructured.
10. `D:\System Volume Information`. Windows owns it.
11. `D:\acc`. Account recovery codes, sensitive, never opened and never copied.
12. `D:\$RECYCLE.BIN`. Personal, the owner decides.
13. Anything a running process holds. Live during this scan: `AHome\apps\local-core\.venv` (4 processes), `SIR AI\node_modules\@esbuild` (1), `SIR Laptop Manager\.venv` (2, a pytest run), `Android\jdk21` (2 Java) and `Android\Sdk` (adb), `_SIR\tools\sir-autonomy\.venv` (1).
14. The live paths that tools hardcode: `D:\Projects\_SIR\_quarantine`, `D:\Downloads`, `D:\Projects\AI_Models_Hub\ollama`.
15. The `D:\AI_Models_Hub` path itself. The `sir-guards` hook in `mods/sir-guards/hooks/register.ts` blocks any write to it, so nothing should ever be moved back there.

## 9. Runbook for the day the owner says go

Read only, copy only, no deletion, in this order, with a free-space reading before and after every step.

```
# 0. before anything: read both drives
Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" |
  Select-Object DeviceID, @{n='FreeGB';e={[math]::Round($_.FreeSpace/1GB,2)}}

# 1. stop the writers: no worker round, no dev server, no game
#    (the autopilot is paused by the owner for the window)

# 2. move one folder from D: to C: (copy first, verify, then remove the source)
robocopy "D:\Games\Need For Speed Underground" "C:\Games\Need For Speed Underground" /E /COPY:DAT /DCOPY:DAT /R:1 /W:1 /XJ
#    verify the copy with a listing diff, it must report 0 differences:
robocopy "C:\Games\Need For Speed Underground" "D:\Games\Need For Speed Underground" /MIR /L /XJ
#    only then remove the source, and only after the owner confirms

# 3. read the drives again, and stop when C: free drops under 9.5 GB

# 4. rollback: robocopy back to D:, then remove the copy from C:
```

Rules for the window: no deletion before the copy is verified file count by file count and byte count by byte count; one folder per step; a free-space reading after every step; the owner present for the games; never two folders at once.

## 10. Open items for the owner (one line each)

1. Games: which of the five game folders stay, which go to an external drive, which can be deleted. The only move worth more than 8 GB.
2. `D:\Projects\ahome-audit-before`: keep as an audit safety copy or drop it (2.00 GB).
3. `D:\Projects\sir-study-before-661a0d9`: keep or drop (0.19 GB).
4. `D:\AI_Models_Hub`: confirm the voice pipeline reads `D:\Projects\AI_Models_Hub` only, then the 0.41 GB duplicate can go.
5. `D:\d\Projects`: a stray copy of `AHome` and `SIR Hagoozat`. Confirm it can go.
6. C: floor: agree to keep at least 9.5 GB free on C: so the pagefile never eats it again.
7. External drive: a USB drive of 64 GB or more is the only thing that can take `GTAVEnhanced` (104.78 GB).
8. HQ cleanup: the environment variable `npm_config_store_dir` does not control pnpm on this machine, the live store is `D:\.pnpm-store\v11`. Correct the variable or drop it, so nobody deletes the store by mistake.

## 11. Numbers recap

- D: total 265.01 GB, used 212.77 GB, free 52.23 GB.
- C: total 210.00 GB, used 192.49 GB, free 17.51 GB.
- Top five folders on D: `D:\Games` 152.14 GB, `D:\Projects` 62.70 GB, `D:\Caches` 2.15 GB, `D:\AI_Models_Hub` 0.41 GB, `D:\$RECYCLE.BIN` 0.12 GB.
- Top five single items on D: GTAVEnhanced 104.78 GB, Pro Evolution Soccer 2019 29.50 GB, SIR ModPack 14.98 GB, AI_Models_Hub 11.68 GB, Mortal Kombat 9.25 GB.
- Top three moves: run the track 1 cleanup (about 8.2 GB of D: freed, no C: used), move `Backups` plus `Need For Speed Underground` onto C: (2.93 GB, C: stays at about 14.6 GB free), and settle the games in one pass with the owner (up to 152 GB, external drive or bin).
