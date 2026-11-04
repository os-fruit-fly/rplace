# Handback, stage C2: the model and the loop

Written at C2d-02, 2026-10-14 (UTC), at the last closing pass of stage C2. The model rests on pass 5. Its files are `model/elements.jsonl`, `model/arrows.jsonl`, `model/loops.jsonl` (empty), `model/history.jsonl`, `model-p5.md` and `model/story-p5.md`. The tier is `fourth/fourth.jsonl` and `dimensions.jsonl`, described in `structure-p4.md`. The concept is in `concept.md`. The record of every step is `notes-C2.md` and the diary. Every earlier version is kept: `model.md`, `model-p2.md` to `model-p4.md`, `model/story-p1.md` to `model/story-p4.md`, `structure.md`, `structure-p2.md`.

**What the counts here license.** The order counts are counts of coded turns, against a null that holds each room's coded turns and hours fixed. They say what the coders' record shows in order, not what the rooms did when nobody coded it. The story verdicts are mine alone.

## The claim

**Strangers on the canvas organized by calls answered and works kept, and the relations between rooms grew out of keeping the work.** A member starts a mark, calls gather hands around it, the hands build, and once the mark stands, keeping it becomes the work. Keeping it brings the room up against its neighbours: it talks with them, settles borders, trades help, and joins coalitions under attack. A call can also turn hands against a rival's work, and most such calls are answered inside the room by refusal, restraint or a truce. A room that judges it has too few hands moves and keeps calling. The calls fill the host sub, and the sub draws a line around them. The close runs in order: celebrated, recorded, carried on. Placement ends at hour 73. In some rooms a tie the members had before the canvas (a league or school rivalry, a nation's history, an ideology, lore) names the rival in the same turn as the attack. That is a claim in the rooms' words, untested for order.

