# Handback, stage D3: the return, adjudicated

Legs D3a-01 to D3a-57, D3b (two batches) and D3c, 16 to 24 October 2026. The model entered D3 at pass 15 (e15f96470271763d9913e79ed8e332c164a1f176106eefacfe8ffac8e1b3fecd). It is frozen at D3c as one version, 46384686d6173fdeb4c749667478c1363e675bc6b52bb6f4fdc211d387e68525. That is the version served to all 705 rooms at the re-check (QD3-011, option b). The detail and the scripts are in `notes-D3.md`, `exception-report-D.md` and `uncomposed-D.md`.

## The claim

Returned to all 705 rooms, the model held in most of its statements. The rooms restate its parts far more often than they correct them. Of 95,736 ruled lines, 46,046 specify a statement as written, and 72 are accepted corrections. The return changed the model in three ways.
- **It corrected two statements** where rooms showed the same failure. The starter's role no longer includes the members who join (R01). Repair is tied to the form the keepers know, so a change the room planned is repaired away until the keepers learn of it (P05).
- **It bounded the field's arrow** on who may commit the room (A21). The stated limit comes at the making of terms in 36 rooms, not only after an agreement.
- **It added what the rooms did and the model lacked.** Fifteen candidates entered from the rooms' own proposals (the chat, asking and explaining, people the work brings in, new jokes and eleven more). Five earlier candidates and the field's three entries now stand on the rooms' lines.

