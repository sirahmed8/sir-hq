# modern-web-guidance

- Tool: `gemini-plugin` (plugin: `modern-web-guidance-plugin`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\modern-web-guidance-plugin\skills\modern-web-guidance\SKILL.md`
- SKILL.md size: 7883 chars

## What it does

| Search tool for modern web development best practices. MANDATORY: Execute FIRST for all HTML/CSS and clientside JS tasks. Do NOT skip — web APIs evolve rapidly and training weights contain obsolete patterns. Trigger immediately for: modals/dialogs/popovers, tables, dark mode, anchor positioning, container queries, view transitions, scroll-driven animations, parallax/reveals, forms, validation, autofill, accessibility, custom selects, scrollbars, CWV (LCP, INP, CLS), content-visibility, fetch priority, image optimization, security, passkeys, HTML sanitization, web components, dates/timezones, built-in AI, WebAssembly, standard HTML/CSS/DOM in frameworks, etc. DO NOT trigger for: backend (SQL, ORMs, API routes), infra/scripts (CI/CD, Docker, Actions, Python/Go, Git), or tooling/trivial (Vite, tsconfig, ESLint, tests, copy/renames, 3P docs), etc.

## Structure (headings inside SKILL.md)

- Modern Web Guidance
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
- - **Runner & Permissions**: Prefer `pnpx` over `npx` if `pnpm` is available (`pnpx` does not use `-y`); on Windows, use `npx.cmd`. When requesting tool permissions, allowlist `npx -y modern-web-guidance@latest *` (or `pnpx modern-web-guidance@latest *`) specifically, never bare `npx *` or `pnpx *`.
- - These guides use vanilla HTML/CSS/JS; adapt them to your framework without dropping the modern feature:

## Key rules (verbatim lines from SKILL.md)

1. - **When retrieved guides shaped your code**: Write **one** bullet (1–2 sentences, ≤75 words) per newly applied `<id>` in first-person voice explaining the non-obvious implementation choices, CSS/API overrides, or fallbacks `<id>` required and the pitfall it prevented, anchored by a short verbatim q
2. - **Never** guess `<id>`s or quotes from memory after context compaction (re-run `search`/`retrieve` if needed), and credit **only** guide-backed changes from the current turn.
3. - **Runner & Permissions**: Prefer `pnpx` over `npx` if `pnpm` is available (`pnpx` does not use `-y`); on Windows, use `npx.cmd`. When requesting tool permissions, allowlist `npx -y modern-web-guidance@latest *` (or `pnpx modern-web-guidance@latest *`) specifically, never bare `npx *` or `pnpx *`.
4. - **Sandboxes & Network**: Fetching `modern-web-guidance` requires outbound network access. In sandboxed or approval-gated environments (e.g., Codex, Claude Code), **proactively request approval/allowlisting with network access BEFORE the first execution** to avoid timeouts, and set `NPM_CONFIG_CACH
5. - Always search **first** to find the most relevant guides. Do not hallucinate guides or ignore them; they represent the preferred local standard for the user's project.

## Files inside the skill

- (SKILL.md only)
