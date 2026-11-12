# review-agent

Tools: claude (also codex/cursor/opencode/windsurf; claude chosen). Source: C:\Users\a7med\.claude\skills\review-agent\SKILL.md (57 lines, read in full)

## Summary
A read-only, defect-first code review protocol for delegated reviews: inspect the requested diff (uncommitted changes, base-branch diff, or commit), verify each finding against tests/call sites, and return severity-ranked findings (P0-P3) — or "No findings." Explicitly forbids modifying files, committing, pushing, posting comments, or delegating further.

## When to use / not use
Use when another agent delegates review of a specific change. NOT for authoring code, for open-ended "look at my project" audits, or when write access is expected — this skill is strictly read-only reporting.

## Inputs, outputs, dependencies
Input: a review target (diff range, commit, or uncommitted changes) + applicable AGENTS.md instructions. Output: findings list `[P1] Title — file:line` + short paragraph + overall assessment + test gaps. Needs: git for diff/merge-base resolution, the codebase for context.

## Key rules
1. For base-branch reviews, diff against merge-base of the UPSTREAM comparison ref, not the branch tip — `git merge-base HEAD <ref>` then `git diff <sha>`; try configured upstream before declaring unavailable.
2. A finding must pass ALL gates: introduced by THIS change, affects correctness/security/perf/maintainability meaningfully, discrete+actionable, demonstrable from code, author would fix it.
3. Excluded: speculative concerns, pre-existing problems, intentional behavior changes, style nits.
4. Continue through the WHOLE diff after the first issue — no early exit.
5. "No findings." is a valid complete result — never invent a finding to fill the report; add brief assessment + material test gaps/residual risks after.

## Risks / owner items
- Severity scale (P0 release blocker → P3 low-impact) is the agent's judgment; consumers should sanity-check P0/P1 claims.
- Read-only constraint means it can't verify fixes — a follow-up review of the fix diff is a separate invocation.
- Merge-base resolution assumes standard git topology; unusual branch setups may need manual ref specification.

## Category and tags
build, ai — code-review, read-only, defect-detection, subagent.

## Revision note
Single-file protocol identical across tools; minimal and strict — the anti-noise review contract.
