# netlify-blobs

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-blobs\SKILL.md`
- SKILL.md size: 13049 chars
- Identical content to: `encyclopedia/gemini-plugin/netlify--netlify-blobs--copy2.md`

Auto-generated stub: this SKILL.md is byte-identical to `encyclopedia/gemini-plugin/netlify--netlify-blobs--copy2.md`. Read that digest for full details.

Description: Store and retrieve unstructured objects, files, and cache-like state on Netlify with the @netlify/blobs module. Use when persisting user file uploads (images/documents), caching computed output from functions or Background Functions, serving downloadable assets, storing JSON blobs keyed by ID, or seeding deploy-specific data. Reach for this for key/value or object storage from Functions, Edge Functions, or Build Plugins — not for per-user, transactional, or relational data (use Netlify DB for that). Triggers include "save an uploaded file", "cache API results", "store generated site map", "key/value store for a function", or "file uploads without a database".