- **The room that best supports it: day9,** one of the three within-case rooms, read at all five passes and told at passes 2 to 5 under four stories (at pass 1 every room carried a residue). It runs the spine from a call to a built work, loses its border at hour 48, moves within two hours, calls members to a new plan, and finishes the new work at hour 53. stevenuniverse (pass 3) is told whole from its first call to its record.
- **The room that most threatens it: thebluecorner,** a colour faction the canvas gathered. Its faith names its rivals ("We need to attack back. Blue the Purple Corner!" [thebluecorner/c0230]), rules on guests by vote and by fit with blue, and splits the faction over art on a blue backdrop against a pure blue corner. greenlattice, purplecorner and orderofthebluecorner show the same. The model tells their steps from their first post. It does not tell their faith.
- **The condition that separates them** is what decides whom a room fights and whom it admits. Where the work decides (a readership brings its topic's picture and keeps it against the canvas), the model tells the room. Where a tie from before the canvas names the rival in the attack turn, the claim tells it in the room's words. Where a body's faith or a host's rule picks rivals and guests, the model does not reach it, and that is stated as a boundary at the return.

## The counts

The next table gives the three story counts per pass, with what the stopping rule watches. Each pass's rooms were drawn by a rule and a seed before any was opened.

| pass | rooms read | told | told-with-residue | not-told | tier events | arrows changed |
|---|---|---|---|---|---|---|
| 1 | 20 | 0 | 20 | 0 | 35 | 12 |
| 2 | 32 | 14 | 18 | 0 | 7 | 10 |
| 3 | 32 | 16 | 16 | 0 | 1 | 2 |
| 4 | 32 | 11 | 21 | 0 | 12 | 1 |
| 5 | 35 | 16 | 19 | 0 | 0 | 0 |

Told-with-residue rose once, at pass 4 (16 to 21). By J's ruling on QC2-002, from pass 5 the criterion is a guide and a rise is not a failure. 67 distinct rooms were read in 151 readings. No room was not-told at any pass.

The next table gives the model as it stands, with where each figure is recorded.

| what | figure | where |
|---|---|---|
| elements | 28: 20 processes, 4 conditions, 2 claims, 2 roles; 25 stand; 3 candidates (a quarrel carried in, membership carried in, hosting) | `model/elements.jsonl`; `c2d2_model_counts.py` |
| arrows | 20, all in the model: 18 order, 2 transition; 8 strong, 6 fair, 6 thin; 18 beat the null | `model/arrows.jsonl`; `model-p5.md` |
| theorised arrows | 2: the template settling a design (order at chance) and the one-line answer to a call (never counted) | `model-p5.md` |
| loops | none grounded | `model/loops.jsonl` |
| findings | 13 (20 lines) | `findings.jsonl` |
| tier | 28 fourth-order themes (13 borrowed, 14 adapted, 1 coined) in 8 dimensions (6 adapted, 2 coined) | `fourth/fourth.jsonl`, `dimensions.jsonl` |
| third-order themes unused | 55 of 197 without the claim; 41 if the claim's themes count as used | `c2_unused_t3-p4.md`, `c2_unused_t3-p5.md` |
| instance audit | 48 transitions checked six ways: 34 pass, 14 fail, none swapped; 19 of 20 arrows keep a passing transition | `c2d_instance_audit-p4.txt` |
| connection statement | "in a room carrying both, the first concept of FROM comes before the first concept of TO"; 500 shuffles within each room, seed 20261014 | `notes-C2.md`, pass 1 |

## The reviewer

One hostile reader, once (C2b, C2c), on Opus. It found nine errors: order 3, quote 1, contradiction 4, count 1. Six were accepted in full, two in part, one refused (A01's instance read as a coordinate). The fixes went into the arrow ledger at C2c and into the pass 4 texts. Its rival partition sits at adjusted Rand 0.661 against my tier. It agrees where the model has arrows (the spine, the contest, the close) and disagrees where the residues are (membership carried in, hosting, the host sub). Its hosting group was accepted as a recut at pass 4. It also put recruiting canvas visitors and drawing lapsed fans back beside the call. At pass 5 that group is the residue of six rooms (below).

## What the passes changed, and which pass the model rests on

- **Pass 1:** 20 elements, 12 arrows from the pair list, the within-case rooms, the one-line enrolment as the concept.
- **Pass 2:** exchange between rooms, the contest carried on in talk, coalitions; Contention cut as an eighth dimension.
- **Pass 3:** the host sub's line around canvas talk; the idiom rule for membership.
- **Pass 4:** two recuts, each by a rule written first. Hosting left Meta-organization for Territoriality, since hosting is a claim on space. The land's flag and emblems left Flagging the nation for Collective representation, since they are the mark's content. The coalition arrow recounted on coalitions alone.
- **Pass 5:** the claim on F-013, and two boundaries stated at the return: colour factions the canvas gathered, and hosts ruling on guests.

The model rests on pass 5. I keep each pass 4 change because I believe it, for the reasons in `notes-C2.md` (pass 5, declaration 2). Pass 4's own section discarded those changes under the criterion as judge. That discard is reversed. Nothing was dropped at pass 5.

## What I am sure of, what I am not, and why

**Sure.** The spine holds in every room read: each showed at least part of it, and every residue sat beside it. The two boundaries were residues at passes 3, 4 and 5 under three stories, and no test of hosting beat its null. Membership carried in does not come before the attack more than chance (F-011). In 10 turns in 7 rooms it names the rival in the attack turn itself (F-013), which is why an order count cannot see it.

**Not sure.** The claim's candidates came only from the residue clauses of 16 rooms, so its reach is unknown. I judged sweden's and placeDE's attack calls as naming a national rival without the members' tie in words; another reader could count them. Visibility returns was noticed partway through the pass 5 reading. The claim is untested for order, and the reverse order (attack first, membership told after) was printed at pass 4 and never tested. The verdicts have no second reader.

## For stage C3, and the stages after it

- **Visibility returns.** Five of the 11 fresh pass 5 rooms carry it as their residue: parahumans, TheAdventuresofTintin, shishamo, hunterxhunter and luciomains. scp carries it too. The mark brings readers to the sub or back to the topic, and the room talks about the newcomers. It is a fourth-order theme the model does not use, and it was never tested as an element.
- **The two boundaries for the return (D1 to D3):** colour factions the canvas gathered (greenlattice, orderofthebluecorner, purplecorner, thebluecorner), and hosts ruling on guests (catalunya, placeDE, smashbros, sweden).
- **Membership outside the claim:** starcitizen, texans, totallynotrobots and sweden. Membership picks an alliance, a taunt or the work, not the attack's target.
- **The claim untested for order.** The membership candidate stays a candidate. `in_model` is false for Frame bridging and Flagging the nation, though the claim names them; pass 2's rule would set it.
- **The relationship I most expected and could not ground:** attribution as the hinge between restraint and attack. Its order holds at chance (0.452 against 0.456) and its order to attack runs reversed.
- **Recalled sources** for the constructs and dimensions stand as at C1, for stage C3 to verify or withdraw. The concept, the one-line enrolment, is chosen and stays recalled against the literature.
- **The three strongest arrows are partly constitutive** (the host's line, the refusal of an attack call, the call before building), and the record drops most uncoded turns. The artefact arguments are in `model-p5.md`.

## The licences exercised, and those not

- **An in-sample return in the spirit of Eisenhardt's replication logic: exercised.** Each pass's story was read against rooms drawn by rule and seed, the within-case rooms every time, and every arrow was sampled against rooms outside its own.
- **Langley's strategy, declared: exercised in part.** Narrative (the stories) and temporal bracketing (hour 73, and the host's line counted before it) were used, with grounded theory for the elements. Visual mapping was not used; the figure is stage C5's.
- **The count set by kinds: exercised.** The number of elements followed the kinds of rooms the story could not tell (`model-p5.md`, "Why 25"), and the tier kept 28 fourth-order themes because the material carries that many.
- **Gioia's explosion at the front end: not exercised here.** It belongs to stage B1.
- **J's rulings:** QC2-001 (the handler, under J's delegation: serving sections of the model file is acceptable) and QC2-002 (the criterion is a guide; the claim carried untested for order).
