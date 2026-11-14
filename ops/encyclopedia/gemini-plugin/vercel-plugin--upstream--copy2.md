# upstream

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-sandbox\upstream\SKILL.md`
- SKILL.md size: 39934 chars

## What it does

Creates isolated Linux MicroVMs using Vercel Sandbox SDK. Use when building code execution environments, running untrusted code, spinning up dev servers, testing in isolation, or when the user mentions "sandbox", "microvm", "isolated execution", or "@vercel/sandbox".

## Structure (headings inside SKILL.md)

- _CRITICAL_: Always Use Correct `@vercel/sandbox` Documentation
- Official Resources
- What changed in v2
- Quick Reference
- Creating Sandboxes
- Basic Creation
- Retrieve an Existing Sandbox
- Get-or-Create (Idempotent)
- Re-warming on Resume
- With Git Source
- With Private Git Repository
- With Private npm Packages
- From Tarball
- From a Snapshot
- From a Custom Image (VCR)
- Forking an Existing Sandbox
- When to fork a sandbox or a drive
- Auto-Dispose Pattern
- Running Commands
- Basic Command Execution
- With Options
- Detached Commands (Background Processes)
- Root Access
- File Operations
- Write Files
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - If the sandbox exists but its snapshot expired → deletes the stale sandbox,
- - When the team has no npm credentials, creation fails with a 400 error.
- - CLI: `sandbox create --credentials=npm`.

## Key rules (verbatim lines from SKILL.md)

1. - Pagination uses **cursor-based** iterators (async-iterable) instead of `since`/`until`.
2. - v1 sandboxes are backfilled so the only required code change is using `name`

## Files inside the skill

- (SKILL.md only)
