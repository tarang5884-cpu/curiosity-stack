# Fair Value Module v2.1

**Version**: 2.1 (Locked)  
**Last Updated**: 19 August 2026  
**Status**: Permanent Curiosity Stack Module  
**Parent**: Advanced Fundamental Audit + J-Curve Scorecard  
**Purpose**: Produce conservative, probability-weighted, auditable fair value bands. Designed to prevent overpayment for peak-cycle or pre-inflection stories.

---

## 0. Pre-Requisite Hard Gates (Zero-Bloat Filters)

Before any fair value calculation, the company **must** clear:

| Gate | Rule | Failure Action |
|------|------|----------------|
| **Liquidity Floor** | Median daily traded value > ₹3 Cr | Do not assign institutional-size FV; flag as liquidity-constrained |
| **Surveillance Clean** | Not in Stage-4 ASM/GSM (no 5% daily bands) | Avoid or extreme caution |
| **ROCE Floor** | ROCE > 10% (unless temporary massive capex cycle is clearly documented) | Cap conviction and multiple |

If any gate fails → Fair value exercise is suspended or heavily caveated.

---

## 1. Core Process (Mandatory Sequence)

1. Run **J-Curve 9-Factor Scorecard** → determine Stage.
2. Run **Advanced Fundamental Audit** (8 layers) → obtain conviction score.
3. Apply **Strategic Positioning Premium** (Module v2.2) only if earned.
4. Build earnings trajectory (FY27E / FY28E / FY29E).
5. Assign multiple band (peer-relative + absolute, stage-adjusted).
6. Calculate probability-weighted fair value band.
7. Publish both Base FV and Adjusted FV (if premium applied).

---

## 2. Earnings Trajectory Rules

| Principle | Rule |
|-----------|------|
| Management guidance | Primary input when credible (met in ≥2 of last 3 years) |
| Conservative bias | Prefer lower half of guidance range for base case |
| One-offs | Strip exceptional items; normalise |
| Margin assumptions | Do not assume peak margins persist without structural proof |
| Volume vs price | Prefer volume-driven growth assumptions |

Always show three years: FY27E, FY28E, FY29E.

---

## 3. Multiple Band Construction

| Stage (from J-Curve) | Base Multiple Stance |
|----------------------|----------------------|
| Stage 1 | Discount to peer median (use lower end of band) |
| Stage 2 | Peer median to slight premium |
| Stage 3 | Full peer premium justified only with margin + cash proof |

**Additional Adjustments**
- Cyclical businesses → use mid-cycle earnings and compressed multiples.
- High WC / low CFO conversion → reduce multiple by 1–3 turns.
- Debt-free + high ROCE → allow upper end of band.
- Strategic Positioning Premium (v2.2) applied **after** base band is set (max +25%).

**Relative Invalidation Rule**  
If the assigned multiple is >20% premium to the top-2 peer median, Guidance Alignment / Strategic Score must be ≥8.0, otherwise revise multiple down.

---

## 4. Probability-Weighted Fair Value Calculation

**Standard Weights** (adjust only with strong justification):

| Year | Weight |
|------|--------|
| FY27E | 55–60% |
| FY28E | 30–35% |
| FY29E | 10–15% |

**Formula**
```
Lower Bound = (FY27 Low × w1) + (FY28 Low × w2) + (FY29 Low × w3)
Upper Bound = (FY27 High × w1) + (FY28 High × w2) + (FY29 High × w3)
```

Always publish the full calculation so it is auditable.

---

## 5. Hard Scoring Caps (from v2.1 refinements)

| Trigger | Impact |
|---------|--------|
| CFO / EBITDA < 50% (3-year average) | Cash Flow layer capped; total score capped at 6.5 |
| Capex expanding while Employee Cost flat | Governance layer → 0; Immediate Avoid |
| Falling Laggard (Price < 200 DMA + Rising Retail) | Thematic Fit capped |
| Peak Margins + Peak Multiple | Zone of Danger flag; force mid-cycle valuation |

---

## 6. Standard Output Format (Mandatory)

1. **Pre-Requisite Gates** – Pass / Fail
2. **J-Curve Stage** – Score + Label
3. **8-Layer Summary** – Brief scores
4. **Earnings Trajectory** – FY27/28/29 EPS or PAT
5. **Multiple Band** – with justification
6. **Probability-Weighted FV Calculation** – full arithmetic
7. **Final Fair Value Band** – Base and Adjusted (if premium)
8. **Stance** – Accumulate / Hold / Trim / Avoid + preferred entry zone
9. **Key Monitorables**

---

## 7. Usage Protocol inside Curiosity Stack

- File location: `library/fair-value-module-v2.1.md`
- Always run **after** J-Curve Scorecard.
- Callable: “Run Fair Value Module on [Company]” or “Full FV with J-Curve on [Ticker]”
- Update `watchlist.md` with FV band, stage, and preferred entry zone.

**Related Files**
- J-Curve Scorecard: `library/j-curve-9-factor-scorecard.md`
- Advanced Fundamental Audit: `library/advanced-fundamental-audit.md`
- Strategic Positioning Premium: `library/module-v2.2-strategic-positioning-premium.md`
- Scorer: `library/fundamental_scorer/scorer.py`

**Locked**: 19 August 2026
