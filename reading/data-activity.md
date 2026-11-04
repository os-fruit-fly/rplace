# Reading copy: data-activity

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/data-activity.md), SHA-256 `ca95c4106c8c71c23eba51ef52be5016a6b435638a607dab7cec8ec2b230e5e8`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# activity-week-before.csv

One row per room of the frame: how active it was in the 168 hours before the canvas opened (2017-03-24 16:00 to 2017-03-31 16:00 UTC).

    sub, posts_week_before, comments_week_before, distinct_posters_week_before,
    first_record_utc, existed_before_window, founded_during_event

`distinct_posters_week_before` counts the accounts that posted or commented in the room that week, less `[deleted]`, `[removed]` and `AutoModerator`. `first_record_utc` is the room's first item in the 24-day record; `existed_before_window` is 1 if that falls before the canvas opened; `founded_during_event` is 1 if the room's first item falls inside the event. A room with no poster that week has 0 there.

Counted from each room's full 24-day record (raw24) as collected in August 2026, the same record the coders' rooms were cut from, and the same scan whose author lists define `px_by_pre_members` in `pixels.csv`. It measures size before the event, not anything the room did on the canvas. Stage D4 uses it for the volume check: `log(1 + distinct_posters_week_before)`.

## Provenance by row (2026-10-04)

705 rooms. 690 rows come from the study's pre-window list (`_pre_progress.jsonl`, LINK.md; sha256 ee3f8eebbfaf427b9351457363256e01cb3dcfd1d2bf63903a1320e4f4fc743e): 679 that `build_pixels.py --activity` reproduces byte for byte from it; r/dota2, r/globaloffensive, r/leagueoflegends and r/overwatch, appended from it on 2026-10-02; and r/anime, r/DestinyTheGame, r/hearthstone, r/masseffect, r/pcmasterrace, r/rickandmorty and r/wow, appended from it on 2026-10-04 when they joined the frame. r/lehigh and r/upvote left the frame on 2026-10-04 and their rows with them. r/chelseafc and r/hyperlightdrifter were remade from their full records on 2026-09-27, and 13 communities added to the census on 2026-09-26 and 27 come from their raw24 lists (`--lists-from-raw24`).
