# brainstorming

**Source:** `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\brainstorming\SKILL.md` (+ `visual-companion.md`, `builder-check-prompt.md`, `scripts/`)
**Category:** design
**Tags:** brainstorming, design-doc, planning, superpowers, requirements, visual-companion, product-discovery

## Summary
A superpowers skill that must be used before any creative work (creating features, building components, adding functionality, modifying behavior, or planning anything new, in software or out of it) to find out what the user actually wants and why before anything is built. It is a conversation framework: look before you ask, ask one question at a time, lay out approaches for the user to pick, write a design doc (short or full), get approval (a hard gate), then invoke `superpowers:writing-plans`. It adds a builder-check step that dispatches a fresh subagent to find gaps, and an optional visual companion (a browser tab for mockups and diagrams).

## When to use / when not to
Use it for any non-trivial creative work where the request is missing something important, or when the user explicitly asks for a design discussion or brainstorming. Do not use it for quick, fully specified tasks ("make the icon cornflower blue") where you simply do the work and report it, and it ends early if the user opts out of the questions.

## Inputs, outputs, tools
Inputs: the user's request, project context and code, and the answers to the conversation. Outputs: an approved design doc at `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`, then a plan produced by the writing-plans skill. Tools: subagent dispatch for the builder check, and the optional visual companion server (`scripts/start-server.sh`). No MCP.

## Five most important rules
1. Before implementing, lay out the approaches in a message of their own, write the design doc, get the user's approval, then invoke writing-plans; nothing is built before that approval (hard gate).
2. Look before you ask: read the project and the referenced context first, and never ask what it already answers or reopen a decided question.
3. Ask one question at a time, only when the answer would change what gets built; get the user describing before offering named options.
4. For a project-size design, dispatch a fresh builder-check subagent and sort its questions into already answered, minor (decide yourself and mark it), and theirs (only these go back to the user).
5. Use the visual companion only for visual questions (mockups, layouts, diagrams), offered just-in-time; keep requirements, scope and tradeoffs in text.

## Risks and owner actions
The hard gate means nothing gets built until the user approves the design doc, and the visual companion runs a local server that the user must open. No secrets are involved.

## Revisions
Only one copy exists (`.gemini/config/plugins/superpowers/skills/brainstorming`, 15190 bytes, dated 2026-11-12).
