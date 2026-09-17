# MOS + Market Consensus Price Algorithm v1.1

**Locked after Devson Catalyst live test:** 17 Sep 2026  
**Parent:** Fair Value Module v2.1  
**Does not replace:** J-Curve, liquidity gates, spike-DMA, NSE-filing-first

Purpose: decide *how far below work FV you may pay* after the tape and the Street have already voted. Consensus is a ceiling check. MOS is taken from **your** mid-cycle floor.

---

## Fine-tunes from the Devson test (do not skip)

1. **Dilution-adjusted EPS only.** Post-IPO / bonus / fresh issue: PAT ÷ *current* shares. Devson FY26 PAT ₹12.52 Cr on 1.3588 Cr shares = **₹9.21**, not the pre-issue ₹12.22. Using 12.22 understates PE by ~25%.
2. **No broker coverage → P_cons := CMP.** Do not invent a Street TP. MOS still vs work FV.
3. **Undisclosed TCV cannot lift SPP or FY27 EPS.** “Orders from NMDC and Tata Steel” with no rupee figure = Engine B partial, SPP = 0.
4. **Cap C × T × R at 1.60.** Uncapped product sent Devson MOS to 90%. That is a “no add”, not a number.
5. **Peak-margin year:** blend last-3-year OPM before multiplying. Devson FY26 OPM 30% vs FY24 15% / FY25 20%. Use mid-cycle ~22%, not 30%.
6. **Sales flat + PAT up = fake J-curve check.** Cap stage at 2 until revenue accelerates with the new capacity.
7. **SME ADV < ₹3 Cr:** MOS_base floor 35%, size ≤ 0.5%, never institutional FV.

---

## Three prices

| Symbol | Definition | Role |
|---|---|---|
| P_work | Mid-cycle EPS × M_base, probability-weighted FY27/28/29 (60/30/10) | Intrinsic |
| P_adj | P_work × (1 + SPP), SPP 0–25% only if earned | Defensible ceiling |
| P_cons | Median broker TP, or consensus EPS × consensus PE. If none: **CMP** | What the market already paid |

```
P_add = P_adj × (1 − MOS_req)
```

If P_cons > P_adj by >15%: Street is paying CAP. Do not lift M_base. Widen MOS.
If CMP > P_adj and CMP ≥ P_cons: trim. MOS is gone.

---

## MOS_req

```
MOS_req = min( MOS_base × C × T × R , MOS_cap )
MOS_cap = 0.50 SME / thin float ; 0.40 liquid
```

### MOS_base

| Type | Base |
|---|---|
| Fortress compounder (net cash, ROCE ≥20%, 3-yr visibility) | 15% |
| Quality growth / export / qualified OEM | 20% |
| Capex J-curve / Stage 2 | 30% |
| SME / thin liquidity / circuit-prone | 35–40% |
| Commodity / peak-margin cyclical | 40% |

### Cycle C

| State | C |
|---|---|
| Early / Stage 2 utilisation rising | 0.85 |
| Mid-cycle | 1.00 |
| Late / peak margin + peak PE | 1.35 |

### Tape T

| State | T |
|---|---|
| BASE READY + V+ / dry coil | 0.90 |
| MEAN-REV into 20/50 with delivery | 1.00 |
| SPIKE / Dist-52W <5% after vertical / circuit | **no add** |
| Break 50 or 200 DMA on V− | 1.25 or kill |

### Regime R (India, review quarterly)

| Bucket | R |
|---|---|
| Liquid large-cap quality | 1.00 |
| Midcap expensive-but-earning | 1.10 |
| Small / SME / theme already rerated | 1.20 |

---

## When SPP (premium multiple) is allowed

All six must hold. Else SPP = 0.

1. J-Curve Stage 3 with leverage **and** cash
2. Mix / export / qualification is invoicing with a dated TCV
3. ROCE mid-teens+ or turning after documented capex
4. Assigned multiple ≤ peer median +20%
5. Tape is BASE READY, not listing-week / circuit
6. Not a peak-margin + peak-PE print

---

## Standard output card

```
MOS card | [Name] | [date]
CMP / mcap / diluted EPS / trailing PE
P_work band | P_adj | P_cons | P_add
MOS_base, C, T, R → MOS_req
Stance + size cap
Kill switch
```

Callable: “Run MOS-consensus on [ticker]”
Related: `library/fair-value-module-v2.1.md`
