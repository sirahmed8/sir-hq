# Fluid Spring Animations, Design Tokens & OKLCH Theming

This reference provides CSS tokens, Tailwind CSS v4 configurations, and spring physics easing functions for modern web and native interfaces.

---

## 1. Tailwind CSS v4 Token Configuration (`globals.css`)

```css
@import "tailwindcss";

@theme inline {
  /* OKLCH Perceptually Uniform Palette */
  --color-background: oklch(0.145 0 0);
  --color-foreground: oklch(0.985 0 0);
  --color-card: oklch(0.205 0 0);
  --color-card-foreground: oklch(0.985 0 0);
  --color-primary: oklch(0.588 0.22 255.4);
  --color-primary-foreground: oklch(0.985 0 0);
  --color-muted: oklch(0.269 0 0);
  --color-muted-foreground: oklch(0.708 0 0);
  --color-accent: oklch(0.269 0 0);
  --color-accent-foreground: oklch(0.985 0 0);
  --color-border: oklch(0.269 0 0 / 0.6);
  --color-ring: oklch(0.588 0.22 255.4);

  /* Radius Hierarchy */
  --radius: 0.75rem;
  --radius-sm: calc(var(--radius) * 0.75);
  --radius-md: var(--radius);
  --radius-lg: calc(var(--radius) * 1.25);
  --radius-xl: calc(var(--radius) * 1.5);
  --radius-2xl: calc(var(--radius) * 2);

  /* Spring Physics Easing Curve */
  --ease-spring: linear(
    0, 0.006, 0.025 2.8%, 0.101 6.1%, 0.539 18.9%, 0.721 25.3%, 0.849 31.5%,
    0.937 38.1%, 0.985 45.4%, 1 54.4%
  );
}
```

---

## 2. Spring Micro-Interactions & Hover Dynamics

### Tactile Button with Spring Physics
```tsx
<button className="
  px-4 py-2.5 rounded-lg font-medium text-sm
  bg-primary text-primary-foreground
  shadow-sm hover:shadow-md
  transition-all duration-200 ease-[var(--ease-spring)]
  hover:brightness-110 active:scale-[0.97]
  focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring
">
  Save Changes
</button>
```

---

## 3. CSS `@starting-style` Dialog & Popover Animations

```css
dialog[open] {
  opacity: 1;
  transform: scale(1);
  transition: opacity 0.25s var(--ease-spring), transform 0.25s var(--ease-spring), display 0.25s allow-discrete;
}

@starting-style {
  dialog[open] {
    opacity: 0;
    transform: scale(0.95);
  }
}
```
