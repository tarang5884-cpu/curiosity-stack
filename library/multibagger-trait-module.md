# Multibagger Trait Module v1.0

**Locked:** 17 Sep 2026  
**Status:** Active Curiosity Stack module  
**Runs after:** J-Curve 9-Factor + Advanced Fundamental Audit  
**Runs before:** Fair Value v2.1 multiple band and 8-slot  
**Does not replace:** MOS, spike-DMA, NSE-filing-first, liquidity gates

Purpose: turn the 20 common “multibagger traits” into a **ranked state**, not a poster. Most names that look like 10/20 traits are already **Priced**. The money is in Setup / Inflight **before** the rerating trait prints.

---

## Philosophy

A multibagger is **earnings duration + a change in what the market believes the earnings are**. Traits are not equal.

- **Leading** traits change the P&L or the asset before the tape.  
- **Lagging** traits (narrative change, sudden rerating) are the *result*. Scoring them as causes is how you buy Azad at 120× and call it a setup.

Sequence (same as J-Curve, stricter):

```
New cycle / product / mix
  → capacity at the right time
    → utilisation + operating leverage
      → revenue then PAT 30–50%+
        → cash inflection + BS repair
          → ownership still thin
            → narrative + multiple change
```

If you start at the last line, you are late.

---

## The 20 traits — five engines

Score each **engine** 0 / 0.5 / 1.0. Do not tick 20 boxes.

### Engine A — Earnings physics (weight 3)
Must be earned with filings, not a slide.

| Trait | Pass | Fail / trap |
|---|---|---|
| 30–50%+ earnings growth | Recurring PAT / EPS, next 2–3 years visible, not one quarter | Low-base, tax, inventory, other income |
| Operating leverage kick-in | PAT or EBITDA growing **faster** than sales; incremental ROIC > WACC | Sales up, margin flat |
| Margin expansion | Mix / utilisation / pricing, durable 2+ prints | Commodity spike |
| Cash-flow inflection | OCF turning + or OCF/EBITDA rising toward 60%+ | PAT up, WC eating cash |
| Low-base effect | Allowed only as *context*. Never a Pass on its own | First profitable year after a wipeout |

**Engine A score:** 1.0 if ≥3 Pass including earnings **and** (leverage or cash). 0.5 if earnings visible but cash lagging. 0 if only low-base or one-off.

### Engine B — Structural change (weight 2)
Something that was not true 8–12 quarters ago.

| Trait | Pass | Fail / trap |
|---|---|---|
| New industry | Company entered a category with a multi-year TAM and a named SKU/invoice | “AI / DC / EV” on a deck |
| New cycle | Industry utilisation / price / policy just turned; mid-cycle not late |
| New product | Qualified, shipping, or booked — not R&D slide |
| Hidden opportunity | Segment or geography not in the Street model, **and** already invoicing |
| Change of management | New capital allocator with a 2-year proof print |
| Business-mix upgrade | High-VA / export / branded share up in reported mix |
| Export / import substitution | Documented share win vs import or export TCV |
| Capacity at the right time | COD into a tight market, not empty sheds into a glut |

**Engine B score:** 1.0 if ≥2 Pass with a dated filing. 0.5 if one real change. 0 if narrative only.

### Engine C — Industry physics (weight 2)

| Trait | Pass | Fail / trap |
|---|---|---|
| Strong sector tailwind | 3–5 year demand that does not need a perfect company |
| Industry consolidation | Share accruing to qualified / licensed names |
| Pricing power | Realised price / spread up without volume collapse |

**Engine C score:** 1.0 if tailwind **and** (consolidation or pricing). 0.5 tailwind only. 0 peak-cycle call.

### Engine D — Balance sheet and ownership (weight 2)

| Trait | Pass | Fail / trap |
|---|---|---|
| Balance-sheet improvement | D/E down, WC days down, or net-cash after a capex spike |
| Under-ownership | Low FII/DII / low float **and** no prior 3–5× spike this cycle |

**Engine D score:** 1.0 both. 0.5 one. 0 if “under-owned” after a vertical SME circuit (that is SPIKE, not under-owned).

### Engine E — Market recognition (weight 1, lagging)

| Trait | Pass | How to use |
|---|---|---|
| Sudden structural rerating | Multiple already moved from cyclical to structural band | **Lagging.** Raises rank only if A+B already Pass |
| Narrative change | Street / X / funds now tell a different story | **Lagging.** Never a Pass that lifts MB-0 to MB-3 |

