# base44-cli

- Tool: `gemini-plugin` (plugin: `base44`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44-cli\SKILL.md`
- SKILL.md size: 42770 chars

## What it does

The base44 CLI is used for EVERYTHING.

## When to use (from skill text)

- ## When to Use This Skill vs base44-sdk
- Workflows are the automation system (cron schedules, entity triggers, connector events, in-app agent actions). These commands are read-only: they answer "what workflows exist" and "did my scheduled work fail, and why".
- Use this skill when the user asks to export, download, or share a report as a PDF.

## Structure (headings inside SKILL.md)

- Base44 CLI
- ⚡ IMMEDIATE ACTION REQUIRED - Read This First
- Critical: Local Installation Only
- MANDATORY: Authentication Check at Session Start
- Overview
- When to Use This Skill vs base44-sdk
- Project Structure
- Installation
- Global `--app-id` Option
- Run a one-off script against a specific app
- Fetch logs for a deployed app without a local checkout
- Global `--json` Option
- Available Commands
- Authentication
- Project Management
- Workspace Management
- Development
- Deployment
- Entity Management
- Function Management
- Workflow Runs
- Actor Management
- Agent Management
- Agent Skills Management
- Connector Management
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Entity tools**: `entity_name` + `allowed_operations` (array of: `read`, `create`, `update`, `delete`)
- - **Server route tools** (full-stack apps): `tool_name` (1-64 chars of letters, digits, `_`, `-`) + `route_path` (app-relative, starts with a single `/`, no query string) + `method` (`get`\|`post`\|`put`\|`patch`\|`delete`, default `post`) + `description` (default `"agent server route"`)
- - `npx base44 functions delete <name>` - Delete a deployed function
- - `npx base44 actors delete <name>` - Tear down a deployed actor

## Key rules (verbatim lines from SKILL.md)

1. - **DO NOT run `npx base44 create`** — that creates a second, duplicate app. See [scaffold.md](references/scaffold.md).
2. - Do NOT activate base44-sdk yet
3. - **DO NOT proceed** with any CLI operations
4. - Wait for the user to confirm they have logged in before continuing
5. - `base44 deploy` still requires a local project directory because it reads local resources

## Files inside the skill

- `references/actors-create.md` — "Creating Actors"
- `references/actors-deploy.md` — "base44 actors deploy"
- `references/agent-skills-pull.md` — "base44 agent-skills pull"
- `references/agent-skills-push.md` — "base44 agent-skills push"
- `references/agents-pull.md` — "base44 agents pull"
- `references/agents-push.md` — "base44 agents push"
- `references/api-catalog.md` — "base44 api catalog"
- `references/api-fetch.md` — "base44 api fetch"
- `references/api-grep.md` — "base44 api grep"
- `references/api-search.md` — "base44 api search"
- `references/auth-login.md` — "base44 login"
- `references/auth-logout.md` — "base44 logout"
- `references/auth-password-login.md` — "base44 auth password-login"
- `references/auth-pull.md` — "base44 auth pull"
- `references/auth-push.md` — "base44 auth push"
- `references/auth-social-login.md` — "base44 auth social-login"
- `references/auth-sso.md` — "base44 auth sso"
- `references/auth-whoami.md` — "base44 whoami"
- `references/connectors-create.md` — "Creating Connectors"
- `references/connectors-initiate.md` — "base44 connectors initiate"
- `references/connectors-list-available.md` — "base44 connectors list-available"
- `references/connectors-pull.md` — "base44 connectors pull"
- `references/connectors-push.md` — "base44 connectors push"
- `references/create.md` — "base44 create"
- `references/dashboard.md` — "base44 dashboard open"
- `references/deploy.md` — "base44 deploy"
- `references/dev.md` — "base44 dev"
- `references/eject.md` — "base44 eject"
- `references/entities-create.md` — "Creating Entities"
- `references/entities-push.md` — "base44 entities push"
- `references/exec.md` — "base44 exec"
- `references/functions-create.md` — "Creating Functions"
- `references/functions-delete.md` — "base44 functions delete"
- `references/functions-deploy.md` — "base44 functions deploy"
- `references/functions-list.md` — "base44 functions list"
- `references/functions-pull.md` — "base44 functions pull"
- `references/link.md` — "base44 link"
- `references/rls-examples.md` — "RLS Examples"
- `references/scaffold.md` — "base44 scaffold"
- `references/secrets-delete.md` — "base44 secrets delete"
- `references/secrets-list.md` — "base44 secrets list"
- `references/secrets-set.md` — "base44 secrets set"
- `references/site-deploy.md` — "base44 site deploy"
- `references/site-open.md` — "base44 site open"
- `references/types-generate.md` — "`base44 types generate`"
- `references/visibility.md` — "base44 visibility"
- `references/workflows-list.md` — "base44 workflows list"
- `references/workflows-runs.md` — "base44 workflows runs"
- `references/workspace-get.md` — "base44 workspace get"
- `references/workspace-list.md` — "base44 workspace list"
- `references/workspace-move.md` — "base44 workspace move"
