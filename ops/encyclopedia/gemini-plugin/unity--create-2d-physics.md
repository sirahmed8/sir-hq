# create-2d-physics

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\create-2d-physics\SKILL.md`
- SKILL.md size: 10595 chars

## What it does

Creates and fixes Unity 2D physics in both systems, 2D Physics Core and the legacy Rigidbody 2D system. Use when the user asks about any 2D physics task, even if neither system is named. Not for 3D physics.

## When to use (from skill text)

- - For components you added or configured in the scene, use `script eval` to check each one exists on its GameObject and its properties hold the values you set, such as a Collider 2D's `isTrigger` or the members listed on a Core component's type page.
- 3. Add temporary `Debug.Log` lines that print the behaviour you changed, such as a body's position or velocity, or a contact or trigger callback firing.

## Structure (headings inside SKILL.md)

- Create and fix Unity 2D physics
- Important
- Passing C# to `script eval`
- Step 0: Which physics system
- Full topic map
- API reference
- Worked examples
- Final step
- Final report
- (none)

## Tools / MCPs it needs

- allowed-tools: WebFetch, WebSearch
- allowed-tools (frontmatter): `WebFetch, WebSearch`

## Risks / cautions found in text

- - **docs.unity.com**: The product version, eg `7000.0`

## Key rules (verbatim lines from SKILL.md)

1. - Before making changes, establish a baseline of the current behavior so you can tell whether a later result is actually caused by your change.
2. - Do only what's asked. Don't change unrelated assets or files.
3. - Avoid long explanations.
4. - Verify runtime behaviour with temporary `Debug.Log` lines, then remove them, because the user didn't ask for logging and leftover lines clutter their script and console. Don't build settle-detection or permanent logging they didn't ask for. See [Final step](#final-step).
5. - Never reflect over types to discover an API — fetch the member page instead. The system probe is the one exception.

## Files inside the skill

- `references/2d-physics-core.md` — "2D Physics Core"
- `references/legacy-2d-physics.md` — "Legacy 2D physics"
- `SECURITY.md` — "Security notes: create-2d-physics"
