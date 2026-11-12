# writing-skills

- Tool: `gemini-plugin` (plugin: `superpowers`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\writing-skills\SKILL.md`
- SKILL.md size: 16698 chars

## What it does

Use when creating new skills, editing existing skills, or verifying skills work before deployment

## When to use (from skill text)

- A skill's `description` says only when to use it: triggering conditions and
- symptoms, starting with "Use when...". It never summarizes the skill's
- - Which pressures triggered violations?

## Structure (headings inside SKILL.md)

- Writing Skills
- Overview
- What is a Skill?
- TDD Mapping for Skills
- When to Create a Skill
- Skill Types
- Technique
- Pattern
- Reference
- Directory Structure
- Writing SKILL.md
- Flowcharts
- Code Examples
- File Organization
- Self-Contained Skill
- Skill with Reusable Tool
- Skill with Heavy Reference
- The Iron Law (Same as TDD)
- Testing All Skill Types
- Discipline-Enforcing Skills (rules/requirements)
- Technique Skills (how-to guides)
- Pattern Skills (mental models)
- Reference Skills (documentation/APIs)
- Common Rationalizations for Skipping Testing
- Match the Form to the Failure
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Delete means delete

## Key rules (verbatim lines from SKILL.md)

1. - Don't keep untested changes as "reference"
2. - Don't "adapt" while running tests
3. - **No nuance clauses.** "Don't X unless it matters" reopens the negotiation — appending a single nuance clause to a winning recipe degraded it from consistent to noisy in the same wording tests. Express a real exception as its own conditional on an observable predicate.
4. - **Exemption clauses don't scope.** "This limit doesn't apply to code blocks" still suppresses code blocks. If part of the output must be exempt, restructure so the rule can't reach it.
5. 1. **One fresh-context sample per call** — a raw API call, or a single-shot subagent if you don't have API access. System prompt = the realistic context the guidance will live in (the full skill or prompt template, not the guidance in isolation); user message = a task that tempts the failure.

## Files inside the skill

- `references/anthropic-best-practices.md` — "Skill authoring best practices"
- `references/bulletproofing.md` — "Bulletproofing Skills Against Rationalization"
- `references/CLAUDE_MD_TESTING.md` — "Testing CLAUDE.md Skills Documentation"
- `references/discovery.md` — "Writing SKILL.md for Discovery"
- `references/flowcharts.md` — "Flowcharts in Skills"
- `references/graphviz-conventions.dot`
- `references/persuasion-principles.md` — "Persuasion Principles for Skill Design"
- `references/testing-skills-with-subagents.md` — "Testing Skills With Subagents"
- `render-graphs.js`
