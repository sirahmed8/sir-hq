# ml-best-practices (gemini)

Source read: `C:\Users\a7med\.gemini\skills\ml-best-practices\SKILL.md` (9.8 KB; gemini CLI skills; gemini listed). CRITICAL-usage skill for ML/data-analysis tasks.

## Summary
Notebook-first ML methodology for clustering, time-series forecasting, EDA/anomaly detection, classification, regression, and model comparison. Universal doctrine: "read a story about the data" — every code cell is followed by a markdown analysis cell, and the notebook ends with a summary that comprehensively answers the prompt; adapt the matching example plan when one fits. Per-task pipelines: clustering (schema understanding → feature histograms/scatterplots → timestamp dates → prefer existing pre-encoded features → keep data over dropping → ordinal/one-hot encoders → standardize → silhouette-score sweep → PCA 2D scatter by cluster and by discrete feature → text description of clusters); forecasting (chronological split ONLY, seasonality, stationarity tests, two models, validation metrics, retrain on test+validation); classification/regression (schema sanity rows, missing-target rows, leakage check in regression, encoders, multiple models, over/underfit response, confusion matrices, actual-vs-predicted plots); comparison (align metrics to business cost of FP/FN). SQL/BigQuery tasks defer syntax to the `bigquery` skill while this dictates analysis steps.

## When to use / when NOT
Use for ANY ML or data-analysis task, especially notebook deliverables. Not for pure SQL writing (bigquery skill) or non-ML data wrangling.

## Inputs, outputs, tools
- Inputs: dataset + analysis question; BigQuery context when applicable.
- Outputs: notebook with code+markdown pairs ending in a comprehensive-answer summary cell.
- Tools: pandas/sklearn-style workflow (encoders, standardization, PCA, silhouette), matplotlib visuals, chronological splits; BigQuery ML handoff for SQL.

## 5 most important rules
1. Every code cell MUST be followed by a markdown analysis cell; end with a summary answering the prompt.
2. Time series: chronological split only — never random.
3. Prefer keeping data and existing pre-encoded features; ordinal→ordinal encoder, nominal→one-hot, restrict high-cardinality categoricals in regression.
4. Standardize numerical features; sweep parameters (e.g., cluster count via silhouette).
5. Match metrics to business cost (FP vs FN) when comparing models; address overfitting with regularization, underfitting with features.

## Risks / owner notes
Notebook outputs must not fabricate results — analysis cells must reflect real computed output. Group leakage is called out only for regression; apply the same skepticism elsewhere.

## Category and tags
Category: data. Tags: machine-learning, notebook, clustering, forecasting, classification, regression, bigquery, eda.
