# netlify-config

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-config\SKILL.md`
- SKILL.md size: 15999 chars

## What it does

Configure Netlify builds and routing via.

## Structure (headings inside SKILL.md)

- Netlify configuration
- Modern vs legacy syntax to reach for
- `netlify.toml` build + contexts
- Redirects and rewrites
- Proxies
- Custom headers
- Functions
- Environment variables
- Injecting env values into headers/redirects
- Useful read-only build vars
- Secrets Controller
- Sensitive variable policy (public repos only)
- Ignore builds
- Monorepos
- JavaScript SPAs
- Netlify Dev `[dev]`
- Plugins & extensions
- Netlify house rules (config)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Secret values are **write-only** — no readable version after set; the flag can't be removed to reveal it.
- - Secrets need explicit contexts + scopes; **cannot** carry the `post processing` scope.
- - `SECRETS_SCAN_ENABLED=false` — disables **all** scanning (loses all secret protection).
- - `SECRETS_SCAN_SMART_DETECTION_ENABLED=false` — disables smart detection only.

## Key rules (verbatim lines from SKILL.md)

1. - Functions bundler: use `node_bundler = "esbuild"`. `zisi` is the legacy JS default; TypeScript always uses `esbuild`.
2. - Headers apply only to files from Netlify's store — **NOT** to proxied content or function/edge (SSR) responses; those must set their own headers.
3. - Secret values are **write-only** — no readable version after set; the flag can't be removed to reveal it.
4. - Only code on Netlify (edge/serverless/build) reads unmasked values; off-Netlify sees masked. The `dev`-context value is exempt (unmasked from UI/CLI/API); `netlify build` never emits raw values.
5. - **Require approval** (default) — untrusted deploys wait for a member's approval.

## Files inside the skill

- (SKILL.md only)
