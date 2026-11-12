# search

- Tool: `gemini-plugin` (plugin: `mobbin`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\mobbin\skills\search\SKILL.md`
- SKILL.md size: 8166 chars

## What it does

Gets better results from every Mobbin search.

## Structure (headings inside SKILL.md)

- Searching Mobbin
- How search works
- Choosing the tool
- Writing the query
- Choosing the mode
- A second pull
- When a search falls short
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **The query also sets a language filter** on screens and flows when it names one ("Japanese banking app"). Name a language only when the task needs it.
- - **When results are weak, change the query.** Drop or reword a constraint, or use the user's own words. Don't add parts they didn't ask for. Raising `limit` or resending the query as it was brings back the same matches. To get more results for a query that works, see [A second pull](#a-second-pull)
- - `search_sections` and `search_flows`: the next `page`, dropping results already seen. When `has_next_page` is false, there is no next page, so change the query instead.
- 1. If the query spelled the name differently from the product, search again with the product's own spelling.

## Key rules (verbatim lines from SKILL.md)

1. - **Name an app only when the task needs it.** Adding an app name to the query filters results to that app. But not every result is from that app, so check `app_name` and `site_name` before citing.
2. - **When results are weak, change the query.** Drop or reword a constraint, or use the user's own words. Don't add parts they didn't ask for. Raising `limit` or resending the query as it was brings back the same matches. To get more results for a query that works, see [A second pull](#a-second-pull)
3. - **Every constraint comes from the request or the problem.** Never add parts you expect the target to have, such as an avatar on a profile or plan cards on a paywall. They narrow the results to screens that match your guess.
4. - **Search at the target's level.** A screen target searches the whole screen ("expense tracker home with no transactions"), never one card of it. A component target searches the screen it lives on.
5. - **Say each thing once.** "Empty state", "no transactions yet" and "before any are added" are one state. Keep the shortest.

## Files inside the skill

- (SKILL.md only)
