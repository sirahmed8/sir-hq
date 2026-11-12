# notebook-guidance

- Tool: `gemini`
- Category: design
- Source: `C:\Users\a7med\.gemini\skills\notebook-guidance\SKILL.md`
- SKILL.md size: 15080 chars

## What it does

|- This skill guides the use of Jupyter notebooks for data analysis, exploration, and visualization, particularly with BigQuery. It outlines best practices for notebook execution and validation (supporting both cell-by-cell execution and full notebook generation depending on tool availability), library installation, and structuring notebooks for clarity. It also covers specific rules for data cleaning, plotting, and integrating with BigQuery SQL and machine learning workflows. Relevant when any of the following conditions are true: 1. The user request involves a data analysis, data exploration, data visualization, or data insights task that requires multiple steps, queries, or visualizations to answer. 2. The user explicitly requests a notebook (.ipynb). 3. You are creating, editing, or executing cells in a Jupyter notebook. 4. You need to query BigQuery from within a notebook. DO NOT use the Python BigQuery client library; instead, you MUST use the `%%bqsql` magics explained in this skill.

## Structure (headings inside SKILL.md)

- Notebook Guidance
- When to Use a Notebook
- Notebook Best Practices
- Kernel & Environment Management
- Kernel Types
- No Active Kernel / Setup Check
- Proper Library Installation
- Data Analysis & Visualization Rules
- Notebook Layout
- Plotting Rules
- Data Cleaning Rules
- Specialized Notebook Guidance
- 1. BigQuery in Notebooks
- Initialize BigFrames and load %%bqsql magics
- 2. Machine Learning in Notebooks
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2.  You MUST NOT drop columns unless absolutely necessary. Dropping columns is

## Key rules (verbatim lines from SKILL.md)

1. *   📝 **Simple Fact/Status**: The request only requires a single number (e.g.,
2. 3.  **CLEAN FINAL STATE**: The final notebook MUST NOT have failed cells. If a
3. 5.  **GENERATE VISUALIZATIONS**: Always accompany data insights with
4. *   **Check first (REQUIRED)**: Before writing any `%pip install` cell, run
5. *   MUST NOT add Python code to the summary.

## Files inside the skill

- (SKILL.md only)
