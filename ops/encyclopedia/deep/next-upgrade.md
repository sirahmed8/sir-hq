# next-upgrade

Tools: codex, cursor, kilo, opencode, windsurf (codex copy used; identical across tools).
Source: C:\Users\a7med\.codex\skills\next-upgrade\SKILL.md

## Summary
A short procedural skill for upgrading a Next.js project to the latest version. It reads package.json for the current version, fetches the official upgrade/codemod docs from nextjs.org, determines the upgrade path (incremental for major jumps), runs `@next/codemod` transforms for automated breaking changes, upgrades next/react/react-dom together, applies manual breaking-change fixes, and verifies with build + dev.

## When to use / not use
Use when a project needs a Next.js version bump, especially across majors (13→14→15→16). Not needed for routine dependency updates or non-Next.js upgrades; it also assumes network access to fetch docs.

## Inputs, outputs, dependencies
Input: a Next.js project with package.json. Output: upgraded dependencies plus codemod-applied source changes. Needs: npm/npx, WebFetch (or equivalent) to read nextjs.org guides, and a working build/test setup. Named codemods: `next-async-request-api`, `next-request-geo-ip`, `next-dynamic-access-named-export` (all v15-era).

## Key rules
1. Detect current version first; never guess the starting point.
2. Upgrade major versions incrementally, one major at a time.
3. Run official codemods before manual edits — they automate the breaking API changes.
4. Upgrade `next`, `react`, `react-dom` (and `@types/react*`) together; peer deps must move in lockstep.
5. Verify with `npm run build` and `npm run dev` before declaring success.

## Risks / owner items
- The skill's codemod list only names v15 transforms; for v16 upgrades the agent must fetch the current guide rather than trusting the examples.
- It does not mention running the project's test suite or checking framework-specific config (e.g., `cacheComponents` changes in v16); a human should review the diff.
- WebFetch dependency means offline environments cannot complete step 2.

## Category and tags
build, web — nextjs, upgrade, migration, codemod, dependencies.

## Revision note
Identical across tools; single ~50-line file, read in full.
