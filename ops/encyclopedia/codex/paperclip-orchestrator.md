# paperclip-orchestrator

Tools: claude, codex, cursor, gemini-plugin, kilo, opencode, windsurf (kilo copy used; identical across tools).
Source: C:\Users\a7med\.config\kilo\skills\paperclip-orchestrator\SKILL.md (50 lines, read in full)

## Summary
A meta-harness pattern for running multiple AI agents as a virtual company: a CEO/orchestrator delegates to Directors (Engineering, Design, QA/Security) who delegate to Leads and Workers, with structured task envelopes (scope, inputs, outputs, token/time budgets), explicit status transitions, cross-harness interoperability (Antigravity, Claude Code, Codex/OpenCode/Kilo), and human approval gates for destructive actions.

## When to use / not use
Use when coordinating several agents across different harnesses on one project with role separation and governance. Not for single-agent tasks or when agents can't actually communicate — the skill describes the org pattern, not a runnable bus (the real bus lives in _SIR ops tooling).

## Inputs, outputs, dependencies
Input: a task hierarchy decomposed into scoped assignments. Output: delegated work flowing Assigned→Running→Review→Completed/Blocked with quality gates before merge. Needs: multiple agent runtimes, a task/status channel, and a human or CEO-level approval path.

## Key rules
1. Every subordinate task carries explicit scope, inputs, expected outputs, and token/time budgets — no open-ended delegation.
2. Status machine is explicit: Assigned → Running → Review → Completed/Blocked.
3. Match harness to work: Antigravity for multi-file orchestration/visual validation, Claude Code for terminal/rapid edits, Codex/OpenCode/Kilo for isolated background tasks.
4. Destructive actions (migrations, production deploys, secret changes) require CEO/human sign-off.
5. Quality gates: lint + unit tests + security scan before merge to main.

## Risks / owner items
- The org chart is aspirational without an enforcement mechanism — status transitions and budgets need real tooling to mean anything.
- Approval gates only work if the orchestrator actually blocks; a worker with direct prod access bypasses the model.
- Token budgets per agent are stated but the skill gives no mechanism to enforce them.

## Category and tags
ai, ops, build — multi-agent, orchestration, delegation, governance, virtual-company.

## Revision note
Identical across tools; conceptual pattern (org chart + protocol), not an implementation.
