# alloydb-omni-container

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-container\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A skill for deploying and managing AlloyDB Omni instances as Kubernetes stateful sets or Docker containers. It handles the full lifecycle from cluster creation (on-premises, cloud, or hybrid) to configuration, scaling, monitoring, and teardown. The skill integrates with the AlloyDB CSI driver for persistent storage, promotes connection pooling via PgBouncer, and provides health checks and auto-recovery for database pods.

## When to use / when NOT
Use when you need to run AlloyDB Omni in a containerized environment (Kubernetes or Docker Compose) and want automated lifecycle management. Do NOT use if you are running AlloyDB directly on bare metal without container orchestration — the skill's automation assumes a container runtime. Do NOT skip the storage configuration step; AlloyDB Omni requires persistent PVCs for data durability, and the skill will fail without a valid storage class.

## Inputs, outputs, tools
- Inputs: Kubernetes cluster name or Docker host, AlloyDB version, storage class name, initial database name and user, resource limits (CPU, memory).
- Outputs: deployed AlloyDB stateful set or container, PgBouncer connection pool configuration, health check results, logs tail, connection string for the deployed instance.
- Tools: `kubectl`, `docker compose`, `gcloud` AlloyDB API, `kubectl get storageclass`, `pg_isready` for health checks. MCP: google-maps-platform (for workload placement), gemini-plugin connector.

## 5 most important rules
1. **Always specify a persistent volume claim** with a storage class that supports ReadWriteOnce or ReadWriteMany — AlloyDB Omni data cannot reside in ephemeral volumes.
2. **Set PgBouncer connection pooling** with `max_connections` appropriate to your workload; the default of 100 may be too low for connection-heavy applications.
3. **Configure liveness and readiness probes** using `pg_isready`; without probes, Kubernetes will not auto-recover a crashed AlloyDB instance.
4. **Enable automatic backups** via the AlloyDB API; the skill can schedule daily snapshots and retain them for a configurable number of days.
5. **Use label selectors for monitoring** — tag all AlloyDB pods with `app=alloydb,instance=<name>` so Prometheus can scrape metrics correctly.

## Risks / owner notes
Storage misconfiguration is the most common cause of data loss — if the PVC is deleted or the storage class is changed, AlloyDB data may be lost. The owner should test backup restore procedures quarterly. Resource overcommit (requesting more CPU/memory than the node can provide) will cause Kubernetes to evict the AlloyDB pod.

## Category / tags
database · kubernetes, docker, container-orchestration, alloydb, postgres, deployment, observability

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.