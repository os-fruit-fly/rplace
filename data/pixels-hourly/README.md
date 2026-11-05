# Hourly pixels per community

`pixels.csv`: one row per community per hour, hours -16 to 72 from the canvas opening, for the communities of the census the member lists were made for: the study's 763, plus 13 added to the census on 26 and 27 September 2026, whose lists were made with `--lists-from-raw24` from `Layer A/raw24_additions` and appended (r/chelseafc's and r/hyperlightdrifter's lists were remade the same way from their full records). Twelve of the 13 have no atlas link; their regions are the artworks in `data/atlas/credits_beyond_links.csv`, and r/tenma has none. The aggregator's canvas step (`aggregator/handler/build_canvas.py`) keeps the frame's rooms and the run reads them as `package/pixels.csv`; `mem.py canvas` shows each room's share placed by its own members.

    sub, hour_since_open, px_in_region_any, px_by_pre_members, px_by_window_members

A placement counts for a community if it lands in the union of the atlas artworks that link to it. `px_by_pre_members` counts those by people who posted in the subreddit in the 168 hours before the opening; `px_by_window_members`, by people who posted from the opening to seven days after the freeze. Members are matched to placers by hashing the username as the record does. Regions overlap (1,231,586 pixel-community pairs on 921,826 pixels), so a rate per community is sound and a sum across communities is not.

**Build it** (from `data/`; needs the record, `pixels/get_pixels.sh`, and member lists: the study's are not public (`LINK.md`), so the second command makes them from raw24; numpy and Pillow, pandas optional; about a minute):

    python3 pixels-hourly/build_pixels.py

or, to make the member lists from raw24 instead of taking the study's:

    python3 pixels-hourly/build_pixels.py --lists-from-raw24 raw24/

and, for stage D4's size measure, the table of each room's activity in the week before (counts only), written beside `pixels.csv`; the handler's `build_canvas.py` cuts it to the frame and puts it in the run's `DROPS/D4/data/`:

    python3 pixels-hourly/build_pixels.py --lists-from-raw24 raw24/ --activity pixels-hourly/ROOMS.tsv

`ROOMS.tsv` lists the 705 rooms of the frame (the first column of the study's `aggregator/input/coders/ROOMS.tsv`); `CENSUS.csv` lists the census's 777 communities, which `--lists-from-raw24` reads when no member lists are here (the `sub` column of the study's `coder/census/MASTER-census.csv`).

**The member lists.** `_pre_progress.jsonl` and `_win_progress.jsonl`, one line per community. The rule: every author in raw24 inside the span, less `[deleted]`, `[removed]` and `AutoModerator`. The study's lists were made from its raw24 on 27 August 2026; the pre-window list holds usernames, the window list their hashes. `--lists-from-raw24` writes hashes only. A raw24 collected later lacks accounts deleted since: on r/thenetherlands one account of 2,815 was gone, and it had placed nothing in the room's region, so the room's rows came out the same.

**Also from `_pre_progress.jsonl`:** its counts for the week before (posts, comments, distinct posters) give stage D4 its size measure, delivered as `aggregator/runs/claude-v43-1/DROPS/D4/data/activity-week-before.csv` (`--activity`; tested 2026-09-26: byte-identical to the shipped table).

**How it was made.** The study built the file in five steps on 27 August 2026 (`p1_keys.py` to `p5_emit.py`, archived in `Layer A/61_sandboxes/Sandboxes/Gioia v28/_session-2026-08-27/device-scripts/`). `build_pixels.py` is those steps in one file; its output is byte-identical to theirs run today.

**One pixel.** Run today, the region of r/mariokart rasterises one pixel smaller than in the study's file (247 against 248; Pillow 9.5 to 12.2 all give 247), so four of its hours hold 1 or 2 fewer placements in `px_in_region_any`: 1,029 over the event against 1,034. Its member columns are 0 either way. On 26 September 2026 the run's copy was replaced by this build (`aggregator/handler/memory/DECISIONS.tsv`), so the file the analyst reads is the one this script makes.

**Tested 2026-09-26:** from the archive.org record, the run's atlas and the study's member lists: every cell of both member columns equal to the study's file, totals 1,013,168 and 2,434,404; `px_in_region_any` equal but for the four r/mariokart cells. With lists made from raw24 for r/thenetherlands: that room's 89 rows unchanged.

## Codebook

`pixels.csv`: `sub`; `hour_since_open` (-16 to 72, hour 0 starting 2017-03-31 16:00 UTC); `px_in_region_any`, `px_by_pre_members`, `px_by_window_members` (placements, as defined above).

`activity-week-before.csv`: `sub`; `posts_week_before`, `comments_week_before`, `distinct_posters_week_before` (the 168 hours before the opening, less `[deleted]`, `[removed]`, `AutoModerator`); `first_record_utc`; `existed_before_window` and `founded_during_event` (1 or 0).
