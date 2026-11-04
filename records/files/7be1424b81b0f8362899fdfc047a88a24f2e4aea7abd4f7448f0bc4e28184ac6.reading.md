# Notes, stage D2 (the return: the check leg)

The labelers and the verdict readers returned against the model frozen at pass 15 (e15f96470271763d9913e79ed8e332c164a1f176106eefacfe8ffac8e1b3fecd). `ingest.py D` compiled the ledger and the verdicts at 08:53 UTC on 16 October. I adjudicate nothing here, edit no return, and run no labeler or reader. QD1-001 (J: an element may sit in two or more dimensions) was settled at D1a, and nothing here rests on it.

Scripts, all read-only over the returns: `_analysis/d2_ingest.py` (§1), `_analysis/d2_verdicts.py` (§2; the split rooms in `_analysis/d2_verdict_rooms.json`), `_analysis/d2_sample.py` (§3; the draw in `_analysis/d2_sample.json`). The ledger was read by count only.

## 1. What ingest did

**Rooms.** 705 rooms returned and were accepted. None was rejected, none is unreturned, and `RUN.json` says none was reissued. The counts agree across `ingest-D.md`, `RUN.json` (`D2`: accepted 705, reissued 0, unreturned 0), `DROPS/D/DONE` (returned 705, unreturned 0), `UNRETURNED.tsv` (header only) and the ledger (705 rooms).

**Reissues.** `ingest.py` counts a room as reissued when its `run.json` records more than one attempt. Every room records one. The handler's recap says 378 rooms needed one to four repairs of attempt 1 in the same session. Those repairs, and the rules they fixed, are in no file this stage may read.

**Lines.** 42,243 lines. Per room: min 21, p10 52, quartiles 57, 60 and 64, p90 68, max 91.

| op | lines | share | rooms holding it |
|---|---|---|---|
| instantiate | 17,648 | 41.8% | 705 |
| absent | 14,675 | 34.7% | 705 |
| restrict | 4,406 | 10.4% | 633 |
| add-step | 1,889 | 4.5% | 654 |
| add-condition | 1,408 | 3.3% | 511 |
| propose | 1,362 | 3.2% | 543 |
| link | 844 | 2.0% | 484 |
| contradict | 11 | 0.03% | 11 |

- **By kind, as ingest stamps it:** specification 32,323 (76.5%), correction 4,417 (10.5%), elaboration 4,141 (9.8%), proposal 1,362 (3.2%).
- **The absent lines split by evidence.** Only 67 of 14,675 are evidenced: observed-absent 36, not-needed 31. The rest mark limits of the evidence: unobserved 7,806 and not-testable 6,802. The schema says those support neither specification nor correction, but ingest stamps every absent line as specification. Read without the split, the kind counts overstate what the rooms specify by 14,608 lines. A room holds between 1 and 50 absent lines, median 19.
- **Contradict** (11 lines, one room each): P13 5, P10 3, A10 1, A04 1, A07 1.
- **Propose:** 1,362 lines in 543 rooms. None names an element.

**Flagged lines.** Ingest rejects a room whole when any line fails rules 1 to 4 or 6. It keeps a line that fails portability (rule 5) with `portable: false`. So portability is the only flag left in the ledger, and it is the rule that flagged most lines: 763 lines (1.81%) in 356 rooms. By op: instantiate 484, absent 185, restrict 31, propose 19, add-step 17, add-condition 15, link 10, contradict 2. 169 of them name the room itself.

**None rooms.** 0. Every room returned lines.

**Unplaced source themes** (the lines D3 may mint from). 134 of 27,571 sourced lines (0.5%) have a source theme placed nowhere. They sit in 98 rooms: propose 61, instantiate 32, restrict 19, add-step 16, add-condition 5, link 1. Every source is a second-order theme.

**Candidates and tentative entries.** The labelers answer the five candidates often, as `MODEL.md` allows. Rooms with at least one line on the entry other than absent:

| entry | status | rooms | instantiate lines |
|---|---|---|---|
| P06 | candidate | 564 | 600 |
| K04 | candidate | 530 | 584 |
| R02 | candidate | 500 | 493 |
| P19 | candidate | 240 | 217 |
| K03 | candidate | 124 | 118 |
| P22 | tentative | 191 | 158 |
| P21 | tentative | 128 | 80 |
| A21 | tentative | 101 | 37 |

D3 rules on these. I report the counts only.

**The labelers.** All 705 `run.json` copies record `gpt-6.1-sol`, resumed with `gpt-5.6-sol`, one attempt. Every line is `origin: labeler`, `decision: pending`, at one model version.

