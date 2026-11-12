# create-2d-physics (Unity)

## Summary
Skill for creating and fixing Unity 2D physics across BOTH systems — the new 2D Physics Core (`Unity.U2D.Physics`, Physics Pose/Area/Constraint/Simulation components, Unity 6000.7+ with `com.unity.2d.physics`) and legacy Rigidbody2D/Collider2D — which share no code and never interact. Its core discipline: identify the system FIRST (components are the reliable signal; a probe checks loaded assemblies), fetch version-correct docs instead of trusting memory, establish a baseline, and verify runtime behaviour with temporary Debug.Logs in Play mode.

## When to use / when NOT
Use for any 2D physics task even when the system isn't named; stop and say so if the user means 3D. Do NOT use for 3D physics or for general Unity scripting.

## Inputs, outputs, tools
- Inputs: the physics task; project signals (scene components, scripts, wording).
- Outputs: physics code/components in the correct system, verified in Play mode.
- Tools: `unity` CLI (`unity command --format json`, `script eval`), unity-cli/unity-pipeline skills, WebFetch/WebSearch for docs; references `references/2d-physics-core.md`, `legacy-2d-physics.md`; versioned docs via xrefmap.yml caching.

## 5 most important rules
1. Step 0 is mandatory: determine Core vs Legacy before writing any physics code — wrong-system code compiles and does nothing.
2. Components beat wording; if still ambiguous, run the assembly probe or STOP and offer all three routes — never choose for the user.
3. `script eval` takes a statement block: no `using`, fully qualified types (`UnityEngine.Rigidbody2D`, `UnityEngine.Object` not bare `Object`).
4. Never reflect over types to discover APIs — fetch the member page; version docs by Unity version / package version from manifest or packages-lock.
5. Final step: zero console errors → read back component/script values → temporary Debug.Logs → Play mode check → remove logs. No screenshots.

## Risks / things needing the owner
Runtime physics changes need Play-mode verification; leftover Debug.Logs must be removed. Requires the Unity Editor/CLI installed and project open.

## Category / tags
mobile · unity, 2d-physics, gamedev, verification

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\unity\skills\create-2d-physics\SKILL.md` (v0.3.0) + 2 reference docs. Only gemini-plugin holds it.
