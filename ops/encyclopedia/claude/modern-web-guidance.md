# modern-web-guidance

- Tool: `claude`
- Category: security
- Source: `C:\Users\a7med\.claude\skills\modern-web-guidance\SKILL.md`
- SKILL.md size: 9812 chars

## What it does

| Search tool for modern web development best practices. MANDATORY: Execute FIRST for all HTML/CSS and clientside JS tasks. Do NOT skip — web APIs evolve rapidly and training weights contain obsolete patterns. Trigger immediately for: - UI/Layout: Modals/dialogs/popovers, tables, dark mode, anchor positioning, container queries, `:has()`, etc. - Scroll/Motion: View Transitions, Scroll-driven animations, parallax/reveals, etc. - Performance: CWV (LCP, INP), content-visibility, Fetch Priority, image optimization, etc. - System/APIs: Security, passkeys, HTML sanitization, Web Components, dates/timezones, Built-in AI, WebAssembly, etc. - Frameworks: Standard HTML/CSS/DOM in React, Vue, Angular, etc. - General Frontend: Forms, validation (`:user-valid`), autofill, accessibility, custom selects, scrollbars, etc. DO NOT trigger for: - Backend: SQL, ORMs, API routes, etc. - Infra/Scripts: CI/CD, Docker, Actions, Python/Go, Git, etc. - Tooling/Trivial: Vite, tsconfig, ESLint, tests, copy/renames, 3P docs, etc.

## When to use (from skill text)

- Must use this skill:

## Structure (headings inside SKILL.md)

- Modern Web Guidance
- When to use
- Usage Instructions
- Step 1. Search Use Cases
- Step 2. Retrieve Best Practices
- Step 3. Verify Guidance Compliance
- Step 4. Disclose Skill Usage
- Using npx / pnpx
- Guidelines
- Interpreting Browser Support & Fallbacks
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Keep queries focused and generic**: Describe the user-visible capability (`<verb> + <UI/platform object>`, optionally paired with the target HTML/CSS/JS feature name if known). Omit framework/library names (`React`, `Vue`, `Tailwind`, etc.) and app/domain nouns (product, route, or component/file
- - When requesting tool permissions, allowlist `npx -y modern-web-guidance@latest *` specifically (or `pnpx modern-web-guidance@latest *`), never bare `npx *` or `pnpx *`.
- - Fetching and running `modern-web-guidance` requires outbound network access. If running in a sandboxed, permission-gated, or approval-based environment (e.g., Codex, Claude Code), **proactively request approval/allowlisting for the command with network access BEFORE executing it the first time**, 
- - These guides use vanilla HTML/CSS/JS; adapt them to your framework without dropping the modern feature:

## Key rules (verbatim lines from SKILL.md)

1. - Before creating or updating a component, to check if a standardized modern web pattern already exists.
2. - To avoid implementing ad-hoc solutions or loading large dependencies unnecessarily.
3. - **When retrieved guides shaped your code**: Write **one** bullet (1–2 sentences, ≤75 words) per newly applied `<id>` in first-person voice explaining the non-obvious implementation choices, CSS/API overrides, or fallbacks `<id>` required and the pitfall it prevented, anchored by a short verbatim q
4. - **Never** guess `<id>`s or quotes from memory after context compaction (re-run `search`/`retrieve` if needed), and credit **only** guide-backed changes from the current turn.
5. - When requesting tool permissions, allowlist `npx -y modern-web-guidance@latest *` specifically (or `pnpx modern-web-guidance@latest *`), never bare `npx *` or `pnpx *`.

## Files inside the skill

- `references/modern_web_apis.md` — "Modern Web Platform APIs & Native Standards"
