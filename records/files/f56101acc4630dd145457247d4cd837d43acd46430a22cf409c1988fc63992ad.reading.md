# Survival per branch

Stage D5, leg D5b, 2026-10-26 UTC. This file reports, for each of the 35 branches, when the members' coordinating ended, how much of it came after the close, and what the members' own records say became of their work. It reports these from the record first. The canvas comes afterwards, in section 5, with the direction of its bias named (rule 7). Section 6 checks the dated changes in the branch narratives against prior.md's brackets and the members' placements by hour. Nothing here is a score, and a branch's size is not its importance.

## 1. The three measures, from the record

Stage A1 wrote three fields for every room (`organizing_end-A1.jsonl`), under the rules in prior.md section 5.

- **organizing_end_hour.** The hour of the room's last coordinating turn in the forest. It dates the last observed coordinating act. It does not show that all organizing stopped then, and work off the platform is not in it.
- **The aftermath share.** The share of the room's coded turns after hour 73 that coordinate rather than recount. The branch figure is the mean over members, as in `branches-D5.jsonl`.
- **work_remained.** The room's own last word on what became of its work: kept, lost or silent. Silence is an unknown outcome, and it counts.

The clock: placement was disabled at hour 73, and the last 24 hours of the 97-hour window are aftermath (prior.md section 4). Of the 476 rooms in a branch, 53 ended their coordinating before hour 64, 303 between hour 64 and the close, and 120 at hour 73 or later. For most rooms, then, the close is what the record shows stopping the coordinating. Over the 705 rooms the median end is hour 72.02; over the 476 in a branch it is 72.20.

## 2. work_remained, read again

prior.md section 5 measured the field's error before the scheme: right in 25 of 34 rooms. At D5a-33 to D5a-35 I found lines cited for the field that were about another room, that came before the close, or that said the opposite (defects lines 95, 97 and 99). So at this leg I read the field again for every room in a branch, by a rule I logged before the reading.

