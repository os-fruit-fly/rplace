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

## D6a-09: corrections after the interview (J's rulings, 27 October, 09:27 Berlin)

**The close-check report of D6b, at the interview cut** (`_analysis/d6b_validate_D6_final.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**J's rulings, through the handler (the PI's message of 08:27 UTC).** This leg was added after D6b and replaces nothing. It corrects the telling's wording and records what is owed, and it changes no data file. The interview's answers themselves are not in the folder: `out/interview/` holds my brief under a new name and no transcript. So I worked from J's summary of answers 3 and 4 and recomputed every count by script.

### What this leg did, ruling by ruling

- **1a, the wording.** "Specifies without contradicting" and its kin are replaced in the frame (`retelling-D6-parts/D01.md`), part 2 (`D6b-telling.md`, rewritten whole), `handback-D6.md` (rewritten whole) and the figure's opening paragraph. The figure was redrawn by its script, with the drawing and the tables unchanged, checked in Python. The new wording:
  - No form replaces an element.
  - Replace was nearly unreachable: the readers returned 11 contradict lines among 42,243 at the first return and 4 among 53,493 at the re-check (`adaptations.jsonl`, `adaptations-recheck.jsonl`), and none stands among the forms' selected lines.
  - Of each form's restrict lines on arrows, D5's sort finds that the arrow fails in the room in A 201 of 432, B 135 of 292, C 172 of 301, D 171 of 316, E 130 of 304 and F 72 of 114. That is 43 to 63 per cent, as J's summary of answer 4 said; the shares count the lines sorted as fails alone, not those sorted as both.
- **1b, the sensitivity section.** It is written by `_analysis/d6a09_sensitivity.py --md` to `retelling-D6-parts/D6a09-sensitivity.md` and assembled after part 2. The marks are in `out/form-cells-sensitivity-D6.tsv`, from the same script.
  - The base run (ratio 1.2, floor 10 per cent) gives back all 396 written relations.
  - Changed cells by ratio 1.0 to 1.5: 99 to 27 at the 10 per cent floor, 67 to 20 at 15 per cent.
  - Of the 72 changed cells, 20 are marked "robust" (they keep their relation at ratio 1.5 and floor 15 per cent) and 52 "marginal": A 0 of 11, B 2 of 7, C 1 of 10, D 6 of 17, E 4 of 13, F 7 of 14.
  - In the prose, "robust" appears only as J's name for the mark, in quotes, because the prose check counts it as a watch word.
- **1c, local validation.** The frame now says that it is not established, and that every room named as showing a pattern shows it in its ruled lines, not in a validated account. Part 2's opening and the handback say the same.
- **1d, the branch-naming rule.** `departures.jsonl` line 21 is dated 2026-10-27 and applies backwards to every branch line from D6a-01; no line changes. `_analysis/d6a09_branch_rule_check.py` reads each line.
  - 38 of the 50 stand on the rule as stated (the key's element is the cell's).
  - 12 stand on the widened readings: key theme 1, arrow end 5, antecedent theme 2, and the branch's own words of change 4.
  - 7 of the 12 were written before D6a-04: F11 and F12 at P01 in D; F35 at A12 in E; F07 at P02 and at A11 in C; F33 at A11 in C; F08 at P05 in F.
  - The four J named all stand. F08 at P05 in F rests on its change's words, at 1.51 and 2 of 7 holders, the weakest. F35 at A12 in E is an arrow end below the form's lean. F11 and F12 at P01 in D rest on their change's words, at 2.62 and 2.69 and 3 of 16 holders.
- **1e, form B.** It is told as a residual grouping with three facets, counted by the lines' fourth-order themes (`_analysis/d6a09_b_facets.py`, which reproduces the account's 49, 48 and 40 and its 20 rooms with none).
  - 43 of its 113 defining rooms lie nearer another form's centre, the most of any form.
  - Its lead after the close is restated as a property of the chat and script rooms: 26 of its 35 after-close rooms hold the chat or the scripts (26 of 78), against 3 of the 15 raid-only rooms.
- **2 to 5, what is owed.** These are recorded in part 2 ("What is owed") and in the handback:
  - the size-held test, at D6a-10;
  - prior.md section 3's element-reach half, at E1;
  - defects 100 and 101, open, with no rewrite;
  - PR-D6-10, unvalidated and flagged for E1 against the D3a-55 ruling.

**Licences exercised at D6a-09.**
- B's facets are counted by the lines' fourth-order themes, which reproduce B's account. An element-based count gives 56, 51 and 30 and is not used.
- The "robust" and "marginal" marks follow J's definition (ratio 1.5 and floor 15 per cent), applied as "keeps its written relation".
- The figure's opening paragraph and its line on B were corrected with the telling, though the ruling names only the retelling and the handback.

**Slips at D6a-09.**
- A first count of B's facets by elements did not reproduce the account and was replaced.
- A `diff` with process substitution was refused by the sandbox, and the chain after it did not run. The comparison was redone in Python, and the figure was redrawn after it.

## D6a-10: the size-held test (J, 27 October, 09:27 Berlin)

**The close-check report of D6a-09** (`_analysis/d6a09_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**J's word, through the handler (the PI's message of 09:02 UTC).** This leg was added after D6a-09. It tests each of the 72 changed form cells with record size held fixed, and reports by form, A and F first. It changes no data file and no form.

