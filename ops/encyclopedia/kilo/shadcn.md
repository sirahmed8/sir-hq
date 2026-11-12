# shadcn

Tools: claude (also codex/cursor/opencode/windsurf; claude chosen). Source: C:\Users\a7med\.claude\skills\shadcn\SKILL.md (554 lines, read in full)

## Summary
Complete shadcn/ui operating manual: CLI commands (init/add/search/view/docs/build/migrate), the "copy source into your repo" model (Radix UI or Base UI primitives + Tailwind), components.json configuration, CSS-variable theming with oklch tokens, dark mode, custom registries, Vercel-stack design direction, composition recipes, and hard-won gotchas (Geist font circular var, Avatar sizing, unified radix-ui package).

## When to use / not use
Use when installing shadcn/ui components via CLI or composing Radix/Base UI primitives with Tailwind theming in any supported framework (Next.js, Vite, React Router, Astro, Laravel/Inertia, TanStack Start). NOT for non-React stacks or projects wanting a dependency-installed component library — shadcn copies source, you own it.

## Inputs, outputs, dependencies
Input: a project to init or components to add. Output: components.json, ui/ component source files, themed globals.css, cn() util. Needs: Node/npx, Tailwind CSS, chosen base (radix default — REQUIRED for AI Elements compatibility), optional registry URLs/tokens.

## Key rules
1. ALWAYS `init -d` (defaults) for non-interactive use — `-y` alone still prompts for library selection; `--base radix` mandatory if AI Elements may be used (Base UI breaks its types).
2. Components are SOURCE in your repo — customize by editing files/cva variants directly; sizing is Tailwind classes not variant props (Avatar has no size prop).
3. Theme via CSS variables in @theme inline with oklch values; radius tokens use multiplicative calc (--radius-lg = var(--radius), xs = *0.5) in CLI v4.
4. Post-init font fix is mandatory: literal font names in @theme inline ("Geist", "Geist Fallback"...) because @theme inline resolves at parse time and can't see runtime-injected vars; font variable classNames go on <html> not <body>.
5. Design direction: new-york style, dark mode default for dashboards/AI/internal tools, Geist Sans/Mono, zinc/neutral/slate base + one accent, token surfaces only (bg-background/bg-card), one density per page, Lucide h-4/h-5 icons; AlertDialog for destructive confirms, never Dialog; no nested cards/gradients/glassmorphism.

## Risks / owner items
- CLI v4 removed flags: --style, --base-color, --src-dir, --no-base-style, --css-variables error out; registry:build/mcp deprecated (use registry:base/font).
- Unified `radix-ui` package (Feb 2026) replaced individual @radix-ui/react-* — migrate via `npx shadcn@latest migrate radix` then remove old deps.
- Presets (--preset) reconfigure EVERYTHING including components — switching presets is destructive to customizations.
- Custom registries can carry auth headers via ${REGISTRY_TOKEN} env — secret hygiene on private registries.

## Category and tags
web, design, build — shadcn, radix, tailwind, ui-components, design-system, react.

## Revision note
Single claude revision but current through Feb 2026 (unified radix-ui, Base UI, presets, RTL migrate).
