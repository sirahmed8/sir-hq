# r72-d-drive-org-plan — D: drive audit and organization plan (READ ONLY)

Owner request 2026-11-13: Ahmed freed a lot of space on C: (deleted games etc). D: must stay untouched for now. When current build tasks finish, we will move space from D: to C:. Prepare the plan now so the move is fast and safe later.

## Hard limits

- DO NOT delete, move, rename or modify anything on D: outside D:/Projects/_SIR.
- DO NOT touch AHome or Habiba private content (names and sizes only, never open files).
- DO NOT touch C: at all.
- This is a planning task only. Output is one markdown file.

## What to do

1. List every top-level folder on D: with size in GB (use PowerShell Get-ChildItem or robocopy /L style counting; keep it fast, skip reparse points). Include hidden folders.
2. For each folder classify it:
   - SIR workspace (D:/Projects and its subfolders) — keep, list per-project sizes.
   - Tool caches / regenerable data (npm, pip, uv, playwright, pnpm, cargo, gradle, .cache style folders) — candidates to relocate to C: or clean.
   - Games / apps / media — candidates to move back to C: if they fit, or note for owner decision.
   - System or unknown folders — list them, do not judge contents.
3. Note current free space: C: about 17.5 GB free, D: about 52 GB free (re-measure and report real numbers).
4. Write a ranked move plan: which folders give the most GB back to C: with least risk, estimated GB each, and any folder that must NOT move (e.g. active project paths hardcoded in scripts, pagefile-adjacent, tools in use by running agents).
5. Check D:/Projects subfolders for junk that can be cleaned inside _SIR only if clearly safe (build outputs, node_modules are regenerable but DO NOT delete them in this task — just list sizes).

## Output

Write the full plan to D:/Projects/_SIR/ops/plans/D_DRIVE_ORG_PLAN.md (create ops/plans if missing). Include the size table, classification, ranked move list, and a short "do not touch" list. In your final report summarize the top 5 biggest folders and the top 3 recommended moves.
