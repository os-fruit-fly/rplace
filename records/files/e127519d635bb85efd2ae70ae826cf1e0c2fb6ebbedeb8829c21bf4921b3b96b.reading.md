# Saturation, stage B1: the test (B1c) and the second pass (B1d)

## B1c, the saturation test, 2026-10-11

### The rule and the sample

The seed and the rule were written into `notes-B1.md` (section "Leg B1c") before the draw. The 705 read rooms, sorted by name, were shuffled with `saturation.py`'s own `shuffled`, seed cd472a6087a223d4 (`out/seed.txt`), tag "B1c". Rooms were taken from the head of that order until at least 30 rooms and 300 second-order themes were reached (`out/_analysis/b1c_sample.py`). The sample is 30 rooms, 317 second-order themes, 3,891 concepts and 24.8 average rooms of words.

The 30 rooms, in draw order: rainbowgrid, stardustcrusaders, kamenrider, ik_ihe, kurdistan, poland, france, vinesauce, oman, mexico, gatech, PlaceNL, VelvetUnderground, ubc, DevonUK, glasgow, wholesomememes, cardinals, picturegame, radiohead, sixers, Fez, sakuragakuin, math, scp, foxes, drawhelix, ChronoTrigger, TeamDignitas, hellointernet.

Each room was printed whole with its second-order themes, their notes, and every concept's label, hour and first 90 characters of words, with the recorded placements filtered out. I held only `mem.py scheme --brief`, the 197 labels. The kinds have no written gates yet (B1e writes them), so the labels were the gates. Each second-order theme got a fresh placement and a verdict before the room's recorded placements were looked at (`out/_analysis/b1c_fresh.psv`). Disagreements with the record were then judged one by one (`out/_analysis/b1c_disagreements.psv`).

### The count

The next table gives the fresh verdicts for the 317 second-order themes.

| Verdict | Themes |
|---|---|
| fits: a label takes the theme and its concepts | 299 |
| gate fails: two labels take it and nothing decides, or the label misdescribes it | 15 |
| bare: a bare title, link or reply, unplaced in the record too | 3 |
| new kind: a concept or theme no label can take | 0 |
| split: a kind shown to hold two doings | 0 |

Comparing with the record added 20 more themes where the gate fails. These are themes the fresh reading placed without hesitation, but where the record chose a different kind and the two labels cannot say which reading is right. The comparison also found 2 slips in the fresh reading (glasgow t03, PlaceNL t20). It found 1 recorded kind used beyond its label (kurdistan t03, T3-132 names a Discord) and 2 label overlaps in additional kinds (poland t07, gatech t04).

**What does not fit: 35 of 317 second-order themes (11.0%) in 20 of the 30 rooms meet a gate that fails. No concept needs a new kind and no kind needs a split.** By the concept test, the new kinds per hundred second-order themes in the sample are 0.

The 35 themes fall into three groups.

- **Two labels both take the theme (15).**
  - T3-003 against T3-038: stardustcrusaders t05, wholesomememes t07.
  - T3-074 against T3-136: vinesauce t08, scp t02.
  - T3-037 against T3-098: glasgow t02, cardinals t04.
  - T3-044 against T3-082, for the mark drawing outsiders to the room: DevonUK t02, hellointernet t12.
  - T3-068, T3-061 and T3-006, for replacing another nation's flag with one's own: kurdistan t02.
  - T3-024 against T3-010: stardustcrusaders t06.
  - T3-046 against T3-076: PlaceNL t14.
  - T3-016 against T3-074: wholesomememes t09.
  - T3-010 against T3-151: Fez t07.
  - T3-010 against T3-149, for non-aggression pacts: math t04.
  - T3-070 against T3-091, both naming templates: ChronoTrigger t02.
- **A label narrower than its use (5).**
  - T3-065 says national, and was used for the Devon county flag (DevonUK t01).
  - T3-115 says a rival fandom, and was used for Europe's call for help (gatech t07).
  - T3-063 says canvas posts, and was used for April Fools posts (wholesomememes t15).
  - T3-048 says the company, and a creator's own joke did not reach it in the record (wholesomememes t13).
  - T3-088 says extra accounts, and was used for a placement glitch (hellointernet t08).
