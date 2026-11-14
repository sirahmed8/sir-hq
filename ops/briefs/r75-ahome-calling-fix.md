# AHome: Fix voice/video calling - ringing, camera, quality

## Problem (from owner screenshots and text)
1. Voice/video calls start immediately without ringing - "they start while habiba didnt even join the site"
2. Should ring until other person answers or I answer
3. Video call not opening camera immediately
4. Noise cancellation needs improvement
5. Higher quality voice/video/screen share calls needed

## Required fixes
1. Implement proper call signaling: INVITE -> RINGING -> ANSWERED
2. Caller hears ringback tone, callee sees incoming call screen with accept/decline
3. Video call: camera starts only after call is ANSWERED (not on INVITE)
4. Add noise suppression (WebRTC noise cancellation, RNNoise, or platform APIs)
5. Increase bitrate/resolution for video, enable screen share with proper encoding
6. Add connection quality indicator

## Files to check
- apps/mobile/app/(tabs)/call-screen.tsx
- services/webrtc/CallManager.ts
- services/webrtc/Signaling.ts
- components/IncomingCallScreen.tsx
- hooks/useCall.ts

## Acceptance
- Outgoing call shows "جاري الاتصال..." with ringback tone
- Incoming call shows full-screen accept/decline UI
- Camera activates only after answer
- Noise cancellation measurable (test with background noise)
- Video quality: at least 720p @ 30fps on good connection
- Screen share works without freezing