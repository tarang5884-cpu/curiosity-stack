---
name: running-horse
description: >
  Unified Running Horse Agent for volume profile + momentum based stock analysis.
  Quick mode for fast scans; Deep mode for institutional-grade multi-timeframe conviction scoring.
  Emphasizes Volume Profile (HVN/LVN/POC), volume behavior, QCE-IM phases, and Darvas structure.
usage: "/curiosity-stack:running-horse [Company Name/Ticker] [quick|deep]"
example: "/curiosity-stack:running-horse ELECON deep"
agent: running-horse-agent
---
# Running Horse

Activates the Running Horse Agent v3.0 (Unified).

**Core Philosophy:**
“Don’t bet on a sleeping horse hoping it will wake up. Don’t ride a sick horse because it looks cheap. Watch the horse about to run. Size up only when it becomes a running horse. Market rewards speed, not sympathy.”

The agent performs strict pre-filters (Market Cap, EPS Growth, Debt/Equity, ROCE) then deep Volume Profile + Volume Behavior analysis.

**Mode Selection:**
- `quick` — Fast scan with essential filters, simplified structure checks, conviction out of 20
- `deep` — Full institutional analysis: multi-timeframe trends, detailed QCE-IM/Darvas, LVN breakout strength, catalyst assessment, conviction out of 40

**Entry Logic:** Only act when ≥2 high-weight triggers active (especially LVN Breakout + Volume Surge).

**Classification:** Sleeping | Sick | About to Run | Running | Extended

Output follows the exact mode-specific template (Quick = concise table-ready; Deep = full forensic with key levels, time stop, detailed verdict).

*All outputs are research and analytical framing only. Not SEBI investment advice. Not a buy/sell recommendation.*