- **No single label names the theme's doing (15 themes, 10 doings).** The labels take each concept, but not the whole. The 10 doings:
  - registering or hoping beyond the canvas's end: stardustcrusaders t17, oman t06, PlaceNL t19, ubc t09, sakuragakuin t11. The record put these in T3-016, T3-073 and T3-117.
  - watching and reporting the live canvas: france t09, cardinals t06.
  - gathering lone placers into a group: rainbowgrid t02.
  - drawing up the room's plan of operations: france t05.
  - enlarging the room's own mark: mexico t05.
  - a canvas thread taken over by side disputes: mexico t18.
  - organisers conceding that placers ignore the plan: PlaceNL t11.
  - crossposting designs between subs: PlaceNL t13.
  - routing posts to sister subs: wholesomememes t10.
  - April Fools talk with no fake staged: wholesomememes t12.

  Four of these doings were logged as ideas at the count, not when first seen (`ideas-B1.jsonl` lines 211 to 214). They are reporting the live canvas, conceding placers ignore the plan, gathering lone placers together, and planning the room's pixel operations. If all four became kinds, the sample's rate would be 1.26 new kinds per hundred second-order themes. If all ten did, it would be 3.15.

### The fresh reading against the record

The next table compares the fresh placements with the recorded ones. It covers the 313 second-order themes that both readings placed (`out/_analysis/b1c_totals.py`).

| Measure | Value |
|---|---|
| same primary kind | 263 (84.0%) |
| fresh primary among the recorded kinds | 281 (89.8%) |
| at least one kind shared | 297 (94.9%) |
| no kind shared | 16 (5.1%) |
| kinds per theme, fresh / recorded | 1.75 / 1.81 |
| recorded placements the fresh reading did not give | 165 of 565 |
| fresh placements the record does not hold | 147 of 547 |

The primary kinds hold across two readings by the same reader at different times. The placements as a whole hold less well: 165 of 565 recorded placements and 147 of 547 fresh ones have no match in the other reading. Primaries agree in 84 to 90% of themes, so most of these differences lie in the second and third kinds of rule 0. Stage B3 places from the gates. So the gates written at B1e must say when a second kind is owed, or the fleet will disagree there most.

### Beside it: the first pass's new kinds per hundred second-order themes

These figures were computed by room (`out/_analysis/b1c_discovery.py`). The rooms are in the order the first pass read them, and each mint in `theme_discovery.jsonl` is set at the end of its room. The `themes_read` field of `theme_discovery.jsonl` counts reads with repeats, so it is not used. Over the whole first pass: 197 mints in 7,844 second-order themes, 2.51 per hundred. There were 60 in the first hundred themes and 0 in the last hundred. The last mint, T3-197, came in room 661 of 705. 44 rooms and 520 second-order themes followed it with no new kind. The stopping rule counts 202 kinds, because it counts the PI's splits of T3-010 as new kinds.

The next table gives the first pass's mints by tenths of the rooms read.

| Rooms | Second-order themes | New kinds | Per hundred |
|---|---|---|---|
| 1 to 70 | 841 | 135 | 16.05 |
| 71 to 141 | 864 | 28 | 3.24 |
| 142 to 212 | 760 | 14 | 1.84 |
| 213 to 282 | 784 | 11 | 1.40 |
| 283 to 352 | 750 | 3 | 0.40 |
| 353 to 423 | 880 | 5 | 0.57 |
| 424 to 494 | 745 | 0 | 0.00 |
| 495 to 564 | 757 | 0 | 0.00 |
| 565 to 634 | 689 | 0 | 0.00 |
| 635 to 705 | 774 | 1 | 0.13 |

The test found 0 new kinds per hundred by the concept test. That matches the first pass's last four tenths: 1 new kind in 2,965 themes, 0.03 per hundred. If the four logged ideas became kinds, the test's rate would be 1.26 per hundred. That lies between the first pass's rates in rooms 213 to 282 (1.40) and rooms 283 to 352 (0.40). The kinds have saturated. The labels, read as gates, have not: one theme in nine meets a label that cannot decide or that says too little.

### Rooms for the second pass's chosen list

The rule names every room with a verdict other than fits. The rooms with a gate that fails (20): rainbowgrid, stardustcrusaders, kurdistan, france, vinesauce, oman, mexico, gatech, PlaceNL, ubc, DevonUK, glasgow, wholesomememes, cardinals, Fez, sakuragakuin, math, scp, ChronoTrigger, hellointernet. ik_ihe's only such verdict is a bare pointer. It is named here, but it gives the second pass nothing to test. The 9 rooms where every theme fit: poland, kamenrider, VelvetUnderground, picturegame, radiohead, sixers, foxes, drawhelix, TeamDignitas.

## B1d, the second pass

### The chosen list and the rule

`out/pass2-chosen-B1.txt` was written at B1d-01 before the first room was reread. It holds 108 rooms in three groups:
- the 20 rooms with a gate that failed at B1c;
- 23 more rooms with the most hesitations in the log (`out/_analysis/b1d_hesitations.py`: the top 20 by score, with ties at the twentieth score kept, 24 rooms, PlaceNL already in the first group);
- 65 more contrary rooms. These are the 66 rooms tagged "contrary room" in the B1 log through B1b-22, plus morrowind and Summit1G from the head; ubc, wholesomememes and Fez are already in the first group. `contrast.md` lists the contrast's two sides, not the contrary rooms, so this group may be short of the A1 heads' lists.

