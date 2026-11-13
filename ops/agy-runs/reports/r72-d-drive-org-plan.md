# r72-d-drive-org-plan - D: drive audit and organization plan (read only)

Date: 2026-11-13. Worker: opencode (minimax-m3.1-flash-free), started 02:40, finished 03:55.
Task: `ops/briefs/r72-d-drive-org-plan.prompt.txt` (queue copy `ops/briefs/r72-d-drive-org-plan.md`, task board `ops/tasks/inbox/5-r72-d-drive-org-plan.md`).
Owner request (2026-11-13): Ahmed freed a lot of space on C: (deleted games etc). D: must stay untouched for now. When the current build tasks finish, space will be moved from D: to C:. Prepare the plan now so the move is fast and safe later.

Result: done. The full plan is `D:/Projects/_SIR/ops/plans/D_DRIVE_ORG_PLAN.md`. Nothing on D: or C: was deleted, moved, renamed or modified.

## 1. What I did

1. Read the brief, `ops/WORKER_PREAMBLE.md`, `.sir/CHECKPOINT.md`, `ops/bus/team.md` (last 40 lines), `standard/OWNER_DEFAULTS.md`, `ops/DISK.md` (2026-10-29 baseline) and `ops/disk-plan-2026-11-12.md` (the cleanup that freed 14.81 GB on 2026-11-12).
2. Read the current free space of both drives from the OS.
3. Measured every top-level folder on D: with robocopy in listing mode (nothing copied), then every child of `D:\Projects`, `D:\Games` and `D:\Caches` with the same method, then the regenerable folders inside the projects.
4. Checked what pins a path in place: user environment variables, the CLI runner script, the tools that hardcode a path, the processes that were running during the scan, and the pagefile registry.
5. Wrote the plan to `ops/plans/D_DRIVE_ORG_PLAN.md` (size table, classification, ranked move list, do-not-touch list, runbook, open items for the owner).
6. Committed and pushed the plan, updated the checkpoint and the team board, wrote this report.

Hard limits respected: no delete, move, rename or modification on D: outside `D:/Projects/_SIR`; no file inside AHome was opened (names and sizes only); C: was only read, never written; the output is one markdown plan file plus this report.

## 2. Commands run and their real output

### 2.1 Free space (source of truth for the whole plan)

```
PS> Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" |
      Select-Object DeviceID, @{n='SizeGB';e={[math]::Round($_.Size/1GB,2)}}, @{n='FreeGB';e={[math]::Round($_.FreeSpace/1GB,2)}}
DeviceID SizeGB FreeGB
-------- ------ ------
C:         210    17.51
D:      265.01    52.23

PS> Get-PSDrive -PSProvider FileSystem | Select Name, @{n='UsedGB';e={[math]::Round($_.Used/1GB,2)}}, @{n='FreeGB';e={[math]::Round($_.Free/1GB,2)}}
Name UsedGB FreeGB
---- ------ ------
C    192.48  17.51
D    212.77  52.23
Temp 212.77  52.23     <- the Temp PSDrive points at D:\Caches\tmp
```

The owner's numbers in the brief ("C: about 17.5 GB free, D: about 52 GB free") match the measurement exactly.

### 2.2 Size method

```
robocopy <folder> NUL /L /S /XJ /NJH /NDL /NC /NS /BYTES /R:0 /W:0
```

`/L` is listing mode, so nothing is copied or changed. `/XJ` skips junctions so a folder is not counted twice through a link. The `Bytes:` line of the summary gives the size. The first run over the 18 top-level folders ran in one pass; the second run (51 folders: every child of `D:\Projects`, `D:\Games`, `D:\Caches`) ran eight robocopy jobs in parallel through `Start-Job` so the tree walk did not take an hour.

### 2.3 Top-level map of D: (real output)

