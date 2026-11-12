# bootstrap

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\bootstrap\SKILL.md`
- SKILL.md size: 6157 chars

## What it does

Bootstrap and repair repositories with.

## Structure (headings inside SKILL.md)

- Project Bootstrap Orchestrator
- Rules
- Preflight
- Resource Setup: Postgres
- Preferred path (Vercel-managed Neon)
- Fallback path 1 (Dashboard)
- Fallback path 2 (Neon CLI)
- AUTH_SECRET Generation
- Env Verification
- App Setup
- UI Baseline for Next.js + shadcn Projects
- Bootstrap Verification
- Summary Format
- Bootstrap Result
- Bootstrap Next Steps
- next-forge Projects
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Never echo secret values in terminal output, logs, or summaries.
- 1. Add a baseline primitive set: `npx shadcn@latest add button card input label textarea select switch tabs dialog alert-dialog sheet dropdown-menu badge separator skeleton table`
- 4. Default to dark mode for product, admin, and AI apps unless the repo is clearly marketing-first.
- - **Secrets**: AUTH_SECRET set in Vercel (value never shown)

## Key rules (verbatim lines from SKILL.md)

1. - Do not run `db:push`, `db:migrate`, `db:seed`, or `dev` until Vercel linking is complete and env keys are verified.
2. - Never echo secret values in terminal output, logs, or summaries.
3. 3. If not linked, inspect available teams/projects before asking the user to choose:
4. - Required env key diff is empty.
5. - **Env Keys**: <count> required, <count> present, <count> missing

## Files inside the skill

- (SKILL.md only)