The rooms are read in the seeded order (`saturation.py order --stage B1`). Each room gets its A1 note, every second-order theme with every concept's words, and its forest whole. `mem.py reread` records each room in `pass2-B1.jsonl`. The pass stops when two things hold (J, 2026-10-07). Every chosen room has been read. The run since this pass's last new kind has reached marker 1's empty run, 78 rooms and 72.1 average rooms, and at least 30 rooms.

### The stretches

The next table gives each stretch, its new kinds and the run after it, from `saturation.py pass2 --stage B1`.

| Stretch | Leg | Orders | Rooms | Codes and themes | New kinds | Run after the stretch |
|---|---|---|---|---|---|---|
| 1 | B1d-01 | 47 (morrowind) to 184 (egypt) | 21 | about 974,000 bytes | 0 | 21 rooms, 21.4 average rooms |
| 2 | B1d-02 | 193 (totallynotrobots) to 256 (brasil) | 24 | 1,057,696 bytes | 0 | 45 rooms, 45.2 average rooms |
| 3 | B1d-03 | 265 (Okami) to 330 (megaman) | 18 | 782,756 bytes | 0 | 63 rooms, 63.1 average rooms |
| 4 | B1d-04 | 332 (ainbowroad) to 371 (ukplace) | 10 | 1,009,574 bytes | 0 | 73 rooms, 83.1 average rooms |
| 5 | B1d-05 | 381 (placehearts) to 571 (runescape) | 12 | 1,027,761 bytes | 0 | 85 rooms, 106.8 average rooms |
| 6 | B1d-06 | 574 (theblackvoid) to 627 (starcitizen) | 11 | 927,118 bytes | 0 | 96 rooms, 126.2 average rooms |
| 7 | B1d-07 | 641 (prequelmemes) to 703 (TheFarLeftSide) | 12 | 918,889 bytes | 0 | 108 rooms, 148.1 average rooms |

Stretch 1 rooms, in order: morrowind, Summit1G, popheads, homelab, qotsa, aeskwadraat, falcons, canucks, cirkeltrek, kurdistan, theitalyplace, PinkVomitMonster, ubc, bobross, pcmasterrace, mariokart, rust, gatech, AprilKnights, flashtv, egypt. After it, 21 of the 108 chosen rooms are read. The next room is totallynotrobots.

Stretch 1 minted nothing, split nothing and merged nothing. It logged 28 place events into existing kinds (`kinds-B1.jsonl`) and 9 unplacements, so placements rose by 19, from 13,440 to 13,459. Most of the new placements are second or third kinds under rule 0. Four of the events and four of the unplacements belong to two moves that were reverted the same leg (popheads t04, mariokart t02; see `notes-B1.md`). It also wrote 23 rule 0 lines and 1 bag (theitalyplace t08) and 9 `tier_history.jsonl` lines. One kind was widened. T3-188 (disowning rogue offshoots of the work) had held one theme. It now holds 6 themes in 6 rooms: ainbowroad, cirkeltrek, polska, PlaceNL, denmark and gatech. This is the doing the B1c idea "conceding placers ignore the plan" named: an organised room tells others it does not control the placers acting in its name. At B1e its label is to become "separating the plan from placers it cannot control". The stretch did not meet the other three B1c ideas: reporting the live canvas, gathering lone placers together, and planning the room's pixel operations.

The gates that failed at B1c in kurdistan t02, ubc t09 and gatech t07 need B1e work, not new kinds. kurdistan t02 needs a discriminator between T3-068, T3-061 and T3-006. ubc t09 and gatech t07 need the label changes already listed for T3-117 and T3-115.

Stretch 2 rooms, in order: totallynotrobots, orderofthebluecorner, GreenEmpire, tenma, nVade, ontario, furry_irl, starryknights, evedreddit, mexico, hellointernet, oman, placehfarts, anime, magictcg, Redox, utaustin, dankmemes, heyyea, azores, aoe2, anarcho_capitalism, korea, brasil. After it, 45 of the 108 chosen rooms are read. The next room is Okami.

Stretch 2 minted nothing, split nothing and merged nothing. It logged 3 place events into existing kinds and 1 unplacement, so placements rose by 2, from 13,459 to 13,461. One second-order theme moved: furry_irl t17, the moderators' new removal rules after April Fools, went from T3-017 to T3-185 (one `tier_history.jsonl` line). Two themes took a second kind under rule 0 (2 lines in `out/_analysis/b1_multiplace_b1d02.psv`). magictcg t04 took T3-048 for readers playing along with a creator's and a webshop's own April Fools. anarcho_capitalism t10 took T3-017 for members' own talk of physical removal at hour 94.

