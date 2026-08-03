# Advanced Fundamental Audit Module

**Version**: 1.1  
**Last Updated**: 03 August 2026  
**Purpose**: Lean, high-signal fundamental analysis framework for Curiosity Stack stock analysis. Includes automated scoring algorithm for consistent conviction tagging.

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

## 7. Automated Scoring Algorithm (v1.1)

### Scoring Categories & Weights

| Category                      | Weight | Max Score |
|-------------------------------|--------|-----------|
| 1. Balance Sheet Strength     | 20%    | 20        |
| 2. Earnings Quality           | 25%    | 25        |
| 3. Cash Conversion            | 15%    | 15        |
| 4. Governance & Transparency  | 15%    | 15        |
| 5. Growth Visibility          | 15%    | 15        |
| 6. Valuation Margin of Safety | 10%    | 10        |
| **Total**                     | 100%   | **100**   |

---

### Detailed Scoring Rules

#### 1. Balance Sheet Strength (Max 20)

| Criterion                              | Score | Condition |
|----------------------------------------|-------|-----------|
| Capex + Asset Turnover strong          | +5    | High Capex with rising asset turnover |
| Capex ≥ 2× Plant & Machinery           | +3    | Significant expansion (Must-Read flag) |
| Deleveraging + Rising Equity           | +4    | Clear reduction in debt / equity growth |
| Receivables + Inventory < 35% of Assets| +4    | Clean working capital |
| Receivables + Inventory 35–50%         | +1    | Acceptable |
| Receivables + Inventory ≥ 50%          | –5    | Red flag (possible fictitious sales) |
| Excess idle cash (no interest income)  | –3    | Capital inefficiency |
| Contingent Liabilities > 25% of NW     | –3    | Material risk |

#### 2. Earnings Quality (Max 25)

| Criterion                              | Score | Condition |
|----------------------------------------|-------|-----------|
| ROE ≥ 18% (consistent 3 yrs)           | +6    | High quality |
| ROE 15–18%                             | +4    | Acceptable |
| ROE < 12%                              | –3    | Weak |
| Stable / Rising Gross Margin           | +5    | Pricing power |
| Highly volatile margins                | –4    | Cyclicality / manipulation risk |
| Interest Coverage ≥ 10x                | +4    | Strong |
| Interest Coverage 7–10x                | +2    | Acceptable |
| Interest Coverage < 7x                 | –5    | Fragile |
| No repeated exceptional losses         | +3    | Clean |
| Repeated exceptional items / write-offs| –6    | Major red flag |
| Volatile Depreciation policy           | –4    | Earnings management risk |

#### 3. Cash Conversion (Max 15)

| Criterion                              | Score | Condition |
|----------------------------------------|-------|-----------|
| CFO / EBITDA ≥ 80%                     | +6    | Excellent conversion |
| CFO / EBITDA 70–80%                    | +4    | Healthy |
| CFO / EBITDA 50–70%                    | +2    | Average |
| CFO / EBITDA < 50%                     | –4    | Poor quality of earnings |
| Declining Debtor + Inventory Days      | +4    | Improving cash cycle |
| Rising Payable Days (reasonable)       | +2    | Positive |
| Negative Working Capital (B2C style)   | +3    | Strong |

#### 4. Governance & Transparency (Max 15)

| Criterion                              | Score | Condition |
|----------------------------------------|-------|-----------|
| Consistent auditor + clean report      | +4    | Good |
| Auditor resignation mid-term           | –8    | Severe red flag |
| Regular concalls even after weak results| +3   | Transparent |
| Stopped concalls after bad results     | –5    | Governance concern |
| Promoter buying                        | +3    | Alignment |
| First-time promoter selling            | –4    | Peak signal risk |
| Warrants converting to promoter equity | –3    | Monitor closely |
| Capex rising but employee cost flat    | –6    | Possible misreporting |

#### 5. Growth Visibility (Max 15)

| Criterion                              | Score | Condition |
|----------------------------------------|-------|-----------|
| Revenue / PAT growth > 20% sustained   | +6    | Fast growth |
| Growth 15–20%                          | +4    | Solid |
| Growth 10–15%                          | +2    | Moderate |
| Growth < 10% or declining              | –3    | Weak |
| Clear volume-led growth                | +3    | Higher quality |
| Only value-led growth                  | +1    | Lower quality |
| Visible order book / capacity ramp     | +4    | Forward visibility |
| Peak margins + Peak valuation          | –5    | Danger zone |

#### 6. Valuation Margin of Safety (Max 10)

| Criterion                              | Score | Condition |
|----------------------------------------|-------|-----------|
| Trading at significant discount to intrinsic| +5 | Strong MOS |
| Reasonable valuation vs growth         | +3    | Fair |
| Expensive but growth supports          | +1    | Limited MOS |
| Peak margins + Peak PE                 | –4    | High risk |
| Clear over-earning due to temporary factors| –3 | Margin of safety low |

---

### Final Score Interpretation

| Total Score | Conviction Tag | Action Guidance |
|-------------|----------------|-----------------|
| **85 – 100** | 8.5 – 9.5     | High Conviction – Core / Aggressive tracking |
| **70 – 84**  | 7.0 – 8.4     | Strong – Suitable for Tier 1 / high allocation |
| **55 – 69**  | 6.0 – 6.9     | Acceptable – Tier 2 / Monitor |
| **40 – 54**  | 5.0 – 5.9     | Weak – Speculative / Low allocation |
| **Below 40** | < 5.0         | Avoid or Deep stress-test required |

### Hard Disqualification Rules (Override Score)
Any of the following automatically caps maximum score at **45** (or forces Avoid):
- Auditor resignation before term completion
- Receivables + Inventory ≥ 50% of Total Assets with no credible explanation
- Repeated exceptional losses / inventory write-offs across years
- Capex rising sharply while employee cost remains flat (suspected misreporting)
- Interest Coverage consistently < 5x

---

## 8. Usage Protocol (Curiosity Stack)

When analysing any stock:

1. Run this module first (Balance Sheet → P&L → Cash Flow → Governance).
2. Apply the **Automated Scoring Algorithm** and calculate total score.
3. Flag all red items immediately.
4. Apply Hard Disqualification Rules if triggered.
5. Map final score to Conviction Tag (see table above).
6. Update `watchlist.md` with the new conviction score and key monitorables.
7. Only then proceed to sector, order book, and qualitative thesis work.

**File Location**: `library/advanced-fundamental-audit.md`  
**Callable via**: Library reference or direct audit request on any ticker.
