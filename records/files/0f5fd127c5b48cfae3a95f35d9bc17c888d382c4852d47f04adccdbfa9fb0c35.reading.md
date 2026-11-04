# Handback, stage D4: the taxonomy from adaptations

Legs D4a-01 to D4a-03, 24 and 25 October 2026. The taxonomy is read off the adjudicated ledger (the re-check, all 705 rooms), adapted against the model frozen at D3 (46384686…). The model is unchanged: the P05 and A11 amendments of D4a-01 were reverted (QD4-001) and are held proposals. The detail and the scripts are in `tree-D4.md`, `notes-D4.md`, `branches.jsonl`, `forms/`, `crosslinks.jsonl`, `chunk-share-D4.*` and `projections-D4.jsonl`.

## The claim

The rooms adapted the model in many small shared ways, not into a few forms. 35 branches hold 476 of the 705 rooms, and they overlap: 759 cross-links join 348 pairs of branches that do not nest. A room makes several element-level changes at once. The branches are facets of those changes, not exclusive types. The comparison built without the ledger agrees in its own way: its partition beats its null but barely separates the rooms (silhouette 0.024), does not survive a change of distance, and largely sorts the rooms by how much the coders coded. What the branches say is specific:

- **Rooms add work the model does not state.** They administer the April Fools play (F01). They carry out deals: they move work, retarget scripts and relay terms (F10). They keep the shared instruction current, because a stale template or bot target undoes their own new work (F15, F33, F08). They keep the chat open (F16). They make help wait on their own work and spare hands (F22, F28). And they carry on by renewing the work elsewhere, often before the close (F11 to F14).
- **They limit P05's added clause.** In design, at the border and in keeping (F07, F26, F27), informed members reject a planned change, or the record does not show the untold keepers the clause needs.
- **They show two links the model lacks.** After a move the room builds again (F09). After a celebration it defends again (F32).

**The room that best supports it: fivenightsatfreddys.** It is in eight branches across seven elements. It runs a takeover as a temporary regime (F01, F02), does not show the telling clause at its design (F07), builds again after a move (F09), carries out a deal (F10), carries on past the close (F23), depends on chat access (F29) and hosts by one-off permission (F31). One room, many facets, no single form.

**The room that most threatens it: ainbowroad.** It is the largest room in no branch (2,054 concepts). Its shared changes sit on keys held by fewer than 20 rooms, which the pass did not read. A room can hold rich organizing that the branches do not show.

**The condition between them** is whether a room's change lands on a node that many other rooms use. Where it does, the room appears in a branch, often in several. Where its changes are its own, or shared by only a few rooms at one node, it appears in none. The branches are a census of common changes, not of the rooms' organizing.

## The return value

| What | Count |
|---|---|
| Branches | 35: 14 at the fourth order and 11 at the third (top level); 10 subforms, all at the third order |
| Branches by kind (majority of their lines; not relied on for add-condition, add-step and restrict) | elaboration 7, specification 28 |
| Subforms | F02 to F06 under F01; F12 to F14 under F11; F18 and F19 under F17 |
| Cross-links | 759 lines over 348 pairs of branches that do not nest |
| The unadapted group | 0 (no room returned `none`) |
| Rooms in no branch | 229, each named in `tree-D4.md` with its count of smaller keys |
| The four counts against n_analysed | 476 in a branch + 0 unadapted + 229 in no branch + 0 unreturned = 705 |
| Tree-likeness | delta 0.4227 (Monte Carlo SE 0.0020), combined level-3 matrix, 20,000 quartets |
| Trees drawn | the average-linkage dendrogram and the leaf-to-root view, as views of the distance; the dendrogram is a chain with no partition; no tree of forms, since the branches overlap |
| Comparison engine | `chunk-comparison-v1.1` (departure, QD4-002) |
| Empties | 0 |
| a and the median own-data weight | a = 1.0; 0.990 with all rooms, 0.991 without the low-information rows |
| Rand indices among the three distances, at the carried k | Ward/CLR against Jaccard -0.007 and Hellinger -0.008 (all rooms); 0.014 and -0.005 (without low-information) |
| Smoothing sensitivity at the carried k | a/10 0.145, 10a 0.164 (all); 0.143 and 0.556 (without) |
| The third tier's sparsity | 195 columns, 13.52 nonzero per room |
| The tier verdict | dimension ARI 0.110 and third-tier ARI 0.170 at k 4 |
| The volume verdict | eta squared of log concepts by cluster 0.255, at the 100.0th percentile of the permutation null (null maximum 0.026); the clusters largely sort the rooms by size (`_analysis/d4a03_volume.txt`) |
| k carried | 4 with all 705 rooms (worst margin +0.052, silhouette 0.024); 2 without the 79 low-information rows, 626 rooms (worst margin +0.099, silhouette 0.097) |
| Clusters | VA 176, IT 292, TX 155, CH 82 |
| Residue share per room (QD4-002) | 199 rooms hold residue concepts; median 0.000; 39 rooms at 0.10 or more, 7 at 0.30 or more |
| Feature space | **no verdict, canvas field or branch entered the comparison**; it reads the concept store, placements, tiers, dropped cases and the prior |

