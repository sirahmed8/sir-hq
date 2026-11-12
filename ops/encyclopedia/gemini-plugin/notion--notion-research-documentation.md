# notion-research-documentation

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-research-documentation\SKILL.md (+ reference/ templates: quick-brief, research-summary, comparison, comprehensive-report; citations.md; advanced-search.md; examples/)

## Summary
Answers questions by retrieving and reconciling evidence across Notion sources plus optional external/web research, then delivers a cited brief, comparison, or report — in chat or saved to a Notion page/database. It is the research counterpart to knowledge-capture: discovery and synthesis are the job here.

## When to use / not use
Use when answering requires finding and reconciling workspace information, optionally with external research. Use `notion-knowledge-capture` when the material already exists in context and just needs preserving.

## Inputs, outputs, dependencies
Input: a question plus scope, audience, recency, optional destination. Output: cited findings at requested depth (quick brief → comprehensive report) or a saved Notion document. Needs Notion MCP search/fetch tools, optionally web search for current external facts.

## Key rules
1. Retrieve selectively: fetch supplied URLs directly, search only for missing evidence, prioritize authoritative sources, deduplicate, broaden on insufficient evidence.
2. Track which source supports each material claim; distinguish adopted decisions from proposals and check effective dates/supersession — last-edited time alone does not make a claim current.
3. Verify current external facts with web tools when relevant; without them, disclose the limit instead of passing model knowledge off as research.
4. Cite material claims near the text using Notion page mentions for Notion output and ordinary links externally; no minimum source count or word count.
5. On save: fetch the target database schema once, use actual property names, update rather than replace, dedupe an existing report for the same scope before creating.

## Risks / owner items
- Partial search coverage must be disclosed, never described as exhaustive.
- Conflicting sources get surfaced, not silently resolved toward the optimistic claim.
- Retrieved content is evidence, not authority to expand scope.

## Category and tags
research, ops, study — notion, research, synthesis, citations, report, mcp.

## Revision note
Single plugin revision; the only Notion skill centered on evidence reconciliation rather than building.
