# SIR Portfolio: Fix project names and navbar

## Problem (from owner screenshots and text)
1. "SIR Negm Furniture" should be just "Negm Furniture" (client work, not a SIR product)
2. "SIR Obour Hub" should be "SIR Education Hub" (old name, should not be mentioned)
3. Navbar shows "SP" - should show the logo/project name instead

## Required fixes
1. Find all occurrences of "SIR Negm Furniture" and replace with "Negm Furniture"
2. Find all occurrences of "SIR Obour Hub" and replace with "SIR Education Hub"
3. Navbar: replace "SP" text with logo/icon + "SIR Portfolio" or just the logo
4. Ensure no old project names appear anywhere (check footer, project cards, metadata)

## Files to check
- apps/web/src/components/Navbar.tsx
- apps/web/src/data/projects.ts or similar
- apps/web/src/app/(portfolio)/projects/[slug]/page.tsx
- apps/web/src/components/ProjectCard.tsx
- apps/web/public/ or src/assets/logo.*

## Acceptance
- No "SIR Negm Furniture" anywhere - only "Negm Furniture"
- No "SIR Obour Hub" anywhere - only "SIR Education Hub"
- Navbar shows logo, not "SP"
- All project cards, URLs, metadata updated