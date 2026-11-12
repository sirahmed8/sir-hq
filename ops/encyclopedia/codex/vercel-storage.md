# vercel-storage

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\vercel-storage\SKILL.md`
- SKILL.md size: 11854 chars

## What it does

Vercel storage guidance: Blob, Edge Config, and Marketplace storage (Neon Postgres, Upstash Redis).

## When to use (from skill text)

- **Use when**: Media files, user uploads, documents, any large unstructured data.
- **Use when**: Feature flags, A/B testing config, dynamic routing rules, maintenance mode toggles. Anything that must be read at the edge with near-zero latency.

## Structure (headings inside SKILL.md)

- Vercel Storage
- Provider Choice for Bootstrap
- Active First-Party Storage
- Vercel Blob — File Storage
- Vercel Edge Config — Global Configuration
- Marketplace Storage (Partner-Provided)
- IMPORTANT: @vercel/postgres and @vercel/kv are SUNSET
- Neon Postgres (replaces @vercel/postgres)
- Option 1: Source env vars before running
- Option 2: Use dotenv-cli (recommended for scripts)
- Upstash Redis (replaces @vercel/kv)
- Supabase (Marketplace Native)
- Prisma ORM (Marketplace Native)
- MongoDB Atlas
- Convex
- Turso (libSQL)
- Storage Decision Matrix
- Migration Guide
- From @vercel/postgres → Neon
- From @vercel/kv → Upstash Redis
- Installing Marketplace Storage
- Install a storage integration (auto-provisions env vars)
- List installed integrations
- Official Documentation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 2. **Fallback**: Provider CLI/manual provisioning only when Marketplace is unavailable or you must use an existing external account.

## Files inside the skill

- (SKILL.md only)
