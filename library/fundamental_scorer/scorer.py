"""
Curiosity Stack - Fundamental Scorer (Skeleton)
-----------------------------------------------
Version: 0.1.0
Date: 2026-08-03

Purpose:
- Extract structured features from company financial data
- Apply the rules-based scoring engine (production baseline)
- Provide a clean interface that can later accept a trained ML model

This is intentionally simple and dependency-light.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, Any
import math


# ------------------------------------------------------------
# 1. Feature Container
# ------------------------------------------------------------

@dataclass
class FundamentalFeatures:
    """All quantifiable features used by the scorer."""

    # Balance Sheet
    capex_to_pnm: Optional[float] = None          # Capex / Plant & Machinery
    asset_turnover: Optional[float] = None
    debt_to_equity: Optional[float] = None
    equity_growth_3y: Optional[float] = None
    recv_inv_to_assets: Optional[float] = None    # (Receivables + Inventory) / Total Assets
    cash_to_assets: Optional[float] = None
    contingent_liab_to_nw: Optional[float] = None
    is_deleveraging: Optional[bool] = None

    # Earnings Quality
    roe_3y_avg: Optional[float] = None
    roe_stability: Optional[float] = None         # 1 - (std/mean)
    gross_margin_trend: Optional[float] = None    # slope
    opm_volatility: Optional[float] = None
    interest_coverage: Optional[float] = None
    has_repeated_exceptionals: Optional[bool] = None
    depreciation_volatility: Optional[float] = None

    # Cash Flow
    cfo_to_ebitda: Optional[float] = None
    cfo_growth: Optional[float] = None
    debtor_days_change: Optional[float] = None    # negative = improvement
    inventory_days_change: Optional[float] = None
    payable_days_change: Optional[float] = None
    is_negative_wc: Optional[bool] = None

    # Governance
    auditor_resigned: Optional[bool] = None
    concall_stopped_after_weak: Optional[bool] = None
    promoter_buying: Optional[bool] = None
    promoter_first_sale: Optional[bool] = None
    warrant_to_promoter: Optional[bool] = None
    capex_vs_employee_cost_mismatch: Optional[bool] = None

    # Growth & Valuation
    revenue_cagr_3y: Optional[float] = None
    pat_cagr_3y: Optional[float] = None
    is_volume_led: Optional[bool] = None
    orderbook_to_sales: Optional[float] = None
    pe_vs_growth: Optional[float] = None
    is_peak_margin_peak_pe: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ------------------------------------------------------------
# 2. Score Result
# ------------------------------------------------------------

@dataclass
class ScoreResult:
    total_score: float
    category_scores: Dict[str, float]
    conviction_tag: float
    hard_disqualified: bool
    disqualification_reasons: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def summary(self) -> str:
        status = "DISQUALIFIED" if self.hard_disqualified else "OK"
        return (
            f"Score: {self.total_score:.1f}/100 | "
            f"Conviction: {self.conviction_tag:.1f} | "
            f"Status: {status}"
        )


# ------------------------------------------------------------
# 3. Rules-Based Scorer (Production Baseline)
# ------------------------------------------------------------

class RulesScorer:
    """
    Implements the v1.1 Automated Scoring Algorithm.
    Fully deterministic and auditable.
    """

    def score(self, f: FundamentalFeatures) -> ScoreResult:
        scores = {
            "balance_sheet": 0.0,
            "earnings_quality": 0.0,
            "cash_conversion": 0.0,
            "governance": 0.0,
            "growth": 0.0,
            "valuation": 0.0,
        }
        notes = []
        disqualify_reasons = []

        # ---------- 1. Balance Sheet (Max 20) ----------
        bs = 0.0
        if f.capex_to_pnm is not None and f.asset_turnover is not None:
            if f.capex_to_pnm > 0.3 and f.asset_turnover > 0.8:
                bs += 5
                notes.append("Strong Capex + Asset Turnover")
            if f.capex_to_pnm >= 2.0:
                bs += 3
                notes.append("Capex >= 2x P&M (Must-Read expansion)")

        if f.is_deleveraging:
            bs += 4

        if f.recv_inv_to_assets is not None:
            if f.recv_inv_to_assets < 0.35:
                bs += 4
            elif f.recv_inv_to_assets < 0.50:
                bs += 1
            else:
                bs -= 5
                notes.append("Receivables+Inventory >= 50% of Assets (Red Flag)")

        if f.cash_to_assets is not None and f.cash_to_assets > 0.25:
            # crude check for idle cash – refine with interest income later
            bs -= 2

        if f.contingent_liab_to_nw is not None and f.contingent_liab_to_nw > 0.25:
            bs -= 3

        scores["balance_sheet"] = max(min(bs, 20), -10)

        # ---------- 2. Earnings Quality (Max 25) ----------
        eq = 0.0
        if f.roe_3y_avg is not None:
            if f.roe_3y_avg >= 0.18:
                eq += 6
            elif f.roe_3y_avg >= 0.15:
                eq += 4
            elif f.roe_3y_avg < 0.12:
                eq -= 3

        if f.gross_margin_trend is not None and f.gross_margin_trend > 0:
            eq += 5

        if f.opm_volatility is not None and f.opm_volatility > 0.35:
            eq -= 4

        if f.interest_coverage is not None:
            if f.interest_coverage >= 10:
                eq += 4
            elif f.interest_coverage >= 7:
                eq += 2
            else:
                eq -= 5

        if f.has_repeated_exceptionals:
            eq -= 6
            notes.append("Repeated exceptional items / write-offs")
        else:
            eq += 3

        if f.depreciation_volatility is not None and f.depreciation_volatility > 0.4:
            eq -= 4

        scores["earnings_quality"] = max(min(eq, 25), -15)

        # ---------- 3. Cash Conversion (Max 15) ----------
        cf = 0.0
        if f.cfo_to_ebitda is not None:
            if f.cfo_to_ebitda >= 0.80:
                cf += 6
            elif f.cfo_to_ebitda >= 0.70:
                cf += 4
            elif f.cfo_to_ebitda >= 0.50:
                cf += 2
            else:
                cf -= 4

        if f.debtor_days_change is not None and f.debtor_days_change < 0:
            cf += 2
        if f.inventory_days_change is not None and f.inventory_days_change < 0:
            cf += 2
        if f.payable_days_change is not None and f.payable_days_change > 0:
            cf += 2

        if f.is_negative_wc:
            cf += 3

        scores["cash_conversion"] = max(min(cf, 15), -8)

        # ---------- 4. Governance (Max 15) ----------
        gov = 0.0
        if f.auditor_resigned:
            gov -= 8
            disqualify_reasons.append("Auditor resigned mid-term")
        else:
            gov += 4

        if f.concall_stopped_after_weak:
            gov -= 5
        else:
            gov += 3

        if f.promoter_buying:
            gov += 3
        if f.promoter_first_sale:
            gov -= 4
        if f.warrant_to_promoter:
            gov -= 3
        if f.capex_vs_employee_cost_mismatch:
            gov -= 6
            disqualify_reasons.append("Capex rising but employee cost flat")

        scores["governance"] = max(min(gov, 15), -20)

        # ---------- 5. Growth Visibility (Max 15) ----------
        gr = 0.0
        growth = f.pat_cagr_3y if f.pat_cagr_3y is not None else f.revenue_cagr_3y
        if growth is not None:
            if growth > 0.20:
                gr += 6
            elif growth > 0.15:
                gr += 4
            elif growth > 0.10:
                gr += 2
            else:
                gr -= 3

        if f.is_volume_led:
            gr += 3
        if f.orderbook_to_sales is not None and f.orderbook_to_sales > 1.0:
            gr += 4

        if f.is_peak_margin_peak_pe:
            gr -= 5
            notes.append("Peak margins + Peak PE (Danger zone)")

        scores["growth"] = max(min(gr, 15), -10)

        # ---------- 6. Valuation MOS (Max 10) ----------
        val = 0.0
        if f.pe_vs_growth is not None:
            if f.pe_vs_growth < 1.0:
                val += 5
            elif f.pe_vs_growth < 1.5:
                val += 3
            elif f.pe_vs_growth < 2.5:
                val += 1
            else:
                val -= 2

        if f.is_peak_margin_peak_pe:
            val -= 4

        scores["valuation"] = max(min(val, 10), -8)

        # ---------- Total & Hard Disqualification ----------
        total = sum(scores.values())
        total = max(min(total, 100), 0)

        hard_disqualified = False
        if f.auditor_resigned:
            hard_disqualified = True
        if f.recv_inv_to_assets is not None and f.recv_inv_to_assets >= 0.50:
            hard_disqualified = True
            disqualify_reasons.append("Receivables+Inventory >= 50%")
        if f.has_repeated_exceptionals:
            hard_disqualified = True
        if f.capex_vs_employee_cost_mismatch:
            hard_disqualified = True
        if f.interest_coverage is not None and f.interest_coverage < 5:
            hard_disqualified = True
            disqualify_reasons.append("Interest Coverage < 5x")

        if hard_disqualified:
            total = min(total, 45)

        # Map to conviction tag (rough linear mapping)
        conviction = round((total / 100) * 10, 1)
        conviction = max(min(conviction, 9.5), 1.0)

        return ScoreResult(
            total_score=round(total, 1),
            category_scores={k: round(v, 1) for k, v in scores.items()},
            conviction_tag=conviction,
            hard_disqualified=hard_disqualified,
            disqualification_reasons=disqualify_reasons,
            notes=notes,
        )


# ------------------------------------------------------------
# 4. Future ML Model Interface (Placeholder)
# ------------------------------------------------------------

class MLModelInterface:
    """
    Placeholder for a future trained model.
    Any model that implements `.predict(features: dict) -> float`
    can be plugged in here.
    """

    def __init__(self, model=None):
        self.model = model  # e.g. sklearn / lightgbm / pytorch model

    def predict(self, features: FundamentalFeatures) -> Optional[float]:
        if self.model is None:
            return None
        # Example: convert features to vector and call model
        # X = self._vectorize(features)
        # return float(self.model.predict(X)[0])
        raise NotImplementedError("Plug in trained model here")


# ------------------------------------------------------------
# 5. Main Hybrid Scorer
# ------------------------------------------------------------

class FundamentalScorer:
    """
    Production entry point.

    - Always runs the rules-based engine
    - Optionally blends / overrides with ML prediction when available
    """

    def __init__(self, ml_model: Optional[MLModelInterface] = None):
        self.rules = RulesScorer()
        self.ml = ml_model

    def score(self, features: FundamentalFeatures) -> ScoreResult:
        rules_result = self.rules.score(features)

        # Future: if ML model exists and confidence is high, blend or override
        # ml_score = self.ml.predict(features) if self.ml else None
        # if ml_score is not None:
        #     ... blending logic ...

        return rules_result


# ------------------------------------------------------------
# 6. Example Usage
# ------------------------------------------------------------

if __name__ == "__main__":
    # Example feature set (replace with real extracted data)
    example = FundamentalFeatures(
        capex_to_pnm=1.8,
        asset_turnover=1.1,
        debt_to_equity=0.4,
        is_deleveraging=True,
        recv_inv_to_assets=0.28,
        roe_3y_avg=0.19,
        interest_coverage=12.5,
        has_repeated_exceptionals=False,
        cfo_to_ebitda=0.82,
        is_negative_wc=False,
        auditor_resigned=False,
        promoter_buying=True,
        revenue_cagr_3y=0.22,
        pat_cagr_3y=0.25,
        is_volume_led=True,
        orderbook_to_sales=1.4,
        is_peak_margin_peak_pe=False,
    )

    scorer = FundamentalScorer()
    result = scorer.score(example)

    print(result.summary())
    print("Category scores:", result.category_scores)
    if result.notes:
        print("Notes:", result.notes)
    if result.disqualification_reasons:
        print("Disqualify reasons:", result.disqualification_reasons)
