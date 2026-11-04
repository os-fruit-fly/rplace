# Reading copy: data-users

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/data-users.md), SHA-256 `539141bd7b6696e63616cb3a05bb7ea04a7727a7e68eb205ac5561c5bc41dd46`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# The placer accounts

One file per account that placed at least one pixel and whose name resolves: everything it wrote on Reddit from 2017-03-24 16:00 to 2017-04-17 17:00 UTC, posts and comments, as arctic-shift holds them, unprojected, with `kind` (post or comment) and `segment` (pre, during, after) added. The study holds 1,101,801 accounts, about 14 GB; half the heaviest placers wrote nothing at all, so an empty file is a result, not a failure.

**Build it:**

1.  `python3 users/build_worklist.py`: counts each hash's placements in the tile dump, resolves it through opl's table, writes `users/worklist.csv.gz`, most placements first.
2.  `python3 _lib/10_collect_authors.py --worklist users/worklist.csv.gz --out users/_collected`: the collector. Resumable (a checkpoint after every 250 accounts), single instance, every failed request in `_gaps.jsonl`; its header explains each rule. Days for the full list.
3.  `python3 users/organise_users.py`: moves each file to `users/<bb>/<username>.jsonl` (<bb>: the first two characters of the name) and writes `users/_users.csv`.

**How the study's copy differs:** it was collected in passes (the 87,903 heaviest placers, a recovery pass, then the tail to 1,101,801) and repacked into this layout; its `_users.csv` also records each pass and when each file was written.

**Tested 2026-09-26:** three real accounts collected (477 records, no gaps), then laid out. `build_worklist.py` on the full record, in 38 seconds: 1,166,924 hashed accounts, 1,101,801 resolved to a name, the study's count. Against Layer B's table of every placer (`W3_worklist_all_pareto`, which counts only placements on the canvas): the same 1,101,322 accounts and names, plus 479 whose only placements fell off the canvas; 18 accounts' counts differ there for a reason not found. Order within tied counts differs, as the script's note says.

**The most identifying store.** One file per real account name.

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

Beside `kind`, each account's record adds `segment`: `pre`, `during` or `after` the canvas. `_users.csv`: `username`, `path`, `bucket`, `bytes`. `worklist.csv.gz`: `order`, `username`, `user_hash` (base64 of the SHA-1 of the name, as the pixel record writes it), `placements_total`.
