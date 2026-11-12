# memory-leak-debugging (codex family)

Source read: `C:\Users\a7med\.codex\skills\memory-leak-debugging\SKILL.md` (4.3 KB; codex revision; cursor/kilo/opencode/windsurf/gemini-plugin listed; `references/common-leaks.md` exists).

## Summary
JS/Node memory-leak diagnosis workflow built on Chrome DevTools MCP heap tools. Prerequisite: advanced tools (`compare_heapsnapshots`, `get_heapsnapshot_*`) need the server started with `--memoryDebugging`; check availability first. Method: isolate browser vs Node leak; amplify by repeating user interactions ~10x; capture baseline/target/final `.heapsnapshot` files via `take_heapsnapshot`; compare with `get_heapsnapshot_summary` then `compare_heapsnapshots` (classIndex drills only for suspicious growth); trace retainers via `get_heapsnapshot_class_nodes`, `get_heapsnapshot_retainers`, `get_heapsnapshot_retaining_paths`, `get_heapsnapshot_dominators`, `get_heapsnapshot_edges`, `get_heapsnapshot_object_details`, `get_heapsnapshot_duplicate_strings`; use built-in categorized filters (`objectsRetainedByDetachedDomNodes`, `...EventHandlers`, `...Contexts`, `...Console`). Never read raw heapsnapshot files (token blowup); `close_heapsnapshot` after investigation.

## When to use / when NOT
Use for reported high memory usage, OOM errors, or heap-snapshot work in JS/Node. Not for native/memory leaks outside the JS heap, and not a substitute for fixing once the retainer path is found.

## Inputs, outputs, tools
- Inputs: a running page (pageId) or Node process with MCP memory debugging enabled; reproducible user interactions.
- Outputs: identified retaining path/root cause and fix guidance from `references/common-leaks.md`.
- Tools: chrome-devtools-mcp memory tools; `--memoryDebugging` server flag.

## 5 most important rules
1. Check `--memoryDebugging` availability before anything; if missing, fix MCP config first.
2. NEVER read raw `.heapsnapshot` files — always go through the MCP summary/compare/inspect tools.
3. Amplify the leak (repeat interactions ~10x) and capture baseline/target/final snapshots.
4. Start comparisons at summary level; drill into `classIndex`/nodeIds only for suspicious classes.
5. Always `close_heapsnapshot` loaded snapshots when done; ask the user before nulling detached DOM nodes (sometimes intentional caches).

## Risks / owner notes
Snapshots are huge — leaving them open exhausts MCP server memory. Detached-DOM "leaks" may be deliberate caches; confirm intent before changing code.

## Category and tags
Category: build. Tags: debugging, memory-leak, heapsnapshot, chrome-devtools-mcp, nodejs, performance.
