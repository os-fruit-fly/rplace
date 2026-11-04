# Notes, stage D6

Target length: under 4,000 words. One section per leg. Each item that `notes-D5.md` left for this stage is answered here: acted on (as an unvalidated proposal, since `amendments-D6.jsonl` stays empty), declined with a reason, or sent to the dimension leg where its element falls, and then answered there. The close-check report of each leg is pasted at the opening of the next leg's section, because `done.sh` closes the leg.

## D6a-01: the names, the rule, D01 (Critical mass)

**How the stage is read.** On J's word through the PI (message of 27 October, 03:28 UTC): the forms are the six room forms of D4a-08c, the 35 branches are the level below, and `fractal-D6.jsonl` has one line per element and room form, with a branch only where it explains the form. The line's field `branch` holds the form's letter; `branches` names any D4 branch that explains it.

**The final names (J, 27 October 00:43 Berlin).** Written to `room-forms-names.md` and logged as moves 314 to 319 (contrasting), one per form, each with a `tier_history` line and a snap. A, Border terms and the announced plan; B, Behind the thread: chat, scripts, raids; C, The design reopened; D, Keeping, with help or carrying on; E, The sub's play, run as work; F, Moving for the spot. Below D, the splits the account kept: D.1, Keeping with the call; D.2, Keeping inside the sub's play; D.2.1, The play, carried on; D.2.2, The play, kept.

