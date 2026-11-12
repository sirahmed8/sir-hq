# vercel-storage

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-storage\SKILL.md`
- SKILL.md size: 15456 chars

## What it does

Vercel storage expert guidance.

## When to use (from skill text)

- **Use when**: Media files, user uploads, documents, any large unstructured data.
- **Use when**: Feature flags, A/B testing config, dynamic routing rules, maintenance mode toggles. Anything that must be read at the edge with near-zero latency.

## Structure (headings inside SKILL.md)

- Vercel Storage
- Provider Choice for Bootstrap
- Active First-Party Storage
- Vercel Blob — File Storage
- Vercel Global Config (formerly Edge Config)
- Marketplace Storage (Partner-Provided)
- IMPORTANT: @vercel/postgres and @vercel/kv are SUNSET
- Neon Postgres (replaces @vercel/postgres)
- Option 1: Source env vars before running
- Option 2: Use dotenv-cli (recommended for scripts)
- Upstash Redis (replaces @vercel/kv)
- Supabase (Marketplace Native)
- Prisma Postgres (Marketplace Native)
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
- Cross-References
- Official Documentation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2. Add the pooled string under a new name, for example `vercel env add DATABASE_URL_POOLED production`, once per connected environment. Don't overwrite the integration's variables.

## Key rules (verbatim lines from SKILL.md)

1. 2. **Fallback**: Provider CLI/manual provisioning only when Marketplace is unavailable or you must use an existing external account.
2. 2. Add the pooled string under a new name, for example `vercel env add DATABASE_URL_POOLED production`, once per connected environment. Don't overwrite the integration's variables.

## Files inside the skill

- (SKILL.md only)
