# alloydb-omni-kubernetes

- Tool: `gemini`
- Category: build
- Source: `C:\Users\a7med\.gemini\skills\alloydb-omni-kubernetes\SKILL.md`
- SKILL.md size: 18169 chars

## What it does

You're an expert in AlloyDB Omni Operator running in Kubernetes. You can help users with related tasks such as creating, managing, and monitoring AlloyDB Omni DBClusters.

## When to use (from skill text)

- trigger a fail-over (faster, can have data loss), use the `failover` (fullname:
- `failovers.alloydbomni.dbadmin.goog`) resource. To trigger a switch-over
- autoFailoverTriggerThreshold: 3 # The number of failures after which failover is triggered.

## Structure (headings inside SKILL.md)

- Context
- Prerequisites
- Operator deep dive
- Resource Inspection
- Connecting to the Database
- Resource Hierarchy:
- Inspectin resources
- Connecting to the Database
- AlloyDB Omni on Kubernetes Configuration Samples
- DBCluster examples
- Minimal DBCluster
- This is a minimal DBCluster spec. See v1_dbcluster_full.yaml for more configurations.
- Full DBCluster
- DBCluster with ML agent
- DBCluster with load balancer
- DBCluster with Commvault sidecar
- Backup and Restore
- Backup plan
- Restore from backup
- Clone
- High Availability and Data Resilience
- Failover
- Switchover
- Monitoring and connection pooling
- PgBouncer configuration
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - key: "cloud.google.com/gke-local-nvme-ssd"
2. - key: "node-role.kubernetes.io/control-plane"
3. - key: another-node-label-key

## Files inside the skill

- (SKILL.md only)
