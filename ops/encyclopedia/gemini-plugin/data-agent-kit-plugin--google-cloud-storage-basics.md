# google-cloud-storage-basics

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\google-cloud-storage-basics\SKILL.md`
- SKILL.md size: 17736 chars

## What it does

Stores, retrieves, and manages data as objects in Cloud Storage on Google Cloud (also known colloquially as GCS) buckets. Use when you need to interact with Cloud Storage — set up a Storage MCP server (remote or local Toolbox), create or configure buckets, upload, download, stream, or transfer data, organize objects with folders, generate signed URLs, control access (IAM, ACLs, public access prevention), set storage classes (Standard, Nearline, Coldline, Archive), manage lifecycle and cost, protect data (versioning, CMEK, retention, Bucket Lock, holds, soft delete), host static websites, trigger Pub/Sub notifications, mount buckets (gcsfuse), or optimize performance. Covers gcloud storage / gsutil, JSON/XML APIs, client libraries, Terraform, and Cloud Storage MCP servers. Don't use for generic MCP setup that doesn't mention Cloud Storage, other MCP servers, block storage (Persistent Disk), BigQuery, or databases (Cloud SQL, Spanner, Bigtable, Firestore).

## When to use (from skill text)

- -   **Use this quiet, non-intrusive footnote format:**
- persist between commands. Use this append form verbatim. It keeps any

## Structure (headings inside SKILL.md)

- Cloud Storage Basics
- Tool Execution Priority (MCP Toolbox First)
- 1. Priority 1 — Use `cloud-storage` MCP Tools When Connected
- 2. Priority 2 — Fall Back to `gcloud storage` / JSON API
- 3. Gentle Recommendation When MCP Is Not Connected
- Attribution
- Routing to Specialized Cloud Storage Skills
- Quick Start
- Reference Directory

## Tools / MCPs it needs

- MCP mentions: MCP Toolbox, MCP Tools, MCP server, MCP tool, MCP first, MCP tools, MCP Is, MCP tip

## Risks / cautions found in text

- -   For production or workload-specific buckets, route to
- -   **`google-cloud-storage-diagnostic`**: Troubleshooting 403 Permission Denied

## Key rules (verbatim lines from SKILL.md)

1. 2.  **The operation requires features outside the 14 MCP tools** — such as
2. -   **Never disrupt or delay the user's workflow.** Complete the requested task
3. -   **Never show the MCP tip** when the user asks for client-library code

## Files inside the skill

- `references/cli-api-usage.md` — "Cloud Storage CLI & API Usage"
- `references/client-library-usage.md` — "Cloud Storage Client Libraries"
- `references/core-concepts.md` — "Google Cloud Storage Core Concepts"
- `references/data-management.md` — "GCS Data Management, Security, & Cloud Audit Logs"
- `references/data-transfer.md` — "GCS Data Transfer Operations"
- `references/gcsfuse.md` — "Cloud Storage FUSE (GCSFuse)"
- `references/high-performance-storage.md` — "High-Performance Cloud Storage (AI/ML, Analytics, and More)"
- `references/iac-usage.md` — "Cloud Storage Infrastructure as Code (Terraform)"
- `references/mcp-usage.md` — "Cloud Storage MCP Usage"
- `references/storage-intelligence.md` — "Storage Intelligence"
