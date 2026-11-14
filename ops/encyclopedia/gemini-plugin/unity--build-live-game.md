# build-live-game

Tools: gemini (antigravity plugin). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\build-live-game\SKILL.md (read in full) + 14 references (read in full)

## Summary
Build and operate a live game backend with Unity Gaming Services: Authentication, Cloud Code (native .ccmu modules or legacy .ccmr, plus CloudBehaviours), Cloud Save (Default/Protected/Public/Custom), Remote Config, Access Control, Game Overrides, Leaderboards, Deployment Window, and UGS CLI. Server-authoritative writes for XP/rewards/currency go through Cloud Code; Protected and Custom data are writable only by server code or IAdminClient.

## When to use / not use
Use when building trusted server-side game logic, player progress, remote config, sign-in, achievements, battle passes, or leaderboards. NOT for backend-only non-Unity services or pure CLI scripts.

## Inputs, outputs, dependencies
Input: Unity project linked to a UGS project ID/environment; feature goal. Output: C# client code, Cloud Code modules, cloud resource files (.rc/.ac/.ccmu/.lb/.ugo), manifest entries. Needs: UGS packages (core 1.16+, auth 3.6.1+, cloudcode 3.0+ for .ccmu, cloudsave 3.4+, remote-config 4.2.5+, deployment 1.7.2+, tooling 1.4.1+), project linked to UGS.

## Key rules
1. Initialize UnityServices before sign-in and sign in before any service call; sensitive writes (XP, rewards, currency) go through Cloud Code, never direct client SaveAsync.
2. Author new modules as .ccmu on Unity 6000.5+ via Create > Services > Cloud Code Module Script; .ccmr is legacy maintenance only; a hand-built module without a .ccmu never appears in the Deployment Window.
3. Mark injected parameters with [CloudCodeService]; register IGameApiClient via config.AddGameApiClient() in CloudSetup.cs; Api Compatibility Level must be .NET Standard 2.1.
4. Cloud Save access classes must match between write and read (mismatch returns no data); Protected/Custom buckets are writable only by server code or IAdminClient.
5. Deploy cloud resource files via the Deployment Window or Deploy.cs; .ccmu and .ugo are not deployable via the UGS CLI; verify every file reports Success; bump importer versions to force reimport.
6. Access Control: Deny takes precedence over Allow; use deny-all-then-allow; validate by a direct client write returning 403.

## Risks / owner items
- CloudBehaviours require com.unity.services.cloudcode 3.1.0-exp.1+; if the create-menu entry is missing, fall back to a plain stateful module.
- Persisted [StateScope] state outlives code; renaming a member, class, or scope orphans state; initialize collections empty to avoid duplicate growth on load.
- The client assembly must reference the Editor-only cloud assembly (stubs are emitted for builds); a missing reference surfaces as CCSG127.
- ClearSessionToken on an anonymous-only account permanently loses it; console platforms need manual token refresh.
- DeleteAccountAsync deletes only auth data; manually clean Cloud Save, Leaderboards, and other services.

## Category and tags
unity, ugs, live-game, cloud-code, cloud-save, remote-config, leaderboards, build.

## Revision note
Single gemini revision; SKILL.md and all 14 references read in full.
