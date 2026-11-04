# How the rooms are allocated to the room forms

Leg D4a-08, 26 October 2026. J ruled through the handler (22:18 Berlin): "6 it is. Please tell the agent to document how they are allocated and the allocation it did earlier, as we need this soon. Also they need to push the full analysis down to the leaves so we get all the further cuts at smaller levels. Not that they needed it, but we do for the graph." The amendment is dated in `departures.jsonl` (line 16).

The room forms are the six forms of D4a-08c. Sections 1 to 3 say how every room reaches its form. Section 4 describes the tree below the forms, written for the figure. Section 5 gives the earlier allocations in order. The room forms are an addition after the 35 branches, not a recut. `branches.jsonl`, `crosslinks.jsonl`, `tree-D4.md`, `room-forms-D4a05.*` to `room-forms-D4a08c.*` and every D5 file are unchanged.

## 1. The six forms

| form | name | rooms | defining | thin | core |
|---|---|---|---|---|---|
| A | the terms between neighbours, with the plan announced | 166 | 135 | 28 | 3 |
| B | the work behind the thread: the chat, the scripts and raiding | 141 | 113 | 23 | 5 |
| C | the design and its marking | 125 | 96 | 27 | 2 |
| D | keeping, with traded help and carrying on | 119 | 96 | 20 | 3 |
| E | the sub's April Fools play | 98 | 84 | 12 | 2 |
| F | the spot: lost, chosen or yielded, and building again | 56 | 34 | 16 | 6 |
| all | | 705 | 558 | 126 | 21 |

Each of the 705 analysed rooms is in exactly one form. Defining rooms shaped the forms. Thin rooms and core rooms were placed afterwards (steps 8 and 9). The forms are lettered by their number of defining rooms, largest first; C and D tie at 96. The largest form holds 2.96 times as many rooms as the smallest. Each form's pattern and whether a differing account could be written are in `room-forms-D4a08c.md`.

## 2. How a room reaches its form

A room is compared with the others by two profiles. The change profile records where the global model failed the room. The code profile records what the room did. The rule of each step was logged in the diary before its script ran.

**Step 1. The rooms and their changes.** The unit is the room. A room's *selected changes* are its ledger lines, accepted or modified at adjudication, that change the model: the ops restrict, add-step, add-condition, link and contradict. Lines that instantiate an element or record an absence change nothing and are left out. 6,637 lines are selected. 6,634 of them carry a lift up the ladder and are used; three carry none. 684 rooms hold at least one selected change. 21 rooms hold none, and they are the core.

**Step 2. The change profile.** Each selected line counts at three levels of the ladder: its third-order theme, its fourth-order theme and its dimension. Its lift gives these nodes, starting from the second-order theme the line was written from. Two kinds of lines also count as links between nodes.
- *An arrow line* changes one of the model's arrows. It counts as a link from the arrow's source element to its target element. Each end reaches the ladder through the element's anchors in `model/elements.jsonl`. At the fourth-order level the end takes the element's fourth-order themes, and a third-order anchor is taken up to its fourth-order theme. At the dimension it takes the dimension that holds that theme. At the third-order level it takes the element's third-order anchors where it has them; otherwise the line's own third-order theme, if that theme lies under the end; otherwise the end's fourth-order theme. One element, P15, is anchored outside the ladder, so its end stays at the element.
- *A link-op line* proposes a connection the model lacks. It counts as a link from the line's own node to the element's anchor.

An arrow line or a link-op line gives half its weight to its own node and half to its link. A link with several pairs of ends is split equally over the pairs. Every other line gives its whole weight to its node. Columns held by only one defining room are dropped. That leaves 406 third-order columns (262 of them links), 200 fourth-order columns (172 links) and 67 dimension columns (59 links), 673 in all.

Within each level, a room's counts become shares. So rooms are compared by the mix of their changes, not by their number. Each share is replaced by its square root and divided by the square root of 6. The squared distance between two rooms is then the mean, over the three levels, of the squared Hellinger distance between their shares. Each level counts equally. A room with no change sits at 0, the global model with nothing changed.

**Step 3. The code profile.** A room's coded concepts (`package/store/codes.jsonl`, 115,388 concepts in the 705 rooms) go up the ladder through the placements of their second-order themes (`assignments_final.jsonl`). They reach the third-order themes, the fourth-order themes (`fourth/fourth.jsonl`) and the dimensions (`dimensions.jsonl`). A concept whose second-order theme is placed in several third-order themes is split equally over them. 407 concepts have no placement and do not count. Columns held by only one defining room are dropped. That leaves 183 third-order columns, 28 fourth-order columns and 8 dimension columns, 219 in all.

