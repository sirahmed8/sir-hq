---
name: repomix-token-optimizer
description: "Use when packing a codebase into a compact context with Repomix and Tree-sitter signature extraction to save tokens."
---

# Repomix Token Optimizer & Codebase Compressor

Inspired by [`yamadashy/repomix`](https://github.com/yamadashy/repomix), this skill provides guidelines for token-efficient codebase packing, AST signature compression, and secret scanning before feeding context to AI models.

---

## 1. Operating Principle: Tree-Sitter AST Pruning

When an AI assistant needs to understand the architecture of an entire project or package, feeding full source code with function implementations is wasteful.

**Tree-Sitter Compression**:
- Strips internal function and method bodies (`{ ... }`).
- Retains type definitions, interface contracts, class declarations, exported function signatures, and docstrings.
- **Result**: Reduces token usage by **60% to 75%** while retaining 100% of the semantic structural information needed for planning and reasoning.

---

## 2. Repomix CLI Execution

To pack a codebase into a single AI-friendly document:
```bash
# Run Repomix with AST compression enabled
npx repomix --compress --style xml

# Or using a custom configuration file
npx repomix --config repomix.config.json
```

### Security & Sanitization:
- Built-in **Secretlint** scans to prevent API keys, private tokens, or `.env` credentials from being included in packed output.
- Automatically respects `.gitignore` and `.repomixignore`.

---

## 3. Recommended `repomix.config.json`
```json
{
  "output": {
    "filePath": "repomix-output.xml",
    "style": "xml",
    "parsableStyle": true,
    "compress": true,
    "removeEmptyLines": true,
    "showLineNumbers": true
  },
  "ignore": {
    "useGitignore": true,
    "customPatterns": [
      "**/node_modules/**",
      "**/.git/**",
      "**/dist/**",
      "**/build/**",
      "**/.next/**",
      "**/*.lock"
    ]
  },
  "security": {
    "enableSecurityCheck": true
  }
}
```
