---
name: customization-architect
description: "Use when auditing, token-optimizing, or syncing AI assistant customizations such as skills, rules, and instruction files across tools."
---

# Customization Architect: 100x Customization, Skill & Rule Engineering

This skill defines the definitive protocol for auditing, engineering, optimizing, and synchronizing AI assistant customizations across **Google Antigravity**, **OpenAI Codex**, **Cursor**, and **Claude Code**.

---

## 1. The Token-Smart Customization Philosophy

Every customization rule, skill, and instruction must deliver maximum engineering leverage per token consumed:

1. **Information Density over Verbosity**:
   - Strip conversational fluff, preamble, and repetitive explanations.
   - Use high-density imperative directives, clear boolean tables, and concrete examples.
2. **Selective Plugin & Skill Activation**:
   - Never load heavyweight, domain-specific plugins globally (e.g. data science / BigQuery ETL plugins when working on frontend or native desktop).
   - Reserve global skills for cross-cutting standards: Architecture, Security, UI/UX, Production Engineering, and Customization.
3. **Cross-Platform Compatibility Matrix**:
   - **Antigravity**: Loaded via `~/.gemini/config/rules/AGENTS.md` and `~/.gemini/config/skills/<skill>/SKILL.md`.
   - **Cursor**: Loaded via project-root `.cursorrules` or `.cursor/rules/*.mdc`.
   - **OpenAI Codex / Copilot**: Loaded via project-root `AGENTS.md` or `.codex/instructions.md`.
   - **Claude Code**: Loaded via project-root `CLAUDE.md`.

---

## 2. File-by-File Audit & Enhancement Rubric

When auditing or refining any skill, rule, or configuration file, evaluate against this 5-point standard:

| Evaluation Vector | Failure Mode (Generic / Bloated) | 100x Production Standard |
| :--- | :--- | :--- |
| **Token Efficiency** | Verbose paragraphs, narrative intros | High-signal bulleted rules, code contracts |
| **Data Persistence** | Recommends in-memory arrays or stubs | Demands real persistent storage (Postgres, SQLite, Drift, Room) |
| **UI/UX Aesthetics** | Generic neon gradients, pill buttons everywhere | 60-30-10 color rule, purposeful radii, tactile physics |
| **Security & Auth** | Client-side role checks, raw string SQL | Server-side Zod validation, UUID tenant isolation, parameterized queries |
| **Defensive Execution** | Unchecked errors, empty try/catches | 5-state UI, atomic database transactions, idempotency keys, health checks |

---

## 3. Core Protocols for Skill Engineering

### Standard Skill Directory Anatomy
```text
~/.gemini/config/skills/<skill-name>/
├── SKILL.md            # Mandatory: YAML frontmatter + core executable instructions
├── references/         # Deep API specs, schemas, and architectural patterns (on-demand)
├── examples/           # Working code templates (zero TODO stubs)
└── scripts/            # Helper validation or scaffolding scripts
```

### Writing the Perfect `SKILL.md`
1. **Frontmatter**:
   ```yaml
   ---
   name: <kebab-case-name>
   description: <Actionable, third-person description with exact trigger conditions>
   ---
   ```
2. **Deterministic Trigger Map**: Explicitly state when the skill MUST and MUST NOT be activated.
3. **Non-Negotiable Guardrails**: Clear, bold rules prohibiting known antipatterns.
4. **Concrete Implementation Examples**: Real production code rather than abstract pseudo-code.

---

## 4. Cross-Platform Rules Synchronizer

To export and sync the master rules from `AGENTS.md` to external AI environments:

### For Cursor (`.cursorrules`):
Strip markdown headers that duplicate Cursor UI context; focus on file-level conventions, imports, and strict TypeScript/Python rules.

### For OpenAI Codex / GitHub Copilot (`AGENTS.md`):
Place a clean, focused `AGENTS.md` in the workspace root enforcing anti-monolith structure, test-driven validation, and zero fake data.

### For Claude Code (`CLAUDE.md`):
Include standard terminal build commands, test runners, linter invocations, and code style directives at the top of the file for instant CLI execution.

---

## 5. Token Budget Recovery Protocol

If Antigravity reports low available customization budget (<15%):
1. **Identify Heavy Inactive Plugins**:
   Inspect `~/.gemini/config/config.json`. Check for plugins injecting 20+ specialized skills (e.g. `data-agent-kit-plugin`).
2. **Deactivate Domain-Specific Plugins**:
   Set `"enabled": false` for plugins not relevant to current tasks.
3. **Consolidate Overlapping Skills**:
   Merge small, fragmented 1-paragraph skills into unified, cohesive reference modules.
4. **Prune Stale MCP Schemas**:
   Disable unused local MCP servers in `mcp_config.json`.
