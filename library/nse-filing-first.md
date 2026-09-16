# NSE filing first — why is this stock moving?

**Embedded:** 16 Sep 2026  
**Runs in:** CSK daily scan (`c587c14c`) and Daily winners forensics (`b614c787`) every weekday 08:15 IST  
**Sits before:** X / Suresh / news tabs / spike tags

## The rule

Before you search X for why a name moved, check what the company told the exchange.

Do not start with 10 news websites. Start with the disclosure.

## Path

NSE → Corporate Filings → Announcements

URL: https://www.nseindia.com/companies-listing/corporate-filings-announcements

From there:

- Search a company (F&O names included)
- Search a keyword
- Filter by date (default last 5 sessions, T-4 to T)
- Scan the F&O universe when the board is noisy

SME / BSE-only names: same check on BSE Corporate Announcements.

## What you are hunting

- Orders received / LoA / LoI / PPA / COD
- M&A / agreements / MoUs
- Project / capacity updates
- Regulatory actions (SEBI, SAT, penalty, rating)
- Deals / blocks that were *filed*
- Business updates / results
- Other material Reg-30 items

## Tags

| Tag | Meaning |
|-----|--------|
| ORDER | Dated award / LoA / LoI with counterparty |
| AGREEMENT | MoU / JV / offtake — not an invoice |
| PROJECT | Capacity / COD / capex progress |
| REG-30 | Other material event |
| REGULATORY | SEBI / SAT / penalty / rating watch |
| DEAL | Acquisition, stake, scheme |
| RESULT | Earnings / board meeting outcome |
| NOTHING | No filing in the window. X is flow or rumour. |

## Hard stops

- Bucket **A (earnings)** or **B (order/COD)** only if a dated exchange PDF exists.
- X thread with no filing = **F (narrative)** or **H (unknown)**.
- Cite subject + timestamp on the card.
- If NOTHING, say NOTHING, then you may open X.
- Filing exists ≠ add. Still run invoice / MOS / spike-DMA rules.

## Daily output stub

`name | % | filing Y/N | type | subject+time | X only if NOTHING`
