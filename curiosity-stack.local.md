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
