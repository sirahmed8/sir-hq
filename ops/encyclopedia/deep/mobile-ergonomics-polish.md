# mobile-ergonomics-polish

Source read: `C:\Users\a7med\.claude\skills\mobile-ergonomics-polish\SKILL.md` (2.2 KB; claude revision; codex/cursor/kilo/opencode/windsurf listed).

## Summary
A mobile UX checklist for eradicating amateur layout bugs: viewport containment (mandatory `overflow-x: clip|hidden` on root, `box-sizing: border-box`, `max-width:100%; height:auto` on media, no fixed widths >100vw), mobile nav (hamburger drawer with spring entrance + backdrop blur, closes on route change/Escape), interactive elements (logo links to `/`, `tel:+`/`mailto:` contact links in international format), touch ergonomics (44x44px minimum targets per Fitts's law, 8px spacing between adjacent targets), and micro-feedback (dynamic `getFullYear()` copyright, toast/banner success feedback, inline errors with Retry, dead-button/`href="#"`/placeholder-copy eradication).

## When to use / when NOT
Use as an audit/fix pass on any site or app with mobile layout, scroll, or touch problems. It is a checklist overlay, not a redesign tool — pair with a design skill for visual direction.

## Inputs, outputs, tools
- Inputs: a UI/page with mobile issues (horizontal scroll, small targets, dead controls).
- Outputs: fixed CSS/markup for containment, nav, targets, feedback states.
- Tools: none — pure frontend guidance (CSS, Tailwind classes referenced).

## 5 most important rules
1. Zero horizontal scrolling is non-negotiable — `overflow-x: clip` on root containers.
2. 44x44px minimum touch targets with 8px gaps (Fitts's law).
3. Mobile menu must close on route change and Escape; spring drawer + backdrop blur.
4. Every button needs a real handler/route — kill `href="#"`, dead onClicks, Lorem ipsum, "Coming soon".
5. Dynamic copyright year; success toasts and inline errors with explicit Retry.

## Risks / owner notes
Low risk; verification is visual (mobile viewport screenshots at 320/390px). `tel:`/`mailto:` links expose the owner's contact details — confirm they're meant to be public.

## Category and tags
Category: design. Tags: mobile, ux, touch-targets, responsive, fitts-law, micro-interactions.
