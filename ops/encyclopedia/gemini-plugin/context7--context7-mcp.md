# context7-mcp

## Summary
Thin skill wrapping the Context7 MCP server: when a question involves a library/framework/API, resolve the library to a Context7 ID (`resolve-library-id`), pick the best match (name fit, benchmark score, version-specific IDs, official over forks), then fetch docs with `query-docs` — one concept per query — and answer from current documentation instead of training data.

## When to use / when NOT
Use for setup/config questions, code involving known libraries ("Write a Prisma query..."), API references, or any mention of React/Vue/Svelte/Express/Tailwind etc. Do NOT use for general knowledge, proprietary/internal codebases, or when no library is involved.

## Inputs, outputs, tools
- Inputs: library name + what to look up; optional version mention.
- Outputs: current doc excerpts and code examples to ground the answer.
- Tools: Context7 MCP tools `resolve-library-id` and `query-docs`. Requires the Context7 MCP server configured.

## 5 most important rules
1. Always resolve-library-id first; never guess a library ID.
2. One topic per query-docs call — split multi-concept questions unless they ask how concepts interact (combined queries dilute ranking).
3. Prefer version-specific IDs when the user names a version ("Next.js 16", "React 19").
4. Prefer official/primary packages over community forks on ties.
5. Cite the library version when relevant in the answer.

## Risks / things needing the owner
Requires the Context7 MCP server (network service, sends library names/queries externally). Its description frontmatter is a stub ("This skill should be used when the user asks") — trigger matching is weak; the body carries the real triggers. Docs may lag newest releases.

## Category / tags
ai · docs, mcp, context7, research, libraries

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\context7\skills\context7-mcp\SKILL.md`. Only gemini-plugin holds it.
