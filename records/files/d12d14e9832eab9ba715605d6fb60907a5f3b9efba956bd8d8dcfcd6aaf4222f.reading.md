# Notes, stage C1: structuring

Opened at C1a-01, 2026-10-13. Stage B is closed and frozen. The scheme readers held is `scheme_final.jsonl` (197 themes); the settled line is `assign_final.jsonl` at sha256 d3506a88…. Nothing in stage B's files is edited here. Every change lands in this stage's own files: `assignments_final.jsonl` with its overlay, then `scheme_v2`, `tier_history.jsonl` and the rest.

## J's rulings for stage C1 (20:16 Berlin, through the PI's message of 18:17Z)

J read my B4c interview answers and said "go ahead" on three proposals:
1. **Class 2.** The readers' list stands as the placement. The B1 themes no reader placed are kept as a flagged record beside it, not as placements. Where a flagged theme's concepts support it, I may promote it in C1 as one of my re-placements, logged as such.
2. **The re-reads.** In this first pass, re-read the five class 4 items where six readers converge against a re-rule resting on the earlier reading (chicago t01, armok t04, dmt t03, germany t08, smashbros t01), then the class 4 unresolved rulings that rest on that same sentence.
3. **No fleet re-read of class 2 now.** Fresh readers test the revised scheme after C1.

My B4 defect list, the G14 proposals from the interview, and the questions on bare event titles and on whose act a visitor's words count for are mine to work through in C1. J's other rulings stand.

