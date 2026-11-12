# search (mobbin-search)

Tools: gemini-plugin (mobbin). Source: C:\Users\a7med\.gemini\config\plugins\mobbin\skills\search\SKILL.md (92 lines, read in full)

## Summary
The query-craft manual for Mobbin's three search tools: `search_screens` (app screens/components, ios|web platform), `search_sections` (marketing site sections, no platform), `search_flows` (user journeys). Teaches meaning-based natural-language queries, the 3-constraint limit, mode selection (standard vs deep), pagination via exclude_screen_ids/page, and failure recovery — invoked by calling skills like redesign-screen.

## When to use / not use
Use whenever calling any Mobbin search tool — it defines HOW to query well. NOT a standalone research tool; it serves calling skills (redesign-screen etc.) and says so itself. Read best-practices skill first per its own instruction.

## Inputs, outputs, dependencies
Input: a search intent (screen/section/flow target). Output: ranked Mobbin results with app_name/site_name/image_url/webp previews. Needs: Mobbin MCP tools; `platform` ios|web only (no Android — search ios and disclose); calling skill's query rules override these defaults.

## Key rules
1. Meaning over keywords: plain phrases beat keyword lists; type+domain are free, each state/step/visual-trait is ONE constraint, max three — extras stay in your head, never a second query.
2. Constraints come ONLY from the request/problem — never add expected parts (avatars, plan cards) that narrow to your guess; never put the problem or a fix in the query.
3. Tool choice: screen/component → search_screens+platform; marketing section → search_sections; journey or step-in-context → search_flows. One target per query, one call per screen type.
4. mode: no constraints → standard; 1-3 constraints → deep (drops weak matches, may return fewer than limit — short pull ≠ empty database).
5. Second pull = same query + exclude_screen_ids (screens) or next page (sections/flows); weak results → reword, don't raise limit. Webp previews that won't open → retry image_format=jpg; a screen you couldn't see is not a reference.

## Risks / owner items
- iOS/web only — Android targets silently search iOS and MUST be disclosed as such.
- Language filter is implicit in query phrasing — name a language only when needed.
- Tool refusal is terminal for that call (don't retry/reword); input errors are fixable.
- Named-product misses: try exact spelling → next page → other platform → then proceed without it, never describe the missing product from memory.

## Category and tags
design, research — mobbin, search, ux-research, query-craft.

## Revision note
Single plugin revision; the shared search discipline layer for all Mobbin skills.
