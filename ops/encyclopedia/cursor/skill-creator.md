# skill-creator

## Summary
skill-creator is a meta-skill: it teaches an agent how to invent and register brand-new skills on the fly instead of stopping when no existing skill fits. It defines a quality bar every generated skill must meet (valid YAML frontmatter with a trigger-rich description, concrete first-principles content, executable typed code blueprints, explicit anti-hallucination guardrails, and a standard folder layout with optional scripts/ and references/), then a 4-step protocol: deconstruct the domain into inputs, transformations, deliverables and edge cases; draft triggers and behavioural constraints; write SKILL.md; register it so later sessions can auto-activate it. It is guidance text only; the agent does the authoring with its normal file tools.

## When to use / when NOT
Use when the owner asks for a new capability, workflow or automation that no installed skill covers, or when a recurring task deserves a permanent skill. Do NOT use it for one-off tasks (just do the work), for editing an existing skill (edit it directly), or for installing a third-party skill (that is skill-installer / skills-discovery-engine).

## Inputs, outputs, tools
- Inputs: a description of the capability or workflow the owner wants, plus knowledge of the machine's skill directories.
- Outputs: a new `<skill-name>/SKILL.md` plus optional `scripts/` and `references/` folders under the chosen skills root, and a manifest/index entry if the tool requires one.
- Tools: plain file read/write plus knowledge of where each harness keeps skills (`.claude/skills`, `.codex/skills`, `.config/kilo/skills`, `.cursor/skills`, `.codeium/windsurf/skills`, `.gemini/config/skills`). No MCPs, no network.

## 5 most important rules
1. Frontmatter must be exactly `name:` and `description:`, and the description must say WHEN to trigger, not just what it does.
2. Content must be first-principles methodology with concrete formulas/rules, not vague advice.
3. Include executable blueprints (Python/TypeScript/Bash/XAML) showing real usage.
4. Add explicit guardrails: what the skill must NOT do (anti-slop, anti-hallucination, safety boundaries).
5. Place output in the standard layout `skills/<name>/SKILL.md` with optional `scripts/` and `references/`; the claude revision hard-codes the Gemini skills path as the install target, which is a quirk to be aware of.

## Risks / things needing the owner
Low risk: it only writes markdown and small scripts. The real risk is skill sprawl and poorly-triggered skills that fire on unrelated tasks; descriptions need care. Nothing here needs the owner unless a new skill would touch secrets, payments or private data, which then falls under the normal law.

## Category / tags
ops · meta-skill, skill authoring, automation, agent tooling

## Revisions
Six copies exist (claude, codex, kilo, cursor, windsurf, opencode). The codex/kilo/cursor/windsurf/opencode copies are byte-identical (2081 bytes); the claude copy (1988 bytes) differs only in the frontmatter description wording and otherwise carries the same body. Best revision: any of the identical five; the claude copy is equally valid but its description is terser. Content quality is identical, so pick whichever harness is running.
