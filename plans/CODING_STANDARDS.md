# SIR CODING STANDARDS & ARCHITECTURE PLAYBOOK
**Target**: Every Autonomous Engineer & Gemini Chat Across Portfolio Repositories  
**Standard**: Master Directive (`00-master-directive.md`), Quality Bar (`23-premium-code-bar.md`)  
**Scope**: All 17 Projects (`D:\Projects`) · Version: 1.0.0 (Strictly enforced)

---

## 1. Approved Technology Stacks

To prevent framework fragmentation and ensure seamless maintenance across all 17 projects, only approved, modern stacks may be used:

| Tier | Category | Approved Technology | Prohibited Alternatives |
|---|---|---|---|
| **Web Apps** | Framework | Next.js 15 (App Router, React 19) or Vite + React 19 | Pages Router, CRA, Angular, Vue 2 |
| **Desktop Apps** | Native Shell | Tauri v2 (Rust core, web UI) or Electron (only for heavy media/native bindings) | WPF, WinForms, Python Tkinter/PyQt |
| **Mobile Apps** | Cross-Platform | Expo SDK 52 (React Native) or Capacitor PWA | Cordova, Xamarin, Flutter (unless legacy port) |
| **Styling** | Engine | Tailwind CSS v4 + Vanilla CSS Custom Properties | Emotion, styled-components runtime CSS-in-JS |
| **Backend** | Microservices | Node.js (TypeScript) + Fastify / Hono, or FastAPI (Python 3.12) | Express v4 (legacy), Flask, PHP |
| **Database** | Persistence | PostgreSQL (Drizzle ORM / Prisma) or Cloud Firestore; SQLite for desktop | Raw untyped SQL strings, MongoDB |
| **State** | Client Store | Zustand or TanStack Query (React Query) | Redux boilerplate, MobX |
| **Testing** | Suite | Vitest (unit/component) + Playwright (E2E browser smoke tests) | Jest, Mocha, Cypress |

---

## 2. Universal Directory Layout

Every repository must strictly adhere to this standardized directory structure:

```text
<project-root>/
├── .sir/                      # SIR workspace memory, plans, checkpoints
│   ├── CHECKPOINT.md         # Active progress state and next step
│   └── MASTER_PLAN.md        # Comprehensive 25-task blueprint
├── public/                   # Static assets (SVGs, favicon, brand icons)
├── src/
│   ├── app/                  # Next.js App Router routes / pages
│   ├── components/
│   │   ├── ui/               # Primitive design system components (Button, Input, Sheet, Modal)
│   │   └── features/         # Domain-specific composite views
│   ├── hooks/                # Custom React hooks (keyboard, springs, viewport)
│   ├── lib/                  # Utilities, formatters, validation schemas
│   ├── services/             # API client, database connectors, SDK wrappers
│   ├── styles/               # Global tokens, typography, CSS logical property utilities
│   └── types/                # Strict TypeScript interfaces and domain schemas
├── tests/
│   ├── unit/                 # Vitest unit test suites
│   └── e2e/                  # Playwright end-to-end integration specs
├── .env.example              # Plain template with all required keys (no secrets)
├── package.json              # Strict dependencies, locked at version 1.0.0
└── tsconfig.json             # Strict TypeScript configuration
```

---

## 3. Real Animation Recipes & Spring Physics Code

### 3.1. Dynamic Island Spring Physics (CSS & Web Animations API)

Transitions must never feel linear or robotic. All expandable panels, dialogs, sheets, and islands must use the SIR Spring Signature:
- **Damping Ratio**: `0.85` (no oscillating overshoot, clean organic settling)
- **CSS Curve**: `cubic-bezier(0.16, 1, 0.3, 1)` (Apple Dynamic Island standard)
- **Duration**: `380ms` for micro-interactions, `480ms` for full-screen sheets.