**The rule for each fractal line** is logged in the diary before it ran and stated at the head of `retelling-D6.md` (`_analysis/d6_fractal.py`). Its floor is proportional, max(5, a tenth of the form's defining rooms), so that form F is read at all. An element without a dimension (P15) and the arrow that ends at it (A12) are read with D01, the dimension of the call they answer.

### Answers to the room-form notes (D5a-36 to D5a-41)

- **D's renaming proposal (D5a-39, *or* for *and*).** Taken up in D's final name (move 317).
- **C's and E's sharpenings (D5a-38, D5a-40).** Carried into their final names (moves 316, 318).
- **Subform candidates A.2, B.2 and B.1.2 (D5a-36, D5a-37).** Declined as subforms: the split rule did not read their splits. They are listed in `room-forms-names.md` as candidates named, not kept.
- **D.1, D.2, D.2.1 and D.2.2 (D5a-39).** Named (move 317); not cut. The D4 tree stays as it is, and a cut would be a new structural claim; the telling at D6b uses them as named parts of D.
- **E.2 and E.1.2 (D5a-40).** Declined: the account called them descriptions, not candidates.
- **D.2 beside E (D5a-39, D5a-40).** Accepted: D.2 is a part of D (`room-forms-names.md`).
- **The return from carrying on to the call (D5a-39) and from the move to building and the call (D5a-41).** Acted on: PR-D6-01, the call returns.
- **To their dimension legs:** A's candidate reading (terms and plans that bind only the placers they reach; D04); D's A13, help from surplus (D04); F's A10, the cause of the move, and A04, border talk before keeping (D04); C's P05 telling clause met by disagreement (D03) and A11 (D02); E's play held only as a key, and F01 with E restating each other in part (D06); the share where the record cannot show an arrow, highest in E (D6b, the telling).

### Answers to the branch notes that touch D01

- **F32 (D5a-32), A02: a proposal that is itself the call.** Acted on: PR-D6-03. Forms D and E restrict A02 at the rule's lean, and their lines say that the start and the first call share one post.
- **F35 (D5a-35), P15 and A12: an answer that asks for a task.** Acted on: PR-D6-02. Form F restricts A12 at the lean; F35's 18 members show the same exchange.
- **F34 (D5a-34), a link from K02 to P02.** To D02, where P02 is read: F34 leans to form C (11 of its 22 rooms), and C's P02 lines include designs sized to the hands.
- **F16 (D5a-16), the chat theme holding phone-placing instructions that fit P24.** To D02, where the chat (P23) is read. P24 is untouched as a change in all six forms.
- **F21 (D5a-21), r/osu: a link from K01 to P01 and P23.** To D06, where K01 is read.

The other branch notes (D5a-01 to D5a-35, D5b) are answered in the dimension legs where their elements fall, and listed in each leg's section.

### D01 in brief

42 lines, 7 leaning cells, 35 untouched. Three forms specify the call (C, D, F), each by making it return later in the work; D and E restrict A02; F restricts A12; B restricts P32. Three unvalidated proposals: PR-D6-01, PR-D6-02, PR-D6-03.

**Licences exercised at D6a-01.** The PI's reading of the stage file; the final names as categorization moves (314 to 319, contrasting); the proportional floor; P15 and A12 read with D01; the how sentences of leaning cells written by me after reading the deciding lines, the untouched cells' sentences generated with counts.

**The close, and QD6-001.** `validate.py D6` at this leg's end gave 110 errors in 6 shapes (`_analysis/d6a01_validate_D6.txt`): every fractal line's branch field holds a form's letter, which the check refuses (42); the figure and the handback are not written; no branch has a fractal line yet (35) and the retelling names 30 of them nowhere yet. The check treats the presence of `retelling-D6.md` as the last leg. The form-level lines follow the PI's message; the conflict is asked as QD6-001 and recorded as `departures.jsonl` line 19. Meanwhile the per-dimension legs close at their safe stops with `done.sh D6 --pause`, the work half done by design, and D6b places and names every branch.

## D6a-02: the restructure (QD6-001), D02 (Coordination without command)

**The close-check report of D6a-01** (`_closes/` holds no report for a pause close; `_analysis/d6a01_validate_D6.txt`): 110 errors in 6 shapes, as above, the sixth being the missing trusted tree hash (below).

**QD6-001 answered (option c, the handler's view on J's instruction; J has not seen it), with the PI's message of 03:57 UTC.** Done as one amendment, `departures.jsonl` line 20, citing J's 18:01 ruling and applying backwards to D6a-01's outputs; line 19 stays. The 42 form lines moved to `fractal-forms-D6.jsonl` (letter in `form`; content compared equal), with one correction on its line: P01|F no longer names F09, because of F09's rooms in F only r/penguins links the call, and not to a move. `fractal-D6.jsonl` holds branch lines only (16 after this leg). `retelling-D6.md` was moved to `retelling-D6-parts/D01.md`, and D02's section is `retelling-D6-parts/D02.md`; D6b assembles `retelling-D6.md`.

**QD6-002 asked.** After the restructure `validate.py D6` gives one error: "D4 tree has no matching trusted closure hash", because `_closes/tree-D4.sha256` was never written (only the checks' test fixtures write it). The tree has not moved: `branches.jsonl` and `crosslinks.jsonl` match the D4a-08 close snap, and `subforms.jsonl` is absent then and now. I do not write a trusted hash myself. Until the answer, a leg whose only refusal is this file closes with `done.sh D6 --pause`.

### Answers to the branch notes that touch D02

- **Branch renaming proposals (F07, F15, F16, F24, F30).** Declined as amendments: the D4 tree is frozen at D6 (`tree_moved`), and a branch's name is part of it. The proposed names stay in `defects.jsonl` for E1, and the retelling describes each branch by what its rooms do.
- **F09 (D5a-09), the arrow from P10 to P03.** Acted on: PR-D6-04. Form F specifies P03 by link lines, and 8 of the 12 holders are F09's rooms.
- **F34 (D5a-34), a link from K02 to P02** (sent here at D6a-01). Acted on: PR-D6-05, from F34's rooms holding P02 lines in forms C (4) and E (5).
- **F15 (D5a-15), the plan follows the work.** Borne out at the form level, without a proposal: form A specifies P04 by add-steps that correct the template against the placements, and 20 of the 32 holders are F15's rooms. It lies inside P04's statement.
- **F15 and F33 (D5a-33), one change at two nodes.** At the form level they fall in different forms, F15 in A and F33 in C, so the coders' placement of the template talk follows the form's lean. No change.
- **F15, F29 and the held A11 proposal (D5a-15, D5a-29).** Noted beside the held proposal, which stays held (QD4-001); form C restricts A11, with 40 of 58 lines failing as stated.
- **F16, F29 and F30 (D5a-16, D5a-29, D5a-30), the chat family.** Read together, as asked: form B holds F16 and F29 at its P23 specification, A specifies P23's upkeep, and E restricts it. One change at P23 with three ops; no amendment.
- **F16, P24 in the coders' chat theme** (sent here at D6a-01). P24 is untouched as a change in every form, and E's restricting P23 line from r/pcmasterrace says the same: interface instructions in a chat-labelled theme are teaching. A coding note for E1, no change.
- **F16, entry control; P33 not coded for it.** No form changes P33. The reading stays a reading.
- **F24 (D5a-24), P14's two evidence states.** Declined as a change: the form lines already keep them apart (A and D restrict P14 where scripts are offered and not shown placing; B, E and F specify it where machines are run).
- **F24, a norm of means without enforcement; F24 and F30, restrict-keyed branches.** For D07 and E1: the first is a remainder the telling names, the second a coding pattern for E1.
- **F07, F08 and F15 (D5a-07, D5a-08, D5a-15), P05's telling clause** (F-025, the machine form, the clause carried through the plan). To D03, where P05 is read.
- **F16 (D5a-16), host containment and the move to a chat (P20 to P23).** To D06, where P20 is read.

### D02 in brief

78 form lines (21 leaning, 57 untouched) and 13 branch lines; 197 evidence codes resolve. Each form specifies the part of coordination its name says; D only restricts here (A01, A06, P14). Two unvalidated proposals: PR-D6-04, PR-D6-05.

**Slips at D6a-02.** Two Edits to `_analysis/d6a02_move_form_lines.py` in one turn; a stray `open('/dev/stdout','w')` in a check command, which raised an error and wrote nothing; one Python read of `notes-D5.md` refused by the guard, redone with `grep`.

**Licences exercised at D6a-02.** QD6-001's shape; the correction to P01|F recorded on its line; a branch named as explaining a cell only where it leans to the form and its own key matches the cell (chosen from a script's candidates); the renamings declined because the tree is frozen.

## D6a-03: QD6-002 answered, D03 (Maintenance)

**The close-check report of D6a-02** (`_analysis/d6a02_validate_D6.txt`): 1 error, 1 warning. The error was the missing trusted tree hash; the warning, that `retelling-D6.md` is not written yet, is expected until D6b.

**QD6-002, answered by J's ruling** (27 October, 06:33 Berlin, through the PI's message of 05:34 UTC): "The file should be the last cut we did. Prepare a file like the one it needs and give it the authority it needs for the run to continue." The handler wrote `_closes/tree-D4.sha256` with the tree hash at D4a-08's close (0499928b..., the value I had checked). The answer recorded in `asks.jsonl` is the handler's earlier view (do not write it; keep pausing); J's ruling supersedes it, and I record the ruling as QD6-002's answer here and in the diary. From this leg the dimension legs close with `done.sh D6`.