## 2. The verdicts

**The fleet.**
- **Model:** `deepseek/deepseek-v4.1-flash`, verified, on the gateway route at medium effort; two readers per room, reissue limit 2.
- **Attempts:** 1,442. 1,410 were valid and 32 invalid; among the invalid, 24 lacked `served` and 6 lacked the end marker. Each invalid attempt was reissued, and none was exhausted. The fleet cost USD 13.03.
- **`verdicts-D.jsonl`:** one line per room, 705 lines, with two reader lines each (r1 686, r2 693, 31 from reissued readers) and the labeler's grade beside them.

**Reader verdicts** (1,410): composes-with-residue 927 (65.7%), composes 432 (30.6%), cannot-tell 49 (3.5%), does-not-compose 2 (0.1%).

**Room verdicts.** The two readers agree in 542 rooms:
- composes-with-residue: 387;
- composes: 140;
- cannot-tell: 14;
- does-not-compose: 1 (picturegame).

They differ in 163 rooms, **a disagreement rate of 23.1%**. By pair:
- composes against composes-with-residue: 142 rooms (20.1% of all rooms);
- cannot-tell against composes-with-residue: 11 (1.6%);
- cannot-tell against composes: 10 (1.4%).

No split involves does-not-compose. Within each value, the share of rooms where one reader chose it and the other did too is: with-residue 72% (387 of 540), composes 48% (140 of 292), cannot-tell 40% (14 of 35).

The disagreement rate bounds whether the written criterion decides a room, not whether the model is right (FLEET §2). Most splits fall on one line: whether a room's unused concepts carry organizing the model lacks. The 163 split rooms are listed at the end of these notes for D3, which rules on each with the criterion in front of it.

**Cannot-tell, by threshold.** 49 reader lines: coded-share 39, off-platform 10, both 0. The lines carry no counts, so I checked each against the room's figures in `rooms.jsonl`, which each packet stated, and against `prior.md` §8. All 39 coded-share lines fall in rooms below the concept floor of 10. All 10 off-platform lines fall in rooms past the off-platform threshold. **The numbers support every cannot-tell line, so none goes to D3 as unsupported.** The thresholds are review prompts, not rules, so the converse also holds: readers judged most rooms below the floor or past the threshold.
- **The 42 rooms below the floor:** composes 14, cannot-tell 13, split 13, with-residue 2.
- **The 68 rooms past the threshold:** with-residue 47, split 16, composes 4, cannot-tell 1.

**Residue.** A with-residue reader line names a median of four themes or concepts as residue.

**The labeler's grade beside the verdict.** Every one of the 705 `model-D.md` files grades composes-with-residue, and every one says `local_status: unresolved`. The cross-table has one row:

| labeler grade | composes | composes-with-residue | does-not-compose | cannot-tell | split |
|---|---|---|---|---|---|
| composes-with-residue | 140 | 387 | 1 | 14 | 163 |

By reader line, the row reads: composes-with-residue 927, composes 432, cannot-tell 49, does-not-compose 2. The grade does not vary, so it cannot be set against the verdict. It sits beside the verdict and never replaces it. The cause goes to the handback.

**The return lines.**
- **`served`:** each packet states a value for the reader to copy. 1,409 of 1,410 lines copy it exactly; one (ducks, r1) drops two characters.
- **`sub`:** 225 reader lines write the room's name another way. 185 add `r/`, 16 change the case, and 24 write another name, such as a sister sub or the words one community. Ingest takes the room from the dispatch folder, so no verdict changed rooms.
- **Extra field:** three lines carry an extra field, `agent` (daftpunk, kuwait, ssbpm).

