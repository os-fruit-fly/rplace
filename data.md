# The record in numbers

The dataset joins four public records of the 2017 event: Reddit's log of every pixel change, the table of the usernames behind its hashed names, the Place Atlas of the finished canvas, and the posts and comments of the subreddits behind its artworks. This page shows what each holds. Every figure is computed from the shared files; the [data guide](sources/data-README.html) explains how to download and rebuild them.

## Pixel changes

Reddit's log records the time, position, color and hashed account of every change: 16,559,897 changes by 1,166,924 accounts (Reddit, 2017). The canvas opened to the public on 31 March 2017 and froze on 3 April at 17:00 UTC: a little over 72 hours of placing from the first minute of public traffic, at 16:55 UTC. The study's window opens at 16:00, so its hours run from 0 to 73; the last pixel change came at 16:58:54. Activity rose and fell with the day: it dipped between about 04:00 and 12:00 UTC, and peaked in hour 51 at 401,442 changes.

<figure class="data-figure"><img src="assets/data/pixels-per-hour.svg" alt="Pixel changes per hour over the 72 hours. 391 test changes by 18 accounts before the opening are left out." width="630" height="290" loading="lazy"><figcaption>Pixel changes per hour over the 72 hours. 391 test changes by 18 accounts before the opening are left out.</figcaption></figure>

Most accounts did little. The median account made 3 changes, and a third of all accounts (382,233) made just one. The most active account made 656; the five-minute timer allowed about 876 over the event. The top 10% of accounts made 60% of all changes, and the top 1% made 15%.

<figure class="data-figure"><img src="assets/data/changes-per-account.svg" alt="Accounts by the number of pixel changes each made. Both axes are on a log scale." width="630" height="290" loading="lazy"><figcaption>Accounts by the number of pixel changes each made. Both axes are on a log scale.</figcaption></figure>

### Which pixels changed color most often?

The bottom-right pixel (999, 999) changed color 25,926 times. The median was 7 changes per pixel. Of the one million pixels, 4,109 kept the same color throughout the study window.

<figure class="data-figure"><img src="assets/data/pixel-color-change-rank.svg" width="630" height="292" loading="lazy" alt="Per-pixel color changes fall from 25,926 at rank one to zero at the end of the ranking."><figcaption>All one million canvas coordinates, ranked by visible color changes. The horizontal axis uses a log scale. The vertical axis uses a log scale of one plus the count to include zero.</figcaption></figure>

<table class="episode-table"><thead><tr><th scope="col">Rank</th><th scope="col">x</th><th scope="col">y</th><th scope="col">Color changes</th></tr></thead><tbody><tr><td>1</td><td>999</td><td>999</td><td>25,926</td></tr><tr><td>2</td><td>0</td><td>0</td><td>6,548</td></tr><tr><td>3</td><td>998</td><td>999</td><td>5,031</td></tr><tr><td>4</td><td>999</td><td>998</td><td>3,938</td></tr><tr><td>5</td><td>775</td><td>409</td><td>3,880</td></tr><tr><td>6</td><td>237</td><td>461</td><td>3,812</td></tr><tr><td>7</td><td>999</td><td>0</td><td>3,631</td></tr><tr><td>8</td><td>821</td><td>280</td><td>3,501</td></tr><tr><td>9</td><td>831</td><td>280</td><td>3,300</td></tr><tr><td>10</td><td>998</td><td>998</td><td>3,002</td></tr></tbody></table>

Each change replaces the color already visible at that coordinate. Placing the same color again adds zero. The canvas starts white, and the 391 earlier placements establish its state when the study window begins, at 16:00 UTC on 31 March. Only placements inside the 1,000 × 1,000 canvas count. When colors at one pixel share a timestamp, we apply them in palette-index order, the tie rule used for the study’s canvas reconstruction. Pixels with equal counts share a rank. Coordinates start at (0, 0) in the top-left corner.

[Download the ranking for all pixels (compressed CSV)](assets/data/color-changes-by-pixel.csv.gz)

## Artworks

The Place Atlas outlines 1,473 artworks on the finished canvas (Place Atlas, 2017). The median artwork covers 289 pixels, about 17 by 17; one in ten covers more than 1,763. The largest, Rainbow Road, covers 90,552 pixels, 9% of the canvas, and drew 1,130,384 changes. The Entire Dutch Area follows at 33,760 pixels. The median artwork drew 3,368 changes, or about 12 per pixel: most pixels were placed, overwritten and placed again.

<figure class="data-figure"><img src="assets/data/artwork-area.svg" alt="Artworks by area. The horizontal axis is on a log scale." width="630" height="290" loading="lazy"><figcaption>Artworks by area. The horizontal axis is on a log scale.</figcaption></figure>

Of the 1,473 artworks, 1,236 credit at least one subreddit. These credits are where the census of communities starts ([how we came to 705](census.html)).

## Communities

The 705 communities in the census wrote 2,130,302 posts and comments from the opening to a day after the freeze, 1,590,890 of them while the canvas was open. Sizes span four orders of magnitude. The median community wrote 549 posts and comments while the canvas was open; r/leagueoflegends wrote 54,110, most of them about its game and not the canvas. The coders read every item and coded what concerned the event.

<figure class="data-figure"><img src="assets/data/community-rank.svg" alt="The 705 communities ranked by their posts and comments while the canvas was open. Both axes are on a log scale. Red dots mark the 78 communities whose first record falls during the event." width="630" height="290" loading="lazy"><figcaption>The 705 communities ranked by their posts and comments while the canvas was open. Both axes are on a log scale. Red dots mark the 78 communities whose first record falls during the event.</figcaption></figure>

The week before the event shows who was already there. The median community had 276 distinct posters in those seven days. 78 communities have no record in the week before; most were founded for the event. [New communities](emergence.html) says what they were.

Writing and placing were done by different people. Across the 704 communities with an artwork region, a median of 11% of the changes inside the community's artworks came from accounts that posted in the community between the opening and seven days after the freeze. Most hands that built an artwork left no post in the community that claimed it. Regions overlap, so these shares are sound for each community but cannot be added across communities.

## Sources

Every number on this page comes from `pixel_record.npz` and `artworks_index.csv` (the pixels-per-artwork build), `MASTER-census.csv` (the census) and the hourly pixel table `pixels.csv` with its week-before activity table. All are rebuilt by the [collection scripts](sources/data-README.html).

Place Atlas. (2017). *atlas-2017* [Data set]. GitHub. https://github.com/placeAtlas/atlas-2017

Reddit. (2017). Place datasets [Data set]. r/redditdata.
