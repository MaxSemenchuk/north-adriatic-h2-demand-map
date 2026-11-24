# Starter kit: use the demand map inside Claude

This folder lets you set up a Claude project that knows the North Adriatic demand data and can answer questions and write a weekly brief. You do not need GitHub or any code. You need a Claude account (Team or Enterprise lets you share the project with colleagues).

## Set up (about 5 minutes)

1. In Claude, create a new **Project** (for example "North Adriatic offtake radar").
2. Paste the contents of [`INSTRUCTIONS.md`](INSTRUCTIONS.md) into the project's instructions.
3. Add these files to the project knowledge:
   - [`data/installations.csv`](data/installations.csv)
   - [`data/airports.csv`](data/airports.csv)
   - [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md)
   - [`WEEKLY_BRIEF.md`](WEEKLY_BRIEF.md)
4. Optionally share the project with colleagues (Enterprise admins can control who gets access).

## Try these questions

- Who are the five likeliest hydrogen buyers in the core area, and why?
- What would a 10 kt/yr e-SAF plant need in hydrogen, electricity and CO₂, and which local sources could supply the CO₂?
- At gas 35 €/MWh and ETS 80 €/t, what is the break-even hydrogen price? What if ETS is 120?
- Write this week's brief (see [`EXAMPLE_BRIEF.md`](EXAMPLE_BRIEF.md) for the shape).

## Weekly brief on a schedule

If scheduled tasks are available on your plan, create one that runs weekly with the prompt in [`WEEKLY_BRIEF.md`](WEEKLY_BRIEF.md). The prompt tells Claude to search for new signals, keep only items with a source link, and mark anything unverified. A person should read the brief before it goes beyond the team.

## Adding your own information

Contacts, meeting notes and deal status are your own confidential data. Add them as extra files **in your project only**; do not put them in the public repository.

## Updating the data

The data in this repo changes when we rebuild it (new Commission data each spring, new airport figures). To update your project, replace the two CSV files with the new versions from `claude/data/`. The repo's `scripts/export_claude.py` regenerates them.

## What the data is, and is not

Public data plus our assumptions. Sector shares, fuel per passenger and e-SAF mandate shares are unvalidated assumptions; locations come from account-holder postcodes. See [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md).
