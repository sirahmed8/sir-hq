# is-agentic (vercel-plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\is-agentic\SKILL.md` (3.7 KB; gemini-plugin; `overlay.yaml` sibling). Audits web apps and MCP servers for "agent-readiness".

## Summary
A thin client skill for the public is-agentic.com audit service. It scores a URL 0-100 for how well AI agents can use the site, via `npx is-agentic <domain> --json` (returns a stored report or starts a scan and waits), a read-only REST API (`GET /api/v1/report?url=`), or an MCP endpoint (`https://is-agentic.com/mcp` with `is_agentic_get_report`, `is_agentic_get_methodology`, `is_agentic_get_developer_docs`). Reports are immutable `PublicScanReport` snapshots: `score` (nullable with `score_label`), `score_breakdown.essential/.recommended/.bonus`, `issues[]` with `id`, `tier`, `result`, evidence `details`, and a `recommendation`, plus canonical `report_url` and `scanned_at`. Improvement loop: fix essential failures first, then recommended, ignore bonus; re-scan and check `scanned_at` to avoid reading a stale snapshot.

## When to use / when NOT
Use to score or improve a public site's agent-readiness (docs for agents, MCP, structured content). Do NOT use on authenticated/private targets (score may be null), and do not treat bonus signals as defects.

## Inputs, outputs, tools
- Inputs: a public HTTP/HTTPS URL or domain (exact — path and query are separate reports).
- Outputs: JSON score report, issue list with fixes, `report_url` for humans.
- Tools: `npx is-agentic`, REST API, MCP server; all free, no API key; RFC 9457 problem+json errors (`invalid_url`, `report_not_found`, `rate_limit_exceeded`, `report_temporarily_unavailable`).

## 5 most important rules
1. Prefer the CLI; omit `--json` only for human terminal reading.
2. Work issues in order: essential failures → essential partials → recommended; bonus is additive, never required.
3. Reports refresh only when a visit finds them >6h old — after deploying fixes, verify `scanned_at` changed before concluding; use the page's Rescan for immediate re-runs.
4. API vs CLI differ on missing reports: API 404s, CLI starts a scan and waits — pick deliberately.
5. Honor `Retry-After` on 429; rate limit is 120 req/IP/60s; `Accept: text/markdown` gives token-light pages.

## Risks / owner notes
Sends the target URL to a third-party service — fine for public sites, never for private/internal URLs. Scores are snapshots; a green score can be up to ~6h stale.

## Category and tags
Category: web. Tags: seo, agent-readiness, audit, vercel, mcp, public-api.
