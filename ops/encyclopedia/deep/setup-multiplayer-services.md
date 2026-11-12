# setup-multiplayer-services

Tools: gemini-plugin (unity). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\setup-multiplayer-services\SKILL.md (36 lines) + references/{entrypoints,implementation-fit,examples,dgs-entrypoint,workflows-prerequisites,underlying-services}.md

## Summary
Unity Multiplayer Services (MPS) guidance for real-time online multiplayer: routes by task to reference files covering Sessions-first implementation (`IMultiplayerService`/`ISession`), dedicated game server (`Unity.Services.Multiplayer.Server`), and lower-level Lobby/Matchmaker/Relay clients only as fallback. Grounding order: docs.unity.com llms.txt map is authoritative over memory.

## When to use / not use
Use for network topology, hosting, matchmaking, session-based play (rooms/parties/lobbies) decisions and implementation. NOT for backend features unrelated to real-time multiplayer.

## Inputs, outputs, dependencies
Input: a multiplayer requirement (topology, discovery, match flow, platforms, net stack). Output: grounded recommendation + implementation path. Needs: Unity project with MPS packages, the references/ files, optionally docs.unity.com/en-us/mps-sdk/llms.txt; user-facing language rules in implementation-fit.md.

## Key rules
1. Documentation map first: llms.txt is authoritative for what is documented; skill markdown + installed package source are fallback when unreachable — never mention llms.txt to the user.
2. Sessions-first: primary path is `Unity.Services.Multiplayer` (`IMultiplayerService`/`MultiplayerService.Instance`/`ISession`); lower-level Lobby/Matchmaker/Relay namespaces ONLY when primary APIs can't meet the goal or user explicitly asks.
3. Recommendation grounding order: conversation → project state → short targeted questions (implementation-fit.md) before prescribing topology.
4. User-facing text never names Lobby/Matchmaker/Relay/Multiplayer Sessions as separate products unless the user did — code uses real type/namespace names, explanations stay product-agnostic.
5. Dedicated servers have their own entrypoint (dgs-entrypoint.md): `IMultiplayerServerService`, `UNITY_SERVER` defines, asmdef constraints — don't apply client patterns to server builds.

## Risks / owner items
- Requires Unity project context and MPS package installation — skill guides choices, doesn't install.
- llms.txt reachability is network-dependent; offline fallback is skill refs + package source (version drift possible).
- Choosing wrong abstraction layer (going straight to Lobby/Relay) creates unmaintainable integrations — the Sessions-first rule exists to prevent this.

## Category and tags
build, cloud — unity, multiplayer, netcode, sessions, game-services.

## Revision note
Single plugin revision (2026-11-07); reference-file architecture with explicit priority ordering.