Against the revised model, 630 rooms compose with no residue (the readers' agreed verdicts, and my rulings where they split), against 201 before. The rewrite fixed what the evidence pointed at in 48 rooms. One clause it added fails in nine rooms. In six, the keepers learn of the change by reading its shape. In three, informed members hold the change against keepers who do not know. That clause is frozen with a bound and a cluster branch, not as a universal claim (F-024).

- **The room that best supports it: monsterhunter.** At h54.08 a member tells the keepers: "Stop repairing the potion. We have a pact with placestart now." [monsterhunter/c0138]. Its first-return correction caused the P05 revision (move 173). After the revision, its three re-check lines on P05 are specifications, and the readers judge it to compose under both versions.
- **The room that most threatens it: halo.** No member tells the keepers. After the close, a member reports: "I love how once it reached a critical mass and people saw what it was they just naturally began protecting it instead of destroying it." [halo/c0402, h79.66]. Its re-check correction (R-halo-b988854ba168-036) fails the frozen clause. The room still composes by my ruling of its split, so the verdict alone does not show the failure; the correction shows it.
- **The condition that separates them** is how the keepers can learn that a change is planned. Where they can learn of it only by being told, and no informed member holds it, the frozen clause tells the room. Where the change's shape is legible to the keepers, or informed members carry it, the clause does not.

## The return value

| What | Count |
|---|---|
| Lines ruled | 95,736 (first return 42,243; re-check 53,493), every line once by its last ruling; `adjudications.jsonl` holds 96,568 lines with the appended re-rulings |
| Lines by decision | accept 84,114; reject 8,872; particular 2,749; modify 1; pending 0 |
| Accepted lines by kind | specification 46,046; evidence limit 34,922; paired elaboration 2,343; proposal 731; correction 72 |
| By ledger (`exception-report-D.md`) | first return: specification 20,637, elaboration 1,282, correction 54, proposal 729, limit 13,981, particular 484 and NONPORTABLE 752, rejected 4,324. Re-check: 25,410, 1,061, 18, 2, 20,941, 699 and 814, 4,548 |
| Elements and arrows at the freeze | 30 standing elements, 15 candidates, 21 arrows. History 172 lines; findings 38 lines (24 findings) |
| Re-check rooms | all 705 (`recheck-scope.json`: 705 affected, 0 unaffected; 18 contrasting cases), all returned and ruled |
| Verdicts ruled | 163 split rooms at D3a-56 (61 composes, 102 with residue); 161 re-check splits at D3b (160 composes, 1 with residue) |
| The four verdicts, first return (e15f9647…) | composes 201; with residue 489; cannot tell 14; does not compose 1 |
| The four verdicts, re-check (46384686…) | composes 630; with residue 56; cannot tell 19; does not compose 0 |
| does-not-compose, by kind | picturegame, out-of-scope, at the first return; none at the re-check, where both readers give it composes with residue |
| cannot-tell, by threshold | first return: coded-share 13, off-platform 1; re-check: coded-share 19 |
| Local status (the labelers) | unresolved in 705 rooms; their grade composes with residue in 705 |

`validate.py D3` prints 330, 364, 10 and 1, and coded-share 10. Its map takes my last ruling per room, else the first-return readers' line, so it mixes the two versions. It also reads picturegame's kind as outside-the-model, since it takes the first kind name in the room's block (`uncomposed-D.md`, re-check note).

## Revisions and their causes

| move | element | leg | what changed | caused by |
|---|---|---|---|---|
| 172 (splitting) | R01 | D3a-01 | the joining clause split from the starter's role | corrections of the joining clause in 12 rooms (history line 135) |
| 173 (relating) | P05 | D3a-04 | repair related to the form its keepers know, and to the room's planned changes (P02) | OnePiece-012, leagueoflegends-053, monsterhunter-016, portugal-029 |
| 174 | P22 | D3a-06 | ruled standing; range names the commonest form | the rooms' lines (history lines 137 to 139) |
| 175 | P21 | D3a-26 | ruled standing; frame 'dispute, or state the limits of' | the rooms' lines (140, 141) |
| 176 | A21 | D3a-27 | standing with a bound; connection aligned with P21; mechanism's request clause dropped | 36 corrections in two families, 26 and 10 (142 to 150; 171 names all 36) |
| 177 to 181 | P06, R02, K03, K04, P19 | D3a-49 to D3a-53 | re-admitted as standing from candidates | each element's own lines and census (151 to 155) |
| 182 to 196 | P23 to P34, K05 to K07 | D3a-55 | entered as candidates | 729 accepted `propose` lines (156 to 170) |
| 197 | P05 | D3c | scope decided: a bounded trunk, a cluster branch and a second limit; no change to the frozen model | nine re-check corrections (172; F-024) |

Moves 172 and 173 name splitting and relating. Moves 175 to 197 name developing working hypotheses. Move 174's lines 137 and 138 name 'stabilizing', which is not one of Grodal, Anteby and Holm's eight, and line 139 corrects the name to developing working hypotheses. Each move is logged and snapped.

## Elements bounded, minted or made candidate

- **Bounded:** A21, by its `bound` (move 176). P05's added clause, by F-024 and history line 172 (move 197), with its words unchanged.
- **Minted:** none. No third-order theme was minted, split or merged, and `tier_history.jsonl` holds no D3 line.
- **Made candidate:** 15 (P23 to P34, K05 to K07). **Re-admitted as standing:** P06, R02, K03, K04 and P19. **Out of tentative:** P21, P22 and A21, all standing.

## The re-check rooms, and what the rewrite fixed

All 705 rooms went back (D3a-57), and all came back in two batches (QD3-009, QD3-010).
- **R01:** the re-check accepts no correction on R01 in 11 of the 12 rooms. hearthstone repeats its first-return line word for word, and the revised statement now holds that line. The added sentence draws four new corrections (criticalrole, gravityfalls, rhythmheaven, transformers); they do not reach a trigger. J: "Keep R01 as it is."
- **P05:** the four cause rooms' 19 re-check lines on P05 are all specifications. The added clause draws nine new corrections in nine other rooms (move 197).
- **A21:** 34 of the 36 rooms carry no correction. adventuretime and weezer repeat their first-return lines.
- **By room:** a correction on a revised element is fixed in 48 rooms and stands in 3 (repeats). 13 rooms carry a new correction (R01 4, P05 9), held. In 263 rooms nothing in the first return pointed at the rewrite, and the re-check tested the revised model there.

## Diagnostics against prior.md

- **Particulars:** 2.8% of the re-check's lines (699, and 814 NONPORTABLE), in 525 of 705 rooms. 127 rooms (18.0%) carry one on a top element (the spine: R01, P01, P03, P05, A02, A01, A03). No room's adaptations are all particulars, and every room has at least one shared line.
- **Distinct shared changes:** 499 groups by D3's pairs, over 2,368 ledger lines. 267 are met in two rooms. Over a seeded order of rooms the curve adds 122, 183 and 194 by third. It does not flatten, and prior.md names this a sign of unbounded revision. Random orders give 123, 190 and 186 for these group sizes, so the shape comes from how few rooms each change is met in. The pairs join two lines at a time, so the group count can exceed the distinct changes. D4's keys and D5's cluster adequacy decide whether the branches explain their members.
- **Corrections met twice:** 19 groups (element and node), all cited in history. They caused moves 172, 173, 176 and 197.
- **Fit before and after adaptation:** before, the fixed-global verdicts above. After, the labelers' grade, which does not vary (composes with residue in all 705), as D2 reported.

## Bounds, with their second room, and the conditions still one room's description

- **A21's bound:** the stated limit at the making of terms ('We have a deal! I can't speak for every member', polska-064; 'I approve that, but people are uncontrollable', finland-056; 36 rooms), and with no agreement in force (FloydVsVoid-033, turkey-029, uiuc-031; 13 rooms).
- **P05's branch, 'the shape read':** polska and satania meet at T4-006, and halo and bangtan at T3-170 and T4-019; completeanarchy and thesilphroad complete the six. **Its second limit:** armok, maryland and oneshot, at three nodes, below the trigger.
- **One room's description:** TheHulk's rally to defend a figure the members love as a landmark (ruled a particular, its residue at the re-check); picturegame's own play as its whole record (out-of-scope). In all, 1,513 re-check particulars stay local, 814 of them NONPORTABLE.

## Residue kinds named