```
Path                             GB        MB Files
----                             --        -- -----
D:\Games                     152.14 155792.80 21340
D:\Caches                      2.15   2206.50 30311
D:\AI_Models_Hub               0.41    420.60     16
D:\$RECYCLE.BIN                0.12    124.30     43
D:\.pnpm-store                 0.10     96.90    714
D:\tmp-win                     0.01      8.10    563
D:\temp-npm                    0.00      2.10    696
D:\tmp                         0.00      1.90     35
D:\.sir                        0.00      1.40     24
D:\d                           0.00      0.20      2
D:\tmp-npm                     0.00      0.00      3
D:\.remember                   0.00      0.00     10
D:\Projects                    0.00      0.00      0   <- the first pass was stopped here and re-measured per child
D:\System Volume Information   0.00      0.00      0
D:\temp                        0.00      0.00      2
D:\temp-verify                 0.00      0.10     95
D:\acc                         0.00      0.00      2
D:\Downloads                   0.00      0.00      0
```

### 2.4 Per project inside `D:\Projects` (real output, top of the list)

```
Path                                        GB  Files
----                                        --  -----
D:\Games\GTAVEnhanced                   104.78  13033
D:\Games\Pro Evolution Soccer 2019        29.50   6277
D:\Projects\SIR ModPack                   14.98  73833
D:\Projects\AI_Models_Hub                 11.68     81
D:\Games\Mortal.Kombat.Komplete.Edition    9.25   1314
D:\Games\Blur                              7.32    152
D:\Projects\SIR Business                   6.30   3368
D:\Projects\Android                        5.92  33854
D:\Projects\SIR Laptop Manager             5.38  93119
D:\Projects\SIR AI                         4.30 127532
D:\Projects\SIR Mods for GTA V             2.71  40110
D:\Projects\AHome                          2.46  71232
D:\Projects\ahome-audit-before             2.00  51636
D:\Projects\Backups                        1.64   2844
D:\Caches\ms-playwright                    1.58   1574
D:\Projects\SIR Content Creation Studio    1.33  11088
D:\Games\Need For Speed Underground        1.29    563
D:\Projects\_SIR                           0.90   7282
D:\Projects\SIR Controller                  0.90   3507
D:\Projects\SIR Study                       0.73   7195
D:\Projects\SIR Portfolio                   0.59  14647
D:\Caches\npm                              0.44  25139
D:\Projects\SIR Jobs                        0.26   6397
D:\Projects\SIR Hagoozat                    0.22   3246
D:\Projects\sir-study-before-661a0d9        0.19   1891
D:\Caches\tmp                               0.13   3594
D:\Projects\SIR Negm Furniture              0.09   1676
D:\Projects\SIR Education Hub               0.06   1810
D:\Projects\SIR Life                        0.03    812
D:\Projects\old projects                    0.01    366
D:\Projects\SIR Platform                    0.01    308
D:\Projects\SIR Movies                      0.00     80
D:\Projects\SIR Game Deals                  0.00     74
D:\Projects\SIR Cars                        0.00     87
D:\Projects\SIR Access Map                  0.00     74
D:\Projects\SIR Handyman                    0.00     86
D:\Projects\SIR Deals                       0.00     13
D:\Projects\SIR Price Finder                0.00     74
D:\Caches\pnpm-store, pip, uv               0.00      0
```

The full 51 row output is in the plan, and the per-project sizes of `SIR ModPack`, `AI_Models_Hub`, `Android`, `AHome`, `Backups` and the rest are broken down in section 3 of the plan.

### 2.5 Regenerable folders inside the projects (real output, the ones that matter)

