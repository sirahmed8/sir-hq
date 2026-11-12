# financial-analysis

## Summary
A compact finance reference: the three-statement architecture (P&L → EBITDA → net income; balance-sheet identity Assets = Liabilities + Equity with current/quick ratios; cash-flow statement with FCF = OCF − CapEx), SaaS unit-economics formulas with healthy benchmarks (LTV = ARPU×GM/churn ≥3×CAC, CAC payback ≤12 months, LTV/CAC 3–5×, NRR ≥110%, runway ≥18 months), and valuation methods (DCF with WACC and terminal value, EV/Revenue, EV/EBITDA, P/E, precedent transactions).

## When to use / when NOT
Use when a task needs corporate financial modeling, statement deconstruction, unit economics, burn/runway math, or valuation multiples — typically for business analysis of the owner's products (e.g. SIR income model) or coursework. Do NOT use as investment advice or for audited-grade reporting; it is a formula/benchmark sheet, not a data source.

## Inputs, outputs, tools
- Inputs: financial figures (revenue, COGS, opex, cash balances, churn, S&M spend, customer counts) or a request to compute specific metrics.
- Outputs: computed metrics, ratios, DCF/valuation estimates, benchmark comparisons — as analysis text or a model (pairs naturally with excel-generator for the workbook).
- Tools: none — pure reasoning/math; optionally python/openpyxl or a spreadsheet for the model itself.

## 5 most important rules
1. Keep the statement identities straight: Gross Profit = Revenue − COGS; EBIT = Gross Profit − OPEX; EBITDA = EBIT + D&A; Net Income = EBIT − Interest − Taxes.
2. Balance sheet must balance: Assets = Liabilities + Equity; working capital and current/quick ratios measured against current liabilities.
3. FCF = Operating Cash Flow − CapEx; distinguish OCF/ICF/FCF financing flows before quoting "cash flow".
4. Use the SaaS benchmarks as gates: LTV ≥ 3× CAC, payback ≤ 12 months, LTV/CAC 3–5×, NRR ≥ 110%, runway ≥ 18 months.
5. DCF discounts FCF_t at (1+WACC)^t plus terminal value; cross-check with comparable multiples (EV/Revenue, EV/EBITDA, P/E) and precedent transactions rather than a single method.

## Risks / owner needs
None technical. Caveat: benchmarks are rules of thumb, not guarantees; real valuations need real data — never invent figures (matches workspace truth rule).

## Category and tags
Category: business. Tags: finance, unit-economics, saas, valuation, dcf, modeling.

## Revisions
Identical content across codex, cursor, kilo, opencode, windsurf (kilo digest confirms byte-identical to codex). Any copy equivalent; kilo used.
