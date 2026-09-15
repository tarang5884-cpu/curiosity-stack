# Sanjay Popatlal Jain — weekly bulk tracker

**Status:** flow radar. Not a buy list. Not SEBI advice.
**PAN / client string (exact):** `SANJAY POPATLAL JAIN` / `JAIN SANJAY POPATLAL`
**Do not mix with:** Jain Global LLC (US 13F), Sanjay Jain + HUF of Enviro Infra (promoter), random Sanjay Jain PANs.
**Style:** SME / listing-week bulk. High turnover. A sit is rare (Goldstar 4.53% is the exception).
**CSK size:** SME-plus only. Never 8-slot. MEAN-REV / BASE READY. No add on UC week.

## Weekly protocol (automation: `SPJ weekly bulk scan`)

Run every **Monday 08:45 IST**.

1. NSE + BSE bulk/block last 7 days — client name contains `SANJAY POPATLAL JAIN` or `JAIN SANJAY POPATLAL`.
2. Trendlyne / Primeinfobase bulk filter same string.
3. Tag each print:
   - **SIT** — buy, no offsetting sell within 5 sessions, or % of equity ≥1%.
   - **FLIP** — buy and sell same name inside 5 sessions (Technocraft, MV Electro pattern).
   - **EXIT** — sell only.
4. If SIT and not already on this file → add to table + one-line business (what they make).
5. Promote to `library/sme-tracker.md` Active only if SIT **and** user confirms. Do not auto-Live.
6. Append a Log row. If no prints: write `quiet week`.

Sources: NSE bulk deal CSV, BSE bulk, Trendlyne client search. SHP lag is 45–60 days — bulk is the live book.

## Disclosed SHP (Jun-26, exact PAN)

| Stock | Stake | Qty | ~Value | Tag |
|---|---|---|---|---|
| Goldstar Power | 4.53% NEW | 1.30 Cr sh | ~₹10 Cr | SIT |
| Takyon Networks | 1.12% | 1.60 L | ~₹29 L | leftover / small |
| Wherrelz IT Solutions | 1.03% | 4,000 | ~₹6 L | leftover |
| Indobell Insulations | 1.00% | 63,000 | ~₹50 L | leftover |

## Bulk tape seed (May–Sep 2026)

| Date | Name | Side | Qty | Avg ₹ | % vol | Tag |
|---|---|---|---|---|---|---|
| 11 Sep 26 | Qualiance International | Buy | 70,000 | 224.90 | 0.52% | SIT watch — technical garments |
| 3 Sep 26 | Kwick Forensic Solutions | Buy | 1.12 L | 155.29 | 0.52% | SIT watch — already on sme-tracker |
| 26 Aug 26 | Sham Foam | Buy | 5.32 L | 72.80 | 4.63% | SIT watch — confirm still held |
| 19 Aug 26 | (ticker TBD @ 478.55, 3 L, 0.71%) | Buy | 3.00 L | 478.55 | 0.71% | resolve ticker next scan |
| 14 Aug 26 | Technocraft Ventures | Buy 2 L / Sell 1 L | 292.71 / 307.42 | listing | FLIP |
| 11 Aug 26 | Aegeus Technologies | Buy | 1.20 L | 124.50 | 1.43% | SIT watch — CSK history |
| 6–7 Aug 26 | MV Electrosystems | Buy 2 L @ 541 / Sell 1.5 L @ 652 | — | — | FLIP |
| 30 Jul 26 | BaiKakaji Polymers | Sell | 3.42 L | 200 | 1.60% | EXIT |
| 27 May 26 | Vegorama Punjabi Angithi | Buy | 2.00 L | 118.10 | 1.20% | check if still held |
| 8 May 26 | OnEMI Technology | Buy 20.9 L / Sell 1.9 L | 198 / 225 | — | partial FLIP |
| 30 Apr 26 | Adisoft Technologies | Buy | 2.00 L | 205 | 1.23% | check |
| Mar 26 | PNGS Reva Diamond | Buy 10.3 L / Sell 3 L | 375 / 368 | — | FLIP |

## Research tickets (not orders)

1. Goldstar Power — only disclosed 4.5% sit.
2. Qualiance International — 11 Sep bulk, export/technical apparel.
3. Sham Foam — 4.6% of day volume; confirm Sep hold.
4. Kwick / Aegeus — flow confirmation only; work FV already run.

## Log

| Week of | Action |
|---|---|
| 2026-09-15 | File created. Seed from Trendlyne bulk + Jun-26 SHP. Weekly automation armed. |
