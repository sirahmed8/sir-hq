# building-data-apps

- Tool: `gemini`
- Category: design
- Source: `C:\Users\a7med\.gemini\skills\building-data-apps\SKILL.md`
- SKILL.md size: 6317 chars

## What it does

| Build modern data apps, dashboards, and interactive reports using either React + Vite or Streamlit. Includes optional Gemini Data Analytics chat integration for an AI powered "chat with your data" experience. Relevant when any of the following conditions are true: 1. User explicitly requests to build a data dashboard, data application, or visualization UI, and the UI pulls data from a GCP database (defaulting to BigQuery unless otherwise specified). 2. You need to generate a frontend web application to interact with, query, and visualize data from GCP data sources. 3. User wants to build a "chat with your data" experience or integrate the Gemini Data Analytics chat API into a web interface. Do NOT use when any of the following conditions are true: 1. The request is for building backend-only services. 2. The request is for simple CLI scripts or command-line applications. 3. The web application is not data-centric or does not involve visualizing/querying data from GCP sources.

## Structure (headings inside SKILL.md)

- Building Data Applications
- Step 0: Framework Selection
- Choice: Streamlit
- Choice: React + Vite
- Guidance:
- Step 1: Implementation Plan
- Shared Design Standards
- Framework Implementation
- If using Streamlit:
- If using React + Vite:
- AI Chat Interface (Optional Feature)
- Acceptance Criteria
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   **Default to React + Vite** for production-grade applications that require
- -   [ ] Do z-indexes stack correctly so dropdowns appear above table headers?

## Key rules (verbatim lines from SKILL.md)

1. -   **Check for existing stack first**: ALWAYS prefer the framework the user is
2. -   **Default to React + Vite** for production-grade applications that require
3. 1.  **Gather Technical Details**: You MUST read `references/chat_integration.md`

## Files inside the skill

- `examples/express_chat.ts`
- `examples/fastapi_chat.py`
- `examples/react_chat_panel.jsx`
- `references/chat_integration.md` — "Gemini Data Analytics Chat Integration"
- `references/react_framework.md` — "Building with React + Vite"
- `references/shared_design_system.md` — "Unified Data App Design System"
- `references/streamlit_framework.md` — "Building with Streamlit"
- `resources/chat_integration.md` — "Gemini Data Analytics Chat Integration"
- `resources/react_framework.md` — "Building with React + Vite"
- `resources/shared_design_system.md` — "Unified Data App Design System"
- `resources/streamlit_framework.md` — "Building with Streamlit"