## The branches, in the order cut, with the verdict and canvas percentiles

Verdicts are projections.py's map (my last ruling at D3, else the readers' agreed verdict), so the D3 versions are mixed. Each row: id, parent, level, members; composes, with residue, does not compose, cannot tell; the does-not-compose percentile; the median area and its percentile. The canvas percentiles follow room size (`tree-D4.md`).

| id | name | parent | level | n | verdicts | dnc pct | median area (pct) |
|---|---|---|---|---|---|---|---|
| F01 | the play administered: steps that test, police, end and convert the April Fools frame | - | fourth | 103 | 54 / 49 / 0 / 0 | 43.5 | 610.5 (67.1) |
| F02 | the takeover run as a temporary regime | F01 | third | 33 | 18 / 15 / 0 / 0 | 47.4 | 789.0 (89.0) |
| F03 | the joke tested: members check a claim's truth | F01 | third | 18 | 9 / 9 / 0 / 0 | 48.8 | 349.0 (9.4) |
| F04 | the licence policed: objections to the play, its limits and its end | F01 | third | 13 | 4 / 9 / 0 / 0 | 49.0 | 957.5 (88.8) |
| F05 | the styling ended: ordinary use restored | F01 | third | 12 | 6 / 6 / 0 / 0 | 49.0 | 706.5 (67.8) |
| F06 | the joke kept: a request that its change last | F01 | third | 8 | 5 / 3 / 0 / 0 | 49.3 | 1535.25 (95.0) |
| F07 | the telling clause not shown at the design: informed members reject the planned change | - | fourth | 59 | 21 / 38 / 0 / 0 | 45.9 | 770.0 (95.3) |
| F08 | machine hands kept on one target: installing, teaching and updating every runner | - | third | 50 | 21 / 29 / 0 / 0 | 46.6 | 821.5 (96.2) |
| F09 | the move returns to building: relocation followed by renewed construction | - | fourth | 54 | 22 / 32 / 0 / 0 | 45.5 | 464.25 (16.2) |
| F10 | a deal carried out as work: prepared in the room, then implemented and relayed | - | third | 38 | 16 / 22 / 0 / 0 | 47.4 | 696.0 (77.7) |
| F11 | carrying on as renewed work, begun before the close | - | fourth | 43 | 18 / 25 / 0 / 0 | 46.7 | 985.5 (99.2) |
| F12 | the spine restarted on another canvas | F11 | third | 22 | 9 / 13 / 0 / 0 | 48.6 | 777.0 (82.8) |
| F13 | the work remade in other media, often before the close | F11 | third | 9 | 2 / 7 / 0 / 0 | 49.2 | 3202.0 (100.0) |
| F14 | the mark adopted as the room's emblem while it is still placed, damage included | F11 | third | 7 | 4 / 3 / 0 / 0 | 49.5 | 588.0 (50.7) |
| F15 | the plan kept current: correcting, updating and re-circulating the template | - | fourth | 42 | 20 / 22 / 0 / 0 | 46.8 | 554.75 (39.0) |
| F16 | the chat kept open: invitations renewed, entrants screened, outcomes relayed to the thread | - | third | 35 | 13 / 22 / 0 / 0 | 47.8 | 1127.5 (99.5) |
| F17 | the marking provisional and contested: success judged and credit disputed while the work goes on | - | fourth | 36 | 12 / 23 / 0 / 1 | 47.0 | 601.25 (51.9) |
| F18 | success judged while upkeep continues | F17 | third | 15 | 4 / 11 / 0 / 0 | 48.9 | 462.0 (28.9) |
| F19 | credit contested during the work | F17 | third | 14 | 6 / 7 / 0 / 1 | 49.1 | 563.0 (45.4) |
| F20 | the close as news: late arrivals told that placement has ended | - | third | 10 | 2 / 7 / 0 / 1 | 49.5 | 839.0 (77.5) |
| F21 | the canvas call not a joke: the April Fools frame kept apart from the canvas work | - | fourth | 32 | 21 / 10 / 1 / 0 | 97.4 | 406.0 (10.8) |
| F22 | help conditional on the helper's own work and spare hands | - | fourth | 30 | 13 / 17 / 0 / 0 | 47.6 | 360.5 (6.6) |
| F23 | the close scoped to the original canvas: continuation renewed, uncertain and contested | - | fourth | 30 | 8 / 22 / 0 / 0 | 47.6 | 2096.0 (100.0) |
| F24 | machine hands debated, not shown placing | - | fourth | 27 | 12 / 15 / 0 / 0 | 48.0 | 655.0 (69.7) |
| F25 | carrying on in talk: proposals and single attempts, not shown taken up | - | fourth | 27 | 15 / 11 / 1 / 0 | 98.0 | 1237.5 (99.1) |
| F26 | the telling clause not shown at the border: informed members contest the terms | - | third | 23 | 10 / 13 / 0 / 0 | 48.4 | 1008.0 (95.9) |
| F27 | the telling clause not shown in keeping: interference seen, its cause and loss not | - | fourth | 27 | 9 / 18 / 0 / 0 | 48.0 | 1389.5 (99.4) |
| F28 | help at the border conditional: on the home work, the terms and harm to a third room | - | third | 22 | 11 / 11 / 0 / 0 | 48.6 | 1005.5 (96.2) |
| F29 | the chat's reach conditional: access, and the return of decisions to the thread | - | third | 25 | 8 / 17 / 0 / 0 | 48.2 | 1800.0 (100.0) |
| F30 | the chat seen only through its invitations and returned reports, not its choices | - | third | 24 | 7 / 17 / 0 / 0 | 48.2 | 836.5 (88.0) |
| F31 | hosting as one-off permission: requests and leave, no standing host rule | - | third | 22 | 12 / 10 / 0 / 0 | 48.6 | 663.25 (67.0) |
| F32 | the marking returns to keeping: celebration followed by renewed defence | - | third | 21 | 5 / 16 / 0 / 0 | 48.5 | 1158.0 (98.0) |
| F33 | the plan kept current while the design settles | - | fourth | 23 | 10 / 13 / 0 / 0 | 48.4 | 633.0 (61.0) |
| F34 | the design sized to the hands: scale and detail conditioned on crew, upkeep, space and colours | - | fourth | 22 | 9 / 13 / 0 / 0 | 48.6 | 442.0 (22.7) |
| F35 | the call made workable: answers ask for a task, and callers supply it | - | third | 18 | 8 / 10 / 0 / 0 | 48.8 | 374.25 (12.8) |
| VA | cluster | - | - | 176 | 64 / 112 / 0 / 0 | 38.4 | 1016.0 (100.0) |
| IT | cluster | - | - | 292 | 165 / 116 / 1 / 10 | 79.8 | 312.0 (0.0) |
| TX | cluster | - | - | 155 | 73 / 82 / 0 / 0 | 39.3 | 642.0 (84.2) |
| CH | cluster | - | - | 82 | 28 / 54 / 0 / 0 | 44.3 | 914.25 (99.8) |

