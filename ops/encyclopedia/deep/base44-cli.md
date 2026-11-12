# base44-cli

**Source:** `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44-cli\SKILL.md` (+ `references/`)
**Category:** build
**Tags:** base44, cli, deployment, backend, entities, actors, agents, scaffolding

## Summary
The Base44 CLI skill for creating and managing Base44 apps from the command line. It covers authentication, project creation (`create`), scaffolding an existing app (`scaffold`), linking and ejecting, workspaces, local development (`dev`), full deployment (`deploy`), entity/function/actor/agent/agent-skill/connector management, auth configuration, secrets, one-off script execution (`exec`), TypeScript type generation, site deployment, and a public API fallback (`api search/catalog/grep/fetch`). It is the prerequisite skill for `base44-sdk` in new projects.

## When to use / when not to
Use it to create a new Base44 project, initialize local files for an existing app, deploy or push resources, run local development, or perform any CLI operation. Do not use it to write feature code in an existing project (use `base44-sdk`), and do not run the app with plain `npm run dev`, which hits production data.

## Inputs, outputs, tools
Inputs: a Base44 account (`npx base44 whoami`), an app ID or linked project, and local project files. Outputs: created or scaffolded projects, deployed resources, generated types, logs, and machine-readable JSON. Tools: `npx base44` (local install only; never bare `base44`), Node and a package manager. No MCP.

## Five most important rules
1. Check `npx base44 whoami` first; if not logged in, stop and ask the user to run `npx base44 login` before any other command.
2. Check for `base44/config.jsonc`: if it exists, use `base44-sdk`; if not and the app was provisioned externally, use `scaffold`, never `create`, which would create a duplicate app.
3. `create` always needs both `name` and `--path` for non-interactive mode; choose `backend-and-client` for new apps and `backend-only` for an existing framework.
4. Build with `npx base44 build`, not bare `npm run build`, so `VITE_BASE44_APP_ID` is injected; deploy with `npx base44 deploy -y`.
5. Prefer a dedicated command only when it does exactly what was asked; otherwise read the endpoint contract and use `base44 api fetch`.

## Risks and owner actions
`create`, `scaffold` and the push commands are destructive or create real apps, and connector OAuth needs the owner. `base44 dev --remote` reads and writes production data. No secrets belong in git or in the app config.

## Revisions
The installed config copy (43092 bytes, 2026-11-02) and the marketplace cache 1.0.0-beta.1 (42932 bytes, 2026-10-30) have identical bodies; only the description frontmatter differs. The config copy is the live one.
