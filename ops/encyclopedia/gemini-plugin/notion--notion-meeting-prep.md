# notion-meeting-prep

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-meeting-prep\SKILL.md (+ reference/ templates for decision, status, brainstorm, sprint, retro, 1:1; reference/next-meeting.md, meeting-to-actions.md; examples/)

## Summary
Prepares meeting materials — agendas, internal pre-reads, decision briefs — grounded in Notion context plus selective research. It scales depth to the meeting, keeps internal strategy out of external/customer agendas, and can optionally record outcomes and follow-up tasks afterward.

## When to use / not use
Use for preparing the next or a named meeting, recurring-meeting context, or updating meeting outcomes. Use `notion-knowledge-capture` for a standalone record of an already-held discussion.

## Inputs, outputs, dependencies
Input: meeting purpose, date, duration, attendees, audience, project; optional Notion destination. Output: chat brief or saved agenda/pre-read pages (with draft status respected). Needs Notion MCP tools, optionally calendar tools for "next meeting" prep, and web search for current external facts.

## Key rules
1. Establish scope first; ask only for details that materially change preparation. Default to an agenda; add a pre-read only when substantial internal background justifies it.
2. For "next/upcoming" meetings with calendar tools, create and show the agenda first, then improve the same note with one focused research pass — no connector search in that path.
3. Distinguish source facts from analysis; cite evidence; if research tools are unavailable, state the gap rather than presenting model knowledge as current.
4. Audience separation is strict: customer agendas omit internal strategy and negotiation positions; "Internal" titles do not establish permissions — resolve placement when audience is uncertain.
5. Time allocations must fit the known duration; unknown owners/dates/metrics stay labeled unknown; preparing docs does not authorize invitations, sharing, or messages.

## Risks / owner items
- Internal-only material saved to the wrong destination is a real confidentiality risk; the skill errs toward keeping it in draft.
- Research claims need live web tools; without them the output must disclose limited currency.
- Follow-up task creation stays within requested scope; unresolved items carry forward.

## Category and tags
ops, business — notion, meetings, agenda, pre-read, mcp.

## Revision note
Single plugin revision; uniquely handles the internal/external audience split and calendar-driven "next meeting" flow.
