# netlify-image-cdn (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-image-cdn\SKILL.md`. On-demand image transforms via `/.netlify/images`.

## Summary
Single documented surface: `GET /.netlify/images?url=<source>[&w=][&h=][&fit=][&position=][&fm=][&q=]` — `url` required (relative path or remote URL), rest optional. Params: `w`/`h` px integers; `fit` = `contain` (default, keeps ratio, one dim may undershoot)/`cover` (fills exactly, crops — REQUIRES both w and h, `position` picks anchor)/`fill` (stretches); `fm` = `avif|jpg|png|webp|gif|blurhash` (default content-negotiated: webp if Accept allows, else avif, else original — a source-only request still converts format); `q` = 1-100 quality, lossy formats only (avif/jpg/gif/webp), default 75. Remote sources MUST be allowlisted in netlify.toml `[images] remote_images` (regex array) or requests fail; percent-encode remote URLs (`encodeURIComponent`) since `?`/`&` break params. Also covers: image redirects, cache headers on transformed responses, framework image handling (Angular/Astro/Gatsby/Next/Nuxt), user-uploaded pipelines, debugging 404s on `/.netlify/images`.

## When to use / when NOT
Use for responsive images, format conversion (WebP/AVIF), thumbnails, blur placeholders, remote/third-party image proxying, upload pipelines, or 404 debugging. NOT for local-only processing or non-Netlify hosting.

## Inputs, outputs, tools
- Inputs: source image URL/path, transform params, remote-domain allowlist.
- Outputs: transformed image responses (resized/cropped/reformatted/quality-adjusted).
- Tools: `/.netlify/images` endpoint, `[images] remote_images` in netlify.toml, framework image components.

## 5 most important rules
1. `url` is required; `fit=cover` requires BOTH `w` and `h`.
2. Remote sources need `[images] remote_images` allowlist — unlisted = failure.
3. `encodeURIComponent` remote URLs — `?`/`&` in source URLs break params.
4. Omitted `fm` content-negotiates (webp→avif→original) — even bare `url` requests transcode.
5. `q` only affects lossy formats; `blurhash` is a valid `fm` for placeholders.

## Risks / owner notes
Allowlist is a security boundary (open proxy risk if `.*` too broad). Transform misses 404 — check allowlist first. Animated gif/webp supported but watch size. CDN caching applies to transformed responses.

## Category and tags
Category: cloud. Tags: netlify, image-cdn, optimization, responsive-images, avif, webp, allowlist.
