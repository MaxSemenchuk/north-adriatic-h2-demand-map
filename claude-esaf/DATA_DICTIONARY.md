# Data dictionary

All files are in `data/`. Status date is November 2026 unless stated. Confidence values are low, medium or high as assessed when collected.

## projects.csv (55 rows)
Source of the project list: Transport & Environment, "The e-SAF market" (June 2025), Annex 3; e-kerosene volumes only (the bio share of hybrid projects is already excluded).
- `e_kerosene_kt_per_yr`: announced capacity. `announced_start_year`: from the source; if not stated we assumed 2033 (`start_year_stated` = no).
- `stage_assumed`: our classification: `op` operating, `build` under construction, `feed` FEED/permitting, `ann` announced with no news.
- `lat`, `lon`: approximate site (blank if not located).
- `status_nov2026`, `status_detail`, `status_source_url`, `status_confidence`: result of a search-based status check. A summary of web search results, not a primary-source audit.

## scenarios_by_region.csv
`scenario` is announced, base or cautious (rules in `INSTRUCTIONS.md`); `year` 2030, 2032 or 2035; kt per year of e-kerosene reaching the market that year in that region. These are our assumptions, not data. The region `Associated (NO/IS/UK)` is outside the EU27: for comparison with the EU27 quota, leave it out (base case 2032: 169 kt EU27, about 173 kt with Associated). Regions with no rows (Italy, Balkans, Other EU) have no project in our list, not zero supply by design.

## region_demand_and_quota.csv, jet_fuel_demand_by_country.csv
Jet fuel (kerosene-type, excl. biofuel; international plus domestic aviation) from Eurostat nrg_cb_oil, 2024. Region requirement = share of EU27 jet fuel use x ReFuelEU quota. "Associated" (Norway, Iceland, UK, Switzerland) has no EU quota. Ukraine is not included.

## sites_ranked.csv
Ten candidate sites. `score_before_adjustment` is the 20-point score; `score_adjusted_of_20` after competition within 150 km and owner's own SAF route; `competition_and_adjustments` explains. `co2_enough_*` says whether documented CO2 covers a small (7-8 kt e-SAF) or large (60-70 kt) plant. Airport and pipeline links are verified for sites 1-5 only; the rest are plausible but unchecked. `pipeline_evidence` is the first, unverified desk assessment; `airport_pipeline_check` is the later check and wins where they differ. `co2_documented_volume` can show two numbers, for example "~690 kt (about 490 stated)": the first adds derived estimates to the stated figures, the second is only what sources state; prefer the stated one when being cautious.

## co2_sources.csv
`class_our_label`: bio (biogenic), mixed (waste-to-energy, cement) or fossil. `number_meaning` says what the kt figure refers to (capacity, plant total, estimate). Several volumes are derived or old; read `confidence`.

## ft_directory.csv
Operating, planned and technology-provider Fischer-Tropsch units. `status`, `capacity`, `kerosene_saf_capability` and a contact note per row.

## actors.csv and actor_relations.csv
Nodes (`type`: developer, investor, offtaker, public_funder, refiner_energy, tech, alliance, other) and edges (`relation`, date, source, confidence). Public information only.

## balkans_scan.csv, ukraine_scan.csv
Refineries, hydrogen and e-fuel projects and other relevant facts for regions with no e-SAF project. Coordinates can be approximate or blank.

## Known limitations
- No project found in Italy, the Balkans, Ukraine or Switzerland; may be a data gap.
- CO2: registry-level data (EU ETS, E-PRTR) was not joined; those registries have no biogenic column.
- 2026 status is from search summaries. Scenario probabilities are our assumptions.
- Intermediary fees for investor introductions can need a licence in some countries (for example Austria and Liechtenstein); keep the role to data and analysis and ask a lawyer.
