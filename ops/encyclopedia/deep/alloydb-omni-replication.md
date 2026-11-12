# alloydb-omni-replication

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-replication\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A replication and high-availability skill for AlloyDB Omni that sets up synchronous and asynchronous replication between clusters, monitors replica health, and performs failover operations. It manages replication clusters, monitors replication lag, promotes read replicas to primary, and handles failover without data loss when using synchronous replication with quorum.

## When to use / when NOT
Use when deploying AlloyDB Omni in a production environment that requires high availability or when migrating from a single-node setup to a multi-node cluster. Do NOT configure replication without first designing a failover plan — the skill will set up the infrastructure, but the owner must define which replica promotes to primary during an outage. Do NOT use asynchronous replication alone for critical workloads; the skill recommends synchronous with quorum for zero-data-loss guarantees.

## Inputs, outputs, tools
- Inputs: source cluster connection string, target replica connection strings, replication type (sync, async), failover policy, health check intervals.
- Outputs: replication topology diagram, replica status (healthy/lagging/caught_up), failover test results, promoted primary node, replication lag metrics.
- Tools: `gcloud alloydb replicas`, `psql`, `pg_stat_replication`, `kubectl get pods` (if on Kubernetes), `alloydb-failover` CLI. MCP: gemini-plugin connector.

## 5 most important rules
1. **Use synchronous replication with quorum for zero-data-loss HA** — the skill configures this by default; asynchronous-only should only be used for read-only analytics workloads.
2. **Set a replica lag threshold of 5 seconds** — if a replica falls behind by more than 5 seconds, the skill will generate a warning and recommend promotion or investigation.
3. **Test failover in a staging environment before production** — the skill can simulate a primary outage; verify that the correct replica promotes and that application connections re-establish.
4. **Monitor the `pg_replication_slot` health** — missing or disabled replication slots will cause replication to stop; the skill alerts on this.
5. **Keep all cluster nodes on the same AlloyDB version** — mixing versions can cause replication incompatibilities; the skill will warn if version skew is detected.

## Risks / owner notes
Asynchronous replication can result in data loss if the primary fails before replication lag is resolved. The owner should understand the trade-off between performance (async) and data safety (sync with quorum). Failover tests that are never run may result in the wrong replica promoting or applications failing to reconnect; always test in staging first.

## Category / tags
database · replication, high-availability, alloydb, postgres, ha, failover

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.