# Advanced Fundamental Audit Module

**Version**: 1.0  
**Last Updated**: 03 August 2026  
**Purpose**: Lean, high-signal fundamental analysis framework for Curiosity Stack stock analysis. Designed for rapid audit + deep dive.

---

## 1. Balance Sheet Audit

### Capex & Asset Quality
- **High Capex + High Asset Turnover** → Strong positive signal. Predicts future revenue growth.
- If planned Capex is **2x current Plant & Machinery**, treat as **Must-Read** company (significant capacity expansion underway).
- Check whether new capacity is being utilised or just adding depreciation drag.

### Capital Structure Strength
- **Deleveraging** + **Rising Equity Base** = High quality.
- Preference order for investments on Balance Sheet:
  - Financial Assets < 20% of total assets (preferred)
  - Associates 20–50%
  - Subsidiaries > 50% (higher complexity / lower transparency)

### Working Capital Quality
| Item | Red Flag Threshold | Interpretation |
|------|--------------------|---------------|
| Trade Receivables + Inventory | ≥ 50% of Total Assets | Possible fictitious sales / channel stuffing |
| Cash | Excessively high with near-zero interest income | Capital inefficiency or parked funds |
| Debtor Days | Declining | Positive → better cash conversion |

### Liability Notes
- Preference shares & warrants are **not** pure liabilities (watch conversion risk into equity).
- Contingent liabilities as % of Net Worth must be tracked.

---

## 2. Income Statement Audit

### Core Quality Filters
- **ROE > 15%** preferred (consistent).
- Quick Market Cap check: `PAT × PE ≈ Market Cap` (sanity test).
- **Stable or rising margins** preferred over highly fluctuating ones (cyclicality warning).
- **Rising Gross Margin** → Pricing power signal.

### Operating Leverage
- Sales rising while expenses stay relatively flat = positive operating leverage.
- Volume growth is more important than pure value growth long-term.

### Red Flags in P&L
| Item | Warning |
|------|--------|
| Volatile Depreciation | Possible change in asset life to inflate profits |
| Inventory Gains | Temporary gross profit boost from low RM cost — reverse risk high |
| Repeated Exceptional Losses | Avoid businesses that keep booking these in Other Income |
| Inventory Write-offs | Often indicates prior period fudging |
| Interest Coverage < 7x | Fragile; any shock can become existential |
| Peak Margins + Peak PE | Zone of maximum danger |

### Margin of Safety Criteria
- Reasonable valuation
- Fast earnings growth
- Not currently over-earning due to temporary shortage / one-time factors
- Always analyse profit growth **after removing exceptional items**

---

## 3. Cash Flow Audit

### Quality of Earnings
- **CFO rising** because of:
  - Falling Debtor Days
  - Falling Inventory Days
  - Rising Payable Days
- Exception: Realty & NBFCs (different working capital dynamics).

### Cash Conversion
- **CFO / EBITDA > 70%** is healthy (especially strong in B2C).
- Asset-light models naturally generate higher Free Cash Flow.

### Cash Flow Statement Mapping
| Section | What to Track |
|---------|---------------|
| **CFO** | Core operating cash generation |
| **CFI** | Capex + Investments (growth vs waste) |
| **CFF** | Funding pattern (debt vs equity) |

- Acquisitions appear in Investing activities.

---

## 4. Corporate Actions & Governance Audit

### High Priority Red Flags
- Capex rising but **Employee Cost not rising** → Possible fraud / misreporting.
- **Auditor resignation before completion of term** → Major red flag.
- Company issuing **warrants** that later convert into promoter equity → Track closely.
- Promoter selling after never having sold before → Possible peak signal.
- Company stops holding **concalls after bad results** → Governance concern.

### Positive Signals
- Promoter buying (check insider trade disclosures).
- Consistent auditor.
- Transparent guidance and regular investor communication.

### Search Keywords for Quick Scan
`Ace Investors`, `sector`, `guidance`, `capex`, `resign`, `warrant`, `related party`, `contingent`

---

## 5. Company Nature Classification

| Type | Characteristics | Action Bias |
|------|------------------|-----------|
| **Fast Growing** | Revenue / PAT growth > 15% sustained | Prefer growth at reasonable price |
| **Secular** | Long-term uptrend in earnings + consistent OPM/GPM | Core holding candidates |
| **Cyclical** | Earnings & margins swing with cycle | Buy at support P/B, sell at resistance P/B |
| **Commodity** | Highly price-sensitive | Avoid when commodity prices are at all-time highs |

---

## 6. Annual Report Deep-Dive Checklist

Must-read sections in order of priority:

1. **MD & CEO Message** – Tone, honesty, forward visibility
2. **Management Discussion & Analysis (MDA)**
3. **Segmental Performance** + Revenue Bifurcation
4. **Future Plans / Capex Guidance**
5. **Board of Directors** quality & independence
6. **Key Audit Matters**
7. **Related Party Transactions (RPT)**
8. **Contingent Liabilities** as % of Net Worth
9. **Remuneration as % of PAT**
10. **Milestones & Customer Concentration**
11. **Consolidated vs Standalone** differences
12. **Auditor’s Report** (qualifications / emphasis of matter)

**Connecting the Dots Rule**: Always cross-link Balance Sheet changes → P&L impact → Cash Flow reality → Management commentary.

---

## 7. Quick Audit Scorecard (Use for every stock)

| Category                    | Score (1–5) | Notes |
|----------------------------|-------------|-------|
| Balance Sheet Strength     |             |       |
| Earnings Quality           |             |       |
| Cash Conversion            |             |       |
| Governance & Transparency  |             |       |
| Growth Visibility          |             |       |
| Valuation Margin of Safety |             |       |
| **Overall Conviction**     |             |       |

**Scoring Guide**:
- 5 = Excellent / Clean
- 3 = Acceptable with monitoring
- 1 = Major red flags present

---

## 8. Usage Protocol (Curiosity Stack)

When analysing any stock:

1. Run this module first (Balance Sheet → P&L → Cash Flow → Governance).
2. Flag all red items immediately.
3. Only then proceed to sector, order book, and valuation work.
4. Update conviction tag in `watchlist.md` based on audit score.

**File Location**: `library/advanced-fundamental-audit.md`  
**Callable via**: Library reference or direct audit request on any ticker.
