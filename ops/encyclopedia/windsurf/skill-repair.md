# skill-repair

## Summary
skill-repair is a Google-published repair assistant for broken agent skills. It is designed to run inside a skill-management UI flow: the prompt gives it a Skill ID, a Source Path, an Installed Path and a Manifest Path plus the reported error. Its job is to fix the skill's files at the installed location, then surgically update `manifest.json` so the entry shows `"status": "installed"` with the `"error"` field cleared, after which the UI refreshes automatically. It is deliberately narrow: it does not author skills, it repairs one.

## When to use / when NOT
Use when a skill installation failed or a manifest entry is stuck in an error state and the agent has been handed the four context paths. Do NOT use it to create skills (skill-creator), install new ones (skill-installer), or for general debugging of unrelated software.

## Inputs, outputs, tools
- Inputs: Skill ID, Source Path, Installed Path, Manifest Path, and the error message.
- Outputs: corrected files under the installed skill directory and an edited `manifest.json` entry (`status: installed`, `error: null`).
- Tools: file read/write only; no scripts, no network, no MCPs. The verification step is passive (the host UI detects the manifest change).

## 5 most important rules
1. Analyse the error first; do not guess the fix.
2. List ALL files in the skill directory and analyse them collectively; multi-file skills often fail on a missing resource or bad sub-script, not the SKILL.md itself.
3. Fix at the Installed Path, not the Source Path.
4. Only after ALL relevant files are fixed, update the manifest entry for that Skill ID.
5. Set `"status": "installed"`, set or remove `"error"` (null), leave `"disabled"` untouched.

## Risks / things needing the owner
Low risk; it edits local skill files and one JSON manifest. The main caution is marking a skill "installed" while it is still broken, which would hide the failure from the UI; the repair must actually fix every file before the manifest flip. No owner action needed.

## Category / tags
ops · skill repair, manifest, debugging, agent tooling

## Revisions
Seven copies exist (claude, codex, gemini, kilo, cursor, windsurf, opencode). The claude copy (1661 bytes, Apache-2.0, publisher google, version v1) is the canonical Google revision; the others are near-identical syncs of the same text. Best revision: the claude copy (or any copy, they are the same content).
