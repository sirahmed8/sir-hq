# r39 AHome haiku report (2026-11-12)

## Done
- Item 7 (part 1): cyber tunnel now draws through a WebGL2 layer (one instanced SDF batch, additive neon glow). Falls back to the old 2D canvas if WebGL2 is missing. Commit 1a0bd97, pushed to main.
  - Checks: `tsc --noEmit` exit 0. `npm run lint` exit 0, 0 errors, 112 warnings (unchanged).
  - Not checked: the look on screen. No browser run was done, so treat the visual result as unverified.

## Not done
- Racer (SpeedRacer3DGame) on the GL layer.
- Per-game pause and restart, levels, high-score chips from real saved scores.
- Item 8 audit loop (10 defects at 320/390/768/1280).
- Owner list re-check (keyboard scroll, emoji panel, ringing, video call, polls, game invites, notification sounds).
- Real transcription check: needs the PC core running.
- Local evidence lives in .sir/evidence/r39/ (gitignored).
