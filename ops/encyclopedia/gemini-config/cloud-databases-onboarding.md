# cloud-databases-onboarding

- Tool: `gemini-config`
- Category: data
- Source: `C:\Users\a7med\.gemini\config\skills\cloud-databases-onboarding\SKILL.md`
- SKILL.md size: 4804 chars

## What it does

Guides users through discovering their database requirements, recommends a Google Cloud database product or migration destination based on a recommendation matrix, and assists in database creation. Use when a user asks 'What database service should I use?', 'Help me pick a database', asks which Google Cloud database to migrate or onboard a workload to, or wants to create a new database on Google Cloud. Don't use for general Google Cloud maintenance, managing existing databases, or troubleshooting active Database Migration Service (DMS) jobs.

## Structure (headings inside SKILL.md)

- Google Cloud Database Onboarding Skill
- Progressive Disclosure
- Workflow & Just-in-Time (JiT) Instructions
- Phase 1: Requirement Discovery & Information Gathering
- Phase 2: Recommendation Analysis & Matrix Consultation
- Phase 3: Implementation & Provisioning (Plan-Validate-Execute Pattern)
- Supporting Resources & Documentation

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   [Google Cloud Databases Overview](https://cloud.google.com/products/databases)

## Key rules (verbatim lines from SKILL.md)

1. *   **Reading / Progressive Disclosure:** When interacting with a user during a
2. 1.  **Load Discovery Instructions (JiT):** Read the complete contents of
3. 2.  **Execute Discovery:** Optionally check `get_active_gcp_connection` and

## Files inside the skill

- `OWNERS`
- `references/onboarding_prompts.md` — "Database onboarding agent instructions"
- `references/recommendation_matrix.txt` — "Recommendation Matrix for Database Migrations to Google Cloud"
