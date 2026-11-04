# The pixel record

Reddit's release of every placement on the 2017 canvas: 16,559,897 rows, no header, `ts_ms,username_sha1_b64,x,y,color`. The second column is base64(sha1(username)), so a name can be matched to its placements; only this release's hashes work this way. Beside it: opl's table of 1,102,111 usernames and their hashes, collected by people who recorded the canvas's traffic during the event.

**Get it:** `bash pixels/get_pixels.sh` (from `data/`). It checks the row counts. `pixels-per-artwork/code/fetch_sources.py` fetches the record too, if it is not here.

**Files after the script:** `place_tiles_sha1.csv` (894 MB), `reddit-place-username-hashes/reddit-place-username-hashes.csv`.

**Read by:** `users/build_worklist.py` (who placed, and how often), `pixels-per-artwork/code/fetch_sources.py`.

**Which copy.** The study parsed static.aperiodic.net's `original_tile_placements.csv.xz`, the same rows sorted as text. archive.org's copy is grouped differently within each second; `fetch_sources.py` restores the study's order, and the parse then equals the study's in every array.

**Tested 2026-09-26:** the record downloaded from archive.org in 22 seconds and passed every count; the username table held 1,102,111 rows.

## Codebook

`place_tiles_sha1.csv`, no header, one placement per row:

| Column | Meaning |
|---|---|
| 1 | time, milliseconds since 1970, UTC; whole seconds in practice |
| 2 | the placer: base64 of the SHA-1 of the username, 28 characters |
| 3, 4 | x and y, 0 to 999, y downwards; 3,256 rows fall outside |
| 5 | colour, an index 0 to 15 into the 2017 palette |

`reddit-place-username-hashes.csv`, no header: `"username","hash"`, the hash as in column 2.
