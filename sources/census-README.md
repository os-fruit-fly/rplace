# The census

The files that decide which communities are rooms. They record judgements, so they cannot be regenerated from downloads; [the census page](../../Manual/census.md) explains each step from 1,473 atlas artworks to 706 communities.

| File | What it holds | Kind |
|---|---|---|
| `MASTER-census.csv` | one row per community (777: the 763 the atlas links, 4 named on the canvas, 9 credited in atlas descriptions, and r/TFLS, a redirect): its counts in each window, the lexical screen, the coder's verdict, the validation, and `handable` (1 for the 706) and `disposition` | counts from raw24, plus the judgements below applied |
| `census_740_mapping.csv` | each community and the atlas artworks credited to it, with its window counts | the atlas links as resolved by hand |
| `atlas_35_resolution_worksheet.csv` | the 35 links that matched no downloaded community at first, and the candidates for each | working sheet of the resolution |
| `atlas_link_unresolved.csv` | the 15 links that remain, and why each is not a community | judgement |
| `screen_audit.csv` | the rooms a coder read as `none`, beside their screen hits | the check that the screen and the coders agree |
| `validations.jsonl` | rooms whose membership a reading decided, with the evidence: four the screen flagged (27 August 2026), four named on the canvas and the Robin room behind a truncated link (26 September 2026) | judgement |
| `ROOM-RULES.md` | what counts as a room, rule by rule, for this yard and for venues_yard; the 706 rooms and the 71 discarded rows by Reddit's own name and id, and the links and makers that name no community (2026-10-04) | the rules stated; names from each venue's record |
| `ROOM-LIST.tsv` | the same lists, one line per name: reddit_name, subreddit_id, census_sub, status, coded, in_yard, disposition, why, name_source | data |
| `artworks_outside_population.csv` | the atlas artworks that credited none of the population on 26 September 2026 (312; three have since moved to r/TheFarLeftSide, and two more left on 4 October 2026 with r/lehigh and r/upvote, #1725 and #1250, not added as rows): why each is outside, its size, overlap with credited artworks, surviving-pixel authors, and a `kind` read from its description ([the report](../../Manual/artworks-outside-the-population.md)) | counts from the atlas and the placement record, plus a judgement (`kind`) |

Built 27 August 2026 and rebuilt 26 September 2026 (two records collected again, three links resolved, four communities from the canvas) by `build_master_census.py` and its three companions, in [builders/](builders/README.md) with the run order and what a rerun needs. A handler starting a yard takes the rooms with `handable = 1`.

## Changed 4 October 2026

The rule for being there is writing about the event during the 73 hours the canvas was open, not any post in them (J: "we need only communities in which there was some writing"). Two rows changed by hand in `MASTER-census.csv`, each with its reason in `validation_note` and a line in `validations.jsonl`: r/lehigh (`event_talk_after_freeze`, a new disposition: posts while the canvas was open, but its writing about the event begins at hour 78.98) and r/upvote (`screened_out`: its one coded thread names no canvas, drawing or placement). `handable`, `in_population` and `positive` are 0 for both; `coder_verdict` stays as the coders wrote it. The population is 706. The builders, kept unchanged as the study's record, do not know the new rule; a rebuild needs these two validations applied after it.
