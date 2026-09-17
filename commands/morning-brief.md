---
name: morning-brief
description: >
  Lean morning brief. Runs the ONE CSK momentum scan, then overlays the locked watchlist.
usage: "/curiosity-stack:morning-brief"
example: "/curiosity-stack:morning-brief"
---

# India Daily Edge — Master Morning Brief

**One scan only.** Source of truth:
- `library/csk-momentum-scan.md` (the screen)
- `watchlist.md`
- `library/nse-filing-first.md`
- `library/spike-dma-base-rule.md`
- `THESIS-supply-chain-MOS.md`

Do not run a second winners-forensics pass. Do not dump Board-99 as a separate product.
Do not promote kill-list names into Tier 1 or 8-slot.

### Screen (mandatory first block)

```
Close > 20 DMA
AND 20 DMA > 50 DMA
AND Dist from 52W high < 15%
ORDER BY 3-month return DESC
Default: mcap > ₹2,000 Cr
```

Watchlist / SME-core names that fail the mcap gate may appear in an appendix if they still pass the DMA + 52W test.

### Locked Watchlist (synced 2026-09-13 rev 6)

**Tier 1 – MOS Add set**  
NLC India | Reliance Industries | Varroc | MSWIL | Pitti Engineering | Aurionpro | Merritronix | Himadri Speciality | ISGEC | INOX Wind

**Tier 2 – Hold / no MOS at CMP**  
Kilburn | Yash Highvoltage | GE Vernova T&D | TARIL / TRIL | **CleanMax** | Devson Catalyst | BLEL | Metalic Technoforge | Marine Electricals | Shree Refrigerations | KMEW | CFF Fluid Controls | QPower | ABS Marine

**Tier 3 – Queue / dip only**  
Indo-MIM | Centum | Astra | Data Patterns | GFL | Neogen | Precision Wires | Harsha | Goodluck | **CleanMax ≤₹1,050** | BLEL ≤₹320 | Metalic ≤₹105 | Shree Ref ≤₹300 | Devson ≤₹200 | OBSCP ≤₹480 | Millworks ≤₹650 | Yash HV ≤₹750

**Do not scan unless HIGH filing**  
OBSCP at ~₹870 | Millworks | Vivid | Avana | Omnitech | DIACABS | SETL | Aimtron | aero 55–300× | ESDS circuits

### Strict Process
1. Latest completed cash session only.
2. Run the momentum screen. Cap pass-list at 25.
3. NSE filing first on every passer and every locked name that moved ±3%.
4. Spike / MEAN-REV / BASE READY tag. 8-slot only BASE READY or MOS add-zone.
5. Overlay Tier 1–3: which locked names *also* passed the screen vs which failed 20>50 or are >15% off high.
6. Pulse one line: Power T&D, C&I RE, Defence, Precision, Specialty materials.

### Output
**India Daily Edge | [Date]**  
**Market Bias**: one line

1. Momentum pass list (table)
2. 8-slot
3. Locked-list overlay (passed / failed screen)
4. Filing table
5. Mean-rev / spike watch
6. Action Summary (max 4 lines)

### Hard Rules
≤ 500 words after tables. Primary sources. Research framing only — not SEBI advice.

Generate today’s brief now.
