# env-vars (Vercel)

## Summary
Vercel environment-variable management guide: the `.env` file hierarchy and Next.js load order (.env → .env.[environment] → .env.local → .env.[environment].local, later wins; `.local` files gitignored and skipped in test), critical rules (never commit secrets to tracked env files, `NEXT_PUBLIC_` exposes to browser bundle, everything else server-only), the `vercel env` CLI (pull/add/rm/ls with --environment/--sensitive/--yes), a fresh-clone bootstrap flow (link → pull → diff against .env.example), and `vercel env run` for one-off runs without writing files.

## When to use / when NOT
Use when working with .env files, `vercel env` commands, OIDC tokens, or environment-specific config on Vercel/Next.js. Do NOT use for non-Vercel platforms or for deciding WHICH secrets an app needs (that's app design).

## Inputs, outputs, tools
- Inputs: env var names/values, target environment (development/preview/production), project link.
- Outputs: `.env.local` files, Vercel-side env vars, verified key presence.
- Tools: `vercel env pull|add|rm|ls|run`, `vercel link`, `.env.example` diff loop.

## 5 most important rules
1. Secrets live in `.local` variants or Vercel env vars — NEVER in git-tracked `.env`/`.env.production`.
2. `NEXT_PUBLIC_` prefix = shipped to the browser bundle — secrets must never carry it.
3. `vercel env pull` writes to `.env.local` (gitignored); use `--environment=` to target preview/prod; `--yes` avoids prompts in scripts.
4. Bootstrap order: `vercel link` first (so pulls hit the right project), then pull, then verify every `.env.example` key exists.
5. `vercel env add --sensitive` for values that must not appear in logs; `vercel env run -- <cmd>` injects envs without persisting a file.

## Risks / things needing the owner
Env vars often contain production secrets — pulling them onto a machine is a security event; confirm the machine/context is appropriate. Deleting env vars (`env rm`) can break deployments.

## Category / tags
cloud · vercel, env-vars, secrets, configuration, security

## Revisions
Five tools hold it (codex, cursor, gemini-plugin, kilo, opencode, windsurf — no claude); codex copy chosen, all ~8617 bytes identical.
