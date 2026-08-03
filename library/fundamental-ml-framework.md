# Fundamental ML Framework

**Version**: 1.0  
**Last Updated**: 03 August 2026  
**Status**: Feature Engineering + Rules Baseline Ready | Supervised Model – Future Phase  
**Parent Module**: `library/advanced-fundamental-audit.md`

---

## 1. Design Philosophy

We do **not** currently have a trained production machine learning model.  
What we implement here is:

1. A clean **feature set** derived from the Advanced Fundamental Audit rules
2. A **rules-based scoring engine** (already live) as the production baseline
3. A clear **ML roadmap** so that when labeled historical data becomes available, a supervised model can be trained and layered on top

This keeps the system honest, auditable, and immediately usable.

---

## 2. Feature Store Definition

All features are designed to be quantifiable from standard financial statements + corporate actions.

### A. Balance Sheet Features

| Feature Name                        | Type     | Description                                      | Direction |
|-------------------------------------|----------|--------------------------------------------------|-----------|
| `capex_to_pnM`                      | Numeric  | Capex / Current Plant & Machinery                | Higher better (expansion) |
| `asset_turnover`                    | Numeric  | Revenue / Total Assets                           | Higher better |
| `debt_to_equity`                    | Numeric  | Total Debt / Equity                              | Lower better |
| `equity_growth_3y`                  | Numeric  | 3-year CAGR in Equity                            | Higher better |
| `recv_inv_to_assets`                | Numeric  | (Receivables + Inventory) / Total Assets         | Lower better |
| `cash_to_assets`                    | Numeric  | Cash & Equivalents / Total Assets                | Moderate optimal |
| `contingent_liab_to_nw`             | Numeric  | Contingent Liabilities / Net Worth               | Lower better |
| `is_deleveraging`                   | Binary   | 1 if Debt reduced YoY and Equity rising          | Positive |

### B. Earnings Quality Features

| Feature Name                        | Type     | Description                                      | Direction |
|-------------------------------------|----------|--------------------------------------------------|-----------|
| `roe_3y_avg`                        | Numeric  | Average ROE last 3 years                         | Higher better |
| `roe_stability`                     | Numeric  | 1 – (Std Dev of ROE / Mean ROE)                  | Higher better |
| `gross_margin_trend`                | Numeric  | Slope of Gross Margin (3–5 yrs)                  | Positive better |
| `opm_volatility`                    | Numeric  | Coefficient of variation of OPM                  | Lower better |
| `interest_coverage`                 | Numeric  | EBIT / Interest                                  | Higher better |
| `has_repeated_exceptionals`         | Binary   | 1 if exceptional items in ≥ 2 of last 3 years    | Negative |
| `depreciation_volatility`           | Numeric  | Variation in Depreciation / Gross Block          | Lower better |

### C. Cash Flow Features

| Feature Name                        | Type     | Description                                      | Direction |
|-------------------------------------|----------|--------------------------------------------------|-----------|
| `cfo_to_ebitda`                     | Numeric  | CFO / EBITDA                                       | Higher better |
| `cfo_growth`                        | Numeric  | YoY growth in CFO                                | Higher better |
| `debtor_days_change`                | Numeric  | Change in Debtor Days (negative = improvement)   | Negative better |
| `inventory_days_change`             | Numeric  | Change in Inventory Days                         | Negative better |
| `payable_days_change`               | Numeric  | Change in Payable Days                           | Positive better |
| `is_negative_wc`                    | Binary   | 1 if Working Capital is negative                 | Positive (B2C) |

### D. Governance Features

| Feature Name                        | Type     | Description                                      | Direction |
|-------------------------------------|----------|--------------------------------------------------|-----------|
| `auditor_resigned`                  | Binary   | 1 if auditor resigned mid-term                   | Strong Negative |
| `concall_stopped_after_weak`        | Binary   | 1 if concalls stopped after poor results         | Negative |
| `promoter_buying`                   | Binary   | 1 if net promoter buying in last 12 months       | Positive |
| `promoter_first_sale`               | Binary   | 1 if promoter sold for first time                | Negative |
| `warrant_to_promoter`               | Binary   | 1 if warrants converting to promoter equity      | Negative |
| `capex_vs_employee_cost_mismatch`   | Binary   | 1 if Capex rising sharply & employee cost flat   | Strong Negative |

