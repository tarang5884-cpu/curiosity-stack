# Spike → DMA base rule

**Embedded:** 15 Sep 2026  
**Runs in:** CSK daily scan (`automation c587c14c`) every weekday 08:15 IST  
**Sits with:** StockScans 50-DMA rest after a run · Gemini-bee DEP (10/20 EMA) · pillars 1–9 then 10

## The market fact

A reckless up-move **without a prior 2–4 week base** usually means:

1. A **catalyst** was strong enough to force price, and
2. The name was **under-owned** by institutions.

That first leg can last. It is **not** the entry if you missed it.

When allocation is done, price typically **falls back to the 10-DMA, then 20-DMA, then 50-DMA** and tries to **build a base**. That coil is the research window.

## Tags (every daily scan)

| Tag | Tape | Action |
|-----|------|--------|
| **SPIKE / EXTENDED** | Vertical, thin prior base, far above 10/20/50 | Watch only. No 8-slot. |
| **MEAN-REV WATCH** | First touch or coil on 10, then 20, then 50; volume quieter than the spike | Open / refresh the 10-pillar file. Still not an auto-add. |
| **BASE READY** | 8–20 sessions tight on a *rising* 20 or 50; dry volume; early expansion | May enter 8-slot **only if** 1–9 pass and MOS / invoice still holds. |
| **FAILED BASE** | Loses 50-DMA on *rising* volume | Kill / demote. Allocation over or thesis fading. |

## Order of DMAs

Homework starts at the **first** mean-reversion, not the last.

1. **10-DMA** — earliest, often noisy. Size = zero unless already MOS and delivery is dry.
2. **20-DMA** — standard first institutional rest (also Gemini DEP).
3. **50-DMA** — StockScans window. Best for “missed the move” names that still have duration.

A close back above the DMA on **rising** volume after a dry coil is the *trigger to finish homework*, not a market order.

## Hard stops vs other rules

- 52W high **with no base** = SPIKE, not a CSK add.
- 52W high **out of a 50-DMA coil** = possible BASE READY.
- SME circuits after a gap = SPIKE until a multi-week rest. 0.3–0.75% still applies later.
- Pillar 10 still requires MOS. A beautiful 50-DMA base at 55× is CAP.
- Compute sleeve (ESDS / E2E / Netweb): SPIKE first; MEAN-REV does not override the AI-slowdown no-add unless invoice-quality cash appears.

## Daily output stub

`name | tag | nearest DMA | vol vs spike | next action`