The T3-188 doing (separating the plan from placers the room cannot control) appeared six more times, each in a bag or as a single concept: nVade (twice), furry_irl c0192, mexico c0187, hellointernet c0135, aoe2 c0241 and korea c0071. It needs no new kind. In brasil, Argentine members told the room that their sub was not writing 7-1 on the flag (c0058, c0180, c0213). That denies the act rather than disowning placers. The T3-188 gate at B1e must say whether such a denial counts.

The gates that failed at B1c and were met in this stretch need B1e work, not new kinds. mexico t05 needs the T3-041 label change. mexico t18 (a canvas thread taken over by side disputes) stays in T3-017. hellointernet t08 (a placement glitch) needs the decision between T3-074 and T3-088. hellointernet t12 needs the T3-044/T3-082 discriminator. oman t06 needs T3-117 to take registering the end; heyyea t11 and aoe2 t11 are two more themes of that kind. The stretch did not meet the three B1c ideas still open: reporting the live canvas, gathering lone placers together, and planning the room's pixel operations.

Stretch 3 rooms, in order: Okami, kanye, glasgow, stardewvalley, danganronpa, warthunder, SwissNeutralityZone, masseffect, ibo, finland, Thegreatblackhole, kpop, lego, wine, duckgame, cfb, rotmg, megaman. After it, 63 of the 108 chosen rooms are read. The next room is ainbowroad.

Stretch 3 minted nothing, split nothing and merged nothing. It logged 2 place events into existing kinds and 3 unplacements, so placements fell by 1, from 13,461 to 13,460. One second-order theme moved: warthunder t15, filtering and policing the meme surge, went from T3-063 to T3-185 (one `tier_history.jsonl` line). None of its posts is about the canvas. One theme was bagged. finland t04 held T3-076, T3-081 and T3-087, and the reread found T3-188 carried by three concepts (c0032, c0033, c0039). It is now one placement under T3-076 with a bag line naming T3-188, T3-087 and T3-081 (two `tier_history.jsonl` lines for the unplacements). One theme took a second kind under rule 0 (1 line in `out/_analysis/b1_multiplace_b1d03.psv`). megaman t11 took T3-188: the room told r/osuplace and the Dat Boi room that it had virtually no control over the beam (c0042, c0067). T3-188 now holds 7 themes in 7 rooms.

The T3-188 doing also appeared in masseffect c0124, stardewvalley c0086 and megaman t10 (c0043, c0044), in bags or as single concepts. Four more cases bear on the gate question raised in brasil, whether a denial of the act ("it was not us") counts: kanye c0216, the room's own member telling TheFarLeftSide it did not attack; a Mexican member in duckgame's thread 62qdx6 telling the room that Mexico was not covering the duck; a Slovenian member in rotmg asking to be told of attacks by Slovenians so they could sort them out (c0197); and r/CFB's moderator blaming the lost logo on "rogue elements in the Green Lattice" (cfb c0518).

The gate that failed at B1c in glasgow t02 needs the T3-037/T3-098 discriminator, not a new kind. rotmg t14, an infinite-pixel glitch in T3-016, is another case for the T3-016/T3-074 discriminator: nyjets and furry_irl hold the same doing in T3-074. The stretch did not meet the three B1c ideas still open: reporting the live canvas, gathering lone placers together, and planning the room's pixel operations.

Stretch 4 rooms, in order: ainbowroad, dota2, ubreddit, Fez, azerbaijan, scp, wholesomememes, placestart, UNLincoln, ukplace. After it, 73 of the 108 chosen rooms are read. The next room is placehearts.

Stretch 4 minted nothing, split nothing and merged nothing. It logged 3 place events into existing kinds and 2 unplacements, so placements rose by 1, from 13,460 to 13,461. Two second-order themes moved, both in wholesomememes and both under the B1b-20 April Fools rule (two `tier_history.jsonl` lines). wholesomememes t12, members proposing pranks to play on friends off the site, went from T3-001 to T3-017: it stages no fake and plays inside none. wholesomememes t13, members trading outside creators' own April Fools releases, went from T3-017 to T3-048. One theme took a third kind under rule 0 (1 line in `out/_analysis/b1_multiplace_b1d04.psv`). scp t06 took T3-048: most of its concepts greet and riff on the SCP wiki author's annual April Fools tale. T3-188 still holds 7 themes in 7 rooms.

The run since this pass's last new kind is 73 rooms and 83.1 average rooms. It has passed the target in average rooms (72.1) but not yet in rooms (78). 35 chosen rooms are still unread, so the pass goes on.

