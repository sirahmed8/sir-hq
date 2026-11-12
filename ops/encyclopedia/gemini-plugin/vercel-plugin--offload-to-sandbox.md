# offload-to-sandbox

Tools: gemini-plugin (Vercel plugin). Source: C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\offload-to-sandbox\SKILL.md (284 lines, read in full)

## Summary
Operational playbook for offloading heavy work (full test suites, long Linux builds, parallel agent tasks) to Vercel Sandbox microVMs via the `vercel sandbox` CLI. Covers base-snapshot preparation, one-sandbox-per-task naming/tagging, non-persistent lifetime management, pushing git-tracked source without reinstalling node_modules, remote exec pitfalls, result retrieval, sharding, and a ready-made `sbx` wrapper script.

## When to use / not use
Use for resource-heavy builds, sharded test suites, many parallel tasks, or disk-filling work that should stay off the local machine. Keep editing, git, small focused tests, typecheck/lint, orchestration, and anything needing local credentials or hardware local.

## Inputs, outputs, dependencies
Input: a Vercel account with `vercel` CLI auth (`VERCEL_TOKEN` for CI), a project scope, and a base snapshot ID. Output: remote test/build results copied back as compact files. Needs the `vercel sandbox` CLI; optionally pairs with the `vercel-sandbox` skill for the SDK/untrusted code.

## Key rules
1. Build a base snapshot once (toolchain + built baseline + helper scripts) and start every task from it; snapshots bill until deleted (`--expiration 0` = never expires).
2. Always `--non-persistent`, name per owner+purpose, tag with `owner=`/`app=`, size within plan limits (Hobby: 4 vCPU/45m; Pro: 8 vCPU/3h examples), and `remove` (not `stop`) when done.
3. `vercel sandbox exec` exits 0 even when the remote command fails — end remote commands with `echo "exit=$?"` or use the `sbx` wrapper which propagates status.
4. Push source as a git-files tarball preserving node_modules; never push `.git` or build macOS binaries into the Linux VM; pass remote shell commands as one single-quoted `sh -c` string.
5. Separate pre-existing/baseline failures from new ones by rerunning failures on the untouched tree in the same sandbox; run the full suite only on the final candidate.

## Risks / owner items
- Billed by Active CPU + memory + snapshot storage; Hobby includes only 5h Active CPU/month — heavy offloading needs Pro. Quotas can pause creation mid-run; keep scripts idempotent and write results to disk.
- Non-persistent sandboxes lose the whole filesystem at session timeout — copy results out before it expires.
- Long jobs must run detached (`nohup` + status file) and be polled; the session timeout still applies.
- Exit 137 usually means OOM kill — size up or lower parallelism, don't retry blindly.

## Category and tags
build, cloud, ops — vercel, sandbox, ci-cd, remote-build, cost, mcp-plugin.

## Revision note
Single plugin revision; unusually operational and honest about CLI quirks (verified exit-code bug, billing model).