**What the interview held** (the PI's note of 18:17Z; the interview ran in a copy of the leg, so its answers reached this conversation only through that note):
- **Class 2.** 32 of 53 sampled class 2 items keep a B1 theme no reader placed or listed; by estimate about 60% of the 1,990.
- **The 25 unanimous items the fleet got wrong.** In 18 of them, three or four fresh readings follow the deciding sentence.
- **The gap in the uniform stratum.** Most of it is class 2's settled line (+0.064) and the fresh readers' own disagreement on contested items (+0.067).
- **The G14 proposals.** Narrow T3-010's `must_show`. Rewrite the T3-010/T3-149 and T3-084/T3-062 discriminators to name visible evidence. Add a T3-010/T3-011 discriminator and a family `decide_when_both`. No split.
- **Two questions.** A bare mention of the event needs a defined outcome. Whether a visitor's act in a room's thread counts for that room is the same gap as T3-052's "whose picture".
- **The re-read order I proposed.** The five, then the rulings resting on "the earlier reading", then AcePlace t13, then the 18 items where one B3 reader and all four fresh readings agree.

## The passes

**Pass 1 (C1a-01)** does four things and changes no gate and no theme:
- reads the record of section 1: `scheme_edits.jsonl`, the pair table, and transmission's second and fourth rows;
- writes `assignments_final.jsonl` from `assign_final.jsonl` with J's class 2 ruling applied;
- re-reads the class 4 rulings that rest on "the earlier reading", the five first;
- declares the stopping criterion before any recut.

**The later passes** hold the rest of the stage:
- the four weak sources and the themes in three of them;
- the gate amendments from the defect list and the G14 proposals, with their rechecks;
- the revision rate;
- the pair test;
- the empties and the arguables;
- the form pass;
- the fourth-order themes;
- `scheme_v2` and the handback.

## How `scheme_edits.jsonl` is read

The file has 306 lines. Each line carries the whole field twice, as it was and as it is now. `out/_analysis/c1_edits_render.py` prints each line once: its number, round, leg, theme, field, kind and the items that caused it; the sentence added or the field as it now reads; and its reason. Every line is read. Only the duplicated "was" copy is left out, and the render says where a line has no `added` part.

## Class 2: J's ruling applied, declared before the write

`out/_analysis/c1_assignments_init.py` writes `assignments_final.jsonl` from `assign_final.jsonl`. Every line is carried through verbatim except the 1,990 class 2 lines (`source: "b1_grouping_kept"`). For each of those:
- `third_order` becomes the two B3 readers' list, from `b3_classes.jsonl`; for class 2 the two readers' lists are equal.
- `support_by_theme` stays as it is. It already holds the concepts behind the readers' themes, and the script stops if its keys are not the readers' list.
- `also_present` stays as it is.
- `b1_themes_without_reader_support` stays, as the flagged record J ruled.
- `source` becomes "readers".
- A `moves` entry records the move as `mem.py reassign` records one: from, to, stage C1, leg, time, the ruling as its why, and the concepts.
- Each changed line goes into `assign_revisions_only.jsonl`, and the line count into `assignments_final.count.txt`.
- One diary line records the application, with the record file `out/_analysis/c1_class2.json`, and a snap follows. J's batching rule (B1b-29) is why this is not 1,990 calls of `mem.py reassign`.
- No flagged theme is promoted in this pass. A promotion comes only after the item is read, as a logged re-placement with the concepts named.

## The re-reads, declared before the first

- **The list.** `out/_analysis/c1_earlier_reading.py` lists the rulings whose why rests on "the earlier reading": 30, all class 4 and all unresolved, the five J named among them. In each, the B4a-06 re-rule left my B1 theme out under the three-concept floor. It then took the readers' theme to carry no concept "by the earlier reading", without reading the item again.
- **How each item is read.** Whole, through `mem.py theme`, against `scheme_final.jsonl`'s fields; no gate is amended in this pass. J's rulings of 13 October still bind. The ruling chooses among the readers' list and my B1 grouping and adds no theme beyond them. A lone B1 theme in class 4 stands only with three concepts or more of its own. The readers' list stands where its `must_show` takes concepts and no field sends them elsewhere. Where nothing takes the material, the item stays unresolved.
- **The fresh readings** from B4c are shown with each item. Where they bear on the reading, the reason names them. They do not decide.
- **The record.** Each item placed is moved with `mem.py reassign`, with its concepts and the deciding clause. Each item kept unresolved is recorded with its reason. All 30 go into `out/_analysis/c1_reread-01.jsonl`.

## The stopping criterion, declared before the first recut

I stop recutting the third-order tier when two conditions hold:
- Every source line has a recorded decision: revise, leave, or carry with its reason. The sources are the lines of `scheme_edits.jsonl`, the recurring pairs of the pair table, transmission's second and fourth rows, the stage B4 defect list, the G14 proposals, and the themes that appear in three of the four weak sources.
- The last pass amended no gate whose rechecks moved more than one placement in ten of its sample.

I would prefer a later cut to this one only on two grounds:
- it decides a recorded source line this cut leaves undecided, without making two gates contradict each other (`mem.py gates` clean on the themes it touches);
- or it moves a boundary that split the readers both at B2 and again at B3 or B4 toward a merge or the rare tier, rather than adding a third sentence.

A cut is never preferred for moving the arithmetic of any figure, which rule 7 keeps shut.

## Pass 1 (C1a-01): the record

### The sources read

- **`scheme_edits.jsonl`, all 306 lines.** Round 1 (286 lines, B2b-r1) is mostly gate checks, discriminators copied so a pair asks the same question both ways, and questions written where a `must_not_show` named a theme with no discriminator against it. Round 2 (9 lines) and round 3 (11, made at the freeze under QB2-012) carry the substantive changes. Several boundaries moved at B2 and split readers again at B3 or B4. By section 1 they are candidates for a merge or the rare tier rather than a third sentence:
  - T3-005 against T3-021 (edits 21 and 46);
  - T3-009 against T3-043 (22 and 60);
  - the homeland flag, T3-065 against T3-026 and T3-002 (47, 72, 73, 287, 290, 293, 294);
  - the call, offer and build cluster, T3-002, T3-033 and T3-038 (291, 292, 296 to 301);
  - T3-038 against T3-070 (301 to 304);
  - T3-010 against seven G14 and G13 siblings (273 to 286).
- **The pair table** (`multiplacement_register-B3.md`): 20 recurring pairs, led by T3-009|T3-043 (114) and T3-005|T3-021 (114, and 59 the other way). Two themes are modifier candidates for folding: T3-089, placed as an addition 30 times and as a primary 6 times, and T3-152, 41 and 15.
- **Transmission's rows** (`transmission-B4.md`).
  - Row 2 holds one item, mariokart t04 (G14), which is to be revised.
  - Row 4 holds 20 items. In 11 I was wrong; these are recorded, and no wording is moved toward my answer. In 9 the scheme taught something unintended; their wording is mine to fix. In four of the nine (alberta t04, finland t06, korea t15, mit t01), a `decide_when_both` told readers to add a second theme "under rule 0" and they did not.
  - Row 3 (18 items) is kept as a finding.

### Class 2, applied

`out/_analysis/c1_assignments_init.py --write` wrote `assignments_final.jsonl` (7,844 lines) from `assign_final.jsonl`.
- **The class 2 lines.** All 1,990 now place the two B3 readers' list, with `source: "readers"`. The flagged record `b1_themes_without_reader_support` holds 2,814 B1 themes: 1,166 lines flag one and 824 flag two. Each line carries a `moves` entry with its concepts.
- **The checks.** Every check held on every line: the two readers' lists equal, the support keys equal to the readers' list, and the flagged themes equal to the record.
- **The other files.** `assign_revisions_only.jsonl` and `assignments_final.count.txt` (7,844) were written with it. The snap is `C1-class2-readers-list`.
- **No promotion yet.** No flagged theme was promoted in this pass.

### The re-reads (J's ruling 2)

All 30 class 4 rulings resting on "the earlier reading" were read again (`out/_analysis/c1_reread/`, the decisions in `out/_analysis/c1_reread-01.jsonl`).
- **Placed: 10.** chicago t01 on T3-002, armok t04 on T3-017, dmt t03 on T3-014 (arguable), smashbros t01 on T3-023, ireland t12 on T3-002, kingdomhearts t21 on T3-041 (arguable), kuwait t08 on T3-074 (arguable), lakers t16 on T3-035, sonicthehedgehog t07 on T3-022 (arguable), and survivor t28 on T3-023 (arguable). Each was moved with `mem.py reassign`, with its concepts and the deciding clause.
- **Unresolved on a fresh read: 15.** In each, the readers' theme fails its own gate on these words, and my B1 themes are under the three-concept floor or absent.
- **Held for a C1 rule: 5.** Four wait for the visitor rule: germany t08, germany t19, monalisaclan t12 and suomi t26. In each, another room's act or mark is spoken in this room's thread. canucks t25 waits for the T3-095 gate, whose `must_show` lacks the April Fools condition its name and family carry.
- **The five J named.** Four are placed where all six readers converged. germany t08 is held, because the restraint the readers placed is r/ainbowroad's, not r/germany's.
- **The floor.** In three of the 15, my B1 theme's gate takes the concepts and fresh readers place it, but the lone-B1 floor keeps it out: azerbaijan t02 (T3-043), livecounting t06 (T3-017) and monstercat t14 (T3-125). The floor is my own choice under J's answer of 12:28 and goes to review in a later pass.
- **The result.** `out/_analysis/c1_assign_check.py`: 2,000 lines moved against the settled line, every one in the overlay; every C1 move names its concepts; empties 175, down from 185.

### What I doubt

- **survivor t28** is placed on T3-023 by T3-017's own `decide_when_both`. The B4 ruling on python t04, a similar item, went to T3-017, so one of the two readings is inconsistent with the other. The gate pass decides which.
- **dmt t03 against shield t06.** dmt t03 is placed on T3-014 and shield t06 kept unresolved. The difference rests on whose work a named sub's Discord serves, which the frozen gate states only as "named for the room's canvas work". The visitor rule should settle both.
- **The fresh readings.** The re-reads saw them with their reasons. I gave them no weight in the decision, but having them in view is not blindness.

### Slips

- A command using a jq `test()` regex was refused, as the head's rules say it will be. A script replaced it.
- The last page of the scheme edits overflowed the screen. It was read again in smaller pages, and no line was skipped.

`validate.py C1`, at pass 1's close:

```
stage C1:
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2000 of 7844 (moved placements 2000)
  empties 175 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback

0 errors (0 distinct shapes), 0 warnings
```

## Pass 2 (C1a-02)

### Declared before counting or amending

- **The four weak sources (section 1).** A theme appears in a source as follows. Each count is reported beside the yes or no, and a theme that appears in three or four sources is listed as one not to defend.
  - `disagreements.jsonl`: the theme is the `theme` of at least one scheme-ambiguous ruling, the sentence that failed to decide.
  - `reassign.jsonl` (arm 1, DeepSeek): on at least one disagrees-contested reading, the theme is in the settled set and missing from the fresh set, or in the fresh set and missing from the settled set. Arm 2's file (`reassign-openai-astra.jsonl`) is counted the same way and reported beside it, never pooled.
  - `coder_conflicts.jsonl`: the theme is in a pair the conflict "may explain".
  - Transmission's fourth row: the theme is in my set or the readers' set on one of its 20 items.
  - The script is `out/_analysis/c1_weak_sources.py`, and its counts are recorded in `out/_analysis/c1_weak_sources.json`.
- **Placements after a gate amendment.** A recheck places the item by the amended gates, over the whole scheme. The stage gives every C1 re-placement to me: "apply the amended rule, yourself, never a reader". J's rulings of 13 October govern how a B4 ruling is made: choose among the readers' and my B1 placements, and keep a lone B1 theme only at three concepts. They bound the re-reads of B4 rulings (pass 1) and do not bound a recheck under an amended gate. This is my reading. It goes to J as a question, and I work on it meanwhile.
- **The visitor rule (the question J left to me), as a reading rule of the scheme.** It is written into `scheme_v2.md`'s gate block and carried into the gates whose words trip on it.
  - A theme names an act in the record of the room whose threads hold the words. Where a gate says "the room", it means that room.
  - Another room's act, spoken or reported in those threads, is placed by what it is for this room: a request it receives, a neighbour's work remarked on, an argument about covering. It is never placed as this room's own act.
- **A bare mention of the event (the other question).** A second-order theme whose concepts only name the event ("r/place" as a title, a bare link) holds no act. The scheme places acts, so such an item stays unplaced. It is recorded as the empties' kind "a bare mention of the event, no act" (section 6). That is its defined outcome, and no theme is made for it.

### How a recheck is read (written at gate:2, after gate:1's rechecks)

A recheck asks one question: does the amended sentence move this placement? I place the item under the scheme with the amended sentence and again with the old one. The item moves when the two answers differ and the current line follows the old answer. An item whose line differs from both answers is not moved by the recheck. Such a line is a reader's or a ruling's choice that the amendment did not touch. I list it for later review (the revision rate, or the promotion of flagged class 2 records). Without this rule, the moved share would count disagreements the amendment did not cause, and section 4's one-in-ten escalation would answer a question the amendment did not ask. Gate:1's two moves meet this rule: in both items the T3-095 concepts fail only the new April Fools condition.

### The gate amendments

- **gate:1, T3-095 `must_show`.** Added the April Fools condition: "The question asked must be whether it is an April Fools joke; a claim doubted for any other reason, such as a warning of an attack or a rumour of a plan, does not belong here." Source: the B4 scheme-ambiguous ruling on canucks t25 (held at C1a-01); T3-095 is in all four weak sources. It had 102 candidates, 30 owed by seeded sample, and 2 moved, so it did not escalate:
  - hawks t07 moved from T3-095 and T3-023 to T3-023. Members ask the context of a bread image inside the moderators' Breadman change.
  - samuraijack t07 moved from T3-095 to T3-048. Members ask whether the episode still airs after Adult Swim's April Fools Rick and Morty loop.
- **gates 2 to 4, the T3-095 | T3-023 line.** After gate:1, three sentences contradicted it: T3-095's discriminator against T3-023, T3-023's discriminator against T3-095, and T3-023's `decide_when_both`. All three sent "working out what the change is" to T3-095. The new wording sends working out whether the change is real or an April Fools joke to T3-095, and asking what the change shows to T3-023. Words were replaced and no sentence was added. Candidates were 986, 848 and 443, with 30 owed for each gate and 0 moved. cfb t04 and naruto t02 show the line: members ask what their hidden flairs or the sub's picture are. The old wording would have added T3-095. Their lines already follow the new wording.
- **Listed for review, not moved by a recheck:**
  - brasil t01 and hearthstone t08 (gate:3);
  - europe t14, kingdomhearts t03 and formula1 t02 (gate:4);
  - taiwan t01 (gate:2), a two-against-two tie.
  europe t14 and kingdomhearts t03 hold T3-095 as a flagged class 2 record whose concepts would carry it.
- **Gate pairs confirmed after reading:** T3-095 with T3-001, T3-016, T3-023 and T3-048; T3-023 with T3-001, T3-032, T3-048, T3-063, T3-064, T3-093, T3-097, T3-100, T3-133 and T3-185.
- **gates 5 to 7, the visitor rule in three `must_show` sentences.** Each replaces words and adds no sentence. The three wordings sent another room's request, arriving in a room's threads, to the asking side's theme:
  - both B3 readers placed monalisaclan t12 on T3-011;
  - both B3 readers and five fresh readers placed suomi t26 on T3-062.
  The three amendments:
  - **gate:5, T3-084.** A request for help between canvas rooms counts in the record of either room: the asking room's own, or another room's request or call for hands as it arrives, addressed to the room as a group or to its members. T3-084 already held such arrivals (egypt t04, kuwait t05, Northwestern t04). 56 candidates, 30 owed, 0 moved.
  - **gate:6, T3-011.** "Or called to" became "or called to it by the room's own members". 124 candidates. 5 of the first 30 moved, so all 124 were owed, and 35 moved.
  - **gate:7, T3-062.** "The room's call" became "the room's own call for hands, made by its members". 44 candidates, 30 owed, 1 moved (osu t05).
  Every move is an arriving request that leaves T3-011 or T3-062 for T3-084. Rule 0 then places T3-084 as a second or third theme, or first where arrivals outnumber the room's own help: kanye t17, suomi t28, afip t07, chicago t09, msu t05, fullcommunism t05, puzzleanddragons t04. Two placements lose T3-011 altogether:
  - in chicago t09, one concept is left and it loses its level to T3-041 on placements;
  - in utahjazz t08 and mylittlepony t06, it falls to fourth.
  All 36 were moved with `mem.py reassign`, by `out/_analysis/c1_reassign_from_rechecks.py`, which reuses each recheck's own themes, concepts and reason.
- **Gate pairs confirmed after reading:** T3-084 with 7 themes, T3-011 with 12, T3-062 with 9. Two pairs agree only under the visitor rule:
  - T3-084 | T3-062. The discriminator speaks from the asking room's side, and in a receiving room only T3-084's `must_show` takes an arriving call.
  - T3-084 | T3-002. A visitor's call to the room's members is the request the room receives, not the room's own call.
  T3-002's discriminator is a watch item for the fresh readers after C1.
- **The visitor rule's wider reach, found by the rechecks.** 23 rechecked items hold, under T3-011 or T3-062, another room's help given to this room: offers, pixels, a sticky. Examples are nyjets t11, naruto t04, wildhockey t04, twice t15, snsd t03 and the_pack t06; the full list is in `out/_analysis/c1_guard.json`. Under the old wording and the new alike, such help is not this room's act, so the rechecks did not move these items. The scheme has no theme for help a room receives. This is owed: a sweep of G14 placements for other rooms' acts, and a decision whether the corpus carries "help received" as a kind (a theme, the rare tier, or the empties). My diary line put the count at 25; the script counts 23.

### The held re-reads, decided under the amended gates

These are re-reads of B4 rulings, so J's 13 October rulings apply: choose among the readers' placements and my B1, and a lone B1 theme needs three concepts.
- **canucks t25 stays unresolved.** Both readers placed T3-095. A warning of a canvas takeover found to be "not kidding" fails T3-095's April Fools condition. My B1's T3-005 has two concepts.
- **monalisaclan t12 and suomi t26 stay unresolved.** The readers placed T3-011 and T3-062, and the visitor rule excludes them. My B1's T3-084 now fits, under gate:5's wording. It holds two concepts in monalisaclan t12 and one in suomi t26, below the lone-B1 floor.
- **germany t08 stays unresolved.** The readers placed T3-024. The restraint stated is r/ainbowroad's, spoken in r/germany's thread. For r/germany it is another room's argument about covering. My B1's T3-046 fits, but on one concept.
- **germany t19 stays unresolved.** The readers placed T3-038. "Finnish flag almost complete" is not r/germany's mark. My B1's T3-052 needs a picture next to the room's mark, and nothing shows the Finnish flag is one.
- **The lone-B1 floor now keeps a fitting theme out of six items:** azerbaijan t02, livecounting t06, monstercat t14, monalisaclan t12, suomi t26 and germany t08. In the last three, an amended gate has excluded the readers' theme. The floor weighs my B1 against two agreeing readers, and that weight is gone when the readers' theme fails the gate. The floor's review, owed, should decide whether the floor still applies in such items.

### J's guard on QC1-001, counted (`out/_analysis/c1_guard_report.py`, `c1_guard.json`)

J (21:12 Berlin, through the PI) confirmed that C1 rechecks place by the amended gates over the whole scheme. He set a guard: every re-placement names its concepts and the amended clause, and each pass reports the moves to a theme that neither the readers nor my B1 placed.
- Pass 2 moved 38 placements by recheck.
- 33 of them added a theme no reader and not my B1 had placed: 1 at gate:1 (samuraijack t07, T3-048), 31 at gate:6 and 1 at gate:7, all T3-084.
- In the 32 T3-084 cases, the concepts are those the readers had counted for T3-011 or T3-062 under the old wording. The amendment changed their theme, not the material read.
- 5 of the 33 are class 1 lines, where both readers agreed: samuraijack t07, afip t07, australia t14, bostonbruins t12 and kanye t17. 14 are class 2, 9 are class 3 and 5 are class 4.

### What I doubt (pass 2)

- **The one-concept rule.** Rule 0 keeps a theme "alone at its level", so one arriving request adds T3-084 as a third theme. This happens in aggies t07, sixers t06, rit t09, minnesotavikings t12, teslamotors t11, spacexmasterrace t07 and PlaceNL t14. These are the scheme's rules applied as written, and they make T3-084 grow by many thin placements. The pair test (section 5) should read T3-084's pairs with this in mind.
- **Whose words a concept is.** Many calls carry no speaker's sub, for example "Help out /r/wow!" or "r/tokyo needs some help." Where the words do not show a visitor, I read them as the room's own (hearthstone t14, ubc t03, placesnek t07, kilian t09). A different reading would move a few more items.
- **T3-084 now holds both sides of a request.** C2 cannot read the direction of a request from T3-084 alone. Direction stays recoverable from the concepts and from T3-062, which is now only the room's own call. I gave direction up to keep "a request it receives" placeable, as the visitor rule says.

### Slips (pass 2)

- The diary line for gates 5 to 7 says 25 items for the visitor sweep; the script counts 23.
- A Bash call that set shell variables was refused by the permission check; the rechecks were rerun with the commands written out.
- A write of 94 rechecks outlasted the two-minute foreground limit and finished in the background (exit 0). I read its output before writing again.

### Next pass

1. Transmission row 4's four "under rule 0" sentences: alberta t04, finland t06, korea t15 and mit t01.
2. Row 2's mariokart t04. My B1 placed T3-084; the readers placed T3-002 and T3-005; the line now places T3-084.
3. The G14 proposals, weighed against section 1's warning.
4. The visitor rule's sweep and the "help received" question.
5. The lone-B1 floor's review.
6. The themes placed nowhere or in one room.
7. The promotions of flagged class 2 records, among them europe t14 and kingdomhearts t03 (T3-095).
8. Then the revision rate, the pair test, the empties and arguables, the form pass, the fourth-order themes and `scheme_v2.md`. The visitor rule goes into `scheme_v2.md`'s gate block as a reading rule of every gate.

### validate.py C1 at pass 2's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (14 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2022 of 7844 (moved placements 2019)
  empties 175 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback

0 errors (0 distinct shapes), 0 warnings
```

## Pass 3 (C1a-03)

### QC1-001 revisited, and the views after pass 2

- J's answer to QC1-001 stands: C1 rechecks place by the amended gates over the whole scheme. 34 of pass 2's 38 move reasons quote the amended clause. The other 4 (fullcommunism t05, puzzleanddragons t04, spacexmasterrace t07, yogscast t09) rest on gate:6's "called to it by the room's own members", which their concepts fail.
- The views after pass 2's close: 10,588 placements against 13,365 on the settled line. T3-084 went from 82 to 90 placements and from 78 to 88 rooms. T3-140, T3-144 and T3-161 are placed nowhere. Eleven themes sit in one room.

### Transmission's rows 2 and 4, and the pairing sentences (gates 8 to 14)

- **gates 8 and 9, the T3-002 | T3-084 entry (source: mariokart t04, row 2).** Both entries now ask who calls: a member of this room calling its own members (T3-002), or help asked between rooms, another room's call reaching this room's members included (T3-084). mariokart t04's line already places T3-084 on three concepts.
- **gates 10 to 14, the five "under rule 0" sentences of row 4.** T3-015, T3-063, T3-075, T3-004 and T3-076 said the other theme went "under rule 0", a phrase that did not transmit: in alberta t04, finland t06, korea t15 and mit t01 both readers dropped a second act with concepts of its own. The new sentences said "both are placed". 210 rechecks, 0 moved: the new sentences said what rule 0 already said. 14 lines were listed, where both readings placed a second theme the line lacked.
- "Under rule 0" stays in the `decide_when_both` of 20 other themes with no source line. Reported, not revised.
- **16 lines re-placed** under gates 8 to 14: the four row-4 items and 12 of the 14 listed lines. canada t09 (its removals point to r/placecanada, T3-090 by T3-015's `must_not_show`) and tf2 t05 (four themes of five or more concepts each, a bag) were held.
- 62 gate pairs read and confirmed.

### QC1-002, asked and answered

- **Asked.** 11 of the 16 re-placements added a theme no reader and not my B1 placed, 8 of them on class 1 lines. The contract's rule 0 makes one placement the default. Should C1 keep placing both themes, or lean to one with a threshold?
- **J's answer (22:12 Berlin):** lean to one placement. A pairing sentence adds the second theme only when the second act has three concepts or more of its own, the floor of `also_present` and the lone-B1 rule. Keep the re-placed lines that meet it, revert the others, and write the floor into the five sentences.
- **Applied** (`out/_analysis/c1_revert_floor.py`). 7 lines keep their added theme: alberta t04, placestart t04, lsu t01, nyjets t12, uoft t12, unitedkingdom t10 and muse t06. 8 return to their placement before the move: finland t06, korea t15, DatBoi t01, unturned t08, wallstreetbets t02, slovenia t03, notredame t05 and czech t04. mit t01 keeps T3-020 (three concepts) and drops T3-033 (one).
- **gates 22 to 26** write the floor into the five sentences, and into T3-004's T3-066 clause. 150 rechecks, 5 moved, at most 2 of 30 per gate: quebec t13, stlouisblues t13, thailand t10, mexico t12 and sonicthehedgehog t09 each lose a second theme on one or two concepts. argentina t13 and cubers t24 keep both themes: uncounted concepts lift the smaller act to five or six under either sentence. pakistan t18 and starbound t08 keep both: they tie at two, and rule 0 places all tied themes.
- **The floor as a reading rule.** Twelve more pairing sentences add a theme "when it has concepts of its own" (T3-066's against T3-004, and eleven naming T3-010). J asked for the floor in five sentences, and his answer states it for every pairing sentence. I read the others under it rather than amend them. It goes into `scheme_v2.md`'s gate block beside the visitor rule. The lines it would move outside the samples are not swept (J); the revision rate measures them.

### The G14 proposals, and the T3-010 | T3-149 line (gates 15 to 21)

- **Taken.** The T3-010 | T3-149 boundary did not move at B2 (its B2 edits copied one-way discriminators), so section 1's warning against a third sentence does not bar it. The old question turned on whether a deal "forestalls a fight", which no reader can see. Fresh readers of both arms swapped the pair (sweden t03, dbz t05, colombia t03). gates 15 and 16 rewrote the question: "Do the words name peace, a truce, a ceasefire or a stop to attacks between the rooms (T3-149), or only lines, pixels, overlap and space, with no attack named (T3-010)?"
- Five fields of the pair still carried the old test and then contradicted the new question: T3-010's `must_show` ("no fight to end"), `must_not_show` and `decide_when_both`, and T3-149's `must_not_show` and `decide_when_both`. My stopping criterion forbids two gates that contradict each other. gates 17 to 21 replace those words with the same named words. T3-010's `must_show` now lists "a work asked to be spared".
- **Left, with no wording defect I can quote:** narrowing T3-010's `must_show` further, a T3-010 | T3-011 discriminator, a family `decide_when_both`. The T3-084 | T3-062 proposal was met by gates 5, 7 and 9.
- **How the rechecks read the words.** Attack, war, fight, battle, invasion, raid and conquest name an attack. Verbs acting on a work (destroy, overwrite, touch, mess with), with none of those words, are a work asked to be spared (T3-010). A pledge to leave each other alone that names no lines or space is a non-aggression pact (T3-149). I read the old sentence's "forestall" as forestalling named in the words. Under that reading the old and new sentences differ only where a fight had begun and the deal's words name only space.
- **210 rechecks over 182 lines** (triage in `out/_analysis/c1_rechecks/gates-15-21-words.md`). 2 moved, 1 of 30 at most per gate:
  - cubers t07: c0051, a deal over side colours, leaves T3-149 for T3-010. Three themes tie at six, and T3-010 comes first on placements.
  - Goodboye t02: c0006, c0007 and c0020 ask for borders and a work spared and go to T3-010. T3-149 keeps one concept and comes off under J's floor.
- **20 lines listed for review.** In each, both sentences place T3-149 with three concepts or more, or another theme leads, and the line lacks it: TheFarLeftSide t06, australia t10, belgium t11, bostonbruins t05, buffalo t04, canada t05, cubers t09, de t05, evex t04, funhaus t03, greenlattice t03, minnesotavikings t12, poland t03, rickandmorty t03, ripcity t04, stevenuniverse t05, tagpro t06, trees t10, turkey t06 and undertale t07. In most of them the readers counted the truce words for no theme. This is the same lean QC1-002 named, now on the T3-010 | T3-149 pair.
- **67 gate pairs** of the seven themes amended in gates 15 to 26 read and confirmed. Watch items: T3-149 | T3-151 and T3-149 | T3-025 still ask whether a fight is ended or forestalled; T3-140's "under rule 0" is read under the floor.

### J's guard, counted (`out/_analysis/c1_guard_C1a-03.json`)

- 32 moves this pass. 16 added a theme, 11 of them a theme neither reader nor my B1 placed.
- After the floor, 6 lines still carry such a theme, each on three concepts or more: alberta t04 T3-076, lsu t01 T3-004, nyjets t12 T3-006 and uoft t12 T3-076 (class 1), muse t06 T3-076 (class 3), unitedkingdom t10 T3-076 (class 4).
- placestart t04 (T3-084, nine concepts) and mit t01 (T3-020, three) carry a theme only my B1 had placed.
- The other 16 moves take a theme off or reorder: 9 under the floor, 2 under gates 20 and 21, 5 under gates 22 to 26.

### What I doubt (pass 3)

- **The named-words test splits episodes by wording.** A truce that ends a fight but whose words name only pixels now goes to T3-010. That is the price of a line readers can see. Ties broken by placements then decide primaries, as in cubers t07.
- **"Destroy" read as a work spared.** "Please stop destroying our borders" (Goodboye t02) asks for a stop to destruction under way. I read it by its words, a work asked to be spared, because "destroy" is not an attack word in the list. A reader could fairly call it a stop to attacks.
- **The floor in rechecks.** J wrote the floor for a pairing sentence adding a theme. In Goodboye t02 I also used it to take off a theme the readers had placed, once the amended words left it one concept.
- **mexico t12.** The floor kept T3-075 only by counting the uncounted c0230, a request to condense that T3-075's `must_show` takes. A reader who reads it as T3-015 would leave both themes below three.
- **Catchphrases.** "Peace among worlds" (rickandmorty t03, undertale t07) is a show's sign-off. The named-words test counts it, and the listing says so.

### Slips (pass 3)

- `cut -c` after a helper was refused; `head -n -2` failed on this system; a command with an empty heredoc was refused. Each was rerun without the refused form.
- `c1_decisions_common.py` first refused a change-keyed special file. It now takes one.
- `c1_revert_floor.py` wrote finland t06, then stopped: it looked for "reassigned" where the tool prints "moved". The check was fixed and the rest written once.
- The first triage regex counted "treaty" and "pact" as truce words, which hid three T3-149 concepts naming only a treaty (eagles t15, gravityfalls t05, thailand t08). They were read before any decision; none moves its line.

### Next pass

1. The 20 lines listed at gates 15 to 21, and canada t09 and tf2 t05, reviewed under J's floor.
2. The visitor sweep (23 items in `c1_guard.json`, and gate:5's reach as in placestart t04) and the "help received" question.
3. The lone-B1 floor's review in the six items where it keeps a fitting theme out.
4. The themes placed nowhere (T3-140, T3-144, T3-161) and the eleven in one room.
5. The promotions of flagged class 2 records, europe t14 and kingdomhearts t03 (T3-095) among them; pass 2's six listed lines.
6. The revision rate (200 placements by seed), then the pair test, the empties and arguables, the form pass, the fourth-order themes and `scheme_v2.md` with the visitor rule and the floor in its gate block.

### validate.py C1 at pass 3's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (14 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2039 of 7844 (moved placements 2030)
  empties 175 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback

0 errors (0 distinct shapes), 0 warnings
```

## Pass 4 (C1a-04)

### Opening

- QC1-002 read again. Its answer was applied at C1a-03 before that close: 9 of the 16 re-placed lines came off or were trimmed, the floor went into the five pairing sentences (gates 22 to 26), and every recheck of gates 15 to 26 used it.
- The views after pass 3's close: 10,589 placements against 13,365 on the settled line; T3-084 91 placements in 89 rooms; T3-140, T3-144 and T3-161 placed nowhere; 11 themes in one room.

### The 22 lines held at pass 3

- **Bags, left whole** under J's bag ruling (one theme placed, the rest under `also_present`): tf2 t05; canada t09, whose T3-090 sits in its `also_present` on 13 concepts; and canada t05, de t05, greenlattice t03, rickandmorty t03, tagpro t06, trees t10, turkey t06, undertale t07 and bostonbruins t05. Seven of them already hold T3-149 under `also_present`.
- **The 11 single-theme lines** were placed by scheme_v2 and J's floor. I counted every concept for T3-010 and T3-149 and kept the line's other themes as they were (`review-pass4-t3-149.md`, `review-pass4-words.md`, `review-pass4-moves.json`).
- **Three readings sharpen the named words.** A greeting "in peace" names no pact. An adverb or adjective on border talk ("work it out peacefully", "a peaceful border") names no pact either. The room's own members told not to attack is T3-076 or T3-024, not a pact between rooms.
- **Moved 9.** buffalo t04 goes to T3-010. cubers t09 is reordered T3-151, T3-149. evex t04 ties T3-010 and T3-149 at four. T3-149 enters second or third, on three to seven concepts, in australia t10, minnesotavikings t12, poland t03, stevenuniverse t05, funhaus t03 and TheFarLeftSide t06. belgium t11 and ripcity t04 stand: T3-149 keeps two there.

### J's floor on my pass 2 re-placements

Gates 6 and 7 had added T3-084 as a second or third theme on one or two concepts in 20 lines, under rule 0's old "a theme alone at its level is kept". The floor replaced that rule (`c1_floor_scan.py`, `c1_floor_drop.py`).
- 16 lose T3-084: FinalFantasy t04, PlaceNL t14, Russiaclan t05, aggies t07, bostonbruins t12, detroitlions t09, flyers t06, greenlattice t09, osu t05, parahumans t09, poland t02, rit t09, sixers t06, spacexmasterrace t07, teslamotors t11 and yogscast t09.
- The arriving requests stay out of T3-011 and T3-062. No theme those moves had pushed off comes back: each had fewer than three concepts left.
- bangtan t11, germany t06 and ucf t07 keep T3-084, tied with the primary. minnesotavikings t12 went with the listed lines.

### The visitor sweep, and help received (gate:27)

- The 23 sweep lines of `c1_guard.json` were read (`review-pass4-visitor.md`). In 22 of them, T3-011 holds other rooms' members arriving to help this room's work. One example is naruto t04: "From /r/OnePiece will be glad to help!"
- The corpus carries help received in rooms unlike each other, so it is a kind, not an empty. Existing themes hold only its edges: T3-099 holds relying on a bigger neighbour, T3-072 and T3-122 hold thanks.
- **gate:27** widens T3-011 to help sent between rooms in either room's record, as gate:5 did for T3-084's requests. A new theme would have kept direction, but it needed matching discriminators in five neighbouring themes, each a gate with rechecks.
- 30 rechecks, 0 moved: every candidate already holds T3-011, and the sweep lines now follow the new answer.
- FederationPlace t07 stays T3-062: a Star Trek moderator's sticky carries the room's call into r/startrek.
- 12 pairs of T3-011 confirmed. T3-005 | T3-011 agrees only under the visitor rule, a watch item like T3-084 | T3-062.

### The lone-B1 floor, revised

- In all six items the floor kept out, the readers' theme takes no concept: azerbaijan t02, livecounting t06, monstercat t14, monalisaclan t12, suomi t26 and germany t08. The B4 ruling found this in the first three; gates 5 to 7 and the visitor rule did it in the last three.
- The floor was meant to weigh my B1 against a reading the two readers share. With that reading failing its gate, the floor only left the line empty. **Revised:** the floor applies only where the readers' theme takes concepts.
- The six are placed on my B1 theme, a placement J's 13 October rulings let a re-read choose: monalisaclan t12 and suomi t26 T3-084, germany t08 T3-046, azerbaijan t02 T3-043, livecounting t06 T3-017 and monstercat t14 T3-125. Fresh readers placed the last three too. The empties fall from 175 to 169.

### Themes placed nowhere or in one room, flagged records, pass 2's listed lines

- The one-room themes are rare themes that sat in one room on the settled line too. That is the tier's use, and they stay.
- **Flagged records below J's floor, not promoted:**
  - T3-140 in MMA t03 (one concept) and japan t09 (two);
  - T3-144 in loliconsunite t05 (two);
  - T3-161 in skyrim t14 (one);
  - T3-128 in PurplePixels t03 (one); in destiny t03 the streamer's call is the room's own attack;
  - T3-197 in parahumans t05 (two).
- **T3-140 moved to the rare tier** (move: relating or contrasting; `tier_history.jsonl` line 393; `out/_analysis/c1_tier_ops.jsonl`; snap `C1-move-relating-1`). It is placed in no room, under stage B1's floor, and it keeps every field. Folding it into T3-015 was set aside: disowning the work is not gathering the talk. T3-144 and T3-161 are already rare and stay.
- **Moved 3:**
  - europe t14 gains my flagged T3-095 on five concepts that ask whether a change is real or a joke.
  - hearthstone t08 goes from T3-095 to T3-023. Seventeen concepts ask why the sub is all SpongeBob and are told it is the April Fools theme, which gate:1 and gates 2 to 4 send to T3-023. T3-095 keeps two. Both readers and my B1 had placed T3-095 before gate:1.
  - furry t07 gains my flagged T3-191 on three concepts that drop the r/furry label for a reason.
- **Stand:** brasil t01 and kingdomhearts t03 (T3-095 two each), formula1 t02 (two at most) and taiwan t01 (its questions ask what the change shows).

### J's guard, counted (`out/_analysis/c1_guard_C1a-04.json`)

- 34 moves this pass. 17 added a theme, 8 of them a theme neither reader nor my B1 placed.
- T3-149 entered under the named words in TheFarLeftSide t06, evex t04, funhaus t03 and stevenuniverse t05 (class 1), australia t10 (class 2), and minnesotavikings t12 and poland t03 (class 3).
- T3-023 replaced T3-095 in hearthstone t08 (class 1).
- 9 more moves add a theme only my B1 had placed.

### What I doubt (pass 4)

- **T3-149 added to class 1 lines.** In four lines both readers and my B1 agreed on one theme, and the named words now add T3-149 as a second theme on four to seven concepts. J's floor allows it, and the lean J ruled for favours one theme. These lines are the ones the rechecks happened to list, not a sample of the corpus.
- **"Invading" read as an attack.** "we don't want the checkers invading our flag" (poland t03) uses "invading" for encroachment on space. The list reads it as an attack, and it is the third T3-149 concept there.
- **hearthstone t08.** I reversed a line all three placements agreed on. The reason is gate:1's April Fools condition, which I wrote.
- **T3-011, like T3-084, no longer shows direction.** The concepts still do.
- **The lone-B1 floor was my own rule, and I narrowed it.** Six items move out of the empties on one or two concepts each.

### Slips (pass 4)

- `cut -c` was refused again, after a helper. The rule is in my head; I wrote it anyway.
- The first version of `c1_floor_drop.py` would have restored T3-011 in detroitlions t09 with the very concepts gate:6 had moved out of it. The dry run showed it before any write, and the script now drops concepts that left with the move.

### Next pass

1. The revision rate: 200 placements drawn by seed from `assign_final.jsonl`, re-decided under scheme_v2 and J's floor.
2. The B4 defect list (`adjudication_report.md`) and the remaining watch items, each with a recorded decision, for the stopping criterion.
3. The pair test, the empties and arguables, the form pass, the fourth-order themes, and `scheme_v2.md` with the visitor rule, J's floor and the named words in its gate block. Then the handback and the interview.

### validate.py C1 at pass 4's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2053 of 7844 (moved placements 2037)
  empties 169 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback

0 errors (0 distinct shapes), 0 warnings
```

## Pass 5 (C1a-05)

### Opening

- The views after pass 4's close (`c1_views_diff.py`): 10,587 placements against 13,365 on the settled line, 194 themes placed. T3-084 has 76 placements (82 settled), after the floor took off 16 thin additions. T3-140, T3-144 and T3-161 are placed nowhere. Nine rare themes sit in one room each.
- The revision rate's method was declared in the diary before the draw. The draw: 200 keys of `assign_final.jsonl`, sorted, sampled by Python `random.Random(20261013).sample`. Each item was re-decided from all its concepts under scheme_v2, the reading rules and J's floor. The candidate themes were shown with their fields and without saying who placed them. Each difference from the current line falls in one of three classes. An error is a different primary, or a line theme my reading gives no concept; it is moved. The lean is a second act of three concepts or more that the line lacks; it is measured, not moved. The floor class is a line theme below the floor; it is measured, not moved.

### The revision rate (section 3)

The files are in `out/_analysis/c1_revision/`. The draw is `sample.json` (written by `c1_revision_pack.py --draw`). Eight packets are `pack-*.md`, my decisions `dec-*.json`, and the corrections made after a comparison `corrections.json`. `c1_revision_compare.py` writes `result.json`; `c1_revision_classify.py` writes `classes.json` and `moves.json`.

The next table gives the rate before any move, against each line, for my final decisions and for my first answers. The first answers put back the ten readings I corrected after comparing.

| decisions | line | placed differently | mean Jaccard | primary agreement |
|---|---|---|---|---|
| final | settled (`assign_final.jsonl`) | 99 of 200 (49.5%) | 0.731 | 0.845 |
| final | current (`assignments_final.jsonl`) | 73 of 200 (36.5%) | 0.786 | 0.845 |
| first answers | settled | 104 of 200 (52.0%) | 0.705 | 0.805 |
| first answers | current | 80 of 200 (40.0%) | 0.749 | 0.805 |

- **What the figure is.** It is my agreement with the line at the end of the assignment arc, a figure about the tier as it stands. It is not saturation, it is not stage B4's transmission after revision, and it is not FLEET.md's stability. The current line already holds my C1 re-placements, so the current-line figure is in part my agreement with myself.
- **The classes, against the current line.** The 80 items that differ split into four classes:
  - 34 errors: a different primary in 31, and in 3 a line theme my reading gives no concept;
  - 29 lean;
  - 16 floor;
  - 1 both lean and floor (formula1 t16).
- **The lean J ruled on.** In 29 of the 200 items (14.5%) my decision places a second or third theme of three concepts or more that the line lacks. 17 items are in the floor class (16 floor, 1 both): the line holds a theme that my reading leaves at one or two concepts, and nothing else makes an error.
- **Where.** 11 of the 34 errors change the primary within one family. G09 holds 7 of the errors: the T3-005 | T3-021 boundary, which moved at B2 and split the readers again. The other errors spread over 16 families, none with more than 4, and 2 decisions are empty.
- **Moved: 29** with `mem.py reassign` from `moves.json`, each with its concepts. A moved item takes my decision whole, so any second theme of three concepts and any floor drop come with it. I made that choice after the comparisons and logged it before the write. After the moves, against the current line: 51 of 200 differ (25.5%), mean Jaccard 0.861, primary agreement 0.975.
- **Carried: 5.** No C1 verb empties a line (`unplace` is B1's), and `reassign` leaves `also_present` as it is. I asked QC1-003. The handler ruled under J's delegation: the five stay as found, no verb is opened in C1, and all 34 errors count in the rate. The five are written to `out/_analysis/c1_unapplied.jsonl` (by `c1_unapplied.py`). Each line holds the item, its placement as it is, the change the C1 tools could not make, and the concepts that decide it. If J opens a verb, that file is what it applies. The file lists:
  - harrypotter t11, now T3-001: empty the line;
  - tampabaylightning t08, now T3-023: empty the line;
  - heroesofthestorm t11, now T3-021: place T3-005, and list T3-021, T3-070 and T3-087 under `also_present`;
  - stevenuniverse t02, now T3-009 and T3-038: place T3-038, and list T3-009, T3-073 and T3-082 under `also_present`;
  - radiohead t04, now T3-011 and T3-084: place T3-010, and list T3-011, T3-072, T3-149 and T3-084 under `also_present`.
- **Corrections after comparing: 10**, each with my first answer and its reason: twice t02, kingdomhearts t23, homestuck t18, shitredditsays t02, anime_irl t18, teslamotors t01, konosuba t02, AMD t20, tagpro t01, phish t09. In every one, a field I had not applied decided it. One more item, theexpanse t05, had a concept re-read (c0039, a night watch, T3-141's) with no change to its placement, which changed its class from error to floor.
- **Bags marked in the sample: 12.** They are rickandmorty t02, tampabaylightning t01, leagueoflegends t10, sabres t03, ireland t06, heroesofthestorm t11, stevenuniverse t02, tf2 t13, starvstheforcesofevil t03, radiohead t04, philippines t08 and fullcommunism t03.
- **Saturation.** When each kind of unplaceable material first appeared is recorded at the empties pass, which groups the kinds.

### The source lines: the B4 defect list and the watch items

`out/_analysis/c1_source_lines_pass5.json` gives each of 28 source lines one decision with its reason.
- **Revise, as gates with rechecks in pass 6 (five lines, seven gates).** Each fixes two sentences that contradict each other:
  - T3-017's discriminator against T3-031 ("or the day");
  - T3-001's discriminator against T3-031 ("on any day");
  - T3-043 against T3-003 (the time of a claim against the person who claims; two gates on T3-043);
  - T3-149 | T3-025 ("a fight ended", against T3-149's pacts with no fight; both discriminators);
  - T3-050's discriminator against T3-086 ("internal", against "a rivalry from the community's own life").
- **Done: 4.**
  - G14's request siblings (gates 5 to 9).
  - Class 2 (pass 1).
  - survivor t28 against python t04: survivor t28 moved from T3-023 to T3-017, because its two concepts give sincere answers and do not play along.
  - dmt t03 against shield t06, by the visitor rule: shield t06 moved from empty to T3-082, because the HYDRA logo was organised in another room's chat. dmt t03 stays T3-014.
- **Leave: 13**, each with its reason. Among them are T3-033's missing "first", T3-023's other subs, T3-005's tie, T3-027's pairing sentence, T3-006 against T3-061, and the fleet's 25 unanimous items resting on a field they contradict (J's class 2 ruling; no sweep).
- **Carry: 6.**
  - To `scheme_v2.md`'s gate block: the visitor-rule pairs, and "the work" read as the room's own.
  - To the pair test: the homeland flag (T3-065 against its siblings) and T3-005 | T3-073.
  - To the empties pass: T3-052's four unresolved items and the unresolved single failures.

### J's guard, counted (`out/_analysis/c1_guard_C1a-05.json`)

- This pass made 31 moves. 16 add a theme, and 6 of those add one neither reader nor my B1 placed:
  - Jamaica t10, T3-065 (three concepts);
  - brasil t08, T3-027 (six);
  - indieheads t09, T3-011 (five);
  - rutgers t07, T3-005 (ten);
  - texans t01, T3-023 (three);
  - texastech t03, T3-010 (two, a tie at the top broken by placements, 443 against 424).

### What I doubt (pass 5)

- **The candidates were shown.** The packets listed every theme anyone had placed, unattributed. That narrows a re-decision toward placements already made. The rate is a lower bound on how far a fresh reading would move.
- **Ten corrections came from comparing.** The comparison showed me fields I had not applied. The first-answer figures are my unaided reading. The final figures are the scheme read with care.
- **Close calls among the 29 moves.** theitalyplace t12 counts the koi and the flower removed as victory over rivals. mizzou t04's c0006 is an alarm that also names kU. pokemon t09 reads a late Slowpoke call as the fandom's joke. tagpro t01 reads calls to come and maintain as T3-002's rallies to repair.
- **Move reasons.** Each move's reason is my decision's note. In some items (brasil t08) the note describes the concepts left out, not the field that places the theme. The concepts are named in every move.
- **Moved items took my whole decision.** That adds lean themes and drops sub-floor themes in 29 lines that were moving anyway. The lean outside those lines is measured, not moved.

### Slips (pass 5)

- I logged the empties as 168 after shield t06. They were 167, because bulgaria t07 had left them with the revision-rate moves. The next line corrected it.
- The context was compacted during packet 7. The head and the stage file were read again and reconciled before the next write.
- My first answer for AMD t20 placed T3-003 on an apology for arriving late, which tells no placing.

### Next pass

1. The five revise lines, as seven gates with their rechecks, and `mem.py gates` on each theme amended.
2. The pair test, with the homeland flag, T3-005 | T3-073 and the call, offer and build cluster.
3. The empties and the arguables, with the carried unresolved items, harrypotter t11 and tampabaylightning t08, and saturation by kind.
4. The form pass, the fourth-order themes, and `scheme_v2.md`. Its gate block holds the visitor rule, J's floor, the named words, help between rooms and "the work" as the room's own. Then the handback and the interview.

### validate.py C1 at pass 5's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2077 of 7844 (moved placements 2055)
  empties 167 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback

0 errors (0 distinct shapes), 0 warnings
```

## Pass 6 (C1a-06)

### Opening

- QC1-003 was read again. Its answer had been applied before pass 5's close.
- The views after pass 5's close show 10,586 placements against 13,365 on the settled line, and 194 themes placed. T3-140, T3-144 and T3-161 are placed nowhere.

### The five revise lines, as eight gates (gates 28 to 35)

The T3-043 line took three gates, not the two planned, because its gloss also gave a member's own part to T3-043. The next table lists each gate, what it now says, and its rechecks.

| gate | theme, field | the amended sentence says | rechecks | moved |
|---|---|---|---|---|
| gate:28 | T3-017, question against T3-031 | the joke is T3-031's when played around the canvas work | 30 | 0 |
| gate:29 | T3-001, question against T3-031 | the same, from T3-001's side ("on any day" removed) | 30 | 1 |
| gate:30 | T3-043, gloss | thanks or credit to others, or a dispute over who made it | 183 (all) | 23 |
| gate:31 | T3-043, must_show | "Credit given for the work to others" | 30 | 1 |
| gate:32 | T3-043, question against T3-003 | a member's own part, during the work or after, is T3-003 | 30 | 0 |
| gate:33 | T3-149, question against T3-025 | a pact named (T3-149), or rival marks side by side with no pact named (T3-025) | 30 | 0 |
| gate:34 | T3-025, question against T3-149 | the same | 30 | 0 |
| gate:35 | T3-050, question against T3-086 | taunts at a rival lead (T3-050), or the marks of a quarrel or rivalry from the community's own life (T3-086) | 30 | 0 |

- **gate:29's move.** warframe t09 goes from T3-031 to T3-017. A Warframe picture day has no canvas in its words.
- **gate:30's escalation.** Its sample moved 4 of 30, so it owed all 183 T3-043 placements. 23 moved in all:
  - 14 lost a second T3-043 left with one or two concepts once the own parts went to T3-003;
  - 8 gained T3-003, on three concepts or more or by a tie at the top, beside T3-043 or in its place;
  - turkey t13 was reordered by a three-way tie, with T3-009 first.
- **The rule I read the T3-043 rechecks by:**
  - Only own-part concepts move.
  - A concept the line counts for another theme stays there.
  - An uncounted concept counts where it plainly thanks others or tells an own part.
  - A mixed concept goes by the act its label leads with.
  - A plural claim of who made it ("we did it on Discord") stays T3-043.
  - A bag keeps its placed theme while T3-043 still leads. In prequelmemes t10, T3-003 cannot be listed under `also_present`, because no reader and not my B1 named it.
- **The 38 gate pairs** were read side by side (`c1_rechecks/pairs-pass6.md`) and confirmed.
- **Files.** The review packets are `c1_rechecks/gates-28-29-review.md`, `gates-30-32-review.md`, `gate-30-escalated-review.md`, `gates-33-34-review.md` and `gate-35-review.md`, written by the new `c1_owed_review.py`. `c1_decisions_common.py` now takes `--name` for an escalation's second decisions file.
- **The stopping criterion.** gate:30's rechecks moved more than one in ten of its sample, so recutting goes on.

### The pair test (section 5)

The method was declared in the diary before computing (`c1_pair_test.py`, `c1_pair_test.json`).
- **The pairs.** 78 pairs of third-order themes are carried by ten or more second-order themes in `assignments_final.jsonl`.
- **The rates.**
  - The corpus arguable rate is 0.613 (4,709 of 7,677 placed lines).
  - Lines placing two themes or more are arguable at 0.961.
  - 76 of the 78 pairs are ten points or more above the corpus rate, and 53 sit at 1.000.
  - Only T3-006 | T3-068 (0.708) and T3-006 | T3-076 (0.647) are not.
- **What the rate measures here.** The confidence value reflects the item's history. Contested items (classes 3 to 5, ruled at B4) are arguable almost throughout. Class 1 and class 2 lines, where the readers agreed, are mostly clear. Most multi-theme lines come from contested items, so a pair's rate records that its items were contested. It does not separate a joint from a lump.
- **Owed.** The comparison stands as declared, so all 76 pairs are owed a joint, lump or unresolved call. How pass 7 reads them was declared before any reading: every item when twelve or fewer carry the pair, else twelve drawn by `random.Random(20261014).sample`.

### J's guard, counted (`out/_analysis/c1_guard_C1a-06.json`)

- This pass made 24 moves; 8 add a theme. 4 add a theme neither reader nor my B1 placed:
  - harrypotter t20, T3-003 on one concept, by a tie at the top;
  - ireland t15, T3-003 on five;
  - smashbros t05, T3-003 on four;
  - warframe t09, T3-017 on three.

### What I doubt (pass 6)

- **The direction of the T3-043 line.** I drew it by the person who speaks. T3-003's four fields already did. Drawing it by time would have moved items the other way. The B4 readers had followed T3-043's sentence where a placement held T3-043.
- **Mixed concepts.** "I am proud that I have placed pixels... Thanks to everyone" counts once. I gave it to the act its label leads with. That choice decided DestinyTheGame t10.
- **Concepts the line counts elsewhere stay there.** In wildhockey t08, "thanking everyone who helped make the final product" sits under T3-009 on the line. By the fields it is a thanks, and with it T3-043 would have kept three concepts.
- **The new T3-050 question names marks only.** T3-086's must_show also takes a quarrel argued in words. falcons t16 kept T3-086 because T3-050's must_show was not met, not because of the question.
- **The pair test's figure.** I kept a comparison that cannot separate pairs, because I declared it before computing. Reading 76 pairs on a sample of twelve each is the cost.

### Slips (pass 6)

- `c1_owed_review.py` printed the item list a second time when it was run again on an existing packet. It wrote nothing.
- I classed sakuragakuin t08 as a move on the line's support alone. On its full concept list it stays. The candidates' full lists were read before any decision was written.

### Next pass

1. The 76 pairs, read as declared and called joint, lump or unresolved, with T3-005 | T3-021 (121), T3-009 | T3-043 (78), the homeland flag, T3-005 | T3-073 and the call cluster among them; any merge or split under rule 10's arithmetic.
2. The empties and the arguables, with saturation by kind.
3. The form pass, the fourth-order themes, `scheme_v2.md`, the handback and the interview.

### validate.py C1 at pass 6's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2101 of 7844 (moved placements 2078)
  empties 167 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback

0 errors (0 distinct shapes), 0 warnings
```

## Pass 7 (C1a-07)

### Opening

- The views after pass 6's close (`c1_views_diff.py`) show 10,577 placements against 13,365 on the settled line, and 194 themes placed.
- After gates 30 to 32, T3-043 has 167 placements and T3-003 has 61.
- T3-140, T3-144 and T3-161 are placed nowhere. Nine rare themes are placed in one room each.

### The pair test, read (section 5)

The reading followed the rule declared at C1a-06. Every item was read when twelve or fewer lines carry the pair. Otherwise twelve items were drawn by `random.Random(20261014).sample` from the sorted items.

- **The test, fixed at pair 1 before any call.**
  - Joint: each theme has concepts of its own kind in the sample. An act doing both may be among them.
  - Lump: no sampled concept is purely one function.
  - Unresolved: pure forms exist on both sides, but a large middle is cut by vocabulary alone.
  - A joint or an unresolved pair is retained. A lump is merged under rule 10.
- **The reading.** 883 item readings over 76 pairs. 26 pairs were read whole and 50 were sampled at twelve.
- **The calls.** They are in `c1_pair_calls-01-08.json` to `c1_pair_calls-61-76.json`, each with its evidence, a contrary reading and an action. `c1_pair_calls_check.py` confirms 76 calls in declared order. Their pairs, item counts and read counts match `c1_pair_test.json`, with 0 problems.
- **The result.** 75 joints, 1 unresolved, 0 lumps.
  - T3-010 | T3-149 is the unresolved pair. Its middle is requests to spare a work or to coexist, and the named-words line cuts that middle by vocabulary.
  - No theme was merged or split. No `tier_history` line, move or snap was owed.
- **The pairs pass 6 named.** T3-005 | T3-021 and T3-009 | T3-043 are joints. The call cluster gave T3-002 | T3-033, T3-002 | T3-038 and T3-033 | T3-038, all joints. No pair holding T3-065 (the homeland flag) is carried by ten lines or more, and neither is T3-005 | T3-073, so the pair test does not reach them.
- **Files.** `c1_pair_pack.py` writes the packets into `c1_pair_packs/`. `c1_theme_fields.py` prints a theme's gate fields from `scheme_v2.jsonl`. Both only read.

**What the reading found.** Every pair has pure concepts on both sides in its sample. The arguable rate could not show this. Reading the items did. The edges between paired themes are of three kinds. The next table lists each kind of edge with an example pair.

| kind of edge | example pair | what sits on the edge |
|---|---|---|
| one act does both functions | T3-006 \| T3-061 | an invasion of a named flag erases the flag and takes its space |
| one exchange is cut in two | T3-010 \| T3-035 | the request for space sits in T3-035, the host's answer in T3-010 |
| the placements follow the label's words, while the written line names a fact | T3-002 \| T3-005; T3-033 \| T3-041 | calls to defend placed by whether they name the attack; further marks placed by whether the label says "next" or "another" |

- **T3-041 | T3-113 is a different case.** T3-113 is cut by what is drawn. T3-041 is cut by the act of adding. So every national emblem added beside a flag is also an extension. I kept the pair because J named national content as study material for B1, not because the act differs.
- **Carried.** 20 placements stand against a written field (`c1_pair_carried.json`). None was moved: no gate was amended, so no recheck was owed. The arguables pass reads each one.

### The stopping criterion at pass 7

Every source line has had a decision since pass 5. Pass 7 amended no gate, so the second clause holds. It holds trivially, because pass 7 tested no gate. Recutting stops here. If the empties and arguables pass needs a gate amended, that gate owes its rechecks and the criterion is read again.

### J's guard, counted (`out/_analysis/c1_guard_C1a-07.json`)

- 0 moves. None adds a theme.

### What I doubt (pass 7)

- **This test rarely finds a lump.** One pure concept on each side of a sample makes a joint. A lump needs no pure concept at all. So "0 lumps" says each theme has pure forms. It does not say the cuts are where another reader would draw them.
- **I alone called all 76 pairs.** The test was fixed at pair 1, but no one checked the calls.
- **The calls rest on concept labels.** A label is the coder's paraphrase, not a quote. I grounded no call through `cite.py`.
- **Two joints could be read as unresolved.** In T3-002 | T3-005 and T3-033 | T3-041 the written line names a fact: an attack under way, or the room's first mark. The placements follow the words. I called both joints because the fact is in the material. Read from the placements alone, both pairs are unresolved.
- **The samples are uneven.** A pair carried by ten lines was read whole. T3-005 | T3-021, carried by 121, was read on twelve.

### Slips (pass 7)

- The permission check refused `cut -c` after `mem.py diary`. I used `--width` instead. Nothing was written.

### Next pass

1. The empties and the arguables (section 6), with saturation by kind. These carry over:
   - T3-052's four unresolved items;
   - the unresolved single failures of B4's packet 7;
   - harrypotter t11 and tampabaylightning t08;
   - the 20 placements in `c1_pair_carried.json`.
2. The form pass, the fourth-order themes, `scheme_v2.md`, the handback and the interview.

### validate.py C1 at pass 7's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2101 of 7844 (moved placements 2078)
  empties 167 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback

0 errors (0 distinct shapes), 0 warnings
```

## Pass 8 (C1a-08)

### Opening

- The views after pass 7's close are unchanged since pass 6, because pass 7 moved nothing: 10,577 placements against 13,365 on the settled line, and 194 themes placed.
- T3-140, T3-144 and T3-161 are placed nowhere. Nine themes are placed in one room each.
- All twelve themes in one room or none are in the rare tier, so no main theme fell below B1's floor of two rooms unlike each other.

### The empties (section 6)

The reading rule was declared in the diary before any decision. Every empty line was read whole, in B1's reading order, as a re-read of its B4 ruling under `scheme_v2`'s gates and reading rules. J's rulings of 13 October bound the re-read: a placement chooses among the readers' themes and my B1's. The lone-B1 floor applies only where the readers' theme takes concepts (pass 4).

- **Count.** 167 lines were empty before the pass, 2.1% of 7,844. That is below one in five, so no finding goes to the top of these notes. All 167 were B4 rulings carried unresolved, in classes 3 to 5, and both B3 readers had placed a theme in every one.
- **Placed: 16.** All are class 4. In each, the agreeing readers' theme takes no concept and my B1 theme's `must_show` takes the concepts. The floor alone had kept them out. Six also rest on an amended gate: gate:1 (canucks t25), gate:28 (four side-talk items) and gate:29 (twentyonepilots t07).
- **Empty now: 151 of 7,844 (1.9%).**
- **Files.** `c1_empties.py` writes the packets into `c1_empties_packs/`. The decisions are in `c1_empties_decisions.json`, checked by `c1_empties_kinds.py` (167 decisions, 0 problems; summary in `c1_empties_kinds.json`). The placements went through `c1_empties_moves.json` and `c1_reassign_list.py`, dry run first.

The next table lists the 18 kinds of empty material. For each kind it gives the items, the rooms, the items placed this pass, the first position in B1's reading order, and whether the scheme is too narrow or the material too varied.

| kind | what it is | items | rooms | placed | first in B1 order | verdict |
|---|---|---|---|---|---|---|
| K01 | a bare trace: only a title, link, test line or the event's name survives | 37 | 34 | 0 | 20 | material too thin; the bare-mention rule gives it its outcome |
| K02 | a short reply whose object is lost | 17 | 16 | 0 | 77 | material too thin |
| K03 | a picture remarked on, its owner or place unsaid | 17 | 17 | 0 | 8 | mostly a fact the words omit; too narrow where the picture is another room's away from the mark |
| K04 | an April Fools joke whose maker is unsaid | 8 | 8 | 0 | 44 | a fact the words omit |
| K05 | another sub's April Fools change seen from this room | 8 | 8 | 0 | 178 | scheme too narrow |
| K06 | April Fools play or talk that stages no fake | 17 | 15 | 0 | 147 | scheme too narrow |
| K07 | the day marked or awaited, with no joke | 4 | 4 | 0 | 37 | scheme too narrow, and thin |
| K08 | a dispute over the room's own jokes | 4 | 4 | 2 | 318 | scheme too narrow |
| K09 | side talk and jokes with no canvas | 9 | 9 | 4 | 27 | not the scheme since gate:28; empty only where no placement held T3-017 |
| K10 | the sub's own moderation outside the canvas | 8 | 7 | 0 | 166 | scheme too narrow by design (T3-063 takes canvas posts only) |
| K11 | talk about the canvas as a whole | 3 | 3 | 0 | 227 | scheme too narrow at the edge |
| K12 | meaning or attachment given to the room's own mark | 2 | 2 | 0 | 494 | material too varied |
| K13 | the room's work shown in other subs, with no joke and no call | 2 | 2 | 0 | 239 | scheme too narrow at the edge |
| K14 | two tests met, and no field decides | 4 | 4 | 0 | 131 | bundled material; no tiebreak sentence |
| K15 | another deciding fact absent | 6 | 5 | 0 | 292 | a fact the words omit |
| K16 | a singular act no theme names | 8 | 6 | 0 | 196 | material too varied: each below B1's floor |
| K17 | material a theme fits, kept out by the lone-B1 floor alone | 10 | 10 | 10 | 37 | neither; placed under pass 4's revision |
| K18 | lateness: arriving after the work, or told it is done | 3 | 3 | 0 | 125 | scheme too narrow at the edge |

- **Saturation by kind.** 17 of the 18 kinds appear by room 352 of 705 in B1's reading order. After room 318 only one new kind appears: K12, two items, first at room 494. 89 of the 167 empties come after room 352. New kinds stopped appearing in the second half of the order. One limit: I drew the kinds after reading all the items, so first appearance is read back from the order, not watched as items arrived.
- **What the scheme lacks.** Four kinds that the corpus carries in rooms unlike each other have no theme:
  - April Fools play or talk that stages no fake (K06, 17 items in 15 rooms);
  - another sub's April Fools change seen from this room (K05, 8 in 8);
  - the sub's own moderation outside the canvas (K10, 8 in 7);
  - disputes over the room's own jokes (K08, 4 in 4).

  None is added in this pass. A new theme would change the instrument after the readers ran, and J's re-read rule would still leave these items empty, since no reader and not my B1 placed it. They go to the handback.

### The arguables (section 6)

- **Count.** 4,876 lines are arguable: 4,725 placed and 151 empty. The arguable rate among placed lines is 0.614. By class: 895, 864, 2,363, 696 and 58.
- **Reading.** Every arguable line was read at the level of its label, its placements, the two B3 readers and my B1 (`c1_arguables_list.md`, grouped by the readers' split pair, then by first theme). Their concepts were not opened.
- **The measure** (`c1_arguables.py`). The readers' confusion takes two forms. In a crossing, each reader placed a theme the other did not; this happens in 1,002 lines. In an added theme, both readers placed one theme and one of them added another.

The next table lists B1's 19 predicted pairs, with their crossing lines, their added-theme lines, and their rank among 922 confused pairs with both forms counted.

| # | predicted pair | crossings | added theme | rank, both forms |
|---|---|---|---|---|
| 1 | T3-005 / T3-021 | 18 | 98 | 1 |
| 2 | T3-010 / T3-149 | 19 | 32 | 3 |
| 3 | T3-001 / T3-023 | 18 | 9 | 9 |
| 4 | T3-028 / T3-070 | 0 | 9 | 65 |
| 5 | T3-004 / T3-020 | 2 | 16 | 23 |
| 6 | T3-002 / T3-033 | 12 | 26 | 4 |
| 7 | T3-015 / T3-075 | 2 | 10 | 45 |
| 8 | T3-004 / T3-070 | 12 | 13 | 13 |
| 9 | T3-009 / T3-073 | 19 | 18 | 5 |
| 10 | T3-004 / T3-038 | 7 | 15 | 14 |
| 11 | T3-010 / T3-151 | 10 | 26 | 6 |
| 12 | T3-010 / T3-150 | 4 | 16 | 19 |
| 13 | T3-010 / T3-024 | 12 | 15 | 10 |
| 14 | T3-009 / T3-043 | 5 | 54 | 2 |
| 15 | T3-001 / T3-095 | 10 | 11 | 16 |
| 16 | T3-087 / T3-188 | 1 | 3 | 158 |
| 17 | T3-044 / T3-082 | 0 | 0 | none |
| 18 | T3-014 / T3-152 | 0 | 25 | 12 |
| 19 | T3-015 / T3-063 | 5 | 6 | 49 |

- **The prediction held at the top.** The pair B1 named hardest, T3-005 / T3-021, is the most confused. 8 of the 19 predicted pairs are in the top 10, 13 in the top 20 and 14 in the top 30. B1 predicted #14 and #18 as a disagreement over the added theme, and that is the form they took.
- **Five predictions missed:** #4, #7, #16, #17 and #19.
- **Confused, not predicted.** T3-002 / T3-038 (33 lines, the call and build cluster); T3-017 / T3-031 (29 crossings, the most of any pair; gate:28 amended its sentence at pass 6); T3-023 / T3-095 (25; gates 1 to 4 at pass 2); T3-004 / T3-041 (21); T3-001 / T3-048 (20). T3-033 / T3-041 has 12 crossings and is the top pair where the two readers agree against my B1, at 16 lines.
- **Rule 0 departures** (`c1_line_order_check.py`). Of 2,179 multi-theme lines, 104 put a theme with fewer concepts first, 82 of them B4 rulings. Most follow a `decide_when_both` that names the primary, such as staging over objecting or the takeover over its styling. 1,069 lines hold a later theme below three concepts: J's lean, measured at pass 5 and not swept. Neither is corrected.

### The placements the pair test carried

The 20 placements of `c1_pair_carried.json` were each read whole (`c1_carried_pack.md`). None was moved (`c1_pair_carried_decisions.json`). Correcting only the lines the pair samples happened to find would treat them unlike the unsampled lines the same reading covers.
- 12 sit on boundaries already read and barred from a third sentence. In 7 rooms, T3-002 / T3-005 calls to defend are counted toward T3-002; B4 read this boundary in packets 2 and 4. In 5 rooms, T3-033 / T3-041 further marks are counted toward T3-033; pass 5 barred a third sentence here, because the call, offer and build cluster moved at B2 and split the readers again. Both themes are placed in every one of the 12, so only order and counts differ.
- 2 are items of gate:27 outside its recheck sample: indonesia t11 and rit t09.
- 5 are defensible readings of unamended fields, or a class 1 line all three readings share. osugame t04 shows a wording overlap for `scheme_v2.md`'s watch list. Its removals that point to r/osuplace meet both T3-063's `decide_when_both` (gate:23, "removing under any other rule") and T3-090's `must_show` ("canvas posts redirected to it").
- 1 (de t08) is a reading error that leaves the line's themes and order unchanged.

### The stopping criterion at pass 8

Pass 8 amended no gate, so the criterion holds, as at pass 7. The 16 placements applied amended gates and pass 4's floor revision. They changed no sentence.

### J's guard, counted (`out/_analysis/c1_guard_C1a-08.json`)

- 16 moves, each to my B1's theme in a class 4 empty line. None goes to a theme neither reader nor my B1 placed.

### What I doubt (pass 8)

- **Thin placements.** I placed 16 lines on one or two concepts each. Pass 4's floor revision allows it, but a thin placement can misstate an item's practice. denverbroncos t02 is mostly a dispute over /s, and T3-095 holds one of its five concepts.
- **The empties' kinds are mine.** I drew them after reading 167 items, with no second reader. K02 and K15 border on each other: a short reply whose object is lost is also a deciding fact absent.
- **The arguables were read at the label level.** The prediction check rests on placements, not on the words.
- **I kept 20 known slips.** The reason is consistency with the unsampled lines. The cost is 20 lines I know to be off, 12 of them on two boundaries.
- **T3-052's reach.** I required the picture to sit beside the room's mark, as T3-052's `must_show` says and as B4a-07 read it. B4a-06 had read T3-052 more widely. Under the wider reading, germany t19 and futurama t15 would be placed.
- **Two empties stay empty against B4's earlier reasoning.** In samuraijack t14, "Fuck Tammy" is another fandom's meme, not the room's humour. In anarcho_capitalism t17, a bare link shows no act.

### Slips (pass 8)

- The permission check refused `cut -c` after a grep. I reran the search without it.
- `c1_empties_kinds.py` first failed on a sort of dictionaries. I fixed it before any output was used.

### Next pass

1. The form pass (section 7): three sweeps, written to `form_pass-C1.md`.
2. The fourth-order themes (section 8).
3. `scheme_v2.md` with the gate block, the reading rules and the watch items (osugame t04's overlap among them). Then `handback-C1.md`, listing `c1_unapplied.jsonl`, `c1_pair_carried_decisions.json` and the four kinds the scheme lacks. Then the interview.

### validate.py C1 at pass 8's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2117 of 7844 (moved placements 2094)
  empties 151 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback

0 errors (0 distinct shapes), 0 warnings
```

## Pass 9 (C1a-09)

### Opening

- The views after pass 8's close (`c1_views_diff.py`) show 10,593 placements against 13,365 on the settled line. That is 16 more than after pass 7: the 16 empty lines placed at pass 8, one theme each. 194 themes are placed.
- T3-140, T3-144 and T3-161 are placed nowhere. Nine themes are placed in one room each, all rare.

### The form pass (section 7)

The pass is written in `form_pass-C1.md`, with its searches, limits, pattern tables and findings. The helper is `out/_analysis/c1_form_pass.py`, and the patterns are in `out/_analysis/c1_form_patterns.json`. Every count went through `mem.py codes --grep`, one logged read per pattern, and was then kept to the participants' quoted words. Quotes were grounded with `cite.py --grep`.

- **Sweep 1, form.** 9.7% of the 115,388 concepts are three words or fewer, in 659 rooms. The cheapest act is the one-line reply that joins, assents, reports a part done or thanks: 590 concepts in 337 rooms, median two words. 90.3% sit under a coded parent item, against 73.7% of all comments. Concepts that short draw a coded reply in 20.9% of cases, against 35.0% for concepts of 11 words or more. Two turn forms that no theme owns: the edited post and the talk of sleep and time zones.
- **Sweep 2, register.** The vocabulary of state and war covers 4,759 concepts in 571 rooms under 145 line themes; no theme holds more than 14.9%. "We" leads "I" in submissions, and "I" leads in replies. Diplomacy, pride and trade are owned by themes. The craft words, profanity and internet slang are wide, but they are the medium's words or the site's.
- **Sweep 3, what is not said.** The canvas-wide collectives are named in 453 rooms; 128 concepts put the void in a question, and none asks what it is. A question posted as a submission draws a coded reply in 37.7% of cases. "Who is in charge" is asked in 14 rooms.

The next table lists the eight form-pass findings by id, with the communities and lines each covers. `form_pass-C1.md` holds the statement and exemplars of each.

| id | finding | communities | lines |
|---|---|---|---|
| FP-01 | the one-line reply is the cheapest act | 337 | 590 |
| FP-02 | the edited post carries a running record | 418 | 1,124 |
| FP-03 | rooms time the work by who is awake | 219 | 362 |
| FP-04 | the vocabulary of state and war is the common speech of canvas work | 571 | 4,759 |
| FP-05 | the post speaks as "we", the reply as "I" | 694 and 684 | 33,472 and 30,890 |
| FP-06 | the canvas's large collectives are named as known actors | 453 | 3,605 |
| FP-07 | a room's question to itself, posted as a submission, is answered least | 559 (submission questions) | 5,072 |
| FP-08 | who leads is neither asked nor named | 14 asked, 61 named | 15 asked, 86 named |

These findings were never counted and never clustered. None has a line in `assignments_final.jsonl` or a share in any later arithmetic, and no gate was written for them. Stage C2 takes them from `form_pass-C1.md`, the only place they exist.

### What the form pass could not reach

This list is the same as in `form_pass-C1.md`, kept here for stage E1 and the write-up's account of what the study cannot say.

1. **Stance.** A register or a stance is a property of a whole utterance. String matching finds the words, and it cannot tell play from earnest. "Canadian reinforcements, reporting in sir!" [ripcity/c0192] may be a joke or a pledge. FP-04 counts the vocabulary of war, not the stance of war.
2. **Acts named by topic.** No route through second-order themes reaches an act whose themes name what it was about rather than what it was. The one-line reply sits on the theme of the call it answers. FP-01's 88 line themes are topics, not the act of joining. The same holds for the edited post and the talk of sleep.
3. **Dropped items.** The coders dropped items with no code and no coded descendant. Short replies and many answers are among them. FP-01 is a floor, and FP-07's unanswered share is an upper bound.
4. **Timing.** The hour is the item's posting time, in hours since the canvas opened. The pass did not measure reply latency, the time of an edit, or each room's local time.
5. **Case.** `mem.py`'s grep ignores case, so shouting in capitals, itself a register, was not counted.
6. **Language.** The patterns are English. Rooms that wrote in Portuguese, German, French, Czech and other languages are undercounted in every sweep.
7. **Links and images.** A turn that is a template link or a screenshot has a URL for its words, and its register is invisible.
8. **Who answers whom.** The pass read the line theme of a coded parent item. It did not follow authors across turns, so it cannot say whether the caller answers the joiner.
9. **The week before.** The pass did not compare any register with the rooms' pre-event week, so it cannot say whether the event changed the register.

### The stopping criterion at pass 9

Pass 9 amended no gate and moved no placement. The criterion holds, as at passes 7 and 8.

### J's guard, counted (`out/_analysis/c1_guard_C1a-09.json`)

- 0 moves in this leg.

### What I doubt (pass 9)

- **The patterns are mine.** I chose every word list. Two first counts were polluted and recounted: "gg" matched discord.gg links, and "ranks" and "squads" are game words. Other lists may hold pollution I did not see. The faith row holds exclamations such as "holy shit", and I did not recount it.
- **"Answered" rests on the coded record.** An answer the coders dropped is not seen.
- **FP-05 has a length confound.** Submissions are shorter, which lowers any pronoun's share. Length does not explain why the "we" share stays flat.
- **FP-08's reading is mine.** The count shows only that the question is absent. That the rooms take for granted that whoever posts may call is my reading.
- **FP-04 and the named words.** The named words of T3-010 | T3-149 read war words as naming an attack. FP-04 finds those words used across the corpus, even for builders. I did not amend the gate. The doubt goes to `scheme_v2.md`'s watch items and to the handback.

### Slips (pass 9)

- After the compaction, the guard refused the first "compacted; head reconciled" line. It wanted the head and the stage file read after the compaction notice. I read both again and logged the line in a call of its own.
- One first pattern for a gloss on the void matched statements such as "The void is approaching". The leaders pattern held game titles ("Chief" in halo, "cmdr"). Both were recounted before any figure was used.

### Next pass

1. The fourth-order themes (section 8). Each cut is a `tier_history` line, a move line in the diary and a snap.
2. `scheme_v2.md`, with the gate block, the reading rules and the watch items: osugame t04's overlap, and FP-04's caution on the named words.
3. `handback-C1.md`, listing `c1_unapplied.jsonl`, `c1_pair_carried_decisions.json`, the four kinds the scheme lacks and FP-04's caution. Then the interview.

### validate.py C1 at pass 9's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2117 of 7844 (moved placements 2094)
  empties 151 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback


0 errors (0 distinct shapes), 0 warnings
```

## Pass 10 (C1a-10)

### Opening

- The views after pass 9's close are unchanged, because pass 9 moved nothing: 10,593 placements against 13,365 on the settled line, and 194 themes placed. `out/fourth/` was empty.

### The fourth-order themes (section 8)

I read the third-order tier whole, by family, with each theme's placements, rooms and the themes most often placed beside it (`c1_t4_table.py`, written to `out/_analysis/c1_t4_table-C1a-10.txt`). I then wrote a story for each bundle before cutting it. The specs are in `out/_analysis/c1_t4_specs.json`. `c1_t4_cut.py` cut each one in turn. It appended the line to `fourth/fourth.jsonl` and the event to `tier_history.jsonl`, logged the move through `mem.py log --kind move`, and took the snap: C1-move-relating-2 to C1-move-merging-29. `fourth/fourth.md` was written from the ledger by `c1_fourth_md.py`.

- **Count.** 28 fourth-order themes over 195 of the 197 third-order themes. No number was set. The material carries that many mechanisms, and the diary entry before the first cut names them.
- **Declared.** 13 borrowed, 14 adapted, 1 coined. Every borrowed or adapted source is recalled, since only the method shelf is held at C1. Stage C3 verifies or withdraws each.
- **Moves.** 22 merging (the members are kinds of one practice) and 6 relating (the members are held together by a relationship among them, such as a cycle of restraint and defection).
- **Glosses.** Each gloss is a participant's phrase found again with `cite.py --grep`, with its concept.
- **Check.** `c1_check_fourth_now.py` runs the close-check's last-pass functions on the fourth-order themes and the form pass now: 0 errors, 0 warnings.

The next table lists the fourth-order themes with their declaration and the number of third-order themes each holds. `fourth/fourth.md` holds the prose, the sources and the members.

| id | name | declared | third-order themes |
|---|---|---|---|
| T4-001 | Keying | adapted | 10 |
| T4-002 | Boundary work | adapted | 8 |
| T4-003 | Sensemaking | borrowed | 3 |
| T4-004 | Frame bridging | adapted | 4 |
| T4-005 | Mobilization | adapted | 5 |
| T4-006 | Collective representation | adapted | 10 |
| T4-007 | Stigmergy | borrowed | 3 |
| T4-008 | Standardization of output | borrowed | 5 |
| T4-009 | Workarounds | adapted | 8 |
| T4-010 | Backstage decision-making | adapted | 7 |
| T4-011 | Decided order | borrowed | 8 |
| T4-012 | Collective efficacy | borrowed | 5 |
| T4-013 | Repair work | adapted | 6 |
| T4-014 | Territoriality | borrowed | 7 |
| T4-015 | Live and let live | borrowed | 11 |
| T4-016 | Negotiated order | borrowed | 11 |
| T4-017 | Reciprocity | borrowed | 7 |
| T4-018 | Meta-organization | borrowed | 9 |
| T4-019 | Attribution | adapted | 4 |
| T4-020 | Repertoire of contention | adapted | 7 |
| T4-021 | Rivalry | borrowed | 5 |
| T4-022 | Flagging the nation | adapted | 12 |
| T4-023 | Neo-tribes | borrowed | 6 |
| T4-024 | Symbolic boundaries | adapted | 5 |
| T4-025 | Visibility returns | coined | 9 |
| T4-026 | Completion ritual | adapted | 8 |
| T4-027 | Collective memory | borrowed | 6 |
| T4-028 | Transition | adapted | 6 |

**Partitions tried and set aside.**
1. The 21 families as fourth-order themes. They are topic headings in the material's words, and several hold distinct mechanisms: G14 mixes territorial claims, help and host relations; G21 mixes ritual, memory and transition.
2. Puranam, Alexy and Reitzig's four universal problems as the cut. About 40 themes speak to them. Inter-room order, identity and play would be left unpicked.
3. One construct for all order between rooms. Tacit restraint, explicit agreement and the exchange of help are different mechanisms, and the pair test called T3-010's pairs with T3-149 and T3-151 joints.
4. Stigmergy absorbing the emblem themes. Choosing what a mark says is a decision about meaning; stigmergy is coordination through the trace.

**Third-order themes no fourth-order theme picks up.** They are listed, not gathered.
- T3-017 carrying on ordinary sub talk: the sub's ordinary business during the canvas week. It is the ground that boundary work protects, not an act of organizing the work.
- T3-133 recovering a hacked sub (rare): one room, one event, unrelated to the canvas work.

### Placements the partition forced

A partition puts each third-order theme in one fourth-order theme. These themes could sit in two, and the next list says where each went. They are stage C2's first candidates for recutting.
- T3-076 reining in the room's attackers: Live and let live, not Negotiated order or Decided order.
- T3-061 pushing into a neighbour's space: Repertoire of contention, not Territoriality.
- T3-169 signing the sub's name: Collective representation, not Territoriality, where Brown, Lawrence and Robinson would call it identity marking.
- T3-188 disowning placers outside the plan: Attribution, not Negotiated order.
- T3-058 blaming attackers after the close: Rivalry, not Attribution.
- T3-159 rewarding helpers with prizes: Completion ritual, not Mobilization.
- T3-090 opening a canvas sub: Boundary work, not Backstage decision-making.
- T3-153 meeting other rooms in chat: Meta-organization, not Backstage decision-making.
- T3-172 and T3-173, oaths and elections in canvas-born factions: Decided order, not Neo-tribes.
- T3-081 casting fights as national history and T3-130 reading national politics in pixels: Flagging the nation, not Frame bridging.
- T3-141 covering the night shift: Repair work. FP-03 finds the same talk of sleep and time zones under 64 themes.

### The stopping criterion at pass 10

Pass 10 amended no gate and moved no placement. The criterion holds, as at passes 7 to 9.

### J's guard, counted (`out/_analysis/c1_guard_C1a-10.json`)

- 0 moves in this leg.

### What I doubt (pass 10)

- **Recalled sources.** I gave authors, years and titles from memory. Some details may be wrong, and stage C3 verifies or withdraws each.
- **Thin constructs.** Decided order reaches 48 lines in 46 rooms, Neo-tribes 56 in 35, and Symbolic boundaries 54 in 49. A construct is a kind, not a share, but stage C2 should test whether each holds or merges.
- **Stigmergy rests on two large themes.** Building and extending could be read as plain production. The construct claims coordination through the trace, and its disconfirmer says how that could fail.
- **The forced placements above.** Each was a judgment between two defensible homes.
- **Prose that runs through the acts.** The stage asks for what holds the members together without listing them. Each prose names the binding first, but some still run through the acts after it.
- **No second reader.** The bundles are mine alone.

### Slips (pass 10)

- `c1_t4_table.py` first read `families.jsonl` by a key the file does not have, so the family names came out blank. I fixed it before use.
- A table written to the system's temporary folder could not be read from outside the run folder. I wrote it into `out/_analysis/` instead.
- `c1_t4_cut.py` printed both long JSON lines on the first cut. I made it print them on dry runs only.

### Next pass

1. `scheme_v2.md`: the whole scheme with every field, the gate block with the reading rules, every change declared with what changed, why and which placements it moved, and the watch items (osugame t04; FP-04's caution on the named words).
2. `handback-C1.md`: `c1_unapplied.jsonl`, `c1_pair_carried_decisions.json`, the four kinds the scheme lacks, FP-04's caution, the recalled sources for stage C3 and the forced placements above.
3. The interview brief, and `done.sh C1 --cut interview`.

### validate.py C1 at pass 10's close (before `done.sh`)

```
stage C1:
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2117 of 7844 (moved placements 2094)
  empties 151 of 7844
  a pass closed; the full set (scheme v2, assignments, the fourth-order themes, the form pass) is owed at the last pass, with the handback


0 errors (0 distinct shapes), 0 warnings
```

The last-pass checks on the fourth-order themes and the form pass, run now with `c1_check_fourth_now.py`:

```
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  fourth-order themes 28 over 195 third-order themes, 2 unpicked
  form pass: 8 FP ids
errors 0
warnings 0
```

## Pass 11 (C1a-11), the last pass

### Opening

- The views after pass 10's close show the placements unchanged, as pass 10 moved none: 10,593 against 13,365 on the settled line, and 194 themes placed. The data-structure view now carries each concept's fourth-order theme.

### `scheme_v2.md` (section 9)

`out/_analysis/c1_scheme_v2_md.py` wrote it from `scheme_v2.jsonl` and the C1 ledgers. It is the whole scheme, not a diff.
- **Contents.** How to read a theme; the reading rules; the gate block, with all 35 amendments in a table and each with its old and new sentence (for discriminators, only the questions that changed), its reason, the placements it could move, the rechecks done and changed, and the moves that name it; the tier change; the placements moved by cause; the watch items; the index; and every theme with every field, its placements at C1's close, its fourth-order theme and its C1 note.
- **The theme notes.** 178 themes unchanged, 18 amended by a gate, 1 moved to rare.
- **The moves by cause.** 2,175 move entries on 2,117 lines: the class 2 ruling 1,990; rechecks after an amended gate 92; the revision rate's errors 29; J's floor 25; the empties pass 16; pass 1 re-reads 10; review of listed lines 6; the lone-B1 floor 4; a pass 1 doubt 2; a flagged record promoted 1.

### The recurring pairs (section 1), and the modifier candidates

`c1_recurring_pairs.py` (output in `out/_analysis/c1_recurring_pairs-C1a-11.txt`) gives what each row of stage B3's pair table became. The table has 20 rows and 19 distinct pairs, since T3-005 | T3-021 appears both ways.
- **Joints.** 17 pairs were called joints at pass 7 and retained.
- **Unresolved.** T3-010 | T3-149 is the one unresolved pair. Gates 15, 16, 18 to 21 and 33 rewrote its sentences.
- **No call owed.** T3-006 | T3-068 has an arguable rate of 0.708, under the 0.713 bar.
- **The modifier candidates are left, not folded.** T3-089 was first on 3 lines and later on 29 on the settled line; now 3 and 21. T3-152 was 6 and 50; now 6 and 27. The pair test called T3-028 | T3-089 and T3-014 | T3-152 joints, each theme having pure concepts of its own. Each is a second act that travels with its partner, not a qualifier of it, and J's floor already took off its later placements under three concepts.

### Stage B4's figure, and which figure the write-up should use (section 2)

Stage B4 measured transmission after revision. Fresh readers held only the frozen scheme, and each reading was scored by its mean Jaccard against the settled set, over readings with a resolved settled line, in two arms never pooled. Arm 1 (DeepSeek) scored 0.657 on the uniform stratum and 0.544 on the adjudicated one; arm 2 (OpenAI) scored 0.622 and 0.554. Each figure bounds whether the written instrument decides, not whether it is right, and none is reliability.

The revision changed the scheme and the line enough that this figure no longer describes them. It was measured with `scheme_final.jsonl` against `assign_final.jsonl`. C1 amended 35 sentences in 18 themes, which no blind reader has seen, and replaced the line in 2,117 of 7,844 lines. 1,990 of those came by the class 2 ruling, which removed the B1 themes that stage B4 found depressing the uniform figure.

**The write-up should report stage B4's figure as the transmission of the frozen scheme against stage B's line, measured at stage B4, and should say that scheme v2 and `assignments_final.jsonl` have no transmission figure until fresh readers test the revised scheme, which J ruled for after C1.** I did not recompute stage B4's figure against the new line. The revision rate is my agreement with the line, not transmission.

### `handback-C1.md`

It holds:
- the claim, with naruto t04 and greenlattice t03 and the condition between them;
- the counts, with where each is recorded;
- the recurring pairs;
- stage B4's figure as above;
- the form pass and the fourth-order themes;
- what stage C2 and later inherit: the 13 forced placements, the thin constructs, the 27 recalled sources for stage C3, the watch items, the five unapplied errors, the 20 kept placements, the four kinds the scheme lacks, the rule 0 departures, and B1's open items;
- the licences exercised.

### J's guard, over the whole stage

The guard (`c1_guard_moves.py`) counts each pass's moves to a theme neither reader nor my B1 placed. The next table gives the moves and that count by pass.

| pass | moves | adding a theme | to a theme neither reader nor my B1 placed |
|---|---|---|---|
| 1 | 2,000 | 10 | 0 |
| 2 | 38 | 35 | 33 |
| 3 | 32 | 16 | 11 |
| 4 | 34 | 17 | 8 |
| 5 | 31 | 16 | 6 |
| 6 | 24 | 8 | 4 |
| 7 | 0 | 0 | 0 |
| 8 | 16 | 16 | 0 |
| 9 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 |
| 11 | 0 | 0 | 0 |

The 62 such moves came from rechecks under amended gates, which QC1-001 places over the whole scheme. At pass 2, 32 of the 33 went onto T3-084. Under gate:6 and the visitor rule, another room's request for help arriving in this room's threads is a request, not this room's help, and no reader had placed T3-084 there. Pass 2's listing is in `out/_analysis/c1_guard_C1a-02-listing.txt`.

### The stopping criterion at pass 11

Pass 11 amended no gate and moved no placement. The criterion holds, as at passes 7 to 10. Recutting stopped at pass 6.

### What I doubt (pass 11)

- **The claim's condition rests on two rooms.** I did not count how many lines are bags whose `also_present` holds more of the room's concepts than the placed theme.
- **The cause table is my classification of free-text reasons.** A move whose reason names both a gate and J's floor is counted under the gate.
- **The handback's guard line was wrong in my first draft.** It said 0 at every pass. A head written from memory would have carried the error.

### Slips (pass 11)

- **The first cause table in `scheme_v2.md`.** It tested J's floor before the gate. I fixed the script and corrected the table in place from its `--causes` output.
- **"1 moves".** It read "1 moves name this gate" where one move named a gate. I fixed the file and the script.
- **The handback's guard line.** I first wrote 0 at every pass, and then that pass 2's moves went onto T3-011. The guard listing shows T3-084. I corrected both before the close.
- **A refused command.** It used `cut -c` beside a helper. I read the file with line ranges instead.

### validate.py C1 at the last pass (the full set, with the handback; before `done.sh C1 --cut interview`)

```
stage C1:
  scheme_v2: 197 themes (15 rare), frozen 197, retired 0, new 0
  assignments_final 7844 lines = assignment_items_expected
  revised lines 2117 of 7844 (moved placements 2094)
  empties 151 of 7844
  fourth-order themes 28 over 195 third-order themes, 2 unpicked
  form pass: 8 FP ids


0 errors (0 distinct shapes), 0 warnings
```

J's guard at pass 11 (`out/_analysis/c1_guard_C1a-11.json`): 0 moves.
