---
name: india-vcp-scan
description: >
  Daily India VCP Factory scan. Regime first, then grade VCP / pocket pivot /
  DEP setups on CSK pass list + locked watchlist. Actionable max 4 names.
usage: "/curiosity-stack:india-vcp-scan"
example: "/curiosity-stack:india-vcp-scan"
agent: india-vcp-factory-agent
---
# India VCP Factory — Daily Scan

Run `library/india-vcp-factory-v1.md` exactly.

### Order of work
1. Regime Gate (Nifty, Midcap100, Smallcap100 vs 50-DMA; distribution days; FII index-futures net). If risk-off → print regime + do-nothing and stop.
2. Take CSK pass list (max 25) + watchlist Tier 1–3. Do not rescreen all of NSE unless the user says `full`.
3. NSE filing first on any name ±3% or volume ≥2× ADV.
4. Grade each survivor: WAIT / PP TODAY / VCP TRIGGER / DEP FLAG / EXTENDED / REJECT.
5. Volume Profile one-liner (HVN support vs overhead).
6. Delivery vs 20-day median on the last green session.
7. Print Actionable only if trigger + regime permission + stop ≤ 8%.

### Output
**India VCP Factory | [Date] | Regime:**

1. Regime card
2. Factory Watch table (max 12)
3. Actionable (max 4) with entry / stop / add / invalidation
4. Rejects
5. Open-book actions
6. Do-nothing line if empty

≤ 450 words after tables. Research framing only. Not SEBI advice.

Generate today’s scan now if market data is available; otherwise print the blank template and the screen query.
