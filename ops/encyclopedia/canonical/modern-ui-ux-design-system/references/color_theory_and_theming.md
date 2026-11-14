# Color Theory, OKLCH Dynamics & Flawless Light/Dark Theming

This reference provides exact formulas, contrast standards, and implementation patterns for modern theming systems.

---

## 1. 60-30-10 Color Architecture

- **60% Dominant Base**: Canvas / Page background (`--color-background`).
- **30% Secondary Structure**: Card surfaces, sidebars, headers, dialog surfaces, and subtle borders (`--color-card`, `--color-muted`, `--color-border`).
- **10% Accent Intent**: Primary CTA buttons, focus rings, active navigation indicators, and key metric badges (`--color-primary`, `--color-ring`).

---

## 2. OKLCH Perceptual Uniformity

Unlike HSL or RGB, OKLCH provides **perceptually uniform lightness**. When shifting hue, the perceived brightness does not distort:

$$\text{oklch}(L \quad C \quad H)$$
- $L$ = Perceived Lightness ($0.0 \to 1.0$)
- $C$ = Chroma / Saturation ($0.0 \to 0.4$)
- $H$ = Hue angle ($0^\circ \to 360^\circ$)

### Dark & Light Mode Coordinated Tokens
```css
:root {
  /* Light Mode */
  --color-background: oklch(0.99 0 0);
  --color-foreground: oklch(0.14 0 0);
  --color-card: oklch(1 0 0);
  --color-card-foreground: oklch(0.14 0 0);
  --color-primary: oklch(0.55 0.22 260);
  --color-primary-foreground: oklch(0.99 0 0);
  --color-muted: oklch(0.95 0 0);
  --color-muted-foreground: oklch(0.45 0 0);
  --color-border: oklch(0.90 0 0);
}

.dark {
  /* Dark Mode */
  --color-background: oklch(0.14 0 0);
  --color-foreground: oklch(0.98 0 0);
  --color-card: oklch(0.19 0 0);
  --color-card-foreground: oklch(0.98 0 0);
  --color-primary: oklch(0.65 0.22 260);
  --color-primary-foreground: oklch(0.14 0 0);
  --color-muted: oklch(0.24 0 0);
  --color-muted-foreground: oklch(0.70 0 0);
  --color-border: oklch(0.26 0 0 / 0.7);
}
```

---

## 3. WCAG AAA Contrast Verification

- Normal body text ($< 18\text{pt}$): Minimum contrast ratio **7:1**.
- Large headings ($\ge 18\text{pt}$ or bold $\ge 14\text{pt}$): Minimum contrast ratio **4.5:1**.
- Essential UI components and interactive borders: Minimum contrast ratio **3:1**.
