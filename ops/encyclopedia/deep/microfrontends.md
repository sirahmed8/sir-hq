# microfrontends (vercel-plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\microfrontends\SKILL.md` (3.6 KB; gemini-plugin; `references/` has configuration, path-routing, local-development, managing, troubleshooting, security).

## Summary
Vercel Microfrontends orchestration: split an app into independently deployable units rendered as one app, routed on Vercel's global network via `microfrontends.json`. Concepts: default app (owns the file, serves unmatched requests), child apps (`routing` path patterns), asset prefix (prevents static-asset collisions), independent deployments. Framework support via `@vercel/microfrontends` for Next.js (App+Pages Router), SvelteKit, React Router, Vite. Documents the `vercel microfrontends`/`vercel mf` CLI: `create-group` (interactive or `--non-interactive` with `--project`, `--default-app`, `--default-route`, `--project-default-route`; blocked past free-tier limits), `add-to-group` (always confirms, no `--yes`), `remove-from-group` (`--yes` skips prompts), `delete-group` (irreversible), `inspect-group` (`--format=json` for automation), `pull`, `proxy`, `port`.

## When to use / when NOT
Use for splitting a large app into independently deployed microfrontends on Vercel. Not for monorepo-only code sharing without deployment split, and not worth it for small apps — routing complexity is real.

## Inputs, outputs, tools
- Inputs: project list, group name, default app/route assignments, path routing rules.
- Outputs: `microfrontends.json`, group config, local dev proxy, per-project asset prefixes.
- Tools: `vercel mf` CLI, `@vercel/microfrontends`, `microfrontends.json`, references for path expressions/middleware/security.

## 5 most important rules
1. Search `references/` per-topic (configuration, path-routing, local-development, managing, troubleshooting, security) — do not load all upfront.
2. `microfrontends.json` lives in the default app; children declare `routing` path patterns; unmatched requests fall to default.
3. Asset prefixes are mandatory per child to prevent collisions.
4. CLI group ops have asymmetric interactivity: `add-to-group` always confirms; `create-group --non-interactive` needs `--project-default-route` per non-default project and is blocked past free limits.
5. `delete-group` is irreversible — confirm intent; `inspect-group --format=json` is the automation-safe read.

## Risks / owner notes
Group creation can hit billing/free-tier limits requiring interactive confirmation — a CI/agent run may stall there. Deployment protection/WAF interplay is covered in `references/security.md`; check before exposing children publicly.

## Category and tags
Category: cloud. Tags: vercel, microfrontends, multi-tenant, routing, cli, deployment.
