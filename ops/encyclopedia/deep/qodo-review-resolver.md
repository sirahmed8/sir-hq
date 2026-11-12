# qodo-review-resolver

Tools: gemini-plugin (qodo plugin). Source: C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-review-resolver\SKILL.md (460 lines) + references/

## Summary
Reads and resolves Qodo review findings on ANY pull request via managed tools (`get-pr-review-findings`, `pr-review-dismiss`, `pr-review-mark-implemented` on MCP; `qodo read pr-review-session findings` + `pr-review-session` writes on CLI) — never scraping PR comments with gh/curl. Reports review status/findings as JSON, optionally babysits a PR until clean, applies authorized code fixes, and records dispositions that clear Qodo's merge-policy block.

## When to use / not use
Use for "is the review clean on PR #N", "what did Qodo flag", merge-gating on review state, resolving open findings, or watch-until-clean loops. NOT for pre-PR local review (that's `qodo-review`) or non-review PR chores. Never for gh/curl comment scraping.

## Inputs, outputs, dependencies
Input: a PR URL (never guessed — confirmed with user if inferred), current head SHA, optional `extended` flag for citation audits. Output: review session state (`status`, `commit_sha`, `findings[]` with id/title/category/action_level/location/evidence), then code fixes + recorded dispositions. Needs: QAR MCP or authenticated `qodo` CLI >=2.0.0, checkout bound to the PR's exact repo (`origin` must match `owner/repo` case-insensitively).

## Key rules
1. Read session state FIRST: act only on a `completed` review whose `commit_sha` equals the PR head — running/stale/failed/aborted/superseded reviews can't authorize anything; `null` review_session = no review yet.
2. Extended mode adds code snippets, dismissal reasons, review_runs, fuller citations — for audits only; `qar_operation_result_truncated:true` = incomplete read, never a clean verdict.
3. Triage by `attribution_status`: OPEN = pending/partial_implementation/not_implemented/focus_areas_edited; CLOSED = implemented/full_implementation/dismissed/detected_after_merge/outdated; unfamiliar values get reported, not silently excluded.
4. Fix authority ≠ status-write authority: code fixes need fix authorization; dismiss/mark-implemented writes need SEPARATE explicit user authorization with stable idempotency keys; only record outcomes actually settled.
5. Freshness loop: after fixes, Qodo re-reviews the new commit; clean verdict requires completed review at CURRENT head — tests passing or a status write succeeding doesn't establish that.

## Risks / owner items
- Applying findings from one repo to another worktree is explicitly forbidden — origin/PR repo mismatch = stop and ask.
- Never silently reassign a conflicting PR binding; investigate instead.
- Dismissals are persistent review-DB state — wrong dismissals suppress real findings on future reviews; reasons (`intentional` etc.) must be truthful.
- Watch loops must respect retry delays and stop if the review makes no progress.

## Category and tags
ai, build, security — qodo, code-review, pr, findings, merge-gate, automation.

## Revision note
Single plugin revision (v1.4.10); the remote-PR counterpart to qodo-review.
