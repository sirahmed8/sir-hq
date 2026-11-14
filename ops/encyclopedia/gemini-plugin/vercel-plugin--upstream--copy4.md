# upstream

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-cli\upstream\SKILL.md`
- SKILL.md size: 8255 chars

## What it does

Deploy, manage, inspect, and troubleshoot Vercel projects from the command line. Use for Vercel deployments, Vercel Toolbar comments, build failures, projects and teams, environment variables, domains and DNS, logs, metrics, Speed Insights, Core Web Vitals, request traces, usage, activity, alerts, firewall rules, cache, cron jobs, deploy hooks, Edge Config, feature flags (`vercel flags`), integrations, connectors, Blob storage, Container Registry (VCR), microfrontends, rolling releases, custom environments, Sandbox, agent/MCP setup, preview access, local development, or `vercel api` fallback.

## When to use (from skill text)

- Use this to route to the correct reference file:

## Structure (headings inside SKILL.md)

- Vercel CLI Skill
- Critical: Project Linking
- Quick Start
- OR
- Decision Tree
- Anti-Patterns

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Build failures, deployment errors, logs, metrics, Speed Insights, Core Web Vitals, activity, performance, preview access, or production debugging** → `references/monitoring-and-debugging.md`
- - **Alerts, usage, contracts, billing purchases, tokens, telemetry, or CLI upgrades** → `references/platform-ops.md`
- - **Hardcoding tokens in flags**: Use `VERCEL_TOKEN` env var instead of `--token`.

## Key rules (verbatim lines from SKILL.md)

1. - **CLI command is unavailable or output is missing required fields** → use `vercel api` after first-class CLI paths are unavailable or insufficient (see `references/advanced.md`)
2. - **Forgetting non-interactive flags in plain CI runs**: detected agents get `--non-interactive` by default, but plain CI does not — pass it explicitly there, and add `--yes` only for commands that require confirmation.
3. - **Using `vercel deploy` after `vercel build` without `--prebuilt`**: The build output is ignored.
4. - **Hardcoding tokens in flags**: Use `VERCEL_TOKEN` env var instead of `--token`.

## Files inside the skill

- `command/vercel.md` — "d"
- `references/advanced.md` — "Advanced Commands"
- `references/agent-and-ai.md` — "Agent, MCP, Skills, and AI Gateway"
- `references/bun.md` — "Bun on Vercel"
- `references/ci-automation.md` — "CI/CD Automation"
- `references/comments.md` — "Vercel Toolbar Comments"
- `references/connectors.md` — "Connectors"
- `references/container-registry.md` — "Container Registry (VCR)"
- `references/deployment.md` — "Deployment"
- `references/domains-and-dns.md` — "Domains & DNS"
- `references/environment-variables.md` — "Environment Variables"
- `references/firewall.md` — "Firewall"
- `references/flags.md` — "Feature Flags"
- `references/getting-started.md` — "Getting Started"
- `references/global-options.md` — "Global Options"
- `references/integrations.md` — "Integrations"
- `references/local-development.md` — "Local Development"
- `references/microfrontends.md` — "Microfrontends"
- `references/monitoring-and-debugging.md` — "Monitoring & Debugging"
- `references/monorepos.md` — "Monorepos on Vercel"
- `references/node-backends.md` — "Node Backends on Vercel"
- `references/platform-ops.md` — "Platform Operations"
- `references/project-infra.md` — "Project Infrastructure"
- `references/projects-and-teams.md` — "Projects & Teams"
- `references/routing.md` — "Routing Rules"
- `references/sandbox.md` — "Sandbox"
- `references/security.md` — "Security"
- `references/storage.md` — "Blob Storage"