### Answers to the branch and form notes that touch D03

- **F07, F26 and F27 (D5a-07, D5a-26, D5a-27): read F-024 to F-027 together, beside the held P05 proposal, before any change to P05.** Done at the form level (`retelling-D6-parts/D03.md`). Four ways the clause holds only in part are seen in the forms: refusal by informed keepers (C; r/de in A), the border (D04), the script's target (F; F08) and the check before repair (D). No form's lines show a planned change lost only for want of telling. P05 is not amended (the model is frozen), and the held proposal stays held.
- **F27 (D5a-27), a step the room models propose: checking whether a change is intended before undoing it.** Acted on: PR-D6-06, the check before repair, from D's P05 add-steps (five rooms) and one link line in A.
- **F08 (D5a-08), a machine form of the telling clause.** Seen in form F's keeping (r/wildhockey's repair tool) and carried in PR-D6-06's text as a route; no separate proposal, since F-027 already states it.
- **F15 (D5a-15), the telling clause carried through the plan.** Seen in form A's P04 add-steps (D02: helpers ask for warnings on obsolete templates so that repair does not undo the plan). No separate proposal; it is the template route of F-024's scope.
- **C's note (D5a-38), P05's telling clause meets disagreement.** Borne out at the form level: C restricts P05 (46 of 96), and F07 explains it.
- **F32 (D5a-32), the marking returns to keeping.** Form A specifies P05 by link lines, and 9 of F32's rooms hold them; a return from the marking (P11) to keeping (P05) that the model's arrows do not state, read in the telling at D6b beside PR-D6-01 and PR-D6-04.

### D03 in brief

18 form lines (4 leaning: P05 in A, C, D and F; 14 untouched) and 4 branch lines (F07, F27, F32, F08); 62 evidence codes resolve. One unvalidated proposal: PR-D6-06 (proposals now 6).

