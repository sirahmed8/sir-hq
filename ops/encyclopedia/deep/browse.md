# browse

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\browse--browse.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A web browsing skill that fetches and parses webpage content, extracting main text, headings, links, and metadata. It can render JavaScript-dependent pages using a headless browser, scroll to specific sections, and capture screenshots. The skill is designed for research, data aggregation, and content extraction tasks, and respects robots.txt and meta robots tags.

## When to use / when NOT
Use when you need to extract content from a webpage quickly — the skill handles HTTP fetching, JavaScript rendering, and content parsing in one step. Do NOT use for scraping protected data or bypassing authentication — the skill only fetches publicly accessible content and will return an error if a page requires login. Do NOT set a very high scroll depth without a specific target — the skill may scroll indefinitely; always set a maximum scroll count or a target selector.

## Inputs, outputs, tools
- Inputs: URL to browse, maximum scroll count, CSS selector for target content, wait time (ms).
- Outputs: extracted text content, headings hierarchy, list of links with URLs and anchor text, page metadata (title, description, author), screenshot (optional).
- Tools: headless Chrome/Playwright, HTML parser, meta robots checker, robots.txt fetcher. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always respect robots.txt** — the skill checks robots.txt before browsing; if the page is disallowed, it will return an error rather than bypassing the restriction.
2. **Set a maximum scroll count** — the skill defaults to 10 scrolls; increase only if you have a specific target selector that requires more scrolling.
3. **Use CSS selectors to target specific content** — the skill can extract content matching a CSS selector; this avoids capturing navigation menus, footers, and other non-essential elements.
4. **Set a reasonable wait time** — the skill defaults to 2000ms for page load; reduce for faster browsing or increase if the page loads slowly.
5. **Cache frequently browsed URLs** — the skill does not include caching; if you browse the same URLs repeatedly, implement a Redis or in-memory cache to reduce API calls and speed up retrieval.

## Risks / owner notes
The skill may capture navigation menus, footers, and advertisement content if no CSS selector is provided; the owner should always use a selector to target the main content area. JavaScript-rendered content may not always be captured correctly if the page uses dynamic loading patterns that the headless browser cannot detect; manual verification of extracted content is recommended for critical use cases.

## Category / tags
research · web-scraping, content-extraction, headless-browser, html-parsing, robots-txt, data-aggregation

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.