# netlify-frameworks

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\codex\skills\netlify-frameworks\SKILL.md`
- SKILL.md size: 14660 chars

## What it does

Deploy and configure web frameworks on Netlify — build settings and SSR/edge adapters plus local platform emulation and env vars. Use when setting up or fixing a framework deploy (Next.js / Astro / Nuxt / SvelteKit / Remix / React Router / TanStack Start / SolidStart / Gatsby / Angular / Vite / Express / Hydrogen / Hugo / Eleventy / Vue / React), adding SSR or edge functions or middleware wired to Netlify context, fixing SPA redirect and catch-all rules, setting a build command or publish directory, or debugging "why isn't my env var updating" and framework build failures.

## Structure (headings inside SKILL.md)

- Env vars: modern rules (read first)
- SPA redirects and the SSR catch-all footgun
- Local dev with platform emulation (no Netlify CLI)
- Build settings by framework
- SSR / adapter setup
- Astro
- Next.js (13.5+ only)
- SvelteKit
- React Router (7+)
- Remix
- Nuxt
- SolidStart
- TanStack Start
- Gatsby
- Angular
- Express
- Hydrogen
- Static-site gotchas
- Hugo
- Eleventy
- Vite meta-framework support matrix
- Deploy via CLI (Express, Nuxt, React, Vite)
- Netlify house rules (frameworks)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Edge functions don't work locally with `netlify dev` for SvelteKit.
2. - SSR on Edge Functions requires a different Nitro deployment preset (not auto-detected).
3. - **5.11.0 or earlier (Essential Gatsby plugin):** auto-installs `@netlify/plugin-gatsby`; also manually install `gatsby-plugin-netlify` (required for SSR, Gatsby redirects, asset caching). Generates `__api`, `__ssr`, `__dsg`, `__ipx`. Skip via `NETLIFY_SKIP_GATSBY_FUNCTIONS` (all) / `NETLIFY_SKIP_A
4. - Gatsby 5 requires Node 18.
5. - Large sites: set `GATSBY_EXCLUDE_DATASTORE_FROM_BUNDLE` to load datastore from CDN (avoids max function deploy size; slower first SSR/DSG load).

## Files inside the skill

- `references/astro.md` — "Astro on Netlify"
- `references/nextjs.md` — "Next.js on Netlify"
- `references/nuxt.md` — "Nuxt on Netlify"
- `references/sveltekit.md` — "SvelteKit on Netlify"
- `references/tanstack.md` — "TanStack Start on Netlify"
- `references/vite.md` — "Vite + React on Netlify"
