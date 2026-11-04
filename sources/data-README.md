# Data

How to get every piece of data the study used, and the scripts that made each. Seven stores, one folder each. A folder holds its README (what the store is, how big, how it was built, what was tested), the scripts that build it, and either the data or `LINK.md` with where the study's own copy is.

| Store | Folder | What one file is | Size in the study | Study's copy |
|---|---|---|---|---|
| the pixel record | [pixels/](pixels/README.md) | Reddit's 2017 tile dump: every placement, with the placer's hashed name | 16,559,897 placements | public source; Drive |
| the atlas | [atlas/](atlas/README.md) | the 2017 atlas: 1,473 artworks, their outlines and the subreddits they name | 675 KB | public, pinned; the run's copy is in `aggregator/input/canvas/` |
| the placer accounts | [users/](users/README.md) | one account: everything it wrote on Reddit in 24 days around the canvas | 1,101,801 accounts, about 14 GB | Drive |
| venues, placers only | [venues-placers/](venues-placers/README.md) | one subreddit: only what placers wrote there | 50,936 venues, 13.6 GB | Drive |
| venues in full (raw24) | [raw24/](raw24/README.md) | one subreddit: everything anyone wrote there in the 24 days | 24,093 venues, about 51 GB | Drive (the atlas venues: [folder](https://drive.google.com/drive/folders/1itd-IZsAhBq9lMzCnrQERlO2vfxdT9g6)) |
| hourly pixels per community | [pixels-hourly/](pixels-hourly/README.md) | one row per community and hour: placements in its region, by anyone and by its own members | 67,907 rows, 1.4 MB | built here in a minute; member lists on the Drive |
| pixels per artwork | [pixels-per-artwork/](pixels-per-artwork/README.md) | one artwork: every placement inside its outline; and a 30-minute panel per artwork | 23,058,857 rows, 1.1 GB | built here in minutes; Drive |

## If you want all of it, in order

From this folder, with Python 3 (numpy and Pillow for the last step), curl and xz.

1. `bash pixels/get_pixels.sh`: the pixel record, from archive.org, and the table of usernames and their hashes.
2. `bash atlas/get_atlas.sh`: the atlas, pinned and checked byte for byte against the copy the study used.
3. `python3 users/build_worklist.py`: every placer account, resolved from its hash, most placements first.
4. `python3 _lib/10_collect_authors.py --worklist users/worklist.csv.gz --out users/_collected`, then `python3 users/organise_users.py`: every account's writing. Days at the API's pace; resumable.
5. `python3 venues-placers/build_aggregate.py`: the venues, from what placers wrote.
6. `python3 raw24/venue_list.py`, `python3 raw24/12_collect_subreddits.py --list raw24/venues.txt --out raw24/_collected`, then `python3 raw24/flatten_to_raw24.py --from-dir raw24/_collected --out raw24`: every venue a placer wrote in during the canvas, in full. Days; resumable.
7. `python3 pixels-per-artwork/code/fetch_sources.py`, then `bash pixels-per-artwork/run_all.sh`: the pixel record split by artwork, and the panel the aggregator's canvas step reads. About 4 minutes; this step alone needs no other.

8. `python3 pixels-hourly/build_pixels.py`, with the two member lists from `pixels-hourly/LINK.md` (or `--lists-from-raw24 raw24/`): the hourly series the aggregator's canvas step reads. About a minute.

Or take the study's copies from the Drive, store by store; each `LINK.md` says which.

## Where it comes from

Every text record came through arctic-shift (`arctic-shift.photon-reddit.com/api`), a public archive that serves Reddit's record as it was ingested at the time, before later deletions. No key is needed. The pixel record is Reddit's own release, on archive.org (the study took the same rows from static.aperiodic.net); the usernames behind its hashes are from opl's table on archive.org; the atlas is the 2017 place-atlas. The event window is fixed in one file, [\_lib/rplace_window.py](_lib/rplace_window.py): the canvas opened 2017-03-31 16:00 UTC and froze 2017-04-03 17:00 UTC; the 24 days run from a week before to two weeks after.

## Tested

On 2026-09-26, every step above ran end to end on a small sample, in a Linux shell with the network: the atlas downloaded and matched the study's copy byte for byte; a sample of 2,075 placements (three real r/armenia placers and 2,000 random accounts) went through the account list; the three accounts were collected from arctic-shift (477 records, no gaps), laid out, and grouped into 41 venues; one of them, r/KarabakhConflict, was collected whole (884 records) and assembled into raw24; and the sample placements went through the per-artwork flow (743 artworks touched; the atlas outlines cover 956,741 pixels, as in the study). A second test, on a room the coders read, went further:

- r/thenetherlands was collected into raw24 (36,867 records, no gaps), and the yard's `build_room.py` rebuilt the coders' room from it: the window's items, threads and text equal the yard's room; five context comments by one deleted account are gone.
- One active r/thenetherlands placer was collected (215 records, no gaps) and grouped into 14 venues, 6 of them written in while the canvas was open.
- The pixel record downloaded from archive.org and passed every count; its parse equals the study's in every array; the per-artwork flow and panel built from it equal the study's C5 data (`pixels-per-artwork/README.md`).
- The handler's `build_outcome.py` and `build_canvas.py` rebuilt the run's `case_facts_outcome.jsonl`, `artworks.jsonl` and `pixels.csv` byte for byte, and the room's files for the run matched the run's copy.
- The hourly series from the record, the atlas and the study's member lists: both member columns equal to the study's in every cell; four r/mariokart cells differ by one pixel of its region, and the v38 run now carries this build (`pixels-hourly/README.md`).
- The account list from the full record: 1,101,801 resolved accounts, the number the study collected (`users/README.md`).

Not tested: the full collections, which take days.

Not rebuildable from here: the step that assembled the study's raw24 for the 740 atlas venues (its script has not been found); `raw24/flatten_to_raw24.py` does the same job for any list, and the study's copy is on the Drive (`raw24/LINK.md`).

## Terms

The data is public Reddit posting under real account names, and a pixel record whose hashes resolve to those names. See [the Manual's data page](../Manual/data-and-collection.md#terms-of-use) before publishing anything drawn from it.
