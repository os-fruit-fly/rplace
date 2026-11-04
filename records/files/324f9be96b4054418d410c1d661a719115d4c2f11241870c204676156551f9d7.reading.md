# Handback, stage D6: the retelling, the model with its forms inside it

Legs D6a-01 to D6a-08 and D6b, 27 October 2026, corrected at D6a-09 on J's rulings (27 October, 09:27 Berlin, through the handler). One leg per aggregate dimension, then the telling, then the corrections. Outputs:
- `retelling-D6.md`, assembled from `retelling-D6-parts/`;
- `fractal-forms-D6.jsonl` (the form lines) and `fractal-D6.jsonl` (the branch lines);
- `form-cells-sensitivity-D6.tsv`;
- `figure-D6.md`;
- `proposals-D6.jsonl`, and an empty `amendments-D6.jsonl`;
- `notes-D6.md` and this file.

The forms are the six room forms of D4a-08c by their final names, and the 35 branches are the level below (the PI's message for D6, on J's word). The model is the one frozen at D3 (46384686…), unchanged at this stage. The P05 and A11 amendments are held proposals (QD4-001), stated in full in the retelling. No data file changed at D6a-09: the ledger, branches, forms, form lines and branch lines stand as they were.

**Local validation is not established.** prior.md section 3's measure was not computed, and every member's adapted local account is unresolved. Every room the telling names as showing a pattern shows it in its ruled lines, not in a validated account. No account relies on the kind of an add-condition, add-step or restrict line (J after the D3c interview). The canvas is not read anywhere in this stage.

## The claim

Each of the six forms changes the part of the shared model its name says. A changes the terms with neighbours and the plan, C the design, D keeping, help and carrying on, F the spot and the move, and E the host sub's April Fools play. B is a residual grouping whose three facets are the chat, the scripts and the raids. Of the 396 form lines (66 elements and arrows by six forms), 37 specify, 35 restrict, 324 leave the unit untouched, and none replaces it.

That no form replaces an element shows less than it seems. The coding vocabulary made replacing nearly unreachable: the readers returned 11 contradict lines among 42,243 at the first return and 4 among 53,493 at the re-check, and none stands among the forms' selected lines. Many restrictions are failures. Of each form's restrict lines on arrows, as sorted at D5, 43 to 63 per cent say that the arrow fails in the room: A 201 of 432, B 135 of 292, C 172 of 301, D 171 of 316, E 130 of 304, F 72 of 114. The forms do not show that the level below never contradicts the level above. They show that the vocabulary gave almost no way to say so, and that the rooms' lines often said it as a restriction.

Most single cells are leans at the rule's own thresholds. 20 of the 72 changed cells keep their relation at ratio 1.5 and floor 15 per cent, and 52 do not. D, E and F keep their central changes. B keeps its scripts and its chat, and C keeps the design. A keeps none. Record size explains less. With each form's rooms matched to rooms of the other forms of the same record size, and separately of the same amount of canvas-work concepts, 62 of the 72 cells keep their lean and 10 are size-dependent: A 4, E 3, and B, C and F one each, D none. A is the most fragile form on both tests.

By the rooms' own word, the forms that changed keeping (D, with C) kept the work alive to the freeze most often. After it, the rooms that coordinated most were the chat and script rooms of B, then rooms of A and D. These are readings of the record, not tests.

**The form I am most sure of: E, The sub's play, run as work.** One element carries it: 56 of its 84 defining rooms add steps to the April Fools frame, against 18.5 per cent of the 558. The cell keeps its relation at the stricter thresholds. One branch family explains it: F01's rooms are 54 of the 58 holders, and each subform (F02 to F06) explains a part.

**The form I am least sure of: B, Behind the thread: chat, scripts, raids.** It is a residual grouping, not a form, with three facets held by different rooms at about chance overlap:
- the scripts, held by 49 of its 113 defining rooms;
- the chat, 48;
- the raids, 40.

7 rooms hold all three, against 7.4 if the facets were independent, and 20 hold none. 43 of its 113 defining rooms lie nearer another form's centre, the most of any form. Its seven changes may describe three sets of rooms.

