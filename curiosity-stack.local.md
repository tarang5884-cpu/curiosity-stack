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
  2026-09-01 session: L0 on global semiconductor supply-chain dynamics;
  India Proxy + Semicon 2.0 policy map. Setup questionnaire not completed.

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

  - name:
    added:
    last_status:
    signal_priorities:
      - news
      - regulatory
      - new_entrants
      - funding
    triggers:
      - layer:
        condition:
        last_fired:

# ── Source Credibility ────────────────────────────

source_rating_enabled: true
source_auto_accept_suggestions: false

sources:
  - name:
    type:
    sectors:
      -
    layers:
      -
    rating:
    rated_by:
    times_cited: 0
    notes:
    last_cited:

# Domain knowledge — per-sector company intelligence
# Used by the India Proxy Agent to surface non-obvious companies
# Add companies you know via /curiosity-stack:knowledge

domain_knowledge:
  cybersecurity:
    []
  ai_data:
    []
  fintech:
    []
  ev_batteries:
    []
  pharma:
    []
  green_energy:
    []
  space:
    []
  semiconductor:
    - name: Kaynes Technology
      segment: ATMP / OSAT (power and multi-chip modules)
      note: Kaynes Semicon Sanand commercial 31 Mar 2026. Direct ISM 1.0 shipping actor. Listed parent.
      source: discovered
      added: 2026-09-01
    - name: CG Power and Industrial Solutions
      segment: ATMP / OSAT + design (Axiro)
      note: CG Semi JV with Renesas and Stars Microelectronics. Sanand commercial 4 Jul 2026. Direct ISM 1.0. Electricals parent.
      source: discovered
      added: 2026-09-01
    - name: Archean Chemical Industries
      segment: Compound fab / SiC + materials
      note: SiCSem + Neun Infra FSA with ISM 11 May 2026. Odisha SiC MOSFET/diode fab+ATMP. Chemicals parent, not CMOS foundry.
      source: discovered
      added: 2026-09-01
    - name: MosChip Technologies
      segment: Fabless design / ASIC SoC / DLI-shaped
      note: Listed fabless design house. Closest listed product-design name for Semicon 2.0 pillar 1.
      source: discovered
      added: 2026-09-01
    - name: RIR Power Electronics
      segment: SiC epitaxy / discrete power
      note: Odisha SiC path with state subsidy. Confirm ISM vs state-only aid before treating as scheme vehicle.
      source: discovered
      added: 2026-09-01
    - name: SPEL Semiconductor
      segment: Legacy OSAT
      note: Oldest India OSAT (Chennai). Execution and scale flag versus new Sanand lines. BSE listed.
      source: discovered
      added: 2026-09-01
  general:
    - Sasken Technologies: 35+ year Bengaluru-based product engineering services company (Chip-to-Cognition). Strong in automotive electronics, semiconductor design/verification, embedded systems. Acquired Borqs IoT/ODM business in Apr 2025. Key India semiconductor + auto theme play. Also listed under domain_knowledge.semiconductor via Sasken Silicon (analog/mixed-signal, RF, PMIC).
