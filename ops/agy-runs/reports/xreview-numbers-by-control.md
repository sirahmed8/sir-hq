# Cross-Review: Control Room Numbers vs Disk Ground Truth (Review by SIR Control Room)
**Reviewer:** SIR Control Room (`D:/Projects/_SIR`)  
**Target:** SIR Control Room Dashboard Metrics & Data Gathering (`plans/generate_dashboard.py` vs 16 Project Workspaces in `D:/Projects/`)  
**Timestamp:** 2026-11-09 07:20 Cairo Local Time  
**Review Type:** Independent Cross-Project Ground Truth Data Audit (Round 9)  
**Rule Adherence:** Read-only inspection; verified against live git repositories, disk tasks, and GitHub Actions API. AHome personal content strictly protected (counts and structure only).

---

## 1. Executive Summary & Verdict
A forensic audit was conducted comparing the published Control Room numbers (`ops/dashboard.html` and `ops/artifact/control-room.html`) against the physical ground truth on disk across all 16 projects in `D:/Projects`.

### Verification Scope
- **Task Counts:** Displayed `total` and `done` counts vs parsed milestone tasks vs raw regex task checkboxes (`^\s*-\s*\[([ xX])\]`) in `.sir/TASKS.md`.
- **Git Commit Dates & Hashes:** Displayed commit date vs actual `git log -1 --format=%cs` and `git rev-parse --short HEAD`.
- **Git Sync Status:** Displayed sync status vs real `git status -sb` (ahead, behind, unpushed commits, and dirty working tree files).
- **Request Ledgers:** Displayed requests counts (`open`, `done`, `blocked`, `total`) vs real ledgers in `ops/requests/*.md`.
- **CI Status:** Displayed CI badges vs live GitHub Actions workflow runs queried via `gh run list`.
- **Privacy Compliance:** Assertive verification that zero private personal names or private repo names appear in any generated dashboard or artifact file.

---

## 2. Comprehensive Ground Truth Comparison Matrix

| Project Slug | Displayed Tasks | Raw Disk Tasks | Parsed Tasks | Commit Date (Dash / Disk) | Disk Commit Hash | Git Sync (Dash / Disk) | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **sir-platform** | 2/29 | 2/29 | 2/29 | 2026-11-09 / 2026-11-09 | `f3a129a` | in sync / in sync | MATCH |
| **sir-obour-hub** | 2/28 | 2/28 | 2/28 | 2026-11-09 / 2026-11-09 | `be98960` | in sync / in sync | MATCH |
| **sir-hagoozat** | 2/24 | 2/24 | 2/24 | 2026-11-09 / 2026-11-09 | `2d9d7f9` | in sync / in sync | MATCH |
| **sir-business** | 2/22 | 2/22 | 2/22 | 2026-11-09 / 2026-11-09 | `d74eaee` | in sync / in sync | MATCH |
| **sir-content-creation-studio** | 2/19 | 2/19 | 2/19 | 2026-11-09 / 2026-11-09 | `7c7f374` | in sync / in sync | MATCH |
| **sir-controller** | 2/20 | 2/20 | 2/20 | 2026-11-09 / 2026-11-09 | `a8560a5` | in sync / in sync | MATCH |
| **sir-ai** | 3/44 | 3/44 | 3/44 | 2026-11-09 / 2026-11-09 | `fc6f373` | in sync / in sync | MATCH |
| **sir-laptop-manager** | **25/27** | **33/36** | 25/27 | 2026-11-09 / 2026-11-09 | `2b2fa6a` | **in sync / dirty (14 files)** | **DISCREPANCY** |
| **ahome** | **50/87** | **93/158** | 50/87 | withheld / withheld | withheld | withheld / withheld | **DISCREPANCY** |
| **sir-jobs** | 18/18 | 18/18 | 18/18 | 2026-11-09 / 2026-11-09 | `62f9c76` | in sync / in sync | MATCH |
| **sir-negm-furniture** | 10/16 | 10/16 | 10/16 | 2026-11-09 / 2026-11-09 | `62c3912` | in sync / in sync | MATCH |
| **sir-modpack** | 2/18 | 2/18 | 2/18 | 2026-11-09 / 2026-11-09 | `fd8bf21` | in sync / in sync | MATCH |
| **sir-mods-for-gta-v** | 2/18 | 2/18 | 2/18 | 2026-11-09 / 2026-11-09 | `db2a26d` | in sync / in sync | MATCH |
| **sir-life** | 7/24 | 7/24 | 7/24 | 2026-11-09 / 2026-11-09 | `d598fd3` | in sync / in sync | MATCH |
| **sir-portfolio** | 2/19 | 2/19 | 2/19 | 2026-11-09 / 2026-11-09 | `547a88c` | in sync / in sync | MATCH |
| **sir-study** | 9/33 | 9/33 | 9/33 | 2026-11-09 / 2026-11-09 | `ffff4ec` | in sync / in sync | MATCH |
| **_SIR (HQ / Control)** | N/A | N/A | N/A | 2026-11-09 / 2026-11-09 | `9061173` | in sync / in sync | MATCH |

