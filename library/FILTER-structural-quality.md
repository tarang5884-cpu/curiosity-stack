# Filter — structural runway + business quality

**As of:** 18 September 2026  
**Cadence:** Monday **08:20 IST** automation `Weekly structural-quality sector filter`  
**Lists it owns:** [`watchlist.md`](../watchlist.md) (mainboard) · [`SMEwatchlist.md`](../SMEwatchlist.md) (SME)  
**There are no other watchlists.** `library/sme-*.md` files are stubs.

A name stays on an *action* list only if it clears **both** gates. A name sits on **exactly one** of the two lists.

Next scheduled run: **Monday 21 Sep 2026, 08:20 IST**.

---

## 0. Weekly job

Each Monday the automation:
1. Reads this file + `watchlist.md` + `SMEwatchlist.md`.
2. Applies theme + quality gates.
3. Moves a name between the two files if it listed up / stayed SME.
4. Cuts / restores / tags NO-ADD.
5. Pushes a dated log block here.
6. Sends Tarang a one-page delta.

Restore a cut name **only** if a filing changed the SKU.

## 1. Theme gate — structural runway (2026–30)

| Theme | What counts | What does not |
|---|---|---|
| **Defence** | Qualified parts, fluid, electro, aero, sensors with named OEM / MoD book | Caption, charter aviation, forensic kits |
| **Power** | T&D OEM, HV SKU, cables, line-pipe, genset, grid cooling, funded RE | Listing-week boiler, coal-steam with RPT |
| **Technology manufacturing** | EMS / ESDM, precision electronics, OFC invoice glass, DC design with cash | GPU-rental lottery, colo IPO, CCTV vs China |
| **Biotech / energy materials** | CDMO / formulation with export proof; carbon / catalyst for steel, LFP, H2 | Fragrance, hospital roll-up, device one-liner |

Precision auto stays only if the shop is quality and the part is hard to skip.

## 2. Quality gate

- No scarce SKU  
- Top-10 ~100% and no second geography  
- Unexplained RPT >15%  
- CIRP / pledge circus  
- SME with no exit and no work-FV MOS  
- Peak-margin + peak-PE as the only story (NO-ADD, not auto-delete from universe)  
- Book <0.5× sales while targeting 3×  
- Policy-toy or listing flow

## 3. Which file

| If | Then |
|---|---|
| NSE / BSE mainboard | `watchlist.md` |
| NSE Emerge / BSE SME | `SMEwatchlist.md` |
| Migrates off SME | Move the row. Do not copy. |

## 4. CUT log — 18 Sep 2026 (seed)

See git history of rev 8 for the full prune. Apparel / forensic / fragrance / parking / charter / one-liner flow stay cut.

## 5. Week log

| Week of | Cuts | Restores | Notes |
|---|---|---|---|
| 2026-09-18 | seed prune (~45) | — | Two-list split. |
| 2026-09-21 | *(automation)* | | First scheduled run. |
