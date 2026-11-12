# memory-leak-debugging

- Tool: `codex`
- Category: security
- Source: `C:\Users\a7med\.codex\skills\memory-leak-debugging\SKILL.md`
- SKILL.md size: 4348 chars

## What it does

Diagnoses and resolves memory leaks in JavaScript/Node.js applications. Use when a user reports high memory usage, OOM errors, or wants to capture, compare, or inspect heap snapshots with Chrome DevTools MCP memory tools.

## Structure (headings inside SKILL.md)

- Memory Leak Debugging
- Prerequisites
- Core Principles
- Workflows
- 1. Capturing Snapshots
- 2. Comparing Snapshots
- 3. Inspecting Retainers and Dominator Chains
- 4. Advanced Analysis and Categorized Filters
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tools, MCP configuration, MCP memory, MCP heap, MCP server

## Risks / cautions found in text

- - **Prefer MCP memory tools:** Do NOT attempt to read raw `.heapsnapshot` files directly, as they are extremely large and will consume too many tokens. Use the Chrome DevTools MCP heap snapshot tools to summarize, compare, and inspect snapshots.

## Key rules (verbatim lines from SKILL.md)

1. - **Prefer MCP memory tools:** Do NOT attempt to read raw `.heapsnapshot` files directly, as they are extremely large and will consume too many tokens. Use the Chrome DevTools MCP heap snapshot tools to summarize, compare, and inspect snapshots.
2. - **Common Culprits:** Look for detached DOM nodes, unhandled closures, global variables, event listeners not being removed, and caches growing unbounded. _Note: Detached DOM nodes are sometimes intentional caches; always ask the user before nulling them._
3. - **Close Loaded Snapshots:** Heap snapshots can be large. After completing an investigation, use `close_heapsnapshot` for each loaded snapshot to release memory held by the MCP server.
4. - Revert the page back to the original state after interactions to see if memory is released.
5. - Use `take_heapsnapshot` (with `pageId`) to save `.heapsnapshot` files to disk at baseline, target (after actions), and final (after reverting actions) states.

## Files inside the skill

- `references/common-leaks.md` — "Common Memory Leaks"
- `references/compare_snapshots.js`
- `references/memlab.md` — "Using Memlab"
