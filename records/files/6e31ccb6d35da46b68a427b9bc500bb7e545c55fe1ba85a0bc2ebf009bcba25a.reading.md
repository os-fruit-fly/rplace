# Notes, stage C2 (the loop)

## The criterion, written before pass 1 (section 1)

I will prefer a later pass to an earlier one only when four things hold together. First, the later story tells more of the rooms drawn against it in their own terms: fewer `told-with-residue` and `not-told` verdicts among rooms drawn by a rule written before any room is opened, the three within-case rooms and one room from each size quartile among them, with no element loosened to make a room fit. Second, more of its in-model arrows rest on an instance a reader can be shown (a participant's words through `cite.py`, or two coded turns in one thread in order), each with `mechanism_fails_if` written before its strength and each sampled against rooms outside its own where it could fail. Third, its tiers stay a step up in abstraction: no fourth-order theme or dimension that renames its members, and every dimension answers a question none of its members answers alone. Fourth, it reaches the contract's four things (how a scattered readership becomes able to act, how it settles what to act on, what sends it back to the beginning, what it leaves behind) with an element for each or a stated absence. A pass that adds elements or arrows without improving the first two is not preferred, however much it explains on paper. A pass in which `told-with-residue` rises is a stopping failure, and its residues are the next pass's material. A tie goes to the earlier pass, so the loop does not ratchet. Every pass is numbered and every version kept (`structure.md` then `structure-p2.md`, `model.md` then `model-p2.md`, `model/story-pN.md`); the last pass says which one the model rests on. The stopping rule is contract section 6's guide: two consecutive passes with no `tier_history` event, no arrow added, bounded, demoted or withdrawn, and no story sentence naming an arrow or element changed.

## Pass 1 (C2a-01)

### Before the pass

- **Read:** `METHOD.md` whole; the read tier (Gioia, Corley and Hamilton whole); the contract's section 1; `prior.md`; `contrast.md`. The explanation literature stays shut until C3.
- **The ledger** (`mem.py pairs`, third, fourth and second level). 62,838 coded turns answer coded turns. Most stay inside one theme. Across fourth-order themes, the rooms with a transition run, for example, Completion ritual then Repair work (274), Repair work then Negotiated order (264), Mobilization then Repair work (195), Mobilization then Collective representation (155), Collective representation then Stigmergy (146), Mobilization then Stigmergy (127). The ledger is elapsed order: "a reply is a reply: posted after, not caused by". It is never, on its own, an arrow.
- **What the handler's interview carried in** (a fork; nothing from it reached the run). My own words there, set beside the stage file here: decided order looked rare and mostly real; `also_present` read as a second layer, never pooled; FP-04 and FP-08 as conditions, never weights; where to start the model: the spine from calls to emblem, trace and template, then repair, then the close, ordered by the clock and grounded in cited concepts, then the hinge from attribution to restraint or contention; test T3-076 first among the forced placements, then T3-141 with FP-03. I take these as working hypotheses to test, not as findings.

### The three within-case rooms, named before any was read (section 4)

They were drawn by `out/_analysis/c2_within_case_pick.py`. All three come from the middle half of rooms by `items_in_window` (156 to 2,770, the held-size band of `contrast.md`, 353 rooms), so size does not pick them, and each was drawn with `random.Random(20261014)` from its candidate list.
- **The ordinary room: ubc.** Rule: its placements reach all four of the most widely reached fourth-order themes (Repair work, Completion ritual, Mobilization, Collective representation), and its organizing end (stage A1) lies inside the corpus's interquartile range, h68.70 to h72.93. 53 candidates. ubc has 1,475 items and 45 coordinating turns, and its organizing ends at h72.75.
- **The room whose form the scheme could not have predicted: ultrahardcore.** Rule: the share of its placed lines carrying a third-order theme placed in fewer than ten rooms is in the top tenth of the band. Such a room's form rests on kinds the scheme holds only thinly. 36 candidates. ultrahardcore has 918 items; 2 of its 10 placed lines carry such a theme.
- **The room that stopped early: day9.** The first rule (organizing end before hour 24, with five coordinating turns or more) found no room in the band. I restated it before any room was read: an organizing end in the lowest tenth of all 705 rooms (at or before h58.79), with five coordinating turns or more. 14 candidates. day9 has 361 items and 23 coordinating turns, and its organizing ends at h53.28.

I read each through `mem.py` with placements hidden (`--blind`), from its concepts, forest and timeline, and write them with no theme above the second tier.

### Part A, pass 1: the tiers

- **The fourth-order tier: 28 themes, no recut at pass 1.** The material carries 28 because each answers a question its members do not answer alone, and none renames its members (stage C1, pass 10; `fourth/fourth.md`). At this pass each line gained `changed`, `mistaken_for`, `in_model` and `pass`, with the old line kept as `was` in `tier_history.jsonl` (28 lines). 17 are in the model and 11 are not. The forced placements are tested against rooms before any recut. Pass 1's story rooms point to two places a recut may come: attack as a room's own work, and exchange between rooms (below).
- **Seven dimensions**, cut one at a time with their pairwise separation (7 `tier_history` lines; snaps C2-move-*-1 to 7, each named merging or relating): D01 Critical mass, D02 Coordination without command, D03 Maintenance, D04 Order without law, D05 Collective identity, D06 Host framing, D07 Imprinting. Five are adapted, two coined. Each gathers two fourth-order themes or more and answers a question none answers alone. Seven, because the four things and the material split there: the hands, their alignment, the keeping of the work, the order between rooms, the membership carried in, the host's frame, and what is left.
- **Part A's return** is at the head of `structure.md`. Third-order themes per fourth-order theme and fourth-order themes per dimension are in its first table. The two dimensions I am least sure of are Maintenance and Host framing (two members each). The rejected alternative is a separate contention dimension, now open as `_questions/contention-dimension.md`. 72 of 72 coder conflicts reached `structure.md`. The fourth-order theme I am least sure of is Stigmergy.
- **Consistency, computed** (`structure.md`): every third-order theme placed in `assignments_final.jsonl` is defined in `scheme_v2.jsonl` (194 placed, 197 defined). Each sits in a fourth-order theme's members or in the unpicked list (T3-017, T3-133). Every fourth-order theme sits in a dimension's members (28 of 28). Every dimension used is defined. The three counts sum to 705 for every third-order theme, under the opportunity gates declared before counting.

### The onset contrast, pass 1 verdict

The next table repeats the shares that decide stage A1's expectations at held size (`items_in_window` 156 to 2,770). The late side has 12 rooms at held size, so every late share is thin.

| what | held early (n=41) | held late (n=12) |
|---|---|---|
| choosing a canvas spot | 0.22 | 0.33 |
| asking a host for space | 0.05 | 0.08 |
| relocating after losing the spot | 0.20 | 0.00 |
| extending the room's work | 0.27 | 0.25 |
| defending the work against attackers | 0.66 | 0.42 |
| calling to deface rivals' work | 0.41 | 0.08 |
| trading taunts with rivals | 0.15 | 0.08 |
| Host framing (dimension) | 0.83 | 0.25 |

- **First expectation** (late rooms organize around finding room; early rooms around claiming, enlarging and holding): it held in part. Late rooms choose a spot more often. Asking a host for space is rare on both sides. The extension gap vanishes at held size, but the defence gap stays. Relocation runs against the expectation: early rooms move, and no held late room does.
- **Third expectation** (early rooms name rivals and keep fights going; most of this was expected to vanish at held size): it did not vanish. Calls to deface rivals' work stay at 0.41 against 0.08, and taunts at 0.15 against 0.08.
- **Host framing** (0.83 against 0.25) differs largely by construction. Late rooms first wrote after hour 48, when the April Fools frame was over.
- **On the arrows:** the late side holds A04 in 6 of 15 rooms (talk with neighbours before upkeep, a bound) and A08 in 8 of 15. A06 and A09 have three late rooms each, too few to read.

### Part B, pass 1

`concept.md`: the one-line enrolment (FP-01), chosen provisionally. It is in the model as P15 and arrow A12, never counted. Its nearest concept is slacktivism, which substitutes for action; the enrolment comes before action and is the room's head count. It appears in 337 of 705 communities under the form pass's declared gate, as a floor. The candidate I came closest to choosing instead is organizing without decided order (C01). The rejected candidates are kept in the file.

### Part C, pass 1: the model

- **20 elements:** 15 processes, 2 conditions, 1 claim, 2 roles. 17 are named for what they do. Why 20: the four things and the concept need 17 (`model.md`, "Why 20"). Three more (attribution, attack, the envoy) carry the hinge the interview asked me to test; the hinge was not grounded, and the within-case rooms need the three elements.
- **12 arrows:** 10 order and 2 transition. 5 are strong, 3 fair, 4 thin. All are grounded `codes-read`, and each rests on quotes and a transition in one thread. 10 beat a permutation null (500 shuffles within each room, seed 20261014). A11's order is at chance, so it is kept as a transition. A12 is never counted. Connection statement: "in a room carrying both, the first concept of FROM comes before the first concept of TO".
- **Theorised arrows**, listed apart: A11 and A12. The thin arrows that beat the null are A05 and A10. `model.md` shows the model without each set.
- **Tested and not grounded** (`model.md`, "Looked for and not found"):
  - attribution before restraint (0.452 against 0.456) and before attack (0.194 against 0.408, reversed);
  - attack before repair (0.444 against a 95th percentile of 0.449) and before a move (0.561 against 0.610);
  - calls and building after a move, below chance (finding F-002);
  - doubt before calls (0.175 against 0.352, reversed);
  - machine hands before upkeep (0.202 against 0.375, reversed; replaced by A06).
- **No loop is grounded.** `model/loops.jsonl` is empty.
- **The relationship I most expected and could not ground:** attribution as the hinge between restraint and contention.
- **Findings at pass 1:** F-002 to F-006 (`findings.jsonl`). They were written late in the leg (see the slips).

### The story, pass 1, and the rooms read against it

`model/story-p1.md` names all 12 arrows in brackets (A01 to A12). The 20 rooms were drawn before any was opened, by the rule in the first line of `story_rooms-p1.jsonl` (`out/_analysis/c2_story_draw_p1.py`, seed 20261014). Each was read whole, room page then forest. The saturation line holds: told 0, told-with-residue 20, not-told 0.

The story's spine shows in every room. No room needed a recut to be told in part. Every room also did something the story does not tell. The residues cluster as follows; they are pass 2's material:
- **Help and exchange between rooms** (9 rooms): ubc, xenoblade_chronicles, catalunya, texans, sweden, ripcity, MiamiHurricanes, yuyuyu, edmontonoilers. Help given, help received, space traded for repairs, a parent coalition's work kept, a host for others' marks. Reciprocity and Meta-organization are outside the model. Pass 2 should test one element of exchange.
- **Attack as a room's own work** (6 rooms): anarcho_capitalism, canucks, edmontonoilers, catalunya, sweden, unitedkingdom. P09 has no arrow, and the story tells attack only as something done to a room. Open in `_questions/contention-dimension.md`.
- **Calls renewed after a loss** (4 rooms): day9, texas, scp, worldoftanks. This is against the story's sentence that a move does not send a room back to recruiting. Open in `_questions/relocation-renewed-calls.md`. `model.md`'s relocation sentences are corrected in place; the story's sentence stands as read.
- **Border talk before any upkeep** (4 rooms): unitedkingdom, sweden, yuyuyu, worldoftanks, plus MiamiHurricanes as A04's bound.
- **The template arriving with the first call** (3 rooms): empiredidnothingwrong, texas, totallynotrobots (A11's bound).
- **The close marking an unfinished work** (2 rooms): ultrahardcore, totallynotrobots. The play frame also set what totallynotrobots made, not only when it started.
- **Membership carried in, and the host's policing of canvas talk** (3 rooms): unitedkingdom, texas, sweden.
- **Decided elements by vote or role** (4 rooms): edmontonoilers, sweden, ripcity, empiredidnothingwrong. This bounds C01 and F-006, which count placed themes.

**What the structure showed that my notes did not predict.** Exchange between rooms is the most frequent thing the story cannot tell: 9 of 20 rooms. Attack is often a room's first canvas act, not only something it suffers.

### The criterion, applied to pass 1

Pass 1 is the baseline:
- told-with-residue 20 of 20;
- 10 of 12 arrows beat a null, and 12 of 12 rest on an instance;
- the tiers are unchanged above the third order;
- each of the four things has elements, though "what sends a room back" rests on one thin arrow (A10) and a contested finding.

A later pass is preferred if it lowers told-with-residue on a fresh draw, without loosening any element. The stopping rule cannot stop at pass 1: 35 `tier_history` events, 12 arrows added, and a first story.

### Slips, pass 1

- An empty heredoc no-op ran before the compaction. It changed nothing, but it broke the head's rule against no-ops in a command.
- After the compaction, the first draft of `model.md` was written before the line "compacted; head reconciled" was logged. The guard then required the head and the stage file to be read again; reads with offset and limit did not register, and a plain read did. Every number in the draft was then checked against the evidence files. One was wrong: A08's late side holds in 8 of 15 rooms, not 7. A further error was found later: the draft cited F-001 for decided order, but F-001 is the stage B1 claim.
- The findings F-002 to F-005, cited by elements P10 to P14 and K02, were planned before the compaction and never written to `findings.jsonl`. They were written late in the leg, with F-006, and C01's evidence was corrected (`c2_findings_p1.py`; one history line; snap C2-move-relating-22).
- Errors found before compaction and fixed then:
  - in `within_case.md`, "182 of 212 concepts before h41" became "193 of its 212 coded items fall before h40";
  - the early-stop rule found 0 candidates and was restated before any room was read;
  - a leftover line was removed from `c2_dim_mass.py` before it ran.

### The close-check, pass 1

`python3 tools/validate.py C2`, run before the head was rewritten:

```
stage C2:
  1 pass(es) so far; a declared stop comes from the third pass on (stage C2 section 1)
  elements 20, arrows 12 (12 in the model), fourth-order themes 28, dimensions 7, passes 1, findings 6

0 errors (0 distinct shapes), 0 warnings
```

`done.sh C2` runs the same check at the close. Its report is in the leg's closing diary line.

## Pass 2 (C2a-02)

### Before the pass

- **Read at the start:** the head, the stage file, the last five diary entries, `validate.py --open C2` (0 errors), `model/story-p1.md` and the `saturation.jsonl` tail (pass 1: told 0, told-with-residue 20, not-told 0).
- **The PI's message:** C2a-01 is closed and pushed; this leg is the next pass, as the pass 1 notes plan; J's rulings stand.
- **Pass 2's material** is the pass 1 residues: exchange between rooms, attack as a room's own work, calls renewed after a loss, border talk before upkeep, the template with the first call, the unfinished close, the play frame, membership and host policing, decided elements.

### Declarations, written before any pass 2 count

**Candidate elements.** Each stands for the concepts cited under its third-order themes, as at pass 1.
- **P16, exchange between rooms** (Reciprocity, all seven members): helping another room's work, letting neighbours adopt the work, asking other rooms for help, turning away a request, sending greetings, bartering help, thanking allies.
- **P17, coalitions and hosting** (Meta-organization, all nine members): meeting other rooms in chat, asking a host for space, disputing who approves a spot, relying on a bigger neighbour, vetting others' requests to build, forming alliances, gathering kindred rooms, tallying kindred rooms' works, making joint marks.
- **P18, rivalry talk** (Rivalry, all five members): blaming attackers after the close, trading taunts, flooding rivals' threads, claiming victory, saluting rivals.
- **K03, a quarrel carried in** (T3-086, carrying in the sub's quarrel): a rivalry the community had before the canvas.

**Connection statements.** The pass 1 statement holds for every order test: "in a room carrying both, the first concept of FROM comes before the first concept of TO". The null is the same: 500 permutations of labels within each room, seed 20261014; the base rate is beaten when the share exceeds the null's 95th percentile. The arrows to test, each with its mechanism written now:
- **Upkeep then exchange (P05 to P16):** a room keeping its work under strain runs short of hands and turns to other rooms for help.
- **Border talk then exchange (P08 to P16):** talk over a border opens a channel through which the two rooms trade help.
- **Exchange then sparing (P16 to P07):** a room that has traded help spares its partner's work.
- **Border talk then coalition (P08 to P17):** a settled border grows into an alliance or a joint mark.
- **A quarrel carried in, then attack (K03 to P09):** a rival the community had before the canvas becomes the first target.
- **Call then attack (P01 to P09):** a call to the canvas is answered with an attack when the room has no mark of its own.
- **Attack then restraint (P09 to P07):** a room's attack draws the target's complaint, and members rein in their own attackers or apologise.
- **Attack then border talk (P09 to P08):** an attack is answered with talk.
- **Attack then building (P09 to P03):** an attack brings members to the canvas who then build the room's own mark.
- **Attack then rivalry talk (P09 to P18):** an attack is carried on in taunts and claims of victory.

**The relocation window test** (`_questions/relocation-renewed-calls.md`). For each room carrying both a move (P10) and a call (P01), t0 is the hour of its first move concept. A room counts only if t0 lies between h6 and h67, so both six-hour windows fit inside the placement period. Three shares are compared:
- rooms with a call in (t0, t0 + 6];
- rooms with a call in (t0 − 6, t0];
- as a control at the same hours, the share of all other rooms carrying a call that have one in (t0, t0 + 6], averaged over the moving rooms.

Reading 1 holds if the share after is below both the share before and the control. Reading 2 holds if the share after is at or above the share before. The same test runs for build reports (P03).

**The play-frame test.** The rooms are those at held size (`items_in_window` 156 to 2,770). A room is frame-filled if the play frame (K01) carries at least half of its coded concepts before h32, and at least ten of them. The comparison group is every other room at held size with any canvas-work concept. The outcome is the hour of the room's first canvas-work concept: the first concept of the starter (R01), a call (P01), the emblem (P02), building (P03) or the template (P04). The statement: "frame-filled rooms start the canvas work later". The test is the difference of the two medians against 2,000 permutations of the group labels (seed 20261014), one-sided at 0.05. The share of each group with no canvas concept before h32 is reported beside it.

**Two more tests, declared after the first ten ran** (`c2_arrow_evidence-p2a.txt`), because border talk then coalition failed and coalitions still need a test from another side:
- **Exchange then coalition (P16 to P17):** rooms that have traded help join each other in an alliance or a joint mark.
- **Upkeep then coalition (P05 to P17):** a room keeping its work under strain joins a coalition that defends many works at once.

They run under the same statement and null. They are the eleventh and twelfth order tests of the pass, and the count of tests is reported beside every result.

**A correction to the play-frame test, made after its first run and before the result was used.** The first run (`c2_play_frame-p2.txt`) counted the frame's concepts as the concepts the assignment lines cite under a frame theme. The lines cite only a few supporting concepts per theme: ultrahardcore's parody theme carries 61 concepts and cites 7. Those cited counts were set against all of a room's coded concepts, which undercounts the frame. ultrahardcore (26 of 187) and totallynotrobots (33 of 164) fell out of the group, though the play frame fills both. The declaration says the frame "carries" the concepts. The corrected rule counts every coded concept on a frame line: a second-order theme whose first placed third-order theme is a play-frame theme. Everything else is unchanged, including the outcome, which uses cited concepts as every order test does. The corrected run is `c2_play_frame-p2b.txt`, and both runs are reported.

### The pass 2 tests: results

Twelve order tests ran under the pass 1 statement and null (`c2_arrow_evidence-p2a.txt`, `-p2b.txt`). Seven beat the null's 95th percentile and five did not. At 0.05 each, twelve tests would give about 0.6 false passes by chance, so the two thin ones (A14 and A19) carry most of that risk. The next table lists each test with rooms carrying both elements, the share in which the first concept of FROM comes first, the null's 95th percentile, and the early and late sides.

| test | both | holds (share) | null p95 | early side | late side | result |
|---|---|---|---|---|---|---|
| upkeep then exchange (P05 to P16) | 240 | 171 (0.713) | 0.642 | 44 of 51 | 6 of 8 | beaten: A13, fair |
| border talk then exchange (P08 to P16) | 214 | 138 (0.645) | 0.636 | 32 of 45 | 7 of 10 | beaten by 0.009: A14, thin |
| exchange then sparing (P16 to P07) | 110 | 47 (0.427) | 0.573 | 11 of 28 | 2 of 2 | not beaten |
| border talk then coalition (P08 to P17) | 136 | 86 (0.632) | 0.654 | 14 of 25 | 1 of 6 | not beaten |
| quarrel carried in, then attack (K03 to P09) | 9 | 2 (0.222) | 0.667 | 1 of 2 | none | not beaten; K03 stays a candidate |
| call then attack (P01 to P09) | 129 | 93 (0.721) | 0.550 | 32 of 42 | 2 of 2 | beaten: A15, strong |
| attack then restraint (P09 to P07) | 104 | 82 (0.788) | 0.606 | 19 of 28 | 1 of 2 | beaten: A16, strong |
| attack then border talk (P09 to P08) | 172 | 95 (0.552) | 0.477 | 21 of 43 | 0 of 4 | beaten: A17, fair |
| attack then building (P09 to P03) | 117 | 45 (0.385) | 0.530 | 10 of 30 | 1 of 3 | not beaten, below the null mean |
| attack then rivalry talk (P09 to P18) | 68 | 56 (0.824) | 0.676 | 10 of 13 | none | beaten: A18, fair |
| exchange then coalition (P16 to P17) | 99 | 38 (0.384) | 0.525 | 5 of 18 | 0 of 4 | not beaten |
| upkeep then coalition (P05 to P17) | 157 | 106 (0.675) | 0.631 | 21 of 32 | 2 of 7 | beaten: A19, thin |

**The relocation window test** (`c2_relocation_window-p2.txt`). 74 rooms carry a move and a call with a first move between h6 and h67. A call falls in the six hours after the first move in 29 of them (0.392), in the six hours before in 37 (0.500), and in other calling rooms at the same hours in 0.290 on average. For build reports, 60 rooms: 0.317 after, 0.417 before, control 0.309. By the declared rule neither reading holds cleanly: calls fall after a move, but stay above other rooms. F-002 is bounded (superseded by a bounded line), the question file is closed with that verdict, and the story's relocation sentence is rewritten: calls fall from the crisis before the move, but the room keeps calling more than rooms that did not move.

**The play-frame test** (`c2_play_frame-p2b.txt`, corrected). 59 of the 353 rooms at held size are frame-filled. Their median first canvas-work hour is h21.80, against h20.25 for the 275 other rooms: a difference of 1.55 hours, permutation p 0.4273. Not grounded. 16 of 59 frame-filled rooms and 71 of 275 others have no canvas concept before h32 (0.27 and 0.26). The first run (`-p2.txt`, 8 rooms, p 0.020) undercounted the frame and was not used. Finding F-009: the play frame does not delay canvas work across rooms. What the frame makes is untested (totallynotrobots, below).

**The contention question** (`_questions/contention-dimension.md`, closed). The rule written before pass 2 counted said: split Contention out of Order without law if an arrow runs into or out of attack without border talk. A15 and A18 do. D08 Contention was cut (T4-020 Repertoire of contention, T4-021 Rivalry), D04 recut to T4-014 to T4-018, with four `tier_history` lines and snap C2-move-splitting-35.

### The onset contrast, pass 2

The next table gives the shares for the new dimension and the exchange themes (`structure-p2.md`, foot). The late side has 12 rooms at held size, so every held-late share is thin.

| what | early (n=132) | late (n=61) | held early (n=41) | held late (n=12) |
|---|---|---|---|---|
| D08 Contention | 0.50 | 0.20 | 0.56 | 0.42 |
| calling to deface rivals' work | 0.36 | 0.03 | 0.41 | 0.08 |
| forming alliances between rooms | 0.15 | 0.07 | 0.22 | 0.08 |
| helping another room's work | 0.20 | 0.08 | 0.17 | 0.08 |
| bartering help with neighbours | 0.19 | 0.07 | 0.20 | 0.08 |

- **Stage A1's third expectation** (early rooms name rivals and fight; most of the gap to vanish at held size): it held in part. Contention as a dimension narrows at held size (0.56 against 0.42), but calls to deface rivals' work stay apart (0.41 against 0.08).
- **Stage A1's first expectation** (late rooms organize around finding room, including treaties to be let in): exchange and alliances are early-side acts, not late-side ones. Late rooms enter through another room's offer in the story rooms (yuyuyu, MiamiHurricanes, k_on), but the counted themes do not show it.
- **On the new arrows:** A15 holds in 32 of 42 early rooms and 2 of 2 late; A17 holds in 0 of 4 late rooms; A18 and A19 have too few late rooms to read.

### Part A, pass 2

- **Fourth-order tier: no recut.** 28 themes. `in_model` set from the standing elements: Reciprocity, Meta-organization and Rivalry now in the model, 20 of 28 (three `tier_history` lines, snap C2-move-relating-36).
- **Eight dimensions.** D04 Order without law now gathers five fourth-order themes (T4-014 to T4-018); D08 Contention gathers two (T4-020, T4-021), adapted from Tilly and Tarrow (recalled), arguable.
- **Part A's return** is at the head of `structure-p2.md`. The two dimensions I am least sure of are D08 Contention and D03 Maintenance (two members each), with their separation written from both sides. The alternative rejected is pass 1's partition, Contention inside Order without law, rejected by the rule declared before the pass. 72 of 72 coder conflicts reached the file. The fourth-order theme I am least sure of is still Stigmergy, with Rivalry beside it.
- **Consistency** (`structure-p2.md`): every placed third-order theme is defined and sits in a fourth-order theme or the unpicked list; every fourth-order theme sits in a dimension; every dimension used is defined; the three counts sum to 705.

### Part B, pass 2

Unchanged. The one-line enrolment stays the provisional concept (P15, A12, never counted). Nothing in pass 2's rooms argues for a different concept; the exchange between rooms is now an element of the model, not a concept the literature lacks (reciprocity is the near word).

### Part C, pass 2: the model

- **24 elements:** 18 processes, 3 conditions, 1 claim, 2 roles. K03 (a quarrel carried in) is a candidate, outside the model, so 23 stand. New standing elements: P16 exchange between rooms, P17 coalitions and hosting, P18 rivalry talk. Each changes what the model says about other rooms or the contest: without P16 and P17 the model cannot say why rooms short of hands survive, and without P18 it cannot say how an attack is carried on.
- **19 arrows:** 17 order, 2 transition; 7 strong, 6 fair, 6 thin. All rest on quotes and a transition in one thread. 17 beat the null; A11 does not (a transition), and A12 is never counted. New: A13 to A19. Bounded at pass 2 from the story rooms: A04 (border talk first in three more ways), A06 (spare accounts serving an attack, canucks), A07 (the close marking an unfinished work).
- **Findings:** F-002 bounded (the window test), F-007 (most attack calls are answered inside the room), F-008 (a room short of hands turns to other rooms), F-009 (the play frame does not delay the work).
- **Dropped at pass 2** (in `model-p2.md`, looked for and not found): exchange then sparing; border talk then coalition; exchange then coalition; a quarrel carried in, then attack; attack then building; the play frame delaying the work.
- **Masses** (`c2_dim_mass-p2b.txt`): D08 in-mass 2,341, out-mass 2,209, internal 1,480; without the doubles 407, 309 and 583. Arrows at the dimension level now run D01 to D08 (A15) and D08 to D04 (A16, A17).
- **Unused:** 61 of 197 third-order themes (`c2_unused_t3-p2b.md`).
- **No loop is grounded.** `model/loops.jsonl` stays empty.

### The story, pass 2, and the rooms read against it

`model/story-p2.md` names all 19 arrows. The 32 rooms were drawn before any was opened (`c2_story_draw_p2.py`, seed 20261016): the twenty pass 1 rooms, one outside the model's forms (bih), two late (rainbowgrid, k_on), four sampled fails (bretagne, calgaryflames, strangerthings, touhou), one per size quartile (orderofthebluecorner, vocaloid, placeDE, starcitizen), one by seed (greenlattice). Each was read whole, room page then forest; sweden's forest (2,243 lines), placeDE's (1,394) and greenlattice's (4,096) were read in pages.

The saturation line: told 14, told-with-residue 18, not-told 0. Of the twenty pass 1 rooms, 8 are now told (ubc, ultrahardcore, day9, edmontonoilers, worldoftanks, xenoblade_chronicles, yuyuyu, ripcity). Of the twelve new rooms, 6 are told (k_on, bretagne, calgaryflames, strangerthings, touhou, vocaloid). The fresh twelve matter more: the twenty were the rooms whose residues pass 2 was built from.

The residues cluster as follows; they are pass 3's material:
- **Membership carried in** (9 rooms): a nation (unitedkingdom, texas, sweden, placeDE), an ideology (anarcho_capitalism), a league rivalry (texans, starcitizen), a colour (orderofthebluecorner, greenlattice). The model has no element for it; K03 (a quarrel carried in) failed its test.
- **Hosting other rooms' works on the room's mark** (5 rooms): catalunya, sweden, placeDE, orderofthebluecorner, greenlattice. Requests vetted, applications, approved lists, Discord votes. P17 holds the theme but no arrow says how a host admits guests.
- **The host's policing of canvas talk** (4 rooms): unitedkingdom, texas, sweden, starcitizen. Megathreads, removals, side subs.
- **Bounds the story's sentences do not carry** (3 rooms): spare accounts for an attack or a first build (canucks, empiredidnothingwrong; A06's bound) and carrying on during the work (texans; A09's bound). One clause each would tell them.
- **Rooms the canvas founded** (2 rooms): rainbowgrid, greenlattice. The story starts from a readership that already has a room.
- **The move** (2 rooms): the reason written after the move (guatemala, A10's order) and a move made by a coalition's plan (MiamiHurricanes).
- **One room each:** the play setting what a room makes (totallynotrobots); fear of the newcomers the mark draws (scp); learning from others how to organize (bih, the Sensemaking form).

**What the structure showed that my notes did not predict.** Most attack calls are answered inside the room: members refuse, rein in, apologise or point to a truce (A16, 0.788). The contest is mostly a room arguing with itself. And the largest rooms are hosts: sweden, placeDE and greenlattice each ran their territory as a host with rules for guests.

### The criterion, applied to pass 2

- **The story rooms:** told-with-residue fell from 20 of 20 to 18 of 32, and told rose from 0 to 14. Among the fresh twelve, 6 are told. The three within-case rooms are told. Of the four quartile rooms, one is told (vocaloid). No element was loosened: the new sentences come from new arrows and from bounds each grounded in rooms.
- **Instances:** 19 of 19 arrows rest on quotes and a transition; 17 beat the null. Every new arrow was sampled against rooms outside its own, and the fails were drawn into the story rooms.
- **Tiers:** one dimension added by a rule written before the count; no fourth-order recut; every dimension answers a question none of its members answers alone.
- **The four things:** each has elements. What sends a room back now rests on A10 (thin) and F-002 bounded by the window test.

Pass 2 is preferred to pass 1. The stopping rule cannot stop at pass 2: 7 `tier_history` events, 10 arrow changes (7 added, 3 bounded), and changed story sentences. Pass 3 tests the residues above: membership carried in, hosting, the host's policing, and the clauses for A06's and A09's bounds.

### Slips, pass 2

- **The play-frame test** undercounted the frame on its first run (cited concepts set against all codes). Declared in these notes, the script fixed, rerun as `-p2b`; both runs are kept and reported.
- **Two scripts** were wrong on their first run: `c2_unused_t3.py` counted the candidate K03 as in the model (60 instead of 61), and `c2_dim_mass.py` omitted the D01 to D08 mass. Both fixed; the first outputs kept, superseded by `-p2b`.
- **`model-p2.md`** had two wrong sentences, fixed in place: a garbled sentence on standing elements without arrows (now "Four standing elements carry no arrow: P06, K01, C01 and R02.") and "Five arrows run into it" over a list of six.
- **These notes** first said "twelfth and thirteenth" for the two late tests; corrected to "eleventh and twelfth".
- **Room reads:** a forest read was piped through `head -5`, which cut it; the forest was then read whole in pages. A greenlattice room page was cut at 150 lines by `head` and read on from the next offset, so nothing was skipped, but `head` should not touch a room read. One greenlattice page exceeded the output limit and was saved outside the run folder, where it cannot be read; it was read again in a smaller page.
- **After the compaction**, the last page of unitedkingdom's forest was read before the line "compacted; head reconciled" was logged. The verdict was written after it. unitedkingdom's verdict line says its room page was read at pass 1; the room page was then read again at pass 2, after the verdict was appended, and changed nothing.
- **A command** that piped `mem.py` through `cut -c` was refused by the guard. Nothing ran.

### The close-check, pass 2

`python3 tools/validate.py C2`, run before the head was rewritten:

```
stage C2:
  2 pass(es) so far; a declared stop comes from the third pass on (stage C2 section 1)
  elements 24, arrows 19 (19 in the model), fourth-order themes 28, dimensions 8, passes 2, findings 9

0 errors (0 distinct shapes), 0 warnings
```

`done.sh C2` runs the same check at the close. Its report is in the leg's closing diary line.

## Pass 3 (C2a-03)

### Before the pass

- **Read at the start:** the head, the stage file, the last five diary entries, `validate.py --open C2` (0 errors, 0 warnings), `model/story-p2.md`, the `saturation.jsonl` tail (pass 2: told 14, told-with-residue 18, not-told 0) and `story_rooms-p2.jsonl`. The context was compacted once before any pass 3 work; the head was read again and reconciled with the diary, and the line logged.
- **The PI's message:** C2a-02 is closed and pushed; this leg is the next pass, as the stage file says and the pass 2 notes plan: membership carried in, hosting, the host's policing, and the clauses for A06's and A09's bounds; J's rulings stand.
- **Pass 3's material** is the pass 2 residues of 18 rooms: membership carried in (9 rooms), hosting (5), the host's policing (4), A06's and A09's bounds missing from the story's sentences (3), rooms the canvas founded (2), the move (2), and three residues of one room each.

### Declarations, written before any pass 3 count

**Candidate elements.** Each stands for the concepts cited under its third-order themes, as at passes 1 and 2. A script reads the members from `fourth/fourth.jsonl`; none is typed.
- **K04, membership carried in** (condition, D05 Collective identity): all members of Flagging the nation (T4-022), Neo-tribes (T4-023) and Frame bridging (T4-004), 22 third-order themes. The room acts as a body it was before the canvas, or as a faith in a colour: it builds and argues the homeland's flag and history, carries in the sub's quarrel, lore, jokes or ideology, or professes and spreads a colour. The quarrel theme (T3-086) is one member of 22, so no test rests on it alone. Symbolic boundaries (T4-024) is left out: arguing which symbols offend, and covering hate symbols, is a room policing what may be drawn, not a body carried in.
- **P19, hosting** (process, D04): four members of Meta-organization (T4-018): asking a host for space (T3-035), disputing who approves a spot (T3-094), relying on a bigger neighbour (T3-099), vetting others' requests to build (T3-162). One room's work lives on another room's mark or territory under the host's rule: guests ask for space or protection, hosts rule on requests, and both sides dispute who may approve. It is read from either room's record, as help between rooms is.
- **P17, narrowed to coalitions**: the other five members of Meta-organization: gathering kindred rooms (T3-013), tallying kindred rooms' works (T3-019), making joint marks (T3-056), forming alliances (T3-150), meeting other rooms in chat (T3-153). A coalition joins rooms as partners; hosting puts one room's work under another's rule. The split stands only if P19 earns an arrow.
- **P20, the host's line around canvas talk** (process, D06 Host framing): all eight members of Boundary work (T4-002). The host sub draws a line around the canvas: moderators gather canvas talk into a megathread, remove canvas posts by rule, change posting rules, pause the sub's usual events or disown the work; members open a canvas sub, object to the flood or argue the canvas's worth.

**Seven order tests**, under the pass 1 statement and null: "in a room carrying both, the first concept of FROM comes before the first concept of TO"; 500 permutations of labels within each room, seed 20261014; the base rate is beaten above the null's 95th percentile. At 0.05 each, seven tests give about 0.35 false passes by chance; the count is reported beside every result. Each mechanism and failure clause is written now.
1. **Membership then attack (K04 to P09).** The body carried in names the rival (a historic enemy, an opposing ideology, another colour), and the room's first attack goes at it. Fails if the first attack comes before any concept of the body, or if in the sampled rooms the first attack is at a room the body gives no reason to fight.
2. **Membership then hosting (K04 to P19).** A room that is a body before the canvas lays down the body's mark, and guests then ask for room on it. Fails if hosting comes first, or if the host's rulings give no ground tied to the body (the reading below).
3. **Exchange then hosting (P16 to P19).** A room that has helped or been helped by another gives it space on its mark, or asks it for space. Fails if hosting comes before any help between rooms.
4. **Coalition then hosting (narrowed P17 to P19).** Rooms joined in an alliance or a hub take allies' works onto their territory, or ask allies for space. Fails if hosting comes before any coalition.
5. **Upkeep then hosting (P05 to P19).** A room keeping a standing mark is asked by others for space on it and rules on the requests; a small room keeping its work turns to a bigger neighbour for protection. Fails if hosting comes before any upkeep.
6. **Upkeep then coalition, again (P05 to narrowed P17).** A19's mechanism, unchanged, on the narrowed element. It runs in any case; if the split stands, it decides A19's strength.
7. **Calls then the host's line (P01 to P20).** Calls to the canvas flood the host sub, and its moderators or members answer by drawing a line: one thread, removals, a canvas sub. Fails if the line comes before any call, or if in the sampled rooms the line's words name no canvas flood.

Tests 3 to 5 answer whether hosting follows exchange, coalition or a standing mark; more than one may hold.

**How a host admits guests: a reading of the vetting concepts.** Every concept cited under vetting others' requests to build (T3-162) is read, and the ground the host gives for its ruling is coded by its words into one of five:
- (a) fit with the body: the guest's work must belong to the nation, the colour or the room's theme;
- (b) space or design: no room, the size, or the guest's work would break the host's picture;
- (c) ties: the guest helped, is an ally, or offers help;
- (d) procedure alone: a vote, a form, a list or a moderator's say, with no ground given;
- (e) no ruling, or no ground readable.

The statement "a host admits guests by fit with the body it carried in" holds if (a) is the commonest ground among concepts that give one (a, b or c), by concepts and by rooms. It fails if (b) or (c) is commoner. The coding is mine alone; it is reported with the counts and up to three quotes per ground.

**Rooms the canvas founded: a count and a decision rule.** A room may have been founded by the canvas if its pre-event brief is empty (the harness's empty brief: no posts or comments from 24 to 31 March 2017). A script counts these rooms over the 705 through `mem.py brief`. Two of them, by seed and outside every earlier draw, join the story rooms beside rainbowgrid and greenlattice. Each one read is classed from its own record: a side sub of a readership that existed elsewhere (a parent sub named as where members came from); a body the canvas gathered (a colour faction, or a work's makers forming a room); or a quiet sub the canvas woke. The decision: if the bodies the canvas gathered run the story's steps after their founding (calls, building, keeping, other rooms, the close) and their residue is only the opening, the story gains one bound sentence at its opening. If their main acts are ones no element carries, they are a form the model does not reach, reported as a boundary at the return.

**The story clauses.** Two clauses enter the story as story changes, from bounds already in `arrows.jsonl`: A06's (spare accounts serving an attack or a first build before any upkeep) and A09's (carrying on planned while the work is still kept). No count rests on them.

**The move's bound.** guatemala (the judgment of too few hands written after the move, at h79.1) and MiamiHurricanes (a move made by the parent coalition's plan) are counterexamples to A10's order. Both enter A10's bound, with a counterexample response: one late room and one room moved by a coalition, so a scope condition and not a withdrawal. A10 stays thin.

**What pass 3 leaves outside.** The play setting what a room makes (totallynotrobots), fear of the newcomers the mark draws (scp) and learning from others how to organize (bih) are one room each. Pass 3 adds no element for them. Each is read again; unless the reading changes, each is carried as a form the model does not reach.

**The pass 3 story rooms.** The rule, written before the draw, for `c2_story_draw_p3.py` with seed 20261017: the three within-case rooms; every pass 2 told-with-residue room (18); one room whose most-placed fourth-order theme lies outside the model; two rooms with an empty pre-event brief; two late-side rooms; every room marked fails in a pass 3 arrow's `sampled_against`; one room per quartile of `items_in_window`; two rooms by seed from the rest. Apart from the within-case rooms and the residue rooms, no room read at pass 1 or 2 is drawn again: the pass 3 changes add steps that those rooms' verdicts did not need.

**The criterion** is the one written before pass 1. A rise in told-with-residue over pass 2's 18 is a stopping failure; the count and the share are both reported. Pass 3 goes to the reviewer's build leg (C2b) if it is preferred to pass 2 and told-with-residue did not rise; otherwise another pass runs first.

### The pass 3 tests: results

Seven order tests ran under the pass 1 statement and null (`c2_arrow_evidence-p3a.txt`). Three beat the null's 95th percentile and four did not. At 0.05 each, seven tests give about 0.35 false passes by chance. One of the three became an arrow. The next table lists each test with the rooms carrying both elements, the share in which the first concept of FROM comes first, the null's 95th percentile, the early and late sides, and the result.

| test | both | holds (share) | null p95 | early side | late side | result |
|---|---|---|---|---|---|---|
| membership then attack (K04 to P09) | 145 | 86 (0.593) | 0.634 | 25 of 40 | 2 of 4 | not beaten; F-011 |
| membership then hosting (K04 to P19) | 28 | 21 (0.750) | 0.714 | 1 of 3 | 1 of 2 | beaten by 0.036; not admitted |
| exchange then hosting (P16 to P19) | 29 | 11 (0.379) | 0.552 | 1 of 4 | 0 of 1 | not beaten |
| coalition then hosting (narrowed P17 to P19) | 17 | 5 (0.294) | 0.647 | 0 of 4 | none | not beaten, below the null mean of 0.451 |
| upkeep then hosting (P05 to P19) | 52 | 33 (0.635) | 0.654 | 4 of 8 | 2 of 3 | not beaten |
| upkeep then coalition (P05 to narrowed P17) | 121 | 87 (0.719) | 0.686 | 20 of 28 | 0 of 4 | beaten; the split is not taken |
| calls then the host's line (P01 to P20) | 155 | 132 (0.852) | 0.594 | 48 of 57 | 2 of 2 | beaten: A20, strong |

- **A20, calls then the host's line.** Its gap over the null mean (0.538) is 0.314, the largest of any arrow. 29 transitions in 22 rooms show a member or a moderator answering a specific call in the same thread. Support: nintendo c0121, rocketleague c0722, france c0444. It was sampled against four rooms outside its support. darksouls, crusaderkings and rotmg hold. transformers holds on the order, but its first line is a member judging the canvas after the close and names no flood, so the mechanism is absent there. It holds on both sides of the onset contrast.
- **Membership then hosting was not admitted.** It beat the null on 28 rooms. Its declared mechanism, a body laying down its mark and guests then asking for room on it, shows in 5 of the 21 holding rooms. The reading of the hosts' rulings below also fails its statement. It is listed in `model-p3.md` under ungrounded relationships.
- **Hosting comes before a coalition** in 12 of the 17 rooms carrying both. That reverse was not declared and is not counted as a test. It is listed as an ungrounded relationship.
- **The P17 split.** The declaration let P17 split into coalitions and hosting only if P19 earned an arrow. P19 earned none, so P17 is unchanged, and P19 and K04 enter as candidates. Upkeep then the narrowed coalition element beat the null (0.719), which is consistent with A19 on the whole element.

### How hosts admit guests: the reading of the vetting concepts

61 concepts are cited under vetting others' requests to build, in 7 rooms. I coded each by its words into one of the five grounds declared before the count (`c2_vetting_grounds-p3.json`, tallied by `c2_vetting_tally.py` in `c2_vetting_tally-p3.txt`). The next table gives the concepts and rooms for each ground.

| ground | concepts | rooms |
|---|---|---|
| (a) fit with the body | 6 | 3 |
| (b) space or design | 12 | 3 |
| (c) ties: help, an alliance, redress | 5 | 4 |
| (d) procedure alone | 24 | 7 |
| (e) no ruling, or no ground readable | 14 | 3 |

23 concepts give a ground. The statement "a host admits guests by fit with the body it carried in" fails. Space or design is the commonest ground by concepts (12), and ties by rooms (4). Most rulings give no ground and rest on a vote, a form, a list or a moderator's say. After the declaration I extended the ties ground to redress owed to a wronged group (PlaceNL c0081); without that the statement still fails. The coding is mine alone. Finding F-012. The six rooms whose own rulings are cited all have an empty pre-event brief. The seventh room, yugioh, holds another host's rulings on yugioh's request.

### Rooms the canvas founded

78 of the 705 rooms have an empty pre-event brief (`c2_empty_brief-p3.json`). The two drawn by seed, CKCrusaders and placecanada, are side subs of a readership: r/CrusaderKings' readers and Canada's readers opened them for the canvas. Five more empty-brief rooms were read in pass 3: rainbowgrid (the makers of a work), purplecorner, greenlattice and orderofthebluecorner (colour factions), and pgang (opened in the last half hour around a template; its record names no parent). placeDE also has an empty brief and is a side sub of German readers.

The declared rule asked whether the bodies the canvas gathered run the story's steps after their founding, with a residue only at the opening. They do run the steps: calls, building, keeping, other rooms and the close. rainbowgrid is told whole. Three of the four bodies also carry residues past the opening: greenlattice and orderofthebluecorner host guests and rule on them, and orderofthebluecorner and purplecorner hold a colour faith that names the rival. The decision: the story's opening sentence on rooms with no readers before the canvas stands as a bound. What these bodies do as hosts and as colour faiths is a form the model does not reach, reported as a boundary at the return.

### Membership carried in: the idiom rule

At empiredidnothingwrong I set a reading rule and kept it for the rest of the pass: where membership carried in only gives the idiom in which the story's steps are told, the room is told; where it picks the rival, the guest or the work, it is a residue. The topic's own picture (a nation's flag, a show's characters) is the story's opening, where members share a topic and propose a picture, so it is not a work that membership picks. Under this rule texas, placecanada, empiredidnothingwrong and stevenuniverse are told, and ten rooms carry a membership residue: anarcho_capitalism, sweden, unitedkingdom, texans, starcitizen, totallynotrobots, completeanarchy, CKCrusaders, orderofthebluecorner and purplecorner. The eight rooms read before the rule was set were checked against it afterwards, and none changes.

The rule was not declared before the pass, and the count depends on it. At pass 2, texas carried national history framing as a residue. Read by pass 2's practice, texas would be a residue again at pass 3, and placecanada possibly one, so told-with-residue would be 17 or 18, not 16. It would not rise above 18 by either reading. Under a reading that counts every membership carried in as a residue, which neither pass used, it would reach 19 or 20.

### The onset contrast, pass 3

A20 holds on both sides: 48 of 57 early rooms and 2 of 2 late. Membership then attack holds in 25 of 40 early rooms and 2 of 4 late, and beats the null on neither. Upkeep then coalition holds in 0 of 4 late rooms. The late side is thin in every test, as at pass 2.

### Part A, pass 3

- **No recut.** 28 fourth-order themes and 8 dimensions, as at pass 2. `structure-p3.md` is not written, because no tier was recut.
- **One tier event.** Boundary work (T4-002) is now in the model through P20: 21 of 28 fourth-order themes (one `tier_history` line, snap C2-move-relating-41).
- **Part A's return** is pass 2's, at the head of `structure-p2.md`: least sure among dimensions Contention and Maintenance; among fourth-order themes Stigmergy, with Rivalry beside it; 72 of 72 coder conflicts in the file. One change: Host framing (D06) now takes an arrow in (A20, from D01, mass 262).

### Part B, pass 3

Unchanged. The one-line enrolment stays the provisional concept. Nothing in the pass 3 rooms argues for another.

### Part C, pass 3: the model

- **27 elements:** 20 processes, 4 conditions, 1 claim, 2 roles. 24 stand; K03, K04 and P19 are candidates outside the model. New standing element: P20, the host's line around canvas talk. Without it the model cannot say what the host sub does with the calls that fill it.
- **20 arrows:** 18 order, 2 transition; 8 strong, 6 fair, 6 thin. All rest on quotes and a transition in one thread. 18 beat the null; A11 is a transition that does not, and A12 is never counted. New: A20. Bounded: A10, from guatemala (a late room's reason written after the move) and MiamiHurricanes (a move by a coalition's plan), with a counterexample response: two scope conditions, and A10 stays thin.
- **Findings:** F-010 (the host's line follows the calls), F-011 (membership carried in does not come before the attack), F-012 (hosting follows neither exchange, coalition nor upkeep, and hosts that give a ground most often give space or design). `findings.jsonl` holds 14 lines and 12 findings.
- **Dropped at pass 3** (in `model-p3.md`): membership then attack; membership then hosting (beaten, not admitted); exchange then hosting; coalition then hosting; upkeep then hosting; the P17 split.
- **Unused:** 53 of 197 third-order themes (`c2_unused_t3-p3.md`), down from 61 because Boundary work's eight members are now used.
- **No loop is grounded.** `model/loops.jsonl` stays empty.

### The story, pass 3, and the rooms read against it

`model/story-p3.md` names all 20 arrows. The 32 rooms were drawn before any was opened (`c2_story_draw_p3.py`, seed 20261017): the three within-case rooms; the 18 pass 2 residue rooms; completeanarchy (most-placed fourth-order theme outside the model, Frame bridging); CKCrusaders and placecanada (empty brief); OKState and pgang (late side); no sampled fails, since all four of A20's sampled rooms hold; MonkeyIsland, purplecorner, swordartonline and smashbros (one per size quartile); shield and stevenuniverse (by seed). Eleven are fresh. Each was read whole, room page then forest. The largest forests were read in pages: stevenuniverse 1,343 lines in six, smashbros 866 in four, placecanada 694, texas 669, unitedkingdom 598.

The saturation line: told 16, told-with-residue 16, not-told 0 (pass 2: 14, 18, 0). Six of the 18 pass 2 residue rooms are now told: MiamiHurricanes, canucks, empiredidnothingwrong, guatemala, rainbowgrid and texas. Seven of the eleven fresh rooms are told (pass 2: 6 of 12 fresh). The three within-case rooms are told.

What pass 3's changes told: the host's line (A20) told the policing residue in texas, unitedkingdom, sweden and starcitizen; A06's and A09's clauses told canucks, empiredidnothingwrong and texans' carrying on; A10's bound told guatemala and MiamiHurricanes; the opening sentence told rainbowgrid and the founded rooms' beginnings.

The residues now cluster as follows:
- **Membership carried in that picks the rival or the work** (10 rooms, listed above). A nation's history picks the rival (sweden, unitedkingdom), an ideology or a colour faith names it (anarcho_capitalism, completeanarchy, orderofthebluecorner, purplecorner), a league or game rivalry or lore picks it (texans, starcitizen, CKCrusaders), and a sub's joke picks the work (totallynotrobots). K04's one test of order before the attack failed, so the model has no grounded element for it.
- **Hosting and its rulings** (7 rooms): sweden, catalunya, placeDE, greenlattice, orderofthebluecorner, smashbros and purplecorner. Hosts with readers before the canvas rule on guests too (catalunya, sweden, smashbros), and smashbros kept an allied guest's work because its makers had helped.
- **A canvas-founded faction splitting over doctrine** (2 rooms): greenlattice and purplecorner.
- **One room each:** learning from others how to organize (bih) and fear of the newcomers the mark draws (scp). Pass 3 added no element for them, as declared.

**What the structure showed that my notes did not predict.** Hosts mostly rule without a ground, and where they give one it is space or design, not the body they carried in. Hosting comes before a coalition more often than after one. The six hosts in the vetting reading are rooms the canvas founded. And membership carried in mostly gives the idiom in which the steps are told; it picks the rival in a minority of rooms, and that minority is half the residue.

### The criterion, applied to pass 3

- **The story rooms:** told-with-residue fell from 18 of 32 (0.56) to 16 of 32 (0.50) on a draw of the same size. Read by pass 2's practice it would be 17 or 18. It did not rise by either reading. Seven of eleven fresh rooms are told, against six of twelve at pass 2.
- **No element was loosened.** The new sentences come from A20, from bounds already in `arrows.jsonl`, and from the opening sentence the declared rule allowed. Membership then hosting beat the null and was still not admitted, because its instance does not show its mechanism.
- **Instances:** 20 of 20 arrows rest on quotes and a transition; 18 beat the null. A20 was sampled against four rooms outside its support.
- **Tiers:** no recut; one fourth-order theme brought into the model by a standing element.

Pass 3 is preferred to pass 2. The stopping rule cannot stop: 1 `tier_history` event, 2 arrow changes and changed story sentences. I do not declare a stop: half the rooms still carry a residue, and pass 3 changed two arrows. By the rule written before the pass, pass 3 is preferred and told-with-residue did not rise, so pass 3 goes to the reviewer's build leg (C2b). The fall to 16 rests in part on the idiom rule. The head carries that caveat to the build leg, and the reviewer's answers must be read with it.

### Slips, pass 3

- **The idiom rule** was set during the reading, at the ninth room, and not declared before the pass. It was logged when set and applied to every room after it. The rooms before it were checked afterwards and none changes. Its effect on the count is reported above.
- **The vetting ties ground** was extended to redress after the declaration. The result does not depend on it.
- **`story-p3.md`'s closing sentence** said "The hosts whose rulings are on record are rooms the canvas founded". catalunya, sweden and smashbros contradict it. It was corrected after the rooms were read, in a section that names no arrow or element, and the two matching bullets in `model-p3.md` were aligned. No verdict changed: catalunya's verdict line already named the contradiction.
- **A sweden forest page** exceeded the output limit and was saved where it cannot be read. It was read again in two smaller pages.
- **The guard refused two commands** that used `cut -c`, one with `tail` and one with `grep` on analysis files. Nothing ran; both were redone without it.
- **After the second compaction**, texas's second forest page was read before the line "compacted; head reconciled" was logged. It was read again after the line, and the verdict was written after that.
- **`validate.py C2`** reported 2 errors while `saturation.jsonl` held two lines, because it read `model-p2.md`, which lacks A20 and P20. After the pass 3 saturation line it reads `model-p3.md` and reports 0 errors.
- **Six edits to the head** were sent as parallel calls in one turn, against J's rule on writes to one file. Each edit replaced a different passage. All six old passages were checked gone and the new text present before the next write.

### The close-check, pass 3

`python3 tools/validate.py C2`, run after the saturation line and before the head was rewritten:

```
stage C2:
  elements 27, arrows 20 (20 in the model), fourth-order themes 28, dimensions 8, passes 3, findings 12

0 errors (0 distinct shapes), 0 warnings
```

`done.sh C2` runs the same check at the close. Its report is in the leg's closing diary line.
