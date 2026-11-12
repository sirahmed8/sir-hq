# repomix-token-optimizer

- Tool: `claude`
- Category: ops
- Source: `C:\Users\a7med\.claude\skills\repomix-token-optimizer\SKILL.md`
- SKILL.md size: 1994 chars

## What it does

Use when packing a codebase into a compact context with Repomix and Tree-sitter signature extraction to save tokens.

## Structure (headings inside SKILL.md)

- Repomix Token Optimizer & Codebase Compressor
- 1. Operating Principle: Tree-Sitter AST Pruning
- 2. Repomix CLI Execution
- Run Repomix with AST compression enabled
- Or using a custom configuration file
- Security & Sanitization:
- 3. Recommended `repomix.config.json`
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Result**: Reduces token usage by **60% to 75%** while retaining 100% of the semantic structural information needed for planning and reasoning.
- - Built-in **Secretlint** scans to prevent API keys, private tokens, or `.env` credentials from being included in packed output.

## Key rules (verbatim lines from SKILL.md)

1. - Strips internal function and method bodies (`{ ... }`).
2. - Retains type definitions, interface contracts, class declarations, exported function signatures, and docstrings.
3. - **Result**: Reduces token usage by **60% to 75%** while retaining 100% of the semantic structural information needed for planning and reasoning.

## Files inside the skill

- (SKILL.md only)