**The rule, logged in the diary before the script ran.**
- Each form's defining rooms are matched with replacement to the 5 nearest defining rooms of the other five forms, by the absolute difference of ln(measure + 1), ties broken by room name.
- Two measures are run separately: coded concepts, and canvas-work concepts (concepts whose second-order theme is placed under D01 to D04; `_analysis/d6a10_room_sizes.py`).
- An op survives where the form's share is 1.2 times the matched share or more. A cell survives a matching where one of its deciding ops survives, and survives the test where it survives both matchings.
- Reported, not used for the mark: the ratio against the other forms unmatched, and survival at 3 and at 10 matches.
- The script checks that the room-level holders give back the facts files' counts for every deciding op. They do.

**The result** (`_analysis/d6a10_size_test.py`; `out/form-cells-size-D6.tsv`; `_analysis/d6a10_size_test.json`).
- 62 of the 72 cells survive and 10 are size-dependent. By form: A 7 of 11, F 13 of 14, B 6 of 7, C 9 of 10, D 17 of 17, E 10 of 13.
- The size-dependent cells: A's C01 and P23 (canvas-work concepts), P12 (record size) and P07 (both); F's A12 (record size); B's A05 and C's P04 (canvas-work concepts); E's A02 (canvas-work concepts), A10 and A09 (record size).
- None of the 20 cells marked "robust" at D6a-09 is size-dependent.
- In 10 of F's 14 cells, matching on record size raises the ratio. Matched on canvas-work concepts, E keeps 7 of its 8 restrictions on arrows.
- At 3 or 10 matches, 12 cells change outcome, with deciding ratios between 1.12 and 1.27 at 5 matches.

**Written.**
- `out/form-cells-size-D6.tsv`: 72 rows, A and F first.
- `out/form-cells-sensitivity-D6.tsv`, regenerated by `_analysis/d6a09_sensitivity.py --tsv` with a last column, `size_mark`: "robust" 20, "marginal" 42, "size-dependent" 10. Its earlier columns are unchanged (checked).
- `retelling-D6-parts/D6a10-size.md`, written by the script (`--md`) and assembled after the sensitivity section.
- One sentence each in the frame (D01.md) and part 2, and the "What is owed" item marked done.
- `retelling-D6.md`, reassembled.
- `handback-D6.md`: the claim, E's threat, a return-value block, the owed list and the slips.

**Licences exercised at D6a-10.**
- A canvas-work concept counts where any of its theme's third-order placements lies under D01 to D04.
- The pool is the other forms' defining rooms only, as J asked, so the unmatched ratio against the other forms is reported beside the matched one, to separate the change of baseline from the matching.
- A cell with several deciding ops survives where any one of them does, as the rule reads a lean.

**Slips at D6a-10.**
- An exploratory command with `|=` in its Python was refused by the guard; the work moved to a script.
- A diary line put the cells that change outcome at 3 or 10 matches at 7; the script counts 12, and the next diary line corrects it.

## D6a-11: the form telling, form A (J, 27 October, 06:41 to 06:58 Berlin)

