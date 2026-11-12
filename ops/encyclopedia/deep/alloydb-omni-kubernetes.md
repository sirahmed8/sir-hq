# alloydb-omni-kubernetes

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-kubernetes\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A skill for deploying AlloyDB Omni on Kubernetes clusters using the AlloyDB CSI driver and operator. It handles cluster provisioning, configuration, connection pooling, and upgrade management. The skill also provides manifests for service accounts, RBAC roles, and storage classes required for AlloyDB Omni to operate in a Kubernetes environment.

## When to use / when NOT
Use when deploying AlloyDB Omni on a new or existing Kubernetes cluster and you need automated, repeatable deployment. Do NOT deploy manually with kubectl apply alone — the skill's operator ensures proper ordering of resources (CRDs, service accounts, RBAC, storage, then the AlloyDB instance). Do NOT skip the storage class validation step; AlloyDB Omni requires a specific storage class with retain and binding mode that the skill will verify before proceeding.

## Inputs, outputs, tools
- Inputs: Kubernetes cluster name/version, cloud provider (GKE, EKS, AKS), storage class name, AlloyDB version, resource requests/limits.
- Outputs: deployed AlloyDB cluster via AlloyDB Kubernetes operator, connection string, service endpoint, health check confirmation, operator status.
- Tools: `kubectl`, `gcloud` (for GKE), `eksctl` (for EKS), AlloyDB operator YAML manifests, `kubectl get crd`, `kubectl get all`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always install the AlloyDB operator before creating the cluster** — the operator manages the full lifecycle; manual kubectl apply can leave resources in inconsistent states.
2. **Use a storage class with `Retain` enabled** — if the PVC is deleted, the AlloyDB data must not be lost; the skill will fail if the storage class doesn't support retain.
3. **Configure RBAC with least-privilege service accounts** — the operator needs specific permissions (create, get, list, watch) for custom resources; never use cluster-admin for the operator service account.
4. **Set resource requests and limits** for the AlloyDB instance pod — without limits, a runaway query can consume all node resources and evict other pods.
5. **Verify the AlloyDB custom resource status is "READY"** before connecting applications — the skill will not report success until the operator has finished initializing the cluster.

## Risks / owner notes
The most common deployment failure is using a storage class without the `Retain` policy, resulting in data loss when the pod is deleted. The owner should validate the storage class before any production deployment. RBAC misconfiguration is also common; the skill's generated manifests should be reviewed and adjusted for your cluster's security policies.

## Category / tags
database · kubernetes, deployment, alloydb, postgres, operator, rbac, cloud-native

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.