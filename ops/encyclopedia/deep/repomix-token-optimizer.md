# repomix-token-optimizer

Tools: claude (also codex/cursor/opencode/windsurf; claude chosen). Source: C:\Users\a7med\.claude\skills\repomix-token-optimizer\SKILL.md (66 lines, read in full)

## Summary
Guidelines for compressing a codebase into AI-context-friendly output using Repomix (`yamadashy/repomix`): Tree-Sitter AST pruning strips function bodies while keeping signatures/types/interfaces/docstrings (claimed 60-75% token reduction), Secretlint scans for leaked credentials, and .gitignore/.repomixignore are respected. Includes a recommended repomix.config.json.

## When to use / not use
Use when an agent needs whole-codebase architecture context but full source would blow the token budget — planning and reasoning tasks. NOT when exact implementation details are needed (bodies are stripped), for single-file questions, or as a substitute for targeted file reading.

## Inputs, outputs, dependencies
Input: a repository directory. Output: a packed XML document (signatures + structure, no bodies). Needs: `npx repomix` (downloads on demand), optional repomix.config.json, Tree-Sitter grammars via Repomix itself.

## Key rules
1. Compress mode is for STRUCTURE, not code: bodies stripped, contracts kept — use it to plan, then read real files for implementation.
2. Security is built in but verify: Secretlint scans for keys/tokens/.env; gitignore + repomixignore respected — still review output before sharing externally.
3. Use the provided config as baseline: xml style, parsableStyle, compress, removeEmptyLines, showLineNumbers, security check on.
4. Ignore noise explicitly: node_modules, .git, dist, build, .next, lock files in customPatterns.
5. Token math: 60-75% reduction claim applies to body-heavy code; interface/type-heavy codebases compress less.

## Risks / owner items
- Stripped bodies mean the packed context CANNOT answer "how does X work internally" — agents must follow up with real reads or they'll hallucinate implementations.
- Secret scanning reduces but doesn't eliminate leak risk (novel secret formats may pass); don't paste packed output into public tools.
- `npx repomix` executes a downloaded package — supply-chain consideration; pin version in CI use.
- Output file (repomix-output.xml) can itself be huge; it's a context artifact, not a deliverable.

## Category and tags
ai, build — repomix, token-optimization, context-engineering, codebase-analysis.

## Revision note
Identical across tools; single-file skill wrapping Repomix CLI best practices.
