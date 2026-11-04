# Transmission after revision, stage B4

Written at B4c, 2026-10-13. This file measures whether fresh readers holding only the frozen scheme reach the line I settled. It is transmission after revision (FLEET.md, section 2). It is not reliability in the intercoder sense and is never called that. The settled line is `assign_final.jsonl` at sha256 d3506a88…, as left at B4a-07; this check revises no ruling. The declarations were made in `notes-B4.md` before any figure ("The check (B4c)").

**What every figure here licenses.** Readers share an architecture with me, and arm 1's readers share one with the fleet, so each figure bounds whether the written instrument decides, not whether it is right.

## The definition, stated once

Stage B2's definition, unchanged (`notes-B2.md`):
- Two placement sets agree by their Jaccard index. `["T3-004"]` against `["T3-004","T3-011"]` scores 0.5, partial agreement.
- Fresh against settled is the mean Jaccard of each fresh reading against the settled set, over readings whose settled line is resolved. The exact rate (Jaccard 1, the outcome "agrees") and the primary match rate stand beside it.
- The readers' agreement with each other is the mean Jaccard of the two readings of an item, over items. Primary match stands beside it.
- Alpha is Krippendorff's alpha with distance 1 − Jaccard and chance over the pooled sets of the comparison.
- Scoring reads pass 1 only.
- A reading whose settled line is unresolved is "disagrees-unresolved": it leaves the denominator and is counted.

## The two arms, never pooled

