# netlify-blobs

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\codex\skills\netlify-blobs\SKILL.md`
- SKILL.md size: 13049 chars

## What it does

Store and retrieve unstructured objects, files, and cache-like state on Netlify with the @netlify/blobs module. Use when persisting user file uploads (images/documents), caching computed output from functions or Background Functions, serving downloadable assets, storing JSON blobs keyed by ID, or seeding deploy-specific data. Reach for this for key/value or object storage from Functions, Edge Functions, or Build Plugins — not for per-user, transactional, or relational data (use Netlify DB for that). Triggers include "save an uploaded file", "cache API results", "store generated site map", "key/value store for a function", or "file uploads without a database".

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
