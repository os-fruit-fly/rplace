# Reading copy: data-venues-placers

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/data-venues-placers.md), SHA-256 `1810bdeeb0128db206d0417a335cdc79e2ce50d894a0c76dd7712bfc0e1365e0`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# Venues, placers only

One file per subreddit: every record a placer account wrote there in the 24 days, and nothing by anyone else. Built from `users/`, not by sweeping the subreddit, so it reaches venues no sweep did: the study's copy has 50,936 venues (13.6 GB), twice raw24's count and a third of its records. It is the right denominator for anything about placers; raw24 mixes placers with the rest of the community.

Same format as raw24: `<sub>.jsonl` sorted by time, and `<sub>.manifest.json` with counts per day; `kind` kept, `segment` dropped (the time is in `created_utc`; a boundary is a filter, never a file).

**Build it:** `python3 venues-placers/build_aggregate.py` (reads `users/`, writes here; two passes through shards, so memory stays at one shard).

**Screening:** this store is how the study found where r/place was discussed: every venue a placer wrote in during the canvas.

**Tested 2026-09-26:** built from the three test accounts: 41 venues, 477 records.

## Codebook

Every text record is one Reddit item as the arctic-shift archive holds it, unprojected. The fields the study reads:

| Field | Meaning |
|----|----|
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

`<sub>.manifest.json`: as raw24's, with `built_from` in place of the sources.
