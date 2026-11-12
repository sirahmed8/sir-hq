# browse

- Tool: `gemini-plugin` (plugin: `browse`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\browse\skills\browse\SKILL.md`
- SKILL.md size: 17175 chars

## What it does

Browserbase browser automation CLI for.

## Structure (headings inside SKILL.md)

- Browse CLI
- Setup Check
- Browser Target Selection
- Browser Automation Workflow
- Parallel Browser Work
- Core Browser Commands
- Cloud APIs
- Browserbase Functions
- Templates
- Skills
- Discovering Browse.sh Skills
- Search Strategy
- Output Formats
- Best Practices
- Troubleshooting
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Chrome not found: use `--remote` with Browserbase credentials, install Chrome, or attach with `--cdp`.

## Key rules (verbatim lines from SKILL.md)

1. - the user asks to complete a task on a specific website — search the domain before automating it by hand
2. - If a search returns nothing, try synonyms (`flights` vs `travel`, `food` vs `restaurants`) before concluding no skill exists.
3. - Many slugs end in a generated suffix (`-2ikb22`), so never guess or construct them. Install only with an exact slug copied from `list` or `find` output: `browse skills add yelp.com/extract-reviews-2ikb22`. The installed skill becomes available to the agent as a regular skill; a new agent session m
4. 1. Run the real command and inspect its output instead of guessing.
5. 2. Use `browse snapshot` before interacting so you have current refs.

## Files inside the skill

- (SKILL.md only)
