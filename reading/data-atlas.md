# Reading copy: data-atlas

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/data-atlas.md), SHA-256 `fcaae3b2d4fe51970795fba4b6316f52caf013e4e80f2cb1cb2609bde550939a`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# The atlas

The 2017 place-atlas: 1,473 artworks, each with its outline on the canvas (`path`), its centre, and the subreddits it names (`links.subreddit`). `get_atlas.sh` downloads the exact copy the study used (sha256 begins `40a93f67dc552878`), pinned to a commit of placeAtlas/atlas-2017. The run keeps its own copy, `aggregator/input/canvas/atlas_2017.json`.

**It is a pointer only.** It says which communities to look at and where they built. Its `name` and `description` fields are one annotator's first reading and never enter the coding.

**Get it:** `bash atlas/get_atlas.sh`. It stops if the bytes differ from the run's copy.

**Read by:** `pixels-per-artwork/code/fetch_sources.py`; in the aggregator, the build's neighbour and canvas steps (`aggregator/input/canvas/atlas_2017.json` is the same file).

**Tested 2026-09-26:** commit `fb730258` downloaded; byte-identical to the run's copy, 1,473 entries.

## Codebook

`atlas_2017.json` is a list of 1,473 entries. The fields the study reads: `id`; `name`; `links.subreddit` (the subreddits the entry credits, as typed); `path` (the outline, a list of `[x, y]` vertices, keyed by period); `center` (keyed the same way). `description` and `name` are an annotator's words and never enter the coding.

## Credits beyond the links

`credits_beyond_links.csv` lists the artworks of the 12 population communities that no atlas link names but that the census admitted from the canvas or from an atlas description (`coder/census/validations.jsonl`): one row per community and artwork, with the route and the words that credit it. r/tenma has none: its name is written on the canvas, but no atlas entry covers it. r/OrderOfTheKoi's koi has no atlas outline either: it was built from hour 30, lost to the Flag of Italy and erased before the freeze. Its region is `derived_regions.json`, 541 pixels taken from the pixel record (the `source` field says how), named in the table's `region` column; the credit it replaced was the whole flag. The census itself does not use this table; the canvas steps do (`data/pixels-hourly/build_pixels.py` for the regions of the hourly series, `aggregator/handler/build_outcome.py` for the six canvas fields, `aggregator/handler/build_canvas.py` for `subreddits_in_frame`). An artwork keeps its atlas links as well.
