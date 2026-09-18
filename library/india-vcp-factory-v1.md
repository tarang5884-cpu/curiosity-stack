# India VCP Factory v1.0
**Module type:** Setup execution engine (not a second morning universe dump)  
**Trigger:** `/curiosity-stack:india-vcp-scan`  
**Parents:** Kovainvest/CAN-SLIM process + Running Horse + Trade Factory (DEP) + CSK One Scan  
**Universe feed:** `library/csk-momentum-scan.md` pass list + `watchlist.md` Tier 1–3  
**Rule:** Do not replace the 08:15 CSK morning brief. This module grades *setups* on names that already passed trend/quality gates.

Not SEBI advice. Research framing only.

---

## Why India needs a rewrite, not a copy-paste

US CAN-SLIM assumes 13F lag, deep float, no circuits, clean volume. NSE reality:

- Delivery % is the only daily proxy for who took the shares home.
- F&O names contaminate volume on expiry / weekly options.
- Circuits (5/10/20%) kill chase entries.
- News often gaps first, then coils (DEP). The real buy is the tight pullback, not the gap day.
- Mid/small leadership can diverge from Nifty.
- Promoter selling + retail delivery spikes can fake institutional tape.

Keep Kovainvest process (filter → wait → VCP/pocket pivot → hard stop → pyramid winners → journal). Swap sensors for NSE.

---

## 0. Market Regime Gate (M) — run first

| Signal | Bull / Confirmed | Pause | Risk-off |
|--------|------------------|-------|----------|
| Nifty vs 50-DMA | Above | Oscillating | Below + falling |
| Midcap100 & Smallcap100 vs 50-DMA | At least one above | Mixed | Both below |
| Distribution days in last 20 sessions | ≤3 | 4 | ≥5 |
| FII index-futures net | Covering or stable | Rebuilding shorts | Fresh extreme shorts + cash sell |
| Breadth (adv/dec 20d) | Expanding | Flat | Contracting |

**Position permission**
- Confirmed: up to 4–5 names, max 25% each, total equity 70–100%.
- Pause: 1–3 names, total equity ≤50%. Only VCP final-contraction or DEP tight-flag.
- Risk-off: cash ≥70%. No new breakouts. Trail existing with 21-EMA / 50-DMA.

If regime = risk-off, output is regime + do-nothing. Do not force a buy list.

---

## 1. Four-dimension filter (all must pass)

### A. Fundamentals
- Quarterly EPS / PAT YoY ≥ 20% (25% preferred).
- Revenue YoY ≥ 15% (20% preferred). Acceleration last 2 quarters is a plus.
- ROCE ≥ 12% (15%+ preferred). D/E ≤ 0.7 unless WC-heavy with clean cash conversion.
- Hard fail: two consecutive quarters of EPS deceleration 30% → 10% or worse with no disclosed one-off.

### B. Technicals
- Price > 50-DMA; 10-DMA ≥ 20-DMA (or 10 crossing 20 this week).
- Within 20% of 52-week high (CSK uses 15%; Factory allows 20% only if VCP is tightening into HVN).
- RS percentile ≥ 80 vs NSE (Kasauti/RSRank), ideally ≥ 90, or 90-day outperformance vs Midcap100 / Smallcap100.
- Preferred stack: 50 > 150 > 200 DMA, 200 rising.

### C. Sponsorship (India 13F substitute)
Need two of four:
1. Promoter holding flat or up last 2 quarters.
2. FII or DII/MF stake up QoQ (≥ 0.3–0.5 pp).
3. Delivery % on up-days ≥ 50% midcap / ≥ 45% smallcap, and above that name’s 20-day median.
4. Volume Profile: HVN support under price, not HVN overhead + LVN air under price.

Hard fail: promoter pledge spike, promoter bulk sell, ASM/GSM, delivery spike only on down-days.

### D. Environment
Regime Gate must not be risk-off. Sector RS in top half, or isolated leader with dated NSE filing catalyst.

---

## 2. Scanner

```
Market cap ₹500 Cr – ₹50,000 Cr
AND Price ≥ ₹80
AND Close > 50-DMA
AND 10-DMA ≥ 20-DMA
AND Dist from 52W high ≤ 20%
AND 3Y sales growth ≥ 15% OR latest quarter sales YoY ≥ 15%
AND ROCE ≥ 12%
AND D/E ≤ 0.7
ORDER BY 3-month return DESC
```

Liquidity: 20-day ADV ≥ ₹3 Cr for new entries (MOS names may use ₹1.5 Cr at half-size). Prefer non-F&O. If F&O, ignore expiry-week volume; use delivery.

Three chart passes: kill ugly → keep VCP/flat/DEP flag → keep live final contraction or this-week pocket pivot → **8–12 Factory Watch**.

Daily job = did any Factory Watch name print a trigger today?

---

## 3. Setup definitions

**True VCP:** price + volume + range all contracting. Pivot = high of final contraction. Trigger = close above pivot AND volume ≥ 1.4× 50-day avg AND delivery not collapsing. Buy zone = pivot to pivot + 4%. No chase.

**Pocket pivot:** up-day volume > highest down-day volume of prior 10 sessions, price holding 10-DMA/21-EMA, delivery ≥ 20-day median.

**DEP tight-flag:** news/gap then 5–15 session tight pullback that does not give back the gap. Entry = reclaim of flag high on volume.

**VP confirm:** trigger out of HVN support or through thin LVN. Fail if breakout into thick overhead HVN with no volume.

---

## 4. Stops, adds, sells

Stops: tightest of final-contraction low / pivot−1–1.5% / entry-day low−1% / 21-EMA, never > 8%.
Time stop: 10 sessions with no +3% progress (15 only if Confirmed and holding 10-DMA).

Pyramid 50/30/20 on winners only. Never add >5% above original pivot. Never add in Pause/Risk-off.

Sell: +20% in 15 sessions → hold 6–8 weeks unless climax; churn → trim 50%; 50-DMA heavy-volume break or earnings gap through 50-DMA → exit same session.

Max 5 names, 25% cap. 3 straight stops → half size. 5 → one week no new risk.

---

## 5. Daily scan output

**India VCP Factory | [DD MMM YYYY] | Regime:**

1. Regime card
2. Factory Watch (max 12)
3. Actionable (max 4): entry | stop | add | invalidation | size
4. Rejects
5. Open book
6. Do-nothing line if empty

≤ 450 words after tables.

## 6. Journal

Date | Name | Why | Regime | Pivot | Entry | Stop | Add | Delivery | Filing | Exit | R | Error tag
