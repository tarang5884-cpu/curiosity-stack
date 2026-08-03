# Advanced Fundamental Audit Module

**Version**: 2.0 (SuperGrok-Alpha Integrated)  
**Last Updated**: 03 August 2026  
**Purpose**: Rigorous 360° fundamental + forensic audit engine for Curiosity Stack. Combines institutional-grade analysis with hard disqualification rules and automated scoring.

---

## Master 6-Layer Framework

### LAYER 1: Balance Sheet & Asset Quality Audit

**1. Capex & Capacity Growth**
- Calculate: `New Capex / Current Plant & Machinery`
- If Capex ≥ **2× Current P&M** → Mark as **MUST-READ PRIORITY COMPANY**
- Estimate prospective revenue using historical Asset Turnover
- Check if new capacity is being utilised or merely adding depreciation drag

**2. Deleveraging & Equity Base**
- Prefer systematic debt reduction + rising equity base

**3. Asset Allocation Quality**
- Financial Assets > 20% of Total Assets → Flag
- Associates (20–50%) and Subsidiaries (>50%) → Note complexity/transparency impact

**4. Fictitious Sales Warning (Hard Gate)**
- Calculate: `(Trade Receivables + Inventory) / Total Assets`
- **RED FLAG GATE**: If ≥ 50% → Explicit fictitious sales / channel stuffing risk

**5. Cash & Working Capital**
- Excessive idle cash with negligible interest income → Inefficiency flag
- Declining Debtor Days → Positive cash flow acceleration
- Exclude preference shares & warrants from structural liabilities (track conversion risk separately)
- Contingent Liabilities as % of Net Worth → Flag if > 15–20%

---

### LAYER 2: Income Statement & Earnings Quality Audit

**1. Profitability Baseline**
- ROE Gate: Prefer consistent **> 15%**

**2. Sales Quality (Volume vs Value)**
- Dissect growth into Volume vs Value (pricing/mix)
- **Rule**: Volume growth is the holy grail for long-term compounders. Pure value growth is less sustainable.

**3. Margin Dynamics & Pricing Power**
- Rising Gross Margin → True pricing power
- Highly fluctuating margins → Cyclicality warning
- Operating Leverage: Sales growing faster than fixed costs → Positive

**4. Forensic P&L Red Flags**
- Inventory Gains (low-cost RM inventory) → Temporary boost, high reversal risk
- Sudden change in depreciation rates / asset life → Earnings management risk
- Under-utilised Capex causing heavy depreciation drag
- Repeated Exceptional Losses → Avoid
- Inventory Write-offs → Strong signal of prior period fudging
- Always analyse PAT growth **after stripping exceptional items**

**5. Solvency**
- Interest Coverage (EBIT / Interest) must be **> 7×**. < 7× = structural vulnerability.

---

### LAYER 3: Cash Flow & Capital Efficiency Audit

**1. CFO Quality Drivers**
- Prefer CFO growth from: Falling Debtor Days + Falling Inventory Days + Rising Payable Days
- Exception: Realty & NBFCs

**2. Cash Conversion**
- Target: `CFO / EBITDA > 70%` (especially for B2C / asset-light)
- Asset-light models naturally generate superior Free Cash Flow and deserve valuation premium

**3. Cash Flow Mapping**
- **CFI**: Capex quality + M&A
- **CFF**: Debt vs Equity funding, dilution, dividends

---

### LAYER 4: Corporate Governance & Promoter Audit (Hard Fails)

**Immediate HARD FAILS / Dealbreakers:**
1. Capex expanding significantly while Employee Cost remains flat/dropping → Suspected fraudulent Capex
2. Auditor resignation before job completion → **IMMEDIATE AVOID**
3. Preference warrants converting into promoter equity → Track dilution carefully
4. Legacy promoter who has never sold begins selling at highs → Possible cycle peak / distribution
5. Management stops concalls after a bad quarter → Major transparency red flag

**Positive Signals:**
- Net promoter buying
- Consistent auditor + clean report
- Regular, transparent communication even in weak periods

---

### LAYER 5: Business Nature & Valuation Matrix