#### Production CSS Spring Utility:
```css
/* Dynamic Island Spring Animation Classes */
:root {
  --sir-spring-easing: cubic-bezier(0.16, 1, 0.3, 1);
  --sir-spring-duration-fast: 260ms;
  --sir-spring-duration-normal: 420ms;
  --sir-spring-duration-slow: 540ms;
}

.island-spring {
  transition-property: transform, width, height, border-radius, background-color, box-shadow;
  transition-duration: var(--sir-spring-duration-normal);
  transition-timing-function: var(--sir-spring-easing);
  will-change: transform, width, height;
}

.island-spring-press {
  transform: scale(0.975);
  transition-duration: var(--sir-spring-duration-fast);
}

.sheet-backdrop {
  background: rgba(15, 23, 42, 0.45);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  transition: opacity var(--sir-spring-duration-normal) var(--sir-spring-easing);
}

@media (prefers-reduced-motion: reduce) {
  .island-spring,
  .island-spring-press {
    transition-duration: 0.01ms !important;
    transform: none !important;
    animation: none !important;
  }
}
```

#### Production JavaScript Spring Solver (Vanilla JS / React Hook):
```typescript
// src/hooks/useSpringIsland.ts
import { useEffect, useRef } from 'react';

interface SpringConfig {
  stiffness?: number; // default: 350
  damping?: number;   // default: 32
  mass?: number;      // default: 1
}

export function animateSpring(
  element: HTMLElement,
  from: number,
  to: number,
  onUpdate: (value: number) => void,
  config: SpringConfig = {}
) {
  const { stiffness = 350, damping = 32, mass = 1 } = config;
  let current = from;
  let velocity = 0;
  let animationFrameId: number;

  const step = () => {
    const springForce = -stiffness * (current - to);
    const dampingForce = -damping * velocity;
    const acceleration = (springForce + dampingForce) / mass;

    velocity += acceleration * (1 / 60);
    current += velocity * (1 / 60);

    onUpdate(current);

    if (Math.abs(to - current) > 0.1 || Math.abs(velocity) > 0.1) {
      animationFrameId = requestAnimationFrame(step);
    } else {
      onUpdate(to);
    }
  };

  animationFrameId = requestAnimationFrame(step);
  return () => cancelAnimationFrame(animationFrameId);
}
```

---

## 4. Active-Only Tab Bar Implementation

Inactive tabs MUST display only their monochrome SVG icon. When a tab is activated, it smoothly expands to reveal both its icon and localized title, with zero white-line flicker or layout jump.

```tsx
// src/components/ui/ActiveTabBar.tsx
import React from 'react';

export interface TabItem {
  id: string;
  label: string;
  icon: React.ReactNode;
}

interface ActiveTabBarProps {
  tabs: TabItem[];
  activeTab: string;
  onTabChange: (id: string) => void;
}

export const ActiveTabBar: React.FC<ActiveTabBarProps> = ({ tabs, activeTab, onTabChange }) => {
  return (
    <nav 
      role="tablist"
      aria-label="Navigation"
      className="inline-flex items-center gap-1.5 p-1.5 bg-slate-900/80 backdrop-blur-xl border border-slate-800/80 rounded-full shadow-2xl"
    >
      {tabs.map((tab) => {
        const isActive = activeTab === tab.id;
        return (
          <button
            key={tab.id}
            role="tab"
            aria-selected={isActive}
            tabIndex={isActive ? 0 : -1}
            onClick={() => onTabChange(tab.id)}
            className={`
              relative flex items-center gap-2 px-3 py-2 rounded-full text-xs font-semibold
              transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]
              outline-none focus-visible:ring-2 focus-visible:ring-indigo-500
              ${isActive 
                ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30' 
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'}
            `}
          >
            <span className="w-5 h-5 flex items-center justify-center shrink-0">
              {tab.icon}
            </span>
            <span
              className={`
                overflow-hidden whitespace-nowrap transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]
                ${isActive ? 'max-w-28 opacity-100' : 'max-w-0 opacity-0'}
              `}
            >
              {tab.label}
            </span>
          </button>
        );
      })}
    </nav>
  );
};
```

---

## 5. Mobile Ergonomics & Responsive Formulas (320px to 4K)

