# offload-to-sandbox

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\offload-to-sandbox\SKILL.md`
- SKILL.md size: 18213 chars

## What it does

Offload resource-heavy builds, test suites.

## Structure (headings inside SKILL.md)

- Offloading work to a Vercel Sandbox
- When to offload, and what to keep local
- Plan limits
- Prepare a base snapshot once
- 1. Create a builder sandbox from the default image (Ubuntu, Node.js, Python, common tools).
- 2. Install the pinned toolchain and build the baseline tree once.
- 3. Snapshot it (this stops the sandbox). The ID is printed on stderr, not stdout.
- 4. The builder is no longer needed. Removing it keeps the snapshot.
- Create one sandbox per task
- Lifetime and cleanup
- Move code in without reinstalling dependencies
- Run commands
- Get results back
- Shard and parallelize
- Separate pre-existing failures from new ones
- Authentication and scope
- Wrap it in one small script
- sbx: offload work to Vercel Sandboxes through `vercel sandbox`.
- sbx create <name>                         new task sandbox from the base snapshot
- sbx push <name> <local-dir> <remote-dir>  sync git-tracked and untracked files, keep node_modules
- sbx exec <name> <script>                  run a shell script remotely, exit with its status
- sbx get <name> <remote-file> <local-file>
- sbx put <name> <local-file> <remote-file>
- sbx rm <name>...                          permanently remove sandboxes
- sbx clean                                 remove every sandbox tagged with your owner tag
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Anything needing local credentials or hardware the sandbox doesn't have.
- - **`vercel sandbox remove <name>` when a task is done.** `vercel sandbox stop` only ends the current session: the sandbox keeps its name, and a persistent sandbox keeps billing for its snapshot. Vercel removes sandboxes that can't resume after 14 days of inactivity, so a stopped non-persistent sand
- - Removing a sandbox does not delete snapshots, so the base snapshot survives task cleanup. `--delete-orphan-snapshots` on `remove` also deletes the sandbox's own snapshots that no other sandbox uses. Don't pass it when removing the builder that made your base snapshot.
- - A tracked file you deleted but didn't stage makes `tar` fail. Stage the deletion (`git rm`) first.

## Key rules (verbatim lines from SKILL.md)

1. - **Name by owner and purpose** (`exp-parser`, `exp-parser-2`) so parallel agents never collide. Names are unique per project and stay taken until the sandbox is removed. Never use another agent's sandbox.
2. - **`vercel sandbox remove <name>` when a task is done.** `vercel sandbox stop` only ends the current session: the sandbox keeps its name, and a persistent sandbox keeps billing for its snapshot. Vercel removes sandboxes that can't resume after 14 days of inactivity, so a stopped non-persistent sand
3. - Removing a sandbox does not delete snapshots, so the base snapshot survives task cleanup. `--delete-orphan-snapshots` on `remove` also deletes the sandbox's own snapshots that no other sandbox uses. Don't pass it when removing the builder that made your base snapshot.
4. - Push after every change; it takes seconds. Then run an idempotent prepare step that installs or rebuilds only what changed (for example, install dependencies only when the lockfile changed).
5. - Build platform-specific artifacts inside the sandbox. Don't copy macOS binaries into a Linux VM.

## Files inside the skill

- (SKILL.md only)
