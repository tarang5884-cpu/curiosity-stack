---
name: mos-consensus
description: Run MOS + market consensus price algorithm on a name.
usage: "/curiosity-stack:mos-consensus"
example: "/curiosity-stack:mos-consensus Devson Catalyst"
---

Read `library/mos-consensus-algorithm.md`.
Use dilution-adjusted EPS. If no Street TP, set P_cons = CMP.
Cap C×T×R at 1.60. Peak-margin years use blended OPM.
Undisclosed order TCV does not lift SPP.
Output the standard MOS card. Rank is not a buy.
