# alloydb-omni-lifecycle

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-lifecycle\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A lifecycle management skill for AlloyDB Omni that orchestrates the full lifespan of a database cluster from creation to deletion. It handles provisioning, version upgrades, patching, scaling (storage and compute), backup management, and graceful decommissioning. The skill maintains a lifecycle state machine that ensures each operation is performed in the correct order and that rollbacks are available if an operation fails.

## When to use / when NOT
Use when starting a new AlloyDB Omni cluster, upgrading an existing cluster to a new version, or scaling compute/storage resources. Do NOT skip the backup verification step before any upgrade — the skill will create a snapshot but the owner must verify it is restorable. Do NOT attempt manual scaling via kubectl or gcloud without running the skill first — the lifecycle state machine will become out of sync and may prevent future operations.

## Inputs, outputs, tools
- Inputs: operation type (create, upgrade, scale, backup, delete), cluster name/identifier, target version, storage delta, backup retention period.
- Outputs: operation status (success/failed/rolling-back), new cluster version, updated resource sizes, backup snapshot ID, decommission confirmation.
- Tools: `gcloud alloydb`, `kubectl`, `gcloud backup`, `pg_dump`, `psql`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always verify the latest backup is restorable before upgrading** — the skill creates a snapshot, but you must test a point-in-time restore on a staging cluster first.
2. **Scale storage and compute in separate operations** — do not combine a storage increase with a compute increase in a single call; the skill handles them as separate state transitions.
3. **Use the skill's dry-run mode for any destructive operation** — the `delete` operation will show what will be removed without actually removing it; review the list before confirming.
4. **Maintain a minimum of 3 backup snapshots** — the skill rotates snapshots; having at least 3 ensures you can roll back to any of the last 3 states.
5. **Document the lifecycle state after each operation** — the skill writes the current state to a file; do not delete this file as it is needed for the next operation.

## Risks / owner notes
The biggest risk is upgrading without a verified backup — if the upgrade introduces incompatibilities, the only rollback is to the last verified backup. The owner should schedule backup restore tests quarterly. Lifecycle state desynchronization (caused by manual gcloud/kubectl commands) is the second most common issue; always use the skill for all lifecycle operations.

## Category / tags
database · lifecycle, provisioning, alloydb, postgres, upgrade, scaling, delete

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.