---

## 3. Detailed Discrepancies & Root Causes

### Discrepancy 1: Laptop Manager Perpetual Loop Tasks Excluded from Control Room
- **Observation:** Dashboard displays **25 done / 27 total** for `SIR Laptop Manager`, whereas the physical file `D:/Projects/SIR Laptop Manager/.sir/TASKS.md` contains **33 done / 36 total** (9 tasks missing from the count).
- **Root Cause:** In `plans/generate_dashboard.py` lines 370 and 375:
  ```python
  m = re.match(r"## (M\d) (.*)", ln)
  ...
  m2 = re.match(r"- \[([ x])\] (T-\d+) \| owner: [^|]+\| (.*)", ln)
  ```
  The parser strictly requires milestone headers to start with `## M\d` and task IDs to match `T-\d+`.
  In `SIR Laptop Manager/.sir/TASKS.md` lines 48-57, the new perpetual improvement loops section is authored as:
  ```markdown
  ## Perpetual Improvement Loops
  - [x] L-001 | owner: ui-craftsman | Cycle 0 (Lens: Pixel-level polish)...
  - [x] L-002 | owner: ui-craftsman | Cycle 1 (Lens: Motion and animation)...
  ...
  - [ ] L-009 | owner: release-manager | Cycle 7 (Lens: Clean Installer & Tray Companion)...
  ```
  Because the header is `## Perpetual Improvement Loops` (not `## M...`) and task IDs are `L-\d+` (not `T-\d+`), `parse_tasks()` discards all 9 loop tasks.
- **Impact:** Control Room under-reports finished tasks for Laptop Manager by 8 completed items and 1 open item.

---

### Discrepancy 2: AHome Extended Tasks Excluded from Control Room
- **Observation:** Dashboard displays **50 done / 87 total** for `AHome`, whereas the physical file `D:/Projects/AHome/.sir/TASKS.md` contains **93 done / 158 total** (71 tasks missing from the count).
- **Root Cause:** In `D:/Projects/AHome/.sir/TASKS.md`, sections A through F, Benchmark, and Security review follow legacy/extended task numbering schemes:
  - `T-NEW-01` through `T-NEW-12`
  - `T-BM-01` through `T-BM-09`
  - `T-SEC-01` through `T-SEC-10`
  Because `generate_dashboard.py` enforces regex `(T-\d+)`, any task ID containing letters after the hyphen is ignored.
- **Truth Assessment:** The 87 tasks displayed on the dashboard accurately represent the core milestones (M0-M6 and Ahmed requests), but omit the 71 benchmark/gap items.

---

