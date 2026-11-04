# From 2,796 subreddits to 705 communities

The wider dataset holds 7.5 million posts and comments across 2,796 subreddits that took part in the event. The population model covers 705 of them. This page shows each step between the two, and marks which steps took a judgment and which a count. The judgments are recorded with their evidence in the census files, so each can be checked or reversed.

## Where the census starts

The census starts from the Place Atlas of the finished canvas (Place Atlas, 2017). Its curators outlined 1,473 artworks; 1,236 of them credit at least one subreddit. A subreddit that built an artwork and was overwritten before the freeze has no atlas entry, so the census undersamples failure (Denrell, 2003).

## The narrowing

One line per step. The artworks column counts the artworks that still credit at least one community on that line.

| Step | Artworks | Communities | Change | Why | Kind |
|---|---:|---:|---:|---|---|
| The 2017 atlas | 1,473 | | | | count |
| Credit a subreddit | 1,236 | | 237 leave | the entry names no subreddit | count |
| Credit a community | 1,227 | 763 | 9 artworks leave | user pages, r/all, a private subreddit, a Discord group, a name with no archive, a subreddit founded in 2022 | judgment |
| Named on the canvas | 1,227 | 767 | 4 join | the name is written on the final canvas and the community organized there in its own threads | judgment |
| Named as maker in a description | 1,227 | 776 | 9 join | an artwork's description credits it, and it took part in its own threads | judgment |
| A redirect kept as a row | 1,227 | 777 | 1 joins | r/TFLS points to r/TheFarLeftSide, which carries its artworks | judgment |
| Silent while the canvas was open | 1,200 | 748 | 29 leave | nothing posted while the canvas was open | count |
| Active only after the freeze | 1,193 | 741 | 7 leave | talk about a frozen canvas is not organizing on a live one | count and judgment |
| Text takes no part in the event | 1,164 | 709 | 32 leave | a community coder, or a check, read no talk about the event | judgment |
| No writing about the event while the canvas was open | 1,162 | 707 | 2 leave | r/lehigh wrote about it only after the freeze; r/upvote never did | judgment |
| r/place, not a case | 1,161 | 706 | 1 leaves | r/place, where the communities met | judgment |
| Excluded | | **705** | 1 leaves | r/The_Donald (below) | judgment |

## The judgments

### Which community a link means

The atlas names subreddits as annotators typed them. Each link was resolved by hand. Typos and folded names were assigned to the community the artwork belongs to: `hyperlightdrifer` to r/hyperlightdrifter, `Chelsea` to r/chelseafc. Links that name no community, such as r/all, user pages or a subreddit founded in 2022, were set aside.

### What counts as being there

The criterion for evidence of coordination is writing about r/place while the canvas was open. Posting about something else in those hours is not enough, and talking about the frozen canvas afterwards is a different act from organizing to place pixels on a live one.

### Whether the text takes part in the event

A word screen flagged likely talk about the event but never removed a community, because its markers are English and miss communities that name their artwork and not the event. A reading decided: a community coder's verdict that the record holds no talk about the event, or a recorded check of the flagged cases.

### Who read

Two Claude sessions made 19 of the 22 checks in `validations.jsonl`. A Cowork session read four flagged communities on 27 August 2026. A chat read the four names on the canvas and the Robin link on 26 September, and the nine makers in atlas descriptions and the r/TFLS redirect on 27 September, on our instructions in that chat. Neither records its model. We ruled the other three, r/place, r/lehigh and r/upvote; the last two followed readings by the aggregator's first stage. The coder verdicts in `MASTER-census.csv` come from the earlier coding with Claude, under contracts 16 to 29, which the final coding with gpt-5.6-sol later redid; that output is not shipped. 335 communities carry a verdict (292 full, 12 trace, 31 none). The sheet's model column, sonnet for 267 and opus for 68, was assumed and not read from the transcripts, as its builder states. Read from the run transcripts, 281 of the 298 communities with an earlier run were coded by Claude Opus 5 and 17 by Claude Sonnet.

### The r/place subreddit

r/place, the subreddit the event was named after, is credited with one small artwork on the atlas. It holds more posts than any other subreddit, and many of them narrate what the other communities did. It is the square where the communities met, and the census does not count it as a case. The Field agent is reading it, and its account will be set against the model as an independent record.

### r/The_Donald

We left out one community for two reasons. Reddit banned it in June 2020 for repeatedly hosting content that broke its rules, the first of which bans promoting hate based on identity or vulnerability (Reddit, 2020). Its exclusion also has little bearing on the model: its single artwork covered 108 pixels, within the lowest quartile of the census, and was largely overwritten before the canvas froze.

## What the 705 hold

The 705 communities wrote 2,130,302 posts and comments from the opening to a day after the freeze, and account for 90% of all pixel changes. Their community coders produced 115,388 first-order codes and 7,844 second-order themes. [The record in numbers](data.html) shows how they are distributed.

## Files

The census ships as `coder/census/` in the repository: `MASTER-census.csv` (one row per community, with its counts, verdicts and disposition), the link worksheets, `validations.jsonl` (every reading that decided a membership, with its evidence) and `ROOM-RULES.md` (the rules, stated). The counts can be rebuilt from the downloads; the judgments are inputs.

## References

Denrell, J. (2003). Vicarious learning, undersampling of failure, and the myths of management. *Organization Science*, 14(3), 227–243.

Place Atlas. (2017). *atlas-2017* [Data set]. GitHub. https://github.com/placeAtlas/atlas-2017

Reddit. (2020, June 29). Update to our content policy. r/announcements.