**Slip at D6a-03.** A `cut -c` after `mem.py diary` at the opening, refused by the guard (J's rule on whole reads); redone without it.

**Licences exercised at D6a-03.** J's ruling recorded as QD6-002's answer; F26 dropped from A's P05 cell after its two rooms' lines were read (they do not concern the border); F27's sentence limited to the two rooms of four that check before repair.

## D6a-04: D04 (Order without law)

**The close-check report of D6a-03** (`_analysis/d6a03_validate_D6.txt`): 0 errors, 1 warning; fractal lines 20, branches placed 14 of 35. The warning, that `retelling-D6.md` is not written yet, is expected until D6b. The leg closed normally with `done.sh D6`. Correction of record: the head was 2,998 words at that close, not 2,997 as its closing diary line said.

### Answers to the branch and form notes that touch D04

- **A's note (D5a-36), terms and plans that bind only the placers they reach.** Borne out at A05 in A, B and D, and carried as PR-D6-07, a bound on A05 (24 rooms; F26 explains A's cell, F08 B's).
- **F26 (D5a-26), A05 as P05's telling clause stated on P07; F-026.** F26 explains A's A05 cell (6 rooms). PR-D6-07 states F-026's border half on A05. The renaming is declined: the tree is frozen.
- **F10 (D5a-10), the telling problem between rooms.** F10 explains A's P08 cell (14 rooms), and relaying the terms to placers is one of its steps (r/poland, r/transformers). It is carried in PR-D6-07. r/buffalobills's limit stands: the record does not show whether the placers who pushed past its deal had heard of it. The renaming is declined.
- **F22 and F28 (D5a-22, D5a-28), P16's order of tasks: the helper's own work first.** Borne out in D (F22: 11 rooms at P16, 3 at A13) and in A (F28: 10 rooms at P16, where the form as a whole leaves P16 untouched). Carried as PR-D6-08, a condition on P16 and a bound on A13. F22 and F28 share no room and fall in different forms, D and A, as the D5 note expected of one change split by where the coders lifted the line. The renamings are declined.
- **F22 (D5a-22), recognising the form, in help and in keeping.** r/OnePiece's P16 line in D says accurate aid needs the allied image. With PR-D6-06 (the check before repair) and PR-D6-07 (the terms reach the placers) it makes one thread: a placer acts on the form or the terms only where they reach it. For the telling at D6b; no separate proposal.
- **F31 (D5a-31), read the hosts' records beside the guests'.** Done for the two hosts the note names. r/greenlattice (form A) holds applications, an approved-project document and no-build diagrams, and hosting contested by a proposal to purge guest work. r/thebluecorner (form B) holds guest permission reversed by a vote or a purity demand. Neither is an F31 member. The host's rule is in the record where the room is the host, so F31's limit is the guests' record's limit, as the note says. F31 restricts P19 in A (8 of 12 holders), and D and F restrict P19 the same way.
- **D's note (D5a-39), help from surplus (A13).** Borne out in C and D; PR-D6-08.
- **F's notes (D5a-41), the cause of the move (A10) and border talk before keeping (A04).** E and F restrict A10. P10's statement already names the loss of the spot, and F-019 agrees, so no proposal. A04 is carried as PR-D6-09: two routes into P08 before keeping, from seeking the spot and from building.
- **F27, F30 and F31 on A07 (D5a-31).** For D07, where A07 ends.

### D04 in brief

120 form lines (22 leaning, 98 untouched) and 7 branch lines (F10, F26, F28, F31, F08, and F22 twice); 134 distinct evidence codes resolve. Branches placed: 19 of 35. Three unvalidated proposals: PR-D6-07 to PR-D6-09 (proposals now 9; their 57 codes resolve).

**Licences exercised at D6a-04.** The D6a-02 rule that a branch's own key matches the cell, read as: the key's element is the cell's element or an end of the cell's arrow, or the key's theme belongs to the arrow's antecedent (F26: restrict on P05 at T3-010, settling borders with neighbours, a theme of P08). F08 at A05 in B rests on its change's own text ("a revision must reach the operator and the target file"), not on its key, as F08 at P05 in F did at D6a-03. F28 and F31 are placed at their key elements in form A, where the form line stays untouched; their branch lines give the branch's share of the form's holders. Candidates set aside after reading their lines: F10 at A14 in A (help as the terms, not the deal's work), F29 at A05 in B (one of three rooms concerns the chat), F07 at A13 in C (its change is the telling clause, not help). The proposals' rooms are my reading of the lines.

**Slips at D6a-04.** A read of `model/elements.jsonl` at the wrong path (the model is in `out/model/`), which failed and wrote nothing. The context was compacted during the leg; the head was reconciled with the diary before the next write.

