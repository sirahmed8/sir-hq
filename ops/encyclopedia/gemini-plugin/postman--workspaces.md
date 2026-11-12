# workspaces

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\workspaces\SKILL.md`
- SKILL.md size: 3818 chars

## What it does

Use when initializing Postman in a repository, binding it to a Postman workspace, interpreting what `postman init` did, or handling CLI-suggested actions for authentication, plan, credits, usage quota, or subscription restrictions. Treats the workspace as the place where a service's API work and its evidence live, kept separate from the services it depends on. Use for requests such as "set up Postman in this repo" or "connect this repo to our workspace".

## Structure (headings inside SKILL.md)

- Workspaces
- Claiming the work
- Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1. `postman init` is the starting point. It gives the repository its place of
2. 2. One workspace holds the context of one service: one Git repository, or in a
3. 3. Other services keep their own workspaces. Their collections, environments,

## Files inside the skill

- (SKILL.md only)
