# stock-analysis (codex/cursor/kilo/opencode/windsurf copies)

## Summary
stock-analysis is a SIR-authored equity-research skill covering the full analysis stack in one document: technical indicators (RSI, MACD, Bollinger Bands, moving averages), fundamental valuation (P/E, PEG, ROIC, debt-to-equity), earnings-call transcript deconstruction, and risk-adjusted return profiling (Sharpe, Beta, Alpha). It is methodology text that tells the agent how to structure a stock research report: gather price data and filings, compute the indicators, deconstruct earnings calls for guidance vs. reality, and end with a risk-adjusted verdict rather than a price target guess. No live market-data API is bundled; the agent must supply data via web search, yfinance-style fetches or documents the user provides.

## When to use / when NOT
Use when the owner asks to analyze a stock, compare companies, evaluate an earnings report, or build an investment thesis. Do NOT use it for placing trades (it produces research, not orders), for crypto (different data model), or when no reliable price/filing data can be obtained — say so rather than inventing numbers.

## Inputs, outputs, tools
- Inputs: ticker(s) or company names, optionally a time window, plus whatever market data the agent can fetch (prices, filings, transcripts) via web search/fetch tools.
- Outputs: a structured research write-up: technical snapshot, fundamental metrics, earnings deconstruction, risk metrics, and a clearly-hedged conclusion.
- Tools: web search/fetch for quotes, filings and transcripts; Python (pandas/yfinance if installed) for indicator math. No dedicated MCP in the skill itself.

## 5 most important rules
1. Never invent prices, ratios or transcript quotes; every number must trace to a fetched source or be marked unavailable.
2. Separate technicals (momentum/mean-reversion signals) from fundamentals (valuation, quality, leverage) and say which is driving the view.
3. Earnings deconstruction means comparing what management SAID vs. what the numbers SHOW, including guidance changes.
4. Risk-adjust it: report Sharpe/Beta-style context and downside scenarios, not just upside.
5. End with a falsifiable view (what would change the thesis) rather than a bare buy/sell label.

## Risks / things needing the owner
Financial advice risk: outputs must carry the disclaimer that this is research, not licensed advice, and SIR rules forbid invented figures. Market data access may need paid APIs the owner has not approved; free sources lag and can be stale, which must be disclosed. Delayed quotes must never be presented as real-time.

## Category / tags
business · stocks, equity-research, valuation, technical-analysis, finance

## Revisions
Five copies exist (codex, kilo, cursor, windsurf, opencode; no claude copy). They are the same document with only frontmatter description wording differing. Best revision: the codex copy (used here); content is identical across the five.