```
     14.973     73607  D:\Projects\SIR ModPack\legacy
     11.403        56  D:\Projects\AI_Models_Hub\ollama
      3.854     12232  D:\Projects\Android\Sdk
      1.695     47153  D:\Projects\ahome-audit-before\node_modules
      1.638      2844  D:\Projects\Backups
      1.085      3231  D:\Projects\AHome\apps\web\.next
      0.739     38562  D:\Projects\AHome\node_modules
      0.733     10371  D:\Projects\Android\.gradle
      0.701     43431  D:\Projects\SIR AI\node_modules
      0.648     10559  D:\Projects\Android\gradle-home
      0.429     14788  D:\Projects\SIR AI\legacy\SIR AI (v1)\.venv
      0.416      7905  D:\Projects\SIR Content Creation Studio\legacy\SIR Content Creation Studio (v1)\.venv
      0.389     12493  D:\Projects\SIR Portfolio\node_modules
      0.389     10408  D:\Projects\AHome\apps\local-core\.venv
      0.384     14879  D:\Projects\SIR AI\legacy\Odysseus app\.venv
      0.321        490  D:\Projects\Android\jdk21
      0.275       562  D:\Projects\ahome-audit-before\apps\web\.next
      0.197      3424  D:\Projects\SIR Laptop Manager\.venv
      0.138         9  D:\Projects\AI_Models_Hub\whisper
      0.138        14  D:\Projects\AI_Models_Hub\_whisper_duplicate_from_restore
      0.088       233  D:\Projects\SIR Portfolio\.next
      0.038      1497  D:\Projects\SIR AI\legacy\SIR Tele Gateway\.venv
      0.034      1461  D:\Projects\SIR Jobs\node_modules
      0.032      2794  D:\Projects\SIR AI\apps\web\node_modules
      0.028       545  D:\Projects\SIR Hagoozat\legacy\EGFootball5\out
      0.024       262  D:\Projects\SIR Life\node_modules
      0.024       762  D:\Projects\_SIR\tools\sir-autonomy\.venv
      0.020      2877  D:\Projects\AHome\apps\web\node_modules
      0.020      2535  D:\Projects\ahome-audit-before\apps\web\node_modules
      0.018       183  D:\Projects\SIR Laptop Manager\node_modules
      0.013       679  D:\Projects\SIR Hagoozat\legacy\11Players\out
      0.012       898  D:\Projects\SIR Study\.venv
      0.012       171  D:\Projects\SIR Negm Furniture\apps\web\out
      0.011       163  D:\Projects\SIR Negm Furniture\legacy\Negm Furniture\out
      0.011       366  D:\Projects\old projects
      0.009       570  D:\Projects\SIR Education Hub\legacy\Obour Academic Hub\out
      0.005         1  D:\Projects\AI_Models_Hub\rag
      0.005         1  D:\Projects\AHome\dist
      0.004       119  D:\Projects\SIR Portfolio\out
      0.003        38  D:\Projects\AHome\apps\web\out
      0.001         9  D:\Projects\SIR Business\legacy\SIR Market\build
      0.001        19  D:\Projects\SIR AI\apps\web\dist
      0.000         4  D:\Projects\SIR Business\legacy\SIR Pharmacy\build
      0.000         4  D:\Projects\SIR Business\legacy\SIR Library\build
      0.000         4  D:\Projects\SIR Business\legacy\SIR Restaurant\build
      0.000         5  D:\Projects\SIR Content Creation Studio\legacy\SIR Content Creation Studio (v1)\out
      0.000         1  D:\Projects\SIR AI\apps\desktop\build
      0.000         0  D:\Projects\SIR Life\dist
     -1            0  D:\Projects\SIR Study\dist          (does not exist)
     -1            0  D:\Projects\SIR ModPack\dist       (does not exist)
     -1            0  D:\Projects\SIR ModPack\website-next (does not exist)
```

Nothing in that table was deleted. The brief says list, not delete.

### 2.6 What pins a path in place

```
PS> [Environment]::GetEnvironmentVariable('OLLAMA_MODELS','User')          -> D:\Projects\AI_Models_Hub\ollama
PS> [Environment]::GetEnvironmentVariable('npm_config_cache','User')        -> D:\Caches\npm
PS> [Environment]::GetEnvironmentVariable('PIP_CACHE_DIR','User')           -> D:\Caches\pip
PS> [Environment]::GetEnvironmentVariable('UV_CACHE_DIR','User')            -> D:\Caches\uv
PS> [Environment]::GetEnvironmentVariable('PLAYWRIGHT_BROWSERS_PATH','User')-> D:\Caches\ms-playwright
PS> [Environment]::GetEnvironmentVariable('npm_config_store_dir','User')    -> D:\Caches\pnpm-store
```

