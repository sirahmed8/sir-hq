# github-gem-seeker

Sources read: `C:\Users\a7med\.claude\skills\github-gem-seeker\SKILL.md` (claude revision chosen; codex/cursor/kilo/opencode/windsurf hold byte-identical copies per digest).

## Summary
An open-source intelligence workflow for surfacing high-potential GitHub repositories before they go mainstream. It defines discovery heuristics (star velocity over raw star count, `created:>`/`stars:>`/`topic:`/`language:` API query recipes, commit frequency and maintainer response time under 48h, releases within 14 days) and a 100-point evaluation scorecard across five pillars: architectural novelty (25), documentation and ergonomics (25), code craftsmanship (20), community health (15), licensing and extensibility (15). When a gem is found it prescribes analysing the core mechanism, synthesising a clean-room equivalent inside the ecosystem instead of vendoring dependencies, and drafting an executive briefing.

## When to use / when NOT
Use when hunting for emerging dev tools, evaluating a repo the user found, or building a shortlist of libraries to adopt. Do NOT use as a generic GitHub search (plain `gh search` suffices for lookups) and do not use it to justify adding heavy dependencies — the skill explicitly prefers clean-room reimplementation.

## Inputs, outputs, tools
- Inputs: a topic, language, or timeframe to hunt in; optionally a specific repo URL to score.
- Outputs: scored evaluation against the 5-pillar table plus an executive briefing (innovation, benchmarks, integration points).
- Tools: GitHub search/API (web or `gh`), repo inspection of `/src` or `/core`.

## 5 most important rules
1. Judge star velocity (stars/day in first ~30 days), not absolute star count.
2. Score every candidate on all five pillars; novelty and docs carry half the weight.
3. Check maintainer responsiveness (median first-PR-response <= 48h) and release recency (tag within 14 days).
4. Prefer permissive licenses (MIT, Apache 2.0) and a clean CLI/API surface.
5. On adoption, analyse the mechanism and reimplement natively rather than importing hundreds of MB of unvetted dependencies.

## Risks / owner notes
Low risk; read-only research. The scorecard thresholds (50-200 stars/day, 48h response) are heuristics, not guarantees — treat scores as triage, not verdicts.

## Category and tags
Category: research. Tags: github, open-source, evaluation, discovery, scorecard.
