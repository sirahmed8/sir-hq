# Psychological & Ergonomic Laws in Modern UI/UX

This reference provides mathematical formulations and design applications for core cognitive psychology and human-computer interaction (HCI) laws.

---

## 1. Hick-Hyman Law (Decision Architecture)

### Mathematical Formulation
$$T = b \cdot \log_2(n + 1)$$
Where:
- $T$ = Mean decision response time.
- $n$ = Number of equally probable alternatives.
- $b$ = Empirical constant (cognitive processing speed).

### UI Engineering Rules:
1. **Limit Root Options**: Cap primary top-level menu items to $\le 5-7$.
2. **Progressive Disclosure**: Break complex workflows into multi-step wizards or collapsible sections.
3. **Hierarchy of Action**: Every card or dialog must have exactly **one** distinct Primary CTA (`bg-primary text-primary-foreground`). Secondary options must use ghost/outline variants.

---

## 2. Fitts's Law (Target Acquisition & Ergonomics)

### Mathematical Formulation
$$\text{Index of Difficulty } (ID) = \log_2\left(\frac{2D}{W}\right)$$
$$\text{Movement Time } (MT) = a + b \cdot ID$$
Where:
- $D$ = Distance to target center.
- $W$ = Width of target along axis of motion.
- $a, b$ = Constants.

### UI Engineering Rules:
1. **Minimum Touch Area**: All interactive targets must be at least **44x44px** (`min-h-10 min-w-10` or `p-3`).
2. **Edge Snapping**: Pin primary mobile navigation bars to the screen bottom (thumb zone) where $D$ is minimized.
3. **Destructive Separation**: Place destructive actions (e.g., "Delete Project") in a secondary dialog separated by $\ge 16\text{px}$ to prevent accidental activation.

---

## 3. Miller's Law (Cognitive Chunking)
- Human working memory holds approximately $7 \pm 2$ chunks of information.
- Format phone numbers, credit cards, dates, and metric dashboards into digestible semantic groups (e.g. `Card` groups containing 3–4 key statistics).

---

## 4. Gestalt Laws of Visual Grouping

1. **Law of Proximity**: Elements placed close together (`gap-2`) are perceived as a single unit; unrelated items must use wider margins (`mt-8` or `space-y-6`).
2. **Law of Common Region**: Enclose related controls inside card boundaries with subtle borders (`bg-card rounded-2xl border border-border/60 p-6`).
3. **Law of Similarity**: Interactive affordances of the same class (all external links, all filter pills) must share identical font-weight, icon style, and hover feedback.

---

## 5. Cognitive Load Optimization

- **Extraneous Load**: Eliminate redundant labels, unnecessary borders, and conflicting accent colors.
- **Intrinsic Load**: Provide contextual tooltips and inline explanations for advanced settings.
- **Germane Load**: Use familiar interaction patterns (Cmd+K command palettes, ESC to close, drag-and-drop handles) to accelerate learning.