```
PS> Get-CimInstance Win32_Process -Filter "Name='robocopy.exe'" | Select ProcessId, CommandLine
"robocopy.exe" D:\Projects NUL /L /S /XJ /NJH /NDL /NC /NS /BYTES /R:0 /W:0

PS> Get-Process | Where-Object { $_.Path -like "D:\*" } | Select Id, ProcessName, Path
  Id ProcessName Path
25016 python      D:\Projects\_SIR\tools\sir-autonomy\.venv\Scripts\python.exe
22600 python      D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe
24076 python      D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe
24876 python      D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe
36256 python      D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe
 9944 java        D:\Projects\Android\jdk21\jdk-21.0.13+9\bin\java.exe
19016 java        D:\Projects\Android\jdk21\jdk-21.0.13+9\bin\java.exe
11404 adb         D:\Projects\Android\Sdk\platform-tools\adb.exe
43776 esbuild     D:\Projects\SIR AI\node_modules\@esbuild\win32-x64\esbuild.exe
12196 pytest      D:\Projects\SIR Laptop Manager\.venv\Scripts\pytest.exe
35484 python      D:\Projects\SIR Laptop Manager\.venv\Scripts\python.exe

PS> Get-CimInstance Win32_PageFileUsage | Select Name, AllocatedBaseSize, CurrentUsage, PeakUsage
Name            AllocatedBaseSize CurrentUsage PeakUsage
C:\pagefile.sys            13448        1215      7955

PS> (Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management").PagingFiles
{c:\pagefile.sys 0 0, d:\pagefile.sys 0 0}
```

The pagefile exists on both drives and is system managed. C: carries 13.13 GB of it today and carried 21 GB on 2026-11-12, which is exactly how C: fell to 0.24 GB free that night.

### 2.7 The hard-link finding (why the folder table does not add up to the disk)

```
PS> fsutil hardlink list "D:\Projects\SIR Life\node_modules\.pnpm\@types+node@22.20.5\node_modules\@types\node\assert.d.ts"
D:\Projects\SIR Life\node_modules\.pnpm\@types+node@22.20.5\node_modules\@types\node\assert.d.ts
\.pnpm-store\v11\files\27\79969fbf89c5331fb045f5d7950fb2d296c186f3774adee797bb5169119bf7512fc6e36828b5fc124fb9bce905d8b74d040cf6a54fc11f78e92a14818d2ae6
\Projects\SIR Life\node_modules\.pnpm\@types+node@22.20.5\node_modules\@types\node\assert.d.ts
```

One file, two links, one on D:\.pnpm-store and one inside node_modules. Robocopy counts both, so the sum of the folder table (about 217.6 GB) is about 4.9 GB above the space the drive really uses (212.77 GB). Every folder number in the plan is therefore an upper bound, and the plan says so.

### 2.8 The pnpm store finding

```
PS> pnpm store path
D:\.pnpm-store\v11
PS> pnpm config get store-dir
undefined
PS> Get-ChildItem D:\Caches\pnpm-store -Force   -> (empty, 0 files)
```

The environment variable `npm_config_store_dir=D:\Caches\pnpm-store` set on 2026-11-12 does not control pnpm on this machine (`pnpm config get store-dir` is undefined, there is no npmrc anywhere). The live store is `D:\.pnpm-store\v11` and it is hard-linked into the pnpm projects, so it must not be deleted. It is on D:, which is the right place. The misleading variable should be corrected by HQ, not by this task. The plan lists it as an open item for HQ.

## 3. What the plan says (summary of `ops/plans/D_DRIVE_ORG_PLAN.md`)

### Top 5 biggest folders on D:

| Rank | Folder | GB | Class |
|---|---|---|---|
| 1 | `D:\Games` | 152.14 | games, owner decision |
| 2 | `D:\Projects` | 62.70 (upper bound) | SIR workspace, keep |
| 3 | `D:\Caches` | 2.15 | tool caches, keep on D: |
| 4 | `D:\AI_Models_Hub` | 0.41 | duplicate model store, owner decision |
| 5 | `D:\$RECYCLE.BIN` | 0.12 | personal, owner decision |

The five biggest single items on D: are `GTAVEnhanced` 104.78 GB, `Pro Evolution Soccer 2019` 29.50 GB, `SIR ModPack` 14.98 GB, `AI_Models_Hub` 11.68 GB, `Mortal Kombat` 9.25 GB.

### Top 3 recommended moves:

