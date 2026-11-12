# shadcn

- Tool: `claude`
- Category: design
- Source: `C:\Users\a7med\.claude\skills\shadcn\SKILL.md`
- SKILL.md size: 18622 chars

## What it does

Use when installing shadcn/ui components through the CLI or composing Radix UI primitives with Tailwind CSS theming.

## When to use (from skill text)

- ### Initialize (non-interactive — ALWAYS use this)
- # Non-interactive init with defaults — USE THIS

## Structure (headings inside SKILL.md)

- shadcn/ui
- Key Concept
- CLI Commands
- Initialize (non-interactive — ALWAYS use this)
- Non-interactive init with defaults — USE THIS
- Non-interactive with a preset (recommended for consistent design systems)
- Non-interactive with explicit base library choice
- Scaffold a full project template (CLI v4)
- Add Components
- Add specific components
- Add all available components
- Add from a custom registry
- Add from AI Elements registry
- Search & List
- Build (Custom Registry)
- View, Info & Docs (CLI v4)
- View a registry item's source before installing
- Show project diagnostics — config, installed components, dependencies
- Get docs, code, and examples for any component (agent-friendly output)
- Migrate
- Migrate components outside the default ui directory
- shadcn/skills (CLI v4)
- Unified Radix UI Package (February 2026)
- Base UI Support (January 2026)
- Configuration (components.json)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Prefer style: `new-york` for product, dashboard, AI, and admin surfaces.
- - Default to dark mode for dashboards, AI apps, internal tools, settings, and developer-facing products. Use light mode only when the product is clearly content-first or editorial.
- - Build core surfaces from tokens: `bg-background`, `bg-card`, `text-foreground`, `text-muted-foreground`, `border-border`, `ring-ring`. Avoid ad-hoc hex values.
- - Entity detail: header + status `Badge` + main `Card` + side `Card` + `AlertDialog` for destructive

## Key rules (verbatim lines from SKILL.md)

1. - `-d, --defaults` — **Use default configuration, skip all interactive prompts** (REQUIRED for CI/agent use)
2. 2. Installs required dependencies (Radix UI, tailwind-merge, class-variance-authority)
3. - Build core surfaces from tokens: `bg-background`, `bg-card`, `text-foreground`, `text-muted-foreground`, `border-border`, `ring-ring`. Avoid ad-hoc hex values.
4. - Repeated `div rounded-xl border p-6` instead of `Tabs` / `Table` / `Sheet` / `Dialog`
5. - Using `Dialog` for destructive confirmation instead of `AlertDialog`

## Files inside the skill

- (SKILL.md only)
