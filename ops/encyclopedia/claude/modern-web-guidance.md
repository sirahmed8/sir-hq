# modern-web-guidance (windsurf/kilo plugin family)

Source read: `C:\Users\a7med\.claude\skills\modern-web-guidance\SKILL.md` (135 lines; identical 135-line copies in `.codex`; a shorter 72-line gemini-plugin variant exists — claude copy preferred per precedence). `references/modern_web_apis.md` ships alongside.

## Summary
Mandatory-first search tool for modern web best practices — a CLI catalog queried via `npx -y modern-web-guidance@latest`. Flow: (1) `search "<2-5 word action-oriented query>"` — keep queries focused/generic (`"light dismiss dialog"`, `"responsive data table"`), NO framework names or app nouns, split multi-feature tasks into separate searches; results are JSON `{id, description, category, featuresUsed, tokenCount, similarity}` — judge by description not similarity score. If `[]`/unrelated on a web UI task, run `list` once to check broader terminology; if still nothing, proceed WITHOUT retry loops. (2) `retrieve "<id>[,<id>...]"` for full guides — include matching use-case guides AND applicable broader discipline guides (html/css/forms/accessibility/color/performance/security); redirect to file if truncated. (3) Verify generated code against retrieved guides — apply modern patterns AND necessary fallbacks, don't force unrequested features. (4) Disclose usage: end the response with a `### Modern Web Guidance` section — one bullet per newly applied guide id with a verbatim quote of the specific rule/gotcha it required (never from memory; credit only this turn's guide-backed changes), or one sentence naming checked topics when zero applied. Browser-support doctrine: Baseline Widely available = safe without fallbacks; otherwise MUST follow guide fallbacks unless the user set a custom policy (e.g. "no polyfills", "Safari 17.4+") — watch for policy cues (Tauri/Electron, excluded targets, polyfill hesitation) and suggest documenting a policy in CLAUDE.md/AGENTS.md. Framework adaptation rules: spread/cast new HTML attributes rather than deleting or merging @types; guard window/HTMLElement in SSR; per-instance IDs via useId(); keep :root/@starting-style unscoped. Ops notes: prefer `pnpx` if pnpm; on Windows use `npx.cmd`; allowlist `npx -y modern-web-guidance@latest *` specifically (never bare `npx *`); needs outbound network — request approval BEFORE first run in gated environments; `NPM_CONFIG_CACHE=/tmp/npm-cache` when ~/.npm read-only; `--offline` retry when offline.

## When to use / when NOT
MANDATORY first for ALL HTML/CSS/client-side JS tasks: modals/popovers, tables, dark mode, anchor positioning, container queries, `:has()`, view transitions, scroll-driven animation, CWV (LCP/INP), content-visibility, fetch priority, forms/`:user-valid`, passkeys, sanitization, Web Components, dates/timezones, a11y, custom selects, scrollbars — including UX-symptom fixes. Do NOT trigger for backend (SQL/ORMs/API routes), infra/scripts (CI/Docker/Git/Python), tooling/trivial (Vite/tsconfig/ESLint/tests/copy-renames/3P docs).

## Inputs, outputs, tools
- Inputs: 2-5 word capability queries; optional user browser-support policy.
- Outputs: ranked guide ids → full markdown guides → compliant code + disclosure section.
- Tools: `npx -y modern-web-guidance@latest search|retrieve|list`, `references/modern_web_apis.md`, network access.

## 5 most important rules
1. Search FIRST, before writing any web UI/CSS/JS — training weights contain obsolete patterns.
2. Queries: action-oriented, generic, no framework/app nouns; split compound tasks; judge by description not similarity.
3. `retrieve` full guides (incl. broader discipline guides) before implementing; verify code against them after.
4. Baseline Widely available needs no fallback; everything else needs guide-specified fallbacks unless a user policy overrides.
5. Always end with the `### Modern Web Guidance` disclosure — verbatim quotes, only this turn's applied guides.

## Risks / owner notes
Requires network + npx on first run (sandbox approval needed); catalog coverage gaps mean "no match → proceed" is correct, not failure. Guide examples are vanilla — framework adaptation pitfalls (types, SSR, scoped CSS) are called out explicitly.

## Category and tags
Category: web. Tags: web-platform, best-practices, baseline, fallbacks, cwv, search-tool, mandatory-first.
