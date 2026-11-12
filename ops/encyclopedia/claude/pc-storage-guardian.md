# pc-storage-guardian

- Tool: `claude`
- Category: automation
- Source: `C:\Users\a7med\.claude\skills\pc-storage-guardian\SKILL.md`
- SKILL.md size: 3121 chars

## What it does

Use when checking disk capacity, pruning temp and cache folders safely, or protecting SSD health on a Windows PC.

## When to use (from skill text)

- - Batch pruning operations to scheduled intervals (e.g., 6-hour cron cycle or manual triggers).

## Structure (headings inside SKILL.md)

- PC Storage Guardian & Telemetry Engine
- 1. Storage Capacity Telemetry & Alerting
- 2. Safe Temporary & Cache Pruning Targets
- Approved Pruning Targets
- 3. Safe Exception Handling & Locking Rules
- 4. Execution Workflow
- 1. Run PC Cleaner in dry-run mode to inspect reclaimable space
- 2. Run real non-destructive purge
- 3. Clean npm global cache
- 4. Verify post-cleanup disk capacity
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - At this threshold, Windows pagefile thrashing, hibernation file sizing, and Antigravity workspace contexts risk sudden failure.
- - Policy: Delete files older than 24 hours. Gracefully skip files locked by running processes.
- - Policy: Delete stale OS patch remnants and installer logs.
- - Policy: Delete `.dmp` files from previous application terminations.

## Key rules (verbatim lines from SKILL.md)

1. 1. **In-Use File Handling**: Always wrap file unlinks and folder deletions in `try...except` blocks. If an application (e.g. browser, editor, Discord) has an open handle on a file, gracefully skip it without halting the cleaner.
2. - Avoid aggressive micro-deletions every few seconds.
3. - Never defragment NVMe solid-state storage (TRIM is handled natively by Windows).

## Files inside the skill

- (SKILL.md only)
