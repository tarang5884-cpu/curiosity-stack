# Curiosity Stack — Personal Context
# Fill this in via /curiosity-stack:setup or edit directly.
# This file is read at the start of every session.

# ── Core Context ─────────────────────────────────

context:
  geography:
themes:
  -
watchlist:
  -
deprioritise:
  -
default_output:
  text_size: comfortable
notes: |
  2026-09-01 session: L0 semiconductor; Semicon 2.0 map; morning-brief locked to MOS list.
  Tracking GE Vernova T&D tape (GVT&D) as liquid T&D hold vs Yash HV.
  Devson Catalyst Hold/Queue (work 190-240; add only <=200).
  CleanMax Hold (work 1050-1400 RR-EBITDA; add only <=1050 IPO). FII 29.8->11.2 Mar-Jun.
  Setup questionnaire not completed.

# ── Decomposition Library ─────────────────────────────

library_save: ask
library_mirror: local
library_count: 1
session_count: 1

# ── Watchlist Monitoring ────────────────────────────

watchlist_cadence: weekly
watchlist_last_run:
watchlist_email:
watchlist_email_enabled: false
watchlist_cowork_summary: true

watchlist_topics:
  - name: Sasken Technologies
    added: 2026-05-16
    last_status: Tier 1 - Chip-to-Cognition (Semiconductor Design + Automotive Electronics + IoT/ODM)
    signal_priorities:
      - news
      - earnings
      - regulatory
      - orders
    triggers:
      - layer: L5
        condition: Major automotive Tier-1 design win OR strong Borqs integration synergy numbers in quarterly results
        last_fired: null
      - layer: L2
        condition: Announcement of PLI 2.0 semiconductor design incentives or new government order
        last_fired: null
      - layer: L3
        condition: Margin expansion above 35% or new high-value design contract
        last_fired: null

  - name: India Semicon 2.0 / ISM FSAs
    added: 2026-09-01
    last_status: Guidelines notified 31 Aug 2026; 1.0 plants shipping at Sanand; 2.0 applications not yet a public list
    signal_priorities:
      - regulatory
      - news
      - new_entrants
      - funding
    triggers:
      - layer: L0
        condition: MeitY or ISM publishes first Semicon 2.0 application shortlist or additional gazette categories
        last_fired: null
      - layer: L4
        condition: New Fiscal Support Agreement signed under ISM or Semicon 2.0 (any fab, ATMP, equipment, or materials project)
        last_fired: null
      - layer: L5
        condition: Listed India company discloses a Semicon 2.0 application, FSA, or scheme-linked capex with a named pillar
        last_fired: null
      - layer: L3
        condition: Advanced packaging (2.5D/3D/WLCSP) project approved in India, or silicon 300mm fab FSA beyond Tata Dholera
        last_fired: null

  - name: GE Vernova T&D India
    added: 2026-09-01
    last_status: Hold / liquid T&D vs Yash HV. Close 31 Aug 2026 Rs 4445. Q1 FY27 execution strong, order intake -30% YoY.
    signal_priorities:
      - earnings
      - orders
      - news
      - regulatory
    triggers:
      - layer: L3
        condition: Quarterly order inflow returns above Rs 2,000 Cr or US data-centre / pending export package is booked into the order book
        last_fired: null
      - layer: L4
        condition: HVDC developer award (Lakadia restart, Begunia path, or new Khavda-class HVDC) names GVT&D as equipment supplier
        last_fired: null
      - layer: L0
        condition: Print breaks Rs 4,000 on volume or retests Rs 5,650 52W high; or FII/DII shareholding swing greater than 150 bps in a quarter
        last_fired: null
      - layer: L5
        condition: Semiconductor-fab or data-centre transformer order disclosed (Q1 already had a 155 MVA / 245 kV semiconductor customer print)
        last_fired: null

  - name: Devson Catalyst
    added: 2026-09-01
    last_status: BSE SME 544823. Hold / queue. Last Rs 259.5 on 25 Aug. Work 190-240; floor 150-170; add only <=200. No MOS at CMP.
    signal_priorities:
      - earnings
      - news
      - orders
      - regulatory
    triggers:
      - layer: L4
        condition: Gujarat expansion COD or first utilisation print on the new catalyst/adsorbent lines (target 2545 to 7633 MTPA)
        last_fired: null
      - layer: L3
        condition: Quarterly sales run-rate holds above Rs 14 Cr or PAT margin prints below 15%
        last_fired: null
      - layer: L5
        condition: Named refinery, fertilizer, steel, or petrochemical qualification / repeat order disclosed
        last_fired: null
      - layer: L0
        condition: Print trades at or below Rs 200 on the BSE SME tape, or volume dries under 20,000 shares for a week
        last_fired: null

  - name: Clean Max Enviro Energy Solutions
    added: 2026-09-01
    last_status: NSE CLEANMAX. Hold. Last Rs 1247 on 31 Aug. Work 1050-1400 on 12-15x run-rate EBITDA; floor 740-850; add only <=1050 IPO. FII 29.8 to 11.2 Mar-Jun 2026.
    signal_priorities:
      - earnings
      - news
      - orders
      - regulatory
    triggers:
      - layer: L3
        condition: Quarterly run-rate EBITDA print below Rs 1,700 Cr or project debt cost back above 9%
        last_fired: null
      - layer: L4
        condition: Envision 1,550 MW WTG term sheet converts to a firm supply + commissioning schedule, or Bikaner-2 curtailment print worsens from ~30%
        last_fired: null
      - layer: L5
        condition: Named hyperscale / Data-and-AI PPA disclosed in GW terms (segment already 42% of contracted book)
        last_fired: null
      - layer: L0
        condition: Print trades at or below IPO Rs 1,053, or FII holding prints another 300 bps down in a quarter
        last_fired: null
