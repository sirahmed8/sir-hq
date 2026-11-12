# antigravity_guide

Source read: `C:\Users\a7med\.gemini\antigravity\builtin\skills\antigravity_guide\SKILL.md` (3.0 KB; gemini revision; references in `references/`).

## Summary
Google Antigravity (AGY) guide and offline sitemap that maps the agent surfaces (CLI `agy`, IDE, Antigravity 2.0 desktop app, Python SDK) and tells the agent which subdocumentation to read for the asked surface.

## When to use / when NOT
Use when the user asks how to use, configure or customize Antigravity, the AGY CLI, the Antigravity IDE, Antigravity 2.0, or the Antigravity SDK. Do NOT use for general Gemini model questions or for other agent platforms.

## Inputs, outputs, tools
- Inputs: the Antigravity surface or feature question.
- Outputs: pointer to the matching reference file plus the live documentation sitemap when needed.
- Tools: references (cli, ide, app, sdk); live fetch of `https://antigravity.google/docs` and its sitemap pages.

## 5 most important rules
1. Read the subdocumentation that matches the asked surface; do not answer from memory.
2. When the question is about the latest updates, advanced Vertex AI integrations or complex setups not covered offline, fetch the live docs.
3. The CLI is configured via `~/.gemini/antigravity-cli/settings.json`; use `agy` flags and `/help` inside the TUI.
4. The Python SDK installs via `pip install google-antigravity`; use the Agent async context manager with LocalAgentConfig and CapabilitiesConfig, stream thoughts and tool calls, or run the interactive loop.
5. The IDE and Antigravity 2.0 coexist; the IDE is the in-editor surface and 2.0 the parallel desktop app, sharing the same agentic capabilities.

## Risks / things needing the owner
Owner-specific Antigravity customizations (skills, rules, MCP, sidecars) live outside this skill; owner sign-in may be required for CLI or SDK use.

## Category / tags
Category: ai. Tags: antigravity, agy, sdk, cli, ide, agent, mcp, gemini.

## Revisions
Single copy in the antigravity builtin set (3.0 KB). No competing revisions.
