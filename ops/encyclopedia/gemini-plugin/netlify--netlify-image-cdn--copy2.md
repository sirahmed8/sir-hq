# netlify-image-cdn

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\codex\skills\netlify-image-cdn\SKILL.md`
- SKILL.md size: 9868 chars

## What it does

Transforms images on demand via Netlify Image CDN's /.netlify/images endpoint with query parameters for resizing/cropping/format/quality. Use when adding image optimization or responsive images, converting formats (WebP/AVIF/PNG), generating thumbnails or blur placeholders, serving remote/third-party images through the CDN, allowlisting remote domains in netlify.toml, setting up image redirects or cache headers, building user-uploaded image pipelines, or debugging a 404 on /.netlify/images. Also covers framework image handling for Angular/Astro/Gatsby/Next.js/Nuxt.

## Structure (headings inside SKILL.md)

- Netlify Image CDN
- resize a deployed image to 50px wide
- Query parameters
- Common transformations
- resize + crop to a 50px square, retaining the left side
- convert JPEG to PNG (response carries content-type: image/png)
- convert JPEG to AVIF at medium quality
- fit behavior
- Format notes
- Remote source images
- remote_images regex escaping
- Response codes
- Reusing parameters across images
- Caching headers
- Blur placeholders (fm=blurhash)
- Local development
- User-uploaded image pipelines
- Framework image handling
- Additional constraints
- Netlify house rules (image-cdn)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Credential-bearing headers (`Authorization`, `Cookie`) are **NOT forwarded** when fetching a remote source. For authenticated sources, use URLs that carry their own authorization (e.g. S3 presigned URLs) and make sure your `remote_images` patterns match those full URLs.

## Key rules (verbatim lines from SKILL.md)

1. - **`cover`:** fills exactly, cropping excess. **Requires BOTH `w` and `h`** — omitting either is invalid. Use `position` to choose what's retained.
2. - Remote sources must be **publicly accessible**.
3. 2. Percent-encode remote source URLs before placing them in the `url`
4. 4. A local 404 on `/.netlify/images` almost always means a framework dev

## Files inside the skill

- `references/user-uploads.md` — "User-Uploaded Images Pipeline"
