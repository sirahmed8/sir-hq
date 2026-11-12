# next-forge

Tools: codex, cursor, kilo, opencode, windsurf (codex copy used; identical across tools).
Source: C:\Users\a7med\.codex\skills\next-forge\SKILL.md (+ references/: architecture.md, customization.md, packages.md, setup.md)

## Summary
Operating guide for the next-forge Turborepo SaaS template: a monorepo with seven apps (`app` SaaS, `web` marketing, `api` webhooks/cron, `email` preview, `docs`, `storybook`, `studio`) and ~20 shared `@repo/*` packages covering auth, database (Prisma/Postgres), payments, email, CMS, design system, analytics, observability, security, storage, SEO, i18n, webhooks, cron, notifications, collaboration, AI, rate-limit, and config. All integrations except the database are optional and degrade gracefully when env vars are missing.

## When to use / not use
Use when scaffolding or working inside a next-forge project, or when evaluating it as a SaaS starter. Do not use it as generic Next.js advice — it is template-specific; for general App Router patterns use the `nextjs` skill instead.

## Inputs, outputs, dependencies
Input: a shell with Node + a package manager (bun recommended). Output: a running multi-app dev environment. Needs: `DATABASE_URL` (PostgreSQL, Neon recommended) as the only hard requirement; optional Clerk, Stripe, Resend, BaseHub, Languine keys per package `keys.ts` (Zod-validated via `@t3-oss/env-nextjs`). Deploys as separate Vercel projects per app root.

## Key rules
1. `page.tsx`/`layout.tsx` are always Server Components; client interactivity goes in separate `'use client'` files.
2. Only `packages/database/.env` `DATABASE_URL` is required; missing optional keys silently disable features via optional chaining.
3. After editing `packages/database/prisma/schema.prisma` run `bun run migrate` (format → generate → db push).
4. Add components with `npx shadcn add <component> -c packages/design-system`; bump the whole set with `bun run bump-ui`.
5. Env files live per-app/per-package; `NEXT_PUBLIC_*_URL` variables point apps at each other (3000–3004 locally).

## Risks / owner items
- Seven apps means seven Vercel projects and seven env sets to configure — a real ops cost before first deploy.
- `bun run migrate` does `db push`, not versioned migrations; production schema changes need care.
- References folder has setup/packages/customization/architecture docs — read `references/customization.md` before swapping auth or payments providers.

## Category and tags
build, web, business — saas, turborepo, monorepo, nextjs, starter-template, prisma.

## Revision note
Identical content across all five tools; codex copy read, references directory confirmed.
