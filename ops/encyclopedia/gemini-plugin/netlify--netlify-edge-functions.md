# netlify-edge-functions

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-edge-functions\SKILL.md`
- SKILL.md size: 17299 chars

## What it does

Write, route, cache, and debug Netlify Edge.

## When to use (from skill text)

- ## Use this form

## Structure (headings inside SKILL.md)

- Netlify Edge Functions
- Use this form
- ⚠️ Footguns
- Files
- Return values
- Endpoint
- Redirect / rewrite
- Middleware (modify origin response)
- Conditional requests
- Read body, then continue
- Netlify user gate (private / team-login-protected projects)
- Post-response work
- Streaming SSR (`.tsx`)
- `Context`
- Declarations
- Inline `config`
- `netlify.toml`
- Order
- Response caching
- Error handling (`onError`)
- Environment variables
- Local dev / deploy / logs
- Limits
- Netlify house rules (edge-functions)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `Netlify.env.set()` or `Netlify.env.delete()` as persistence. They affect only the current invocation.
- - **Don't cache** routing or personalization middleware, such as cookie-based product ordering.

## Key rules (verbatim lines from SKILL.md)

1. - A file with no `config.path` or `pattern` and no `[[edge_functions]]` entry. It deploys but never runs.
2. - **Cached functions shadow static files.** A cached function on `/*` serves `/cat.png` instead of the file.
3. - **Returning a `Response` ends the chain.** Redirect rules for that path never run.
4. - **The request body can be read once.** After `await req.json()`, pass `new Request(req, { body })` to `context.next()`.
5. - **Custom Headers and basic-auth headers do not apply** to edge functions.

## Files inside the skill

- (SKILL.md only)
