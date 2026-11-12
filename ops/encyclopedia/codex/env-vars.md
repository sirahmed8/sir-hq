# env-vars

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\env-vars\SKILL.md`
- SKILL.md size: 8617 chars

## What it does

Vercel environment variable expert guidance. Use when working with .env files, vercel env commands, OIDC tokens, or managing environment-specific configuration.

## When to use (from skill text)

- Use this sequence when setting up a project from scratch:

## Structure (headings inside SKILL.md)

- Vercel Environment Variables
- .env File Hierarchy
- Load Order (Next.js)
- Critical Rules
- vercel env CLI
- Pull Environment Variables
- Pull all env vars for the current environment into .env.local
- Pull for a specific environment
- Overwrite existing file without prompting
- Pull to a custom file
- Add Environment Variables
- Interactive — prompts for value and environments
- Non-interactive
- Add to multiple environments
- Add a sensitive variable (encrypted, not shown in logs)
- List Environment Variables
- List all environment variables
- Filter by environment
- Remove Environment Variables
- Remove from specific environment
- Remove from all environments
- Bootstrap Flow (Fresh Clone / New Machine)
- 1) Link first so pulls target the correct Vercel project
- 2) Pull env vars into .env.local
- 3) Verify required keys from .env.example exist in .env.local
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2. `.env.[environment]` (development, production, or test)
- - **Never commit secrets** to `.env`, `.env.development`, or `.env.production` — use `.local` variants or Vercel environment variables
- - `.env.local` is always gitignored by Next.js — this is where `vercel env pull` writes secrets
- - Variables prefixed with `NEXT_PUBLIC_` are exposed to the browser bundle — never put secrets in `NEXT_PUBLIC_` vars

## Key rules (verbatim lines from SKILL.md)

1. - **Never commit secrets** to `.env`, `.env.development`, or `.env.production` — use `.local` variants or Vercel environment variables
2. - `.env.local` is always gitignored by Next.js — this is where `vercel env pull` writes secrets
3. - Variables prefixed with `NEXT_PUBLIC_` are exposed to the browser bundle — never put secrets in `NEXT_PUBLIC_` vars
4. 3. **Token expiry**: When the local OIDC token expires, re-run `vercel env pull .env.local --yes` to get a fresh one. Consider re-pulling at the start of each dev session to avoid mid-session auth failures
5. 2. **Never hardcode secrets** — always use environment variables

## Files inside the skill

- (SKILL.md only)
