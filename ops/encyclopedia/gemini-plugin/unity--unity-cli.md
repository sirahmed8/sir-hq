# unity-cli

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\unity-cli\SKILL.md`
- SKILL.md size: 69346 chars

## What it does

Controls the Unity Editor and projects from the command line, driving a running Editor to edit scenes and assets or run C#. Use when asked to install or manage Editors, licenses, or projects, set up version control, build, test, or run any unity command.

## When to use (from skill text)

- (`pipeline cloud-build builds start`, `pipeline automation pipelines trigger`) would start it
- | `pipeline cloud-build` (targets incl. groups, create, update, auditlog / builds incl. steps, failures, artifacts, log, download, start, cancel / credentials upload / connections / scm check-url / org free-tier / project / tooling), `pipeline automation` (apps / pipelines incl. trigger / jobs incl.
- cancel builds, download artifacts, trigger pipelines, and follow or act on jobs;

## Structure (headings inside SKILL.md)

- Unity CLI
- Find a command: search, don't grep help
- Drive a running Unity Editor (if one is open)
- Run arbitrary C# — e.g. add a GameObject named "Joe" — when the Editor exposes script eval:
- More than one Editor open? Pass `--project-path`
- Install the CLI (if not already installed)
- Global flags
- Environment variables
- Getting help
- Exit codes
- Commands
- Common workflows
- Inspect and run cloud builds and Pipeline Automation jobs
- Edit a scene, GameObject, or asset — `unity status` first
- then drive it with the commands it lists — for example, if your Editor exposes them:
- Generate an asset, texture, sprite, image, or 3D model: check for the `ai` catalog plugin
- Bootstrap a new project from scratch
- 1. Confirm the CLI works and you're signed in and licensed (see references/auth-license-cloud.md).
- 2. Pick and install an Editor with the modules your target platforms need.
- Default to the latest LTS (most stable, ~2 years of patches). Reach for a Tech-stream
- release (--stream tech) only for a feature not yet in LTS; treat --stream beta/alpha as
- evaluation-only, never for a project you intend to ship. A deadline argues for LTS.
- (lts / latest aliases work almost everywhere a version is accepted — `templates` is the
- exception; see step 3.)
- 3. List the real template ids this Editor offers — don't guess them — and pick by RENDER
- (none)

## Tools / MCPs it needs

- allowed-tools: - Bash
- MCP mentions: MCP server, MCP is, mcp configure, MCP it
- allowed-tools (frontmatter): `- Bash`

## Risks / cautions found in text

- - `--format json` always produces machine-readable output; prefer it over parsing human text. Error envelopes are pretty-printed with the same 2-space indent as success envelopes. The envelope's `command` is the full command path (`projects list`, `cloud org list`), the same in json and ndjson and o

## Key rules (verbatim lines from SKILL.md)

1. - `commands --grep` waits at most 3 seconds for the Editor; `command --query` waits for it. When the Editor was not searched, a last line says why (no Editor, no answer in time, several Editors) and what to run. Wait for the Editor first with `unity status --until-ready --project-path <project>`: be
2. 2. **Not installed? Tell the user, then ask, never install silently.** Say plainly that Unity
3. - `--format json` always produces machine-readable output; prefer it over parsing human text. Error envelopes are pretty-printed with the same 2-space indent as success envelopes. The envelope's `command` is the full command path (`projects list`, `cloud org list`), the same in json and ndjson and o
4. - **Always use the latest version of the Unity CLI unless you are told to use a specific version.** A newer CLI regularly adds commands and output fields these docs describe, so an outdated one fails in ways that read like the docs being wrong.
5. - Since `0.1.0-beta.8` the CLI checks in the background for a newer version and prints an unobtrusive "update available" notice (interactive sessions only; never delays a command). Turn it off with `unity config update-check off` or the `UNITY_NO_UPDATE_CHECK` env var.

## Files inside the skill

- `CHANGELOG.md` — "Changelog — unity-cli skill"
- `references/auth-license-cloud.md` — "Auth, license & cloud — unity-cli command reference"
- `references/build-run-test.md` — "Run, test & build — unity-cli command reference"
- `references/cloud-automation.md` — "Cloud automation"
- `references/collaboration.md` — "Collaboration — unity-cli command reference"
- `references/config-hub.md` — "Config & Hub — unity-cli command reference"
- `references/diagnostics-maintenance.md` — "Diagnostics & maintenance — unity-cli command reference"
- `references/docs-workflow.md` — "Docs workflow: find, cite and match Unity documentation"
- `references/editors-install.md` — "Editors, install & modules — unity-cli command reference"
- `references/integration-advanced.md` — "Integration & advanced — unity-cli command reference"
- `references/playmode-verification-loop.md` — "Play-mode verification loop"
- `references/projects-templates.md` — "Projects, releases & templates — unity-cli command reference"
- `references/version-control.md` — "Version control — unity-cli command reference"
- `SECURITY.md` — "Security notes — unity-cli skill"
