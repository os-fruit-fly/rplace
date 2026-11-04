# For agents: data

This folder holds scripts and READMEs only; every store is downloaded or built in place. [README.md](README.md) gives the order; each store's README has what it holds, how to build it, what was tested, and a codebook.

- The fast stores, minutes each, in this order: `bash pixels/get_pixels.sh`, `bash atlas/get_atlas.sh`, `python3 pixels-per-artwork/code/fetch_sources.py` and `bash pixels-per-artwork/run_all.sh`, `python3 pixels-hourly/build_pixels.py` (needs the two member lists in `pixels-hourly/LINK.md`).
- Each script checks its output against the study's counts and stops if they differ. Trust a stop; do not work around it.
- The text stores (`users/`, `venues-placers/`, `raw24/`) take days against the arctic-shift archive and are resumable.
- Never commit what the scripts write; `.gitignore` lists it.