**The story-miss rooms** (C2's last story told these 19 with a residue). By room verdict:
- **composes-with-residue (14):** bih, catalunya, epublica, greenlattice, orderofthebluecorner, purplecorner, scp, sweden, thebluecorner, totallynotrobots, parahumans, TheAdventuresofTintin, shishamo, luciomains;
- **composes (4):** placeDE, starcitizen, texans, hunterxhunter;
- **split (1):** smashbros.

D3 counts how they fared. I compare them with no prediction here.

## 3. Ten room models, drawn by seed

**The rule** (logged before the draw):
- **Seed:** 20261016, with `random.Random(seed).sample` over each stratum's sorted rooms.
- **Strata:** the room verdict: composes, with-residue, does-not-compose and cannot-tell when both readers agree, and split when they differ.
- **Allocation:** two rooms per stratum, or all of a smaller one; the remainder goes to the largest.

The strata held 140, 387, 1, 14 and 163 rooms. The draw: cannot-tell Lugarix and wario; composes uva and signal; composes-with-residue quebec, flashtv and minnesotavikings; does-not-compose picturegame; split aggies and thetreesnetwork. I checked each file by script and then read it whole.

**What all ten share.**
- **Form:** each file has a section per dimension (D01 to D08) and names all 51 elements and arrows, either cited or marked `[absent <id>]` with its evidence state.
- **Citations:** every paragraph and bullet before Local exceptions carries a concept citation, and every citation is one of the room's own codes. Every element the room's ledger lines adapt is named in the file.
- **Grade:** every file ends with `local_status: unresolved` and the grade composes-with-residue. The grade's sentence names a few of the ledger's elements. In the thinner files it reads as a formula: the account explains what was visible, and the rest is unresolved.
- **The model's terms:** the prose reads as the room's organizing in the model's words, not as a summary of the model. In the rich rooms it gives forest transitions with their minutes, and it changes an element only where the room's turns show a different order.

**Wario** (cannot-tell; one concept). A single title shows a call and a design (P01, P02, R01, P09). Every other entry is unobserved or not testable, with the reason. The labeler restricts P09: the attack reading needs the target shown as another party's work.

**Lugarix** (cannot-tell). Announcement titles and one approving reply carry P11. The labeler challenges a placement, because the in-joke theme claims a history the quote does not show, and keeps the joke as an add-step inside P11. It also settles a P15 boundary locally: approving an announcement is not answering a call.

**Signal** (composes). Call, building, guidance, design critique and credit (P01, P03, P04, P02, P11, P12). The one `[new: …]`, a member's reply to a bot, is not organizing. Some D08 lines sit under Local exceptions.

**Uva** (composes).
- **The order:** a rich room, read turn by turn. The labeler restricts A11, because the template was posted before the disagreement ended. It restricts A05, because the agreement recognised an intention already held: "I had no plans to continue them below that border. maybe others did" (uva/c0021). It also restricts A21.
- **Additions:** a step inside P03, finding a second mark. It uses P06, R02 and K04 as candidates.
- **Grade:** the readers say composes; the labeler grades with-residue on these local changes.

**Quebec** (composes-with-residue).
- **Restrictions:** A11 (scripts defended a design the room had dropped), A12 (a bare refusal), A05 (restraint for a memorial) and A09.
- **C01 locally:** a vote and a declared strategy that the room did not obey throughout.
- **`[new: …]`:** of its six markers, two are practices (moving deliberation into live chat; returning political questions to the room). Two are residue tags.

**Flashtv** (composes-with-residue). Loss and restart, restraint toward kindred fans, and a host's closure prank. The labeler restricts A11, A01, A02, A10 and A05. Of its eight `[new: …]` markers, three are organizing (reusing pixels while relocating; rebuilding after a move; learning a neighbour's design to stop a mistaken repair). Two are not (summoning a conversational bot; sympathy in a joke thread).

**Minnesotavikings** (composes-with-residue).
- **The tentative entries:** it instantiates P21 in a bounded form, from "We can't force people to do anything" (minnesotavikings/c0254), and A21.
- **C01 locally:** a division of work and a vote on the bot.
- **Restrictions:** A11 and A05.
- **`[new: …]`:** five practices, all of them organizing, such as decisions relayed through chat to the member who sets the script.
- **Its own case account:** it corrects the attribution of one complaint there.

**Picturegame** (does-not-compose; the only such room). A guessing-game sub whose one canvas link is a proposed emoji. The labeler keeps the room inside the model's terms: K01 (an April Fools sound round) and P13 (the proposal), with every canvas element unobserved. Its `[new: carrying on ordinary sub talk]` repeats T3-017, which the vocabulary holds. The readers judged that the room's organizing is not canvas organizing; the labeler graded with-residue.

**Aggies** (split).
- **Restrictions:** the labeler folds the start and the call into one act (A02), and restricts A11 and A08 (a screenshot requested before completion).
- **Conditions added:** on P14 (an honor code against scripts), and on A13 and A19 (help bought from former attackers).
- **C01 locally:** an organiser decides and defers.
- **Candidates:** K03, K04 and R02.

