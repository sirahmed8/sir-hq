# figma-generative-plugins

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-generative-plugins\SKILL.md`
- SKILL.md size: 4711 chars

## What it does

Create, author, and extend reusable.

## Structure (headings inside SKILL.md)

- Create and update generative Figma plugins
- Preflight
- Create workflow
- Update workflow
- Authoring rules
- Completion
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Never embed API keys, OAuth tokens, signed URLs, or other secrets. Plugin source is readable by people who can access it. For authenticated integrations, stop and offer a static dataset, a public no-auth endpoint, or a different architecture.
- - Avoid destructive canvas changes unless they are the explicit purpose of the plugin and the UI makes that clear.

## Key rules (verbatim lines from SKILL.md)

1. - Every plugin must provide functional UI for its core workflow. A plugin with no configurable inputs still needs a clear primary action and useful status or validation feedback.
2. - Never embed API keys, OAuth tokens, signed URLs, or other secrets. Plugin source is readable by people who can access it. For authenticated integrations, stop and offer a static dataset, a public no-auth endpoint, or a different architecture.
3. 1. Resolve the requested workflow and its useful controls. Ask a concise question only if required inputs or behavior are genuinely ambiguous.
4. 2. Read every source URI returned by the get tool before editing. Treat those files as the current source of truth.
5. - Before writing replacement files, read [Plugin source authoring](references/authoring.md). It covers the file replacement contract, UI/message lifecycle, PropsKit controls, dynamic-page compatibility, fonts, relaunch behavior, bounded work, geometry, and Plugin API gotchas.

## Files inside the skill

- `references/authoring.md` — "Plugin source authoring"
