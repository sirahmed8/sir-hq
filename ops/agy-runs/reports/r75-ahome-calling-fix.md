# r75-ahome-calling-fix — report

Date: 2026-11-14 ~03:25 Cairo. Tool: kilo (free CLI). Project: D:/Projects/AHome.

## What the owner reported
1. Voice/video calls start immediately without ringing ("they start while habiba didnt even join the site").
2. It should ring until the other person answers, or until I answer.
3. Video call does not open the camera immediately.
4. Noise cancellation needs improvement.
5. Higher quality voice/video/screen share is needed.

## Repair first (tree was broken by the previous model)
The previous model staged a fake React Native "mobile" scaffold:
- `apps/mobile/app/(tabs)/call-screen.tsx`
- `services/webrtc/CallManager.ts`, `services/webrtc/Signaling.ts`
- `components/IncomingCallScreen.tsx`
- `hooks/useCall.ts`

It is not a real project: `apps/mobile` has no `package.json`, no Expo/React Native dependencies, and the files use web-only APIs (`new Audio`, `HTMLVideoElement`, a `Video` component that is never imported) and a `useCall` that is pure `console.log` placeholders. It also is not where AHome runs: the real app is `apps/web` (Next.js, wrapped by `apps/mobile-capacitor` for Android).

Decision (rule 7, logged): remove the scaffold with `git rm -rf apps/mobile components hooks services` and fix the real caller in `apps/web`. Commands and output:

```
$ git rm -rf -- "apps/mobile" "components" "hooks" "services"
rm 'apps/mobile/app/(tabs)/call-screen.tsx'
rm 'components/IncomingCallScreen.tsx'
rm 'hooks/useCall.ts'
rm 'services/webrtc/CallManager.ts'
rm 'services/webrtc/Signaling.ts'
```

## What changed (all in apps/web)
Commit 02503e7 + 48b684e "fix(calls): ring until answered, start camera after answer, noise suppression and quality (r75)", pushed to main.

### 1. Real INVITE -> RINGING -> ANSWERED (`src/hooks/useWebRTCCall.ts`)
- Removed the fake `setTimeout(..., 1200)` that set the call to "connected" 1.2 s after the offer, which is why the call appeared to start before the partner joined.
- New state: `connecting -> ringing -> connected`. The caller sends the offer (INVITE) and stays `ringing` until the partner's `answer` arrives; only then `setCallState("connected")`.
- Ringback tone now loops the whole time the call is `ringing` (was cut off after 1.2 s), and stops on answer / end.

### 2. Camera starts only after ANSWERED (`src/hooks/useWebRTCCall.ts`)
- The caller asks only for the microphone up front (`AUDIO_MEDIA_CONSTRAINTS`, `video: false`).
- For a video call it adds a `sendrecv` video transceiver with no track (`pc.addTransceiver("video", { direction: "sendrecv" })`), so the offer still contains an `m=video` line and the partner's incoming screen still says "video call" (the island reads the type from the SDP).
- On the answer, `startVideoAfterAnswer()` opens the camera with `VIDEO_MEDIA_CONSTRAINTS`, attaches it to `localVideoRef`, hands the track to the reserved sender with `replaceTrack`, applies the video bitrate, and only then clears `isVideoDisabled`.
- The answerer (`useCallAnswer.ts`) opens its camera when it accepts (it only mounts after accept), which is "after answered".
- `toggleVideo` is ignored before the call is connected so the camera cannot be opened during ringing.

### 3. Noise suppression (`src/lib/webrtc/callMedia.ts`)
- `AUDIO_MEDIA_CONSTRAINTS = { echoCancellation: true, noiseSuppression: true, autoGainControl: true, channelCount: 1 }`, used by the caller's initial `getUserMedia`, the answerer's `getUserMedia`, and both `retryMedia` paths. This turns on the platform/browser noise suppression (the WebRTC audio pipeline: RNNoise on Chrome/Android, the platform NS on Safari/iOS).

### 4. Higher quality (`src/lib/webrtc/callMedia.ts`)
- `VIDEO_MEDIA_CONSTRAINTS = { width: { ideal: 1280 }, height: { ideal: 720 }, frameRate: { ideal: 30, max: 30 }, facingMode: "user" }` on both sides.
- `applyVideoBitrate(pc)` sets `sender.setParameters` `maxBitrate = 1_500_000` on every video sender, called after the answer, after the camera starts, and after a re-negotiation. Screen share requests 30fps (`getDisplayMedia({ video: { frameRate: { ideal: 30, max: 30 } } })`) and re-applies the bitrate after `replaceTrack`, both when sharing starts and when the camera returns, so it does not fall back to a low default and freeze.