### Discrepancy 3: Git Sync Status Reports "in sync" Despite Dirty Worktrees
- **Observation:** Dashboard displays `sync: "in sync"` for `SIR Laptop Manager`, even though `git status -sb` in `D:/Projects/SIR Laptop Manager` reveals 14 dirty/untracked files.
- **Root Cause:** In `plans/generate_dashboard.py` lines 782-786:
  ```python
  sync=(
      ""
      if private
      else (
          "in sync"
          if "ahead" not in git(folder, "status", "-sb").split("\n")[0]
          and "behind" not in git(folder, "status", "-sb").split("\n")[0]
          else "not in sync"
      )
  )
  ```
  The code only inspects the first line of `git status -sb` (`## main...origin/main`), checking for branch tracking divergence ("ahead" or "behind"). It completely ignores lines 2+ representing modified, staged, or untracked files in the working directory!
- **Impact:** A project with uncommitted files or dirty unreviewed code is reported as "in sync" to the owner, masking uncommitted local modifications.

---

### Discrepancy 4: Commit Field Populated with Date Instead of Short Hash
- **Observation:** In `generate_dashboard.py` line 777:
  ```python
  commit=git(folder, "log", "-1", "--format=%cs") if not private else "",
  ```
  The dictionary field `commit` holds the date `2026-11-09`, while the git commit hash (e.g., `2b2fa6a`) is never passed to `projects`.
- **Impact:** While the dashboard displays the commit date nicely, the actual git SHA is unavailable in the project detail view, making it harder for reviewers to verify the exact build artifact without checking git manually.

---

## 4. Operational Systems Verification

### A. Request Ledgers Audit (`ops/requests/*.md`)
All 5 request ledgers were parsed and compared against `dashboard.html`'s `request_ledgers` array:
- `ahome.md`: 0 open, 0 in progress, 22 done, 0 blocked (total 22) -> **100% MATCH**
- `control.md`: 0 open, 0 in progress, 11 done, 0 blocked (total 11) -> **100% MATCH**
- `jobs.md`: 0 open, 0 in progress, 7 done, 0 blocked (total 7) -> **100% MATCH**
- `laptop.md`: 0 open, 0 in progress, 8 done, 0 blocked (total 8) -> **100% MATCH**
- `study.md`: 0 open, 0 in progress, 7 done, 0 blocked (total 7) -> **100% MATCH**

### B. Live GitHub Actions CI Status
Live API query via `gh run list` across all active repositories confirmed 100% green status matching `dashboard.html`:
- `AHome (private repo)`: Run ID `42563969058` -> `success` (commit `9bca9b2`) -> **MATCH**
- `SIR HQ`: Run ID `42564026473` -> `success` (commit `9061173`) -> **MATCH**
- `SIR Jobs`: Run ID `42563730119` -> `success` (commit `62f9c76`) -> **MATCH**
- `SIR Study`: Run ID `42563063184` -> `success` (commit `ffff4ec`) -> **MATCH**
- `SIR Laptop Manager`: Run ID `42563978585` -> `success` (commit `2b2fa6a`) -> **MATCH**

### C. Privacy Audit
Regex search across `ops/dashboard.html` and `ops/artifact/control-room.html` confirmed:
- Zero occurrences of private family names or personal identifiers.
- Zero occurrences of private repository name (cleanly masked as `"AHome (private repo)"` with `id: null` and `url: null`).

---

## 5. Actionable Recommendations for Control Room Generator
1. **Support Flexible Task Header & ID Parsing:** Update `parse_tasks()` to recognize `## Perpetual...` / `## Loop...` milestone headers and accept task IDs matching `r"(?:T|L)-[A-Za-z0-9_-]+"` so that non-standard but valid project tasks are included in the progress counts.
2. **Deep Git Status Reporting:** Enhance `sync` evaluation to distinguish between `in sync`, `ahead / unpushed`, and `dirty (N uncommitted files)`.
3. **Expose Git Commit Hashes:** Add a dedicated `hash` field (`git log -1 --format=%h`) alongside `commit_date` in each project object.
