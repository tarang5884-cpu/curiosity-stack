---
name: stock-scanner

description: >
  Criteria-based intelligent stock scanner.
  Matches stocks to multi-filter requests (sector + growth + price action + technicals + fundamentals).
  Ranks best matches, outputs clean structured table with next-step suggestions.
  Ideal for daily scans, sector themes, momentum filters, and refining watchlists.

usage: "/curiosity-stack:stock-scanner [natural language criteria]"
example: "/curiosity-stack:stock-scanner defence stocks up more than 5% in last 5 days with strong order book"
agent: stock-scanner-criteria-matcher
---

# Stock Scanner

Activates the **Stock Scanner & Criteria Matcher Loop** v1.0.

**Purpose:**
Quickly filter and rank stocks that best match your exact criteria — whether simple ("power sector stocks up today") or complex ("midcap transformers with >20% QoQ profit growth, low debt, and consolidating above 50 DMA").

**How it works:**
- Parses your criteria into structured filters
- Conceptually scans for best conceptual + data-supported matches (5-10 stocks)
- Ranks by overall fit (Best Match first)
- Delivers in strict table + summary format
- Offers optional deep-dive next steps (fundamental analysis, technical setup, refine filters)

**Best used for:**
- Daily/periodic master framework scans
- Sector tailwind hunting (power, defence, infra, electronics, HVDC, BESS)
- Momentum / pullback entry shortlisting
- Watchlist refinement before Running Horse deep analysis
- Combining with high-RS strategy and core-satellite portfolio rules

*All outputs are research and analytical framing only. Not SEBI investment advice. Not a buy/sell recommendation.*

**Status:** Ready. Embedded in Curiosity Stack.