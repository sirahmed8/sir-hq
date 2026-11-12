# internet-skill-finder

Source read: `C:\Users\a7med\.claude\skills\internet-skill-finder\SKILL.md` (claude revision; codex/cursor/kilo/opencode/windsurf listed).

## Summary
A discovery-and-vetting workflow for finding agent skills, MCP servers, and prompt frameworks on the open internet. Discovery channels: GitHub topic searches (`agent-skills`, `mcp-servers`, `claude-skills`, `cursor-rules`), registries (skills.sh, pulsemcp.com, smithery.ai, glama.co/mcp), and benchmark signals (star trends, commit velocity, issue health, test coverage). Before adopting anything it mandates a zero-trust audit: scan for malicious payloads (eval, obfuscated base64, reverse shells, odd network calls), check dependency risk (abandoned packages, CVEs), verify license compatibility (flag GPL for commercial use), and prefer clean-room extraction of patterns over cloning dependencies.

## When to use / when NOT
Use when the user asks to find, evaluate, or import a skill/MCP/prompt framework from the internet. Do NOT use to install without vetting, and do not treat registry presence as a safety signal — vetting is mandatory.

## Inputs, outputs, tools
- Inputs: a capability to find (e.g., "a skill for X"), optionally a candidate repo/registry entry.
- Outputs: a vetted shortlist with scores/notes and, on approval, an import plan (preferably clean-room).
- Tools: web search/fetch, GitHub API/search, registries; `npx skills add` per workspace tooling for actual installs.

## 5 most important rules
1. Search the named channels first (GitHub topics + the four registries), then benchmark before recommending.
2. Audit every candidate for malicious payloads before ANY install or import.
3. Check dependency health: abandoned packages and known CVEs disqualify or downgrade.
4. Verify license; flag copyleft (GPL/AGPL) for proprietary/commercial projects.
5. Extract architecture/patterns clean-room rather than vendoring bloated or unvetted code.

## Risks / owner notes
Installing third-party skills/MCPs executes their code with agent privileges — the audit step is the only barrier. Owner should approve anything that adds executables or network endpoints.

## Category and tags
Category: research. Tags: skills, mcp, discovery, security-audit, supply-chain, registries.