**Engine E score:** 1.0 if both visible. 0.5 one. Cap: Engine E cannot add more than +1 rank if Engine A is 0.

---

## Weighted score

```
MB Score = 3A + 2B + 2C + 2D + 1E
Maximum = 10
```

| MB Score | Rank | Label | Desk action |
|---|---|---|---|
| 0 – 2.5 | **MB-0** | Fake / narrative | Ignore or kill. Slide ≠ invoice |
| 3.0 – 4.5 | **MB-1** | Seed | Watchlist only. Size 0. Size up only on next print |
| 5.0 – 6.5 | **MB-2** | Setup | Preferred research window. Add only with MOS + BASE READY |
| 7.0 – 8.5 | **MB-3** | Inflight | Compounder path. Hold / add dips. Multiple can expand |
| 8.5 – 10 | **MB-4** | Priced | Traits worked; rerating done. Trim into strength. Re-add only on MOS wash |

---

## Hard gates (override the score)

1. **No MB-3 without Engine A ≥ 0.5.** Growth story with no earnings physics stays Seed.  
2. **No MB-2+ if Advanced Audit hard-fails** (governance, auditor, fictitious sales).  
3. **Cyclical peak:** if J-Curve Factor 1 is Fail (late cycle), cap at MB-1 even if score is 7.  
4. **Low-base trap:** if >50% of the 30–50% PAT print is base/tax/other income, Engine A = 0.  
5. **SPIKE + under-ownership:** if tape tag is SPIKE / EXTENDED, Engine D under-ownership = 0. Institutions already found it.  
6. **Peak PE + peak margins + Engine E = 1:** force **MB-4 Priced**, not Inflight.  
7. **SME / circuit / mcap < ₹2,000 Cr:** max rank MB-2 and 0.3–0.75% size even if score is 8.

---

## Interaction with the rest of the stack

| Module | How this one uses it |
|---|---|
| J-Curve | Stage 1 → max MB-1. Stage 2 → MB-2 candidate. Stage 3 → MB-3 only if cash also turns |
| Fair Value v2.1 | MB-2 uses lower multiple band. MB-3 can use peer median. MB-4 uses mid-cycle and MOS only |
| Spike-DMA | MB-2/3 may 8-slot only if BASE READY. MB-4 on a spike is a trim, not an add |
| NSE filing first | Engine B Pass needs a dated PDF (order, COD, mix, management change) |
| 10-pillar / MOS | Rank ≠ buy. Pillar 10 still demands MOS + exit |

---

## Standard output (mandatory)

```
MB Trait Card | [Name] | [Date]
J-Curve stage:  
Engine A / B / C / D / E:  (0 / 0.5 / 1) + one-line evidence each
MB Score:  /10
Rank: MB-0 … MB-4
What is leading vs already in the price:
Add / hold / ignore + zone (only if MOS exists)
Kill switch:
```

Max 180 words after the card.

---

## Ranking a list

When scoring a basket (watchlist, sabarisec add-list, gas-turbine sleeve):

1. Run the card on each name.  
2. Sort by **Rank first**, then **MB Score**, then **MOS gap**.  
3. Print only MB-2 and MB-3 as actionable. MB-1 goes to queue. MB-4 to hold/trim. MB-0 drop.  
4. Cap live 8-slot at **two** MB-3 names if both are in the same industry physics (Engine C shared). That is one bet.

---

## Fake-multibagger checklist (run every card)

- [ ] Earnings growth is recurring, not restated / other-income  
- [ ] New product has a customer name and a shipment  
- [ ] Capacity is filling, not just commissioned  
- [ ] Cash is turning with PAT, not against it  
- [ ] Under-owned ≠ just listed / just circuited  
- [ ] Narrative is not the only engine that scores 1  
- [ ] Multiple has not already done the 3–5×

Three or more unchecked → cap at MB-0 / MB-1.

---

## Callable phrases

- “Run MB trait module on [Company]”  
- “Rank this list on MB module”  
- “Is this MB-2 or already MB-4?”

**Related:** `library/j-curve-9-factor-scorecard.md` · `library/fair-value-module-v2.1.md` · `library/spike-dma-base-rule.md` · `library/csk-momentum-scan.md`
