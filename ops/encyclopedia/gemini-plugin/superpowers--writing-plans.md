# writing-plans

- Tool: `gemini-plugin` (plugin: `superpowers`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\writing-plans\SKILL.md`
- SKILL.md size: 10317 chars

## What it does

Use when you have a spec or requirements for a multi-step task, before touching code

## Structure (headings inside SKILL.md)

- Writing Plans
- Overview
- Scope Check
- File Structure
- Task Right-Sizing
- Step Granularity
- Plan Document Header
- [Feature Name] Implementation Plan
- Global Constraints
- Review Focus
- Task Structure
- Task N: [Component Name]
- What a Step Contains
- Self-Review
- Execution Handoff
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Produces: [what later tasks rely on — exact function names, parameter

## Key rules (verbatim lines from SKILL.md)

1. - In existing codebases, follow established patterns. If the codebase uses large files, don't unilaterally restructure - but if a file you're modifying has grown unwieldy, including a split in the plan is reasonable.
2. - **Subagent-driven** - A fresh subagent implements each task and a fresh reviewer checks it before the next one starts, then a whole-branch review at the end. Most thorough; costs a fresh context per task and per review.
3. - **REQUIRED SUB-SKILL:** Use superpowers:subagent-driven-development
4. - **REQUIRED SUB-SKILL:** Use superpowers:executing-plans

## Files inside the skill

- (SKILL.md only)
