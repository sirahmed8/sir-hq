# vercel-cli

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\vercel-cli\SKILL.md`
- SKILL.md size: 3658 chars

## What it does

Vercel CLI guidance: deployments, env vars, project linking, log streaming, and domain management.

## When to use (from skill text)

- Use this to route to the correct reference file:

## Structure (headings inside SKILL.md)

- Vercel CLI Skill
- Critical: Project Linking
- Quick Start
- OR
- Decision Tree
- Anti-Patterns
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Hardcoding tokens in flags**: Use `VERCEL_TOKEN` env var instead of `--token`.

## Key rules (verbatim lines from SKILL.md)

1. - **`.vercel/repo.json`**: Created by `vercel link --repo`. Links a repo that may contain multiple projects. Always a good idea when any project has a non-root directory (e.g., `apps/web`).
2. - **Forgetting `--yes` in CI**: Required to skip interactive prompts.
3. - **Using `vercel deploy` after `vercel build` without `--prebuilt`**: The build output is ignored.
4. - **Hardcoding tokens in flags**: Use `VERCEL_TOKEN` env var instead of `--token`.

## Files inside the skill

- `command/vercel.md` — "d"
- `overlay.yaml`
- `references/advanced.md` — "Advanced Commands"
- `references/bun.md` — "Bun on Vercel"
- `references/ci-automation.md` — "CI/CD Automation"
- `references/deployment.md` — "Deployment"
- `references/domains-and-dns.md` — "Domains & DNS"
- `references/environment-variables.md` — "Environment Variables"
- `references/flags.md` — "Feature Flags"
- `references/getting-started.md` — "Getting Started"
- `references/global-options.md` — "Global Options"
- `references/integrations.md` — "Integrations"
- `references/local-development.md` — "Local Development"
- `references/monitoring-and-debugging.md` — "Monitoring & Debugging"
- `references/monorepos.md` — "Monorepos on Vercel"
- `references/node-backends.md` — "Node Backends on Vercel"
- `references/projects-and-teams.md` — "Projects & Teams"
- `references/storage.md` — "Blob Storage"
