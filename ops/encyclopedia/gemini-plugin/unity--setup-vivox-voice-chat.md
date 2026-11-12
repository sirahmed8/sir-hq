# setup-vivox-voice-chat

Tools: gemini-plugin (unity). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\setup-vivox-voice-chat\SKILL.md (118 lines) + references/{init-and-login,voice-channels,text-chat,events-and-participants,troubleshooting}.md

## Summary
Unity Vivox v16+ voice/text chat integration: single static entry `VivoxService.Instance` (v4 Client/ILoginSession patterns are gone). Strict init order UGS Core → Authentication sign-in → Vivox init → LoginAsync; three channel join methods (group/echo/positional) completing via ChannelJoined event not await; channel + directed text messaging; mandatory event subscription lifecycle.

## When to use / not use
Use for in-game voice chat, mic permissions, mute controls, proximity/positional voice, team/lobby channels, or direct messages in a Unity project with com.unity.services.vivox >=16.4.0. NOT for Vivox v4 codebases (different API entirely) or non-Unity platforms.

## Inputs, outputs, dependencies
Input: Unity project + Vivox package + UGS Core/Authentication companions. Output: working voice/text chat code. Needs: `Unity.Services.Vivox` namespace, event subscriptions, Android RECORD_AUDIO runtime permission / iOS NSMicrophoneUsageDescription, docs map at docs.unity.com/en-us/vivox-unity/llms.txt as authority.

## Key rules
1. Init order is non-negotiable: UnityServices.InitializeAsync → SignInAnonymouslyAsync → VivoxService.InitializeAsync → LoginAsync; double-init throws 5041 — guard on scene reload.
2. Joins complete via EVENTS, not await: subscribe ChannelJoined BEFORE calling Join*ChannelAsync; same for LoggedIn before LoginAsync.
3. Naming asymmetry trap: send is `SendDirectTextMessageAsync` but receive event is `DirectedMessageReceived` — the skill explicitly flags this hallucination.
4. ALWAYS unsubscribe in OnDestroy/OnDisable — VivoxService.Instance is a persistent singleton; leaked handlers double-fire and NRE on scene reload.
5. Limits and security: max 10 non-positional channels/user, 200 participants/channel (20502 error beyond); UGS auth mints tokens automatically — never embed HMAC keys/APP_ID secrets in client; VAT server-minting only for non-UGS identity or privileged channel ops.

## Risks / owner items
- Per-participant events live on VivoxParticipant instances from ParticipantAddedToChannel, NOT on VivoxService.Instance — wrong subscription target = silent failure.
- Without Unity Authentication, identity degrades to per-session GUID (display names work, cross-session identity lost).
- Chat history retention 7 days default; edit/delete/history APIs in references.
- llms.txt authoritative when reachable; offline fallback = skill refs + installed package source.

## Category and tags
build, cloud, mobile — unity, vivox, voice-chat, game-services, realtime.

## Revision note
Single plugin revision; unusually hallucination-aware (explicit wrong-name warnings, validation checklist).
