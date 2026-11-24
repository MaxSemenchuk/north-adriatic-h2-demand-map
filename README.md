# North Adriatic Hydrogen Demand Map

Prototype (v0.2) that estimates who in the North Adriatic region (Slovenia, Croatia, Friuli Venezia Giulia and a wider ring) could physically buy hydrogen, and how much, plus a layer for synthetic aviation fuel (e-SAF).

**Live page:** https://maxsemenchuk.github.io/north-adriatic-h2-demand-map/ with an [About page](https://maxsemenchuk.github.io/north-adriatic-h2-demand-map/about.html) explaining what this is and why.

**Use it in Claude:** see the [starter kit](claude/README.md) to set up a Claude project with this data and a weekly brief.

## What it does
- **Industrial demand map:** about 126 active EU ETS installations (61 in the core area). Potential hydrogen demand = verified CO₂ 2025 × sector share addressable by hydrogen × 0.149 t H₂ per t CO₂ (0.105 for ammonia).
- **Price check:** break-even delivered hydrogen price from gas and ETS prices (sliders).
- **Aviation layer:** passenger traffic of eight regional airports → rough jet-fuel use → e-SAF, hydrogen and CO₂ needed under the ReFuelEU synthetic sub-mandate.
- **CO₂ source rating** for e-fuels (High / Medium / Low), based on process type.

## Caveats
- Sector shares, the fuel-per-passenger figure and the synthetic-fuel shares are **assumptions**, not validated; check them against the regulation and with sector experts.
- Location comes from the account holder's postcode, not the plant, with name-keyword corrections. Check it before relying on a row.
- ETS counts fossil CO₂ only, so biogenic CO₂ is not visible.

## Data sources
- European Commission, Union Registry: *Verified Emissions for 2025* and *List of operators in the EU ETS* (https://climate.ec.europa.eu/eu-action/carbon-markets/eu-emissions-trading-system-eu-ets/union-registry_en)
- Eurostat, table `avia_paoa` (passengers by reporting airport)

## Rebuild
Download the two Commission spreadsheets into `data/raw/` as `verified_emissions_2025.xlsx` and `operators.xlsx`, then:

```bash
pip install openpyxl
python3 scripts/build.py
```

This rewrites `data/installations.json`, `index.html` (fuel) and `hydrogen.html` from the templates in `scripts/`.

To refresh the Claude starter-kit CSVs after a rebuild: `python3 scripts/export_claude.py`.
