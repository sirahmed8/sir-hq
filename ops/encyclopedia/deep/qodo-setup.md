# qodo-setup

Tools: gemini-plugin (qodo plugin). Source: C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-setup\SKILL.md (73 lines) + references/{runtime,authentication,host-recovery,skill-updates}.md

## Summary
Brings Qodo from "plugin installed" to actually ready: verify a connected QAR MCP or resolve/install the `qodo` CLI (requires >=2.0.0), handle version-upgrade routing carefully (never print QODO_UPDATE_BASE_URL, preserve origin/exact versions/update holds), authenticate via `whoami` then refresh the tool catalog, and confirm task capability before handing back to work.

## When to use / not use
Use after plugin installation, on explicit setup requests, or when another Qodo skill reports a missing CLI or login. Not for daily work — once ready, the other qodo-* skills run directly.

## Inputs, outputs, dependencies
Input: a coding-agent environment needing Qodo. Output: verified CLI/MCP connection with refreshed tool catalog. Needs: shell access, Qodo CLI installer (checksum-pinned) or QAR MCP connection, `qodo read whoami`/`tools` commands.

## Key rules
1. Skill installation is not readiness — always verify with a harmless read (`whoami --json`) and check `isError` before trusting `structuredContent`; a catalog proves neither read nor write access.
2. Never handle credentials, never request API keys, never test-write; auth failures are capability problems, not login prompts.
3. Version gate: unparseable or <2.0.0 stops all authenticated calls; upgrade via one deployment-approved route only, preserving origin and exact versions — no channel substitution for pinned versions.
4. Order matters: `whoami` identity first, then `tools --refresh` to confirm capability; report "signed in but tools unavailable" distinctly from auth failure.
5. Never claim readiness after failure; no Keychain disabling, credential copying, or permission changes as workarounds.

## Risks / owner items
- Enterprise/customer deployments may have custom origins — guessing or falling back to Qodo Cloud is explicitly forbidden.
- QODO_UPDATE_BASE_URL overrides the recorded update source; if set, stop for the user rather than changing it.
- Optional Standards installation is NOT authorized by setup.

## Category and tags
ai, ops, build — qodo, setup, cli, mcp, authentication, code-review.

## Revision note
Single plugin revision (v1.0.14); the onboarding gate for the whole Qodo skill family.