**Business Classification**
| Type | Characteristics | Strategy |
|------|------------------|----------|
| Fast Growing | > 15% sustained CAGR | Growth at reasonable price |
| Secular | Consistent earnings uptrend + stable margins | Core holding |
| Cyclical | Earnings & margins swing with cycle | Buy support P/B, sell resistance P/B |
| Commodity | Highly price-sensitive | Avoid when underlying commodity is at ATH |

**Valuation Vulnerability Tests**
- **ZONE OF DANGER**: Peak Margins + Peak PE = High risk of capital loss
- **MARGIN OF SAFETY**: Reasonable valuation + Fast organic growth + Not currently over-earning due to temporary shortages

---

### LAYER 6: Annual Report & Forensic Document Review

Priority reading order:
1. CEO / MD Message & Future Guidance (tone + honesty)
2. Segmental Revenue + Customer Concentration
3. Management Discussion & Analysis (MD&A)
4. Key Audit Matters (KAMs) + CARO / Annexure qualifications
5. Director & KMP Remuneration as % of PAT
6. Related Party Transactions (RPT) vs Standalone revenue
7. Contingent Liabilities as % of Net Worth
8. Consolidated vs Standalone differences
9. Auditor’s Report (qualifications / emphasis of matter)

**Connecting the Dots Rule**: Always link Balance Sheet changes → P&L impact → Cash Flow reality → Management commentary.

---

## Automated Scoring Algorithm (v2.0)

### Category Weights

| Category                      | Weight | Max |
|-------------------------------|--------|-----|
| Balance Sheet Strength        | 20%    | 20  |
| Earnings Quality              | 25%    | 25  |
| Cash Conversion               | 15%    | 15  |
| Governance & Transparency     | 15%    | 15  |
| Growth Visibility             | 15%    | 15  |
| Valuation Margin of Safety    | 10%    | 10  |
| **Total**                     | 100%   | **100** |

### Hard Disqualification Rules (Override)
Any of the following **caps score at 45** or forces **Avoid**:
- Auditor resignation mid-term
- (Receivables + Inventory) ≥ 50% of Total Assets without credible explanation
- Repeated exceptional losses / inventory write-offs
- Capex rising sharply while employee cost stays flat
- Interest Coverage consistently < 5×

### Score → Conviction Mapping

| Total Score | Conviction Tag | Guidance |
|-------------|----------------|----------|
| 85–100      | 8.5–9.5        | High Conviction – Core / Aggressive |
| 70–84       | 7.0–8.4        | Strong – Tier 1 |
| 55–69       | 6.0–6.9        | Acceptable – Tier 2 / Monitor |
| 40–54       | 5.0–5.9        | Weak – Speculative |
| < 40        | < 5.0          | Avoid |

---

## Standard Output Format (Mandatory)

When auditing any company, structure the response exactly as follows:

1. **EXECUTIVE SUMMARY & VERDICT** (Pass / Conditional / Avoid + Conviction Score)
2. **CAPEX & REVENUE PREDICTION MATRIX** (Highlight 2× Capex trigger if present)
3. **BALANCE SHEET & FORENSIC RED-FLAG SCORECARD**
4. **P&L QUALITY & CASH FLOW CONVERSION ANALYSIS** (CFO/EBITDA, Volume vs Value)
5. **GOVERNANCE & PROMOTER AUDIT** (Auditor, Insider trades, Capex-Employee match)
6. **VALUATION & CYCLE ASSESSMENT** (Zone of Danger vs Margin of Safety)
7. **KEY ANNUAL REPORT INSIGHTS** (RPT, Contingent Liabilities, KAMs)

---

## Usage Protocol inside Curiosity Stack

1. Run this full 6-Layer audit first on any new or existing name.
2. Apply the Automated Scoring Algorithm.
3. Enforce Hard Disqualification Rules strictly.
4. Map final score to Conviction Tag.
5. Update `watchlist.md` with score, verdict, and key monitorables.
6. Only after clearing the audit proceed to sector thesis, order book, and technical work.

**Related Files**
- Scoring Engine Code: `library/fundamental_scorer/scorer.py`
- ML Feature Framework: `library/fundamental-ml-framework.md`
- This Module: `library/advanced-fundamental-audit.md`

**Callable Command**: “Run full fundamental audit on [Company]” or “Apply SuperGrok-Alpha protocol on [Ticker]”
