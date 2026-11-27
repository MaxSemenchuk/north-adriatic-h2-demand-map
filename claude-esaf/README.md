# Starter kit: use the Europe e-SAF map inside an AI chat

Live map: https://europe-esaf.pages.dev

This folder lets anyone ask questions about the data behind the map, in plain language, without code.

## Fastest way (no setup)
Paste this into Claude or ChatGPT (a version with web access):

> Read https://raw.githubusercontent.com/MaxSemenchuk/north-adriatic-h2-demand-map/main/claude-esaf/INSTRUCTIONS.md and the files it lists in the same repository (folder `claude-esaf/data/`, meanings in `DATA_DICTIONARY.md`). Follow those instructions. Then answer: <your question>

If the chat cannot open links, upload the files instead.

## Set up a Claude project (about 5 minutes)
1. Create a new **Project**.
2. Paste [`INSTRUCTIONS.md`](INSTRUCTIONS.md) into the project instructions.
3. Add [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) and all files from [`data/`](data/) to the project knowledge.

## Try these questions
- Where is the gap between the ReFuelEU quota and realistic supply in 2032, by region?
- Which candidate sites look best, what could stop them, and who owns the refinery?
- Who works with whom among developers, and which funders have a reason to care?
- If our Fischer-Tropsch partner fails, which alternatives exist?
- What would it take for Ukraine to host an e-SAF plant?

## What the data is, and is not
Public data plus our assumptions. Scenario results are not forecasts; CO2 volumes and 2026 statuses have limits; every row carries a confidence. See [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md).

Contacts, meeting notes and anything confidential belong in your own project files, not in this public repository.

The older Adriatic starter kit is in [`../claude/`](../claude/).
