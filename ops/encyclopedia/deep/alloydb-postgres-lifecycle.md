# alloydb-postgres-lifecycle

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-lifecycle\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A lifecycle management skill for PostgreSQL deployed on AlloyDB Omni, handling the full lifespan from initial deployment to version upgrades, scaling, and decommissioning. It integrates with the AlloyDB Omni lifecycle framework to ensure consistent state management across the PostgreSQL layer, and provides rollback points before any major operation.

## When to use / when NOT
Use for any PostgreSQL lifecycle operation on AlloyDB Omni — deployment, version upgrade, or decommission. Do NOT skip the pre-operation snapshot; the skill creates a backup before any lifecycle operation and the owner must verify it is restorable. Do NOT attempt manual PostgreSQL upgrades via `pg_upgrade` without running the skill first — the lifecycle state machine will become out of sync and may block future operations.

## Inputs, outputs, tools
- Inputs: operation type (deploy, upgrade, scale, decommission), PostgreSQL version, resource parameters (CPU, memory, storage), backup retention.
- Outputs: lifecycle status, new version confirmation, resource size updates, backup snapshot ID, decommission confirmation.
- Tools: `psql`, `gcloud alloydb`, `pg_upgrade` (invoked internally by the skill), `pg_dump`, `pg_restore`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always create and verify a backup before any upgrade operation** — the skill automates the backup, but the owner must test a restore on a staging cluster before proceeding.
2. **Scale storage and compute in separate lifecycle operations** — do not combine a storage increase with a version upgrade in a single call; the skill handles them as separate state transitions.
3. **Use the skill's dry-run mode for decommission** — the `decommission` operation will show what will be removed without actually removing it; review the list before confirming.
4. **Maintain a minimum of 3 backup snapshots** — the skill rotates snapshots; having at least 3 ensures you can roll back to any of the last 3 states.
5. **Document the lifecycle state after each operation** — the skill writes the current state to a file; do not delete this file as it is needed for the next operation.

## Risks / owner notes
The biggest risk is upgrading without a verified backup — if the upgrade introduces incompatibilities, the only rollback is to the last verified backup. The owner should schedule backup restore tests quarterly. Lifecycle state desynchronization (caused by manual `pg_upgrade` or `gcloud` commands) is the second most common issue; always use the skill for all lifecycle operations.

## Category / tags
database · lifecycle, postgres, alloydb, upgrade, scaling, decommission

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.