# netlify-deploy (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-deploy\SKILL.md`. Create/configure/manage deploys from code.

## Summary
Deploy paths: Git CD (default — push triggers build), CLI (`netlify deploy`=manual draft no-build, `--prod`=production, `netlify create`, `--allow-anonymous` temp project claimable in 1hr, skew protection needs CLI ≥23.11.0), drag-and-drop, API (digest/ZIP one-offs), Deploy-to-Netlify button, build hooks (trusted — bypass deploy request policy), AI Agent Runners (auto Deploy Preview at `agent-<runID>--<site>.netlify.app`), Zapier/n8n. Deploys are versioned ATOMIC snapshots — only changed files upload, live site switches after all land. Manual deploys don't run build commands (drag-drop logged-in auto-detects framework is the exception). `netlify.toml` deploy contexts: `[context.production|deploy-preview|branch-deploy|preview-server|dev]` + custom branch contexts; plugins need `[[...plugins]]`; **env vars in netlify.toml are NOT available to the deploy environment** — set via UI/CLI/API; toml is committed so keep secrets out. Deploy Previews auto-build for PRs/MRs (base branch must be production or branch-deploy-enabled; URL `deploy-preview-<num>--<site>`; pending = Not Found). Branch deploys need enabling in UI (specific branches or All; `features/*` wildcard; URL `<branch>--<site>`; persist while branch exists; `[context.branch-deploy]`/`[context.<branch>]`). Branch deploy + open PR = both artifacts. Entry path via `@netlify /path` in PR description (can't change in Drawer after). Skip deploys: `[skip ci]`/`[skip netlify]` in PR title (preview) or commit message (branch/prod) — next unmarked commit deploys everything skipped. CRITICAL: add `.netlify` to `.gitignore` — linking writes `.netlify/state.json` which must not be committed.

## When to use / when NOT
Use for Git CD setup, `netlify deploy`/`--prod`, deploy contexts, Deploy Previews/branch deploys, deploy buttons, build hooks, failed/secrets-scanning deploy fixes, keeping staging out of Google, monorepo deploy config. NOT for routing rules (→ netlify-config) or caching (→ netlify-caching).

## Inputs, outputs, tools
- Inputs: repo, production branch, deploy-context needs, skip-deploy intent.
- Outputs: deploys (draft/prod/preview/branch), contexts in netlify.toml, `.gitignore` entry.
- Tools: `netlify` CLI, netlify.toml contexts, Git integration, build hooks, Agent Runners, Deploy Navigator.

## 5 most important rules
1. `.netlify` MUST be gitignored — `state.json` is local linkage state.
2. Manual `netlify deploy` skips builds; only Git CD and logged-in drag-drop build.
3. toml env vars ≠ deploy-env vars — secrets go through UI/CLI/API, never committed toml.
4. Deploys are atomic snapshots — a failed deploy never leaves a half-live site.
5. `[skip ci]`/`[skip netlify]` placement matters (PR title vs commit message) and skipped changes batch into the next real deploy.

## Risks / owner notes
Build hooks bypass deploy-request policies (trusted). Skipped deploys accumulate — the next deploy ships them all. Anonymous deploys expire in 1 hour. Branch deploys persist and may expose staging publicly unless protected.

## Category and tags
Category: cloud. Tags: netlify, deploy, continuous-deployment, deploy-previews, branch-deploys, build-hooks, atomic-deploys.