At D3a-56 every with-residue ruling named an act the served model lacked: the chat (P23) in 47 rulings, asking and explaining (P24) in 35, new jokes (P26) in 19, people the work brings in (P25) in 8, the work turned toward the people it shows (P30) in 5, and six other candidates in one or two each. At the re-check those acts are in the model. 56 rooms compose with residue: 55 by the readers' agreed verdict, and TheHulk by my ruling, whose residue is one room's particular. I did not sort the 55 rooms' residue by kind at D3c; D4 reads it.

## The last story's misses, and the two composition rates

The last story (`story_rooms-p5.jsonl`, 35 rooms) left no room not told: 16 were told and 19 told with residue. None of them does not compose, under either version. Of the 16 told rooms, Lugarix is cannot-tell under both versions, and bannedfromanime_irl is also cannot-tell at the re-check. The rates: rooms read against a story at C2 against rooms never read against one, 0.985 (66 of 67) against 0.978 (624 of 638) at the first return, and 0.955 (64 of 67) against 0.975 (622 of 638) at the re-check. On these counts, the stories did not raise the rate at which their rooms compose.

## What the return showed that the room notes did not predict

- **Two routes to the keepers' knowledge.** The room notes name mistaken repair only between rooms (flashtv and evex in the leads). The return shows keepers who stop repairing a planned change when they read its shape (six rooms), and informed members who hold a change against keepers who do not know (three rooms).
- **Members turning on their room's own mark** (P34), and in two rooms spoiling it for fun (paladins and portugal, held). A search of the room notes and leads finds no such act.
- **Decided order and the old tie are wider than the coding showed.** A decided element is shown in about 119 rooms, against the 46 coded (F-006). The tie that names the rival is shown in 112 rooms, against F-013's 7.
- **The stories did not help their rooms compose** (above).

## Held for D4, with their rooms

- **P05's relating revision** (move 197): the change is repaired away as damage until its keepers learn of it, by being told or by seeing enough of its shape to read it; informed members can hold it against keepers who do not know; it is lost or given up where neither the telling nor the shape reaches the keepers. Rooms and lines: the nine above and in F-024.
- **R01's added sentence** (four rooms join with no call), as a wording question. **The paladins and portugal proposal,** beside P34.
- **The wording items carried to D3c:** A11's 'settled' (QD3-008); the spine's three links; A04's split; A05's norm; the mechanisms in words of A05 to A10; A12's conditional answers; A13's second path; A14's one offer; A15's AC lines; A16's reasons and visitors' calls; A17 to A20's wording. Each has its rooms in its D3a section.
- **slovenia-029 against slovenia-060**, two rulings on one P13 act.
- **The account, the figure and the data structure:** the re-read lists what each amendment changes (`notes-D3.md`, 'Re-read against the amendments'). The account's keeping paragraph lacks move 173's clause and move 197's bound; it marks P22 tentative and says P06 and R02 'stay cut'. The figure's count of 23 standing elements and its list of what it leaves out are stale. The data structure is unchanged, since no tier moved.

## The blind re-rule check before the freeze

50 lines (46 drawn, 4 forced). Raw agreement over the drawn pairs: decision 42 of 46, decision and kind 35. The 11 drawn differences are not errors; each original applies a written clause or a quote. Two forced lines were errors under rule 13 and are re-ruled by appended lines (anaheimducks-066 and neu-057). The pairs are in `_analysis/d3c_blind/blind-pairs-D3c.jsonl` for the handler's kappa.

## Defects for the operator

1. **`validate.py` reads a does-not-compose kind from the first name in the room's block.** A block that names a kind to rule it out is read as that kind. Reading the kind from a marked line would fix this.
2. **`validate.py`'s verdict map mixes versions.** It takes the last analyst ruling per room, else the first-return readers' line. After a re-check, the counts mix 161 re-check rulings with 544 first-return verdicts. The re-check readers' agreed lines are in `verdicts-recheck-D.jsonl`, which the map does not read.
3. **The labelers' grade and local status still do not vary** (D2's first defect). All 705 re-check accounts say `unresolved` and `composes-with-residue`, so local validation cannot be read from them.

## Licences exercised (METHOD.md)

- **An in-sample return in Eisenhardt's spirit:** exercised. The model went back to all 705 rooms twice, against two versions. Every line was ruled, and both verdicts stand with their versions.
- **Langley's strategy, declared:** exercised in part. Temporal bracketing at hour 73 decides several readings (G20; P12 and P22 after the close).
- **The count set by kinds, not by a head's capacity:** exercised. The candidates entered by the kinds of act the proposals named, and the verdicts and the uncomposed rooms are counted by kind.
- **Gioia's explosion at the front end:** not a D3 licence.

## Slips

- **A wrong count in the D3b notes.** The line giving the labelers' grade as 691, 4 and 10 is reproduced by no source; both give composes with residue in 705. A correction line follows it in the notes.
- **History line 145's adaptations list** named 22 ids, and 25 of the 36 corrections it counted went uncited. Line 171 names them.
- **Edits to one file in one turn, against the rule:** two to `uncomposed-D.md` and three to this handback, at D3c. Each landed on a separate string.
- **Two blind-check errors** in my D3a rulings, fixed (above).

## Questions

None is open. If `done.sh` refuses the close, the refusal goes to J as a question.