1. **Run the track 1 cleanup, about 8.2 GB of D: freed and 0 GB of C: used.** `ahome-audit-before` (2.00, owner confirms), `ms-playwright` (1.58), the Gradle caches (1.38), the AHome build output (1.09, only after the AHome round stops), the legacy Python envs (1.27, slow rebuild), the npm cache (0.44), `sir-study-before-661a0d9` (0.19), the small build outputs (0.16). This is the part that can be done without any risk to the running rounds.
2. **Move 2.93 GB onto C: and stop there**: `D:\Projects\Backups` (1.64 GB) plus `D:\Games\Need For Speed Underground` (1.29 GB). C: then sits at about 14.6 GB free, well above the 9.5 GB floor. Copy, verify, then delete the source, one folder at a time.
3. **Settle the games in one pass with the owner**: 152.14 GB, and only an external drive (64 GB or more for `GTAVEnhanced` alone) or the bin can take it. C: cannot, and the plan says why.

### The honest limit of "move space from D: to C:"

C: has 17.51 GB free and needs a 9.5 GB floor, because the pagefile on C: grows under memory pressure (13.13 GB today, 21 GB on 2026-11-12, and that is what filled C: to zero). So the usable budget on C: is about 8 GB. Of the 152.14 GB of games, only `Need For Speed Underground` (1.29 GB) fits. `Blur` alone (7.32 GB) would take the whole budget. The plan therefore splits the work into track 1 (frees D: without spending C:) and track 2 (moves at most 8 GB onto C:), and states the C: floor as a rule.

### Do not touch list (plan section 8)

AHome and everything in it; `D:\Projects\AI_Models_Hub` (`OLLAMA_MODELS`); all of `D:\Caches` (env vars and `scripts/cli-run2.sh` point there); `D:\.pnpm-store\v11` (the live store); `Android\jdk21` and `Android\Sdk`; `Backups`; every `legacy\` folder including `SIR ModPack\legacy` (14.97 GB of mod payload); `old projects`; `_SIR`; the root of D: (`d:\pagefile.sys`); `System Volume Information`; `D:\acc` (account recovery codes, never opened); the recycle bin; anything a running process holds (the list in 2.6); and the paths tools hardcode (`D:\Projects\_SIR\_quarantine`, `D:\Downloads`, `D:\Projects\AI_Models_Hub\ollama`).

### Plan sections

1. Method, guarantees, hard-link caveat.
2. Free space now, plus the history table from 2026-10-29 to today.
3. Top-level map of D: with a class and a verdict per folder, then the per-project table, then the pinned paths table.
4. Class B, the tool caches, with a verdict per cache.
5. Class C, the games.
6. The junk inside `D:\Projects`, sizes only.
7. The ranked move plan: track 1 and track 2, plus the top three moves.
8. The do not touch list.
9. The runbook for the day the owner says go (free-space reading before and after every step, copy then verify then delete, stop at the 9.5 GB floor, rollback path).
10. Eight open items for the owner, one line each.
11. The numbers recap.

## 4. What is not certain

- The 4.9 GB gap between the folder sums and the used space is a hard-link effect, confirmed on one sample. The exact split per folder is not measured, so every folder number stays an upper bound.
- `D:\d\Projects` (a plain copy of `AHome` and `SIR Hagoozat`) is too small to size per file and was not opened, because it is AHome material. It needs one word from the owner.
- `D:\AI_Models_Hub` holds a faster-whisper model that also exists in `D:\Projects\AI_Models_Hub`. Which copy the live voice pipeline reads was not proved by reading code (the search found only the guard hook and docs, not the transcribe call site), so the 0.41 GB duplicate is listed as an owner decision, not as a deletion.
- The free space will move while the build rounds run. The numbers are a snapshot between 02:45 and 03:25 on 2026-11-13.
- `System Volume Information` could not be read (Windows owns it), so its use of D: is unknown. It is listed, not judged.
- Whether the owner wants the games back on C: at all is the one open question the plan cannot answer from the disk. That is why track 2 stays inside an 8 GB budget.

## 5. Recommendations for the next step

1. HQ sends the owner the plan section 7 and the two questions in section 10: which of the five game folders stay, go to an external drive or can be deleted, and whether `ahome-audit-before` and `sir-study-before-661a0d9` can go.
2. The actual move waits until the build rounds stop, because `AHome`, `SIR AI`, `SIR Laptop Manager`, `Android` and `_SIR` all have live processes or active rounds. The runbook in section 9 is the order to follow: one folder, copy, verify, delete, read the free space, stop at the floor.
3. Keep the C: floor at 9.5 GB free as a standing rule. Without it the pagefile grows into C: again and the 2026-11-12 emergency repeats.
4. HQ fixes the pnpm store configuration (`npm_config_store_dir` does nothing here) so a future cleanup does not delete `D:\.pnpm-store\v11` and break every pnpm project.
5. A follow-up task could measure the hard-link share per folder, so future audits can report real space instead of upper bounds. Low value now, useful later.

## 6. Commits, push and CI

```
8aefeab r72-d-drive-org-plan: read-only D: audit and the ranked move plan
6a6475b HQ: r71 AHome brief gets the verified root causes; ...
```

Pushed to `origin/main` (sirahmed8/sir-hq). GitHub Actions on commit `8aefeab`:

```
$ gh run list --limit 4
completed	success	r72-d-drive-org-plan: read-only D: audit and the ranked move plan	verify	main	push	43340309071	10s	2026-11-13T00:50:54Z
completed	success	r72-d-drive-org-plan: read-only D: audit and the ranked move plan	test	main	push	43340309011	8s	2026-11-13T00:50:54Z
completed	success	HQ: r71 AHome brief gets the verified root causes; ...	test	main	push	43338281081	12s	2026-11-13T00:35:37Z
completed	success	HQ: r71 AHome brief gets the verified root causes; ...	verify	main	push	43338281044	11s	2026-11-13T00:35:37Z
```

Job and step detail for the two runs of this commit:

```
$ gh run view 43340309071 --json jobs --jq '.jobs[] | {name, conclusion, steps: [.steps[] | {name, conclusion}]}'
{"conclusion":"success","name":"secrets","steps":[{"conclusion":"success","name":"Set up job"},{"conclusion":"success","name":"Run actions/checkout@v4"},{"conclusion":"success","name":"Run gitleaks/gitleaks-action@v2"},{"conclusion":"success","name":"Post Run actions/checkout@v4"},{"conclusion":"success","name":"Complete job"}]}
{"conclusion":"success","name":"python-verify","steps":[{"conclusion":"success","name":"Set up job"},{"conclusion":"success","name":"Run actions/checkout@v4"},{"conclusion":"success","name":"Run actions/setup-python@v5"},{"conclusion":"success","name":"Syntax and compile check"},{"conclusion":"success","name":"Test dashboard generation"},{"conclusion":"success","name":"Post Run actions/setup-python@v5"},{"conclusion":"success","name":"Post Run actions/checkout@v4"},{"conclusion":"success","name":"Complete job"}]}