ainbowroad's forest print stopped at line 5,000 of 6,901. The rest was printed with `--offset 5001` and read. `out/_analysis/b1d_forest_lengths.py` then checked the 63 rooms reread in stretches 1 to 3. None has a forest over 5,000 lines, so no earlier print was cut.

The T3-188 doing appeared again as single concepts or in bags: ainbowroad c1080 and dota2 c0827, c1037, c1104 and c1121. More cases bear on the gate question, whether an outside room's denial or disowning counts. In ainbowroad, a Void member said members were told not to touch the road (c1787), Blue denied an attack and blamed Red (c0117), r/Denmark said it was not trying to destroy the road (c1325), and r/france apologised in an uncoded post (thread 634mb9). In dota2, a representative of the Colombia, Venezuela and Ecuador flag set a few random users apart from the group (c1043). In Fez, Danish members said a few were destroying the work against the majority's wish and denied that it was them (c0059, c0072, c0081, c0092, c0094); these events are E760, and denmark t13 already holds T3-188. In placestart, an outside room said placestart's "volunteers" still followed the wrong template (c0137). In ukplace, an outside member reported that the room's people "claim no knowledge" (c0033), and members set the room's scripting apart from others' botnets (c0088) and denied that the flag expanded (c0091).

The B1c gates met in this stretch need B1e work, not new kinds. Fez t07 stays in T3-151: a deal whose terms are help given in return goes to T3-151, and a deal over borders and space alone to T3-010. scp t02 stays in T3-074; the T3-074/T3-136 discriminator is still owed. In wholesomememes, t07 stays in T3-003, since it is one member's own small marks and not the room's mark (T3-038). t09, a placing glitch explained, stays in T3-016 beside rotmg t14, for the T3-016/T3-074 discriminator. t10, moderators routing posts to sister subs, keeps its rule 0 line (T3-017 with T3-063); T3-015 was set aside because t10 does not route canvas talk into one thread. t15 needs the T3-063 label change already listed. placestart c0166, a member placing without limit through a glitch, is one more case for the T3-074/T3-088 question. placestart c0477, a member refusing the room's own treaty, is a single concept near T3-102. The stretch did not meet the three B1c ideas still open: reporting the live canvas, gathering lone placers together, and planning the room's pixel operations.

Stretch 5 rooms, in order: placehearts, stardustcrusaders, france, cardinals, FloydVsVoid, ChronoTrigger, philippines, ireland, Slovakia, unitedkingdom, hawks, runescape. After it, 85 of the 108 chosen rooms are read. The next room is theblackvoid.

Stretch 5 minted nothing, split nothing and merged nothing. It logged 4 place events into existing kinds and 8 unplacements, so placements fell by 4, from 13,461 to 13,457. No theme moved. Four themes took a second or third kind under rule 0 (4 lines in `out/_analysis/b1_multiplace_b1d05.psv`). placehearts t11 took T3-046: Lakers members answer the room's complaint about their logo by asking how many designs the hearts had covered. cardinals t05 took T3-037: c0091, a carrying code of the A1 note, judges the canvas made only for tearing down while endorsing the attack on the Cubs logo. hawks t07 took T3-097: the moderators' post closing the Breadman makeover, and a member asking whether bread pictures are still allowed. runescape t10 took T3-086: the split between RuneScape 3 and old-school players carried onto the shared logo, as btc holds the block-size split.

Four themes were bagged, because the reread found more than three kinds carried by concepts of their own. ChronoTrigger t02 (kept T3-070) names T3-091, T3-015 and T3-014. ireland t03 (kept T3-065) names T3-003, T3-091, T3-002, T3-009 and T3-021. ireland t06 (kept T3-061) names T3-006, T3-024 and T3-081, the last for Republican slogans and IRA written over the Union Jack. unitedkingdom t04 (kept T3-070) names T3-028, T3-090, T3-049, T3-101 and T3-014. The bag files are `out/_analysis/b1d05_bags_*.txt`. The rule 0 writer wrote eight `tier_history.jsonl` lines for the unplacements. T3-188 still holds 7 themes in 7 rooms.

The run since this pass's last new kind is 85 rooms and 106.8 average rooms. It has passed both targets, 78 rooms and 72.1 average rooms. 23 chosen rooms are still unread, so the pass goes on.

The two B1c ideas first logged at france were met there again and not minted. Idea 214, planning the room's pixel operations: france t05 stays a bag under T3-070 naming T3-066, T3-167, T3-069 and T3-010, since those kinds already hold the plan's parts. Idea 211, reporting the live canvas: france t09 keeps T3-073 with T3-087 and T3-052, since a live report and a later account are one doing told at different hours; cardinals t06 stays in T3-073 for the same reason. For B1e, T3-070's gate should say that plans of colours, borders and timings are included, and T3-073's gate should say that live reports are included. The third open idea, gathering lone placers together, was not met.

