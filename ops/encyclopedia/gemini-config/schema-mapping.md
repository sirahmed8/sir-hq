# schema-mapping

- Tool: `gemini-config`
- Category: data
- Source: `C:\Users\a7med\.gemini\config\skills\schema-mapping\SKILL.md`
- SKILL.md size: 11780 chars

## What it does

Guides the process of analyzing, mapping, and documenting transformations between source and target schemas for any database, data warehouse, or data platform. Focuses exclusively on creating a high-fidelity mapping plan (Mapping Manifesto). Used when initiating an ETL, ELT, or data integration task with schema mapping specification for multiple tables (i.e. more than 3 tables) before writing code. Do NOT use this skill for basic SQL generation without mapping requirements, or when the user already has a complete mapping specification.

## When to use (from skill text)

- you MUST use this plan and replace the existing generic plan.
- Use this skill when:

## Structure (headings inside SKILL.md)

- Skill: Semantic Schema Mapping Planning
- When to Use
- Required Input Variables
- Optional Input Variables
- The Schema Mapping Planning Procedure
- Step 1: Semantic & Terminology Translation
- Step 2: Establish the Anchor Table
- Step 3: Proactive Data Sampling & Inspection
- Step 4: Perform Field-Level Gap Analysis & Cleanliness Design
- Step 5: Map Relationships & Joins
- Step 6: Draft the "Mapping Manifesto" (Output Format & Example)
- Mapping Plan: `album`
- Field Mappings
- Critical Operational Rules

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   Many-to-many risks or potential duplicate generation.
- * `cd` JOIN `band` ON `cd.artist = band.name`
- * `band` JOIN `style` ON `band.style = style.id`

## Key rules (verbatim lines from SKILL.md)

1. 3.  **Verify Domain Semantics**: Do not rely purely on lexical matching (name
2. *   **Derived Mapping**: Requires type casting, string manipulation, date
3. *   **Joined Mapping**: Requires looking up values from contributing tables
4. *   **Aggregated Mapping**: Requires collapsing 1-to-many relationships (e.g.,
5. *   **Gaps (Unmapped fields)**: Target fields that do not exist in the source.

## Files inside the skill

- (SKILL.md only)
