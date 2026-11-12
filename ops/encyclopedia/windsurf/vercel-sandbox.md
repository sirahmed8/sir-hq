# vercel-sandbox (codex revision)

## Summary
vercel-sandbox documents running agent-browser + headless Chromium inside ephemeral Vercel Sandbox Firecracker microVMs — for browser automation (screenshots, accessibility snapshots, multi-step form fills) from any Vercel-deployed framework. Core pattern: `Sandbox.create()` (snapshot source for fast start, else `runtime:"node24"` + 120s timeout), install Chromium system deps via dnf + `agent-browser` + `npx agent-browser install` when no snapshot, run `agent-browser` commands via `sandbox.runCommand`, always `sandbox.stop()` in finally. Sandbox SNAPSHOTS (saved VM images with deps pre-installed) cut startup from ~30s to sub-second — set `AGENT_BROWSER_SNAPSHOT_ID`; distinct from agent-browser's accessibility `snapshot` command. Auth: OIDC automatic on Vercel; locally `VERCEL_TOKEN`+`VERCEL_TEAM_ID`+`VERCEL_PROJECT_ID`. Combines with Cron Jobs for recurring browser tasks; framework-agnostic server-code placement table included.

## When to use / when NOT
Use for server-side browser automation that must run isolated/untrusted-code-safe on Vercel (AI-generated code execution, scraping, visual checks). Do NOT use for simple fetches (plain HTTP suffices), for persistent browsers (sandboxes are ephemeral per task), or client-side automation.

## Inputs, outputs, tools
- Inputs: target URL + automation steps; env vars for credentials/snapshot.
- Outputs: screenshots (base64 via file read-back), accessibility snapshots, form-fill results.
- Tools: `@vercel/sandbox` SDK, agent-browser CLI inside VM, `sandbox.snapshot()`, Vercel Cron.

## 5 most important rules
1. `try/finally { await sandbox.stop() }` — never leak VMs; timeout 120_000 default.
2. Without `AGENT_BROWSER_SNAPSHOT_ID` every run pays ~30s dnf/npm install — create the snapshot once and set the env var for production.
3. Credentials: prefer OIDC on Vercel; explicit VERCEL_TOKEN/TEAM_ID/PROJECT_ID only for local dev.
4. agent-browser `--json` output gives paths/refs; screenshot returns a PATH — read it back with `base64 -w 0` inside the sandbox.
5. Snapshot the VM (infra image) ≠ accessibility snapshot (page tree) — don't confuse the two concepts.

## Risks / things needing the owner
Sandbox usage bills per VM time; snapshot creation is a one-time infra step needing Vercel auth. Running untrusted code is the POINT of sandboxes but still scope commands carefully. VERCEL_TOKEN is a secret — never commit it. Cron-triggered browser tasks need CRON_SECRET verification like other crons.

## Category / tags
cloud · vercel, sandbox, browser-automation, microvm

## Revisions
Single source read: `C:\Users\a7med\.codex\skills\vercel-sandbox\SKILL.md` (281 lines). Six-tool skill; codex revision representative.