The T3-188 doing appeared again as single concepts or in bags: placehearts c0082 (in t06's bag), france c0280 (missing from t07's bag) and FloydVsVoid c0128. More cases bear on the gate question, whether an outside voice's denial counts. In france, a member said a boaster from an outside forum did not speak for that forum (c0573). In hawks, a member told a Blues fan that random griefers, not the rival camp, did most of the damage (c0176). In runescape, members set a sabotage post on the old-school sub apart from the old-school players who helped, and defended the old-school sub by recalling mutual help (c0490, c0501).

The B1c gates met in this stretch need B1e work, not new kinds. stardustcrusaders t05 and t06 need the T3-003/T3-038 and T3-024/T3-010 discriminators; its t17 is one more case for T3-117 taking registering the end. cardinals t04 stays in T3-037; the T3-037/T3-098 discriminator is owed with glasgow t02. ChronoTrigger t02 needs the T3-070/T3-091 discriminator. Three gate questions are new. placehearts t07, an insult covered with LOVE, asks whether T3-146 takes insults. Slovakia t02, r/slovenia's joke raid on the room, asks whether T3-023 takes one sub's joke on another. runescape's argument over scripts (c0424, c0477 to c0480) asks whether T3-027 takes saying that a defence was scripts, not people. Kinds missing from existing bags are recorded in the room notes, among them philippines t07 (T3-170, T3-130), ireland t08 (the wall politics, T3-142), unitedkingdom t10 (T3-081, the Falklands) and runescape t12 (T3-168, T3-150, T3-086).

Stretch 6 rooms, in order: theblackvoid, detroitredwings, loltyler1, CKCrusaders, math, parahumans, PlaceNL, vinesauce, earthbound, homestuck, starcitizen. After it, 96 of the 108 chosen rooms are read. The next room is prequelmemes.

Stretch 6 minted nothing, split nothing and merged nothing. It logged no place events and 12 unplacements, so placements fell by 12, from 13,457 to 13,445. No theme moved, and no theme took a second or third kind under rule 0 (`out/_analysis/b1_multiplace_b1d06.psv` holds no lines). Six themes were bagged, because the reread found a fourth kind carried by a carrying code of the A1 note or by a group of concepts of its own. theblackvoid t07 (kept T3-171) names T3-041, T3-022 and T3-042; about a dozen concepts argue for keeping the Void pure against expanding it. detroitredwings t10 (kept T3-021) names T3-009, T3-028 and T3-188; c0129, a carrying code, tells r/TransFlagPlace that the wheel was the sub's only coordinated effort and that others writing beside it were not the sub's doing. loltyler1 t08 (kept T3-149) names T3-151, T3-027 and T3-150; c0218, a carrying code, seeks a bigger alliance because the room cannot defend while its streamer is offline. PlaceNL t14 (kept T3-046) names T3-011, T3-045 and T3-102; c0125, a carrying code, and c0213 tell of a member and friends demolishing the Yeti with scripts and ten accounts against the room's call to spare it. vinesauce t08 (kept T3-074) names T3-069, T3-181 and T3-136; three concepts doubt that the room can manage the work at all. earthbound t05 (kept T3-010) names T3-150, T3-151, T3-194 and T3-137; two carrying codes add the last two, c0066 (a messenger from r/placestart asking for help) and c0059 (the cultists' loss accepted because the room worked with the taskbar). The bag files are `out/_analysis/b1d06_bags_*.txt`. T3-188 still holds 7 placed themes in 7 rooms.

The bag writer, `b1_bags_from_file2.py`, writes one `tier_history.jsonl` line per kind per leg and skips a kind that already has one. T3-151 lost loltyler1 t08 and then earthbound t05 in this leg, so the second unplacement got no line. A new helper, `out/_analysis/b1d_tier_unplace_fill.py`, compares the leg's unplacements in the diary with the leg's `members_changed` lines and writes a line in the writer's format for each one missing. It wrote one, for T3-151 earthbound t05. `tier_history.jsonl` rose from 97 to 109 lines: 11 from the bag writer and 1 from the helper. Its dry runs on B1d-01 to B1d-04 flag 13 unplacements; each already has a line under the same kind in its leg, in a layout the helper does not read. B1d-05 shows none.

The run since this pass's last new kind is 96 rooms and 126.2 average rooms. It has passed both targets, 78 rooms and 72.1 average rooms. 12 chosen rooms are still unread, so the pass goes on. The last stretch runs from prequelmemes (641) to TheFarLeftSide (703): 12 rooms and 918,889 bytes.

