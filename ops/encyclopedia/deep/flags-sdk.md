# flags-sdk

## Summary
Implementation guide for the Flags SDK (`flags` npm package, renamed from `@vercel/flags`) — feature flags as callable functions for Next.js and SvelteKit, evaluated server-side with any provider via the adapter pattern (Vercel Flags first-party via `@flags-sdk/vercel`, plus Statsig/LaunchDarkly/PostHog/etc.). Covers full project setup (install → `vercel link` → `vercel env pull` → Toolbar → flags.ts → Flags Explorer route), creating flags (`vercel flags create --kind` then declare with vercelAdapter), adding dashboard-created flags (`vercel flags inspect` → map kind/variants to type param/defaultValue/options/identify), evaluate() bulk evaluation (~10x faster via bulkDecide), dedupe'd identify for targeting, the precompute pattern for static pages (middleware encodes flag state into URL rewrite), FLAGS_SECRET handling, and encryption helpers for Flags Explorer.

## When to use / when NOT
Use for implementing/configuring flags IN CODE inside a Next.js or SvelteKit app. Planning flags, dashboard management, archiving/deleting variants, and non-Vercel frameworks belong to the `vercel-flags` skill / `@vercel/flags-core` — do NOT run archive/rm flows here. Inside an app repo, treat ambiguous requests as the full setup flow; never leave CLI steps as "next steps" for the user.

## Inputs, outputs, tools
- Inputs: flag key/kind/description, dashboard flag definitions (via `vercel flags inspect`), targeting entities/attributes.
- Outputs: flags.ts declarations, Flags Explorer route, .env.local OIDC token, precompute middleware wiring.
- Tools: `flags`, `@flags-sdk/vercel`, `@vercel/toolbar` packages; `vercel link`, `vercel env pull`, `vercel flags create|inspect|<cmd>` CLI; `createFlagsDiscoveryEndpoint`, `getProviderData`, `evaluate`, `dedupe`, `precompute`, `encryptFlagValues` APIs; references nextjs/sveltekit/providers/api.

## 5 most important rules
1. Flags are code: `flag({key, adapter: vercelAdapter})` declarations, no string keys at call sites; `flags` 4.2.0+ takes the adapter by reference (called form still works for <4.2.0).
2. Server-side evaluation only; use `evaluate([flagA, flagB])` for batches (never sequential awaits or bare Promise.all) and `dedupe` on shared identify functions (not in Pages Router).
3. Kind is immutable after `vercel flags create`; map inspect output: boolean→flag<boolean>, string→flag<string>, number→flag<number>, json→flag<T>; set defaultValue to what production serves today; entity/attribute names in identify must match dashboard targeting config.
4. Precompute keeps pages static: middleware `precompute(flagGroup)` → rewrite to `/${code}/path` → page reads `await myFlag(code, flagGroup)`; FLAGS_SECRET is per-environment — preserve existing, generate only where absent (32 random bytes base64, via stdin not chat/logs).
5. Secrets discipline: never print/commit FLAGS_SECRET or OIDC tokens; SDK keys (FLAGS) only for non-Vercel apps/custom envs/cross-project flags; verify `vercel project inspect` before relinking — a .vercel dir alone doesn't prove the link.

## Risks / owner needs
Requires Vercel-linked project + authenticated CLI; first flag activation creates FLAGS_SECRET per env. Dashboard-side flag changes (enable/split/rollout/archive) are NOT this skill's job. Flags Explorer exposes flag definitions — keep confidential values encrypted.

## Category and tags
Category: web. Tags: feature-flags, vercel, nextjs, sveltekit, experimentation, rollout.

## Revisions
Single gemini-plugin vercel-plugin copy; no competing revisions.