**Thetreesnetwork** (split). The labeler instantiates the candidates P06 (tracing who placed a pixel) and K04 (an insider's membership claim), and restricts P06's reading that the placer meant well. It keeps a personal inscription and a thank-you to the host as `[new: …]`, and conditions P15 on what a bare reply approves.

**Across the sample.**
- **Recurring changes:** five of the ten labelers restrict A11 (a posted template did not settle the design). Four fold the start and the call into one act (A02). Four make restraint (A05) depend on something other than an agreement.
- **Candidates and tentative entries:** they come back as instantiated lines. The labelers name the candidates as candidates.
- **`[new: …]`:** used for practices no element covers, but also for conduct that is not organizing, as a residue tag, and once for a theme the vocabulary holds.

These are D3's to rule on. I report them as the sample showed them.

## 4. Verbal before numeric

I revisited no verdict and no line because of a count. Four facts stand as facts, and D3 judges them against `prior.md`:
- composes-with-residue dominates the verdicts;
- contradict is rare (11 lines);
- the labeler's grade never varies;
- absent lines are a third of the ledger, mostly marking limits of the evidence.

Neither the many repairs nor the absent lines establish failure or success.

## Defects sent to the handback

1. **The labeler's grade does not vary** (task template and return specification).
2. **Ingest stamps every absent line as specification,** whatever its evidence state.
3. **The 378 same-session repairs appear in no file.** `RUN.json` counts 0 reissued.
4. **The verdict return line:** `served` records copying, `sub` is unreliable, and the line carries no count.
5. **`[new: …]` is used for more than organizing** (minor).
6. **Eight ledger lines name a dimension as their element outside `link`** (QD2-001, answered). In 121 ledger lines the element is a dimension id; 113 are `link`, which SCHEMA §3 allows. The other 8 are not:
   - restrict D02: 4chan-013, SquareSpiral-014;
   - add-condition D02: borussiadortmund-013;
   - add-condition D01: cowchop-030, spain-058, torontoraptors-009;
   - restrict D01: ucf-004;
   - add-step D02: vermont-011.

   `ingest.py` accepts a dimension for any op, while `validate.py D2` accepts one only for `link`. So the first close-check failed on these 8 lines alone. I edited no line.

   **J's answer (option 1):** the check now accepts a dimension as the element of restrict, add-condition and add-step as well as link. D3 rules on the 8 lines as they stand.

## The split rooms, for D3 (163; generated from `_analysis/d2_verdict_rooms.json`)

<!-- split rooms, generated -->

**composes against composes-with-residue** (142): 49ers, achievement_hunter, afip, aggies, AmericanFlaginPlace, auburn, australia, bdsm, bindingofisaac, bisexual, blackmirror, bostonbruins, btc, buffalowizards, bulgaria, cgpgrey, chile, Clannad, clashroyale, cmu, coldplay, criticalrole, czech, danganronpa, DestinyTheGame, detroitlions, drawhelix, drugs, drumcorps, dwarffortress, eagles, earthbound, edboxes, edmontonoilers, eesti, egypt, ElderScrolls, elitedangerous, england, falcons, Fez, FlaggyFlag, floridagators, foxes, fxKorea, gatech, geometrydash, germany, giantbomb, globaloffensive, GranColombia, gravityfalls, guatemala, GuildWars2, h3h3productions, hawks, heroesofthestorm, hoodr, hyperlightdrifter, ice_poseidon, iceland, india, jerma985, kamenrider, katawashoujo, kirby, kpop, kurdistan, latvia, lifeisstrange, lofihiphop, magictcg, mamamoo, ManningPlace, marvel, mexico, miamidolphins, mizzou, MMA, MonkeyIsland, monstercat, mordhau, morrowind, muse, mylittlepony, mysterydungeon, nascar, necrodancer, neu, nin, notredame, ohio, patriots, pepe, PinkVomitMonster, pitt, placehfarts, placetardis, pokemon, poland, polandball, popheads, PORTUGALCARALHO, puzzleanddragons, qotsa, re_zero, redpandas, roosterteeth, rush, rust, rutgers, sakuragakuin, seahawks, snsd, sooners, spain, spongebob, ss13, ssbpm, starcraft, strangerthings, telegram, teslamotors, texastech, thailand, thenetherlands, thepointing, thesimpsons, thetreesnetwork, tinytardis, TsundereSharks, twitch, udub, ukraine, uofm, UPenn, uwaterloo, vim, weezer, wholesomememes, yuyuyu, zelda.

**cannot-tell against composes-with-residue** (11): azores, crusaderkings, de, paladins, reddevils, serbia, smashbros, THE_R, TransFlagPlace, trees, UNLincoln.

**cannot-tell against composes** (10): austriahungary, bannedfromanime_irl, Bravenewbies, littlebusters, NovaScotia, oltp, polyamory, Redox, tenma, TheID.

Unsupported cannot-tell lines: 0.
