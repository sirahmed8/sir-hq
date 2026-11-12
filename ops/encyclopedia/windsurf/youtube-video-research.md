# youtube-video-research (claude revision)

## Summary
youtube-video-research is a viral-content engineering framework for YouTube: packaging math (CTR = Thumbnail Intrigue × Title Curiosity Gap × Topic Authority), title rules (<50 chars to survive mobile truncation, unresolved contradiction/extreme contrast like "I Replaced My Entire Team with AI", banned clickbait-without-delivery and all-caps), thumbnail heuristics (rule of thirds, high contrast vs YT dark/light bg, max 3-4 words that complement never repeat the title), a retention-curve timeline (0:00-0:30 critical hook with stakes+payoff preview and NO filler greetings; 0:30-2:00 first actionable insight; 2:00-8:00 escalating value with open loops; end screen bridging without announcing outro), pattern-interrupt cadence every 15-25s (B-roll, SFX/music drop, typography/infographic, camera change), and transcript/competitive audit steps (extract SRT/VTT, segment into chapters, compute informational density = unique concepts per runtime minute, mine comments for objections/unmet demand).

## When to use / when NOT
Use when researching YouTube competitors, deconstructing transcripts/hooks/retention/thumbnails, or planning viral content. It's an ANALYSIS FRAMEWORK — it doesn't fetch transcripts itself; pair with youtube transcript tools/yt-dlp. Do NOT use for actually producing videos (that's motion-graphics-engine/Remotion territory) or for non-YouTube platforms.

## Inputs, outputs, tools
- Inputs: target videos/channels, transcripts (SRT/VTT/text), thumbnail/title assets.
- Outputs: packaging scores, hook/retention deconstructions, title/thumbnail recommendations, comment-demand mining.
- Tools: none built in — transcript extraction via API/scraping tools referenced but external.

## 5 most important rules
1. Titles under 50 chars with genuine cognitive tension — curiosity gap must be DELIVERED in the video.
2. Thumbnails complement titles, never repeat them; max 3-4 words; rule-of-thirds composition.
3. First 30 seconds carry the whole hook: state stakes, show the payoff, zero greetings/filler.
4. Pattern interrupt every 15-25 seconds — retention is engineered, not hoped for.
5 Orofile: benchmark informational density (unique concepts/minute) and mine comments for unmet demand before writing.

## Risks / things needing the owner
No side effects. Quality depends on real transcript/analytics data — the skill gives the rubric, not the data. Copyright: quoting transcripts should stay minimal/fair-use. No owner actions.

## Category / tags
media · youtube, content-strategy, retention, thumbnails, research

## Revisions
Single source read: `C:\Users\a7med\.claude\skills\youtube-video-research\SKILL.md` (55 lines). Six-tool skill; claude revision preferred.
