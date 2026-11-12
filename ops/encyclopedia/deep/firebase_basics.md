# firebase-basics

## Summary
The entry-point skill for all Firebase work: verify the environment (Node 16+, `npx -y firebase-tools@latest`), ensure login (`login`, `--no-localhost` for headless), establish the active project (must pause and ask: existing project ID vs create new — project IDs are 6-30 chars, lowercase, globally unique), and set up the full Firebase skill suite per agent environment via references/setup/*.md. It also encodes usage principles: always npx-prefixed CLI, `developerknowledge_search_documents` MCP before general search, Firebase MCP server tools over raw API calls, and CLI-based app config download (`apps:sdkconfig`) instead of console downloads.

## When to use / when NOT
Use as the prerequisite for ANY Firebase task (auth, firestore, hosting, functions, crashlytics). Do NOT skip its environment-setup reference even when firebase-basics is the only Firebase skill loaded — it routes to per-agent setup docs. Not for implementing a specific service feature (those have their own skills).

## Inputs, outputs, tools
- Inputs: user's choice of existing vs new Firebase project, agent environment (Gemini CLI, Antigravity, Android Studio, Claude Code, Cursor, Copilot, other).
- Outputs: logged-in CLI, active project (`firebase use <id>`), downloaded `google-services.json`/`GoogleService-Info.plist` via `apps:sdkconfig ANDROID|IOS <APP_ID>`.
- Tools: `npx -y firebase-tools@latest` (NEVER naked `firebase`), `projects:create`, `projects:list`, `apps:list`, `use`, `apps:sdkconfig`, `init`, Firebase MCP server, developerknowledge MCP.

## 5 most important rules
1. ALWAYS use `npx -y firebase-tools@latest` — never the bare `firebase` command.
2. MUST pause and ask whether to use an existing project ID or create a new one before configuring anything; confirm the active project with the user.
3. If firebase-basics is the only Firebase skill available, you MUST read references/local-env-setup.md and the per-agent setup doc to install the full skill suite — do not skip.
4. Prefer Firebase MCP server tools and `developerknowledge_search_documents` (include "Firebase" in queries) over manual API calls and general web search.
5. Download app config files via CLI (`apps:sdkconfig`) — never send users to the console for google-services files.

## Risks / owner needs
Login requires interactive auth (owner action if needed). Project creation is a real GCP action — project IDs are globally unique and permanent-ish. SIR rule: every product gets its OWN Firebase project named after the product.

## Category and tags
Category: cloud. Tags: firebase, cli, setup, prerequisites, gcp, mcp.

## Revisions
Identical across claude/codex/cursor/gemini-plugin/kilo/opencode/windsurf; claude copy used.
