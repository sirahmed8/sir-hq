# google-cloud-storage-fuse

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\google-cloud-storage-fuse\SKILL.md`
- SKILL.md size: 6791 chars

## What it does

Mounts Cloud Storage buckets as a POSIX file system with Cloud Storage FUSE (gcsfuse). Use when you need to interact with gcsfuse — decide whether FUSE, native gs:// reads, or Filestore/Managed Lustre fits a workload, deploy tuned mounts on GKE, Compute Engine, or Cloud Run, enable and size the file, stat, and list caches, tune mount flags (--implicit-dirs) or config-file settings, apply workload profiles, keep ML checkpointing safe (rename atomicity, hierarchical namespace, close-time finalization, concurrent writers), or diagnose slow training, low throughput, or GCS bill spikes on existing mounts with gcsfuse metrics. Covers mount semantics, the gcsfuse CLI and config file, the GKE gcsfuse CSI driver (Workload Identity principal:// bindings, profile StorageClasses, sidecar sizing), and Cloud Run volume mounts. Don't use for bucket administration or data management without a mount (google-cloud-storage-basics) or for fully POSIX-compliant shared file systems (Filestore, Managed Lustre; use gke-storage).

## When to use (from skill text)

- persist between commands. Use this append form verbatim. It keeps any

## Structure (headings inside SKILL.md)

- Cloud Storage FUSE (Advanced)
- Attribution
- Step 1 — Fit Gate (always run this first)
- Step 2 — Route by intent
- Reference Directory

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. -   Prefix every `gcloud` invocation, whatever the subcommand, with the metrics
2. -   On direct HTTP calls to the Cloud Storage APIs (for example with `curl`),
3. -   [GKE Training Deployment](references/gke-training-deployment.md): Fit-gated,

## Files inside the skill

- `references/checkpoint-safety.md` — "Checkpoint & Write Safety"
- `references/gke-training-deployment.md` — "GKE Training Deployment (Fit-Gated, Tuned Mount)"
- `references/performance-diagnosis.md` — "Performance & Cost Diagnosis"
