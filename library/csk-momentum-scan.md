# CSK One Daily Scan — Short-Term Momentum Screener

**Live:** 17 Sep 2026  
**Replaces:** split daily jobs (CSK 99-board + Daily winners forensics). Those rules now live *inside this file*.  
**Automation:** `c587c14c` weekday 08:15 IST only.  
**Paused:** `b614c787` Daily winners forensics (merged). Weekly AI/DC and SME scans stay.

Regime: small/mid bull from Apr-2026 is pausing. Scan for *still-in-trend, not-extended-beyond-15%* names. Not a chase list.

## Hard screen (must all be true)

```
Close > 20-DMA
AND 20-DMA > 50-DMA
AND Distance from 52-week high < 15%
     i.e. Close >= 0.85 × 52W high
ORDER BY last-3-month return DESC
```

**Default liquidity gate (8-slot / live):** market cap **> ₹2,000 Cr**.  
Turn the gate **OFF** only for names already on `watchlist.md` or `library/sme-best-core.md`. Those go in the SME appendix, never auto-8-slot.

Optional confirm (tag, do not hard-fail): volume ≥ 20-day average on the session you score.

Chartink / StockEdge equivalent:
- Price > SMA(close,20)
- SMA(close,20) > SMA(close,50)
- (52WeekHigh − Close) / 52WeekHigh * 100 < 15
- MarketCapitalization > 2000
- Sort: ROC(close,63) descending (use 60–63 sessions = ~3 months)

## Universe

1. All NSE + BSE mainboard that pass the four lines.  
2. Flag overlap with Board-99 (old CSK roster) and `watchlist.md` MOS / Hold / Queue.  
3. 52W-high tape of the last session is **not** a separate scan — it is a column on this list (`Dist 52W %`).

## After the screen — not a second job

Run **in this order** on every name that passed:

1. **NSE filing first** (`library/nse-filing-first.md`). Tag ORDER / AGREEMENT / PROJECT / REG-30 / REGULATORY / DEAL / RESULT / NOTHING. X only if NOTHING.
2. **Spike → DMA** (`library/spike-dma-base-rule.md`). Tag SPIKE / MEAN-REV WATCH / BASE READY / FAILED BASE.  
   Note: this screen *already* requires Close > 20 > 50, so FAILED BASE cannot pass. SPIKE still can (price near 52W, no 2–4 week base).
3. Why-bucket (one primary): A Earnings · B Order/COD · C Sector · D Policy · E Flow · F Narrative · G Tape only · H Unknown. A/B only with a dated PDF.
4. Watchlist overlay: MOS add / Hold / Queue / Kill / AI-DC sleeve. Do not promote Kill names to 8-slot.

## Output (single table + stubs)

**CSK Momentum | [session date] | Nifty / Midcap100 / Smallcap100 %**

Market bias: one line (trend / pause / risk-off).

### Pass list (max 25)
`# | name | CMP | mcap | 3M % | Dist 52W % | 20DMA | 50DMA | vol/ADV | filing | tape tag | watchlist | next`

Sort is **3M return desc**. Cap at 25. If >25 pass, keep top 20 by 3M and force-include any MOS-list name that also passed.

### 8-slot (max 8)
Only **BASE READY** or **MOS add-zone**. DC ≤4. No SPIKE. No mcap < ₹2,000 Cr unless already MOS and sized 0.3–0.75%.

### Mean-rev watch
Passed screen last week, now losing 20-DMA or Dist 52W > 15%. Heading to 20 then 50.

### Filing movers
Names ±3% or volume ≥3× ADV: subject + time.

### Rejects (one line)
Failed mcap gate / ASM / listing < 60 sessions / ETF.

Hard rules: ≤500 words after the table. Cues not buys. Not SEBI advice.

## What was deleted from the daily stack

| Old piece | Fate |
|-----------|------|
| CSK Board-99 as a *separate* universe dump | Overlay column only |
| Daily winners forensics as a *second* 08:15 job | Why-bucket + full cards folded into Pass list |
| Forging sleeve daily table | Keep as a *column tag* if a forger passes the screen; no forced 13-name dump |
| 52W-high count as its own product | Dist-52W column |

Weekly AI/DC (`c73d66fc`) and SME X scan stay. Do not recreate a second weekday 08:15 automation.
