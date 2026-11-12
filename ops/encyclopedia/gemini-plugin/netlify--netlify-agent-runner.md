# netlify-agent-runner

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: ops
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-agent-runner\SKILL.md`
- SKILL.md size: 10827 chars

## What it does

Run AI agent tasks remotely on Netlify using.

## Structure (headings inside SKILL.md)

- Netlify Agent Runner
- Prerequisites
- Use only documented CLI surfaces
- How Agent Tasks Run
- Typical workflow
- Creating Agent Tasks
- Run a prompt with the default agent
- Choose a specific agent: claude, codex, or gemini
- Target a specific branch
- Specify a project by name (if not in a linked directory)
- Output result as JSON
- Options
- Managing Agent Tasks
- List tasks
- List all tasks for the current site
- Filter by status
- Output as JSON
- Show task details
- Stop a running task
- Use Cases
- Using as an Agent
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Do not read auth tokens** out of `~/Library/Preferences/netlify/config.json` (or anywhere on disk) to authenticate side-channel calls.

## Key rules (verbatim lines from SKILL.md)

1. - The site must be **linked to a Netlify project** (via `netlify link` or `netlify init`).
2. - The Netlify CLI must be installed and authenticated
3. - **Do not curl `https://api.netlify.com/...`** to fetch, create, or stop a task — the endpoint shapes are not part of the public contract.
4. - **Do not run `netlify api <method>`** as a recovery hatch when a documented command fails.
5. - **Do not read auth tokens** out of `~/Library/Preferences/netlify/config.json` (or anywhere on disk) to authenticate side-channel calls.

## Files inside the skill

- (SKILL.md only)
