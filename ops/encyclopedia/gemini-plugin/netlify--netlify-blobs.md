# netlify-blobs

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-blobs\SKILL.md`
- SKILL.md size: 12688 chars

## What it does

Store and retrieve unstructured objects.

## Structure (headings inside SKILL.md)

- Netlify Blobs
- Choosing a store type
- Core writes and reads
- Persisting a user upload (Function)
- Reading (Function)
- Metadata and conditional reads
- Concurrency: atomic conditional writes
- Listing
- Deleting
- Expiration (no server-side TTL)
- Consistency
- Regions
- File-based uploads (no build plugin)
- Access control (default to private)
- Constraints
- When an operation fails
- CLI and UI
- Module version migration
- Reference
- Netlify house rules (blobs)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `getStore(name)`: site-wide and shared across all deploys. Data persists across deploys, and previews see production data.
- - Local dev (Netlify Dev) uses a sandboxed local store. It does not support file-based uploads and cannot read production data.
- 3. `netlify blobs:list/get/set/delete` exist for inspection; the CLI

## Key rules (verbatim lines from SKILL.md)

1. - `getDeployStore(name)`: deploy-specific and scoped to one deploy. It stays in sync on rollback and is cleaned up on deploy deletion. Use it for isolation and for anything a failed deploy must not corrupt.
2. - **Site-wide stores** default to `us-east-2` and do NOT follow your functions region.
3. - The Fetch API is required (Node.js 18+). Otherwise pass a custom `fetch`: `getStore({ fetch, name: "file-uploads" })`.
4. - File-based uploads require continuous deployment or CLI deploys.
5. 6. Don't build counters, balances, or read-modify-write logic on a blob key —

## Files inside the skill

- (SKILL.md only)
