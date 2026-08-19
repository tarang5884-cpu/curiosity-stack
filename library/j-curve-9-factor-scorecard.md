# J-Curve 9-Factor Scorecard

**Version**: 1.0 (Locked)  
**Last Updated**: 19 August 2026  
**Status**: Permanent Curiosity Stack Module  
**Purpose**: Determine the operational stage of a business (Stage 1 / 2 / 3) before applying valuation. Prevents paying peak multiples for pre-inflection stories and identifies genuine acceleration.

---

## Core Philosophy

A company can only be valued correctly when its position on the growth curve is known.

- **Stage 1** = Base building / investment phase → patience required
- **Stage 2** = Inflection / early acceleration → best risk-reward window
- **Stage 3** = Peak acceleration / mature compounding → higher multiples justified only with proof

The scorecard is deliberately mechanical. Subjective narrative is not allowed to override failed factors.

---

## The 9 Factors (Pass = 1, Partial = 0.5, Fail = 0)

| # | Factor | Pass Criteria | Fail Criteria |
|---|--------|---------------|---------------|
| 1 | **Sector Tailwind** | Clear multi-year structural demand (policy, technology, capacity cycle) | Cyclical peak or fading demand |
| 2 | **Demand Visibility** | Order book ≥ 1.5× trailing revenue **or** high recurring/visible pipeline | Order book thin or highly uncertain |
| 3 | **Capex / Restructuring** | Capacity coming online, product investment, or clean restructuring (asset-light pivot, demerger of drag) | No capacity or structural change underway |
| 4 | **Rising Utilisation** | Clear evidence of improving capacity utilisation or operating leverage beginning | Utilisation flat or declining |
| 5 | **Revenue Acceleration** | YoY revenue growth accelerating (or ≥ 15% sustained) | Flat, declining, or decelerating growth |
| 6 | **Operating Leverage** | EBITDA or PAT growing faster than revenue (margins expanding or costs absorbing) | Margins compressing without credible temporary explanation |
| 7 | **Deleveraging / BS Strength** | Debt falling or already fortress (D/E < 0.3, strong interest coverage) | Rising leverage or weak coverage |
| 8 | **Core Capital Efficiency** | ROCE / ROE improving or already healthy (>12–15% depending on sector) | Persistently low returns without temporary capex explanation |
| 9 | **Guidance / Visibility** | Management guidance clear, credible, and directionally supportive | Guidance vague, withdrawn, or repeatedly missed |

**Total Score** = Sum of the 9 factors (maximum 9.0)

---

## Stage Definitions (Locked)

| Score | Stage | Label | Investment Implication |
|-------|-------|-------|------------------------|
| **0 – 3.5** | Stage 1 | Base Building / Investment | High uncertainty. Only accumulate at deep discount or with clear catalyst timeline. |
| **4.0 – 6.5** | Stage 2 | Inflection / Early Acceleration | **Preferred buying window**. Order visibility rising, leverage not yet fully visible. |
| **7.0 – 8.5** | Stage 3 | Acceleration / Compounding | Higher multiples justified only if margins and cash flow are also expanding. |
| **8.5 – 9.0** | Late Stage 3 | Peak Acceleration | Risk of multiple compression. Prefer to hold or trim rather than add aggressively. |

**Special Cases**
- Restructuring J-Curve (asset-light pivot, demerger of drag): Factor 3 can pass even if revenue growth is still modest.
- Pure cyclical businesses: Cap Stage at 2 even with high score if the upcycle is mature.

---

## Hard Rules

1. **No Stage 3 without Operating Leverage**  
   Factor 6 must score at least 0.5 to reach Stage 3. Revenue growth alone is insufficient.

2. **Partial Scores Allowed**  
   Use 0.5 when evidence is mixed but directionally positive.

3. **Override**  
   Any Hard Fail from the Advanced Fundamental Audit (governance, fictitious sales, auditor resignation) automatically caps the company at Stage 1 regardless of score.

4. **Re-score Frequency**  
   Re-run after every quarterly result or major order/announcement.

---

## Standard Output Format

When applying the module, always show:

1. Factor-by-factor table with Pass / Partial / Fail and brief evidence
2. Total Score
3. Assigned Stage + Label
4. One-line investment implication

---

## Usage Protocol

- Run **before** Fair Value Module.
- Stage determines the aggressiveness of the multiple band and the probability weights.
- File location: `library/j-curve-9-factor-scorecard.md`
- Callable: “Run J-Curve scorecard on [Company]” or “What stage is [Ticker] on?”

**Related Files**
- Fair Value Module: `library/fair-value-module-v2.1.md`
- Advanced Fundamental Audit: `library/advanced-fundamental-audit.md`
- Strategic Positioning Premium: `library/module-v2.2-strategic-positioning-premium.md`

**Locked**: 19 August 2026