Within each level, a room's value on a node is its share of its concepts there minus the mean share over all 705 rooms. This follows J (21:09 Berlin): "Tell it to use the code counts as deviations from a mean normalized use. Same as the changes, 0 should be the global model." A room that uses its codes like the average room sits at 0. The deviations are not divided by their spread. With z-scores a rare theme would weigh as much as a common one, and a room with few codes would take large scores from one or two concepts.

**Step 4. The weighting.** Each block is scaled to the same total variance over the 558 defining rooms. The change block is scaled as a whole. The code block is scaled level by level, each level at one third of the block. Then the change block is multiplied by the square root of 2/3 and the code block by the square root of 1/3. So the changes hold two thirds of the total variance and the codes one third. A room is one point in 892 columns. The distance between two rooms is the Euclidean distance between their points.

Why two thirds: the changes cluster weakly and the codes strongly. At equal weight (D4a-08) the cut follows the codes and loses the forms of rooms that changed the model in the same way. At two thirds, the eight-form cut keeps 82 per cent of the structure that the changes alone show and 77 per cent of the structure that the codes alone show (`room-forms-D4a08b.md`, section 1).

**Step 5. The floor.** A room shapes the forms only if it holds 5 or more selected changes; below that its mix is too coarse. 558 rooms define the forms. The 126 thin rooms, with 1 to 4 selected changes, are placed afterwards.

**Step 6. Ward's method.** The 558 defining rooms are joined by Ward's method (SciPy `linkage`, method `ward`, on the 892 columns). Each join merges the two groups whose merging adds least to the spread within groups. The method seeks compact groups and favours groups of similar size.

**Step 7. The cut.** The tree is cut into six groups (SciPy `fcluster`, `maxclust` 6), and these are the forms. The count is J's ruling, from the counts I offered at D4a-08c; no measure chose it. The six-group cut lasts 0.178 in merge height, the third longest between four and eight (four lasts 0.392, seven 0.272). Stability on matched subsamples is about 0.21 at every count from four to eight. A shuffled null cannot be used with the codes in (`room-forms-D4a08.md`, section 3).

**Step 8. Thin rooms.** A thin room has both profiles, built the same way and scaled by the same factors. It goes to the form whose centre is nearest in the 892 columns. A form's centre is the mean point of its defining rooms.

**Step 9. The core.** A core room has no selected change, so its change profile is 0, the global model. It goes to the form whose centre is nearest in the code columns only. The full distance would add each centre's distance from 0 in the change columns. It would then favour the form whose change centre lies nearest the global model, whatever the room's codes. r/startrek (137 coded concepts) and r/n64 (22) go to E, the April Fools play. The other 19 core rooms hold 1 to 8 coded concepts each, so their placement rests on a handful of codes. The core adds 2 to 6 rooms to each form.

**What does not enter.** No canvas field, verdict, branch or outcome enters the allocation. The signatures and accounts in `room-forms-D4a08c.md` describe the forms after the cut; they place no room.

## 3. How sure the allocation is, and how to reproduce it

The forms are poles of a continuum, not separate kinds. Their stability is low (about 0.21), and many rooms lie between forms. A defining room's form is the Ward group it fell in. A thin or core room's form is a placement at the nearest centre, and it is weaker. A core room's placement rests on its codes alone.

To reproduce, run from the folder root with Python 3, NumPy and SciPy:

```
python3 out/_analysis/d4a08c_room_forms.py > out/_analysis/d4a08c_forms.json
python3 out/_analysis/d4a08d_room_tree.py > out/_analysis/d4a08d_tree.json
```

The first script builds the two profiles, the weighting and the Ward tree. It places the thin and core rooms and cuts at four to eight; `d4a08c_write.py` wrote `room-forms-D4a08c.*` from its output. The second script repeats the same construction and stops unless it gives the same six forms. It then writes the data for the tree below them (section 4). The change features are computed in `out/_analysis/d4a07_features.py`, and the ledger is read through `tools/adaptation_ledger.py`. The inputs, all in `out/`, are `adaptations.jsonl`, `adaptations-recheck.jsonl`, `adjudications.jsonl`, `adaptation-returns.jsonl`, `model/elements.jsonl`, `model/arrows.jsonl`, `assignments_final.jsonl`, `fourth/fourth.jsonl` and `dimensions.jsonl`, with `package/store/codes.jsonl`. The first script also reads `scheme_final.jsonl` for theme names and `branches.jsonl` to count the takeover rooms in its report; neither enters the distance. Ward's method has no random start, so the result is the same at every run.

## 4. The tree below the six forms, for the figure

J asked for every further cut below the six. The splits below the forms are the same Ward tree written down to single rooms. They are not named or argued.