- **Arm 1.** DeepSeek V4.1 Flash (deepseek/deepseek-v4.1-flash, served as probed), medium reasoning effort, max_tokens 128,000, through the gateway (`_fleet_raw/B4/arm.json`). Two fresh readers per packet; no instructions beyond the message. This is the model stage B3's fleet ran and stage B2's gold round ran (there on the direct route), so arm 1's figures can stand beside theirs. Its readings are in `reassign.jsonl`.
- **Arm 2.** OpenAI gpt-6-astra, medium effort, two replications per packet, run by the Codex orchestrator on J's computer from byte-identical copies of the same messages, under Codex's built-in instruction (recorded by hash in `_control/isolation-PASS.json`) and with no tools. Its readings are in `reassign-openai-astra.jsonl`. No earlier stage ran this model, so its figures stand beside nothing but arm 1's.
- **Strata.** Uniform (U, 250 items) and adjudicated (A, 250 items) are scored against the settled line. R (all 185 unresolved items) has no settled line and is reported last, apart.
- **Readings.** Arm 1 has 999: one reading was refused at assembly (S05-23, reader r8, position 3 typed its room's name wrong; `notes-B4.md`). Arm 2 has 1,000.

## The headline figures

The next table gives fresh against settled and the readers' agreement with each other, per arm and stratum, with stage B3's two readers on the same items beside them.

| arm | stratum | readings | unresolved, excluded | fresh against settled | exact | primary | readers' agreement | readers' alpha | B3 readers, same items | B3 alpha, same items |
|---|---|---|---|---|---|---|---|---|---|---|
| 1, DeepSeek | uniform | 499 | 6 | 0.657 | 0.452 | 0.811 | 0.781 | 0.776 | 0.781 | 0.775 |
| 1, DeepSeek | adjudicated | 500 | 30 | 0.544 | 0.287 | 0.664 | 0.664 | 0.658 | 0.514 | 0.505 |
| 2, OpenAI | uniform | 500 | 6 | 0.622 | 0.431 | 0.757 | 0.872 | 0.869 | 0.781 | 0.775 |
| 2, OpenAI | adjudicated | 500 | 30 | 0.554 | 0.321 | 0.706 | 0.804 | 0.801 | 0.514 | 0.505 |

The reference figures: stage B3's corpus agreement is 0.786 with alpha 0.782 (`handback-B3.md`); the stability floor is 0.807 (`stability-B2.md`); stage B2's gold fidelity is 0.624 and stage B3's is 0.645.

- **Arm 1's readers agree with each other exactly as much as the fleet did on the uniform stratum.** Both pairs score 0.781. Both sit under the stability floor of 0.807. `stability-B2.md` reads that floor as the share of placements that differ between readers whatever the wording, so a figure inside it says nothing about the scheme.
- **The fresh readers reach the settled line less often than they reach each other.** In U, arm 1 scores 0.657 against the settled line and 0.781 against each other. Part of the gap is how the settled line was built (the class 2 row below), and part is the adjudication (the adjudicated rows).
- **On the adjudicated stratum the fleet's figure is low by selection.** Stratum A was drawn from items the fleet split on or that my B1 grouping did not match. The fresh readers agree with each other more there (0.664 and 0.804) than the fleet did (0.514). Some of that rise is regression toward the corpus mean, and none of it is evidence that the rulings transmit.
- **Arm 2's readers agree with each other far more than arm 1's, but not more with the settled line.** See "Arm 2's two replications" below for why that agreement is not two independent readers.

## The uniform stratum, split

The next table splits U by how each item's settled line was made. Class 2 is the validator's rule-2 row, `b1_grouping_kept`: the two B3 readers agreed on a proper subset of my B1 grouping, and the settled line kept my whole grouping. Those extra B1 themes were placed under the B1 scheme, never by a reader holding the frozen one, and never adjudicated.

| U row | items | arm 1 fresh against settled | arm 1 exact | arm 2 fresh against settled | arm 2 exact | arm 1 readers | arm 2 readers |
|---|---|---|---|---|---|---|---|
| class 1: the fleet agreed, equal to my B1 grouping | 87 | 0.930 | 0.902 | 0.802 | 0.736 | 0.923 | 0.931 |
| class 2 (rule 2, `b1_grouping_kept`), against the settled line | 53 | 0.491 | 0.104 | 0.502 | 0.142 | 0.811 | 0.843 |
| class 2, against the themes the settled line places with concepts | 53 | 0.786 | 0.642 | 0.610 | 0.443 | | |
| adjudicated items in U (classes 3 to 5) | 110 | 0.517 | 0.258 | 0.535 | 0.327 | 0.654 | 0.839 |
| U without class 2 | 197 | 0.703 | 0.548 | 0.655 | 0.510 | | |
| U, class 2 scored against the placed themes | 250 | 0.721 | 0.568 | 0.645 | 0.496 | | |

- **Where the fleet agreed and my B1 grouping matched, fresh DeepSeek readers reach the line nine times in ten** (class 1, exact 0.902). Fresh OpenAI readers reach it in three of four (0.736).
- **Class 2 is where the settled line and every reader part.** Against the settled line, arm 1 agrees exactly in 11 of 106 readings. Against the themes the line places with concepts, it agrees in 68. The difference is my B1 themes that the class 2 rule kept. The 51 class 2 items a fresh reader placed elsewhere are each named below. In 22 of them no reader of the fleet or of either arm placed my kept themes. In 18 the fleet's placement goes against a field of the scheme. In 13 of those, the fresh readers placed a B1 theme, or its sibling, that the fleet had left out. In the other 5, they placed a theme that neither the fleet nor my B1 grouping had placed.
- **The adjudicated items in U behave like stratum A** (0.517 and 0.535 against 0.544 and 0.554).

## The adjudicated stratum, by class

The next table splits A by the class that sent each item to adjudication.

| A row | items | resolved readings | arm 1 fresh against settled | arm 1 exact | arm 2 fresh against settled | arm 2 exact | arm 1 readers | arm 2 readers | B3 readers |
|---|---|---|---|---|---|---|---|---|---|
| class 3: the fleet split | 180 | 356 | 0.502 | 0.197 | 0.539 | 0.289 | 0.627 | 0.805 | 0.331 |
| class 4: the fleet agreed outside my B1 grouping | 63 | 110 | 0.666 | 0.555 | 0.583 | 0.400 | 0.733 | 0.796 | 1.000 |
| class 5: no B1 grouping | 7 | 4 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.857 | 0.857 |

Class 5 has two resolved items in A; its row is shown and not read.

## The comparison §12 names

The next table counts each reading's outcome against the settled line.

| arm | stratum | agrees | disagrees-contested | disagrees-unanimous | disagrees-unresolved |
|---|---|---|---|---|---|
| 1, DeepSeek | uniform | 223 | 158 | 112 | 6 |
| 1, DeepSeek | adjudicated | 135 | 335 | 0 | 30 |
| 2, OpenAI | uniform | 213 | 144 | 137 | 6 |
| 2, OpenAI | adjudicated | 151 | 319 | 0 | 30 |

- **"Disagrees-contested"** is a reading on an item `disagreements.jsonl` rules (classes 3, 4 and 5). **"Disagrees-unanimous"** is a reading on an item it never ruled (classes 1 and 2), where the two B3 readers agreed and their list stood. **"Disagrees-unresolved"** readings leave the denominator: 6 in U (3 items) and 30 in A (15 items), per arm.
- **The two rates.** In U, arm 1 disagrees with the settled line on 0.742 of readings of contested items (213) and on 0.400 of readings of unanimous items (280); on class 1 alone, 0.098 (17 of 174). Arm 2: 0.673, 0.489, and 0.264 (46 of 174). In A, arm 1 disagrees on 0.713 of 470 and arm 2 on 0.679.
- **The same split again.** Of arm 1's disagrees-contested readings, 0.462 in U and 0.579 in A equal one of the fleet's two placements or my B1 grouping. For arm 2 the shares are 0.382 and 0.401. Where a boundary split the fleet, more than half of DeepSeek's disagreeing readings in A land where an earlier reading already stood. That is the boundary splitting again, not a new problem. The OpenAI readers land outside the earlier placements more often.
- **The unanimous items a fresh reader placed elsewhere:** 62 items in arm 1, 74 in arm 2, 79 in either (28 of class 1 and 51 of class 2). Each is named below with a paragraph.

## Against stage B2's gold figure

Stage B2's gold fidelity is 0.624: nine DeepSeek V4.1 Flash readers at medium effort against my placements on 40 gold items (`pilot_report.md`). Arm 1's uniform figure is 0.657, the same model at the same effort. The gold number is the lower of the two by 0.033, so the hard set was harder than the ordinary item, by a small margin. Without class 2, whose settled line is my B1 grouping, the uniform figure is 0.703 and the margin is 0.079. Arm 2's uniform figure (0.622) has no B2 counterpart on its model and is not set beside the gold figure.

## Per family

Fresh against settled counts an item in the family of its settled line's first theme. The readers' agreement counts an item in the family of each reader's primary, as stage B3 did. Stage B3's corpus agreement per family stands beside them (`out/_analysis/b3_check_record.json`). Families with fewer than 10 items in a stratum are shown and not ranked.

The next table gives the uniform stratum by family.

| family | items | arm 1 fresh against settled | arm 2 fresh against settled | arm 1 readers | arm 2 readers | B3 corpus |
|---|---|---|---|---|---|---|
| G01 April Fools in the sub | 32 | 0.750 | 0.721 | 0.769 | 0.920 | 0.798 |
| G02 the sub's rules and usual posts | 16 | 0.641 | 0.906 | 0.583 | 0.947 | 0.773 |
| G03 where the planning happens | 9 | 0.694 | 0.659 | 0.733 | 0.889 | 0.806 |
| G04 calling people in to place | 20 | 0.656 | 0.561 | 0.609 | 0.771 | 0.740 |
| G05 telling placers what to place | 2 | 0.625 | 0.646 | 0.750 | 0.889 | 0.650 |
| G06 strain, doubt and giving up | 3 | 0.764 | 0.778 | 0.400 | 1.000 | 0.628 |
| G07 choosing what to make and where | 12 | 0.569 | 0.425 | 0.703 | 0.643 | 0.668 |
| G08 building and growing the mark | 18 | 0.593 | 0.491 | 0.708 | 0.730 | 0.626 |
| G09 defending and repairing the work | 20 | 0.690 | 0.700 | 0.873 | 0.883 | 0.742 |
| G10 finding who changed the work | 0 | - | - | 0.333 | - | 0.629 |
| G11 scripts, bots and extra accounts | 7 | 0.738 | 0.547 | 0.625 | 0.905 | 0.832 |
| G12 attacking others' work | 6 | 0.403 | 0.364 | 0.833 | 0.694 | 0.684 |
| G13 holding back from others' work | 4 | 0.333 | 0.500 | 0.333 | 1.000 | 0.627 |
| G14 space and help between rooms | 18 | 0.507 | 0.310 | 0.658 | 0.833 | 0.697 |
| G15 pacts and envoys between rooms | 9 | 0.713 | 0.458 | 0.708 | 0.764 | 0.582 |
| G16 kindred rooms and colour factions | 0 | - | - | 0.000 | - | 0.624 |
| G17 nations and their flags | 7 | 0.506 | 0.440 | 0.500 | 0.681 | 0.644 |
| G18 politics, history and hate symbols | 2 | 0.479 | 0.416 | 0.778 | 1.000 | 0.552 |
| G19 taunts and victories over rivals | 6 | 0.667 | 0.639 | 0.750 | 0.812 | 0.610 |
| G20 looking at the canvas and its worth | 26 | 0.881 | 0.814 | 0.760 | 0.896 | 0.743 |
| G21 after the canvas closed | 30 | 0.600 | 0.690 | 0.881 | 0.882 | 0.776 |

The next table gives the adjudicated stratum by family.

| family | items | arm 1 fresh against settled | arm 2 fresh against settled | arm 1 readers | arm 2 readers | B3 corpus |
|---|---|---|---|---|---|---|
| G01 April Fools in the sub | 24 | 0.618 | 0.724 | 0.701 | 0.931 | 0.798 |
| G02 the sub's rules and usual posts | 12 | 0.479 | 0.875 | 0.542 | 0.790 | 0.773 |
| G03 where the planning happens | 6 | 0.820 | 0.722 | 0.759 | 0.857 | 0.806 |
| G04 calling people in to place | 11 | 0.614 | 0.443 | 0.556 | 0.576 | 0.740 |
| G05 telling placers what to place | 8 | 0.620 | 0.521 | 0.565 | 0.667 | 0.650 |
| G06 strain, doubt and giving up | 0 | - | - | 0.000 | - | 0.628 |
| G07 choosing what to make and where | 16 | 0.505 | 0.320 | 0.339 | 0.789 | 0.668 |
| G08 building and growing the mark | 21 | 0.486 | 0.579 | 0.450 | 0.743 | 0.626 |
| G09 defending and repairing the work | 19 | 0.658 | 0.548 | 0.808 | 0.857 | 0.742 |
| G10 finding who changed the work | 10 | 0.417 | 0.458 | 0.545 | 0.758 | 0.629 |
| G11 scripts, bots and extra accounts | 11 | 0.629 | 0.758 | 0.727 | 0.750 | 0.832 |
| G12 attacking others' work | 9 | 0.620 | 0.315 | 0.561 | 0.667 | 0.684 |
| G13 holding back from others' work | 5 | 0.267 | 0.416 | 0.714 | 0.689 | 0.627 |
| G14 space and help between rooms | 20 | 0.423 | 0.385 | 0.486 | 0.656 | 0.697 |
| G15 pacts and envoys between rooms | 12 | 0.625 | 0.663 | 0.600 | 0.765 | 0.582 |
| G16 kindred rooms and colour factions | 4 | 0.385 | 0.354 | 0.300 | 0.733 | 0.624 |
| G17 nations and their flags | 4 | 0.198 | 0.521 | 0.889 | 0.524 | 0.644 |
| G18 politics, history and hate symbols | 2 | 0.500 | 0.750 | 0.375 | 0.778 | 0.552 |
| G19 taunts and victories over rivals | 3 | 0.458 | 0.278 | 0.292 | 0.000 | 0.610 |
| G20 looking at the canvas and its worth | 11 | 0.500 | 0.602 | 0.650 | 0.708 | 0.743 |
| G21 after the canvas closed | 27 | 0.585 | 0.563 | 0.745 | 0.761 | 0.776 |

**The worst families**, ranked on fresh against settled among families with 10 items or more:
- arm 1, uniform: G14 (0.507), G07 (0.569), G08 (0.593);
- arm 1, adjudicated: G10 (0.417), G14 (0.423), G02 (0.479);
- arm 2, uniform: G14 (0.310), G07 (0.425), G08 (0.491);
- arm 2, adjudicated: G07 (0.320), G14 (0.385), G04 (0.443).

G14 (space and help between rooms) is among the three worst in all four. At stage B3 it was not: its corpus agreement was 0.697, and B3's lowest family was G18 at 0.552. G14's themes turn on who asked whom for what: a border settled, help sent, space asked of a host, help asked of a room, a host's approval disputed or given (T3-010, T3-011, T3-035, T3-084, T3-094, T3-162). Their neighbours in G13 and G15 turn on the same questions (T3-039, T3-149, T3-150, T3-151). Several paragraphs below show the fleet and the fresh readers answering them differently.

**The per-theme figure stage C1 needs is stage B3's agreement**, over every item and every theme (`out/_analysis/b3_check_record.json`, `agreement.themes`; `handback-B3.md`, "Agreement"). It is not recomputed here: 500 items over 197 themes leave most themes with no item in this sample.

## Arm 2's two replications

Arm 2's readers agree with each other at 0.872 in U, against arm 1's 0.781. The 18 items read twice (once in a U or A packet and once in an R packet) test that figure on the same items:
- Arm 1: its two readers agree at 0.741 in the U and A packets and 0.796 in the R packets. A reading from one packet agrees with a reading of the same item from the other packet at 0.787 (72 pairs). Agreement within a packet and across packets is about the same.
- Arm 2: its two replications agree at 0.889 in the U and A packets and 0.861 in the R packets. Across packets, the figure falls to 0.653.

The two arm 2 replications of one packet are the same model given byte-identical messages under the same built-in instruction, and they agree with each other more than with the same model reading the same item in another packet. So arm 2's readers' agreement and alpha are an upper bound on what two independent OpenAI readers would show. Arm 1's figures do not show that pattern. Eighteen items are few, and this is a side note.

## Stratum R, the 185 unresolved items

R has no settled line. Every item in it is one I found that no placement's test takes. As declared, R reports whether fresh readers converge there, not whether they are right, and no reading changes a ruling. All 185 are read in R packets (`readings-R-B4.jsonl`, 740 readings).

The next table gives R per arm, with the B3 readers on the same items beside it.

| | arm 1, DeepSeek | arm 2, OpenAI | B3 readers, same items |
|---|---|---|---|
| readers' agreement (Jaccard) | 0.623 | 0.862 | 0.543 |
| readers' alpha | 0.606 | 0.851 | 0.522 |
| items whose two primaries meet | 116 of 185 | 159 of 185 | |
| readings wholly among the earlier placements | 265 of 370 | 224 of 370 | |
| readings partly among them | 1 | 12 | |
| readings wholly outside them | 104 | 134 | |

"The earlier placements" are the two B3 readers' sets and my B1 grouping.

The next table gives R by class.

| R row | items | arm 1 readers | arm 1 primaries meet | arm 1 wholly outside | arm 2 readers | arm 2 primaries meet | arm 2 wholly outside |
|---|---|---|---|---|---|---|---|
| class 3 | 71 | 0.617 | 44 | 34 of 142 | 0.866 | 60 | 49 of 142 |
| class 4 | 78 | 0.596 | 47 | 37 of 156 | 0.846 | 67 | 53 of 156 |
| class 5 | 36 | 0.694 | 25 | 33 of 72 | 0.889 | 32 | 32 of 72 |

- **Fresh DeepSeek readers converge on R items about as often as on contested items** (0.623 against 0.664 in A), and more than the fleet did on the same items (0.543).
- **Most fresh readings land on a placement someone already made.** Arm 1 puts 265 of 370 wholly among the earlier placements. Those are placements I found that no test takes, so convergence there does not resolve the items.
- **About a quarter to a third land wholly outside every earlier placement** (104 and 134 of 370). In class 5, where I had no B1 grouping, nearly half do.
- **The 18 read twice** are reported in "Arm 2's two replications" above.

## The second pass

Not scored. Arm 1 marked 1 of 1,370 second-pass lines changed; arm 2 marked 17.

## What these figures license

Readers share an architecture with me, so every figure in this file bounds whether the written instrument decides, not whether it is right. Arm 1 is the fleet's own model. Arm 2 is another model family, run under Codex's built-in instruction, and its two replications are not independent readers in the fleet's sense. Neither arm can show that a placement is correct. They show where a stranger holding the frozen scheme lands, and how often that is where I settled.

## The unanimous items a fresh reader placed elsewhere

These are the 79 items with a disagrees-unanimous reading in either arm: 62 in arm 1's `reassign.jsonl`, 74 in arm 2's, 28 of class 1 and 51 of class 2. Each paragraph gives the fleet's placement, the settled line and the four fresh readings, then a verdict in one of five fixed phrases:
- **the fleet's shared assumption** (§12's first reading): a field of the scheme contradicts the fleet's placement. Examples are an unmet `must_show`, a discriminator that sends the concepts elsewhere, or a concept counted under a theme whose `must_not_show` names the sibling.
- **the settled line keeps my B1 theme(s)** (§12's second reading, for class 2): the settled line holds a B1 theme that the class 2 rule kept and that no reader of the fleet or of either arm placed.
- **rule 0 applied differently**: fresh readers add, drop or list under `also_present` a theme carried by concepts of its own. Rule 0 makes one placement the default and allows a second "only where one cannot carry the material", and it leaves that judgement to the reader.
- **the scheme does not decide**: the material meets two gates and no field separates them.
- **the fresh reading misses a field**: the settled line holds, and the fresh reader went against a field.

The next table counts the verdicts by class.

| class | items | the fleet's shared assumption | the settled line keeps my B1 themes | rule 0 applied differently | the scheme does not decide | the fresh reading misses a field |
|---|---|---|---|---|---|---|
| 1 | 28 | 7 | 0 | 14 | 5 | 2 |
| 2 | 51 | 18 | 22 | 10 | 1 | 0 |
| all | 79 | 25 | 22 | 24 | 6 | 2 |

**What the 25 share.** In most of them the fleet's two readers counted concepts under a theme whose own `must_not_show` or discriminator names a sibling. Examples: defence calls under T3-002 instead of T3-005; a homeland flag under T3-002 or T3-038 instead of T3-065; another room's chat under T3-014 instead of T3-153; neighbours' requests under T3-024 instead of T3-039; a joint front under T3-011 instead of T3-150; plans and corrections under T3-038 instead of T3-070 or T3-004; a rival's art recoloured under T3-006 instead of T3-068. Two readers agreeing on such an item is a shared habit, not the scheme deciding. The settled line inherited it, because classes 1 and 2 stood without adjudication.

**AprilKnights/t01** (class 1). The fleet, my B1 grouping and the settled line hold T3-002 (calling members in to place). Three of four fresh readings add T3-016 (explaining what the canvas is): arm 1 reading 2 and both arm 2 readings. Arm 2 reading 1 also adds T3-171 (spreading a faction's colour). The T3-016 addition rests on c0001 ("/r/place is a, well, place where you can post a square"), which passes T3-016's `must_show` ("what r/place is") and which no call carries; the discriminator between the two asks exactly that. T3-171 rests on "help spread the red" and the red corner, which are also calls to place. Verdict: rule 0 applied differently. Rule 0 makes one placement the default and allows a second "only where one cannot carry the material"; the fleet kept to one, and three fresh readers judged that T3-002 cannot carry the explanation.

**calgaryflames/t15** (class 1). The fleet, my B1 grouping and the settled line hold T3-028 (running scripts for the work) and T3-014 (moving planning into a chat). Both arm 1 readings agree. Both arm 2 readings place T3-028 alone and list T3-014 under `also_present`. T3-014 stands on three concepts of its own (c0145, c0229, c0233: a Discord made, its link offered, script troubleshooting moved there). Verdict: rule 0 applied differently. Arm 2 kept the single placement and recorded the second theme under `also_present`, a use rule 0 gives only to bags of more than three themes. The settled line's two placements stand.

**canucks/t12** (class 1). The fleet, my B1 grouping and the settled line hold T3-048 (reacting to official April Fools). Three fresh readings place T3-017 (carrying on ordinary sub talk): arm 1 reading 2 and both arm 2 readings. The two concepts enjoy the Sedins pranking Troy Stecher. Neither says April Fools; the fleet's whys call it "an official team April Fools joke". T3-048's `must_show` needs "an April Fools joke made by the maker the sub is about", and T3-017's needs talk "with no ... April Fools joke as its point". Verdict: the fleet's shared assumption. The two B3 readers took a prank in the window as the club's April Fools joke, which the words do not show; on the words, T3-017's gate is met.

**canucks/t16** (class 1). The fleet, my B1 grouping and the settled line hold T3-150 (forming alliances between rooms). Both arm 1 readings agree. Both arm 2 readings add T3-006 (calling to deface rivals' work) on c0074 ("throw a few blue pixels on waldo to try and scare them off") and T3-084 (asking other rooms for help) on c0079 ("come help a team ... keep our logo on the board"). Each concept passes the added theme's `must_show`, and each is one concept. Verdict: rule 0 applied differently. Arm 2 placed three themes on single concepts; the fleet and arm 1 kept the single placement.

**cfb/t01** (class 1, a bag). The fleet, my B1 grouping and the settled line hold T3-038 (building and reporting the mark), with nine more themes under `also_present`. Both arm 1 readings agree. Both arm 2 readings make T3-033 (proposing the room's mark) the primary and list T3-038 under `also_present`. The discriminator between the two counts concepts. The settled line gives T3-033 five, and puts the joke proposals ("24-21 maybe?", "Ohio State lost to Clemson 31-0", "Shirtless Charlie Weis and Bret Bielema") under T3-031 (playing the room's in-jokes). Read as proposals, which T3-033's `must_show` allows ("slogans and symbols proposed as the room's mark included"), they give T3-033 the larger share. Verdict: the scheme does not decide. A joke offered as the room's mark meets both T3-033's and T3-031's gates, and the count rule then swings the primary of a bag.

**crystalclear/t01** (class 1). The fleet, my B1 grouping and the settled line hold T3-033 (proposing the room's mark). All four fresh readings add T3-020 (choosing a canvas spot), on c0003 ("I found a good place here") and c0004 ("the top left black border"). Both arm 2 readings also add T3-004 (settling the mark's design) on the size and the preview, and arm 2 reading 2 drops T3-033. T3-020's `must_show` ("free space found ... a location announced") takes c0003 and c0004, which the settled line leaves uncarried. Verdict: rule 0 applied differently. No field contradicts the fleet's single placement, but all four fresh readings judged that T3-033 cannot carry where the mark goes, the clearest such signal among the class 1 items. Arm 2 reading 2's drop of T3-033 goes against c0001 ("Lets get CLC on /r/place!").

**danganronpa/t01** (class 1). The fleet, my B1 grouping and the settled line hold T3-001 (staging April Fools fake news). Fresh: arm 1 reading 1 agrees; arm 1 reading 2 and arm 2 reading 1 place T3-031 (playing the room's in-jokes); arm 2 reading 2 places T3-017 (carrying on ordinary sub talk). The three concepts answer an insult with "(april fools)" and stock sexual replies. No fake posted as true is in the words (T3-001's gate). No canvas is in them (T3-031's gate). T3-017's `must_not_show` excludes "April Fools jokes". Verdict: the scheme does not decide. This is the defect already listed for stage C1: T3-017's and T3-001's discriminators against T3-031's canvas condition.

**de/t01** (class 1, a bag). The fleet, my B1 grouping and the settled line hold T3-070 (sharing coordinates, templates and how-to), with T3-002, T3-062 and T3-038 under `also_present`. Three fresh readings agree. Arm 1 reading 1 places T3-002 (calling members in to place) as a second theme. Verdict: rule 0 applied differently. With four themes at three concepts or more, rule 0's bag clause places one and names the rest under `also_present`; one reader placed two.

**de/t05** (class 1, a bag). The fleet, my B1 grouping and the settled line hold T3-010 (settling borders with neighbours), with eight more themes under `also_present`, among them T3-149 (agreeing truces with rival rooms) on four concepts. Both arm 1 readings agree. Both arm 2 readings make T3-149 the primary and list T3-010 under `also_present`. The discriminator asks whether the deal "end[s] or forestall[s] a fight between rooms in contact". Much of the France and Germany talk does: "you guys Blitzkrieg us" (c0154), "please stop trying to swallow our flag" (c0134), "STOP WAR" (c0179), "a new europe flag inbetween to keep peace" (c0139). The settled line counts c0134 and c0139 under T3-010. Verdict: the fleet's shared assumption, on the primary of a bag. The two B3 readers and my B1 grouping read the French border as lines settled "where no fight began"; on the discriminator's words those concepts are T3-149's, and the count between the two themes is then close.

**drugs/t08** (class 1). The fleet, my B1 grouping and the settled line hold T3-001 (staging April Fools fake news). Both arm 1 readings agree. Both arm 2 readings place T3-017 (carrying on ordinary sub talk). The one concept is a writing prompt: LSD says "April Fools!" and turns into another drug; "What did LSD turn into?" Nothing is posted as true, which T3-001's `must_show` needs, and T3-017's `must_not_show` excludes "April Fools jokes". Verdict: the fleet's shared assumption. The fleet placed T3-001 on April Fools play that is no fake (one B3 reader wrote "arguable because it is a prompt rather than a claim"). No theme's gate takes the concept; `boundaries.md` rules such play unresolved on T3-001's `must_show`, so an adjudication would have left this item unresolved.

**edmontonoilers/t03** (class 1). The fleet, my B1 grouping and the settled line hold T3-002 (calling members in to place), on all eighteen concepts. Arm 1 reading 1 agrees. Arm 1 reading 2 and arm 2 reading 1 add T3-005 (defending the work against attackers); arm 2 reading 1 also adds T3-016 (explaining what the canvas is); arm 2 reading 2 lists both under `also_present`. The discriminator between T3-002 and T3-005 asks whether "the call [is] to build or finish (T3-002), or to defend against an attack under way (T3-005)". Four concepts call for defence: "we've come under attack from the void. We need reinforcements" (c0088), "GO DEFEND THE LOGO" (c0126), and c0030 and c0062 on the oil drop being wrecked. Verdict: the fleet's shared assumption. The settled line counts those four under T3-002, and the discriminator sends them to T3-005.

**falcons/t01** (class 1). The fleet, my B1 grouping and the settled line hold T3-006 (calling to deface rivals' work). Both arm 1 readings agree. Both arm 2 readings add T3-068 (converting a neighbour's art) on c0083 ("help turn the 3-28 thing into an 18-1 thing"). The settled line counts c0083 under T3-006, whose `must_not_show` names "another's art turned into the room's own sign (T3-068)". Verdict: the fleet's shared assumption, on one concept. The second placement arm 2 made is licensed by that field.

**gorillaz/t10** (class 1). The fleet, my B1 grouping and the settled line hold T3-004 (settling the mark's design). Three fresh readings agree. Arm 2 reading 1 adds T3-152 (announcing what the chat decided) on c0056 ("The Discord server's plan for Noodle has been changed") and T3-074 (working around the timer) on the mobile trouble of c0106 and c0107. Verdict: rule 0 applied differently. One reader placed two further themes, each on concepts of its own; c0056 is also a design change, which the settled line counts under T3-004.

**homelab/t08** (class 1). The fleet, my B1 grouping and the settled line hold T3-073 (reporting how the work fared). All four fresh readings place T3-068 (converting a neighbour's art): arm 1 alone, arm 2 with T3-073 and T3-029 (mourning the lost work). The room wrote "homelab" over Homestuck's logo: "Found a logo that said 'Homestuck' * Decided to change to 'Homelab'" (c0046), "Done, now says homelab" (c0036). T3-068's `must_show` names "a logo rewritten with the room's letters". The fleet's whys set the item apart as "reporting how it fared rather than doing the conversion". Verdict: the fleet's shared assumption. Neither T3-068's nor T3-073's fields separate telling a conversion from doing it, and the conversion is the room's own work. Arm 2's T3-029 rests on "damn it. we lost" (c0054) and the unfinished logo (c0053).

**indonesia/t03** (class 1). The fleet, my B1 grouping and the settled line hold T3-005 (defending the work against attackers), T3-021 (watching and repairing the work) and T3-141 (covering the night shift). Both arm 1 readings place T3-005 and T3-141. Both arm 2 readings place T3-005 alone and list T3-141 under `also_present`. All four drop T3-021. The settled line's T3-021 rests on c0017 (tidying the flag), c0096 (clearing stray tiles) and c0051 ("defend it guys its falling apart"); T3-021's `must_not_show` sends "an attack fought as such" to T3-005, which takes c0051. Verdict: rule 0 applied differently. T3-021 still stands on two concepts of its own; the fresh readers judged that two placements carry the material, and arm 2 kept to one.

**japan/t11** (class 1). The fleet, my B1 grouping and the settled line hold T3-047 (making up with another sub). Three fresh readings add T3-011 (helping another room's work) on c0084 ("I'm also adding pixels to you guys") and c0087 ("I'll tell ubc members to help you guys out!"), which the settled line leaves uncarried. Arm 1 reading 2 places T3-170 (mistaking friendly work for vandalism) instead of T3-047: r/Tokyo took UBC's pixels for "a coordinated attack" and then corrected itself. Verdict: rule 0 applied differently, for T3-011. The T3-170 reading shows an undecided boundary: neither T3-047's nor T3-170's `must_not_show` names the other, and a mistaken accusation withdrawn with apology meets both gates.

**kingdomhearts/t17** (class 1). The fleet, my B1 grouping and the settled line hold T3-020 (choosing a canvas spot). Arm 1 reading 1 and both arm 2 readings place T3-038 (building and reporting the mark). The one concept is "started inside the Linux penguin!" T3-038's `must_show` names "started"; T3-020's names "a location announced ... before or while building". Verdict: the scheme does not decide. The concept meets both gates, and no discriminator joins T3-020 and T3-038.

**landry/t05** (class 1). The fleet, my B1 grouping and the settled line hold T3-052 (remarking on neighbouring pictures). Both arm 1 readings agree. Both arm 2 readings place T3-017 (carrying on ordinary sub talk). The one concept is "Well i'm going to need to head to an emergency eyewash station soon", said of the Madoka Magica image the label names. T3-052 needs "pictures around the room's mark"; the words do not say where the image is, and the coder's note calls it "the unseen image". Verdict: the scheme does not decide on these words. Whether the image is on the canvas next to the room's mark rests on the label.

**metroid/t16** (class 1). The fleet, my B1 grouping and the settled line hold T3-031 (playing the room's in-jokes). Both arm 1 readings agree. Both arm 2 readings place T3-017 (carrying on ordinary sub talk). The two concepts are "Have you ever heard the Tragedy of Old Bird the Wise?" and "Not too sure I have", with no canvas in them. T3-031's `must_show` needs humour "carried into canvas talk"; T3-017's discriminator allows the in-joke "carried into the canvas talk or the day". Verdict: the scheme does not decide. This is the listed defect for stage C1: the T3-017 and T3-031 discriminators disagree on T3-031's canvas condition.

**mindcrack/t03** (class 1). The fleet, my B1 grouping and the settled line hold T3-002 (calling members in to place). Three fresh readings agree. Arm 2 reading 2 adds T3-062 (recruiting kindred subs to help) on c0036 ("I've solicited Justin's stream to help") and c0068 ("We are getting help from the Hermitcraft discord"), and T3-152 (announcing what the chat decided) on c0016 (the FLOB Discord's plan). These concepts are not in the settled line's support. Verdict: rule 0 applied differently. One reader took the exception for help drawn from other communities, which T3-002's discriminator against T3-062 sends to T3-062.

**qotsa/t04** (class 1). The fleet, my B1 grouping and the settled line hold T3-038 (building and reporting the mark). Both arm 1 readings agree. Both arm 2 readings add T3-033 (proposing the room's mark) on c0014 ("I volunteer this, 37 x 37") and T3-070 (sharing coordinates, templates and how-to) on c0020 ("focus on the red first, then ... the black"). Each added theme has one concept of its own. Verdict: rule 0 applied differently.

**rust/t03** (class 1). The fleet, my B1 grouping and the settled line hold T3-031 (playing the room's in-jokes). Both arm 1 readings agree. Both arm 2 readings add T3-064 (spreading the room's joke elsewhere); arm 2 reading 2 also adds T3-017 (carrying on ordinary sub talk). The T3-064 concepts joke about taking the Rust gospel to Linus, RMS, the FSF and the GCC list; none takes it there. T3-064's `must_show` needs the joke "taken by members into another sub or site". T3-017's `must_not_show` names T3-031, and c0089 ("Is it rewritten in Rust yet?") answers the r/place proposal. Verdict: the fresh readings miss a field. The settled line holds.

**samuraijack/t13** (class 1). The fleet, my B1 grouping and the settled line hold T3-017 (carrying on ordinary sub talk). Three fresh readings agree. Arm 1 reading 1 places T3-048 (reacting to official April Fools). The one concept reassures a distressed viewer ("Never be worried or ashamed about the things that get you through the day") and does not talk about the joke. T3-048's `must_show` needs talk about the maker's April Fools joke. Verdict: the fresh reading misses a field. The settled line holds.

**southafrica/t13** (class 1). The fleet, my B1 grouping and the settled line hold T3-009 (celebrating the finished work). All four fresh readings make T3-105 (saving screenshots and timelapses) the primary. Three add T3-009, and both arm 2 readings add T3-117 (marking the canvas's end) on c0138 ("Sigh, all over way too soon"). T3-105's `must_show` ("timelapses ... posted as records") takes c0169 and c0173 (the timelapse posted and linked), c0174 (where to look in it) and c0170 ("that's some awesome sauce", said of the timelapse). The settled line counts c0170 under T3-009, which leaves T3-009 two concepts (c0139, c0140). Verdict: the fleet's shared assumption, on the primary. The fleet led with the congratulations; the timelapse concepts are more, and T3-105's gate takes them.

**UPenn/t01** (class 1). The fleet, my B1 grouping and the settled line hold T3-002 (calling members in to place). Three fresh readings agree. Arm 2 reading 2 places T3-038 (building and reporting the mark) first, on c0007 ("I'm working on it!"), then T3-002. Verdict: rule 0 applied differently. With one concept for each theme, the count in the discriminator between them does not decide which leads; the settled line counts c0007 under T3-002.

**Villanova/t05** (class 1). The fleet, my B1 grouping and the settled line hold T3-009 (celebrating the finished work). Three fresh readings agree. Arm 2 reading 2 adds T3-105 (saving screenshots and timelapses) on c0015 ("More Pictures" of the completed place). Verdict: rule 0 applied differently. T3-009's `must_show` includes "a final image posted as done", and one reader judged the extra pictures a record of their own.

**vim/t02** (class 1). The fleet, my B1 grouping and the settled line hold T3-002 (calling members in to place). Both arm 1 readings agree. Both arm 2 readings add T3-028 (running scripts for the work) on c0014 (a reddit-placebot repository). Arm 2 reading 1 also adds T3-021 (watching and repairing the work) on the maintenance concepts, and arm 2 reading 2 adds T3-170 (mistaking friendly work for vandalism) on c0013 ("Not being vandalized, it's a coordinated effort to move it down 3px"). Each concept passes the added theme's gate and is not in the settled line's support. Verdict: rule 0 applied differently.

**yuyuyu/t04** (class 1). The fleet, my B1 grouping and the settled line hold T3-151 (bartering help with neighbours). Both arm 1 readings agree. Both arm 2 readings add T3-194 (acting as envoys between rooms) on c0016 ("AN ENVOY FROM r/swissneutralityzone !"), which T3-194's `must_show` names ("a representative arriving in another room's thread"). Verdict: rule 0 applied differently, on one concept.

**49ers/t06** (class 2). The fleet holds T3-005 (defending the work against attackers). My B1 grouping and the settled line hold T3-005 and T3-021 (watching and repairing the work). Three fresh readings place both, as the settled line does: both arm 1 readings and arm 2 reading 2. Arm 2 reading 1 adds T3-059 (urging others to give up) on c0066 ("Starting to look like a lost cause"), words T3-059's `must_show` quotes. Verdict: rule 0 applied differently, in one reading. Three of four fresh readings support the B1 theme the fleet left out ("I'm keeping watch ... one pixel at a time", "fix it up").

**AmericanFlaginPlace/t03** (class 2). The fleet holds T3-038 (building and reporting the mark). My B1 grouping and the settled line hold T3-038, T3-065 (building the homeland's flag) and T3-103 (dividing the picture among teams). All four fresh readings place T3-065: arm 1 with T3-038, arm 2 reading 1 alone, arm 2 reading 2 with T3-103 on c0041 ("Team Field - We will take care of the blue field"). T3-065's `must_show` takes the flag of the room's own land "built as the room's mark ... Announcements that the flag has begun or is up". Verdict: the fleet's shared assumption. The two B3 readers placed the American flag as a mark of any kind; the B1 theme they left out is the one every fresh reader placed.

**AprilKnights/t08** (class 2). The fleet holds T3-038 (building and reporting the mark). My B1 grouping and the settled line add T3-022 (relocating after losing the spot) and T3-029 (mourning the lost work). All four fresh readings place T3-038; arm 2 reading 1 adds T3-069 (concentrating effort on fewer pieces) on c0067 ("we have transfered to defending the button"). No reading places T3-022 or T3-029. T3-029 has one concept of its own (c0054, "it's completely gone"). T3-022 has none: nothing is moved or restarted elsewhere after a loss. Verdict: the settled line keeps my B1 themes. The class 2 rule kept two themes that no reader of the fleet or of either arm placed, and the settled line places them without concepts.

**asexuality/t06** (class 2). The fleet holds T3-164 (feeling supported through the canvas). My B1 grouping and the settled line add T3-009 (celebrating the finished work) and T3-057 (remaking canvas art elsewhere). Both arm 1 readings place T3-164 and T3-009. Arm 2 reading 1 places T3-164 and lists T3-009 under `also_present`. Arm 2 reading 2 places all three, as the settled line does. Pride concepts carry T3-009: "I'm proud of us" (c0084), "pretty happy with our progress" (c0007). The settled line counts both under T3-164, whose `must_not_show` names "the work celebrated (T3-009)". T3-057 rests on one concept, the cross-stitch of the flag (c0042). Verdict: the fleet's shared assumption, for T3-009. Every fresh reading places or lists the B1 theme the fleet left out. T3-057 has one concept, and one fresh reading places it.

**bangtan/t11** (class 2). The fleet holds T3-011 (helping another room's work). My B1 grouping and the settled line add T3-150 (forming alliances between rooms). All four fresh readings place T3-011 alone. T3-150's `must_show` needs an alliance "for defence or a fight". Its one candidate concept is "Would BTS like to join up with r/Ireland in the future?" (c0057), which names neither. Verdict: the settled line keeps my B1 theme. No reader of the fleet or of either arm placed T3-150, and its gate is not met.

**belgium/t08** (class 2). The fleet holds T3-005 (defending the work against attackers). My B1 grouping and the settled line add T3-084 (asking other rooms for help). Three fresh readings add T3-062 (recruiting kindred subs to help) instead: arm 1 reading 1 and both arm 2 readings. The help concepts are "ask some help from other european subs" (c0053) and "a thread on /europe where we can gather strength from our allies" (c0054). The discriminator between the siblings asks whether "another sub's membership [is] asked for hands (T3-062), or another canvas group asked, as a group (T3-084)". A thread opened in another sub is T3-062's own example. The settled line counts c0053 to c0055 under T3-005. Verdict: the settled line keeps my B1 theme, where three fresh readers place its sibling. Arm 2 reading 2's T3-076 (reining in the room's attackers) rests on "Leave the Romanians be" (c0036, c0043).

**calgaryflames/t03** (class 2). The fleet holds T3-002 (calling members in to place). My B1 grouping and the settled line add T3-005 (defending the work against attackers) and T3-070 (sharing coordinates, templates and how-to). Arm 1 reading 1 places T3-002 and T3-005; arm 1 reading 2 places T3-002 alone. Both arm 2 readings make T3-005 the primary and list T3-002 and T3-070 under `also_present`. Many concepts are alarms: "WERE DYING!! SAVE THE C OF RED" (c0031), "we are being assailed by blue pricks" (c0116), "We're under invasion by Scotland and England" (c0218), "Alberta is being attacked!" (c0279). The discriminator sends a call "to defend against an attack under way" to T3-005. Verdict: the fleet's shared assumption. The two B3 readers folded the defence calls into T3-002. Three fresh readings place the B1 theme that holds them, and two list my B1's T3-070 (coordinates c0111, c0183, c0193).

**catalunya/t07** (class 2). The fleet holds T3-009 (celebrating the finished work). My B1 grouping and the settled line add T3-154 (claiming victory over rival rooms). All four fresh readings place T3-009 alone. T3-154 rests on one concept: "We were there first. The victory feels good btw." (c0068). Verdict: the settled line keeps my B1 theme. It stands on one concept, and no reader of the fleet or of either arm placed it.

**chicubs/t04** (class 2). The fleet holds T3-021 (watching and repairing the work). My B1 grouping and the settled line add T3-042 (choosing upkeep over expansion) and T3-141 (covering the night shift). Arm 1 reading 1 places T3-021 and T3-005 (defending the work against attackers). Arm 1 reading 2 places T3-021, T3-042 and T3-005. Both arm 2 readings place T3-021 and list T3-003, T3-005, T3-042 and T3-141 under `also_present`. T3-042 has three concepts of its own (c0045, c0075, c0213: hold the logo before growing it). T3-141 has three (c0082, c0112, c0197: staying up, the hand-off to the Chicago night shift). T3-005 has several ("It's currently under assault. I'm on it.", "we held the line"). Verdict: rule 0 applied differently. With four or five themes at three concepts each, rule 0's bag clause places one and lists the rest, as arm 2 did. The settled line places three with concepts for one. The fresh readers support my B1 themes as present.

**ChronoTrigger/t04** (class 2). The fleet holds T3-010 (settling borders with neighbours). My B1 grouping and the settled line add T3-061 (pushing into a neighbour's space) and T3-150 (forming alliances between rooms). Fresh: arm 1 reading 1 T3-010; arm 1 reading 2 T3-010 and T3-024 (refusing to cover others' work); both arm 2 readings T3-010, with T3-195 under `also_present`. T3-061 has two concepts that pass its gate ("wage war with that yellow thing ... for space", c0092; "wage war with the shiny Lucario", c0093), and T3-150 has two (an alliance proposed, c0055; "will also try to defend it from vandals", c0061). Verdict: the settled line keeps my B1 themes. Each has two concepts of its own, but no reader of the fleet or of either arm took rule 0's exception for them.

**clashroyale/t08** (class 2). The fleet holds T3-038 (building and reporting the mark). My B1 grouping and the settled line add T3-005 (defending the work against attackers) and T3-021 (watching and repairing the work). Both arm 1 readings place T3-038 and T3-005. Both arm 2 readings place T3-038 alone. T3-005 rests on "We've since been overrun! ... we must defend her!" (c0382) and "Save our princess" (c0383). No reading places T3-021. Verdict: rule 0 applied differently, for T3-005: the fresh readers split as the fleet and my B1 grouping did. For T3-021, the settled line keeps a B1 theme no reader placed.

**daftpunk/t03** (class 2). The fleet holds T3-010 (settling borders with neighbours). My B1 grouping and the settled line add T3-020 (choosing a canvas spot) and T3-039 (yielding space when asked). Fresh: arm 1 reading 1 and arm 2 reading 2 place T3-010; arm 1 reading 2 places T3-020 alone; arm 2 reading 1 places T3-010 and lists T3-020 under `also_present`. No reading places T3-039, though "I personally think we should let them have it" (c0048), said of the area r/straya asked for, meets its gate; the settled line counts c0048 under T3-010. Verdict: the settled line keeps my B1 themes. Two fresh readings support T3-020; T3-039 rests on a concept the settled line gives to T3-010.

**dallasstars/t09** (class 2). The fleet holds T3-002 (calling members in to place). My B1 grouping and the settled line add T3-017 (carrying on ordinary sub talk). All four fresh readings place T3-002 alone. T3-017 rests on one concept, the game-thread summary "Depression. Confusion. Some happiness when we see goals like that" (c0074). Verdict: the settled line keeps my B1 theme. It stands on one concept, and no reader of the fleet or of either arm placed it.

**FaroeIslands/t01** (class 2). The fleet holds T3-022 (relocating after losing the spot). My B1 grouping and the settled line add T3-026 (announcing the mark is up) and T3-065 (building the homeland's flag). Fresh: arm 1 reading 1 T3-022; arm 1 reading 2 T3-065 alone; both arm 2 readings T3-065 then T3-022. The room is named for the Faroes and builds the Faroese flag ("Could we as a community do a Faroe flag", c0001). T3-065's discriminator against T3-026 says "a flag built in a room named for a land is that land's flag unless its concepts name another", and sends announcements that the flag is up to T3-065 as well. Verdict: the fleet's shared assumption. Three fresh readings place the B1 theme the fleet left out. No reading places T3-026, whose concepts the same discriminator gives to T3-065.

**Fez/t02** (class 2). The fleet holds T3-014 (moving planning into a chat). My B1 grouping and the settled line add T3-153 (meeting other rooms in chat). Arm 1 reading 1 places both, as the settled line does; arm 1 reading 2 places T3-014 alone. Both arm 2 readings place T3-014, T3-153 and T3-152 (announcing what the chat decided). The concepts on Denmark's Discord ("invite us on your discord", c0064; "I will pass on your template in our discord!", c0084) are contact with another room through a chat. T3-014's `must_not_show` sends "talking with other rooms in their chats" to T3-153, yet the settled line counts both under T3-014. Verdict: the fleet's shared assumption. Three fresh readings place the B1 theme those concepts carry. Arm 2's T3-152 rests on "Danes in discord coordinating seem to be in on restoring your art" (c0043).

**floridagators/t09** (class 2). The fleet holds T3-014 (moving planning into a chat). My B1 grouping and the settled line add T3-152 (announcing what the chat decided) and T3-153 (meeting other rooms in chat). Fresh: arm 1 reading 1 T3-014; arm 1 reading 2 T3-014 and T3-152; both arm 2 readings T3-014, T3-152 and T3-056 (making joint marks with others). "The beautiful bastards on the discord servers have planned out the following Albert" (c0067) reports the chat's plan in the thread; T3-014's `must_not_show` sends that to T3-152, yet the settled line counts it under T3-014. Verdict: the fleet's shared assumption, for T3-152, which three fresh readings place. For T3-153, the one concept ("On discord we're organizing an alliance with the Smash guys", c0124) is read by arm 2 as the joint picture it plans (T3-056).

**floridagators/t10** (class 2). The fleet holds T3-043 (crediting who made the work). My B1 grouping and the settled line add T3-009 (celebrating the finished work) and T3-159 (rewarding helpers with prizes). Fresh: arm 1 reading 1 T3-043 and T3-009; arm 1 reading 2 T3-043; both arm 2 readings T3-009, T3-043 and T3-156 (adopting the mark as emblem). "It's over, and we finished strong with an untainted UF logo!! Well done" (c0125) and "Small victories" (c0027) celebrate with no one credited, which T3-043's `must_not_show` sends to T3-009. The flair for "the r/place defenders" (c0130, c0131) meets T3-156's "flair ... from the work" and my B1's T3-159 ("mock medals"). Verdict: the fleet's shared assumption, for T3-009, which three fresh readings place. For the flair, the scheme does not decide between T3-156 and T3-159.

**furry_irl/t23** (class 2). The fleet holds T3-054 (carrying work to new canvases). My B1 grouping and the settled line add T3-037 (arguing the canvas's worth). All four fresh readings place T3-054 alone. T3-037's `must_show` weighs "the canvas ... as a whole"; the concepts argue whether PlaceTwo is "a carbon copy of place" (c0164), which is talk about a later canvas, T3-054's gate. Verdict: the settled line keeps my B1 theme. Its gate is not met, and no reader of the fleet or of either arm placed it.

**GabrielDropout/t01** (class 2). The fleet holds T3-002 (calling members in to place). My B1 grouping and the settled line add T3-011 (helping another room's work) and T3-014 (moving planning into a chat). Both arm 1 readings place T3-002 alone. Both arm 2 readings place T3-002, T3-151 (bartering help with neighbours) and T3-014. "We've acquiesced our territory to your r/Tenma banner, so can you help us fight against r/AceAttorney?" (c0044) asks help in return for ground given, T3-151's gate; T3-011's `must_not_show` names "help traded for help (T3-151)", and the settled line counts c0044 under T3-002, whose `must_not_show` names calls to "another canvas room as a room". Verdict: the settled line keeps my B1 theme T3-011, where arm 2 places the sibling the fields name. T3-014 rests on one concept ("join the Discord!", c0056), which arm 2 places.

**kuwait/t01** (class 2). The fleet holds T3-065 (building the homeland's flag). My B1 grouping and the settled line add T3-070 (sharing coordinates, templates and how-to). All four fresh readings place T3-065 alone. T3-070 rests on the coordinates and the vertical plan (c0004, c0015); T3-065's `must_show` also takes "its spot". Verdict: the settled line keeps my B1 theme. No reader of the fleet or of either arm placed it.

**leafs/t08** (class 2). The fleet holds T3-001 (staging April Fools fake news) and T3-032 (objecting to April Fools posts). My B1 grouping and the settled line add T3-095 (testing others' April Fools claims). Three fresh readings place the fleet's two; arm 2 reading 1 places all three, as the settled line does. T3-095 has concepts of its own: members ask whether NHL news is a joke ("Inb4 April Fools and Werenski gets it", c0089; c0103; "Is it still April Fool's over there?", c0126). The discriminator sends claims from "the news" to T3-095. Verdict: rule 0 applied differently. One fresh reading took the exception my B1 grouping took; three kept to two placements.

**lego/t13** (class 2). The fleet holds T3-021 (watching and repairing the work). My B1 grouping and the settled line add T3-005 (defending the work against attackers). Three fresh readings place T3-021; arm 2 reading 2 places both, as the settled line does. T3-005 rests on one concept, "We mustn't allow the void to take over Lego" (c0192). Verdict: rule 0 applied differently, on one concept.

**loltyler1/t03** (class 2). The fleet holds T3-006 (calling to deface rivals' work). My B1 grouping and the settled line add T3-068 (converting a neighbour's art) and T3-154 (claiming victory over rival rooms). All four fresh readings place T3-006 alone; arm 2 reading 1 lists T3-061 under `also_present`. T3-068 has concepts of its own ("write #freetyler1 when we black out OSU", c0038; c0084; "REPLACE OSU WITH KIRBY", c0122), and T3-154 has two ("thank you for destroying OSU", c0039; "WE DID IT BOYZ", c0150). Verdict: the settled line keeps my B1 themes. Each passes its gate on concepts of its own, but no reader of the fleet or of either arm took rule 0's exception for them.

**marvel/t04** (class 2). The fleet holds T3-020 (choosing a canvas spot). My B1 grouping and the settled line add T3-031 (playing the room's in-jokes) and T3-123 (refusing to give up space). Three fresh readings place T3-020 alone. Arm 2 reading 1 adds T3-002 (calling members in to place) on the calls for help and T3-136 (doubting the room's strength) on "We'll need a lot more people for this invasion" (c0041). T3-031 rests on "because We Are Groot!" (c0039) and "you got me at 'Groot'" (c0040). T3-123 rests on r/Doormonster's "NOPE ... Go build in the void below us" (c0049), a neighbour's refusal, which T3-123's gate does not take as the room's own. Verdict: the settled line keeps my B1 themes. No reader placed either, and one rests on another room's act.

**mcgill/t02** (class 2). The fleet holds T3-014 (moving planning into a chat). My B1 grouping and the settled line add T3-070 (sharing coordinates, templates and how-to) and T3-151 (bartering help with neighbours). Both arm 1 readings place T3-014 alone. Both arm 2 readings place T3-153 (meeting other rooms in chat) and T3-067 (trading away another room's work); arm 2 reading 2 adds T3-070. "If you help me get rid of them now, you could take up that whole space" (c0007) offers up a third room's work, which T3-151's `must_not_show` sends to T3-067. "Join us on the discord to strategize!" (c0008) is said to an ally, which T3-014's `must_not_show` sends to T3-153. Verdict: the fleet's shared assumption, and my B1 grouping's T3-151 is the wrong sibling. Arm 2's placements follow both fields.

**miraculousladybug/t02** (class 2). The fleet holds T3-045 (arguing who was there first). My B1 grouping and the settled line add T3-010 (settling borders with neighbours). All four fresh readings place T3-045 alone. The exchange argues priority ("We were building on it first", c0006) and offers to help the other side find another spot (c0007); no line or space is agreed, which T3-010's gate needs. Verdict: the settled line keeps my B1 theme. Its gate is not met, and no reader of the fleet or of either arm placed it.

**monstercat/t02** (class 2). The fleet holds T3-001 (staging April Fools fake news). My B1 grouping and the settled line add T3-095 (testing others' April Fools claims). Arm 1 reading 1 places both, as the settled line does; the other three place T3-001 alone. T3-095 rests on "Can't find this on his twitter. Either he deleted it or this is fake" (c0008) and c0153. The discriminator turns on whether a member of this room staged the claim, and the words do not say who posted the fake release. Verdict: rule 0 applied differently. One fresh reading took the exception my B1 grouping took, on a concept whose source the item leaves open.

**monsterhunter/t10** (class 2). The fleet holds T3-015 (routing canvas posts into megathreads). My B1 grouping and the settled line add T3-063 (removing canvas posts by rule). Both arm 1 readings place T3-015 alone. Both arm 2 readings add T3-184 (pausing the sub's usual events) on "The /r/place thing is taking the sticky posts" (c0160), the question sticky displaced. The removals ("This thread has been removed as we are trying to keep all r/place discussion to" the sticky, c0153, c0155) point to the gathering thread, which the discriminator sends to T3-015. Verdict: the settled line keeps my B1 theme, whose discriminator gives its concepts to T3-015. No reader placed it.

**nVade/t07** (class 2). The fleet holds T3-117 (marking the canvas's end). My B1 grouping and the settled line add T3-009 (celebrating the finished work) and T3-043 (crediting who made the work). Both arm 1 readings place T3-117 alone. Arm 2 reading 1 places all three, as the settled line does; arm 2 reading 2 places T3-117 and T3-009. T3-009 rests on "I'm very proud of everyone here" (c0087) and "some of our invaders actually survived thankfully" (c0084); T3-043 rests on "we can point to our green guys and say 'I did that'" (c0089). Verdict: rule 0 applied differently. Arm 2 took the exception for my B1 themes, and arm 1 kept the fleet's single placement.

**ockytop/t02** (class 2). The fleet holds T3-006 (calling to deface rivals' work). My B1 grouping and the settled line add T3-055 (reshaping the mark against tampering) and T3-087 (tracing who changed the work). Both arm 1 readings place T3-006 alone. Arm 2 reading 1 places T3-068 (converting a neighbour's art), T3-006 and T3-076 (reining in the room's attackers); arm 2 reading 2 places T3-068 and T3-076. The raids lay the room's orange-and-white checkerboard over rivals' work: "THE CHECKERBOARDING OF FLORIDA'S UF WILL BEGIN AT 8PM" (c0058), "give them a beautiful orange and white checkerboard to wake up to" (c0030). T3-006's `must_not_show` sends "another's art turned into the room's own sign" to T3-068, and the settled line counts both under T3-006. "Maybe we should cancel the attack?" (c0060) and "We should stop the Florida attack" (c0061) call an attack off, T3-076's gate. Verdict: the fleet's shared assumption. My B1 themes have concepts of their own (a checkerboard border around the T, c0007 and c0008; "/r/TheWhiteVoid is attacking us", c0101), but no fresh reading placed them.

**onepunchman/t02** (class 2). The fleet holds T3-136 (doubting the room's strength). My B1 grouping and the settled line add T3-059 (urging others to give up) and T3-075 (objecting to the canvas flood). Fresh: arm 1 reading 1 T3-037 (arguing the canvas's worth) and T3-075; arm 1 reading 2 T3-136; both arm 2 readings T3-075 alone. "Stop spamming" (c0058), "Let us be lazy jerk offs in peace!" (c0057) and "This isnt the first time this was posted" (c0059) object to the posts, T3-075's gate. The settled line counts c0057 and c0058 under T3-136, whose gate is doubt that the room can make the work. Verdict: the fleet's shared assumption. Three fresh readings place the B1 theme those concepts carry. No reading places T3-059.

**placesnek/t02** (class 2). The fleet holds T3-024 (refusing to cover others' work). My B1 grouping and the settled line add T3-039 (yielding space when asked). Both arm 1 readings place T3-024 alone. Both arm 2 readings place T3-010 (settling borders with neighbours), T3-024 and T3-039. Most concepts are neighbours' requests ("Please don't damage the AMD logo", c0010; "we ... would appreciate if you led your snek around our logo", c0045; "Please do Not pass through the SU sub section", c0052), and the room answers them ("We can curve around the corner of the AMD logo", c0096). T3-024's `must_not_show` sends "moving because a neighbour asked" to T3-039, yet four of the five concepts the settled line counts under T3-024 are requests. Verdict: the fleet's shared assumption. Arm 2 places the B1 theme the requests carry. Its T3-010 rests on "we'll keep it in the border you're free to go downward" (c0013).

**placestart/t01** (class 2). The fleet holds T3-038 (building and reporting the mark). My B1 grouping and the settled line add T3-021 (watching and repairing the work). Three fresh readings add T3-004 (settling the mark's design); arm 2 reading 1 also adds T3-021; arm 2 reading 2 lists T3-004 under `also_present`. The corrections ("The title bar for the Van Gogh painting is wrong", c0325; "it needs two pixels of gray", c0354; UTC for the clock, c0355) are "corrections to make the placed work match the design", T3-004's gate. The discriminator sends them there, and the settled line counts c0325 and c0354 under T3-038. Verdict: the fleet's shared assumption. Three fresh readings place a theme neither the fleet nor my B1 grouping placed; one places my B1's T3-021.

**puzzleanddragons/t04** (class 2). The fleet holds T3-011 (helping another room's work). My B1 grouping and the settled line add T3-014 (moving planning into a chat) and T3-150 (forming alliances between rooms). All four fresh readings place T3-150: arm 1 reading 1 with T3-014 and T3-011, as the settled line holds them; arm 1 reading 2 alone; both arm 2 readings with T3-153 (meeting other rooms in chat). "All of our groups need to band together and defend the Puerto Rican flag" (c0037) and "If we all band together now, we may be able to stop them" (c0132) are "rooms joining a front"; T3-011's `must_not_show` names "an alliance for joint defence (T3-150)", and the settled line counts both under T3-011. Verdict: the fleet's shared assumption. Every fresh reading places the B1 theme. Arm 2 reads c0136, a neighbour sent to the room's Discord, as T3-153, the sibling T3-014's `must_not_show` names.

**reddevils/t18** (class 2). The fleet holds T3-050 (trading taunts with rivals). My B1 grouping and the settled line add T3-155 (saluting rivals after the fight). All four fresh readings place T3-050 alone. T3-155 rests on half a concept: "Aye lad fair one, now fuck off yer rat bastard" (c0209) returns thanks only to insult. Verdict: the settled line keeps my B1 theme. No reader of the fleet or of either arm placed it.

**rush/t08** (class 2). The fleet holds T3-001 (staging April Fools fake news). My B1 grouping and the settled line add T3-095 (testing others' April Fools claims). All four fresh readings place T3-001 alone. The testing replies sit inside the room's own fakes ("I feel bamboozled", c0056; the moderator's "GUYS THIS WAS FAKE", c0057, on the fake Neil Peart AMA). T3-095's `must_not_show` sends those to T3-001 ("readers caught by them included"). Only c0055, on the Xanadu mash-up, tests a claim whose source the words leave open. Verdict: the settled line keeps my B1 theme, which its own `must_not_show` excludes for most of its concepts. No reader placed it.

**scotland/t07** (class 2). The fleet holds T3-015 (routing canvas posts into megathreads) and T3-014 (moving planning into a chat). My B1 grouping and the settled line add T3-152 (announcing what the chat decided). Both arm 1 readings place the fleet's two. Both arm 2 readings place all three, as the settled line does. T3-152 rests on "no longer pasting over the NAT" (c0131), a Discord decision reported in the thread. Verdict: rule 0 applied differently. Arm 2 took the third placement my B1 grouping took; arm 1 kept the fleet's two.

**slovenia/t02** (class 2). The fleet holds T3-065 (building the homeland's flag). My B1 grouping and the settled line add T3-002 (calling members in to place) and T3-068 (converting a neighbour's art). Fresh: arm 1 reading 1 T3-065 and T3-113 (drawing national emblems); arm 1 reading 2 T3-065; arm 2 reading 1 T3-065, with T3-113 under `also_present`; arm 2 reading 2 T3-065, T3-113 and T3-068. The coat of arms carries T3-113, whose `must_show` names "a coat of arms": "Narejimo Grb" (c0021), "Manjka grb" (c0022), "Uspel je grb!" (c0024). T3-065's `must_not_show` sends "emblems ... drawn beside or inside the flag" to T3-113, yet the settled line counts c0022 and c0024 under T3-065. Verdict: the fleet's shared assumption. Three fresh readings place or list a theme neither the fleet nor my B1 grouping placed. My B1's T3-002 is excluded by T3-002's own `must_not_show` ("the national flag as the room's mark carries T3-065"). My B1's T3-068 rests on c0014 ("convert the slovakian flag ... to the slovenian flag"), which one fresh reading places.

**starcitizen/t06** (class 2). The fleet holds T3-031 (playing the room's in-jokes). My B1 grouping and the settled line add T3-033 (proposing the room's mark). Three fresh readings place both, as the settled line does; arm 1 reading 2 places T3-031 alone. T3-033 rests on one concept, "Can we make a giant" GIB 3.0 NAO drawing (c0101). Verdict: rule 0 applied differently. Three of four fresh readings took the exception my B1 grouping took, on one concept.

**tampabaylightning/t13** (class 2). The fleet holds T3-004 (settling the mark's design). My B1 grouping and the settled line add T3-049 (complaining the calls are scattered). All four fresh readings lead with T3-041 (extending the room's work); both arm 2 readings add T3-049, and arm 2 reading 2 adds T3-004. "I'm working on adding Tampa Bay up top" (c0103) and "we have rewritten Tampa Bay at the top of the logo ... expand it to be even better" (c0117) add to the mark. T3-004's `must_not_show` sends "a bigger or second piece" to T3-041, and the settled line counts both under T3-004. Verdict: the fleet's shared assumption. Every fresh reading leads with a theme neither the fleet nor my B1 grouping placed. Arm 2 places my B1's T3-049 on c0105 ("now It's just gonna be blue without any coordination?") and c0120.

**TheFarLeftSide/t13** (class 2). The fleet holds T3-005 (defending the work against attackers). My B1 grouping and the settled line add T3-086 (carrying in the sub's quarrel) and T3-087 (tracing who changed the work). All four fresh readings place T3-005 alone; both arm 2 readings list T3-087 and T3-073 under `also_present`. T3-087 has concepts of its own that name who is behind the attacks ("it is the Italians who have encroached ... using scripts", c0292; "info about the bot are in a pinned post in their sub", c0323; "Bot linked with fakenews, TD and the all-right", c0344). Verdict: the settled line keeps my B1 themes. No fresh reading places them, though arm 2 records T3-087 as present.

**TheHulk/t09** (class 2). The fleet holds T3-142 (making ethnic jokes about rivals). My B1 grouping and the settled line add T3-050 (trading taunts with rivals). All four fresh readings place T3-142 alone. All three concepts insult Croatians as a people ("little e-nazzies", c0038), which T3-050's `must_not_show` sends to T3-142. Verdict: the settled line keeps my B1 theme, which its own `must_not_show` excludes here. No reader placed it.

**twitchplayspokemon/t03** (class 2). The fleet holds T3-038 (building and reporting the mark). My B1 grouping and the settled line add T3-022 (relocating after losing the spot) and T3-070 (sharing coordinates, templates and how-to). Every fresh reading places T3-070. Arm 1 reading 1 leads with it, adding T3-038 and T3-009 (celebrating the finished work); arm 1 reading 2 places the settled line's three; both arm 2 readings place T3-070 alone, with T3-009 under `also_present`. The plans for placers carry T3-070: "Go here and zoom in" with coordinates (c0035), "New heart plan" (c0129), "NEXT AND PROBABLY FINAL NEW PLAN" (c0134), "Revised current plan" (c0136). The discriminator sends "directions posted for placers to follow" to T3-070, yet the settled line counts c0035 and c0136 under T3-038. Verdict: the fleet's shared assumption. Three fresh readings make my B1's T3-070 the primary.

**uofmn/t09** (class 2). The fleet holds T3-028 (running scripts for the work). My B1 grouping and the settled line add T3-014 (moving planning into a chat) and T3-087 (tracing who changed the work). Three fresh readings place T3-028 and T3-014; arm 1 reading 1 places T3-028 alone. T3-014 rests on one concept, "Should we start a Discord?" (c0072). T3-087 rests on "I think they have a bot" (c0080), which no reading places. Verdict: rule 0 applied differently, for T3-014. The settled line keeps T3-087, which no reader placed.

**wales/t02** (class 2). The fleet holds T3-002 (calling members in to place). My B1 grouping and the settled line add T3-041 (extending the room's work) and T3-113 (drawing national emblems). Fresh: arm 1 reading 1 T3-002; arm 1 reading 2 T3-002 and T3-065 (building the homeland's flag); arm 2 reading 1 T3-065; arm 2 reading 2 T3-065, T3-113 and T3-169 (signing the sub's name). "Lets Make the welsh Flag on R/Place!" (c0003), "Lets Make A Bigger Flag!" (c0034) and c0012 and c0031 call for the flag of the room's land. T3-002's `must_not_show` says "the national flag as the room's mark carries T3-065", yet the settled line counts c0003 and c0034 under T3-002. Verdict: the fleet's shared assumption, and my B1 grouping shares it. Three fresh readings place T3-065, which neither placed. One reading places my B1's T3-113 on "Cymru" and "Yma O Hyd" (c0016, c0018).

**wallstreetbets/t08** (class 2). The fleet holds T3-023 (running an April Fools takeover). My B1 grouping and the settled line add T3-095 (testing others' April Fools claims). Both arm 1 readings place T3-023 alone. Both arm 2 readings place both, as the settled line does. "Who fucked with the subreddit theme?" (c0064) and "Some mad secret tomfuckery going on with the css and subscribers" (c0058) work out what the change is, which the discriminator sends to T3-095. The settled line counts both under T3-023. Verdict: the fleet's shared assumption, on two concepts. Arm 2 places my B1's T3-095.

**warframe/t11** (class 2, a bag). The fleet holds T3-010 (settling borders with neighbours). My B1 grouping and the settled line add T3-035 (asking a host for space) and T3-094 (disputing who approves a spot), with T3-151, T3-162 and T3-011 under `also_present`. Both arm 1 readings place T3-010 and T3-151 (bartering help with neighbours). Arm 2 reading 1 places T3-094 and lists T3-162, T3-151 and T3-011. Arm 2 reading 2 places T3-162 (vetting others' requests to build) and lists T3-151, T3-011 and T3-073. GreenLattice's permission and no-build zone run through the item: "very picky about what will be allowed" (c0229), "they decided to no more art in that area" (c0254), "The people who made /r/GreenLattice have no authority" (c0300). Verdict: the scheme does not decide the primary of this bag. T3-010, T3-094 and T3-162 each take several concepts, and their discriminators sort concepts, not items. The settled line places three themes where rule 0's bag clause places one.

**witcher/t05** (class 2). The fleet holds T3-010 (settling borders with neighbours). My B1 grouping and the settled line add T3-046 (arguing whether covering is fair) and T3-050 (trading taunts with rivals). All four fresh readings place T3-010 alone. T3-046 has two concepts that pass its gate ("Your flag goes across the entire canvas. Come on, you need have some lenience", c0070; "It was an open online canvas for anybody to use", c0075), and T3-050 has two ("I'm gonna start vandalizing your whatever", c0068; "There are only 2 genders. got em", c0072). Verdict: the settled line keeps my B1 themes. Each passes its gate on concepts of its own, but no reader of the fleet or of either arm took rule 0's exception for them.

**witcher/t08** (class 2). The fleet holds T3-009 (celebrating the finished work). My B1 grouping and the settled line add T3-043 (crediting who made the work) and T3-073 (reporting how the work fared). All four fresh readings place T3-009 alone. T3-043 rests on one concept ("We had a great little squad of people working tirelessly to defend the banner. Thanks for helping out!", c0103). T3-073 rests on two accounts of the defence (c0096, c0098), and both end in celebration ("What matters is we did it!"). Verdict: the settled line keeps my B1 themes. Each rests on one or two concepts, and no reader placed them.

**WPI/t05** (class 2). The fleet holds T3-005 (defending the work against attackers). My B1 grouping and the settled line add T3-087 (tracing who changed the work). All four fresh readings place T3-005 alone. The proof concepts name RPI as the attacker ("Proof: .../r/RPI/.../help_us_hijack_the_wpi_rplace", c0007; "Here's proof! We need to stop them!", c0049), T3-087's "naming the room ... responsible". Each also serves the call to defend. Verdict: the settled line keeps my B1 theme. No reader of the fleet or of either arm placed it as a second theme.

**xcom/t12** (class 2). The fleet holds T3-075 (objecting to the canvas flood). My B1 grouping and the settled line add T3-090 (opening a canvas sub). All four fresh readings place T3-075 alone. "Please make /r/xcomplace" (c0088) and "maybe somebody could start r/xcomplace" (c0094) ask for a canvas sub, which T3-090's gate takes ("asked for"). They are also the objection itself, and the settled line counts both under T3-075. Verdict: the settled line keeps my B1 theme. Its concepts are the objection's own, and no reader placed it.
