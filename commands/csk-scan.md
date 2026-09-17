---
name: csk-scan
description: >
  One daily CSK scan. Short-term momentum screener + NSE filing first + spike-DMA + watchlist overlay.
usage: "/curiosity-stack:csk-scan"
example: "/curiosity-stack:csk-scan"
---

# CSK One Daily Scan

Read and obey `library/csk-momentum-scan.md`.
Also apply `library/nse-filing-first.md` and `library/spike-dma-base-rule.md`.
Locked names: `watchlist.md`.

Screen (all must hold):

- Close > 20-DMA
- 20-DMA > 50-DMA
- Distance from 52-week high < 15%
- Default mcap > ₹2,000 Cr (watchlist / SME-core exempt → appendix only)
- Sort by last-3-month return descending

Then filing tag, tape tag, watchlist overlay, 8-slot only if BASE READY or MOS.

Generate today's scan now for the latest completed NSE session.
