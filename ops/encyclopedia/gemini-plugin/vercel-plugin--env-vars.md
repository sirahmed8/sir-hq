# env-vars

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\env-vars\SKILL.md`
- SKILL.md size: 11221 chars

## What it does

Vercel environment variable expert guidance.

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
- Interactive — prompts for value, environments, and type
- Non-interactive: read the value from a file so it never lands in shell
- history or process arguments (echo "value" | ... and --value do both)
- Add to production and preview in one command
- Set the type explicitly
- Add development in its own command; development-only adds default to Config
- Update an existing value
- List Environment Variables
- List all environment variables
- Filter by environment
- Remove Environment Variables
- Remove from specific environment
- Remove from all environments
- Bootstrap Flow (Fresh Clone / New Machine)
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
4. - **Public prefixes are always Config**: variables such as `NEXT_PUBLIC_*` or `VITE_*` are exposed to browsers, so the CLI refuses `--type secret` for them. Keep a private value under a name without the prefix.
5. - **Team policy**: **Separate Production Secret Values** requires a Production Secret to differ from the Preview, Development, and custom environment values of the same key. Under it, create separate Production and non-Production values instead of adding one value to all targets. It replaces the dep

## Files inside the skill

- (SKILL.md only)
