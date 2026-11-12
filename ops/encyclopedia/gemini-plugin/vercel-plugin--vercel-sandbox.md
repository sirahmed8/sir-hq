# vercel-sandbox

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-sandbox\SKILL.md`
- SKILL.md size: 21680 chars

## What it does

Run untrusted code safely in ephemeral.

## When to use (from skill text)

- | `env` | – | Environment variables for every command. Per-command `env` overrides these. Use this to inject a credential into the VM. |

## Structure (headings inside SKILL.md)

- Vercel Sandbox
- Install
- Minimal example
- Authentication
- Creating a sandbox
- Running commands
- Files
- Installing system packages
- Ports and preview URLs
- Lifecycle and persistence
- Snapshots
- Images
- Drives
- Network policy and credential brokering
- Running AI agents in a sandbox
- Multi-agent isolation
- CLI
- Limits and cost
- Best-practice checklist
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **On Vercel** (Functions, Cron, builds): the SDK authenticates automatically via the deployment's OIDC token. No config.
- - **External / CI** (no OIDC available): set `VERCEL_TOKEN`, `VERCEL_TEAM_ID`, `VERCEL_PROJECT_ID` and pass them as `token`, `teamId`, `projectId` to `Sandbox.create()` (the SDK does not read them from the environment).
- - **Isolation**: each sandbox is a separate Firecracker microVM, so a crash, fork bomb, or disk-fill is contained to that VM. There are no per-process CPU/PID quotas inside the VM beyond the vCPU and 64 GB disk limits — cap risk with a short `timeout` and `deny-all` for untrusted code.

## Key rules (verbatim lines from SKILL.md)

1. - A detached server returns as soon as the process spawns, **not** when it's listening — so after starting it (in `onCreate` for the first boot and `onResume` for later ones) poll until the port answers before treating `domain(port)` as live (see [Ports](#ports-and-preview-urls)).
2. - For one-off work, `stop()` in a `finally` (safe to call more than once). **Exception**: a long-lived sandbox serving an exposed port — don't stop it, or the URL goes dead; leave it running (it persists/resumes).
3. - `apt-get update` before `apt-get install`; commands are non-root by default (`sudo: true` for root); `sudo`/`detached` are object-form only.
4. - Exposed servers must bind `0.0.0.0`, not `127.0.0.1`.
5. - Pin a custom image by digest for reproducible boots; `ENTRYPOINT`/`CMD` don't run.

## Files inside the skill

- `overlay.yaml`
