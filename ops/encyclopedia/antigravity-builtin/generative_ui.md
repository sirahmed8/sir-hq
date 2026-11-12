# generative_ui (Antigravity builtin)

## Summary
Antigravity's built-in skill for rendering rich interactive HTML in chat: write a self-contained .html file (Tailwind + inline JS) to the artifact directory with `UserFacing: true` metadata, optionally embed inline via `<agent-embed src="file:///<artifact_path>/widget.html">`. Hard CSP constraints: all external CDNs blocked EXCEPT one allowlisted gstatic Tailwind script (`https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js`) which should always be included. The iframe injects the app's semantic theme tokens — use `var(--card)`, `var(--foreground)`, `var(--muted-foreground)`, `var(--border)`, `var(--primary)` etc. instead of hardcoded colors; never declare :root fallbacks; font is applied for you; 12px text floor. Placement doctrine: default to standalone artifact in the side pane; inline only when compact (<500px viewport height) and directly illustrative; never set height on agent-embed (ignored) and never use h-screen/100vh/height:100% on top-level containers (feedback loop collapses the widget to a sliver).

## When to use / when NOT
Use for diagrams, data visualizations, interactive controls, educational walkthroughs — anything richer than markdown. Not for plain text answers or content that doesn't benefit from interactivity.

## Inputs, outputs, tools
- Inputs: the explanation/content to visualize, artifact directory path.
- Outputs: self-contained HTML artifact (+ optional inline embed tag in chat response).
- Tools: write_to_file, ArtifactMetadata (UserFacing), `<agent-embed>`, Tailwind via the gstatic CDN script, CSS theme variables, `document.documentElement.classList.contains('light')` for canvas theming.

## 5 most important rules
1. Self-contained HTML only — CSP blocks all CDNs except the one gstatic Tailwind script; include exactly that script tag.
2. Theme via semantic CSS variables, never hardcoded slate/white utilities and never :root fallbacks — host manages tokens dynamically for light/dark.
3. Inline embeds have a 500px height viewport — design compact; scrolling-in-a-box is usually wrong, make it a standalone artifact instead.
4. Never use viewport-relative sizing (h-screen, 100vh, height:100%) on top-level containers — the frame derives viewport from content, so these collapse the widget.
5. Don't set height on `<agent-embed>` (ignored); transparent `bg-transparent` body + card container for inline, solid `bg-[var(--background)]` for standalone; min font 12px.

## Risks / owner needs
None owner-facing; risk is purely UX — oversized or themed-wrong widgets degrade the chat experience. External images/fonts beyond Tailwind CDN will fail CSP silently.

## Category and tags
Category: design. Tags: generative-ui, html, artifacts, tailwind, inline-widgets, antigravity, visualization.

## Revisions
Single antigravity-builtin copy; no competing revisions.
