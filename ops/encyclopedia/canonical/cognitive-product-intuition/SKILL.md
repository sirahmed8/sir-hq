---
name: cognitive-product-intuition
description: "Use when a UI or flow feels confusing, clone-like, or high-friction and needs checking against human mental models and wizard step order."
---

# Cognitive Product Intuition & Anti-Clone Architecture Protocol

This skill stops AI agents from making lazy, robotic, or nonsensical design decisions. It forces the agent to view software through the eyes of an intelligent, impatient human user.

---

## 1. Eradicate "Clone Syndrome" (Distinct Mental Models)

Never copy-paste an identical layout or card grid across two fundamentally different user tasks:
- **Installer / Setup Wizard**:
  - **Purpose**: A linear, focused, distraction-free sequential funnel.
  - **Mental Model**: Prerequisites Check → Destination Selection → Download/Extraction Progress (bytes/speed/ETA) → Verification → Finish.
  - **Design**: Centered, progress-focused layout, single primary CTA (*"Next"*), and distraction-free framing. NOT an inventory grid.
- **Manager / Inventory Dashboard**:
  - **Purpose**: An exploratory, non-linear organization workspace.
  - **Mental Model**: Search, filter, bulk-actions, status toggles (active/inactive), dependency badges, and sortable table/grid.
  - **Design**: Multi-column data layout with high-density controls and quick-action toolbars.

---

## 2. The Causality & State Sequence Law (Linear Wizards)

When designing step-by-step processes (e.g., Step 1 → Step 2 → Step 3):
- **Future Steps are STRICTLY LOCKED**: Users must **never** be able to click on future steps before completing and validating earlier steps. Stepper numbers or progress bars are read-only visual milestones, NOT arbitrary navigation links.
- **Previous Steps are Revisitable**: Users can click backward to review prior steps, with clear warnings if changing earlier inputs invalidates downstream progress.
- **Active Step Dominance**: Only the currently active step displays actionable inputs and the dominant primary validation button.

---

## 3. The "Human Friction" & Common-Sense Checklist

Scan the user experience for friction points that feel robotic, awkward, or frustrating:
- **Zero Premature Success**: Never display "Done!" or "Completed!" while background disk writes, network downloads, or indexing workers are still active.
- **Confirmation for Destructive Actions**: Purging files, deleting accounts, or resetting configurations must require an explicit confirmation modal with the destructive action styled in high-visibility danger red.
- **No Misleading Clickables**: Any element with hover styling or a pointer cursor must have a real, functioning click handler.
- **Zero Dead-End States**: If an error occurs during an operation, never trap the user. Always provide an explicit "Back", "Retry", or "Cancel" action.
- **Singular Primary CTA**: Never present competing, identically styled primary buttons on the same screen. Exactly one primary constructive action per viewport; all others are secondary or ghost.