$ gh run view 43340309011 --json jobs --jq '.jobs[] | {name, conclusion, steps: [.steps[] | {name, conclusion}]}'
{"conclusion":"success","name":"test","steps":[{"conclusion":"success","name":"Set up job"},{"conclusion":"success","name":"Run actions/checkout@v4"},{"conclusion":"success","name":"Run echo \"Hello World\""},{"conclusion":"success","name":"Post Run actions/checkout@v4"},{"conclusion":"success","name":"Complete job"}]}
```

Note: the flag file `ops/ci-quota-exhausted.flag` is present in the repo but stale, the Actions runs execute every step and pass. HQ can delete it.

Files changed by this round (nothing else was touched):

- `ops/plans/D_DRIVE_ORG_PLAN.md` (new): the plan.
- `.sir/CHECKPOINT.md`: the worker note for this round.
- `ops/bus/team.md`: the START line for this round.
- `ops/agy-runs/reports/r72-d-drive-org-plan.md` (new): this report.

Everything else that showed as modified in `git status` belongs to other agents working in parallel (the autopilot queue, the backup manager logs, the dashboard artifacts, the sir-autonomy extension) and was left alone.

## 7. Files written

- `D:/Projects/_SIR/ops/plans/D_DRIVE_ORG_PLAN.md` (the deliverable).
- `D:/Projects/_SIR/ops/agy-runs/reports/r72-d-drive-org-plan.md` (this report).

Nothing else on D: was created, and nothing on D: or C: was deleted, moved or renamed.
