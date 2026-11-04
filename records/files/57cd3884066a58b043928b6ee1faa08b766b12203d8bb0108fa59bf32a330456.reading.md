# The position curve, stage B3

**Basis: the assembly of record.** `tools/assemble.py B3 --supersede --accept-sub-label --families out/families.jsonl` on 1,212 accepted returns (the four halves of B0192 and B0927 in fleet ids, J at QB3-003), figures by `out/_analysis/b3_check.py --tag record`. The trial versions written while QB3-003 was open are kept under superseded names.

Pooled across the fleet, pass 1, corpus copies with both replicates returned. Three outcomes per line: agreement (Jaccard with the other replicate's line on the same item), multi (more than one theme) and arguable (confidence "arguable"). Each is regressed on position within the batch with batch fixed effects; standard errors are clustered by batch, and one reader holds each batch. Declared before fitting: a tolerable change of 0.10 in each outcome across a 15-position batch (14 steps); the sensitivity is the change over 14 steps detected with 80% power at two-sided 5%, 2.80 × SE × 14.

The next table gives the slope per position, the change it implies across 14 positions with its interval, and the sensitivity.

| outcome | slope per position | SE | change over 14 | 95% interval | sensitivity over 14 | within the tolerance |
|---|---|---|---|---|---|---|
| agreement | 0.0002 | 0.0007 | +0.003 | -0.015 to +0.022 | 0.027 | yes |
| multi rate | 0.0012 | 0.0007 | +0.017 | -0.001 to +0.035 | 0.026 | yes |
| arguable rate | 0.0029 | 0.0008 | +0.040 | +0.017 to +0.063 | 0.033 | yes |

The next table gives each outcome by decile of relative position, (p − 1) ÷ (n − 1).

| decile | lines | agreement | multi | arguable |
|---|---|---|---|---|
| 1 | 2317 | 0.798 | 0.145 | 0.412 |
| 2 | 1155 | 0.777 | 0.149 | 0.438 |
| 3 | 1858 | 0.772 | 0.162 | 0.452 |
| 4 | 1569 | 0.791 | 0.159 | 0.441 |
| 5 | 1110 | 0.784 | 0.152 | 0.443 |
| 6 | 1737 | 0.776 | 0.174 | 0.458 |
| 7 | 1463 | 0.785 | 0.151 | 0.447 |
| 8 | 1606 | 0.804 | 0.154 | 0.446 |
| 9 | 972 | 0.785 | 0.150 | 0.438 |
| 10 | 1901 | 0.787 | 0.173 | 0.467 |

**What it shows.** Agreement does not move with position: +0.003 over 14 positions, interval -0.015 to +0.022, and the fit would have caught a change of 0.027. The multi rate's interval also sits inside the tolerance. The arguable rate rises: +0.040 over 14 positions (+0.017 to +0.063). That is inside the declared tolerance of 0.10, but it is not zero, so it goes into `defects.jsonl` as an unresolved diagnostic with the evidence that would separate its causes (harder items late, context length, earlier answers). A position effect is a diagnostic of changing responses, not an identified cause.

**The multi rate over readers** (quantiles 0, 10, 25, 50, 75, 90, 100%, over 1212 readers): 0.00, 0.00, 0.00, 0.15, 0.23, 0.38, 0.85.

## Beside the curve

**Pass 1 to pass 2.** Over 15688 corpus lines, 0.01% changed their set or primary in pass 2, and 0.03% carry `changed: true`. 0.2% of readers revised anything. The second pass is close to a copy of the first, so it measures within-batch formation weakly.

**Formation per reader**, first five positions against last five, in the 1204 batches of ten or more: arguable 0.431 then 0.451; agreement with the other replicate 0.784 then 0.792. 367 readers lost more than 0.10 in agreement from first to last, and 406 gained more than that, so the per-reader movement is spread both ways.

**The duplicate.** 1210 batches returned both copies. The two copies agree on every one (Jaccard 1.000, disagreement 0.000), against a between-reader exact-set disagreement of 0.297. The readers recognised the repeat: 911 second copies repeat the first copy's `why` word for word, and 186 say it is a repeat (median gap 7 positions). So the duplicate measures recall of an earlier answer in the same context, not fresh within-reader instability.

**What these figures license.** The readers share an architecture with me and with each other, so a figure here bounds whether the instrument decides, not whether it is right.
