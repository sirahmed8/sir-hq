# karpathy-skills

- Tool: `claude`
- Category: data
- Source: `C:\Users\a7med\.claude\skills\karpathy-skills\SKILL.md`
- SKILL.md size: 2851 chars

## What it does

Use when writing or reviewing AI-assisted code and you need guardrails: think before coding, simplicity first, surgical changes, and goal-driven verification.

## Structure (headings inside SKILL.md)

- Karpathy Skills — AI Software Engineering Guardrails
- 1. Think Before Coding
- 2. Simplicity First (YAGNI)
- 3. Surgical Precision
- 4. Goal-Driven Execution
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Do not delete pre-existing dead code unless explicitly requested.

## Key rules (verbatim lines from SKILL.md)

1. - If multiple interpretations exist, present them clearly—never pick silently.
2. - Avoid premature "flexibility", "configurability", or generic factory layers that weren't requested.
3. - Do not write defensive error handling for impossible scenarios.
4. - **Never rewrite entire files.** Use targeted line/block replacement (`replace_file_content` / `edit_file`).
5. - Do not randomly "improve" adjacent code, comments, or formatting outside the task scope.

## Files inside the skill

- (SKILL.md only)
