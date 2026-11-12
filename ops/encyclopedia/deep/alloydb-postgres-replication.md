# alloydb-postgres-replication

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-replication\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A replication skill for PostgreSQL within AlloyDB Omni that sets up streaming replication between primary and replica clusters, monitors replication status, and performs failover operations. It manages replication slots, monitors replication lag, and can promote a read replica to primary status during an outage. The skill also handles recovery after a failover, ensuring that the new primary has caught up with all WAL changes.

## When to use / when NOT
Use when deploying AlloyDB Omni with read replicas for load balancing or high availability. Do NOT configure streaming replication without first ensuring network connectivity between clusters and compatible AlloyDB versions — the skill will validate these before proceeding. Do NOT use asynchronous replication alone for critical workloads requiring zero data loss; the skill recommends synchronous replication with slot retention for HA scenarios.

## Inputs, outputs, tools
- Inputs: primary cluster connection string, replica connection strings, replication type (sync, async), slot management policy, failover promotion policy.
- Outputs: replication topology diagram, replication status (healthy/lagging/caught_up), replication lag metrics, failover test results, promoted primary node confirmation.
- Tools: `psql`, `pg_basebackup`, `pg_replication_slot`, `pg_stat_replication`, `gcloud alloydb replicas`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always create a replication slot before starting streaming replication** — the skill will create a named slot; losing the slot will cause replication to stop and data to diverge.
2. **Set a replication lag threshold of 5 seconds** — if a replica falls behind by more than 5 seconds, the skill will generate a warning and recommend promotion or investigation.
3. **Test failover in a staging environment before production** — the skill can simulate a primary outage; verify that the correct replica promotes and that application connections re-establish.
4. **Retain replication slots for at least 24 hours after a failover** — the skill manages slot lifecycle; premature deletion can cause replication issues when the old primary reconnects.
5. **Keep all cluster nodes on the same AlloyDB version** — version skew between primary and replica can cause replication incompatibilities; the skill will warn if version mismatch is detected.

## Risks / owner notes
Asynchronous replication can result in data loss if the primary fails before replication lag is resolved. The owner should understand the trade-off between performance (async) and data safety (sync with slot retention). Failover tests that are never run may result in the wrong replica promoting or applications failing to reconnect; always test in staging first. Replication slot accumulation (if slots are not cleaned up) can grow unbounded and consume disk space.

## Category / tags
database · replication, ha, postgres, alloydb, failover, streaming-replication

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.