**The close-check report of D6a-10** (`_analysis/d6a10_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**J's instruction, through the handler (the PI's message of 09:25 UTC).** Six legs follow D6b, one per form, A to F (D6a-11 to D6a-16). Each writes the form's telling with a figure of its changes against the global model, with its changes drawn apart by mark. It then picks three representative and rich rooms by a rule stated before any room is read, and shows how the model is instantiated in each, with a figure. The cut (D4a-08c) does not change, and no data file changes.

**The selection rule, logged before any room was read.** The candidates are the form's defining rooms in the nearest quarter of distances to the form's centre (the allocation's columns, as D5 measured it) that lie nearer this form's centre than any other. They are ranked by selected changes, then coded concepts, then distance, and the first three are taken (`_analysis/d6a11_select_rooms.py`). For form A: r/FloydVsVoid (distance 0.690, rank 1 of 135, 26 changes), r/prequelmemes (0.777, rank 13, 25 changes) and r/theexpanse (0.737, rank 5, 24 changes). The rule chose D5's best fit again.

**What was written** (`out/form-telling-D6/`):
- `form-A.md`, `form-A.png`, `form-A.svg` and the graphviz source `form-A.dot`;
- for each room, `room-A-<sub>.md`, `.png`, `.svg` and `.dot`.

Facts are in `_analysis/d6a11_facts_A.json`, from `_analysis/d6a11_form_telling.py`.

**Reading rules used in the telling.**
- **The changes.** Each change is written as op:element at the T3, T4 and dimension of the line's placement; that is where the room's own theme sits, not always the element's dimension.
- **A room's instantiation.** It is read from `_views/rooms-x-elements.tsv`. A unit is carried as stated where the room instantiates it with no change. It is changed where the room has a selected change on it, the current shared lines with a full lift that the forms were cut from. A change line in the ledger view that is not selected is drawn apart and not counted.
- **The signature.** The form's change signature is the allocation's (`room-forms-D4a08c.jsonl`); a count from the lines does not reproduce its columns.
- **The A1 tellings.** Each room's A1 telling (`package/<sub>/case.md`) is cited for moments, not redone. Every quotation was checked against it by script.

**What the marks do to form A.** None of its 11 changed cells survives the stricter thresholds. Four are size-dependent (C01, P23, P07, P12), and seven are marginal and survive size matching. The form is a lean of the population toward the terms and the plan kept current, not a set-apart type. Each of the three rooms shows four or five of the form's eleven changes. r/prequelmemes and r/theexpanse carry the form's border terms as stated.

**Licences exercised at D6a-11.**
- The selection rule's quarter and its ranking are mine, stated before the run.
- The ledger view's changes outside the selected set are drawn apart rather than dropped.
- The figures add, to the C5 drawing, only the elements a form or room changes.

**Slips at D6a-11.**
- The first signature, counted from the lines, did not reproduce the allocation's and was replaced by the allocation's own.
- The first list of units carried as stated required an exact match and missed units with other ledger marks; it was corrected to match the figures.
- A diary line said the prose check read 0 before it was rerun on the corrected file; the rerun read 0.

## D6a-12: the form telling, form B

**The close-check report of D6a-11** (`_analysis/d6a11_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**The selection rule, logged before any room was read** (`_analysis/d6a12_select_B.py`). There is one room per facet, as J asked. A defining room holds a facet where it has a selected change line at the facet's fourth-order theme: the chat T4-010, the scripts T4-009, the raids T4-020. The count reproduces B's account (48, 49 and 40). For each facet, the candidates are the rooms holding that facet alone, at or below the median distance to B's centre (0.9414), and nearer B's centre than any other form's. They are ranked by selected changes, then coded concepts, then distance. No fallback was needed. Chosen:
- the chat, r/dwarffortress (0.859, 24th of 113, 17 changes; 5 candidates);
- the scripts, r/uofm (0.855, 22nd, 12 changes; 6 candidates);
- the raids, r/ockytop (0.870, 29th, 9 changes; the only candidate).

**What was written** (`out/form-telling-D6/`). `form-B.md`, `.png`, `.svg`, `.dot`, and for each room `room-B-<sub>.md`, `.png`, `.svg`, `.dot`. Facts are in `_analysis/d6a12_facts_B.json`, by `_analysis/d6a11_form_telling.py`, unchanged from D6a-11.

**What the marks do to form B.** The chat (P23) and the scripts (P14) are marked "robust" and survive size matching. They are two of the 20 such cells in all six forms. The raids facet's own cell (A15) is marginal. The border cells are marginal (P07, P08) or size-dependent (A05). B is told as a residual grouping held together by two sharp facets.

**What the rooms show.**
- r/dwarffortress shows one of B's seven changes (P23).
- r/uofm shows two (P14, A05).
- r/ockytop shows one (A05). It holds the raids through its own lines on attack calls and hosting, and carries B's raids cell (A15) as the model states it.

Each room holds its facet and little else of B. That is what a grouping whose facets sit at chance overlap would lead one to expect.

**Licences exercised at D6a-12.**
- The facet-only condition and the nearer half (rather than the quarter used for A) are mine, stated before the run. Each facet is a part of the form, and B's centre is a mixture of the three.

**Slips at D6a-12.**
- One command held a no-op (`sleep 0`) beside a listing; it did nothing, and it should not have been written.
- One drafted list of units carried as stated included attack calls (P09), which the room changes; it was removed before the check.

## D6a-13: the form telling, form C

**The close-check report of D6a-12** (`_analysis/d6a12_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**The selection rule, logged before any room was read** (`_analysis/d6a11_select_rooms.py`, the rule of form A, unchanged). The candidates are C's defining rooms at or below the first quartile of distances to C's centre (0.8148), and nearer C's centre than any other form's: 21 candidates. They are ranked by selected changes, then coded concepts, then distance, and the first three are taken. Chosen:
- r/suomi (0.7816, 16th of 96, 20 changes, 308 coded concepts);
- r/gatech (0.7802, 15th, 19 changes, 124 concepts);
- r/bardmains (0.7325, 2nd, 16 changes, 85 concepts).

**What was written** (`out/form-telling-D6/`). `form-C.md`, `.png`, `.svg`, `.dot`, and for each room `room-C-<sub>.md`, `.png`, `.svg`, `.dot`. Facts are in `_analysis/d6a13_facts_C.json`, by `_analysis/d6a11_form_telling.py`. Quotations and item ids were checked against the A1 tellings by `_analysis/d6a13_quote_check.py`.

**What the marks do to form C.** One change is marked "robust": the design settled for a time and reopened (P02). It survives size matching on both measures. The template kept current (P04) is size-dependent. The other eight are marginal. The restrictions that carry C's account, the template that does not settle the design (A11, 58 rooms) and the keepers who refuse a change they know of (P05, 46 rooms), are broad and lean only 1.27 and 1.30 times the population. C is told as the rooms where the design is changed most often and reopened after each finish. The held A11 and P05 proposals bear on the form, and the telling says so.

**What the rooms show.**
- r/suomi shows three of C's ten changes (P01, A11, P08). It carries the design and the template as the model states them, and holds C's theme through other units. It is one of the 31 talk-only rooms of the held A11 proposal.
- r/gatech shows seven (P02, P04, C01, A11, P05, P08, A13). It is the room in which the form's course is most complete. It runs its keeping through scripts, which is form B's "robust" change.
- r/bardmains shows four (P02, A11, P05, A13). Twenty-five units are absent in it, the whole contest among them.

The richest room by count of changes is not the one that shows most of its form. The rule ranks by changes against the global model, and r/suomi's changes lie mostly outside C's cells.

**Licences exercised at D6a-13.**
- The room figure now draws the ends of any changed arrow outside the C5 drawing, so every change of the room is shown. Only r/gatech's A21 had been missing, of the nine rooms told so far. The other figures re-generate unchanged.

**Slips at D6a-13.**
- The first r/gatech figure did not draw A21, a change the telling names. It was found by a check of every room's changed units against its figure, and the figure was re-rendered.

## D6a-14: the form telling, form D

**The close-check report of D6a-13** (`_analysis/d6a13_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**The selection rule, logged before any room was read** (`_analysis/d6a14_select_D.py`). D keeps splits below it, and its three leaves partition its 96 defining rooms: D.1, keeping with the call (54); D.2.1, the play, carried on (27); D.2.2, the play, kept (15). One room is taken per leaf. The candidates in each leaf are its defining rooms at or below the median distance to D's centre (0.9042), and nearer D's centre than any other form's. They are ranked by selected changes, then coded concepts, then distance. No fallback was needed. Chosen:
- D.1, r/rotmg (0.8231, 8th of 96, 20 changes; 18 candidates);
- D.2.1, r/bindingofisaac (0.8037, 4th, 23 changes; 14 candidates);
- D.2.2, r/romania (0.8987, 45th, 15 changes; 2 candidates).

Each is among the three rooms the form's account names as nearest its own part's centre.

**What was written** (`out/form-telling-D6/`). `form-D.md`, `.png`, `.svg`, `.dot`, and for each room `room-D-<sub>.md`, `.png`, `.svg`, `.dot`. Facts are in `_analysis/d6a14_facts_D.json`, by `_analysis/d6a11_form_telling.py`. Quotations and item ids were checked against the A1 tellings by `_analysis/d6a13_quote_check.py`.

**What the marks do to form D.** Six of its 17 changes are marked "robust":
- the call returning from carrying on and loss (P01);
- keeping shared and checked (P05);
- scripts offered and not shown run (P14);
- the host's room for canvas talk (P20);
- carrying on begun before the close (P13), and the record not waited for (A09).

None is size-dependent, and D is the only form so. The help in the form's name is marginal: A13 is held by 33 rooms but leans only 1.32 times the population. D is told as keeping shared and checked, with help and carrying on as two further patterns held by different rooms.

**What the rooms show.**
- r/rotmg shows six of D's changes (P01, A01, P05, A13, P13, A09). Its keeping runs through loss and moving, which is form F's ground.
- r/bindingofisaac shows eight (P01, A02, A05, A13, K01, A20, P13, A09), the most. It carries keeping as stated.
- r/romania shows four (P14, P19, K01, P13). Six of its 15 changes sit at mistaking friendly work for vandalism, which is form C's ground.

Of the three, only r/rotmg shows form D's sharp keeping change (P05). The rooms of D.2 carry the sub's play (K01) and the rooms of D.1 do not, as the parts would lead one to expect.

**Licences exercised at D6a-14.**
- One room per leaf of D's kept splits, and the nearer half rather than the quarter, are mine, stated before the run, as for form B's facets.

**Slips at D6a-14.**
- One check command used `cut -c` after a helper and was refused by the harness. It was re-run without it.
- Two wordings in r/bindingofisaac's draft went beyond the A1 telling (an order for one quotation, and "no answer" where the telling says neither acceptance nor refusal). They were corrected before the check.

## D6a-15: the form telling, form E

**The close-check report of D6a-14** (`_analysis/d6a14_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**The selection rule, logged before any room was read** (`_analysis/d6a11_select_rooms.py`, the rule of forms A and C, unchanged; E keeps no split). The candidates are E's defining rooms at or below the first quartile of distances to E's centre (0.8514), and nearer E's centre than any other form's: 20 candidates. They are ranked by selected changes, then coded concepts, then distance, and the first three are taken. Chosen:
- r/fivenightsatfreddys (0.7051, 2nd of 84, 22 changes, 625 coded concepts);
- r/warframe (0.7042, 1st, 21 changes, 294 concepts);
- r/stevenuniverse (0.8262, 13th, 19 changes, 497 concepts).

**What was written** (`out/form-telling-D6/`). `form-E.md`, `.png`, `.svg`, `.dot`, and for each room `room-E-<sub>.md`, `.png`, `.svg`, `.dot`. Facts are in `_analysis/d6a15_facts_E.json`, by `_analysis/d6a11_form_telling.py`. Quotations and item ids were checked against the A1 tellings by `_analysis/d6a13_quote_check.py`.

**What the marks do to form E.** Four of its 13 changes are marked "robust":
- the sub's play, run as work (K01), held by 56 of the 84 defining rooms at 3.61 times the share, the highest lean of the 72 changed cells;
- three restricted arrows that say what the record cannot show: the call and the building apart (A01), the attack talk inside the recruiting (A15) and the marking before a finished mark (A07).

Three are size-dependent (A02, A10, A09) and six marginal. Eight of the 13 changes are arrows, all restricted. E is told as the rooms whose record is the sub's play, run as work, with the canvas work thinner beside it.

**What the rooms show.**
- r/fivenightsatfreddys shows four of E's changes (K01, A15, A08, A10). Its large canvas record holds a design fight among informed factions, which is form C's ground, and terms with neighbours, which are form A's.
- r/warframe shows six (K01, P02, P23, A08, P13, A09). Its contest is absent, and eight of its changes sit at settling borders with one neighbour.
- r/stevenuniverse shows six (K01, A15, A08, P13, A02, A09). Six of its changes sit at moving planning into a chat, which is form B's ground. It changes the frame once, though its takeover ran for about 33 hours.

All three show the form's sharp change, the play (K01). Each also carries a large canvas effort that lies on another form's ground. The rule ranks by changes against the global model, and in form E most changes outside the play are canvas changes.

**Licences exercised at D6a-15.** None beyond the rule of forms A and C.

**Slips at D6a-15.**
- The first draft of form E's telling wrote three cells' fourth-order themes with the arrow's dimension beside them, as if they were one placement (A02, A15, A10). One sentence called the arrows around keeping and the neighbours "the arrows from keeping". Both were corrected before the check.
- The first draft of r/warframe put a word from the A1 telling's paraphrase ("futile") in quotation marks as if a member wrote it. It was rewritten without quotation marks before the check.

## D6a-16: the form telling, form F

**The close-check report of D6a-15** (`_analysis/d6a15_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**J's ruling for this leg (12:25 Berlin, through the PI).** The three rooms portray together what I find representative of the form, and rich: "A mediod is not representative of a polyfaceted cluster." Nearness to the centre is not required. The rule is still stated before any room is read, and kept.

**The selection rule, logged before any room was read** (`_analysis/d6a16_select_F.py`). What I find representative of F is its course, the three acts its name and gloss give. Each act is a changed cell of F with its op:
- asking first: a restrict line on A04, P19 or P27 (21 holders);
- moving for the spot: a restrict line on A10 (16);
- building again: a link line on P03 (12).

One holder per act is taken, three different rooms. The triple is the one with the most selected changes in sum, then the most of F's 14 changed cells shown together, then the most coded concepts. Chosen:
- asking first, r/sips (0.7577, 2nd of 34, 21 changes; holds that act alone);
- moving for the spot, r/planetside (0.8658, 15th, 20 changes; holds that act alone);
- building again, r/nbaspurs (0.853, 12th, 21 changes; holds all three acts).

Together they hold 62 changes and show 11 of F's 14 cells. All three lie nearer F's centre than any other form's, though the rule did not ask it.

**What was written** (`out/form-telling-D6/`). `form-F.md`, `.png`, `.svg`, `.dot`, and for each room `room-F-<sub>.md`, `.png`, `.svg`, `.dot`. Facts are in `_analysis/d6a16_facts_F.json`, by `_analysis/d6a11_form_telling.py`. Quotations and item ids were checked against the A1 tellings by `_analysis/d6a13_quote_check.py`.

**What the marks do to form F.** Seven of its 14 changes are marked "robust", the most of the six forms. They are the cells of its course: asking first (A04, P19), building again (P03, P04, P01), scripts with the building (A06) and the marking of a partial work (A07). One is size-dependent (A12) and six marginal. The move itself (A10) is marginal, though held by the most rooms of any F cell (16). F is told as the rooms whose record is the search for space. Its claim is sharp but rests on 34 short-recorded rooms.

**What the rooms show.**
- r/sips shows four of F's changes (A04, P19, A06, A12). It asked and waited, built elsewhere, and never moved.
- r/planetside shows four, all marginal (A10, P05, P12, K01). It moved from site to site, was refused, and its record ends with no finished mark.
- r/nbaspurs shows nine, six of them "robust". It bargained while building, lost its spot four times, moved, built again, and kept one Spur to the close.

Taken together, the three rooms show the form as a course with branches: asking without moving, moving without building again, and the whole cycle.

**The six form tellings.** With this leg the form telling J asked for is complete: six form tellings and eighteen room tellings, each with a figure, in `out/form-telling-D6/`. No data file, form or cut changed in any of the six legs.

**Licences exercised at D6a-16.**
- The three acts as the frame of representativeness, and the triple chosen jointly, are mine, under J's ruling of 12:25.
- The form figure's legend now names a signature column that is a link between two themes as a link (`_analysis/d6a11_form_telling.py`). Only form F has such a column, and the form figures of B, D and E re-generate unchanged.

**Slips at D6a-16.**
- The first form-F figure printed "None ... (None)" for the link column of the signature. It was fixed and re-rendered before the telling was written.
- Three wordings in the room drafts went beyond the A1 tellings: "a game change", "the first answer" and "a visitor asked". They were corrected before the check.

## D6a-17: the form telling, round 2

**The close-check report of D6a-16** (`_analysis/d6a16_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**J's instructions** (27 October, 14:03 and 15:23 Berlin, through the handler, after the form-telling interview). There were three tasks:
- a second round of room choices by the rule I gave in the interview, for all six forms, with what changed and why, and only the new rooms told;
- one good-old room per form, the plain typical case;
- the figures redrawn with a hollow border for a form cell the room lacks, and restricts split into "the arrow fails here" and "the record cannot show it".

Everything is in `out/form-telling-D6-r2/`, with a `README.md`. Round 1 in `out/form-telling-D6/` is unchanged. The interview transcript is not in my folder, and I worked from J's summary of my answers.

**The rules, logged before they ran** (`_analysis/d6a17_select_r2.py`).
- **Round 2:** a room shows a form cell where one of its selected lines has the cell's unit and a deciding op. There is one room per part where the form has parts (B's three facets; D's three kept leaves). The triple chosen shows the most of the form's cells jointly; ties go to cells shown in sum, then selected changes, then coded concepts. There is no distance limit.
- **Good old:** the candidates hold every column of the form's change signature and lie nearer the form's centre than any other. They are ranked by cells shown, then distance, then selected changes.

**What the rules chose.** Joint coverage, round 1 against round 2: A 8 and 11 of 11; B 3 and 7 of 7; C 8 and 10 of 10; D 12 and 15 of 17; E 9 and 13 of 13; F 11 and 13 of 14. That is 51 against 69 of the 72 cells.

| form | round-2 rooms | good-old room |
|---|---|---|
| A | r/monalisaclan, r/norway, r/ripcity | r/FloydVsVoid (round 1) |
| B | r/AmericanFlaginPlace (chat), r/evex (scripts), r/PlaceNL (raids) | r/mexico (new) |
| C | r/bisexual, r/gatech (kept), r/spacexmasterrace | r/gatech |
| D | r/Temple (D.1), r/bindingofisaac (kept, D.2.1), r/kirby (D.2.2) | r/gamindustri (new) |
| E | r/4chan, r/paladins, r/stevenuniverse (kept) | r/warframe (round 1) |
| F | r/dbz, r/nbaspurs (kept), r/wildhockey | r/nbaspurs |

Sixteen rooms are new and told, and six are pointed to round 1. Covering the cells reaches rooms between forms: r/norway lies nearer B's centre, and r/evex, r/bisexual and r/Temple nearer A's.

**The figures** (`_analysis/d6a17_figures_r2.py`; six form figures and 22 room figures, each `.dot`, `.png` and `.svg`).
- A form cell a room lacks has a hollow double blue border, and every cell of the form is drawn.
- Restricts on arrows follow the D5 sort of each line: fails here, record cannot show, a condition or an overlap.
- A form figure draws each restricted arrow cell as two parallel arrows with the form's counts.
- `d6a11_form_telling.py`'s room facts now carry each change line's id, an added field, so that the sort can be looked up. Its drawings are unchanged.
- Every changed unit and every form cell is drawn in each room figure (checked by script, `_analysis/d6a17_fig_check.txt`).

**Checks.** Every quotation and item id in the 16 new tellings was found in the room's A1 telling, apart from the quoted label "robust". All r/ names are analysed rooms in exact case. prose_check found 0 hits and there are 0 dashes in all 17 files.

**Licences exercised at D6a-17.**
- The rules' tie-breaks are mine, stated before the run. So is the good-old rule's reading of "the form as a whole" as holding every column of its signature, near its centre.
- The A1 tellings were read through `_analysis/d6a17_case_sections.py`: their Chronology and Relations sections, whole, through `mem.py case`. Their other sections were not read.

**Slips at D6a-17.**
- The first check of the room figures matched arrows by the wrong pattern and reported false misses; it was rewritten before any figure was changed. The second check found one real miss: r/4chan restricts a dimension (D02) as the element of a change, which had no box. The script now draws such a unit, and r/4chan's figure was re-rendered.
- The first version of the room-summary script held a no-op line, which was removed before it ran. It also failed once on a change with no fourth-order theme, which was fixed.
- Drafts went beyond their sources in four places, all corrected before the checks:
  - r/ripcity: "each by its only line";
  - r/mexico: a garbled sentence, and a tie stated as a lead;
  - r/4chan: what "Rule 8" says and what the raided work was;
  - the README: a filename written as a pattern.

## D6a-18: the Dutch telling

**The close-check report of D6a-17** (`_analysis/d6a17_validate_D6.txt`): 0 errors, 0 warnings; fractal lines 50, branches placed 35 of 35.

**J's instruction** (27 October, 06:54 and 06:58 Berlin, through the handler). For each of J's fourteen rooms of the Dutch area, show how the global model is instantiated in that room, as in the form telling. Draw one figure per room as in round 2, and write a short note across the fourteen. All of it is in `out/dutch-telling-D6/`, with a `README.md`. The fourteen were not too many for one leg: two were already told (r/norway and r/PlaceNL, round 2, pointed to), and four of the twelve new rooms are thin.

**What was written.** Twelve room tellings: r/cirkeltrek, r/indonesia, r/placehearts, r/mindcrack, r/Goodboye, r/norge, r/czech, r/armenia, r/sweden, r/blackmirror, r/greece and r/thenetherlands. Each has `.md`, `.png`, `.svg` and `.dot`, and the README sets the fourteen side by side.

**What the fourteen show** (`_analysis/d6a18_dutch_info.json`, `d6a18_dutch_matrix.json`).
- **Forms:** six of the rooms are in A, five in B, and one each in C, D and E.
- **Typicality:**
  - only r/PlaceNL shows more than half of its form's changed cells;
  - four rooms show none;
  - several lie on their form's edge or nearer another form's centre.
- **Held as stated:** all fourteen carry the starter, explaining the canvas and jokes.
- **Changed:** of the 130 selected changes, 60 are restricts. Keeping (8 rooms), scripts (7) and sparing (6) are changed most.
- **The neighbourhood:** in most of the records, a neighbour's border lines answer the Dutch rooms' expansion. Three relations read differently here:
  - border talk comes from expansion, not from keeping;
  - sparing gets reasons the model does not name;
  - agreements reach only some placers.

**Checks.**
- Every quotation and item id in the twelve tellings was found in the room's A1 telling, apart from my labels "robust" and "restrict, not sorted".
- All r/ names are analysed rooms in exact case, prose_check found 0 hits, and there are 0 dashes in all thirteen files.
- Every changed unit and form cell is drawn in each figure (`_analysis/d6a18_fig_check.txt`).

**Licences exercised at D6a-18.**
- `d6a11_form_telling.py` now reads thin rooms' lines as well as defining rooms', so that the thin rooms can be told. The form's cells use defining rooms only, and a defining room's figure and a form figure re-generate byte-identical.
- Thin rooms' restrict lines on arrows were not in the D5 sort, and they are drawn as "restrict, not sorted".
- A thin room's distance to its form's centre is computed in the same space as the defining rooms' (the embedding's thin block) and given as the rank it would have.
- The A1 tellings were read through their Chronology and Relations sections, whole, through `mem.py case`.

**Slips at D6a-18.**
- The first diary read piped `mem.py diary` through `cut`, which the harness refused; it was re-run whole.
- Drafts went beyond their sources in seven places, all corrected before the checks:
  - r/cirkeltrek: "the most units carried", which was false;
  - r/indonesia: "war command" in quotation marks, which was my translation;
  - r/mindcrack: "the organised Dutch builders", which the record's own apology contradicts;
  - r/Goodboye: a gloss for the quoted "blep";
  - r/blackmirror: "the first answer", and a claim not limited to the sections read;
  - the README: "a vote" as a reason for sparing, which no sparing line gives.
