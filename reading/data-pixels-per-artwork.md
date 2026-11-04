# Reading copy: data-pixels-per-artwork

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/data-pixels-per-artwork.md), SHA-256 `f39897930625819db42b9a7112e233c6cf2cf5a0e9930868073ce16a77819c1f`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# Pixels per artwork

Every placement routed to the atlas artwork or artworks whose outline contains it, and a 30-minute panel per artwork. Built from two public sources, the pixel record and the atlas, by two commands. The study's copy is `Layer C/C5_atlas_flow/` (its build kit, `build/`, is what this folder holds).

**Build it** (from `data/`; needs numpy and Pillow, pandas optional; about 1.5 GB free while it works):

1.  `python3 pixels-per-artwork/code/fetch_sources.py`: downloads the record into `pixels/place_tiles_sha1.csv` if it is not there (894 MB, from archive.org), uses the atlas in `atlas/atlas_2017.json`, and writes `pixels-per-artwork/inputs/`. About 2 to 5 minutes.
2.  `bash pixels-per-artwork/run_all.sh`: the five stages, into `pixels-per-artwork/data/`. About 2 minutes, 1.1 GB.

`fetch_sources.py` stops unless every count matches: 16,559,897 rows, 1,166,924 placers, 16,556,641 on the canvas, 1,473 artworks (1,236 naming a subreddit), 956,741 covered pixels, 1,319,701 pixel-artwork memberships, and the final canvas's fingerprint.

**Files after it:**

| File | What it is |
|----|----|
| `data/atlas_flow_all.csv.gz` | 23,058,857 rows, by artwork, then time: `artwork_id,ts_ms,x,y,color,placer_uid,n_artworks,is_primary` |
| `data/by_artwork/aw0000.csv.gz` to `aw1472.csv.gz` | the same rows, one file per artwork |
| `data/artworks_index.csv` | per artwork: name, subreddits, area, placements, distinct placers, first and last placement |
| `data/placers.csv.gz` | `placer_uid` to hashed name, 1,166,924 rows |
| `data/panel_30min.csv.gz`, `.npz` | per artwork and 30-minute bin: placements, placers, pixels touched, repaints, reverts, restorations, net change; 215,058 rows |

**Read by:** `aggregator/handler/build_canvas.py` (its `c5_data` path points here), which reads `artworks_index.csv` and the panel's placements.

**Three things to know.**

- *Overlap.* Outlines overlap on 30.5 per cent of covered pixels, so a placement appears once per containing artwork: 23,058,857 rows for 16,556,641 placements. `is_primary == 1` keeps one row per placement, in the smallest containing outline (16,136,055 rows).
- *Placer ids.* `placer_uid` indexes `inputs/placer_hashes.txt.gz`, which `fetch_sources.py` writes. It numbers placers as the study did, by a 64-bit key of each hash, so ids equal the study's (all 1,166,924 checked). Join across builds on the hash all the same.
- *Ties.* Timestamps are whole seconds, so most rows tie with another, and the two releases of the record order ties differently. `fetch_sources.py` sorts the rows as the study's copy was sorted (as text: time, hashed name, the rest of the line), and `build_artwork_flow.py` breaks every remaining tie by colour and placer. Repaints, reverts and restorations depend on this order. Under this rule, on the primary partition, they are 4,370,182, 12,186,459 and 5,695,139; the study's C4 notes quote 4,369,968, 12,186,673 and 5,695,494 from before the rule. Placements, placers and pixels touched do not depend on order.

**Tested 2026-09-26:** from nothing, in a Linux workspace: the download, the parse and the five stages in about 4 minutes. Every array of `pixel_record.npz` equals the study's stored parse. The outputs equal `C5_atlas_flow/data/` as rebuilt that day: `artworks_index.csv` byte for byte; the long table, the tidy panel, the placer table and the per-artwork files checked, on decompressed content.

## Codebook

Flow rows: `artwork_id` (0 to 1472, the atlas's order); `ts_ms`; `x`, `y`; `color`; `placer_uid` (index into `inputs/placer_hashes.txt.gz`); `n_artworks` (outlines containing the pixel); `is_primary` (1 in the smallest of them).

`artworks_index.csv`: per artwork, its name, subreddits, `area_px`, `center`, `placements`, `placements_primary`, `distinct_placers`, `first_ts_ms`, `last_ts_ms`. `placers.csv.gz`: `placer_uid` and the hash. `panel_30min.csv.gz`: per artwork and 30-minute bin, `placements`, `placers`, `pixels_touched`, `repaints`, `reverts`, `restorations`, `net_change_px`, each also in a `_primary` version, with `bin`, `bin_start_ms`, `hours_from_open`, `area_px` and `placers_total`.