### E. Growth & Valuation Features

| Feature Name                        | Type     | Description                                      | Direction |
|-------------------------------------|----------|--------------------------------------------------|-----------|
| `revenue_cagr_3y`                   | Numeric  | 3-year Revenue CAGR                              | Higher better |
| `pat_cagr_3y`                       | Numeric  | 3-year PAT CAGR                                  | Higher better |
| `is_volume_led`                     | Binary   | 1 if volume growth is primary driver             | Positive |
| `orderbook_to_sales`                | Numeric  | Order Book / Current Sales (if available)        | Higher better |
| `pe_vs_growth`                      | Numeric  | PE / Earnings Growth (PEG-like)                  | Lower better |
| `is_peak_margin_peak_pe`            | Binary   | 1 if both margins and PE are at multi-year highs | Negative |

---

## 3. Target Variables (for future supervised learning)

When historical data is collected, possible prediction targets:

| Target                        | Type        | Use Case |
|-------------------------------|-------------|----------|
| `conviction_score`            | Regression  | Predict 0–100 audit score |
| `future_2y_return`            | Regression  | Predict forward returns |
| `is_high_conviction`          | Classification | Binary: Score ≥ 70 |
| `is_red_flag_stock`           | Classification | Binary: Hits hard disqualification |
| `max_drawdown_2y`             | Regression  | Risk prediction |

---

## 4. Current Production Engine (Rules-Based)

Until a trained model exists, the **Automated Scoring Algorithm** in `advanced-fundamental-audit.md` remains the production system.

It is deterministic, fully auditable, and already maps to Conviction Tags used in `watchlist.md`.

**Hard Disqualification Rules** act as a safety layer (equivalent to a high-precision classifier for “Avoid”).

---

## 5. ML Roadmap (Future Phases)

### Phase 1 – Feature Store (Current)
- Define and document all features (this file)
- Manually compute features during stock audits
- Store feature vectors + final scores for every analysed stock

### Phase 2 – Data Collection
- Build historical dataset (3–7 years) for 200–400 Indian stocks
- Label with forward returns, max drawdowns, and audit outcomes
- Clean and version the dataset

### Phase 3 – Baseline Model
- Train simple models first:
  - Regularized Linear / Logistic Regression
  - Gradient Boosting (LightGBM / XGBoost)
- Evaluate on time-series cross-validation (no leakage)
- Compare against pure rules-based score

### Phase 4 – Production Hybrid
- Keep rules engine as primary (explainable)
- Use ML model as secondary signal / anomaly detector
- Only override rules when model confidence is high and explanation is clear

### Phase 5 – Continuous Learning
- Log every new audit
- Periodically retrain
- Monitor feature drift and performance decay

---

## 6. Implementation Notes for Curiosity Stack

- All feature names above are stable and should be used consistently.
- When running a fundamental audit, extract the feature vector and store it (even if only in notes).
- The rules-based score remains the source of truth for conviction tags until Phase 3+ is complete.
- Never present an untrained or backtested-only model as “production ML”.

---

## 7. Quick Reference – Feature Extraction Checklist

When analysing a stock, capture at minimum:

**Must Have**
- `recv_inv_to_assets`
- `roe_3y_avg` + stability
- `interest_coverage`
- `cfo_to_ebitda`
- `auditor_resigned`
- `revenue_cagr_3y` / `pat_cagr_3y`
- `is_peak_margin_peak_pe`

**High Value**
- `capex_to_pnM`
- `is_deleveraging`
- `has_repeated_exceptionals`
- `capex_vs_employee_cost_mismatch`
- `orderbook_to_sales`

---

**Related Files**
- Parent: `library/advanced-fundamental-audit.md`
- This Framework: `library/fundamental-ml-framework.md`

**Current Status**: Rules engine live. ML feature layer defined. Supervised model = future work pending labeled dataset.
