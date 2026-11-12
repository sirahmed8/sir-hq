# managing-python-dependencies

- Tool: `claude`
- Category: data
- Source: `C:\Users\a7med\.claude\skills\managing-python-dependencies\SKILL.md`
- SKILL.md size: 2757 chars

## What it does

| Ensures proper Python dependency management, avoiding global `pip install` and adhering to project-specific tooling. Use this skill if any of the following are true: 1. Attempting to run `pip install {package_name}`. 2. Python packages or dependencies need to be added or modified. 3. Initiating a new Python project. 4. Creating a new notebook, even if just using BigQuery cells. 5. Generating Python code that includes `import` statements for third-party libraries. 6. Before executing Python scripts via the terminal to ensure the correct virtual environment is active.

## Structure (headings inside SKILL.md)

- Python Dependency Management Rule
- Dependency Manager Detection
- Default: venv + pip
- Initialize environment
- Add dependencies
- Preserve state
- Prohibited
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. -   Always use `.venv/bin/pip` or `.venv/bin/python` (explicit path).
2. -   After installing, run: `.venv/bin/pip freeze > requirements.txt`.
3. -   **NEVER** run `pip install` globally
4. -   **NEVER** override an existing dependency manager with a different one

## Files inside the skill

- (SKILL.md only)