## The held proposals (QD4-001; never served, not re-checked)

- **P05 (move 198; history lines 173 to 176; reverted by move 203, line 181).** The statement would gain: "This holds where the keepers can learn of a planned change only by being told, and no informed member holds it." Status bounded. The bound names completeanarchy, polska, satania, halo, bangtan and thesilphroad (the shape read) and armok, maryland and oneshot (informed members), with their nine re-check lines. The branches F07, F26 and F27 hold 108 rooms where the clause holds only in part.
- **A11 (move 199; history lines 177 to 180; reverted by move 203, line 182).** The arrow from P02 to P04 would be withdrawn under rule 14: it never beat its null; template first is nearly as common as the transition; the failure clause stands alone in 117 rooms, 31 of them talk only.

## Questions, departures and defects

- **QD4-001** (answered): the amendments were reverted, and the model is the D3 version.
- **QD4-002** (answered): the comparison engine was patched to v1.1; declared as a departure (`departures.jsonl` line 10).
- **For the operator.** `validate.py --open D4` reads the startup packet's pattern name `rooms-x-adaptations.<level>.<kind>.tsv` literally. `stage_D4.py` resolves branch keys against elements only, so arrow keys, the largest change keys in this ledger, cannot key a branch. Its member-name check is a substring check: the room 'de' forbids 'decisions' and 'outside'.

## Licences exercised (METHOD.md)

- **The count set by kinds, not by a head's capacity:** exercised. The branches number what the keys and their lines support (35), under rules written before the first cut; the cuts stop at a declared key size.
- **An in-sample return in Eisenhardt's spirit:** its ledger is the taxonomy's material; the taxonomy cannot corroborate it (section 7).
- **Langley's strategy:** not exercised at D4; the two links the model lacks wait for an order test.
- **Gioia's explosion at the front end:** not a D4 licence.

## Slips

- At D4a-01 the session ended inside one command; its log line and snap were written, and the empty F04 dry run was repeated.
- F06's form lists the arrow A12 among the elements its members carry unchanged; the forms are written once.
- Two spec names (F16, F30) were changed before writing, after the member-name check refused them.
- At D4a-03 three Edits to this handback's script ran in one turn, against the rule; each landed on a separate string.
