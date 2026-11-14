---
name: skill-creator
description: "Use when creating a new agent skill with its SKILL.md, scripts, and references from a described capability or workflow."
---

# Skill Creator (Autonomous Meta-Skill Architecture Engine)

This skill provides an autonomous framework for inventing, authoring, validating, and registering brand-new agent skills on the fly to permanently expand the agent's capabilities.

---

## 1. Skill Lifecycle & Standards

Every skill created by this engine must satisfy the 5-point quality checklist:
1. **Valid YAML Frontmatter**: Exactly `name:` and `description:` at the top. The description must be detailed and describe *when* to trigger.
2. **First-Principles Theory & Best Practices**: Concrete methodologies, formulas, and structural rules rather than vague advice.
3. **Executable Blueprints**: Typed code snippets (Python / TypeScript / Bash / XAML) demonstrating real-world usage.
4. **Anti-Slop / Anti-Hallucination Guardrails**: Clear boundaries outlining what *not* to do.
5. **Directory Placement**: Installs directly to `C:\Users\a7med\.gemini\config\skills\<skill-name>\SKILL.md`.

---

## 2. Directory Architecture

```
C:\Users\a7med\.gemini\config\skills\<skill-name>/
├── SKILL.md              # Mandatory: Main instructions & trigger definition
├── scripts/              # Optional: Reusable CLI or Python helper utilities
└── references/           # Optional: Cheat sheets, API schemas, and templates
```

---

## 3. Autonomous Skill Generation Protocol

When asked to create a skill for a new workflow:
1. **Deconstruct the Domain**: Identify the core inputs, transformations, output deliverables, and edge cases.
2. **Draft the Specification**: Formulate triggers, keywords, and behavioral constraints.
3. **Write `SKILL.md`**: Implement markdown sections covering Architecture, Formulas, Blueprints, and Constraints.
4. **Register**: Ensure manifest/index recognizes the skill for autonomous activation across sessions.
