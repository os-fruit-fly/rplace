# Venues in full (raw24)

One file per subreddit: every post and comment by anyone, 2017-03-24 16:00 to 2017-04-17 17:00 UTC (24 days), sorted by time, with `<sub>.manifest.json`: counts per day, the span, what was dropped and why. The coders' rooms are cut from these files. The study holds 24,093 venues, about 51 GB (its notes of 27 August 2026).

**Build it:**
1. `python3 raw24/venue_list.py`: from `venues-placers/`, every subreddit with a placer's record while the canvas was open, into `raw24/venues.txt`.
2. `python3 raw24/12_collect_subreddits.py --list raw24/venues.txt --out raw24/_collected`: one continuous fetch per venue, split by period. A venue over 60,000 records is set aside in `_capped.jsonl` rather than truncated. Resumable. Days.
3. `python3 raw24/flatten_to_raw24.py --from-dir raw24/_collected --out raw24`: one sorted file and manifest per venue.

**How the study's copy was made:** in two parts, disjoint. The 740 venues the atlas names (9.8 GB) were collected by an earlier collector, `collect_v6`, one period at a time, and assembled by a step whose script has not been identified. The other 23,367 (41.2 GB) came through the route above. Both share this format, so one reader reads both.

**Tested 2026-09-26:** r/KarabakhConflict collected and assembled: 884 records (335 before, 139 during, 410 after), no gaps, none outside the span.

**Tested again 2026-09-26, against a coded room:** r/thenetherlands collected in 6 minutes: 36,867 records (13,277 before, 4,419 during, 19,171 after), no gaps. The yard's `build_room.py` then built its room: the 97-hour window's 5,865 items, 511 threads and 928,592 characters equal the room the coders read. Outside the window, five context comments by one account are no longer served, so the week before holds 13,277 items, not 13,285. A rebuild loses what Reddit or the archive has since dropped.

## Codebook

Every text record is one Reddit item as the arctic-shift archive holds it, unprojected. The fields the study reads:

| Field | Meaning |
|---|---|
| `kind` | `post` or `comment`, added at collection |
| `id`, `name` | the item's id, and the same with its type prefix (`t3_` post, `t1_` comment) |
| `created_utc` | seconds since 1970, UTC |
| `author` | the account name; `[deleted]` when the account was gone before the archive took the item |
| `subreddit`, `subreddit_id` | where it was written |
| `title`, `selftext` | a post's title and text |
| `body` | a comment's text |
| `link_id`, `parent_id` | a comment's thread and the item it answers |
| `score`, `ups`, `gilded`, `stickied`, `distinguished`, `edited` | as Reddit reported them when the archive took the item |
| `retrieved_on` | when the archive took it |

The other fields (flair, media, flags) are kept as served and not read.

`<sub>.manifest.json`: `sub`; `after`, `before` (the 24-day span, UTC seconds); `n_records`, `n_posts`, `n_comments`; `first_utc`, `last_utc`; `per_day` (counts per day); `complete_span`; `records_outside_span` and `outside_examples`; `sources_used`, `sources_missing`, `assembled_from`, `assembled_at`; `window_revision` (the version of `_lib/rplace_window.py` used).
