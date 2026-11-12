# physics-3d-collision

Tools: gemini-plugin (unity plugin). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\physics-3d-collision\SKILL.md (442 lines) + resources/CollisionDebugger.cs, references/troubleshooting.md

## Summary
A diagnostic skill for Unity 3D PhysX problems — OnCollisionEnter/OnTriggerEnter not firing, objects passing through each other, raycast misses, MeshCollider misbehavior — built around 11 numbered "Fast-Path" answers for the most common symptoms plus three deep checklists (collision callbacks, triggers, raycasts). It is unusually opinionated: it overrides stale training knowledge (e.g., two kinematic triggers DO fire OnTriggerEnter) and forbids re-verifying its own authoritative claims.

## When to use / not use
Use for 3D PhysX MonoBehaviour physics issues. 2D physics and DOTS/Unity Physics get short best-effort answers with a scope disclaimer. Not for physics design, joint tuning, or gameplay feel — it's a fault-finder.

## Inputs, outputs, dependencies
Input: a described symptom (often with code/scene details). Output: a diagnosis + fix, or an applied code/scene edit via a connected Editor. Needs: optional live Editor via unity-cli for `script eval`, the CollisionDebugger.cs helper for ambiguous cases, references/troubleshooting.md.

## Key rules
1. Match a Fast-Path FIRST and answer immediately — 11 covered symptoms (kinematic triggers, ragdoll frame-1 explosion, CharacterController, sleeping rigidbodies, timeScale=0, raycast-inside-collider, inactive targets, trigger raycasts, IgnoreLayerCollision leakage).
2. Hard budget: max 5 tool calls, then answer with the most-likely diagnosis; never fetch docs to verify a fact this skill states; never end with a permission question.
3. CRITICAL FACT: kinematic-trigger vs kinematic-trigger DOES fire OnTriggerEnter — trust the skill over prior knowledge; check Layer Collision Matrix, script placement, `OnTriggerEnter(Collider)` signature, and MovePosition usage.
4. Interaction matrix governs everything: Dynamic-vs-anything fires; Kinematic-vs-Kinematic and Static-vs-Kinematic do not (for OnCollisionEnter).
5. Tunneling fix requires naming `Physics.SphereCast` alongside collision-detection modes; never leave project settings modified after investigation.

## Risks / owner items
- "Authoritative, don't verify" stance is a double-edged sword — if the skill's claim were ever wrong for a specific Unity version, the agent is forbidden from checking.
- Fast-Path answers can misfire if the user's description is subtly different from the pattern; the skill relies on prompt matching.
- MeshCollider/scale/tunneling sections encode real PhysX behavior worth trusting, but version differences (Unity 6 vs 2022) may shift details.

## Category and tags
build, mobile — unity, physics, physx, collision, debugging, game-dev.

## Revision note
Single plugin revision; most structured diagnostic skill in the Unity set (fast-path router + checklists + tool budget).