**The form that best supports the claim: D, Keeping, with help or carrying on.** It changes 17 units, the most, and keeps 6 of them at the stricter thresholds (keeping, carrying on, the returning call, the host's room for canvas talk, scripts offered and debated but not shown placing, and carrying on before the record). Ten branches have lines in it (F04, F11 to F14, F18, F22 to F24, F27).

**The form that most threatens it: E.** Ten of its 13 changes are restrictions, eight of them on arrows. Its share of restrict lines on arrows that say the arrow fails is the lowest (43 per cent), and many of its lines say the record cannot show the order. Its records hold the play and the reports of the canvas work, and less of the work between them. If a form's restrictions track how thin its record of the canvas work is, the forms partly sort records, not organizing. The size-held test answers part of this. Matched on canvas-work concepts, E keeps 7 of its 8 restrictions on arrows. Three of E's 13 cells are size-dependent (A02 on canvas-work concepts, A10 and A09 on record size).

**The condition between them** is whether a form's record holds the canvas work between the call and the report. Where it does, the form specifies the model where it works (A, C, D, F). Where it does not, the form restricts the model's arrows (E).

## The return value

- **Form lines:** 396 in `fractal-forms-D6.jsonl`, by the rule logged at D6a-01 before it ran. Units changed by each form: A 11, B 7, C 10, D 17, E 13, F 14. Thirty-one units are held as stated by every form.
- **Sensitivity** (`_analysis/d6a09_sensitivity.py`; the section after Part 2 of the retelling).
  - Raising the ratio from 1.0 to 1.5 at the 10 per cent floor takes the changed cells from 99 to 27; at the 15 per cent floor, from 67 to 20.
  - No cell that stays changed at a stricter setting changes its relation.
  - Kept at ratio 1.5 and floor 15 per cent: A 0 of 11, B 2 of 7, C 1 of 10, D 6 of 17, E 4 of 13, F 7 of 14.
  - The marks are in `form-cells-sensitivity-D6.tsv`.
- **The size-held test** (D6a-10; `_analysis/d6a10_size_test.py`; the section after the sensitivity section).
  - The rule was logged before it ran. Each form's defining rooms are matched with replacement to the 5 nearest defining rooms of the other forms, on record size (coded concepts) and, separately, on canvas-work concepts (D01 to D04). A lean survives where the form's share is 1.2 times the matched share or more.
  - Cells that survive both matchings, A and F first: A 7 of 11, F 13 of 14, B 6 of 7, C 9 of 10, D 17 of 17, E 10 of 13; 62 of 72 in all.
  - The 10 size-dependent cells: A's C01, P23, P07 and P12; F's A12; B's A05; C's P04; E's A02, A10 and A09. None of them was marked "robust".
  - In 10 of F's 14 cells, matching on record size raises the ratio. F's rooms change these units more often than other rooms whose records are as short.
  - At 3 or 10 matches, 12 cells change outcome, all with deciding ratios between 1.12 and 1.27.
  - Results by cell are in `form-cells-size-D6.tsv`. `form-cells-sensitivity-D6.tsv` gains a last column, `size_mark` ("robust" 20, "marginal" 42, "size-dependent" 10).
- **Restrict lines on arrows that say the arrow fails** (D5's sort): A 201 of 432, B 135 of 292, C 172 of 301, D 171 of 316, E 130 of 304, F 72 of 114. A further 6 to 34 per form say both that it fails and that the record cannot show it.
- **Branch lines:** 50 in `fractal-D6.jsonl`. All 35 branches are placed and named in the retelling. 38 stand on the naming rule as stated and 12 on its widened readings, recorded as a dated amendment applying backwards (`departures.jsonl` line 21). J's four earlier placements were checked and stand: F08 at P05 in F (the weakest), F35 at A12 in E, and F11 and F12 at P01 in D.
- **Amendments:** none. `amendments-D6.jsonl` is empty.
- **Proposals:** eleven, all unvalidated, against the frozen model:
  - PR-D6-01, the call returns;
  - PR-D6-02, the answer that asks for a task;
  - PR-D6-03, a proposal that is itself the call;
  - PR-D6-04, after the move, the room builds again;
  - PR-D6-05, the design sized to the hands;
  - PR-D6-06, the check before repair;
  - PR-D6-07, the terms bind the placers they reach;
  - PR-D6-08, help from the hands a helper can spare;
  - PR-D6-09, border talk before keeping;
  - PR-D6-10, the play run as work, flagged for E1 against the D3a-55 scope ruling;
  - PR-D6-11, imprinting runs with the work.
- **The figure:** `figure-D6.md`, the C5 drawing with the forms named in its boxes and arrows. Of the 20 arrows, one is specified by a form (A05, by B and D) and 16 are restricted. Its opening paragraph and its legend's line on B were corrected at D6a-09; the drawing is unchanged.
- **Survival by form, from the record** (`_analysis/d6b_survival_forms.json`; defining rooms).
  - The field's kept share is C 60, D 57, B 53, A 50, E 46 and F 44 per cent, against 49 per cent of all 705 rooms. D's records are the least silent (6 of 96).
  - Rooms that coordinated after hour 73: B 35 of 113, A 29 of 135, D 29 of 96, E 20, C 16, F 2 of 34.
  - B's lead sits in its chat and script rooms. 26 of its 35 rooms that coordinated after the close hold the chat or the scripts (26 of 78, 33 per cent). Of the 15 rooms that hold only the raids, 3 did (`_analysis/d6a09_b_facets.json`).
  - The field was right in 25 of 34 rooms at prior.md, and the D5b re-reading agrees with it in 248 of 476.
- **The unadapted group:** empty. No room returned `none`, and 229 adapted rooms are in no branch.
- **The rooms the model could not compose:** by the verdicts the forms carry, one does not compose (r/picturegame) and ten cannot be told. At the re-check none fails to compose, and both readers could not tell 19 rooms. What they share is a short record (1 to 8 coded concepts, against a median of 101), not another way of organizing.
- **What the forms show the model lacks:** three returns, none entered: the call returns (C, D, F), the move returns to building (F; F09) and the marking returns to keeping (A; F32).
- **One condition across the dimensions:** a placer acts on a form or a term only where it reaches them. This holds in keeping, at the border, in a script's target and in help.

## The held proposals (QD4-001; never served, not re-checked)

- **P05 (move 198, history lines 173 to 176; reverted by move 203, line 181).** The statement would gain: "This holds where the keepers can learn of a planned change only by being told, and no informed member holds it." The bound names completeanarchy, polska, satania, halo, bangtan and thesilphroad (the keepers read the change from its shape) and armok, maryland and oneshot (informed members hold it), with their nine re-check lines. The full text is in `retelling-D6.md` and `tree-D4.md`.
- **A11 (move 199, history lines 177 to 180; reverted by line 182).** The arrow from P02 to P04 would be withdrawn under rules 14 and 16. It never beat its null, template first is nearly as common as the transition, the failure clause stands alone in 117 rooms, and 261 accepted restrict lines say a template does not settle the design for good. Form C restricts A11 in 40 of its 58 lines. Both stay held.

## Questions, departures, defects and what is owed

- **QD6-001** (the form lines against the check's branch field). Answered with option (c), recorded as `departures.jsonl` line 20, citing J's 18:01 ruling; line 19 stays.
- **QD6-002** (the missing trusted tree hash). J ruled (27 October, 06:33 Berlin): "The file should be the last cut we did. Prepare a file like the one it needs and give it the authority it needs for the run to continue."
- **The branch-naming rule.** Its widening, written at D6a-04 as a licence and in use from D6a-02, is recorded at D6a-09 as a dated amendment applying backwards (`departures.jsonl` line 21). No branch line changes.
- **Wording items, held with the arrows' wording items from D3c.** A09's and A15's glosses read as causes. Their counts are orders, and their restrict lines deny a cause the arrows do not claim.
- **Owed, on J's rulings of 27 October:**
  - the size-held test, done at D6a-10 (above);
  - prior.md section 3's element-reach half, at E1;
  - PR-D6-10, to be read at E1 against the D3a-55 scope ruling.
- **Defects 100 and 101 are open**, with no rewrite. The account's survival paragraph rests on the `work_remained` field (line 100), and four timings are contradicted by the canvas (line 101).

## Licences exercised (METHOD.md)

- The fractal rule, logged at D6a-01 before it ran, and the reading of "branch" as room form (the PI's message).
- The branch-naming rule and its widening, now a recorded amendment (above).
- Branch lines placed below the form's lean at the branch's key element or an end of its arrow (F20, F28, F30, F31, F35).
- Elements in two dimensions written once, in the first dimension read (K05, P28, C02, P33).
- The instantiation rates of the forms reported beside the untouched lines, with the form medians of coded concepts as the check on record size (D05, D08).
- My reading of the lines decides three things: the proposals' rooms, the split of restrict lines into record-cannot-show and fails, and the facets of B (by the lines' fourth-order themes, as B's account counted them).
- In the survival reading, the canvas is not read, and the uncomposed rooms are given under both verdict counts.

## Slips

- **D6a-01:** the first leg closed with `--pause` after the check refused the form letters (QD6-001).
- **D6a-02:** two Edits to one file in one turn, and a stray `open('/dev/stdout','w')` that wrote nothing.
- **D6a-03 and D6a-05:** a `cut -c` after a helper, refused by the guard.
- **D6a-04:** a read at a wrong path.
- **D6a-07:** a pipe character in a Python set union, refused by the guard.
- **D6b:**
  - one diary line held a typing slip, corrected in the next line;
  - the first draft of the uncomposed rooms gave only the first-return count;
  - three draft statements were caught and corrected before the close;
  - the telling's wording on "without contradicting" overstated what no replacement shows, corrected at D6a-09.
- **D6a-09:**
  - a first count of B's facets by elements did not reproduce the account and was replaced by the account's count by themes;
  - a `diff` with process substitution was refused by the sandbox, and the comparison was redone in Python.
- **D6a-10:**
  - an exploratory command with `|=` in its Python was refused by the guard; the work moved to a script;
  - a diary line put the cells that change outcome at 3 or 10 matches at 7; the script counts 12, and the next diary line corrects it.
