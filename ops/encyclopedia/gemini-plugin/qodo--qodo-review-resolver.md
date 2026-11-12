# qodo-review-resolver

- Tool: `gemini-plugin` (plugin: `qodo`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-review-resolver\SKILL.md`
- SKILL.md size: 32776 chars

## What it does

Read or resolve a pull request's Qodo review using Qodo managed tools through MCP or the CLI — fetch structured status, reviewed commit SHA, and findings for ANY PR as JSON, with optional extended details and citation evidence for audits, then optionally resolve open findings and record outcomes, once or until clean. Use this — never `gh`/`curl` scraping of review comments — for "is the review clean on PR #N", "get Qodo's findings for <pr> as JSON", "audit the review evidence", "show finding citations", "what did Qodo flag", "is this review up to date with head", "check before merging", "resolve my PR review", "fix the review findings", or "babysit this PR until it's clean".

## Structure (headings inside SKILL.md)

- Read & Resolve Findings
- Description
- Prerequisites
- Instructions
- Choose the execution path
- Handle a skill update notice
- Execution
- Runtime compatibility gate
- Quick start
- Preflight
- Fetch the review session
- Extended results for audits and investigation
- Read the session state FIRST (before trusting any finding)
- Present the review state
- Triage
- Honor the user's instruction (optional scope)
- Two modes
- Resolve a finding
- Record the outcome
- Example
- Configuration
- Error Handling
- Guardrails
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP tools, MCP write, MCP call, MCP or

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Windows CLI: read [shell guidance](references/windows-shells.md) before the first call; [launcher recovery](references/windows-launcher.md) only if invocation fails. Reuse the resolved invocation.
2. 2. **Resolve the PR.** Use the PR URL the user gives. If they don't name one and you're inside
3. 3. **Bind edits to the checkout.** Report-only reads may target any PR. Before any local fix,
4. - **By action level** — "resolve the action-required findings" → only `action_level == action_required`;
5. 4. Bound it: stop after a few rounds with no progress and hand back to the user rather than

## Files inside the skill

- `agents/openai.yaml`
- `references/skill-updates.md` — "Manual enterprise skill updates"
- `references/windows-launcher.md` — "Windows launcher recovery"
- `references/windows-shells.md` — "Windows shells"
