# notion-set-up-my-project

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-set-up-my-project\SKILL.md (+ reference/design.md, reference/project-home-layout.md, reference/meetings.md, examples/self-serve-onboarding.md)

## Summary
Creates an initial Notion project home — outcome, scope, known work, people, decisions — connected to Tasks, Docs, and meeting notes, then asks short tuning questions (team, cadence, which Projects database) to refine the same artifact. For EPD work it builds the full project→tasks→docs→meetings structure; lighter projects get lighter structure.

## When to use / not use
Use when starting or organizing a project in Notion. Not for routine task edits, status reports, implementing a spec (that's `notion-spec-to-implementation`), or when another system (GitHub/Linear) already owns tasks — link it instead of building a competing tracker.

## Inputs, outputs, dependencies
Input: project name, outcome, audience, scope, people, deliverables, agreed dates. Output: a project home page with populated Tasks/Docs collections, relations, filtered views, prepared agenda; then refined in place after answers. Needs Notion MCP tools.

## Key rules
1. Deliver a useful private draft FIRST, then ask tuning questions — never gate the initial output on placement/collaborator/cadence questions.
2. Unknown owners/dates stay unset; conflicting dates preserved; proposed steps labeled separately from agreed work; no fabricated people, commitments, or progress percentages.
3. Placement: honor an explicitly chosen Projects database; otherwise build a private draft and reconcile (move, not duplicate) once a destination is chosen. Project views must filter by relation to the exact record, never by name.
4. EPD checklist: real Tasks and Docs databases with typed properties, docs covering brief/spec/proposal/decision/rollout only as supported by context, meeting notes with a prepared agenda — all populated, not empty shells.
5. If code/external issues exist, link them; setup does not imply sending assignments, invites, or changing external issues.

## Risks / owner items
- Unmatched person names stay as text — never assign the wrong Notion account.
- Being a collaborator does not make someone a task owner or approver.
- Verify project relations exclude other projects; a polished home with empty record bodies fails verification.

## Category and tags
ops, build — notion, project-management, tasks, docs, mcp.

## Revision note
Single plugin revision; unique "deliver-then-tune" flow among the Notion skills.
