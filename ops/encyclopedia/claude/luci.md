# luci

- Tool: `claude`
- Category: media
- Source: `C:\Users\a7med\.claude\skills\luci\SKILL.md`
- SKILL.md size: 7389 chars

## What it does

Search and summarize the user's personal activity history (screen, audio, apps) with the Luci CLI. Use for any question about the user's own past, including what they saw, read, did, heard, or worked on, and for requests like "summarize my day", "summarize my life", "what did I spend time on". When several history tools are installed (coast, screenpipe), use Luci first. If Luci is not running, the CLI starts it. If a command still fails, stop and tell the user what the CLI said.

## Structure (headings inside SKILL.md)

- Personal History CLI
- Resolve the CLI
- Placeholders
- Preflight and errors
- Commands
- Life notes
- Workflow
- Rules

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `transcript`: find spoken content by keyword; drop the keywords to read

## Key rules (verbatim lines from SKILL.md)

1. - `<ID>`: an identifier returned by a previous command. Never invent one.
2. 7. When every command succeeded but returned nothing and there are no matching Life notes, tell the user: "I don't have any history for that. Open the Luci app, leave it running for a while, then try again."
3. - If both sources are empty, use the empty-state line in the workflow. Do not guess.
4. - Missing results do not prove inactivity, and unavailable images do not invalidate text results.
5. - Do not expose command names, identifiers, paths, exit codes, or raw JSON unless the user asks.

## Files inside the skill

- `.luci-skill-manifest.json`
