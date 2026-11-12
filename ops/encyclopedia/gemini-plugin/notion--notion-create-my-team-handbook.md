# notion-create-my-team-handbook

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-create-my-team-handbook\SKILL.md (+ reference/design.md, reference/handbook-layout.md, examples/studio-handbook.md)

## Summary
Turns scattered team processes, documents, and requests into a usable Notion handbook: an approachable home routing employees to procedures, a guidance library with named stewards and review states, and an optional request desk database for tracking individual requests linked to procedures.

## When to use / not use
Use to establish or reorganize a team handbook / onboarding system. Not for routine edits to existing records, and not when authoritative policy lives elsewhere — link it rather than copying competing versions.

## Inputs, outputs, dependencies
Input: team name, recurring work, audience, existing procedures/requests. Output: Notion home page + guidance records + optional request-desk database with relations and views. Needs Notion MCP tools and the two reference files.

## Key rules
1. Build around the primary job (find procedures / onboard / handle requests); separate reusable procedures from individual executions.
2. Guidance records carry title, purpose/area, confirmed steward, and review state; dates only when evidence supports them — copying a page is not a policy review.
3. Each procedure states when to use it, inputs, ordered steps, expected result, exceptions/escalation; unresolved steps stay marked open; proposed guidance stays distinct from approved policy.
4. Requests get title, status, coordinator, due date when agreed, and a native relation to the procedure; open/unassigned/undated work must stay discoverable.
5. Keep confidential HR/finance/customer data in its authorized destination — filtered views are not access control. Walk the result as both employee and operator before calling it done.

## Risks / owner items
- Explicit warning: filtered views do not restrict access; sensitive material must live in its proper secured location.
- Does not authorize invitations, notifications, or permission changes.
- Repeat requests must match existing work before creating to avoid duplicates.

## Category and tags
ops, study — notion, handbook, onboarding, procedures, team-knowledge, mcp.

## Revision note
Single plugin revision; shares the Notion plugin's common skeleton (context → build → verify → panel).