## D6a-05: D05 (Collective identity)

**The close-check report of D6a-04** (`_analysis/d6a04_validate_D6.txt`): 0 errors, 1 warning; fractal lines 27, branches placed 19 of 35. The warning, that `retelling-D6.md` is not written yet, is expected until D6b. The leg closed normally with `done.sh D6`.

### Answers to the notes that touch D05

- **F14 (D5a-14), kept damage beside P26 and P05.** P26 is untouched in every form and F14 has 7 members; the case stays a particular of three histories, as the note said. F14's line comes with its key (P13) under D07.
- **F23 (D5a-23), a group outliving its task (P28).** P28 is untouched in every form. F23's line comes with its key (P13) under D07.
- **Absence notes (F22, F33, F35: P26 or K04 held less often in their members; F29: C02 and K03).** F22, F33 and F35 lean to D, C and E, away from B, consistent with the form rates. F29 leans to B (2.00) and still holds C02 in 2 of 25 members and K03 in 4, against 36 and 44 of the 124 rooms of its size (D5a-29): inside B the identity elements sit outside the chat branch. A particular for the telling; no action.

### D05 in brief

36 form lines, all untouched; no branch lines; no proposal. The forms differ only in how often their rooms hold the dimension's elements: B above the 558's rate on all six, F least, E low on C02 and P28 despite the longest records. These are instantiation rates, which the rule does not test; they go to the telling at D6b beside the form accounts. C02 sits also in D08 and P28 in D06: their lines are written here once, and the D06 and D08 legs refer to them rather than writing them again.

