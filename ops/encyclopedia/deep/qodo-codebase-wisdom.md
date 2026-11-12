# qodo-codebase-wisdom

Tools: gemini-plugin (qodo plugin). Source: C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-codebase-wisdom\SKILL.md (241 lines) + references/{windows-shells,windows-launcher,skill-updates}.md

## Summary
Read-only codebase intelligence through Qodo's managed tools (MCP or `qodo read` CLI): search repos, grep/read/blame files, list commits/PRs/issues, find similar past PRs, and map cross-repo coupling — reaching repos not checked out locally and spanning repo boundaries. Delivers cited findings (repo, path:line, PR, SHA) to answer "how does X work", plan changes, debug regressions, or scope fixes.

## When to use / not use
Use when context is missing about unfamiliar code, prior solutions, historical rationale, or inter-repo relationships — especially for repos not on disk or multi-repo work. Local tools still own exact branch/worktree state, uncommitted changes, edits, and tests; this skill only reads remote/indexed knowledge.

## Inputs, outputs, dependencies
Input: a concrete question (where defined, who changed, what would break, how was it solved before). Output: cited findings in natural prose — answer → Qodo-retrieved context → practical implication. Needs: QAR MCP read tools (litegit-search-repos, litegit-grep, litegit-read-file, pull-request-similar, cross-repo-relations) or authenticated `qodo` CLI >=2.0.0; `--repo owner/repo` explicit on MCP (no origin autodetect).

## Key rules
1. Orient → locate → read: cheap discovery (search-repos, stats, relations) before heavy pulls (read-file with line ranges, PR details/patch); never guess slugs — resolve via search-repos first.
2. Three tool groups: `codebase` (current state), `pull-request` (history/prior art), `cross-repo` (coupling/impact).
3. Read-only enforcement: the write tools (approve, post-comment, set-labels, etc.) post to the forge — never call them while investigating; CLI uses fail-closed `qodo read` gateway.
4. Cite everything locatable; say plainly when a fact has no source; distinguish local worktree truth from remote fetched revisions; merged-PRs-only and pending/not_found coupling edges are freshness caveats.
5. `MT-TOOL-LOOP` means stop and change approach; `truncated:true` means narrow and retry once before concluding "not found".

## Risks / owner items
- Coverage limits: pull-request = merged only; cross-repo edges may be pending analysis or absent — missing edges are NOT proof of isolation.
- Same runtime-compatibility gate as the family (CLI >=2.0.0, one approved upgrade route, never print QODO_UPDATE_BASE_URL).
- Different MCP/CLI accounts or tenants are not interchangeable — no silent path switching after auth denial.

## Category and tags
ai, research, build — qodo, codebase-search, code-intelligence, cross-repo, mcp.

## Revision note
Single plugin revision (v1.1.8); the read-side companion to qodo-review.