1. **Card Container Wrapping**:
   - Every action container inside cards and modals must use `flex-wrap: wrap` and `gap: 0.5rem`.
   - Never use fixed pixel widths on action buttons. Use `min-width: 0; flex: 1 1 auto;` to ensure buttons adapt gracefully on narrow 320px screens without clipping.
2. **Virtual Keyboard Safe Inputs**:
   - To prevent Android and iOS virtual keyboards from displacing bottom sheets or scrolling text inputs out of view, bind the CSS viewport height to `window.visualViewport`:
     ```typescript
     // src/hooks/useVisualViewport.ts
     import { useEffect } from 'react';

     export function useVisualViewport() {
       useEffect(() => {
         const handleResize = () => {
           if (window.visualViewport) {
             document.documentElement.style.setProperty(
               '--vvh',
               `${window.visualViewport.height}px`
             );
           }
         };
         window.visualViewport?.addEventListener('resize', handleResize);
         handleResize();
         return () => window.visualViewport?.removeEventListener('resize', handleResize);
       }, []);
     }
     ```

---

## 6. Strict RTL (Right-to-Left) & Arabic Typography Rules

1. **CSS Logical Properties Only**:
   - **Banned**: `margin-left`, `margin-right`, `padding-left`, `padding-right`, `left`, `right`, `float: left`.
   - **Mandatory**:
     - `margin-inline-start`, `margin-inline-end`
     - `padding-inline-start`, `padding-inline-end`
     - `inset-inline-start`, `inset-inline-end`
     - `border-start-start-radius`, `border-end-end-radius`
     - `text-align: start`, `text-align: end`
2. **Arabic Font Stack & Diacritic Safeguards**:
   - Font Family: `'Alexandria', 'Cairo', system-ui, -apple-system, sans-serif`
   - Arabic text requires a minimum line height of `1.6` (minimum 24px on 15px font) to prevent Arabic diacritics (Harakat: Fatha, Damma, Kasra) and character descenders from being clipped by bounding boxes.
3. **Directional Flipping Logic**:
   - Navigation arrows, back buttons, next buttons, and breadcrumbs MUST flip 180deg when `dir="rtl"`:
     ```css
     [dir="rtl"] .flip-in-rtl {
       transform: scaleX(-1);
     }
     ```
   - Audio/video scrubber bars, volume sliders, telephone numbers, and clocks MUST NOT flip in RTL.

---

## 7. Strict Color Tokens & Zero Yellow Mandate

- **Strict Zero Yellow**: Under no circumstances may an agent generate a yellow button (`bg-yellow-400`, `bg-amber-300`, `#FACC15`) for actions, modals, or primary buttons.
- **Approved Semantic Palette**:
  - `primary`: Brand signature token (Sapphire `#2563EB`, Emerald `#059669`, Indigo `#4F46E5`, Violet `#7C3AED`, Crimson `#DC2626`).
  - `surface`: Slate 900 (`#0F172A`) / Zinc 950 (`#09090B`).
  - `surface-elevated`: Slate 800 (`#1E293B`) / Zinc 900 (`#18181B`).
  - `neutral-border`: Slate 700/60 (`rgba(51, 65, 85, 0.6)`).
  - `success`: Forest Emerald (`#10B981`).
  - `danger`: Ruby Crimson (`#EF4444`).
  - `attention`: Deep Amber Ochre (`#D97706`) - text and warning badge only, **never as a primary button background**.

---

## 8. Background Process Silencing (Windows Standard)

Any background daemon, local worker, or Python automation started by a SIR system on Windows MUST be completely invisible to the user:
```python
# Standard Windows Silent Subprocess Execution
import subprocess

CREATE_NO_WINDOW = 0x08000000

def run_silent(cmd_list):
    return subprocess.run(
        cmd_list,
        creationflags=CREATE_NO_WINDOW,
        capture_output=True,
        text=True
    )
```
Never trigger raw `cmd.exe` or `powershell.exe` windows that flash across Ahmed's desktop.