**Slip at D6a-05.** A first command at the opening with `cut -c` after a `grep`, in the same line as `mem.py`, refused by the guard (J's rule on whole reads); redone without it.

**Licences exercised at D6a-05.** Elements in two dimensions written once, in the first dimension read; the instantiation rates reported beside the untouched lines, with the form medians of coded concepts from the room-form accounts as the check on record size; the restrict lines sorted by my reading of the cells read, not all cells.

## D6a-06: D06 (Host framing)

**The close-check report of D6a-05** (`_analysis/d6a05_validate_D6.txt`): 0 errors, 1 warning; fractal lines 27, branches placed 19 of 35. The warning, that `retelling-D6.md` is not written yet, is expected until D6b. The leg closed normally with `done.sh D6`.

### Answers to the notes that touch D06

- **Form E (D5a-40), the model holds the play only as a key.** Borne out at the form level: E, D and F specify K01 by added steps, the steps the model gives the canvas work. Carried as PR-D6-10, a process element beside K01; it would widen the scope that D3a-55 set, which a later model decides.
- **Form E (D5a-40), F01 and form E restate each other in part.** They do, in part. 59 of F01's 103 rooms are in E, all five subforms lean there, and F01 explains E's only leaning cell in this dimension (54 of 58 holders). The other 44 lie in D (23), F (10), C (6) and B (5). F01's rooms are also 23 of D's 24 holders and all 9 of F's, but F01 leans there at 1.32 and 1.22, under the rule's 1.5, so it is named only in E. F01 is a facet mostly inside E, reaching D's split D.2.
- **Form E (D5a-40), D.2 belongs to form D.** Borne out here: 21 of D's 24 K01 holders are D.2 rooms.
- **F01 to F06 and F21, the frame family.** All seven placed at K01 in E; F04 also in D and F. F21's line says that only two of its seven rooms in E bear out its own change; r/osu's line shows the play reaching the canvas work.
- **The held paladins and portugal proposal beside P34 (QD3-011).** P34 is untouched in all six forms; the proposal stays held.
- **F30 (D5a-30), the chat seen only through its invitations.** Not placed yet. It leans to A (1.77) and B (1.67) and its key is on P23, under D02; its line is owed by D6b.

### D06 in brief

24 form lines (5 leaning: K01 in D, E and F; P20 and A20 in D; 19 untouched; P28's rows left out, written at D6a-05) and 9 branch lines (F01 to F06 and F21 at K01 in E; F04 at K01 in D and in F); 81 evidence codes resolve. Branches placed: 26 of 35; still to place F13, F14, F17 to F20, F23, F25 (D07) and F30. One unvalidated proposal: PR-D6-10 (proposals now 10; its 89 codes resolve).

**Licences exercised at D6a-06.** P28's rows dropped from the rule's output before writing (`d6a06_fractal_D06_noP28.json`), since its lines stand under D05. F01 not named at D or F because its lean there is under 1.5, though its rooms hold nearly all of those cells; the prose says so. F21's line written at the cell where it leans, with its disagreeing rooms described, rather than left unplaced. The two counts in PR-D6-10 are of add-step holders (E 56), not of all K01 holders (E 58).

**Slips at D6a-06.** None found.

## D6a-07: D07 (Imprinting)

**The close-check report of D6a-06** (`_analysis/d6a06_validate_D6.txt`): 0 errors, 1 warning; fractal lines 36, branches placed 26 of 35. The warning, that `retelling-D6.md` is not written yet, is expected until D6b. The leg closed normally with `done.sh D6`.

### Answers to the notes that touch D07

- **A07 across F27, F30 and F31 (D5a-31): rooms marked their work during it, before it was finished, after losing it, or on a spot held on leave, which A07's bound does not cover.** Borne out at the form level: E and F restrict A07, and A and D specify P11 with marking during the work. Carried as PR-D6-11 (46 rooms), with A08's, A09's and P13's timing.
- **F11 (D5a-11), A09's wording.** Borne out: in D and E many A09 restrict lines deny that a saved record caused the room to carry on, which A09, an order, does not claim. The wording item stays held with the arrows' wording items from D3c; the telling states A09 as an order.
- **F11 and F23 (D5a-11), one set of events read with two ops?** They meet in D's P13 cell and share 4 of F23's 9 holders there (r/bindingofisaac, r/cgpgrey, r/greyblob, r/naruto). This is the overlap of two groupings at one node, as D4a-04 found for branches that meet at a node; both keep their lines.
- **F14 (D5a-14), kept damage.** F14 is placed at P13 in D (r/texans, r/cgpgrey), and the kept damage shows in r/cgpgrey and, in form A, in r/utahjazz. A particular of a few histories, as the note said.
- **F23 (D5a-23), a group outliving its task.** F23 is placed at P13 in D; P28, where the note pointed, is untouched in every form (D05).
- **r/enterthegungeon (D5a-22, section 7), a wish to reuse that fetched the record after the close.** Its F23 lines in D's P13 cell ask for an implementation report and for evidence of renewed defence; the case stays a particular beside A09's bound, which names a next canvas planned while still building, not a record fetched after the close.
- **F30 (D5a-30).** Placed at this leg, under D02: F30 restricts P23 inside form A (10 of the form's 16 restrict holders), and `retelling-D6-parts/D02.md` names it in one added sentence.
- **The renamings of F11, F17, F19, F20, F23, F25 and F27 proposed at D5.** Declined: the tree is frozen.

### D07 in brief

54 form lines (11 leaning: P11 in A and D, P12 in A and F, P13 in D and E, A07 in E and F, A08 in E, A09 in D and E; 43 untouched; P22, P25 and P30 untouched in all six; K05's rows left out, written at D6a-02) and 14 branch lines (F17, F18, F19 at P11 in A; F18 at P11 in D; F11, F12, F13, F14, F23 at P13 in D; F11 at A09 in D; F25 at P13 in E; F09 at A07 in F; F20 at P12 in B; F30 at P23 in A); 99 evidence codes resolve. All 35 branches now have a fractal line and are named in the parts. One unvalidated proposal: PR-D6-11 (proposals now 11; its 46 codes resolve).

**Licences exercised at D6a-07.** K05's rows dropped from the rule's output before writing (`d6a07_fractal_D07_noK05.json`). F20 placed at its key element in B, where the form line stays untouched, and F30 in A, where the form specifies P23 by add-steps; both lines give the branch's share of the form's holders, as F28 and F31 did at D6a-04. F09 placed at A07 in F by the arrow-end reading of the key rule (its key is on P03, A07's antecedent), with its third room's disagreement written in the line. PR-D6-11's 46 rooms are my reading of the deciding lines, each room counted once.

**Slip at D6a-07.** Two check commands were refused by the permission check; the second contained a pipe character in Python's set union (`|=`), and both were redone without it (`set.update`).

## D6a-08: D08 (Contention)

**The close-check report of D6a-07** (`_analysis/d6a07_validate_D6.txt`): 0 errors, 1 warning; fractal lines 50, branches placed 35 of 35. The warning, that `retelling-D6.md` is not written yet, is expected until D6b. The leg closed normally with `done.sh D6`.

### Answers to the notes that touch D08

- **Form B (D5a-37): A15 cannot be shown in 11 of 18.** Borne out at the form level: B restricts A15, and by my reading 11 of its 18 lines say the record cannot show the same recruited hands attacking, while 7 fall inside A15's bound (the attack call first, or in the opening turn with recruitment).
- **Form A (D5a-36): on delivery and cause, A15 among them, the record cannot show it.** A leaves A15 untouched (13 restrict holders at 0.84 times the share); E restricts it in the same terms as B.
- **The branches' notes on P09 and P18 held less often in their members (F21, F22, F28, F33, F35).** Consistent with the form rates: B holds contention most, and these branches lean to E, D, A, C and E. No action.

### D08 in brief

24 form lines (2 leaning: A15 in B and E; 22 untouched; P09, P18 and A18 untouched in all six; C02's and P33's rows left out, written at D6a-05 and D6a-02); no branch lines; 8 evidence codes resolve. No proposal; A15's gloss is a wording item, held with the arrows' wording items from D3c, as A09's is. The dimension legs are complete: eight parts, 396 form lines, 50 branch lines with all 35 branches placed and named, and 11 unvalidated proposals. D6b assembles `retelling-D6.md` from the parts with the figure, the survival reading by form and the handback.

**Licences exercised at D6a-08.** C02's and P33's rows dropped from the rule's output before writing (`d6a08_fractal_D08_noC02P33.json`). The split of B's 18 lines into 7 inside the bound and 11 that the record cannot show is my reading.

**Slips at D6a-08.** None found.

## D6b: the telling, the figure, the handback and the interview

**The close-check report of D6a-08** (`_analysis/d6a08_validate_D6.txt`): 0 errors, 1 warning; fractal lines 50, branches placed 35 of 35. The warning, that `retelling-D6.md` was not written yet, ended at this leg.

**The close-check report of this leg, before the cut** (`_analysis/d6b_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35. With `retelling-D6.md` present, the check found the figure and the handback, every branch with a fractal line, and every branch named in the telling.

### What this leg wrote

- `retelling-D6.md`, assembled by `_analysis/d6b_assemble.py` from the parts: the frame and D01 to D08 (part 1), then `retelling-D6-parts/D6b-telling.md` (part 2). It has 12,395 words and 235 r/ names, all among the 705 analysed rooms in exact case, and it names all 35 branches. Part 2 tells the model with its forms inside it, which forms kept the work alive, the unadapted group, the uncomposed rooms, the returns the model lacks, the held proposals in full, the eleven proposals apart, and the answer to the theory question. The parts stay in place; D01.md's target-length line was replaced with the assembled length.
- `figure-D6.md`, drawn by `_analysis/d6b_figure.py`. It is the C5 drawing with the forms named in its boxes and arrows, four added boxes (P19, P23, P27, P32) and C01 beside it, a legend and a table of each form's changes and branches.
- `_analysis/d6b_survival_forms.py` and its JSON: the survival reading by form, from the record. The canvas is not read.
- `handback-D6.md` and `interview/D6b.md` (725 words).

### Answers to the notes still open

- **The two missing returns (carried in the head since D6a-01).** Told in part 2 with F32's third: the call returns (PR-D6-01), the move returns to building (PR-D6-04) and the marking returns to keeping (F32). None is entered.
- **The survival paragraph (defects line 100).** The telling reads survival by form from the field and from the D5b re-reading, with silence counted, and states the field's error. The account's own paragraph is not rewritten here; the defect stays open.
- **The uncomposed rooms.** Given under both verdict counts: by the verdicts the forms carry (1 does not compose, 10 cannot tell) and at the re-check (0 and 19). What they share is a short record.

**Licences exercised at D6b.** The survival reading uses defining rooms, with all members and D's splits in the JSON beside them. The canvas is not read. The form I am most sure of (E) and least sure of (B) are my judgment, with the grounds written in the handback.

**Slips at D6b.**
- One diary line held a typing slip in its counts; the next line corrects it.
- The first draft of the uncomposed rooms gave only the first-return count; it was corrected from the D5 handback before any check ran.
- Three statements in the drafts were caught on reading them against their sources and corrected before assembly or close: the handback named seven branches in form D where ten have lines; the figure's legend said no form specifies an arrow, where A05 is specified by B and D; and the telling put form C's refusal under the held P05 bound, where it is F-025.