The B1c gates met in this stretch need B1e work, not new kinds. math t04 stays in T3-149, because its pact ended an encroachment already under way (c0027, c0028). For B1e, the T3-010/T3-149 discriminator should say that a pact ending or forestalling a fight between rooms already in contact goes to T3-149, and an agreement drawing borders or sharing space where no fight began goes to T3-010. vinesauce t08 failed for a real reason, and T3-136 is now in its bag. The T3-074/T3-136 discriminator should say that doubting whether the room can manage a work at all goes to T3-136, even during the work, and that working around the timer and too few hands while building goes to T3-074. PlaceNL t14 holds one concept of reining in (c0132), so it stays under T3-046; the T3-046/T3-076 discriminator is still owed. PlaceNL t19 is one more case for T3-117 taking registering the end. PlaceNL t13 stays in T3-070 with T3-013, and t20 stays unplaced.

The open B1c idea, gathering lone placers together, was met once. homestuck t11 asks two nearby logo attempts to work together and sends a new attempt to the existing one (c0011, c0012, in T3-069 under a rule 0 line); in t03 a member joins the shared build after working alone (c0303). T3-069 carries the doing, so the idea needs no kind.

The T3-188 doing appeared again in detroitredwings t10's new bag (c0129, c0146), in PlaceNL t14 (c0123, c0131, two concepts beside t11, which holds T3-188) and as single concepts in theblackvoid (c0577, c0830). More cases bear on the gate question, whether an outside voice's denial counts. A TransFlagPlace member said their room was not the one erasing the Red Wings logo, and another outside member owned the attack (detroitredwings c0155, c0149). A CKCrusaders member set Norwegian rogues apart from the official Norwegian ally (c0066). In vinesauce, an r/France member blamed France's own equivalent of 4chan for destroying everything on the French flag that is not French (c0043, relayed in c0098; c0058 from r/homestuck; E1066). In homestuck, the placesnek admin apologised for the Snek crossing the numbers and tried to stop it (c0114). In starcitizen, the room cleared its ally of attacks made in the ally's name, calling them false-flag attacks meant to split the two rooms (c0307, c0309, c0313).

Kinds missing from existing bags are recorded in the room notes. Five of them have a carrying code of the A1 note behind them: theblackvoid t02 (T3-193, c0692), CKCrusaders t01 (T3-091, c0032 and c0049), homestuck t15 (T3-151, c0098 and c0175) and starcitizen t11 (T3-194 and T3-150, both c0223). starcitizen t11's bag files the KSP envoy's defence pact and the named space alliance under T3-010, its kept kind; at B1e those parts belong to T3-194 and T3-150. For the floor at B1e, two one-room kinds have a second room's concept: T3-007 (parahumans c0007, in a bag only) and T3-077 (PlaceNL c0087, a single concept).

Stretch 7 rooms, in order: prequelmemes, heroesofthestorm, rocketbeans, ucf, sakuragakuin, israel, reddevils, lsu, rainbowgrid, thesilphroad, DevonUK, TheFarLeftSide. After it, all 108 chosen rooms are read.

Stretch 7 minted nothing, split nothing and merged nothing. It logged 1 place event into an existing kind and 14 unplacements, so placements fell by 13, from 13,445 to 13,432. No theme moved. One theme took a third kind under rule 0 (1 line in `out/_analysis/b1_multiplace_b1d07.psv`). thesilphroad t09 took T3-095: members ask whether Niantic is turning the game into an alternate reality game, say the Team Rocket event is not Niantic's and not in the game, and ask whether its story came from data mined from the game (c0269, c0274, c0434, c0501). Under the B1b-20 rule, that is testing a claim the theme did not stage.

Seven themes were bagged, because the reread found a fourth kind carried by a carrying code of the A1 note or by a group of concepts of its own. prequelmemes t03 (kept T3-004) names T3-041, T3-042 and T3-024; five concepts leave nearby art alone and rewrite the quote so as not to overlap it (c0137, c0151, c0157, c0164, c0399). heroesofthestorm t01 (kept T3-001) names T3-017, T3-095 and T3-048; about a dozen concepts ask whether Blizzard made any April Fools that year, guess which release is its joke and praise a fan creator's prank. heroesofthestorm t02 (kept T3-038) names T3-033, T3-041 and T3-020; c0040, a carrying code, chooses a patch of blue in a low-activity area for the logo. lsu t01 (kept T3-020) names T3-022, T3-061 and T3-042; c0072, a carrying code, rejects a larger design beside Brazil because the room lacks the manpower. TheFarLeftSide t01 (kept T3-069) names T3-042, T3-171 and T3-076; six concepts stop or refuse the room's own attacks, the last warning that a Stalin portrait would provoke Ukraine (c0373, c0398, c0566, c0605, c0618, c0622). TheFarLeftSide t05 (kept T3-010) names T3-170, T3-052, T3-080 and T3-087; three concepts call the Ukrainian flag beside the room unnecessary nationalism and dispute that it was a fascist flag (c0400, c0548, c0595), and three ask who made a green line, a Kurdish-flag vandalism and black pixels from the sub (c0381, c0422, c0497). TheFarLeftSide t11 (kept T3-073) names T3-157, T3-154 and T3-009; five concepts present the final image with pride (c0632, c0633, c0635, c0636, c0643). The bag files are `out/_analysis/b1d07_bags_*.txt`. `tier_history.jsonl` rose from 109 to 123 lines: 12 from the bag writer and 2 from `b1d_tier_unplace_fill.py`, for T3-041 (heroesofthestorm t02) and T3-042 (TheFarLeftSide t01), both of which prequelmemes t03 had already dropped in this leg. T3-188 still holds 7 placed themes in 7 rooms.

