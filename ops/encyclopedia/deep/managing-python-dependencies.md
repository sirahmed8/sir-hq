# managing-python-dependencies (claude+gemini)

Source read: `C:\Users\a7med\.claude\skills\managing-python-dependencies\SKILL.md` (2.8 KB; claude and gemini listed; claude copy chosen).

## Summary
A guardrail rule for Python dependency management: before ANY `pip install`, detect the project's existing dependency manager in strict priority order — uv (`uv.lock` or `[tool.uv]` in pyproject.toml → `uv add`/`uv sync`), Poetry (`[tool.poetry]` → `poetry add`/`install`), Pipenv (`Pipfile` → `pipenv install`), Conda (`environment.yml` → `conda install`/`env create`), then venv+pip (`requirements.txt` only or nothing → `.venv/bin/pip`). Default when no manager exists: create `.venv`, always invoke `.venv/bin/pip`/`.venv/bin/python` by explicit path, and after installs run `.venv/bin/pip freeze > requirements.txt`. Triggers include pip installs, dependency changes, new projects, notebooks, code with third-party imports, and before running Python scripts.

## When to use / when NOT
Use whenever a Python package might be installed or a Python project/script is touched. Do NOT use to override an established project toolchain, and never for non-Python ecosystems.

## Inputs, outputs, tools
- Inputs: workspace files (lockfiles, pyproject, Pipfile, environment.yml, requirements.txt).
- Outputs: packages installed via the correct manager; updated lockfile/requirements.txt.
- Tools: uv, Poetry, Pipenv, Conda, or venv+pip — whichever the project already uses.

## 5 most important rules
1. Detect the dependency manager BEFORE installing anything; detection order is fixed (uv → Poetry → Pipenv → Conda → venv+pip).
2. NEVER run global `pip install`.
3. NEVER override an existing manager with a different one.
4. Default is venv + pip + requirements.txt with explicit `.venv/bin/` paths.
5. After installing, freeze state into `requirements.txt`; on setup, install from it.

## Risks / owner notes
Global installs pollute the machine and break reproducibility; wrong-manager installs create conflicting lockfiles. Low risk, high-frequency rule.

## Category and tags
Category: build. Tags: python, dependencies, uv, poetry, pipenv, conda, venv, reproducibility.
