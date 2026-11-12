# notion-weekly-project-digest

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-weekly-project-digest\SKILL.md (+ examples/mixed-evidence.md)

## Summary
Produces evidence-based weekly project/team updates by comparing the reporting period against a baseline (previous digest or dated snapshot). Its core discipline is an evidence table: a current "Done" status proves only current state, a last-edited timestamp proves only an edit, and only a completion event or reliable completion date proves work finished this period.

## When to use / not use
Use for recurring status digests and weekly updates. Use `notion-spec-to-implementation` for requirement-level implementation tracking; a chat update need not become a Notion page.

## Inputs, outputs, dependencies
Input: project/team name, audience, reporting period, optional destination. Output: a cited digest (chat or saved update record) leading with meaningful changes, continuing blockers carried forward as continuing-not-new, decisions, and next steps. Needs Notion MCP tools with schema inspection and paginated queries.

## Key rules
1. Set scope and resolve the timezone/date boundary when it changes inclusion; state reasonable date assumptions.
2. Find a baseline first: previous digest or dated snapshot; without history, deliver a clearly labeled first snapshot — never invent trends or week-over-week improvement.
3. Apply the evidence table strictly: merged PR ≠ released to users; dedupe records across views; trace changed decisions to supporting notes; report conflicts rather than picking the optimistic claim.
4. Metrics need named population and denominator; counts ≠ estimates; never average percentages across unrelated projects or turn task counts into delivery confidence.
5. Save path: dedupe an existing digest for the same project+period+audience before creating; set the project relation; producing a digest does not authorize task changes or messages.

## Risks / owner items
- Internal-only details must stay out of external-facing updates.
- Partial query coverage must be reported; paginate before making complete-coverage claims.

## Category and tags
ops, business — notion, weekly-report, status-update, metrics, mcp.

## Revision note
Single plugin revision; the evidence-discipline table is its distinguishing feature.