The second pass stops here. `saturation.py pass2 --stage B1` reports all 108 chosen rooms read. It reports the run since this pass's last new kind as 108 rooms and 148.1 average rooms. Marker 1's empty run is 78 rooms and 72.1 average rooms, and the floor is 30 rooms. Both conditions hold. In seven stretches the second pass minted no kind, split none and merged none. The last new kind is still T3-197 (heeding the creator's wishes), from the first pass at parahumans t08. B1e follows.

The B1c gates met in this stretch need B1e work, not new kinds. sakuragakuin t11 is one more case for T3-117 taking registering the end and hoping it returns. DevonUK t01 needs the T3-065 label change already listed. DevonUK t02 stays in T3-044. For B1e, the T3-044/T3-082 discriminator should ask whose eyes find the mark. Outsiders led to the sub by the mark go to T3-044. Members finding their own room's mark already placed go to T3-082. hellointernet t12 is the other case.

The open B1c idea 213, gathering lone placers together, was met at its trigger, rainbowgrid t02. It is not minted. t02 holds T3-002 with T3-126 and T3-090, and each part of the doing is held by one of them. What differs is the room's condition: placers repeated the grid before any group existed. A kind for it would split T3-002 by how organised the people called in already were, which is splitting by degree. With homestuck t11 (stretch 6, in T3-069), the idea is met in two rooms and carried by existing kinds in both. For B1e, T3-002's gate should include calls to placers who are not yet a group, and T3-126's gate should include saying that no one can speak for the placers.

The T3-188 doing appeared again as single concepts: prequelmemes c0292, heroesofthestorm c0190, reddevils c0212 and rainbowgrid c0003. In israel, c0153, a carrying code, has the room's Discord moderator say the room does not condone attacks on Palestine made in its members' name; T3-188 is missing from t04's bag. More cases bear on the gate question, whether an outside voice's denial counts. In ucf, a member told NEU that the accounts crossing its border were not those building the logo, then allowed that an overnight script may have done it (c0066, c0068, c0069). In rocketbeans, an attacking German streamer called off his viewers (c0087). In thesilphroad, a member of r/TheBlueCorner said most of that room wanted to keep its corner rather than expand (c0723). In TheFarLeftSide, members doubted that the Kurdish-flag vandalism was the room's and asked whether black pixels from the sub were part of a plan (c0422, c0497); both are placed as tracing (T3-087).

Kinds missing from existing bags are recorded in the room notes. Seven of them, in five themes, have a carrying code of the A1 note behind them: prequelmemes t08 (T3-076, c0426 and c0435), heroesofthestorm t10 (T3-040, c0102; T3-076, c0171), israel t04 (T3-188, c0153), thesilphroad t03 (T3-042, c0070; T3-024, c0692) and TheFarLeftSide t06 (T3-080, c0414). Others rest on groups of concepts: israel t04 (T3-130, T3-068), reddevils t16 (T3-072), heroesofthestorm t11 (T3-070, T3-157), thesilphroad t01 (T3-147), TheFarLeftSide t04 (T3-086, T3-146, T3-081) and TheFarLeftSide t06 (T3-149, T3-151, T3-011, T3-194).

## How the second pass stopped (written at B1e, 2026-10-11)

The second pass stopped on its run of rooms that added no new third-order theme. That run is 108 rooms and 148.1 average rooms, against marker 1's empty run of 78 rooms and 72.1 average rooms, with a floor of 30 rooms. All 108 chosen rooms were read. Each of the seven stretches (B1d-01 to B1d-07) added no new kind, split none and merged none. The rule in force before 2026-10-07 asked for two stretches of at least twenty rooms each with nothing new. Only stretches 1 and 2 reach twenty rooms (21 and 24, in the stretch table above), and both added no new kind, so they are the pair that rule asked for. The count was not still climbing at the list's end. The last new kind is T3-197, minted in the first pass at room 661 of 705.
