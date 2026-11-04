# How collection works

Collection gathers the public record of the event once, checks it and freezes it, so that every later reader works from the same copy. A collection handler, a model conversation with shell access, follows the data recipes. The census of communities is a set of research judgments, each recorded with its evidence; no download produces it.

## Its instructions

- [The collection handler's brief](agents/collection.html): what it reads, what it checks, what it hands over, and when it stops.
- [The data recipes](sources/data-README.html): seven stores, the scripts that build each, where each comes from and what was tested.
- [The data folder, for agents](sources/data-for-agents.html): the order in which the stores are built, fast ones first.
- [The shared collectors](sources/data-lib.html): the archive collector every text store reuses, and the one place the event window is defined.
- [Start from raw data](agents/download.html): the reading key, with the inputs and access a collection needs.

## The steps

| Step | What it gives | Size in the study | Its documents |
|---|---|---|---|
| 1. The pixel record | every pixel change, with the placer's hashed name, and the table of usernames behind the hashes | 16,559,897 pixel changes | [recipe](sources/data-pixels.html), [the copy](sources/data-pixels-link.html) |
| 2. The atlas | 1,473 artworks, their outlines and the subreddits they name, checked byte for byte against the study's copy | 675 KB | [recipe](sources/data-atlas.html) |
| 3. The placer accounts | everything each placer wrote on Reddit in 24 days around the canvas; days at the archive's pace, resumable | 1,101,801 accounts, about 14 GB | [recipe](sources/data-users.html), [the copy](sources/data-users-link.html) |
| 4. Venues, placers only | what placers wrote in each subreddit | 50,936 venues, 13.6 GB | [recipe](sources/data-venues-placers.html), [the copy](sources/data-venues-placers-link.html) |
| 5. Venues in full | everything anyone wrote in each subreddit in the 24 days; days, resumable | 24,093 venues, about 51 GB | [recipe](sources/data-raw24.html), [the copy](sources/data-raw24-link.html) |
| 6. Pixels per artwork | every pixel change inside each artwork's outline, and a 30-minute panel per artwork; about four minutes | 23,058,857 rows, 1.1 GB | [recipe](sources/data-pixels-per-artwork.html), [the copy](sources/data-pixels-per-artwork-link.html) |
| 7. Hourly pixels per community | pixel changes in each community's region by hour, by anyone and by its own members; about a minute | 67,907 rows, 1.4 MB | [recipe](sources/data-pixels-hourly.html), [the copy](sources/data-pixels-hourly-link.html), [the week before](sources/data-activity.html) |
| 8. The census | which subreddits count as communities: [from 2,796 subreddits to 705 communities](results/population-record.html#census) | judgments with evidence | [the census](sources/census-README.html), [its builders](sources/census-builders.html) |
| 9. Freeze and hand over | every file hashed; `HANDOFF-collection.md` records each input's path, source, bytes, hash, time window, version, checks, gaps and status | | |

A recipe says what a store holds, how to build it and what was tested; "the copy" says where the study's own copy is. Every text record came through the public Arctic Shift archive, which serves Reddit's record as it was ingested at the time, before later deletions. The pixel record is Reddit's own release; the atlas is the 2017 Place Atlas.

## When it stops

The handler stops a route when access is missing, archived bytes are unavailable, a check fails or the choice of collection is unresolved. It names the missing store and the next action. It never infers a census decision and never counts an incomplete download as ready.

[Run it](guides/download.html)
