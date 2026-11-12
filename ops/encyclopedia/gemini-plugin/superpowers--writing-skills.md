# writing-skills (gemini-plugin: superpowers)

## Summary
writing-skills applies TDD to skill authoring itself: writing a SKILL.md IS test-driven development applied to process documentation. The cycle maps test cases to pressure scenarios run with subagents — RED is watching an agent violate the rule WITHOUT the skill and documenting its rationalizations verbatim, GREEN is writing minimal skill text that addresses exactly those failures, REFACTOR is closing newly discovered loopholes and re-verifying. It classifies skills (technique, pattern, reference, discipline-enforcing) with different test approaches for each, gives SKILL.md authoring rules (description starts "Use when..." and says only WHEN, never summarizes the workflow; flat namespace; heavy reference in separate files; one excellent code example not five languages), and adds advanced guidance: match the guidance FORM to the failure type (prohibition+red-flags for discipline failures vs positive recipe/contract for output-shape problems — prohibitions measurably backfire on shaping problems), micro-test wording with 5+ reps against a no-guidance control before full pressure scenarios, and a mandatory per-skill deployment checklist. References include anthropic-best-practices, discovery, flowcharts, bulletproofing, and testing-skills-with-subagents.

## When to use / when NOT
Use when creating a new skill, editing an existing one, or verifying a skill works before deployment. Do NOT use for one-off prompts, project-specific conventions (those go in AGENTS.md/instructions), or mechanical constraints enforceable by regex/validation (automate those instead of documenting). Requires test-driven-development as background.

## Inputs, outputs, tools
- Inputs: the capability/process to document, baseline pressure scenarios, and subagents to run them.
- Outputs: a tested SKILL.md (+ optional supporting files) deployed to the runtime skills directory (`~/.claude/skills/`, `~/.agents/skills/` cross-runtime alias, etc.).
- Tools: subagent dispatch for pressure testing, micro-test API calls, graphviz for flowcharts (render-graphs.js), git for committing the skill.

## 5 most important rules
1. NO SKILL WITHOUT A FAILING TEST FIRST — run baseline scenarios before writing; edits to existing skills need testing too.
2. The description field says only WHEN to use the skill ("Use when..." + triggers/symptoms), never a workflow summary — summaries get followed instead of the skill.
3. Match form to failure: discipline failures need prohibition + rationalization table + red flags; output-shape failures need a positive recipe stating what the output IS; omitted elements need structural REQUIRED fields; condition-dependent behavior needs conditional rules on observable predicates.
4. No nuance clauses or exemption clauses — "don't X unless it matters" reopens negotiation; express exceptions as their own conditionals.
5. Micro-test wording before full scenarios: fresh-context samples, always include a no-guidance control, 5+ reps per variant, read every flagged match manually, treat variance across reps as a binding failure.

## Risks / things needing the owner
Skill testing costs real subagent runs; the checklist is mandatory per skill and forbids batch-creating untested skills. Over-testing trivial reference skills wastes effort — the skill itself says pure reference skills can skip wording micro-tests. Deployment includes optional PR contribution back upstream. Nothing needs the owner.

## Category / tags
ops · skill-authoring, tdd, documentation, superpowers, agent-tooling

## Revisions
Only one revision exists: the gemini-plugin superpowers copy, the most complete version (SKILL.md, render-graphs.js, references/ with anthropic-best-practices, discovery, flowcharts, bulletproofing, testing-skills-with-subagents). No divergent copies.
