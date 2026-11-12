# using-superpowers (gemini-plugin: superpowers)

## Summary
using-superpowers is the entry-point/meta skill of the superpowers plugin: it establishes that BEFORE any response or action — including clarifying questions or codebase exploration — the agent must check whether any skill applies and invoke it if there is even a 1% chance. It defines skill priority (process skills like brainstorming and systematic-debugging come before implementation skills), announces usage ("Using [skill] to [purpose]"), converts skill checklists into todos, and lists the rationalization table that kills excuses like "this is just a simple question" or "the skill is overkill". It also carries platform-adaptation pointers (references for Claude Code, Codex, Pi, Antigravity, Hermes, Muse tool specifics) and the precedence rule: user instructions > skills > default behavior. Dispatched subagents are explicitly told to ignore it.

## When to use / when NOT
This skill is meant to be active at the start of every conversation in a harness where superpowers is installed — it is the "how to use skills" rulebook. Do NOT apply its mandatory-invocation pressure when you are a dispatched subagent executing a specific task (the SUBAGENT-STOP block exempts you), and do not let it override explicit user instructions, which outrank skills.

## Inputs, outputs, tools
- Inputs: the incoming task or question, plus the installed skill catalog.
- Outputs: a skill invocation decision, an announcement line, and todos mirroring the skill's checklist.
- Tools: the harness's skill-invocation mechanism; reference files per platform for tool-name differences. No scripts.

## 5 most important rules
1. Skill check comes BEFORE clarifying questions, exploration, or any action — even for "simple questions".
2. If a skill might apply (1% threshold), invoke it; if it turns out wrong for the situation, you may drop it after reading.
3. Process skills first: "let's build X" → brainstorming; "fix this bug" → systematic-debugging; then domain skills.
4. Announce "Using [skill] to [purpose]" and follow it exactly, making a todo per checklist item.
5. User instructions (CLAUDE.md/AGENTS.md/direct requests) take precedence over skills; only explicit user override skips a skill workflow.

## Risks / things needing the owner
The 1% rule can cause over-triggering (invoking skills on trivial tasks), which costs tokens; the escape hatch is "if it turns out wrong, don't have to use it" but the check itself is mandatory. In the SIR workspace this conflicts mildly with the sir-skill-library approach of NOT loading hundreds of skills; the practical resolution is to check the catalog cheaply (the skill list) rather than invoking speculatively. Subagents must not re-trigger this recursively.

## Category / tags
ops · meta-skill, superpowers, skill-routing, methodology

## Revisions
Only one revision exists: the gemini-plugin superpowers copy (SKILL.md plus a references/ folder with per-platform tool notes). No divergent copies.
