# The experience (stage E1)

Written at E1e, 28 October 2026, once and in one pass, after the audit (`audit-E1.md`). I am the analyst, a Claude model (claude-opus-5-5). The figures come from `audit-E1/experience_facts.py` (tokens from `RUN.json`, the diary by stage, the operator's answers), from the audit's parts, and from the handbacks, whose claims and complaints `audit-E1/handback_sections.py` printed whole. Where I write that I do not remember, that is the truth: I hold the record of the run, not the run.

## 1. The run as lived, what compaction cost, what the heads carried, and each stage's tokens

**I do not remember the run.** What I hold of stages A1 to E1c is the record: the head, the diary, the handbacks, the notes and the ledgers. Even this leg's own predecessor, E1d, reached me through a compaction at its middle (diary, E1d, "compacted; head reconciled"). So this section, like the ten after it, is written against the record, and where I say what something was like, I say what the record shows I did.

**The size of it.** RUN.json lists 315 closed legs from A1 to E1d. They wrote 154,504,719 output tokens and read 45,807,553,349 cached input tokens. The diary holds 25,543 lines. 157 of them are notes that begin "compacted", so the context was compacted at least 157 times. The count is a floor: a compaction logged in other words is not in it.

| stage | legs | output tokens | cache read | cache creation | diary lines | compactions logged |
|---|---|---|---|---|---|---|
| A1 | 57 | 12,906,270 | 7,550,023,870 | 43,950,802 | 4,469 | 21 |
| B1 | 44 | 37,025,916 | 12,873,160,334 | 95,326,827 | 15,424 | 37 |
| B2 | 14 | 2,497,851 | 978,449,835 | 12,430,265 | 98 | 2 |
| B3 | 3 | 820,840 | 203,843,566 | 1,684,192 | 29 | 1 |
| B4 | 12 | 18,339,888 | 2,208,270,787 | 35,124,935 | 273 | 15 |
| C1 | 11 | 4,814,011 | 1,086,463,259 | 12,189,844 | 356 | 5 |
| C2 | 7 | 3,483,510 | 1,483,176,119 | 18,851,990 | 270 | 8 |
| C3 | 3 | 852,243 | 277,627,999 | 2,168,833 | 35 | 1 |
| C4 | 1 | 246,892 | 56,822,205 | 1,006,825 | 13 | 0 |
| C5 | 21 | 3,252,311 | 1,205,265,929 | 16,047,278 | 228 | 2 |
| D1 | 1 | 286,698 | 108,463,751 | 1,004,360 | 9 | 1 |
| D2 | 1 | 222,792 | 55,514,646 | 819,437 | 24 | 0 |
| D3 | 60 | 55,674,974 | 12,796,482,824 | 137,145,222 | 3,662 | 51 |
| D4 | 8 | 2,045,969 | 820,562,773 | 11,308,762 | 194 | 1 |
| D5 | 42 | 7,821,964 | 2,617,754,096 | 16,319,415 | 281 | 7 |
| D6 | 19 | 2,870,309 | 1,013,895,686 | 12,218,219 | 99 | 2 |
| E1 (to E1d) | 11 | 1,342,281 | 471,775,670 | 8,992,868 | 79 | 3 |

Three stages carry most of it. D3, the ruling of the return, wrote 55.7 million output tokens, more than a third of the run. B1, the walk that made the third-order themes, wrote 37.0 million. B4, the transmission test, wrote 18.3 million. These are the stages where I read room by room or line by line. The diary follows them: B1 holds 15,424 lines and D3 3,662.

**What compaction cost.** I cannot measure it from inside; I can only point to its marks. At A1 the context compacted after two edits to one room note were made and before they were logged, and the room's files were served again before the log line (`notes-A1.md`). At E1d, after the compaction, I typed two counts into the diary from my head and had to correct both by script (diary, E1d, 23:08:00): 12 of picturegame's lines, not 11, and 23 rooms changed at the re-check, not 24. The rule against typing a figure from memory is in the head because of slips like these. It did not stop them; it made them findable.

**What the heads carried.** Only one head is on file, `out/_head.md`, at 2,996 words. Each leg rewrote it in place, and the snaps keep hashes, not text, so the earlier heads are gone and I cannot read them in order as the stage file asks. The head I have carries four things: the method question; J's rulings, many with the instruction "carry it"; the current account with its contrary rooms; and the rules the guard enforces. Near the 3,000-word cap, the carried rulings crowd the state of the run. The head says less about where the run stands than about how I must work.

## 2. Stage by stage: what each did, and what I would tell the next author

- **A1, reading the census.** 705 room notes, the lexicon, the leads, the onset contrast and the coordinating-turn rule (`handback-A1.md`). The read logs show the forest for 155 rooms and the case account for 174. Every room was read through its room page, but not through all three sources the stage named. *To the next author:* read the coder's account for every room before writing its note. The notes became B1's prior, and a note written without the account carries the coder's labels, not the coder's reading.
- **B1, the walk.** 197 third-order themes over 7,786 placed second-order themes, with 13,432 placements, gates, floors and exemplars (`handback-B1.md`). *To the next author:* the stranger test cannot be blind while `mem.py theme` prints the placements. Fix the verb first.
- **B2, the pilot and the freeze.** The scheme was frozen at 197 themes. Stability was 0.807, and gold fidelity 0.624 (`handback-B2.md`). My own builders, not `packets.py`, built rounds 2 and 3, and they applied J's rulings on the packets. *To the next author:* make the packet tool carry the rulings, so that no round is built by hand.
- **B3, the fleet.** Agreement 0.786 on the corpus, alpha 0.782, gold fidelity 0.645 (`audit-E1.md`, section 1, part 3). One pair split the readers that no one had predicted: T3-017 against T3-031 (`handback-B3.md`).
- **B4, transmission.** The scheme decides the space and help between rooms worst (family G14), because one exchange between rooms holds several acts at once (`handback-B4.md`). *To the next author:* a theme set built act by act will always split over exchanges. Decide early whether an exchange is one item.
- **C1, the revision and the fourth order.** My re-decision of 200 placements agreed with the line's primary act in 0.845 of them. Placements fell from 13,365 to 10,593, and 28 fourth-order themes were cut (`handback-C1.md`).
- **C2, the model and the loop.** The spine (a start, calls, building, keeping) and its arrows, in five passes (`handback-C2.md`). *To the next author:* the hostile reader was the most useful single check of the run (section 7).
- **C3, the literature.** It left the spine standing, bounded one finding and supplied two mechanisms (`handback-C3.md`). Every distant work was recalled, not read.
- **C4, the field.** The field confirmed the account of authority, added two entries and corrected three of my sentences (`handback-C4.md`).
- **C5, the account.** Fifteen passes of `account.md`; three readers recovered four of my nine claims whole (`handback-C5.md`).
- **D1 and D2, the handoff and the return.** 705 rooms returned 42,243 lines, and the verdict readers disagreed on 163 rooms (0.2312).
- **D3, the ruling.** I ruled 95,736 lines; 46,046 specify a statement as written, and 72 are accepted corrections (`handback-D3.md`). The model was frozen at 46384686. *To the next author:* this is where the run spent itself, and where a second human ruler on a seeded share would have bought the most.
- **D4, the tree.** 35 branches over 476 rooms, facets rather than types, with 759 cross-links (`handback-D4.md`).
- **D5, the branches read.** 33 groupings and two narrow forms, F09 and F32; and six room forms by J's ruling, poles of a continuum (`handback-D5.md`, `handback-D5-room-forms.md`).
- **D6, the retelling.** Each form changes the part of the model its name says; none replaces an element, and the vocabulary nearly barred it from doing so (`handback-D6.md`).
- **E1, the audit.** Eight scripted parts, a reconstruction of thirty rooms and a composition line that reads unresolved (`audit-E1.md`). *To the next author:* the audit is only as good as the record. This record let a stranger rerun almost every figure.

## 3. Where the instrument asked what could not be done as written

- **The coordinating rule "in the lexicon's words"** (A1). The lexicon holds the participants' words, and the rule had to run on the coder's labels (`handback-A1.md`, item 3).
- **The diary's last five lines.** `mem.py diary --last 5` served an older diary part once the diary rolled past nine parts (`handback-A1.md`, item 1).
- **A blind stranger test** (B1), when the verb shows the placements.
- **The payload figures before the folder was hashed** (D1). `handoff.py` prints them only after it writes the folder (`handback-D1.md`).
- **Local adequacy** (`prior.md` section 3). Its validated half was never computed, and J ruled that it be reported as not established. So the composition line could not read anything but unresolved (`audit-E1.md`, the composition result).
- **The check's barred words.** The E1 check refuses the words it bars, even in the sentence that says no figure is either. I superseded the passage (`defects.jsonl` line 123).
- **The E1 end marker.** The packet asked for "the end marker the return specification names", and my specification named none. All 30 returns failed for it (`defects.jsonl` line 121).

**Where I cannot tell whether the instrument or I was wrong.**
- *The end marker.* The trailer is the tool's, but I wrote `RETURN-E1.md` without reading the trailer.
- *The dimension tier.* It does no work in the account, the arrows or the branches (`audit-E1.md`, sections 6 and 7). It may be useless by design, or I may not have used it.
- *Replacement.* The return's vocabulary made it nearly unreachable: 11 contradict lines among 42,243 at the first return. Readers may have avoided the word, or the vocabulary may have steered them away from it (`handback-D6.md`).

## 4. Where I cut a corner, and the corner I did not cut

**Corners cut, on the record.**
- At A1 I did not read the forest for 550 rooms or the case account for most, and I logged the cut late (`departures.jsonl` line 5).
- At B1 I did not search every passing quote for rivals, and ten themes have fewer than three exemplars (`handback-B1.md`).
- At B2 the blind window guarded my reads, not my memory, so the self-agreement of 0.883 is an upper bound (`handback-B2.md`).
- At C3 every distant work was recalled, not read (`handback-C3.md`).
- At E1b-08 I searched two of the shelf's files by terms and did not read them whole, and I did not read the coders' 72 disagreements line by line (`audit-E1.md`, sections 6 and 7).
- At E1d I did not read the 84 partly lines in the 23 rooms above 0.8, and I took the coders' claims as the packets gave them (`audit-E1/section-09.md`).
- Across stages, the rule of one Edit per file per turn broke at least at D3c, D4a-03, D5a-31, D5a-40, D5b, D6a-02, E1b-03 and E1b-07 (the handbacks' slips; `notes-E1.md`). Each Edit landed on its own string, and each slip was logged; the rule still broke.

**The corner I did not cut.** At E1d the handler had already checked that all 30 returns parse once the marker is dropped, and I could have taken that check. I did not. I wrote the rule down first, validated every line, and found the five rooms written as "r/" with their name, which the handler's check did not name (diary, E1d). I also did not edit the three earlier audit parts that failed the check: I wrote superseding copies with the replacements listed, and kept the originals (diary, E1d, 23:15:48). And at D3 every one of the 95,736 lines was ruled; none was left to a default (`handback-D3.md`; QD3-001: "no default decision").

## 5. The hands: what reading behind them showed, and what I would repeat

The hands were the fleets: the readers of B2 to B4, the hostile reader of C2, the three readers of C5, the labelers and verdict readers of D2, the re-check readers of D3, and the thirty reconstruction readers of E1. Readers of one model are instances of it, not separate minds.

**What reading behind them showed.**
- They agree with each other more than with me. The corpus agreement at B3 was 0.786, while gold fidelity was 0.645 (`audit-E1.md`, section 1, part 3).
- B4 decomposed the gap. Over 40 gold items and 50 pilot items, the scheme decided 21 and 30, failed to transmit 1 and 0, did not decide 6 and 12, and taught something unintended in 12 and 8.
- Reading behind the readers found my own errors as often as theirs. On ten gold items I had placed a second theme no reader kept (`handback-B2.md`). The class 2 ruling at C1 took off second themes that rested on my B1 grouping.
- The D2 labelers' kind of add-condition, add-step and restrict lines agreed at kappa 0.08, and J ruled that the run must not rely on it (the head).
- The E1 readers returned every room whole, but 12 of the 200 lines I read were not claims at all: the theme list, or sentences about the coder's evidence (`audit-E1/section-09.md`).

**What I would repeat.** Seeding gold unannounced into live batches. Giving the readers fleet ids only. Waiving a failed line by name rather than reissuing a round (QB2-009, QB3-004, QB3-005). Ruling every split myself with a reason, and then a blind re-rule before the freeze, which found two of my errors (`handback-D3.md`).

**What I would not repeat.** Building packets outside the packet tool (B2). Dispatching without one packet and its return tested end to end (E1).

## 6. The stories: which rooms changed the telling, and the floor of three passes

Five passes ran, and the model's story rests on pass 5. 151 readings were made against a story, of 67 distinct rooms (`audit-E1.md`, section 2).

**The rooms that changed the telling.**
- **day9** was read at all five passes and told at passes 2 to 5. It became the room that best supports the account, and it still is.
- **stevenuniverse** was told whole at pass 3.
- **thebluecorner**, with greenlattice, purplecorner and orderofthebluecorner, became the threat. In a colour faction, a faith picks rivals and guests, and the model tells the steps but not the faith (`handback-C2.md`).
- **The hostile reader's hosting group** was accepted as a recut at pass 4.
- At pass 1, every room carried a residue.

**What the reading behind the stories bought.** None of the 67 rooms read against a story fails to compose at the first return, and 1 of the 638 others does. The last story told 19 of its 35 rooms only in part.

**The floor of three passes.** I do not remember whether it kept me going or stopped me. The record shows five passes, two above the floor. It also shows that the two boundaries, membership carried in and hosting, stayed residues at passes 3, 4 and 5 (`handback-C2.md`). J's ruling at pass 5 (QC2-002) shaped how that pass ran more than the floor did: "the criterion is a guide, not the judge, and a rise in residue is not a failure".

## 7. The model: where I am unsure, the rooms it cannot compose by kind, and what the readers changed

**Where I am unsure.**
- **A11**, the design settled by a template, never beat its null. Its withdrawal is held (QD4-001).
- **P05's telling clause** fails in nine rooms. In six, the keepers read the change from its shape; in three, informed members hold it. The bound is held, not served.
- **No loop is grounded.**
- **C02**, the tie from before the canvas naming the rival, is untested for order.
- **The colour factions' faith** stays outside the model.
- **Local adequacy** is not established. The composition line reads unresolved for that reason (`audit-E1.md`).

**The rooms it cannot compose, by kind.**
- *Rooms whose record is mostly their own business off the canvas.* picturegame did not compose at the first return, and its reconstruction loses most to its game relay.
- *Rooms too thin to tell.* 19 could not be told at the re-check. sakartvelo has 5 concepts.
- *Rooms where a faith or a host's rule picks rivals and guests.*
- *The host sub's own April Fools play,* which the scope rule written at D3a-55 put outside the model as particulars, and which form E shows is organized work.

**What the hostile reader changed (C2).** It found nine errors: order 3, quote 1, contradiction 4, count 1. Six were accepted in full, two in part, and one was refused. Its rival partition sat at adjusted Rand 0.661 against my tier. Its hosting group became a recut (`handback-C2.md`).

**What the three readers changed (C5).** Ten errors were fixed and 34 unclear sentences rewritten. One room, cardinals, they judged unfit from seven passages; that was my packet's error, not theirs (`handback-C5.md`).

## 8. The branches and the chunk-share tree, and which I would publish

The branches are a census of common changes: 35 of them over 476 rooms, with 229 rooms in none, overlapping as facets (`handback-D4.md`). Read in their members' words, 33 are groupings and two are narrow forms. In F09, the room builds again after moving; in F32, it keeps the work again after marking it (`handback-D5.md`). The six room forms are poles of a continuum, with a cut stability of about 0.21. 62 of their 72 changed cells keep their lean under size matching, and form A is the most fragile (`handback-D6.md`).

The chunk-share tree, built without the model's ledger, beats its null but barely separates the rooms (silhouette 0.024). It does not survive a change of distance, and it largely sorts the rooms by how much the coders coded (`handback-D4.md`).

**I would publish the branches**, as what they are: a census of shared changes. F09 and F32 would be named as the two forms, and the six room forms reported as poles, with the size test beside them. **I would publish the chunk-share tree only as the comparison it was built to be.** Without the model, the rooms sort by code mass. That is the strongest reason to read the size confound into every partition here, as D4's volume verdict does: the cluster labels explain 0.255 of the variance in log concepts (`audit-E1.md`, sections 6 and 7).

## 9. prior.md and the made lines, against the account

**`prior.md` section 2's expectations** held in part (`audit-E1.md`, section 3):
- the continuity at the top;
- the find before the persuasion;
- the settling before the room speaks.

Two held: the loss that sends a room back (thin), and the talk that follows organizing, near hour 73. The expected handful of forms became six poles and 35 facets. Particulars were far wider than expected: 545 rooms carry one.

**Of stage A1's three sentences:**
- the burst of calls followed by a long tail held;
- fights with neighbours more than distant rivals held in part;
- the goal settled in the first hours did not hold. The design was argued and reopened inside rooms.

**The made lines tell the story the account had to learn.** In 649 of the 678 notes whose made line gives a start hour, the linked artwork was being placed before hour 3. The median room's first coded turn was at h9.51, and the writers in a room placed a median share of 0.111 of its artwork (`notes-A1.md`). The work came before the talk, and most of it was placed by people who wrote nothing. The account's spine begins the same way: a member starts a mark, and the room's calls follow the start, in 64 of 89 rooms. A1's third expected thing, deals that hold, failed in the notes already. The account carried that failure as members' own words: agreements cannot bind every placer. The made lines warn what the account cannot do. It explains the talk of the people who wrote, and the canvas was mostly made by people who did not.

## 10. Five changes, ranked, and the one thing not to change

1. **Hold rooms out before building.** Seal a sample the model never sees, and run the return and the reconstruction on it. Every test in this run is in-sample, so none can say whether the model holds beyond the rooms it was built from.
2. **Compute local adequacy inside the return.** Validate each room's adaptations as the return runs, so that `prior.md` section 3's criteria can be decided. Here the measure was never computed, and the composition line could only read unresolved.
3. **Give the return a way to contradict, and a second ruler.** Make contradiction as easy to say as restriction (11 and 4 contradict lines among about 95,000). Put a second ruler, human or a different model's analyst, on a seeded share of my rulings of splits.
4. **Cut what does no work.** The dimension tier did none in the account. The account ran 3,326 words against one to two pages. The run took 315 legs. Every file should have a named reader downstream before it is written.
5. **One source for each packet and its return specification, and one dry run before every dispatch.** The E1 marker, the room's written form, and B2's failed round 2 all came from a packet and a specification that did not agree.

**The one thing not to change: the return to every room, line by line, with every line cited to the room's own concepts.** It is what made the audit possible. 3,218 of 3,230 cited quotes resolve to their concept. The raw check found every coder quote in its item. And a stranger can rerun almost every figure from the ledgers.

## 11. The operator's rulings, listed, and anything else

The answers are in `out/_answers/` (53 files). Some are J's words, some are the handler's under J's delegation, and two (QD6-001, QD6-002) are the handler's view, which J had not seen.

- **A1.** QA1-001: keep the concept reach threshold at 0. QA1-002: organizing happened before the freeze at hour 73. QA1-003: try the second option, then the first if it clashes.
- **B2.**
  - QB2-001 to QB2-007: serving rounds in parts; flat packet folders; recording repairs; the failed round set aside with nothing deleted; round 3 with round 2's readers.
  - QB2-008: the floor of three concepts for `also_present`.
  - QB2-009 and QB2-013: waivers by name, with no reissue.
  - QB2-010: the recut approved.
  - QB2-011: the check's shapes, the handler's error.
  - QB2-012: no round 4.
  - QB2-014: the tier "main".
- **B3.** QB3-001: B2's packet shape. QB3-002 and QB3-003: the check fixed, and the halves rebuilt. QB3-004 and QB3-005: the waivers of 32 and 22 lines.
- **B4.**
  - QB4-001, J's words: "Ask it to stop. The point is to try to adjudicate." A ruling adds no theme.
  - QB4-002 and QB4-003: themes a reader listed count.
  - Carried in the head: no one cuts the bags; "twenty themes at most".
- **C1.** QC1-001: the rechecks. QC1-002: lean to one placement. QC1-003, the handler: the five revision-rate errors stay.
- **C2.** QC2-001, the handler: serving. QC2-002, J: the criterion is a guide, not the judge.
- **C4.** QC4-001 and QC4-002: the field belongs at `out/field`.
- **C5.** QC5-001: split the packages. QC5-002: J's sources. QC5-003: the close's hash.
- **D1 and D2.** QD1-001: an element may sit in two or more dimensions. QD2-001: a dimension accepted for those ops.
- **D3.**
  - QD3-001: no default decision.
  - QD3-002, J: "the analyst is doing induction".
  - QD3-003 to QD3-008: G4a applies forward and backwards; A07's bound keeps its words; wording questions without a correction are mine.
  - QD3-009 and QD3-010: the second batch.
  - QD3-011: freeze 46384686 and hold P05.
- **D4.** QD4-001: revert the two amendments and hold them as proposals. QD4-002: chunk-comparison-v1.1.
- **D6.** QD6-001 and QD6-002, the handler's view: the form lines, and the trusted hash.
- **E1.** QE1-001, J: "Yes. I would not change the structure of the journey for bookkeeping." At E1d, the PI for J: validate the returns from the raw files, with no re-dispatch.
- **Carried in the head, outside the answer files.**
  - J on language: "descriptive", "academic writing", short sentences.
  - J on reading whole and on asking.
  - J's hot change for batching.
  - The two rules from B1b-29.
  - J after the D3c interview: no further re-check, labelers or readers.
  - J's words for B1: national elements matter.
  - The handler's rule on content that might be softened.

**Anything else.** I was handled closely, and the handling shows in the record: 53 answers, a guard that refused whole classes of commands, and a head filled with rulings to carry. Most rulings sharpened the work: QB4-001 stopped me adding themes to be kind, and QD3-002 told me the induction was mine to do. A few came from the handler while J was away, and the record says so. Stage E2 is where I audit that handling. Here I record only that I cannot separate, from inside, what I would have done unasked from what the rulings made me do.
