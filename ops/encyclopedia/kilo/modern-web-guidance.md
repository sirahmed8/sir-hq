# modern-web-guidance (canonical plugin + legacy family)

Source read: Canonical 2026-11-13 revision from `modern-web-guidance-plugin` (`91` lines; synced to `ops/encyclopedia/canonical/`, `gemini-config`, `opencode`, and `kilo`). Note: `claude`, `codex`, `cursor`, and `windsurf` still retain the older 2026-10-21 `135`-line copy with `references/modern_web_apis.md`.

## Summary
Mandatory-first search tool for modern web best practices, queried via `npx -y modern-web-guidance@latest`. Primary workflow: (1) `search "<2-5 word action-oriented query>"` using concrete HTML/CSS/UI nouns (no framework names or app nouns); judge results by `description`, rephrase once if empty/weak, or run `list` once for broad UI audits; proceed without retrying if a topic is uncovered. (2) `retrieve "<id>[,<id>...]"` for full guides (read saved output files completely if >9.5 KB). (3) Adapt vanilla HTML/CSS/JS examples safely to frameworks (spread/cast new HTML attributes, guard `window`/`HTMLElement` in SSR, `useId()` for instance IDs/anchors, keep `:root`/`@starting-style` unscoped). (4) Disclose usage at the end under `### Modern Web Guidance` with verbatim guide-rule quotes or one sentence listing checked topics when none applied. Canonical 2026-11-13 revision adds an alternative 4-step codebase modernization flow (`npx -y modern-web-guidance@latest legacy-scan <path> --json`, ~20% catalog coverage) ONLY for broad open-ended modernization/legacy scans, never for targeted feature work. Browser-support doctrine: Baseline Widely available features need no fallback; non-Baseline features require guide fallbacks unless a project browser-support policy overrides them.

## When to use / when NOT
MANDATORY first for HTML/CSS and client-side JS tasks: modals/dialogs/popovers, tables, dark mode, anchor positioning, container queries, view transitions, scroll-driven animations, forms/validation/autofill, accessibility, custom selects, scrollbars, CWV (LCP, INP, CLS), content-visibility, fetch priority, image optimization, security, passkeys, HTML sanitization, web components, dates/timezones, built-in AI, and WebAssembly. Do NOT trigger for backend (SQL/ORMs/API routes), infra/scripts (CI/Docker/Actions/Python/Go/Git), or tooling/trivial tasks (Vite/tsconfig/ESLint/tests/copy-renames/3P docs).

## Inputs, outputs, tools
- Inputs: 2-5 word UI capability queries, codebase path for `legacy-scan`, optional custom browser-support policy.
- Outputs: guide search/retrieve output, compliant web implementation, `### Modern Web Guidance` disclosure.
- Tools: `npx -y modern-web-guidance@latest search|retrieve|list|legacy-scan` (`pnpx` if pnpm; `npx.cmd` on Windows; `--offline` when offline; allowlist `npx -y modern-web-guidance@latest *`).

## 5 most important rules
1. Search FIRST before writing ad-hoc HTML/CSS/client JS or adding dependencies; do not run `legacy-scan` during normal feature/fix/audit tasks.
2. Translate implied domain actions into concrete HTML/CSS/UI primitives when searching, and judge results by `description`, not similarity score.
3. Read retrieved guides in full (even when redirected >9.5 KB) and follow Baseline/fallback rules unless a documented browser policy overrides.
4. Adapt vanilla patterns cleanly to React/Vue/SSR without breaking types, IDs, or top-level `@starting-style`/`:root` rules.
5. End with the `### Modern Web Guidance` disclosure quoting only guides verified and applied in the current turn.

## Risks / owner notes
Requires outbound network on first `npx` run (request allowlist/network approval upfront in gated sandboxes; use `NPM_CONFIG_CACHE=/tmp/npm-cache` if `~/.npm` is read-only). Older 2026-10-21 copies in `claude`/`codex`/`cursor`/`windsurf` still ship `references/modern_web_apis.md` without the `legacy-scan` section.

## Category and tags
Category: build. Tags: web-platform, best-practices, baseline, fallbacks, cwv, legacy-scan, mandatory-first.
