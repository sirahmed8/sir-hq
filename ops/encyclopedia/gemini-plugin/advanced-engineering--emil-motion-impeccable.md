# emil-motion-impeccable

- Tool: `gemini-plugin` (plugin: `advanced-engineering`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\advanced-engineering\skills\emil-motion-impeccable\SKILL.md`
- SKILL.md size: 2407 chars

## What it does

Agency-grade spring physics.

## When to use (from skill text)

- 4. **Layout Continuity**: An expanding card should morph smoothly from its trigger geometry using shared layout animations (`layoutId`).

## Structure (headings inside SKILL.md)

- Emil Motion & Impeccable Design System
- 1. Emil Kowalski Motion Physics Core
- Motion Doctrine:
- 2. Impeccable Design Heuristics (Layout, Fonts, Spacing)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2. **Spring Tokens**:
- 3. **Spacing Rhythm**: Strictly adhere to 4px/8px incremental tokens (`4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`). Never use arbitrary values like `17px` or `29px`.

## Key rules (verbatim lines from SKILL.md)

1. 1. **Never Use Linear Transitions**: Standard `transition: all 0.3s ease` feels artificial. Use physics-based springs (e.g. Framer Motion, Motion One, or Tailwind CSS spring transitions).
2. 3. **Staggered Orchestration**: When lists or grid items mount, stagger by 30–50ms per item (`staggerChildren: 0.04`). Never pop all elements simultaneously.
3. 1. **Fluid Typography Clamp**: Never jump abruptly between mobile and desktop font sizes. Use `clamp(1rem, 0.85rem + 0.75vw, 1.5rem)`.
4. 3. **Spacing Rhythm**: Strictly adhere to 4px/8px incremental tokens (`4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`). Never use arbitrary values like `17px` or `29px`.
5. 5. **Headings Balance**: Apply `text-wrap: balance` to all headers; apply `text-wrap: pretty` to body copy to avoid orphan words.

## Files inside the skill

- (SKILL.md only)
