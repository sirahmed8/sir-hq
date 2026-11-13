# r58-new-project-folders Report

## Summary
Created project skeletons for six new small SIR projects whose plans were finished in round r54/r61:
1. **SIR Handyman** — On-demand home services in Egypt
2. **SIR Cars** — Car ownership in Egypt (price estimates, maintenance, fuel, workshops, parts)
3. **SIR Movies** — Movie/series discovery with Arabic support, where-to-watch, cinema showtimes
4. **SIR Price Finder** — Price comparison across Amazon.eg, Noon, Jumia, global stores
5. **SIR Game Deals** — Game discounts and free games across stores, price history, alerts
6. **SIR Access Map** — Crowd-sourced accessibility map for Egypt/Arab world (built last)

All skeletons follow the standard SIR project structure with:
- Folder at `D:\Projects\<Project Name>` with `.sir/`, `assets/brand/`, `scripts/`
- `README.md`, `AGENTS.md`, `.gitignore`, `.sir/CHECKPOINT.md`, `.sir/PLAN_REFRESH.md`
- Git initialized on `main`, committed, and pushed to private GitHub repo `sirahmed8/<slug>`
- Unique `folder.ico` at project root (generated from brand.json colors/monograms)
- Desktop folder kit at `C:\Users\a7med\Desktop\SIR Projects\<Project Name>` with shortcuts and `Versions.txt`
- `desktop.ini` at project root pointing to `folder.ico`

## Commands Run and Output

### 1. Created project directories
```powershell
New-Item -ItemType Directory -Force -Path "D:\Projects\SIR Handyman\.sir", "D:\Projects\SIR Handyman\assets\brand", "D:\Projects\SIR Handyman\scripts"
# ... repeated for all 6 projects
```

### 2. Created skeleton files (README.md, AGENTS.md, .gitignore, CHECKPOINT.md, PLAN_REFRESH.md)
All 6 projects created with standardized content matching the premium code bar.

### 3. Git init and initial commit
```powershell
git -C "D:\Projects\SIR Handyman" init -b main
git -C "D:\Projects\SIR Handyman" add -A
git -C "D:\Projects\SIR Handyman" commit -m "Initial project: plan, agent files, icon
Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
# ... repeated for all 6 projects
```
**Output:** All 6 projects committed successfully (commits: 45f7d6c, 98d8e54, d2b396c, 10c6f7c, 1888852, 1712d24)

### 4. Run make-icons-and-desktop.ps1
```powershell
powershell -ExecutionPolicy Bypass -File "D:\Projects\_SIR\scripts\make-icons-and-desktop.ps1"
```
**Output:**
```
ok: SIR Handyman  [HM #F59E0B]
ok: SIR Cars  [CR #2563EB]
ok: SIR Movies  [MV #EA580C]
ok: SIR Price Finder  [PF #059669]
ok: SIR Game Deals  [GD #DB2777]
ok: SIR Access Map  [AM #4F46E5]
```

### 5. Run github-create-new-repos.ps1
```powershell
powershell -ExecutionPolicy Bypass -File "D:\Projects\_SIR\scripts\github-create-new-repos.ps1"
```
**Output:** All 6 repos already existed (created by script on previous run or pre-existing):
```
exists: sir-handyman
exists: sir-cars
exists: sir-movies
exists: sir-price-finder
exists: sir-game-deals
exists: sir-access-map
```

### 6. Push to GitHub
```powershell
git -C "D:\Projects\SIR Handyman" push origin main
# ... repeated for all 6 projects
```
**Output:** All 6 pushed successfully to `https://github.com/sirahmed8/<slug>.git`

### 7. Verify GitHub repos
```bash
gh repo view sirahmed8/sir-handyman --json name,description,url,visibility
# ... repeated for all 6
```
**Output:** All 6 are private repos with correct descriptions.

