# Data dictionary

## installations.csv (one row per active EU ETS installation, 2025 data)

| Column | Meaning |
|---|---|
| country | SI, HR or IT |
| zone | `core` or `ring` (see below) |
| installation | Installation name in the EU ETS |
| account_holder | Operator holding the account (may be a parent company, often in another city) |
| city | City of the account holder's address, not necessarily the plant |
| activity | ETS activity category as reported |
| sector | Our grouping of the activity (used for the hydrogen share) |
| h2_share | Share of CO2 we assume could be replaced by hydrogen (assumption) |
| h2_factor_t_per_t_co2 | Tonnes of hydrogen per tonne of CO2 replaced (0.149; 0.105 for ammonia) |
| co2_2025_t, co2_2024_t, co2_2023_t | Verified fossil CO2 emissions, tonnes |
| h2_potential_t_per_yr | co2_2025_t x h2_share x h2_factor (an upper-end estimate, not a forecast) |

Sector shares used: steel and metals 0.45 (aluminium 0.6), ammonia 0.9, refining 0.5, cement 0.1, lime and gypsum 0.3, glass 0.6, ceramics and wool 0.65, paper 0.8, power and heat 0.15, other 0.3. These are illustrative and need expert calibration.

Zones: `core` = all of Slovenia, Croatian postcodes 51/52/53/47 or keyword matches (Rijeka, Istra, etc.), Italian postcodes 33/34 or keyword matches (Friuli Venezia Giulia). `ring` = the rest of Croatia and Italian postcodes 30/31/35/45/48.

## airports.csv

| Column | Meaning |
|---|---|
| airport_code | Eurostat reporting-airport code |
| name | Airport name |
| pax_2023, pax_2024, pax_2025 | Total passengers (Eurostat avia_paoa, schedule and non-schedule, all traffic) |

## Sources
- European Commission, Union Registry: Verified Emissions for 2025; List of operators in the EU ETS (joined on registry and permit ID).
- Eurostat table avia_paoa.

## Known limitations
- Location is from the account holder's postcode, with name-keyword corrections. Check a row before relying on it.
- The data covers only ETS installations (large emitters). Smaller hydrogen users and non-ETS buyers are missing.
- No live signals (grants, permits, cancelled projects, supplier announcements) are in the data. They come from the weekly search.
