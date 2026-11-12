# agent-reach

Source read: `agents/agent-reach.md` (workspace-owned skill; not tied to a specific skill store).

## Summary
A read-only agent skill for retrieving content across multiple platforms: search, posts, comments, subtitles, stock prices, and job listings. It fetches data from Xiaohongshu, Bilibili, Twitter/X, Reddit, YouTube (captions/transcripts), GitHub, V2EX, Xueqiu/Stock quotes, LinkedIn/Boss直聘, Instagram, Facebook, and Xiamen podcasts. The skill does not perform any write operations (no posting, commenting, liking, or DMs), making it suitable for monitoring, research, and data aggregation tasks.

## When to use / when NOT
Use when you need to gather public content from multiple platforms quickly, such as market research, competitive analysis, or trend spotting. Do NOT use for any action that writes, publishes, or interacts socially — the skill is strictly read-only. Do NOT attempt to log in or bypass authentication; it only works with publicly available content.

## Inputs, outputs, tools
- Inputs: a platform name or URL, optional query terms, date filters, or category tags.
- Outputs: structured data containing post/text, author, engagement metrics (likes, views), timestamps, and platform-specific metadata. Returns null or an error if the platform is inaccessible or the content is restricted.
- Tools: HTTP fetch, platform-specific APIs (Reddit JSON, Twitter API v2, YouTube Transcript API, etc.). MCP: none required (pure HTTP client).

## 5 most important rules
1. **Never attempt write operations** — this skill is read-only by design; any attempt to post, comment, or like will fail.
2. **Respect platform rate limits** — make a single batch request per platform per turn to avoid being blocked.
3. **Content is public only** — the skill will not fetch content behind login walls or paywalls; do not attempt to authenticate.
4. **Output format is consistent across platforms** — all results include at minimum: title, source, URL, timestamp, and engagement counts.
5. **Error handling is mandatory** — if a platform returns an error or is unavailable, the skill logs the failure and continues to the next platform in the batch.

## Risks / owner notes
The skill's read-only guarantee depends on external platforms not changing their API terms or adding auth requirements. Owner should monitor for API deprecations, especially on Twitter/X and Reddit. The skill should not be used for sensitive data collection or personal information gathering.

## Category / tags
research · read-only, web-scraping, data-aggregation, monitoring, twitter, reddit, youtube, github

## Revisions
The workspace-owned `agents/agent-reach.md` is the sole source; no codex, claude, or gemini-plugin copies exist. This is the canonical and only revision.