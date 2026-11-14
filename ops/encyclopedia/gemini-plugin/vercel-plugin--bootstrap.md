# bootstrap

**Source:** `C:\Users\a7med\.claude\skills-disabled\bootstrap\SKILL.md` (claude copy, currently disabled; codex and other tools hold the same content)
**Category:** automation
**Tags:** vercel, bootstrap, neon, postgres, nextjs, shadcn, next-forge, environment-variables

## Summary
A Vercel project bootstrap orchestrator that links a repository to a Vercel project, provisions environment variables and shared resources (Neon Postgres), verifies env keys, runs database migrations and seeding, starts the dev server, and optionally establishes a shadcn/Next.js UI baseline. It enforces strict ordering: no migrations and no dev server until linking and environment verification are complete. It also has a dedicated path for next-forge monorepos.

## When to use / when not to
Use it when linking a repository to Vercel and provisioning its environment and resources during bootstrap, especially for Next.js plus shadcn or next-forge projects. Do not use it for ongoing development after bootstrap or for non-Vercel hosting.

## Inputs, outputs, tools
Inputs: a Vercel CLI login, the repository, an env template (`.env.example`, `.env.sample` or `.env.template`), and the chosen team and project. Outputs: a linked project, provisioned Neon Postgres, `.env.local`, a verified env-key diff, migration and seed results, and a bootstrap summary. Tools: Vercel CLI (`vercel link`, `vercel integration`, `vercel env`), Node and a package manager, and the shadcn CLI. No MCP.

## Five most important rules
1. Never run `db:push`, `db:migrate`, `db:seed` or `dev` before Vercel linking and env verification are complete.
2. Prefer Vercel-managed provisioning (`vercel integration add neon`) over provider CLIs, and use the provider CLI only as a fallback.
3. Generate `AUTH_SECRET` without printing it, store it in Vercel, and unset the shell variable.
4. Compare required env keys against `.env.local` by name only, and proceed only when the missing list is empty.
5. For next-forge, use per-app env files, run `pnpm migrate`, deploy three separate Vercel projects, and remove optional service imports to avoid validation errors.

## Risks and owner actions
Bootstrap creates real Vercel projects and provisions Neon resources, so it needs the owner's Vercel account; never echo secret values. The `.app.jsonc` file with the app ID should stay git-ignored.

## Revisions
The claude copy (5863 bytes, 2026-10-28) currently sits in `skills-disabled/`; the codex copy (5826 bytes, 2026-10-11) differs only in the description line. Content is otherwise identical, so the codex copy is the live equivalent in the other tools.
