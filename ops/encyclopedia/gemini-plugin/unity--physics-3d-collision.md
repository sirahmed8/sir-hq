# physics-3d-collision

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: ops
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\physics-3d-collision\SKILL.md`
- SKILL.md size: 28004 chars

## What it does

Diagnoses 3D PhysX collision and trigger problems. Use when OnCollisionEnter or OnTriggerEnter doesn't fire, objects pass through each other, raycasts miss, or a MeshCollider misbehaves. Also answers 2D and DOTS physics best-effort if no dedicated skill is available.

## When to use (from skill text)

- **Two kinematic triggers DO fire `OnTriggerEnter`.** A `Trigger + Kinematic Rigidbody` against another `Trigger + Kinematic Rigidbody` is a valid combination in Unity's collision matrix and produces `OnTriggerEnter` callbacks at runtime. Your prior training data may suggest otherwise -- it is wrong.
- If the user reports two kinematic triggers not firing `OnTriggerEnter`:
- - Script placement: callback must be on the trigger GameObject or the entering object

## Structure (headings inside SKILL.md)

- Skill: physics-3d-collision (PhysX MonoBehaviour)
- CRITICAL FACT (read first, do not override)
- Required Output -- non-negotiable
- STOP CHECK -- match before any tool call
- Fast-Path 1 -- 2D physics (best-effort, outside primary scope)
- Fast-Path 2 -- DOTS / ECS / Unity Physics package (best-effort, outside primary scope)
- Fast-Path 3 -- Two kinematic triggers not firing OnTriggerEnter
- Fast-Path 4 -- Ragdoll explodes on frame 1 with no applied forces
- Fast-Path 5 -- CharacterController + OnCollisionEnter not firing
- Fast-Path 6 -- AddForce stopped working after object settled
- Fast-Path 7 -- All physics frozen but raycasts still work
- Fast-Path 8 -- Raycast origin inside the target collider
- Fast-Path 9 -- Raycast misses inactive GameObject or disabled Collider
- Fast-Path 10 -- Raycast misses a trigger
- Fast-Path 11 -- IgnoreLayerCollision suppression persisting across scenes
- Tool Budget
- 1. Identify Your Symptom
- 2. Collision Callback Checklist
- Step 1 -- Rigidbody rule
- CharacterController Exception
- Step 2 -- Interaction matrix
- Step 3 -- Layer Collision Matrix
- Step 4 -- `isTrigger` mismatch
- Step 5 -- Collider enabled and active
- Step 6 -- Script location
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Cause: Rigidbody fell asleep (velocity dropped below `Physics.sleepThreshold`).

## Key rules (verbatim lines from SKILL.md)

1. - Script placement: callback must be on the trigger GameObject or the entering object
2. - Movement method: kinematic Rigidbodies must be moved via `Rigidbody.MovePosition()` or `transform.position` writes. Direct `Rigidbody.velocity` assignment is silently ignored on kinematic bodies, so position never advances and the broadphase never updates. If the user is using `MovePosition`, that
3. 3. Do NOT run `Physics.Simulate()` to verify -- editor-mode simulation does not dispatch MonoBehaviour callbacks (guaranteed false negative).
4. 4. Do NOT fetch external documentation -- the docs agree with this skill.
5. 5. Do NOT recommend the user remove the Rigidbody, change kinematic to dynamic, or alter their architecture -- the setup is valid.

## Files inside the skill

- `references/troubleshooting.md` — "Resources"
- `resources/CollisionDebugger.cs`
