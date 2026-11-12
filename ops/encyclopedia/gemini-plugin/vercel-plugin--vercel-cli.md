# vercel-cli (codex revision)

## Summary
vercel-cli is routing guidance for the `vercel`/`vc` command-line tool: deploy, manage and develop Vercel projects from the shell. Its core discipline is project LINKING — commands must run inside a directory containing `.vercel/`, which is either `project.json` (single project, from `vercel link`) or `repo.json` (multi-project repo, from `vercel link --repo`, required when projects live in subdirs like `apps/web`). It gives a quick start (install, login, link, pull, dev/deploy/--prod), a decision tree mapping intents to 16 reference files (deployment, local-development, environment-variables, ci-automation, domains-and-dns, projects-and-teams, monitoring-and-debugging, storage, integrations, node-backends, monorepos, bun, flags, advanced, global-options, getting-started), and an anti-pattern list.

## When to use / when NOT
Use whenever a task involves deploying to Vercel, managing env vars/domains/projects, streaming logs, or any `vercel`/`vc` command. Do NOT guess flags — `vercel <command> -h` and the reference files are authoritative; don't use it for non-Vercel hosting.

## Inputs, outputs, tools
- Inputs: user intent (deploy/env/domain/logs/etc.) plus the project directory.
- Outputs: routed reference doc to follow, then actual CLI commands run.
- Tools: `vercel`/`vc` CLI (`npm i -g vercel`), `vercel api` as fallback for missing commands, `vercel curl` for protected previews.

## 5 most important rules
1. Check `.vercel/` FIRST when anything breaks: `project.json` vs `repo.json` tells you how it's linked; `vercel whoami`/`teams switch` for wrong-team mistakes.
2. Monorepos with multiple projects need `vercel link --repo` — `vercel link`/auto-link creates project.json which tracks only one project.
3. Never let commands implicitly auto-link in monorepos; link explicitly first.
4. CI needs `--yes` to skip prompts; after `vercel build`, deploy with `--prebuilt` or the build output is ignored.
5. Use `VERCEL_TOKEN` env var, never `--token` flags; never disable deployment protection — use `vercel curl` for previews instead.

## Risks / things needing the owner
`vercel login` and token/team management are owner-auth steps. Wrong linking silently deploys to the wrong project/team — the #1 stated failure mode. Real deployments have production side effects; `--prod` needs care. Otherwise low risk.

## Category / tags
cloud · vercel, cli, deployment, devops

## Revisions
Single source read: `C:\Users\a7med\.codex\skills\vercel-cli\SKILL.md` (67 lines + references/). Exists across six tools with identical structure; codex revision representative.
