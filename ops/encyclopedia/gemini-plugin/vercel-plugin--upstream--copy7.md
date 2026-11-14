# upstream

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\flags-sdk\upstream\SKILL.md`
- SKILL.md size: 23314 chars

## What it does

> Implement feature flags in Next.js or SvelteKit code with the Flags SDK (`flags` npm package). Use when installing or configuring the SDK, declaring flags with `flag()`, setting up Project Connections, wiring a provider adapter (`@flags-sdk/vercel`, Statsig, LaunchDarkly, PostHog, GrowthBook, Global Config, OpenFeature, Split, Flagsmith, Reflag, Optimizely, or custom), using `identify`, `dedupe`, or `evaluate`, keeping pages static with precompute, setting up Flags Explorer and the Vercel Toolbar, or encrypting flag values. Triggers: `flags/next`, `flags/sveltekit`, `flags/react`, `@flags-sdk/*`, `vercelAdapter`, precompute. For planning a flag, for Vercel Flags rollouts, experiments, and the `vercel flags` CLI, or for other frameworks, use the `vercel-flags` skill.

## When to use (from skill text)

- Use this flow when the flag was created in the dashboard or by someone else, for example when the prompt says the flag "has already been created" or asks you to run `vercel flags inspect`. Do not run `vercel flags create` for an existing key.

## Structure (headings inside SKILL.md)

- Set up and use the Flags SDK
- Core concepts
- Flags as code
- Server-side evaluation
- Adapter pattern
- Set up the SDK
- Before you start
- Steps
- Pull environment variables
- Create a flag
- Before you start
- Steps
- Add a flag that already exists on Vercel
- Vercel Flags adapter
- Declaring flags
- Basic flag
- Flag with evaluation context
- Flag with another adapter
- Key parameters
- Dedupe
- Bulk evaluation
- Flags Explorer setup
- Next.js (App Router)
- With external provider data
- SvelteKit
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2. **Link the project to Vercel** (required for `vercel env pull` and local OIDC token refresh):
- - local evaluation fails with an authentication error; the SDK refreshes an expired token through the linked project, re-pulling is the fallback
- - `defaultValue`: the value to serve when the flag is archived or evaluation fails (usually what production serves today)

## Key rules (verbatim lines from SKILL.md)

1. 2. **Link the project to Vercel** (required for `vercel env pull` and local OIDC token refresh):
2. 5. **Ensure `flags.ts` exists**: If missing, create `flags.ts` (or `lib/flags.ts` / `src/flags.ts` to match the project) with `export {}` so TypeScript treats it as a module. Flags Explorer imports this file — create it before the discovery route.
3. 6. **Set up Flags Explorer** (if not already present): Create `app/.well-known/vercel/flags/route.ts` — see [Flags Explorer setup](#flags-explorer-setup). Do this only after `flags.ts` exists. Point the import at the real flags file path (the snippet assumes root `flags.ts`).

## Files inside the skill

- `references/api.md` — "API Reference"
- `references/nextjs.md` — "Next.js Integration"
- `references/providers.md` — "Provider Adapters"
- `references/sveltekit.md` — "SvelteKit Integration"
