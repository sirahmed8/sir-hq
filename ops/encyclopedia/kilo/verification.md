# verification (windsurf/codex skill)

## Summary
verification is a verification-ORCHESTRATOR skill, not a checklist: infer the complete user story being built, then verify every boundary of the flow with real evidence. Step 1 anchors everything — read recent edits/git diff, identify routes/components/API endpoints/data sources, and state the story in one sentence ("user builds X flowing from UI entry → API route → data source → response rendering"). Step 2 builds an evidence baseline across four layers: browser (console, screenshots, network), dev-server terminal output, runtime logs (`vercel logs` if deployed), and environment (.env.local vs `vercel env ls` vs actual runtime). Step 3 walks the data flow boundary by boundary — UI trigger → client request → route handler → external deps (DB/third-party/Vercel services) → response → UI — checking named break patterns: missing await, wrong HTTP method, env var absent at runtime, server/client import mismatch, type mismatch, missing error boundary. Step 4 emits a structured report (story, per-boundary status table with evidence, issues with fixes, verified-working list).

## When to use / when NOT
Use when a dev server started, a feature "almost works", or the user asks to verify a flow end-to-end. Do NOT use for single-layer checks (that's other skills' job), cosmetic/style review, or verifying unrelated features — stay on the inferred story.

## Inputs, outputs, tools
- Inputs: recent code changes, running dev server, deployed logs, env files.
- Outputs: the structured Verification Report with per-boundary ✅/❌ + evidence.
- Tools: browser checks/screenshots, terminal output, `vercel logs`, `.env*` inspection — no dedicated scripts.

## 5 most important rules
1. NEVER skip story inference — every check anchors to the one-sentence user story.
2. Report contract per check: "Checking / Evidence (quote real output) / Next".
3. Stop at the FIRST broken boundary — report it with evidence and a fix; don't continue past the break.
4. Stop when two consecutive layers give no signal — flag the observability gap and recommend logging instead of looping.
5. Never repeat a check more than twice; ignore cosmetic issues unless asked.

## Risks / things needing the owner
Low risk — read-only verification. Main failure mode is shallow checking (declaring success without evidence); the skill's entire design fights that. `vercel logs` needs CLI auth if deployed. No owner actions beyond existing auth.

## Category / tags
ops · verification, e2e, debugging, evidence

## Revisions
Single source read: `C:\Users\a7med\.codeium\windsurf\skills\verification\SKILL.md` (106 lines). Slice lists six tools; windsurf revision read as representative — codex/kilo copies carry the same orchestrator structure.
