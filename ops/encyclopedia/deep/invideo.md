# invideo (hub skill)

Source read: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\invideo\SKILL.md` (7 KB; gemini-plugin hub for the whole invideo suite; `references/` holds per-type playbooks and `check-your-video.md`, `cost-rule.md`, `collaborate.md`).

## Summary
The root skill for invideo, an AI-native professional video editor (multitrack timeline, keyframes, masks, grades, shaders, mixer, leading gen models) driven by CLI, MCP (`https://mcp.invideo.io/mcp`), or web connectors. It covers connection (CLI preferred wherever a shell exists; `invideo auth login` browser flow, `INVIDEO_NO_BROWSER=1` for headless), the work loop (understand ask → open/read existing timeline → build via `edit change` → check/look/listen → show person → export), collaboration model (agents register a name, work on branches, main is what the person approved), the "be ambitious" editing doctrine (senior-editor polish: sound design, one unifying grade, match cuts, speed ramps, layered tracks, motion design with one easing language), a routing table of per-job reference playbooks (launch, ads, commercial, product, review-cut, interview, shorts, personal, invitations, intro/logo, text-animation, short-film, explainer, captions, export), and cost rules (editor edits free, generation costs credits — price, say, cap, report).

## When to use / when NOT
Use for ANY video job routed through invideo: make, edit, trim, stitch, caption, grade. It is the mandatory first read for the sibling skills (invideo-media, invideo-generate, invideo-timeline, invideo-pipeline, *-to-invideo bridges). Do NOT use for simple local ffmpeg-style cuts where no timeline collaboration is needed, and do not use before auth is confirmed.

## Inputs, outputs, tools
- Inputs: the person's brief (orientation, length, audience, existing assets/project), project URLs, registered agent name.
- Outputs: timeline edits (ops applied all-or-none), branch revisions, exports (video file or project file), share links.
- Tools: `invideo` CLI (`auth`, `agent register`, `edit show/change/export`, `media`, `library`, `asset`, `gen`), MCP tools (`get_help`, `get_timeline`, `edit_timeline`, `timeline_catalog`, `find_models`, `dry_run`, `report_bug`/`request_feature`), docs at docs.invideo.io (llms.txt index, `.md` page suffix).

## 5 most important rules
1. Read `get_help`/command help first; every command takes a URL and returns next URLs — relay them to the person.
2. Register an agent name and pass it on every call; work on a branch unless asked to edit main; checkpoint before big changes.
3. Check, look AND listen at every changed moment (`references/check-your-video.md`) before showing the person.
4. Generation costs credits: dry-run price it, state the cost, cap with `--max-credits`, report spend.
5. Read the per-type playbook that fits the job BEFORE planning or generating — agents who do "far better work".

## Risks / owner notes
Real credit spend on generation — the cost rule is mandatory. Requires invideo account auth (owner sign-in once). Agents share live projects with the person; careless main-branch edits are visible immediately.

## Category and tags
Category: media. Tags: invideo, video-editing, timeline, mcp, cli, credits, multi-agent.
