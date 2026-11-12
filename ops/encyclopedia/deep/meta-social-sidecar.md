# meta-social-sidecar

Source read: `C:\Users\a7med\.claude\skills\meta-social-sidecar\SKILL.md` (4.9 KB; claude revision; codex/cursor/gemini-plugin/kilo/opencode/windsurf listed). Owner-specific social automation — internal skill.

## Summary
Automation spec for the owner's social pipeline: Meta Graph API v21.0 Facebook Page publishing, Remotion video render triggers, and Linktree sync. Key facts: `/me/feed` user-timeline posting is deprecated (error #200) — all publishing targets Page endpoints (`/{page_id}/feed`, `/photos`, `/videos`); auth requires exchanging the user token for a long-lived Page Access Token via `me/accounts` with `pages_manage_posts`, `pages_read_engagement`, `pages_show_list`, stored in `.env` (`FB_PAGE_ID`, `FB_PAGE_ACCESS_TOKEN`, `META_GRAPH_VERSION`). Defines a `ProfessionalSocialPost` JSON schema (hook ≤140 chars, body, metrics, tech_stack, single CTA, linktree_url, media attachment, ar-EG/en-US) aligned with high-conversion-copywriting. Documents two Linktree destinations (developer brand vs media studio) with a pinned-link update payload pattern, and a 3-step render pipeline (Python screenplay generator → `build_flagship_video.py` 60fps 1080x1920 → `meta/client.py --publish-video`).

## When to use / when NOT
Use when preparing or publishing owner-approved social content, rendering Remotion videos for social, or syncing Linktree links after a release. Do NOT use to post publicly without explicit manual approval, and never with a raw user token.

## Inputs, outputs, tools
- Inputs: post content per the schema, video files, Linktree update payloads, `.env` tokens.
- Outputs: published Page posts/photos/videos, rendered MP4s, pinned Linktree links.
- Tools: Meta Graph API v21.0, Remotion CLI, edge-tts, Python scripts (`dynamic_social_engine.py`, `build_flagship_video.py`, `meta/client.py`).

## 5 most important rules
1. Page Access Token only — never post with a personal user token (`/me/feed` is dead in v21.0).
2. Zero public posting without explicit manual approval — the pipeline stages, the owner publishes.
3. Copy follows the professional schema: quantifiable hook, real metrics/stack proof, single CTA, no buzzwords/emojis in headers.
4. Keep the two Linktree destinations distinct; pin new release links with UTM params.
5. Video pipeline order is fixed: screenplay → render → publish; Egyptian Arabic scripts go through the dynamic engine.

## Risks / owner notes
Page tokens are long-lived secrets — `.env` only, never git. Paths reference the owner's `D:\Projects` layout (`Laptop manager`, `SIR AI`) which may move; verify before running. Posting as the owner's brand is an outward-facing act — approval gate is absolute.

## Category and tags
Category: media. Tags: meta-graph-api, facebook-page, remotion, linktree, social-automation, owner-specific.
