# netlify-blobs (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-blobs\SKILL.md`. Object/file/cache storage via `@netlify/blobs`.

## Summary
Key/value object storage for Netlify Functions, Edge Functions, and Build Plugins — `getStore(name)`/`getDeployStore(name)`/`listStores`, `set`/`setJSON`/`get`/`getJSON`/`delete` with metadata support. Context (`siteID`, `deployID`, `token`, `region`) auto-injected server-side; install `npm i @netlify/blobs`. CRITICAL store-scope footgun: `getStore` = site-wide store SHARED across ALL deploy contexts — preview code reads/writes/deletes PRODUCTION data; never run destructive tests or seed throwaway data from a preview against it. Use `getDeployStore` for isolation (stays in sync on rollback, cleaned on deploy deletion). Build plugins can READ any store but WRITE only deploy-specific stores; file-based uploads write only to deploy stores. Blobs is NOT a database — optimized for frequent reads/infrequent writes; per-user/transactional/relational data → Netlify DB.

## When to use / when NOT
Use for user file uploads, caching computed function output, downloadable assets, JSON blobs by ID, deploy-seeded data. NOT for relational/per-user transactional data (→ Netlify DB), and never for destructive testing from previews.

## Inputs, outputs, tools
- Inputs: store name, key, value (ArrayBuffer/Blob/string/JSON), metadata.
- Outputs: stored/retrieved objects with metadata; deploy-scoped or site-wide persistence.
- Tools: `@netlify/blobs` npm module; Functions/Edge Functions/Build Plugins runtime.

## 5 most important rules
1. `getStore` is site-wide and shared with production — previews see/mutate prod data; use `getDeployStore` for anything risky.
2. Build plugins write ONLY to deploy stores; reads can hit any store.
3. It's object storage, not a DB — no relational/transactional guarantees; use Netlify DB for that.
4. Read-optimized: frequent reads, infrequent writes.
5. Context params auto-inject — don't hardcode siteID/deployID/token.

## Risks / owner notes
The site-wide store footgun can corrupt production data from a preview deploy — the #1 hazard. No transactions/consistency guarantees; large blobs have practical limits.

## Category and tags
Category: cloud. Tags: netlify, blobs, storage, kv, cache, deploy-scoping, functions.
