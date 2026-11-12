# ml-best-practices

- Tool: `gemini`
- Category: design
- Source: `C:\Users\a7med\.gemini\skills\ml-best-practices\SKILL.md`
- SKILL.md size: 9805 chars

## What it does

| CRITICAL RULE: You MUST use this skill whenever the task involves any machine learning tasks or data analysis. Use this skill if the user's prompt or requirements mention any of the following: * Clustering * Classification * Regression * Time series forecasting * Statistical testing * Model comparison * ML * Data analysis SQL/BigQuery ML HANDOFF: If the user requires a SQL solution, use this skill to dictate the ANALYSIS STEPS (e.g., markdown analysis cells, visualization logic), but defer to `bigquery` for all SQL syntax.

## Structure (headings inside SKILL.md)

- ML Best Practices
- Clustering:
- Time Series Forecasting:
- Exploratory Data Analysis / Anomaly Detection:
- Classification:
- Regression:
- Comparing ML Models:
- No match:
- Essential ML Practices
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   Prefer to keep data instead of dropping it when possible.
- -   Drop rows that don't match the schema or don't have the target value (if it
- -   Handle missing data. Prefer to keep data instead of dropping it when
- -   Handle missing data. Prefer to keep data instead of dropping it when

## Key rules (verbatim lines from SKILL.md)

1. -   Before applying encoders, check if the dataset already contains pre-encoded
2. -   Prefer to keep data instead of dropping it when possible.
3. -   Always perform a chronological split on the data to create training,
4. -   Identify rows that don't make sense. How many are there and what do they
5. -   Drop rows that don't match the schema or don't have the target value (if it

## Files inside the skill

- (SKILL.md only)