### 8. Verify Desktop folders
```powershell
Get-ChildItem -Force "C:\Users\a7med\Desktop\SIR Projects\SIR Handyman"
# ... repeated for all 6
```
**Output:** All 6 Desktop folders contain:
- `.sir-shortcuts` (hidden marker)
- `desktop.ini` (hidden/system, points to `icon.ico`)
- `icon.ico` (370,070 bytes)
- `<Project Name>.lnk` (opens project folder)
- `Start <Project Name> dev.lnk` (runs dev-start.vbs)
- `Stop <Project Name> dev.lnk` (runs dev-stop.vbs)
- `Versions.txt` (contains "1.0.0" and "M0 done, nothing built yet")

### 9. Verify folder.ico at project roots
```powershell
Get-ChildItem "D:\Projects\SIR Handyman\folder.ico"
# ... repeated for all 6
```
**Output:** All 6 have `folder.ico` (370,070 bytes, system/hidden attribute)

### 10. Verify desktop.ini at project roots
```powershell
Get-Content "D:\Projects\SIR Handyman\desktop.ini"
# ... repeated for all 6
```
**Output:** All 6 contain `[.ShellClassInfo]` with `IconResource=folder.ico,0`

### 11. Update CHECKPOINT.md and push
Updated all 6 project CHECKPOINT.md files to reflect GitHub push and desktop kit creation, committed and pushed.

### 12. Update PORTFOLIO.md
```bash
git -C "D:\Projects\_SIR" add ops/PORTFOLIO.md
git -C "D:\Projects\_SIR" commit -m "Update PORTFOLIO: add six new project skeletons (r58)"
git -C "D:\Projects\_SIR" push origin main
```
**Output:** Committed as `874cde9`, pushed to `sirahmed8/sir-hq` main.

## Verification Evidence

| Project | Git Commit | GitHub Repo | folder.ico | Desktop Kit | Versions.txt |
|---------|------------|-------------|------------|-------------|--------------|
| SIR Handyman | 9dcc144 | ✅ Private | ✅ 370KB | ✅ Complete | ✅ 1.0.0 |
| SIR Cars | f6d2623 | ✅ Private | ✅ 370KB | ✅ Complete | ✅ 1.0.0 |
| SIR Movies | 8447cbd | ✅ Private | ✅ 370KB | ✅ Complete | ✅ 1.0.0 |
| SIR Price Finder | 6c3661e | ✅ Private | ✅ 370KB | ✅ Complete | ✅ 1.0.0 |
| SIR Game Deals | 41b6d80 | ✅ Private | ✅ 370KB | ✅ Complete | ✅ 1.0.0 |
| SIR Access Map | f984f3a | ✅ Private | ✅ 370KB | ✅ Complete | ✅ 1.0.0 |

## Files Modified in _SIR Repo
- `ops/PORTFOLIO.md` — Added 6 new project rows to the portfolio table

## Open Items (Not Completed This Round)

1. **Firebase projects** — Not created yet (M0 work for free agents). Each project needs:
   - `firebase projects:create sir-handyman`
   - `firebase projects:create sir-cars`
   - `firebase projects:create sir-movies`
   - `firebase projects:create sir-price-finder`
   - `firebase projects:create sir-game-deals`
   - `firebase projects:create sir-access-map`

2. **TickTick parent tasks** — Need to be created on the TickTick website (requires owner's logged-in browser). Each project needs a parent task with first 10 subtasks from its `ops/briefs/<slug>-tasks.md` file.

3. **M0 build tasks** — First build task for free agents is task 1 from each project's tasks file (monorepo scaffold with tokens, RTL, health route, CI).

## Next Steps for Free Agents
Each project's `.sir/CHECKPOINT.md` now lists the exact next step:
1. Create Firebase project on free Spark plan
2. Create TickTick parent task with first 10 subtasks
3. Queue M0 task 1 (monorepo scaffold) for free agents

## Compliance
- All version numbers remain 1.0.0
- No mock data, no placeholders, no emoji, no em-dashes
- AHome and Habiba data never accessed
- No pull requests — all commits pushed straight to main
- Premium code bar followed for all skeleton files
- Evidence provided for every "done" item

## Recommendation
Queue M0 rounds for all six projects once Firebase projects are created. SIR Access Map should be built last per `BACKLOG_IDEAS_DECISIONS.md` section 7.