# netlify-functions

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\codex\skills\netlify-functions\SKILL.md`
- SKILL.md size: 20232 chars

## What it does

Write, configure, and deploy Netlify serverless functions in TypeScript, JavaScript, or Go. Use this when adding an API endpoint or backend route, adding a contact form handler, wiring auth or Identity signup/login hooks, identifying which Netlify user is calling a private or team-login-protected app, building streaming or AI-proxy responses, scheduling cron jobs, running long background jobs (batch processing/scraping), reacting to deploy or form events, setting up rate limiting or region/memory config, or reading environment variables and secrets inside a function. Covers file locations, the Request/Context/Response handler shape, path routing, config options, and local testing with netlify dev.

## Structure (headings inside SKILL.md)

- Netlify Functions
- File locations
- Minimal function
- Custom path routing
- Fetchable module shape (alternative)
- Context object
- Who is calling: `context.user`
- Config object
- Integrations
- Streaming responses
- Background functions (long-running)
- Scheduled functions (cron)
- Platform-event functions
- Region
- Memory / vCPU
- Bundling & files on disk
- Limits (not configurable)
- Local testing & deploy
- Node runtime version
- Legacy / Go (avoid unless needed)
- Netlify house rules (functions)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `excludedPath`: carve exceptions, e.g. `excludedPath: ["/product/*.css"]` with `path: "/product/*"`.
- - `context.cookies` — `get(name)` / `set(options)` / `delete(name|options)`. Cross-subdomain cookies need a custom domain (`netlify.app` is on the Public Suffix List).
- - `context.waitUntil(promise)` — run work after the response is sent (analytics, logs) without blocking. Billing/log duration counts until the promise settles. Available for functions deployed on/after 2025-03-20.
- 4. Store secrets in environment variables, never in code.

## Key rules (verbatim lines from SKILL.md)

1. - `context.waitUntil(promise)` — run work after the response is sent (analytics, logs) without blocking. Billing/log duration counts until the promise settles. Available for functions deployed on/after 2025-03-20.
2. - `path` / `excludedPath` — `string | string[]`, must start with `/`.
3. - Scheduled functions don't fire on a schedule locally — invoke once with `netlify functions:invoke <name>`.
4. 3. Never add CORS headers unless explicitly requested.
5. 4. Store secrets in environment variables, never in code.

## Files inside the skill

- (SKILL.md only)
