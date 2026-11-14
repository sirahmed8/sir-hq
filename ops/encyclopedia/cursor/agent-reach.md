# agent-reach

Source read: `C:\Users\a7med\.agents\skills\agent-reach\SKILL.md` plus `references/capabilities.md`, `references/sessions.md`, and `references/maintenance.md`.

## Summary
Agent Reach is a read-only command-line skill for fetching public content across many platforms through one `agent-reach` CLI. It prefers the agent's own public search tools first, then uses Reach channels for search, reading, comments, subtitles, transcripts, market quotes, jobs, and platform-specific actions, returning JSON results with explicit error codes when setup, login, rate limits, blocks, or missing content prevent access.

## When to use / when NOT
Use when the user shares a supported platform link or asks for public content that built-in search cannot fully retrieve, and when a declared channel action is needed. Do not use it for posting, commenting, liking, private messages, logging in on the user's behalf, password handling, private data, or guarantees of complete comment trees and media understanding.

## Inputs, outputs, tools
Inputs are a channel or link, an action and parameters, optional backend selection, and the current login or setup state. Outputs are JSON with `ok`, `items`, `raw`, `meta`, or `error.code` plus hints. Tools are the `agent-reach` CLI commands (`channels`, `read`, channel actions, `add`, `remove`, `login`, `logout`, `doctor`, `check`, `update`, `uninstall`, `browser`, `configure`, `skill link`), a dedicated CloakBrowser or Chrome profile, OpenCLI extension import, and optional keys for services such as Groq or OpenAI.

## 5 most important rules
1. Announce that Agent Reach is being used, then prefer public built-in tools before installing or logging into channels.
2. Run `agent-reach channels` when the available actions or parameters are unclear.
3. Never perform write actions, log in for the user, ask for passwords, or output cookies and credentials.
4. Handle error codes deliberately: setup gaps may use `add` or `configure`, login needs the user, while `RATE_LIMITED`, `PLATFORM_BLOCKED`, `BUSY`, and `UPSTREAM_BROKEN` mean stop rather than retry loops.
5. Respect platform limits: Xiaohongshu read returns text descriptions only, Boss salary fields marked encoded must not be guessed, and subtitle tracks are not the same as transcript text.

## Risks / owner notes
Reach depends on external platforms, browser sessions, rate limits, and optional paid or login-backed paths. The owner may need to install a channel, connect OpenCLI, provide a key, or complete a visible login. Updates should happen only after the user agrees, and maintenance actions should distinguish dependency, browser, login, page-load, and platform failures.

## Category / tags
research · read-only, agent-reach, social-platforms, youtube, github, web-scraping, browser-automation, subtitles

## Revisions
Single workspace-owned source at `C:\Users\a7med\.agents\skills\agent-reach\SKILL.md`, version 1.6.0 in frontmatter. No codex, claude, kilo, cursor, opencode, or windsurf copy was present.
