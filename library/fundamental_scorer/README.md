# Fundamental Scorer (Python Skeleton)

**Location**: `library/fundamental_scorer/`  
**Status**: Rules engine live | ML interface ready for future model

## What this is

A clean, dependency-light Python skeleton that:

1. Defines a structured `FundamentalFeatures` dataclass (all quantifiable inputs)
2. Implements the **rules-based scoring algorithm** (production baseline from `advanced-fundamental-audit.md`)
3. Provides a clean `MLModelInterface` placeholder so a trained model can be plugged in later
4. Exposes a single `FundamentalScorer` entry point

## Quick Start

```python
from scorer import FundamentalFeatures, FundamentalScorer

features = FundamentalFeatures(
    capex_to_pnm=1.8,
    asset_turnover=1.1,
    recv_inv_to_assets=0.28,
    roe_3y_avg=0.19,
    interest_coverage=12.5,
    cfo_to_ebitda=0.82,
    auditor_resigned=False,
    revenue_cagr_3y=0.22,
    pat_cagr_3y=0.25,
    is_volume_led=True,
    orderbook_to_sales=1.4,
    # ... fill other fields as available
)

scorer = FundamentalScorer()
result = scorer.score(features)

print(result.summary())
print(result.category_scores)
print(result.conviction_tag)
```

## Design Principles

- **Rules first**: The deterministic rules engine is the source of truth today.
- **ML-ready**: Any model that implements `.predict(features_dict) -> float` can be injected via `MLModelInterface`.
- **No heavy dependencies**: Pure Python + dataclasses only.
- **Auditable**: Every point addition/subtraction is explicit.

## Future Extension

When a trained model (LightGBM / XGBoost / simple neural net) is available:

```python
ml = MLModelInterface(model=trained_model)
scorer = FundamentalScorer(ml_model=ml)
```

Blending / override logic can then be added inside `FundamentalScorer.score()`.

## Related Files

- `library/advanced-fundamental-audit.md` – Full rules & scoring logic
- `library/fundamental-ml-framework.md` – Feature store + ML roadmap
