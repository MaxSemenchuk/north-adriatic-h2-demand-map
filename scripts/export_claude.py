"""Export the data as CSV for the Claude starter kit (claude/data/)."""
import csv, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
inst = json.load(open(root / "data/installations.json"))
air = json.load(open(root / "data/airports.json"))
out = root / "claude/data"
out.mkdir(parents=True, exist_ok=True)

with open(out / "installations.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["country", "zone", "installation", "account_holder", "city", "activity",
                "sector", "h2_share", "h2_factor_t_per_t_co2", "co2_2025_t", "co2_2024_t",
                "co2_2023_t", "h2_potential_t_per_yr"])
    for r in inst:
        w.writerow([r["c"], r["z"], r["n"], r["h"], r["city"], r["a"], r["s"], r["sh"], r["f"],
                    r["e"], r["e24"], r["e23"], round(r["e"] * r["sh"] * r["f"])])

with open(out / "airports.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["airport_code", "name", "pax_2023", "pax_2024", "pax_2025"])
    for k, v in air.items():
        p = v["pax"]
        w.writerow([k, v["name"], p.get("2023"), p.get("2024"), p.get("2025")])
print("ok", len(inst), len(air))
