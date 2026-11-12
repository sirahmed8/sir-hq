# canva-cli (canva-cli)

## Summary
A minimal, near-empty skill whose entire body is one line: "Use the Canva CLI to use Canva's REST APIs." It declares no workflow, commands, inputs, or constraints — it is effectively a pointer/placeholder that delegates to the external Canva CLI tooling rather than documenting it.

## When to use / when NOT
Use only as a hint that a Canva CLI exists for hitting Canva's REST APIs. Do NOT rely on this skill for concrete command syntax, auth flows, or endpoint details — none are present; consult the Canva CLI's own docs/help. Not suitable for any task needing actionable instructions.

## Inputs, outputs, tools
- Inputs: none documented.
- Outputs: none documented.
- Tools: none named; implicitly the Canva CLI against Canva REST APIs.

## 5 most important rules
1. Treat this skill as a stub — it contains no usable procedure.
2. Do not invent CLI flags or endpoints from it; verify against installed Canva CLI help/docs.
3. Prefer the richer Canva MCP skills (edit-design, bulk-create, etc.) where they cover the need.
4. If a task requires Canva REST access, confirm the CLI is installed and authenticated first.
5. Consider replacing/augmenting this skill with real documentation before depending on it.

## Risks / things needing the owner
No operational content to audit; risk is over-trusting an empty skill and fabricating commands. Any real usage needs Canva account/CLI auth, which is an owner-side setup concern.

## Category / tags
design · canva, cli, rest-api, stub

## Revisions
Single revision: inactive copy at `C:\Users\a7med\.gemini\config\plugins\canva\inactive-skills\canva-cli\SKILL.md` (only ~80 chars: frontmatter + one-line body). No active duplicate. Skill name in frontmatter: canva-cli.