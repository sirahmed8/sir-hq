# building-data-apps

Tools: gemini (antigravity). Source: C:\Users\a7med\.gemini\skills\building-data-apps\SKILL.md (read in full) + examples(3) + references(4) + resources(4) (read in full)

## Summary
Build data dashboards and interactive reports in React + Vite or Streamlit for GCP/BigQuery data, with optional Gemini Data Analytics chat (SSE streaming, thought/content segregation, multi-turn). Shared design system: minimal chrome, zinc palette, card layouts, DM Sans + JetBrains Mono, blue accent.

## When to use / not use
Use for data dashboards, reports, or chat-with-data over GCP (BigQuery default). NOT for backend-only services, CLI scripts, or non-data-centric apps.

## Inputs, outputs, dependencies
Input: data source (BigQuery), framework choice, optional chat. Output: frontend app (React/Vite or Streamlit) plus a backend API for chat. Needs: Node/Vite/Tailwind/ECharts (React) or streamlit/plotly/pandas (Streamlit); Gemini Data Analytics API for chat.

## Key rules
1. Select framework by user profile: Streamlit for Python/data scientists/single-script; React + Vite default for production/complex UI; prefer an existing stack in the project.
2. Follow the shared design system: zinc palette, card-based layout, DM Sans/JetBrains Mono, generous padding; hide framework chrome.
3. React: Tailwind dark mode, lucide-react, date-fns, axios, ECharts, @dnd-kit; sticky headers, icon-only pagination, selection state, sparkline bars.
4. Streamlit: st.set_page_config first, theme toggle in session_state, inject CSS with IS_DARK f-strings, HTML tables instead of st.dataframe, Plotly with PLOT_LAYOUT, displayModeBar False.
5. Chat only if explicitly requested: SSE backend, inline_context must include datasource_references (else 400 REFERENCES_NOT_SET), stream THOUGHT vs FINAL_RESPONSE, SUGGESTIONs, multi-turn history, react-markdown + remark-gfm.
6. Verify with browser tests before declaring done; check hover transitions, date formatting, z-index dropdowns, loading/disabled states, responsiveness, API errors, dark mode, chart rendering.

## Risks / owner items
- Chat requires the Gemini Data Analytics API enabled and BigQuery data; BigLake/Iceberg tables are unsupported.
- 400 if datasource_references is missing; add robust try-catch around SSE streams.
- ReactMarkdown v10+: put className on the parent div, not the component, to avoid crashes.
- Acceptance checklist must be verified, not assumed.

## Category and tags
data, dashboard, react, streamlit, bigquery, gemini, chat, build.

## Revision note
Single gemini revision; SKILL.md, examples(3), references(4), resources(4) read in full.
