# microfrontends

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\microfrontends\SKILL.md`
- SKILL.md size: 3573 chars

## What it does

Architect, configure, and route multi.

## Structure (headings inside SKILL.md)

- Vercel Microfrontends
- Finding Detailed Information
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `remove-from-group` — remove the current project from its group; without `--yes` it needs an interactive terminal (option: `--yes` skips the project-link prompt and removal confirmations, including the warning for projects still referenced in `microfrontends.json`)
- - `delete-group` — delete a group and all its settings, irreversible; without `--yes` it needs an interactive terminal (options: `--group` to pre-select group, `--yes` skips the deletion confirmation; pass both to delete without prompts)

## Key rules (verbatim lines from SKILL.md)

1. - `add-to-group` — add the current project to an existing group; always asks for confirmation (there is no `--yes`), so it needs an interactive terminal, and it refuses to run with `--non-interactive` when adding would go past the free project limit (options: `--group` and `--default-route` pre-fill

## Files inside the skill

- `references/configuration.md` — "Configuration Reference"
- `references/local-development.md` — "Local Development Reference"
- `references/managing-microfrontends.md` — "Managing Microfrontends Reference"
- `references/path-routing.md` — "Path Routing Reference"
- `references/security.md` — "Managing Microfrontends Security"
- `references/troubleshooting.md` — "Testing & Troubleshooting Reference"
