# base44-cli

Source read: `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44-cli\SKILL.md` (gemini-plugin base44 0.1.7, 758 lines) plus its 50-file references/ directory.

## Summary
The operating manual for the Base44 CLI (`npx base44`), the command-line tool for everything Base44-platform: creating and linking projects, scaffolding local files for externally provisioned apps, local dev (`base44 dev`, with a `--remote` mode that hits production data), deploying all resources, pushing entities/functions/actors/agents/agent-skills/connectors/auth config, managing secrets, generating TypeScript types, running scripts via `base44 exec`, site deploy, and a generic `base44 api` escape hatch that searches/calls the platform's OpenAPI spec for anything without a dedicated command. It enforces a strict state check: existing project (`base44/config.jsonc` present) -> hand off to base44-sdk; provisioned app (`BASE44_APP_ID` env or Stripe Projects flow) -> `scaffold`, never `create`; otherwise -> `create`.

## When to use / when NOT
Use for all CLI-level Base44 work: project creation/linking/eject, auth (login/logout/whoami), deploys, entity/function/actor/agent/connector/auth-config push-pull, secrets, types generation, exec, site hosting, and arbitrary API calls. Do NOT use it to write application code in an existing project (that is base44-sdk), and do NOT run bare `base44` — always via the local dev dependency (`npx`/`yarn`/`pnpm`).

## Inputs, outputs, tools
- Inputs: user intent, presence of `base44/config.jsonc`, `base44/.app.jsonc`, env vars (`BASE44_APP_ID`, `BASE44_ACCESS_TOKEN`, `BASE44_REFRESH_TOKEN`, `BASE44_API_KEY`), CLI args.
- Outputs: local project scaffold/edits, deployed Base44 resources, JSON output with `--json`, TypeScript `types.d.ts`.
- Tools: `base44` npm package as devDependency (never a global install), `npx base44 whoami|login|create|scaffold|link|eject|dev|deploy|entities push|functions deploy|actors deploy|agents push|agent-skills push|connectors *|auth *|secrets *|types generate|exec|site deploy|api search|catalog|grep|fetch|workflows list|runs|logs|dashboard open|visibility|workspace *`. MCP: none. 50 reference files cover each command.

## 5 most important rules
1. **Mandatory auth check first**: run `npx base44 whoami` at session start; if not logged in, STOP and have the user run `npx base44 login` — never proceed unauthenticated. (Skipped automatically when `BASE44_API_KEY`/`BASE44_ACCESS_TOKEN` env auth is present.)
2. **NEVER call `base44` directly** — always `npx base44` (or yarn/pnpm); the CLI is a local dev dependency.
3. **State check before acting**: config.jsonc exists -> base44-sdk territory; provisioned app -> `scaffold` (running `create` makes a duplicate app); neither -> `create` (read create.md first — it is marked MUST READ).
4. **`base44 dev` hits a throwaway local backend; `base44 dev --remote` hits PRODUCTION data** — default to local, warn loudly before `--remote`.
5. **Build through the CLI**: `npx base44 build` injects `VITE_BASE44_APP_ID`; a bare `npm run build` produces a site whose API calls fail. Prefer dedicated commands over `base44 api`, but use `api` when a dedicated command does more than asked.

## Risks / owner notes
`--remote` dev and `deploy` touch live production data and incur real platform usage — confirm with the owner before running against a production app. `secrets set` handles credentials; values must never be echoed into files or logs. `eject`/`scaffold` write code locally — verify app identity (`.app.jsonc`) to avoid wiring the wrong app.

## Category / tags
build · base44, cli, deployment, baaS, scaffolding, devops, typescript

## Revisions
Single revision (gemini-plugin base44 0.1.7). Not present in other tool stores — canonical and only source.
