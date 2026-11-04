# The census builders

The four scripts that made `../MASTER-census.csv` on 27 August 2026, copied unchanged from the study's Drive (`venue/` in the Layer A data folder). They are kept as the record of how the sheet was made. Run order:

    build_venue_activity.py  <raw24> <census_740_mapping.csv> <outdir>   _progress.jsonl: venue counts per community
    emit_tables.py                                   (in <outdir>)       venue_activity.csv, venue_summary.csv
    screen_event_talk.py     <raw24> <census_740_mapping.csv> <outdir>   _screen_progress.jsonl: the lexical screen
    build_master_census.py   <outdir>                                    MASTER-census.csv

## What stops a rerun from here

- **Paths are the study's.** `build_master_census.py` reads its inputs beside itself (`_screen_progress.jsonl`, `venue_summary.csv`, `validations.jsonl`), the mapping from `../atlas/`, and the raw folders from `../raw24*`. To rerun, copy the four scripts and those files into one folder laid out that way.
- **The coder verdicts are not shipped as a file.** `build_master_census.py` reads them from `Sandboxes/Gioia v28/case_facts.jsonl`, the coders' output of an earlier run. Their result is the `coded`, `coder_verdict` and `coder_model` columns of `MASTER-census.csv`, which is the file this repository ships.
- **raw24** comes from `data/raw24/` (download or rebuild).

The counts (`items_*`, `screen_class`, `hit_*`) can be rebuilt this way. The judgements (`validations.jsonl`, the mapping, the verdicts) are inputs and cannot.

`recount_during.py`, also in `venue/`, is left out: its output (`during_counts.jsonl`) is read by none of the four.