**The files.**
- `room-forms-tree.nwk`: the tree over all 705 rooms, in Newick format. The leaves are room names, and internal nodes carry their labels. Branch lengths are differences in Ward merge height, so every room lies at the same distance from the root (8.9236).
- `room-forms-tree-linkage.tsv`: the same tree as a SciPy linkage, one row per join in order of height (704 rows). `node` is the new node's id; rooms are 0 to 704, in the order of the room table. `a` and `b` are the two nodes joined. `height` is the merge height, and `rooms` counts the rooms under the node; these four columns load as a SciPy linkage matrix. `kind` is `ward` for a join of the Ward tree and `placed` where a thin or core room hangs from the room it reached. The other columns are `label`, `ward_node` (the node's id in the 558-room Ward tree), `k_from` and `k_to` (the cuts at which the node is a group) and `placed_room`.
- `room-forms-tree-rooms.tsv`: one row per room. It gives the room's role (defining, thin or core), its counts of selected changes and coded concepts, and its form and form name. It gives its label at every cut from k = 2 to 30, and its address down to its leaf. For a placed room it adds how the room was placed, the room it reached, its distance to that room, its drawn height and whether that height was capped.

**The labels.** Above six, a group is named by the forms it holds, for example B+C. At six, the label is the form's letter. Below six, when a group splits, the larger part takes the group's label plus .1 and the smaller part the label plus .2. So a room's label at a finer cut always extends its label at a coarser cut. The address, the label of the room's leaf, holds every cut at once. For example, a room with the address C.1.2 is in C at six, in C.1 once C splits, and in C.1.2 once C.1 splits. The cut at k is the set of groups left when the joins of the Ward tree are undone from the top until k groups of defining rooms remain.

**How placed rooms descend.** A thin or core room keeps its form at six. Below six it follows the rule that placed it. At each split it goes to the part whose centre is nearer: by the whole mix for a thin room, by the code columns for a core room. It goes down to one defining room. Above six it takes the merged group that holds its form. In the drawn tree it hangs from the room it reached, at its distance to that room. Where that distance is greater than the height at which the reached room joins the tree, the drawn height is capped at that height, so heights never fall going up. 117 of the 147 placed rooms are capped, and their drawn height shows where they hang, not how near they are. 130 of the 147 meet at least one split where the two centres lie within 5 per cent of each other, so their labels below the forms are weak. I would draw the placed rooms apart from the defining rooms, for example in another colour.

**Against the four and eight forms of D4a-08c.** In `room-forms-D4a08c.tsv` the thin and core rooms were placed at each count on their own, so their groups at four and eight did not always nest in their form. Here they nest. 17 placed rooms take a different group at four (16 thin, 1 core), and 17 at eight (13 thin, 4 core). Every room's form at six is unchanged, and so is every defining room's group at every count. The nested sizes are as follows:
- At four: B+C 266, D+F 175, A 166 and E 98 (D4a-08c gave 262, 175, 170 and 98).
- At eight:
  - C (the design) 125;
  - D (keeping) 119;
  - B.1 (the chat and the scripts) 107;
  - E (the April Fools play) 98;
  - A.1 (the terms between neighbours) 96;
  - A.2 (the plan made and announced) 70;
  - F (the spot) 56;
  - B.2 (raiding) 34.

  D4a-08c gave, in the same order, 123, 113, 103, 98, 97, 82, 54 and 35.

**The top of the tree.** The first split (k = 2) separates the April Fools play (E, 98 rooms) from the other five forms (607). It is the last join, at a height of 8.92; the join before it is at 4.38. At k = 3 the other five part into A+B+C (432) and D+F (175).

**Checks** (`_analysis/d4a08d_check.py`, which reads only the written files):
- the six forms equal `room-forms-D4a08c.jsonl` for all 705 rooms;
- the cuts equal SciPy's `fcluster` at every k from 2 to 30;
- the labels nest at every cut below six;
- the full linkage is valid and monotone, and its cuts by height give the table's groups at every k from 2 to 30;
- the Newick holds each of the 705 rooms once, with no negative branch length.

## 5. The earlier allocations, in order

Each cut compared rooms, was an addition after the 35 branches, and sits in its own files, unchanged. Each was superseded by the next on J's word through the handler; none was withdrawn. Tier history moves 238 to 313 named their forms. Sizes are in rooms, in the order of the forms' letters; each ratio is the largest form against the smallest, the core aside.

