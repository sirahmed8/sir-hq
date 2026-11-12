# validate-urp-render-graph-renderer-feature

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\validate-urp-render-graph-renderer-feature\SKILL.md`
- SKILL.md size: 14298 chars

## What it does

Reviews a Unity 6 URP ScriptableRendererFeature that uses the Render Graph API, checking resource wiring, material binding, execution structure, and best practices. Use to validate a renderer feature.

## When to use (from skill text)

- Use this skill when:

## Structure (headings inside SKILL.md)

- Skill: Validate a Unity URP Render Graph Renderer Feature
- Purpose
- When to Use
- Inputs
- Output Format
- 1. Validation Summary
- 2. Confirmed Issues
- 3. Likely Issues / Risky Assumptions
- 4. Recommended Fixes
- 5. Corrected Snippets
- 6. Missing Information
- Validation Checklist
- 1. Material Binding
- 2. Texture Resource Wiring
- 3. Execution Structure / Static Render Function
- 4. Render Graph Descriptor Validation
- 5. Manual Copy Pass Simplification
- 6. Manual Blit Pass Simplification
- 7. Global Resource Exposure
- 8. Renderer Feature Input Declaration
- Guardrails
- Non-Goals
- Evaluation Criteria
- Notes for Future Expansion
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - the implementation risks using a dangling or stale handle because pass data is not fully initialized each time it is recorded
- - important properties such as MSAA, graphics format, or compatibility with the active render target are dropped accidentally

## Key rules (verbatim lines from SKILL.md)

1. - validating a custom `ScriptableRendererFeature` before integrating it
2. - required material/shader properties
3. - null handling exists where required
4. - **all required material inputs are bound before execution**
5. - required shader properties are assumed to exist without being set

## Files inside the skill

- (SKILL.md only)
