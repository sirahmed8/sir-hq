# alloydb-omni-access-control

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-access-control\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A database access control skill for Google Cloud AlloyDB Omni that manages user roles, permissions, and connection policies across on-premises, cloud, and Kubernetes-deployed AlloyDB clusters. It integrates with IAM, Google Cloud Identity, and Kubernetes RBAC to ensure that only authorized principals can read, write, or manage AlloyDB databases. The skill also handles SSL/TLS certificate rotation for database connectivity and audits access logs for anomalous patterns.

## When to use / when NOT
Use when provisioning AlloyDB Omni clusters in hybrid or multi-cloud environments and you need to enforce least-privilege access for database users and applications. Do NOT deploy without first defining role mappings — AlloyDB Omni defaults to unrestricted access if no IAM policies are set. Do NOT manage database users solely through SQL GRANT/REVOKE statements for production environments; the skill provides a centralized IAM layer that is more auditable and enforceable.

## Inputs, outputs, tools
- Inputs: cluster connection string, IAM principal emails, Kubernetes service account names, SSL certificate details, desired role assignments (read-only, read-write, admin).
- Outputs: configured IAM policies, role bindings, SSL certificate thumbprints, access audit report, revocation list.
- Tools: `gcloud` CLI, `kubectl` with AlloyDB add-on, Google Cloud Console IAM page, `psql` for initial connection testing. MCP: google-maps-platform (for geo-related access patterns), gemini-plugin connector.

## 5 most important rules
1. **Always use IAM roles rather than SQL-level grants** for application connectivity — IAM is the source of truth for AlloyDB Omni access control.
2. **Bind Kubernetes service accounts to AlloyDB users** via the AlloyDB CSI driver; never expose database passwords in pod specifications.
3. **Rotate SSL/TLS certificates every 90 days** and invalidate old connection strings immediately — rotated certificates must be redeployed via the skill's certificate management workflow.
4. **Audit access logs weekly** for failed connection attempts or privilege escalation attempts; the skill can generate a filtered report by IP, user, or time range.
5. **Never grant ALL PRIVILEGES to a service account** — use custom IAM roles with only the minimum operations needed (select, insert, update, delete, backup).

## Risks / owner notes
Misconfigured IAM policies can lead to data breaches if a compromised service account gains excessive database rights. The owner should enforce periodic IAM audits and use the principle of least privilege. Certificate rotation failures are a common operational issue; automate the rotation workflow to avoid manual gaps.

## Category / tags
database · google-cloud, alloydb, access-control, iam, kubernetes, sql, security

## Revisions
The gemini revision is the only one available; codex, kilo, and cursor do not have AlloyDB skills. This is the canonical source.