**D4a-05** (moves 238 to 245; `room-forms-D4a05.*`, script `d4a05_room_tree.py`).
- *Compared:* the selected changes only. Each line counted once at its third-order theme, its fourth-order theme and its dimension, at its own lift. A changed arrow counted at the theme of the room's evidence, so which arrow it changed did not enter. The report says an arrow counted "through the third-order theme of its source"; the script counted it at the line's own lift, as the D4a-07 report says. Shares were taken within each level, and third-order themes changed by one room only were dropped. The distance was the Hellinger distance, the three levels counting equally.
- *Placed:* all 684 rooms with a change, by Ward's method; a room's form was its Ward group. The 21 rooms with no change stayed apart as the core.
- *Count and sizes:* eight, by the logged rule: the highest silhouette with a bootstrap stability of 0.5 or more, else the most stable count. Every count fell below 0.5, so the most stable count was taken. The sizes were 152, 119, 103, 88, 83, 69, 42 and 28, and the core of 21 (ratio 5.43).
- *Superseded because:* the smallest form was built from thin rooms, the ratio was above J's bound of 3, the count rule favoured more groups, and J's placement rule had not been applied. I proposed these fixes in the interview, and J replied "Go ahead this sounds good" (19:50 Berlin). The 32 sub-forms declared below the eight (moves 246 to 277) were withdrawn by move 278, because the split below waited for J's talk (18:36 Berlin).

**D4a-06** (moves 279 to 286; `room-forms-D4a06.*`, script `d4a06_room_forms.py`).
- *Compared:* the same as D4a-05, with the floor: only the 558 rooms with 5 or more selected changes shaped the forms.
- *Placed:* by J's rule, taken literally. Each room went to the form whose signature holds most of its selected changes, by count. A signature is the fourth-order themes that a form's defining members change at 1.5 times the defining population's share or more, in a third of them or more. A tie went to the nearest centre and was listed. A room with no change on any signature went by its whole mix. The core stayed apart.
- *Count and sizes:* the gap between merge heights carried five. Stability on matched subsamples against a shuffled null carried eight. By the logged rule I carried eight and gave five in full. The sizes were 135, 84, 89, 50, 62, 64, 124 and 76, and the core of 21 (ratio 2.70).
- *Superseded because:* J asked why arrows were not used (20:35 to 20:37 Berlin): "The arrow can work at any level. Just as the T3 are T4 and Ds."

**D4a-07** (moves 287 to 294; `room-forms-D4a07.*`, script `d4a07_room_forms.py`).
- *Compared:* the change profile of step 2, with arrows and link-op lines as links at every level, and the floor of 5.
- *Placed:* by the whole mix. A defining room stayed in its Ward group, and a thin room went to the nearest centre. J's literal rule was reported beside it; under that rule 307 rooms would move. The core stayed apart.
- *Count and sizes:* eight; the gap and the stability agreed. The sizes were 148, 159, 87, 64, 60, 56, 59 and 51, and the core of 21 (ratio 3.12). The largest form was the middle, B: 159 rooms with a weak signature.
- *Superseded because:* J asked to use the code counts as well (21:05 Berlin): "How about using the code counts, dimensions for example, as well?"

**D4a-08** (moves 295 to 299; `room-forms-D4a08.*`, script `d4a08b_room_forms.py`).
- *Compared:* the change profile of step 2 and the code profile of step 3, at equal weight by total variance. A first run on Hellinger distances between code shares was superseded by J's 21:09 message before it was delivered.
- *Placed:* by the whole mix of both blocks. The core stayed apart.
- *Count and sizes:* five, by the gap. Stability against a shuffled null could not choose, because the shuffled copies came out more stable than the data. The sizes were 182, 174, 133, 113 and 82, and the core of 21 (ratio 2.22).
- *Superseded because:* J asked which cut I would stand behind (21:24 Berlin). At equal weight the codes took over. The five forms explained 0.271 of the code variance and only 0.051 of the change variance. The forms of rooms that changed the model in the same way, machine hands and the spot, dissolved.

**D4a-08b** (moves 300 to 307; `room-forms-D4a08b.*`, script `d4a08w_room_forms.py --w 0.6667`).
- *Compared:* both profiles with the weighting of step 4: changes two thirds, codes one third.
- *Placed:* by the whole mix. The core stayed apart.
- *Count and sizes:* eight, chosen on substance: at eight every form has a change signature, so no form is a middle. The sizes were 121, 112, 102, 96, 96, 77, 49 and 31, and the core of 21 (ratio 3.90).
- *Superseded because:* J asked for fewer forms, asked why the core was still alone, and found the smallest forms small (22:00 Berlin): "Also 31, 21, 49 is quite small."

**D4a-08c** (moves 308 to 313; `room-forms-D4a08c.*`, script `d4a08c_room_forms.py`). The cut.
- *Compared and placed:* as in section 2, with the core placed by its codes.
- *Count and sizes:* six, with four offered as a one-line summary. The sizes are 166, 141, 125, 119, 98 and 56 (ratio 2.96).
- *Ruled:* J, 22:18 Berlin: "6 it is."