**The rule.** For each room I read the code or codes the field cites, with their hour and words, and gave one reading. *Stood*: a line at hour 72 or later says the room's own work, or its main work, was there at or after the close. *Gone*: a line at hour 72 or later says it was destroyed, missing or not kept at the end. *During*: a line before hour 72 reports the work finished, standing or lost during the event, so it cannot say what stood at the close. *Other*: the line does not concern the room's own work (another room's work, a post title, a remark). *Unclear*: the line cannot be read either way. *Silent*: no code. Where one line says one work stood and another was lost, the room's main work decides, and the reading is noted as mixed. While reading I adopted four conventions and applied them to all five pages: a celebration posted after the close counts as stood; an edit posted after the close is read by its content; hour 72 is applied strictly; a final canvas or final image posted without naming the room's work is unclear. Three readings were corrected after the files were written (r/detroitlions, r/placetardis and r/liverpoolfc, each to unclear), and the corrections are logged. The pages I read showed the field beside each line. Each reading is of the line's words, and the agreement with the field was computed afterwards (`out/_analysis/d5b_survival.py`).

**What the reading shows.** The field against the reading, for the 476 rooms:

| the field says | stood | gone | during | other | unclear | silent | all |
|---|---|---|---|---|---|---|---|
| kept | 146 | 3 | 61 | 20 | 23 | 0 | 253 |
| lost | 3 | 40 | 54 | 43 | 21 | 0 | 161 |
| silent | 0 | 0 | 0 | 0 | 0 | 62 | 62 |

The field and the reading agree in 248 of 476 rooms. Where the field says kept, a line after the close says the work stood in 146 of 253 rooms. Where it says lost, a line after the close says the work was gone in 40 of 161. In 115 rooms the cited line came before the close, and in 63 it concerned something other than the room's own work. Read again, the rooms' own words after the close say the work stood in 149 rooms and was gone in 43. The field over-reads both outcomes, and it over-reads loss more.

I report both, per branch, in section 3. The re-reading changes no ledger: `branches-D5.jsonl` keeps work_remained as the field gives it. The account's paragraph "Which keep the work alive" rests on the field (kept 347, lost 218, silent 140 of 705). Its shares are shares of a field that over-reads outcomes, so they are a question for the account at stage D6 (`notes-D5.md`, `defects.jsonl`).

## 3. Per branch, the record

Each row gives the branch's members; a room in two branches counts in both. "In a branch" counts each of the 476 rooms once.

| branch | n | median organizing_end_hour | ended before 64 | 64 to 73 | 73 or later | aftermath share (mean) | rooms coordinating after 73 | kept | lost | silent |
|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 103 | 71.98 | 13 | 68 | 22 | 0.0126 | 22 | 51 | 42 | 10 |
| F02 | 33 | 72.02 | 2 | 22 | 9 | 0.0167 | 9 | 16 | 14 | 3 |
| F03 | 18 | 71.21 | 3 | 12 | 3 | 0.0105 | 3 | 9 | 6 | 3 |
| F04 | 13 | 71.98 | 4 | 6 | 3 | 0.0149 | 3 | 8 | 5 | 0 |
| F05 | 12 | 72.09 | 2 | 9 | 1 | 0.0023 | 1 | 6 | 4 | 2 |
| F06 | 8 | 71.05 | 2 | 5 | 1 | 0.0019 | 1 | 3 | 3 | 2 |
| F07 | 59 | 72.35 | 5 | 39 | 15 | 0.0205 | 13 | 33 | 22 | 4 |
| F08 | 50 | 72.75 | 4 | 33 | 13 | 0.0201 | 13 | 27 | 17 | 6 |
| F09 | 54 | 72.09 | 5 | 38 | 11 | 0.0157 | 11 | 35 | 17 | 2 |
| F10 | 38 | 71.93 | 5 | 29 | 4 | 0.0145 | 4 | 18 | 11 | 9 |
| F11 | 43 | 73.48 | 1 | 19 | 23 | 0.0378 | 23 | 26 | 14 | 3 |
| F12 | 22 | 80.76 | 1 | 7 | 14 | 0.0548 | 14 | 12 | 8 | 2 |
| F13 | 9 | 74.88 | 0 | 4 | 5 | 0.0314 | 5 | 8 | 1 | 0 |
| F14 | 7 | 70.59 | 0 | 5 | 2 | 0.0090 | 2 | 4 | 3 | 0 |
| F15 | 42 | 72.08 | 4 | 30 | 8 | 0.0176 | 8 | 21 | 14 | 7 |
| F16 | 35 | 72.06 | 3 | 24 | 8 | 0.0134 | 8 | 17 | 11 | 7 |
| F17 | 36 | 72.20 | 2 | 27 | 7 | 0.0189 | 7 | 18 | 14 | 4 |
| F18 | 15 | 71.49 | 1 | 14 | 0 | 0.0000 | 0 | 9 | 6 | 0 |
| F19 | 14 | 72.80 | 0 | 10 | 4 | 0.0202 | 4 | 6 | 6 | 2 |
| F20 | 10 | 72.60 | 2 | 6 | 2 | 0.0063 | 2 | 5 | 3 | 2 |
| F21 | 32 | 72.07 | 4 | 22 | 6 | 0.0109 | 6 | 14 | 13 | 5 |
| F22 | 30 | 72.14 | 4 | 20 | 6 | 0.0065 | 6 | 14 | 11 | 5 |
| F23 | 30 | 80.66 | 0 | 6 | 24 | 0.0702 | 24 | 17 | 12 | 1 |
| F24 | 27 | 72.16 | 2 | 19 | 6 | 0.0182 | 5 | 17 | 9 | 1 |
| F25 | 27 | 72.91 | 3 | 12 | 12 | 0.0271 | 12 | 14 | 11 | 2 |
| F26 | 23 | 72.22 | 1 | 16 | 6 | 0.0373 | 6 | 11 | 10 | 2 |
| F27 | 27 | 72.76 | 2 | 17 | 8 | 0.0359 | 8 | 14 | 10 | 3 |
| F28 | 22 | 71.69 | 0 | 17 | 5 | 0.0171 | 5 | 11 | 7 | 4 |
| F29 | 25 | 72.99 | 0 | 13 | 12 | 0.0389 | 12 | 16 | 7 | 2 |
| F30 | 24 | 72.27 | 2 | 16 | 6 | 0.0161 | 6 | 8 | 9 | 7 |
| F31 | 22 | 72.22 | 0 | 18 | 4 | 0.0094 | 4 | 13 | 9 | 0 |
| F32 | 21 | 72.30 | 2 | 14 | 5 | 0.0076 | 4 | 14 | 5 | 2 |
| F33 | 23 | 70.59 | 4 | 15 | 4 | 0.0268 | 4 | 10 | 9 | 4 |
| F34 | 22 | 72.31 | 2 | 15 | 5 | 0.0269 | 5 | 14 | 6 | 2 |
| F35 | 18 | 71.51 | 5 | 9 | 4 | 0.0280 | 4 | 9 | 6 | 3 |
| in a branch | 476 | 72.20 | 53 | 303 | 120 | 0.0213 | 117 | 253 | 161 | 62 |
| population | 705 | 72.02 | 120 | 427 | 149 | 0.0200 | 146 | 347 | 218 | 140 |

The population row counts 696 end hours: nine rooms have no coordinating turn under the A1 rule (prior.md section 3), and none of them is in a branch.

The field beside the reading, per branch:

| branch | n | kept | lost | silent | stood | gone | during | other | unclear | silent (re-read) | field agrees |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 103 | 51 | 42 | 10 | 26 | 17 | 24 | 13 | 13 | 10 | 51 |
| F02 | 33 | 16 | 14 | 3 | 11 | 8 | 7 | 3 | 1 | 3 | 22 |
| F03 | 18 | 9 | 6 | 3 | 3 | 4 | 3 | 4 | 1 | 3 | 8 |
| F04 | 13 | 8 | 5 | 0 | 6 | 2 | 2 | 1 | 2 | 0 | 8 |
| F05 | 12 | 6 | 4 | 2 | 2 | 1 | 4 | 3 | 0 | 2 | 5 |
| F06 | 8 | 3 | 3 | 2 | 1 | 0 | 0 | 2 | 3 | 2 | 3 |
| F07 | 59 | 33 | 22 | 4 | 20 | 4 | 16 | 6 | 9 | 4 | 27 |
| F08 | 50 | 27 | 17 | 6 | 17 | 2 | 7 | 12 | 6 | 6 | 25 |
| F09 | 54 | 35 | 17 | 2 | 23 | 4 | 13 | 6 | 6 | 2 | 27 |
| F10 | 38 | 18 | 11 | 9 | 9 | 3 | 12 | 3 | 2 | 9 | 21 |
| F11 | 43 | 26 | 14 | 3 | 16 | 5 | 6 | 6 | 7 | 3 | 24 |
| F12 | 22 | 12 | 8 | 2 | 8 | 5 | 2 | 0 | 5 | 2 | 15 |
| F13 | 9 | 8 | 1 | 0 | 5 | 0 | 2 | 2 | 0 | 0 | 5 |
| F14 | 7 | 4 | 3 | 0 | 2 | 0 | 1 | 2 | 2 | 0 | 2 |
| F15 | 42 | 21 | 14 | 7 | 15 | 4 | 10 | 4 | 2 | 7 | 26 |
| F16 | 35 | 17 | 11 | 7 | 10 | 3 | 8 | 6 | 1 | 7 | 19 |
| F17 | 36 | 18 | 14 | 4 | 11 | 6 | 10 | 4 | 1 | 4 | 20 |
| F18 | 15 | 9 | 6 | 0 | 5 | 4 | 4 | 1 | 1 | 0 | 8 |
| F19 | 14 | 6 | 6 | 2 | 4 | 2 | 4 | 2 | 0 | 2 | 8 |
| F20 | 10 | 5 | 3 | 2 | 1 | 2 | 1 | 3 | 1 | 2 | 5 |
| F21 | 32 | 14 | 13 | 5 | 7 | 4 | 11 | 1 | 4 | 5 | 16 |
| F22 | 30 | 14 | 11 | 5 | 7 | 4 | 9 | 3 | 2 | 5 | 15 |
| F23 | 30 | 17 | 12 | 1 | 12 | 4 | 7 | 4 | 2 | 1 | 17 |
| F24 | 27 | 17 | 9 | 1 | 15 | 1 | 5 | 3 | 2 | 1 | 17 |
| F25 | 27 | 14 | 11 | 2 | 9 | 3 | 7 | 5 | 1 | 2 | 14 |
| F26 | 23 | 11 | 10 | 2 | 5 | 1 | 9 | 5 | 1 | 2 | 8 |
| F27 | 27 | 14 | 10 | 3 | 12 | 2 | 2 | 6 | 2 | 3 | 16 |
| F28 | 22 | 11 | 7 | 4 | 8 | 0 | 6 | 2 | 2 | 4 | 11 |
| F29 | 25 | 16 | 7 | 2 | 10 | 5 | 4 | 1 | 3 | 2 | 16 |
| F30 | 24 | 8 | 9 | 7 | 5 | 5 | 1 | 4 | 2 | 7 | 15 |
| F31 | 22 | 13 | 9 | 0 | 7 | 4 | 2 | 3 | 6 | 0 | 11 |
| F32 | 21 | 14 | 5 | 2 | 9 | 1 | 7 | 2 | 0 | 2 | 12 |
| F33 | 23 | 10 | 9 | 4 | 6 | 0 | 7 | 3 | 3 | 4 | 10 |
| F34 | 22 | 14 | 6 | 2 | 5 | 1 | 7 | 5 | 2 | 2 | 8 |
| F35 | 18 | 9 | 6 | 3 | 6 | 2 | 5 | 1 | 1 | 3 | 10 |
| in a branch | 476 | 253 | 161 | 62 | 149 | 43 | 115 | 63 | 44 | 62 | 248 |

Four branches end late, and each is a branch whose key is carrying on: F12 (median hour 80.76; 14 of 22 members coordinated after the close), F23 (80.66; 24 of 30), F13 (74.88) and F11 (73.48; 23 of 43). That they end late restates the cut: the key that put them together is about work after the close. The earliest medians are F14 and F33 (70.59), F06 (71.05) and F03 (71.21). F18 is the only branch in which no member coordinated after the close. In the re-reading, F24 (stood 15, gone 1), F08 (17 and 2), F27 (12 and 2) and F09 (23 and 4) lean most to stood; F03 (3 and 4) and F30 (5 and 5) do not. F26 holds the largest share of members whose cited line came before the close (9 of 23).

## 4. Each branch's ending, in its own terms

For each branch I say what the last coordinating act was and what the members did after the close. The last act is each member's `last_coordinating_code`; the acts after the close are its `aftermath_coordinating_codes`. Both are read through the fourth-order themes their concepts sit under, as a share of the branch's acts against the population's, by the rule of D5a-01's theme script (a concept split evenly over its themes). Across the 705 rooms the last act is most often repair work (0.142 of last acts), then transition (0.119), negotiated order (0.113) and collective representation (0.098). After the close, transition leads (0.526), then collective memory (0.105) and completion ritual (0.078).

The themes, in plain words: *repair work*, fixing and defending the work; *transition*, taking the work or the group to a new place or form; *negotiated order*, terms with neighbours; *collective representation*, the room showing itself as a group; *mobilization*, calls for hands; *workarounds*, extra accounts, scripts and ways around the wait; *completion ritual*, marking the work done; *collective memory*, records and screenshots; *boundary work*, keeping canvas talk in its place in the sub; *frame bridging*, tying the canvas to the sub's other matters; *reciprocity*, help for help; *sensemaking*, asking how things work; *backstage decision-making*, choices made in a chat.

- **F01, the play administered (103).** The last act was most often repair work (0.21 of the branch's last acts, against 0.142). After the close 22 members coordinated, mostly in transition, with boundary work above the population's (0.143 against 0.043): members sent canvas posts to one thread or another sub (r/thenetherlands, r/stardustcrusaders). The play itself, the sub's April Fools frame, had ended with the day; the canvas work ended at the close like any room's.
- **F02, the takeover run as a temporary regime (33).** The last acts spread over transition, repair work and negotiated order near the population's shares. Nine members coordinated after the close, mostly toward later canvases (r/bindingofisaac, r/totallynotrobots, r/naruto), with r/thenetherlands again sending canvas posts elsewhere. The regime ran on the sub's pages, and the branch's narrative does not date its end.
- **F03, the joke tested (18).** The last act was most often repair work (0.25) and, above the population, territoriality (0.139 against 0.056). Three members coordinated after the close: directions to the logo (r/hunterxhunter), a second logo (r/magictcg) and the logo proposed again (r/warframe). The re-reading finds the work gone in 4 members and standing in 3.
- **F04, the licence policed (13).** Three members coordinated after the close, nearly all in transition (0.875): r/bindingofisaac, r/elitedangerous and r/magictcg. The branch's narrative does not date an end to the objections.
- **F05, the styling ended (12).** The last act was most often repair work (0.367). One member coordinated after the close (r/furry_irl, inviting the room to put its slogan on a new canvas). The branch's own ending, ordinary use restored to the sub, concerns the sub's styling, not the canvas, and the narrative does not date it.
- **F06, the joke kept (8).** The last act was most often a workaround (0.25 against 0.046). One member coordinated after the close (r/kanye, a tribute proposed for the sub's banner). These rooms asked that the joke's change last; the record does not say whether it did.
- **F07, the telling clause not shown at the design (59).** The last act was most often repair work (0.24) or collective representation (0.186 against 0.098). After the close 13 members coordinated, mostly in transition (r/factorio and r/croatia toward copies of the canvas), and frame bridging stood above the population's (0.117 against 0.016): r/AyyMD petitioned to restore the canvas so its logo could be fixed, and r/porterrobinson proposed an old logo before noticing the end.
- **F08, machine hands kept on one target (50).** The last act was most often a workaround (0.22 against 0.046): extra accounts, scripts or ways around the wait were the last coordinating act in these rooms. After the close 13 members coordinated, toward later canvases (r/AmericanFlaginPlace, r/loltyler1) and toward records and banners (r/mexico, r/bakchodi). In the re-reading the work stood in 17 members and was gone in 2.
- **F09, the move returns to building (54).** The last act was most often repair work (0.233). After the close 11 members coordinated, mostly in transition and, above the population, mobilization (0.125 against 0.02): a new letter on another site (r/calgaryflames), another spiral (r/SquareSpiral), a logo defended on a successor canvas (r/twice). The branch's sequence, moving and building again, ran once more on new canvases in these rooms. The re-reading finds the work stood in 23 members and was gone in 4.
- **F10, a deal carried out as work (38).** The last act was most often negotiated order (0.215 against 0.113), and reciprocity stood above the population (0.11 against 0.046): the deals' work went on to the end. Four members coordinated after the close, all in transition (r/fivenightsatfreddys, r/NewMexico, r/phish, r/placetardis). In 12 members the cited line came before the close.
- **F11, carrying on as renewed work (43).** The last act was most often transition (0.444 against 0.119): for these rooms carrying on was the last coordinating act. 23 members coordinated after the close, three quarters of it transition.
- **F12, the spine restarted on another canvas (22).** The last act was transition in 0.591 of members' last acts. 14 members coordinated after the close, and on the copies the spine ran again: r/theblackvoid recruited for new cores on another site until hour 95, r/greenlattice started a gold lattice and moved to a second copy, and r/bindingofisaac called for help when its new drawing was attacked.
- **F13, the work remade in other media (9).** Five members coordinated after the close: the canvas in real life and a building challenge (r/lego), a canvas of the sub's own (r/globaloffensive), a drawing on a second canvas (r/prequelmemes). The re-reading finds no member whose work was gone.
- **F14, the mark adopted as the room's emblem (7).** The last act was most often a workaround (0.286). Two members coordinated after the close; r/cgpgrey proposed stickers that keep the canvas mark. The emblem was the carrying on, and it began before the close.
- **F15, the plan kept current (42).** The last acts spread over negotiated order, transition and repair work near the population's shares. Eight members coordinated after the close, mostly toward later canvases (r/placestart, r/philippines, r/starryknights), and r/ockytop started again on a copy that banned bots.
- **F16, the chat kept open (35).** The last act was most often repair work (0.205), with backstage decision-making above the population (0.086 against 0.034). Eight members coordinated after the close: the finished work proposed as the sub's banner (r/de), a new flag on another canvas (r/TransFlagPlace), and sensemaking above the population (0.182 against 0.017).
- **F17, the marking provisional and contested (36).** The last act was most often negotiated order (0.199) or mobilization (0.139 against 0.065). Seven members coordinated after the close, toward copies (r/AcePlace, r/asexuality, r/fullcommunism) and toward records (r/rocketbeans).
- **F18, success judged while upkeep continues (15).** No member coordinated after the close. The last act was most often mobilization or completion ritual (0.2 each, against 0.065 and 0.034). These rooms judged their success and stopped at the close.
- **F19, credit contested during the work (14).** The last act was collective memory above the population (0.179 against 0.036). Four members coordinated after the close, half of it collective memory: r/rocketbeans sent a request for the drawing's bitmap to an archive, and r/Okami proposed adding a figure after the canvas had closed.
- **F20, the close as news (10).** The last act was most often collective representation (0.2). Two members coordinated after the close (r/Rainbow6 and r/re_zero), mostly in completion ritual. These rooms told late arrivals that placement had ended; the news was their ending.
- **F21, the canvas call not a joke (32).** Six members coordinated after the close, with completion ritual and repair work above the population: r/chile organized to keep its flag, r/patriots called to erase pixels from its work, and r/osu proposed carrying the final image to football games.
- **F22, help conditional on the helper's own work (30).** The last act was more often reciprocity than in the population (0.15 against 0.046). Six members coordinated after the close, mostly toward later canvases (r/gamindustri, r/furry_irl), and r/PlaceNL called to extend its flag after placement had ended.
- **F23, the close scoped to the original canvas (30).** The last act was transition in 0.622 of members' last acts. 24 members coordinated after the close, the most of any branch: a flag on a copy of the canvas (r/catholicism), a memorial, a group elsewhere and new land (r/thebluecorner), a replacement flag and an alliance renewed on another site (r/TheFarLeftSide).
- **F24, machine hands debated (27).** Five members coordinated after the close, with backstage decision-making above the population (0.2 against 0.029): r/placeportalpattern proposed organizing a second version in a chat, and r/frc called to save its logo and then to remake it on another site. The re-reading finds the work stood in 15 members and was gone in 1.
- **F25, carrying on in talk (27).** The last act was transition in 0.451 of last acts. Twelve members coordinated after the close, with completion ritual above the population (0.154 against 0.078): calls back to the canvas after it ended (r/gorillaz), a flag on a copy (r/czech), a logo continued elsewhere (r/starcitizen).
- **F26, the telling clause not shown at the border (23).** Six members coordinated after the close: r/miamidolphins called everyone to pack it up, and r/uiuc asked that the cleaned image go into the sub's theme. In 9 members the cited line came before the close.
- **F27, the telling clause not shown in keeping (27).** Eight members coordinated after the close, with frame bridging above the population (0.179 against 0.016): painters recruited for a copy (r/frankocean), a figure called for after the canvas had finished (r/pokemon), a new site (r/armok).
- **F28, help at the border conditional (22).** The last act was completion ritual above the population (0.114 against 0.034). Five members coordinated after the close: r/quebec called to destroy a neighbour's flag after placement had ended, and r/cloud9 recruited for a flag on a copy.
- **F29, the chat's reach conditional (25).** Twelve members coordinated after the close, with completion ritual above the population (0.243 against 0.078). r/osugame alone holds nine acts after the close: a replacement canvas, a chat with a template, the logo shown atop the sub, and a call to finish the logo on another site. r/EraseThePlace called for the erasing to continue on a copy.
- **F30, the chat seen only through its invitations (24).** Six members coordinated after the close, and transition is below the population's share (0.25 against 0.526); sensemaking and boundary work make up more of it (r/de, r/stardustcrusaders). Seven members are silent on their work.
- **F31, hosting as one-off permission (22).** The last act was most often collective representation (0.254 against 0.098). Four members coordinated after the close, nearly all in transition (r/frankocean, r/seahawks).
- **F32, the marking returns to keeping (21).** The last act was most often repair work (0.183), with reciprocity above the population (0.111 against 0.046). Four members coordinated after the close: r/starvstheforcesofevil recruited spare pixels for a template and started a sign on a copy, and r/ockytop started again on a copy. A last act of repair fits the branch's sequence, in which keeping came after the marking.
- **F33, the plan kept current while the design settles (23).** The last act was most often negotiated order (0.304 against 0.113). Four members coordinated after the close: r/tf2 proposed the canvas design as the sub's logo, and r/india called for help with a flag on an alternative site.
- **F34, the design sized to the hands (22).** The last act was most often repair work (0.238) or collective representation (0.23). Five members coordinated after the close, and three of them proposed smaller or second attempts: a smaller canvas on the sub's own site (r/aeskwadraat), another site (r/aoe2), a smaller copy and a successor canvas (r/farmcarrots).
- **F35, the call made workable (18).** The last act was most often mobilization (0.361 against 0.065): in these rooms the last coordinating act was a call. Four members coordinated after the close, nearly all in transition: another site (r/FlaggyFlag, r/purdue) and a logo on a successor canvas (r/homestuck).

## 5. The canvas, projected afterwards (rule 7)

What the canvas measures, in the contract's words (section 5): "The atlas records what survived the last hour of a 97-hour event. It is not a measure of skill, a large area is not evidence of anything a community intended, and it is what the *drawing* left behind: the instrument has no measure of whether the room went on, whether the arrangements held, whether anyone came back, and a null on the canvas is not a null on §1's last question." And: "Everything you can see is text, and most of the work left no text." Nothing below is a score, and no reading in sections 2 to 4 used the canvas.

**The direction of the bias.** The frame is built from artworks that survived the last hour. A room that organized, placed and was overwritten before the freeze has no row. So the canvas leans toward survival: it cannot show a room that kept nothing, and 475 of the 476 rooms in a branch have an artwork. A room's region is the union of its final artworks. Placements at a site the room left are not counted, so the canvas understates the early work of rooms that moved. Regions overlap, so a contested pixel counts for every room that claims it.

| branch | rooms with artwork | median area (px) | percentile against random groups of its size | members' share of placements in their regions | share of members' placements in hours 8 to 32 | in hours 64 to 73 | peak hour |
|---|---|---|---|---|---|---|---|
| F01 | 103 | 610.5 | 67 | 0.138 | 0.151 | 0.158 | 51 |
| F02 | 33 | 789 | 89 | 0.130 | 0.146 | 0.149 | 52 |
| F03 | 18 | 349 | 9 | 0.146 | 0.099 | 0.190 | 52 |
| F04 | 13 | 957.5 | 89 | 0.181 | 0.142 | 0.149 | 51 |
| F05 | 12 | 706.5 | 68 | 0.169 | 0.186 | 0.165 | 48 |
| F06 | 8 | 1535.25 | 95 | 0.122 | 0.159 | 0.158 | 59 |
| F07 | 59 | 770 | 95 | 0.145 | 0.189 | 0.135 | 53 |
| F08 | 50 | 821.5 | 96 | 0.099 | 0.126 | 0.228 | 71 |
| F09 | 54 | 464.25 | 16 | 0.143 | 0.056 | 0.168 | 52 |
| F10 | 38 | 696 | 78 | 0.114 | 0.130 | 0.181 | 52 |
| F11 | 43 | 985.5 | 99.2 | 0.139 | 0.207 | 0.166 | 71 |
| F12 | 22 | 777 | 82.8 | 0.120 | 0.161 | 0.182 | 71 |
| F13 | 9 | 3202 | 100 | 0.165 | 0.240 | 0.142 | 30 |
| F14 | 7 | 588 | 50.7 | 0.226 | 0.183 | 0.128 | 53 |
| F15 | 42 | 554.75 | 39 | 0.080 | 0.139 | 0.134 | 48 |
| F16 | 35 | 1127.5 | 99.5 | 0.122 | 0.245 | 0.131 | 30 |
| F17 | 36 | 601.25 | 51.9 | 0.095 | 0.160 | 0.166 | 55 |
| F18 | 15 | 462 | 28.9 | 0.128 | 0.151 | 0.178 | 60 |
| F19 | 14 | 563 | 45.4 | 0.058 | 0.137 | 0.206 | 49 |
| F20 | 10 | 839 | 77.5 | 0.101 | 0.044 | 0.178 | 54 |
| F21 | 32 | 406 | 10.8 | 0.173 | 0.160 | 0.183 | 71 |
| F22 | 30 | 360.5 | 6.6 | 0.116 | 0.216 | 0.130 | 52 |
| F23 | 30 | 2096 | 100 | 0.111 | 0.171 | 0.160 | 51 |
| F24 | 27 | 655 | 69.7 | 0.115 | 0.180 | 0.174 | 54 |
| F25 | 27 | 1237.5 | 99.1 | 0.101 | 0.225 | 0.163 | 30 |
| F26 | 23 | 1008 | 95.9 | 0.149 | 0.160 | 0.135 | 52 |
| F27 | 27 | 1389.5 | 99.4 | 0.143 | 0.190 | 0.132 | 54 |
| F28 | 22 | 1005.5 | 96.2 | 0.126 | 0.205 | 0.141 | 48 |
| F29 | 25 | 1800 | 100 | 0.112 | 0.132 | 0.184 | 51 |
| F30 | 24 | 836.5 | 88 | 0.130 | 0.237 | 0.155 | 71 |
| F31 | 22 | 663.25 | 67 | 0.105 | 0.156 | 0.191 | 59 |
| F32 | 21 | 1158 | 98 | 0.161 | 0.201 | 0.123 | 51 |
| F33 | 23 | 633 | 61 | 0.164 | 0.150 | 0.165 | 48 |
| F34 | 22 | 442 | 23 | 0.084 | 0.130 | 0.257 | 72 |
| F35 | 17 | 374.25 | 13 | 0.130 | 0.089 | 0.191 | 72 |
| in a branch |  |  |  | 0.120 | 0.163 | 0.164 | 51 |
| population |  |  |  | 0.109 | 0.175 | 0.158 | 51 |

The percentile places the branch's median area among random groups of the same size drawn from the analysed set (`tools/projections.py`). The members' share is `px_by_window_members` over `px_in_region_any`: the share of a region's placements made by people who wrote in the room.

**Read against the record.**

- **Stood and gone look alike on the canvas.** By the re-reading, rooms whose own words say the work stood have a median area of 770 px (149 rooms), and rooms whose words say it was gone have 758 (43). All of them have an artwork. The canvas does not separate the two at this grain. One timing differs: in the gone rooms, members made 0.201 of their placements in hours 64 to 73, against 0.165 in the stood rooms. That is a timing, not a cause. The silent rooms are small (median 309 px).
- **What the members placed.** In a branch, members made 0.120 of the placements in their own regions (population 0.109); by branch, from 0.058 (F19) to 0.226 (F14). The account's paragraph on keeping says the record "is not a claim about what survived on the room's patch of the canvas, much of which was placed by people who never wrote in the room." The canvas agrees with that clause.
- **F09.** Its members made 0.056 of their placements in hours 8 to 32, against 0.175 in the population, the lowest share of the 35 branches but one (F20, 0.044). The narrative says these rooms lost a first work and built again. With the bias named, the figure fits that timing: the region is where they rebuilt, so the first site's placements are missing.
- **F34 and F35.** The members' placements peak at hour 72, and F34's members made 0.257 of theirs in hours 64 to 73, the largest share of the 35 branches. Both branches left smaller works than random groups of their size (23rd and 13th percentiles). The members' words, designs sized to the hands and calls answered with a request for a task, were not found from the canvas, and the canvas does not show why the placing came late.
- **F08.** The members' placements peak at hour 71, and 0.228 of them fall in hours 64 to 73. The narrative says scripts' targets were kept current to the end. The canvas cannot tell a script's placement from a hand's, and it overstates these rooms' hands.
- **Large works follow room size.** F13, F23 and F29 sit at the 100th percentile of area; their median members have large records. Each account said so.

**What the model implies a room keeps.** The account's spine says keeping follows building in 148 of 190 rooms [A03] and that keeping holds the known form [P05]. A room that keeps should end with its known form in place. The canvas shows a final artwork. It cannot tell a kept form from a late rebuild or a changed design, so it does not test P05. For F32, whose rooms marked the work and then kept it, section 6 checks the timing: members' placements went on after the marking in five of seven rooms, fell in one (r/httyd), and were empty in one (r/ockytop).

## 6. Dated changes against prior.md's brackets and the placements by hour

**The rule** (logged before computing). A dated change is a sentence in a branch narrative (section 1 of the account) that dates an act on the canvas by a named room's members: placing, building, fixing, changing the design, moving the work, or a marking followed by keeping. Remarks, requests, invitations and acts at or after hour 73 are not. For each act I compare the room's `px_by_window_members` in the four hourly bins before the act's bin with the four bins from it, as rates per bin. The placements move if the ratio is 1.5 or more, or 0.67 or less, and the larger side has 10 placements or more. Each act's implied direction was set before computing: building, fixing or a design change implies a rise; moving the work away or ceasing to defend implies a fall; a marking followed by keeping implies no fall. One amendment, made after seeing the output and logged: a window with no member placement on either side is empty and corroborates nothing.

| branches | room | hour | bracket | the act, as the narrative dates it | implied | members' placements, 4 hours before and from it | result |
|---|---|---|---|---|---|---|---|
| F11 F12 | r/clubpenguin | 36.00 | placement (0 to 73) | a member moved the penguin to another site because it was damaged | fall | 0, 0 | not shown |
| F23 F25 | r/thebluecorner | 39.00 | placement (0 to 73) | members called to a copy of the canvas while they wait for the cooldown | continue | 2404, 1396 | contradicted |
| F27 F32 | r/OnePiece | 51.18 | placement (0 to 73) | finally perfect, then kept | continue | 1027, 1236 | corroborated |
| F27 | r/hawks | 61.14 | placement (0 to 73) | adding the colour detail to the feathers | rise | 646, 252 | contradicted |
| F29 | r/jerma985 | 56.11 | placement (0 to 73) | the chat decided to work on the Jerm and the logo now | rise | 22, 398 | corroborated |
| F29 | r/tagpro | 25.41 | placement (0 to 73), April Fools hours 8 to 32 | voted in the chat to get rid of the bomb | rise | 731, 985 | not shown |
| F31 | r/faeria | 29.15 | placement (0 to 73), April Fools hours 8 to 32 | safe pasture secured for the yak on the Bolivian flag | rise | 11, 4 | contradicted |
| F32 | r/japan | 64.57 | placement (0 to 73) | we did it, but we need to protect the flag now | continue | 126, 157 | corroborated |
| F32 | r/httyd | 52.45 | placement (0 to 73) | we did it | continue | 183, 118 | contradicted |
| F32 | r/vim | 61.90 | placement (0 to 73) | we did it reddit | continue | 94, 87 | corroborated |
| F32 | r/ockytop | 35.56 | placement (0 to 73) | we did it guys | continue | 0, 0 | empty (amended: no member placement either side) |
| F32 | r/newzealand | 34.13 | placement (0 to 73) | we did it, then new damage | continue | 779, 696 | corroborated |
| F32 | r/unturned | 37.45 | placement (0 to 73) | off by a pixel or two but we did it | continue | 191, 147 | corroborated |
| F32 | r/clg | 39.16 | placement (0 to 73) | the logo posted in its perfect form; members cannot keep defending as zealously | fall | 118, 23 | corroborated |
| F33 | r/paragon | 62.85 | placement (0 to 73) | the text made white on black | rise | 45, 32 | not shown |
| F33 | r/feedthebeast | 46.57 | placement (0 to 73) | making the background blue from the bottom | rise | 261, 461 | corroborated |
| F33 | r/wine | 55.46 | placement (0 to 73) | shifting everything across one to fit an r | rise | 15, 85 | corroborated |
| F33 | r/india | 11.74 | placement (0 to 73), April Fools hours 8 to 32 | an 18 by 27 flag being made at a set corner | rise | 16, 47 | corroborated |
| F33 | r/gatech | 52.55 | placement (0 to 73) | maintaining the logo by the most recent design | continue | 623, 660 | corroborated |
| F35 | r/stargate | 51.56 | placement (0 to 73) | two pixels down | continue | 0, 14 | corroborated |
| F35 | r/starbound | 59.68 | placement (0 to 73) | doing my part right now | continue | 168, 253 | corroborated |
| F17 | r/swordartonline | 40.19 | placement (0 to 73) | good job everyone: the mark made | continue | 48, 96 | corroborated |
| F18 | r/bostonceltics | 71.00 | placement (0 to 73) | the mark made after several setbacks | continue | 121, 98 | corroborated |
| F20 | r/chibears | 72.99 | placement (0 to 73) | the logo covered; we must replace it | rise |  | not checkable: after the series ends |
| F27 | r/cowchop | 73.11 | aftermath (73 to 97) | the final logo posted, with the holes | continue |  | not checkable: after the series ends |

Of 25 acts, 2 are not checkable because the placement series ends at hour 72. Of the 23 checked, the canvas corroborates the timing of 15, contradicts 4, does not show 3, and is empty for 1. Three acts fall in the April Fools hours (r/india at 11.74, r/tagpro at 25.41, r/faeria at 29.15); the rest fall later in the placement bracket. A corroborated timing is only that: the members' placements moved at the hour the narrative dates. It says nothing about why.

**The contradicted timings, each a question for its account.**

- **r/thebluecorner, hour 39 (F23, F25).** The narratives read the call to a copy of the canvas as something to do beside it, while members waited for the cooldown. The members' placements in the room's region fell from 2,404 in the four hours before to 1,396 in the four hours from it. Did the copy draw members off the canvas?
- **r/hawks, hour 61.14 (F27).** A member announced colour detail being added to the feathers. The members' placements fell from 646 to 252. Was the detail added by a few hands while the rest stopped?
- **r/faeria, hour 29.15 (F31).** A member announced pasture secured for the room's figure on another room's flag. The members' placements fell from 11 to 4. The counts are small, and the region is the final artwork, so placements made elsewhere are not in it.
- **r/httyd, hour 52.45 (F32).** The room marked its work done. The members' placements fell from 183 to 118. In this member the keeping that F32 names is not seen as continued placing at that hour.

## 7. What this file does not say

Kept, lost and silent are the rooms' own words, and the canvas is what the drawing left behind. Neither is a score of a form. The re-reading of work_remained changes no ledger, and the branch lines keep the field as the ledger gives it. A branch whose rooms end late or carry on after the close does so because its key is about carrying on; that is the cut, restated. The canvas corroborates some timings and contradicts four; it never shows a mechanism.