### 5. Connection quality indicator
- `readConnectionQuality(pc)` reads `inbound-rtp` packet loss and the succeeded `candidate-pair` round-trip time; `rateConnectionQuality` maps them to good / fair / poor.
- Both hooks poll every 2 s while connected and expose `connectionQuality`; `PrivateCallModal.tsx` shows a coloured chip ("الاتصال ممتاز / متوسط / ضعيف", "Excellent / Fair / Poor connection").

### 6. Full-screen incoming call (`src/components/chat/IncomingCallOverlay.tsx`, `incomingCall.ts`, `app/page.tsx`)
- `incomingCall.ts` gained `subscribePendingCall(listener)` (and emits on set/clear) so a UI can react to the ringing call the island holds.
- New `IncomingCallOverlay`: fixed full-screen, shows the caller name, "مكالمة واردة", voice/video, and large Accept / Decline buttons. Accept opens the call window (`onAnswer(type)`), which answers the pending offer; Decline broadcasts hangup and clears it.
- Mounted in `app/page.tsx` with `hidden={activeCall.isOpen}` so it steps aside for the call window. The Dynamic Island card still works as before.

### 7. Pre-existing bug fixed: audio calls were silent
- On an audio call the remote `<video>` element was only rendered inside the video branch, so the partner's `MediaStream` was never attached to a media element and no voice played. The remote media element is now always mounted in the stage and only visually hidden when it is an audio call (`h-px w-px opacity-0`), so the voice plays on every call.

## Files touched
- `apps/web/src/lib/webrtc/callMedia.ts` (new)
- `apps/web/src/hooks/useWebRTCCall.ts`
- `apps/web/src/components/chat/useCallAnswer.ts`
- `apps/web/src/components/chat/PrivateCallModal.tsx`
- `apps/web/src/components/chat/incomingCall.ts`
- `apps/web/src/components/chat/IncomingCallOverlay.tsx` (new)
- `apps/web/src/app/page.tsx`
- `apps/web/tests/r75_call_signaling.test.mjs` (new, 6 tests)

## Commands and real output
```
$ npx tsc --noEmit -p tsconfig.json        -> EXIT=0
$ eslint <7 touched files>                  -> EXIT=0 (no errors)
$ node --test tests/r75_call_signaling.test.mjs tests/incoming_call.test.mjs
  -> tests 12, pass 12, fail 0
$ node --test --test-concurrency=1 tests/*.test.mjs
  -> tests 1074, pass 1069, fail 4, skipped 1
  (the 4 fails are "browserType.launch: Executable doesn't exist at D:\Caches\ms-playwright\webkit-2388\Playwright.exe",
   the pre-existing WebKit-not-installed environment failures, same as baseline)
$ npm run build                            -> EXIT=0 (Next.js production build, all routes compiled)
```

Push: `bfde7b2..02503e7 main -> main` and `02503e7..48b684e main -> main`. gitleaks: no leaks. privacy-audit: 1090 files, no matches.
CI quota flag `ops/ci-quota-exhausted.flag` is present, so local verification (tsc + eslint + tests + build) is the gate per WORKER_PREAMBLE rule 18.

## Acceptance lines
1. Outgoing call shows "جاري الاتصال..." then "يرن..." with ringback tone — DONE.
2. Incoming call shows full-screen accept/decline UI — DONE (IncomingCallOverlay + island).
3. Camera activates only after answer — DONE (caller defers; answerer at accept).
4. Noise cancellation measurable — DONE as platform constraints on both sides (not A/B measured on hardware).
5. Video quality at least 720p @ 30fps — DONE (constraints + 1.5 Mbps sender cap).
6. Screen share works without freezing — screen share now requests 30fps and re-applies the 1.5 Mbps video bitrate after `replaceTrack` on both start and stop; not re-tested on hardware.
7. Connection quality indicator — DONE.

## What is unsure / not verified
- Not tested on the owner's two physical devices (needs both signed in). Ringback audibility, the full-screen incoming UI, camera-after-answer and real noise suppression need a live two-device check.
- The 4 failing tests are environment (WebKit not installed), not this change.
- `apps/local-core/scripts/_probe_router.py` is untracked and not from this round; left alone.

## Recommended next
- A two-device live check (owner): call from one device to the other, confirm ringback, full-screen incoming, camera only after accept, and that the voice is audible on an audio call.
- Consider installing the Playwright WebKit browser so those 4 tests run in CI.