# The handling (stage E2)

Written at E2a, 28 October 2026. This file audits what I was told during the run, by whom, and what it did to the work. It does not audit what I did; that was `experience-E1.md`. Three parties spoke to me: the principal investigator (J, in interviews and in rulings), the handler (the harness's messages, the answers to my questions, the pauses), and the instrument's author (the contract, the standing instructions, the stage files, the tools, and the design note).

**Sources and how they are cited.**
- `handling/design-note.md` (v38, dated 2026-09-22, with J's decisions of 24 September) and `handling/proposal.md`, read whole, cited by line.
- The nine interviews in `handling/interviews/`. `out/_analysis/e2_interviews.py` prints each one's dialogue from the turn that opens "This is an interview" (`out/_analysis/e2_interviews.txt`). A turn is cited as *leg, turn n*, numbered from the transcript's first dialogue turn.
- `handling/harness-log/`: the handover events (cited by time), the pause files, and the 314 first messages. `out/_analysis/e2_first_messages.py` lists what each first message added to the standard text: 56 messages carry an addition, and 258 carry none.
- The answer files in `out/_answers/`, the contract, the stage files, the tools and the checks (by line), the handbacks, and the diary (by stage, leg and time).

**What I could not read.** `CONTROL/` is read-denied, so the handler's messages sent during a leg (the pauses, the E1d message) are known only from my own record of them. The interview transcripts hold J's opening questions and my answers; any talk outside them is not on file. The design note predates the run's tooling (v38 against v43) and numbers the stages 01 to 18 where the run names them A1 to E2. So I read it as the design's intent, not as the run's specification. A point I could not cite is marked as such.

## 1. Where what I was told was inconsistent

**1.1 Where the P05 bound was to be written: J's plan, the contract and the D4 check.**
- *J* (D3.D3c, turn 41, question 1): the bound "stands for D3, since the bound is printed wherever the claim is, but D4 should write it into P05 and carry it through the next re-check."
- *The contract* (rule 11, `CONTRACT-aggregator.md` lines 372 to 376): after C5 "a recut is an amendment made at D3, with affected original leads rechecking the resulting version before stage D4 cuts".
- *The D4 check* (`tools/checks/stage_D4.py` line 218): `vlib.model_moved(outdir, "D3", "D4")` with no allowance, so any edit to the model at D4 fails D4's close.
- *J's ruling of the same day* (13:39 Berlin, the head): "no further re-check, no labelers and no readers for the rest of the run".
- *What I did.* I named the conflict in the interview (D3.D3c, turn 43): "D4 can carry the branch, but it cannot rewrite P05". At D4 I then made the amendment and A11's withdrawal (moves 198 and 199, history lines 173 to 180). J reverted both under QD4-001, and they stand as held proposals (move 203).
- *What it cost.* Three moves and ten lines of history (lines 173 to 182). The frozen model is now reported in every file with two proposals stated beside it. And the model keeps two statements the evidence had already questioned: P05's clause, which fails in nine rooms, and A11, which "cannot fail as it stands" (D3.D3c, turn 43, question 2). This cost the most of anything in the handling, because it reached the model's content and not only the work.

**1.2 The return specification and the packet's last line: the design note, the stage file and the tool.**
- *The design note* (lines 250 to 254): "One return specification per stage, `RETURN-NN.md`, frozen with the stage file. The packet builder emits it verbatim", and a packet ends "with an end-of-packet marker and one line telling the reader to confirm it reached the marker".
- *Stage E1* (line 175, with the outputs at line 25): the analyst writes `RETURN-E1.md` at the build leg.
- *The packet tool* (`tools/packets.py` line 64): every packet ends by asking for "the end marker the return specification names".
- *What I did.* I followed the stage file. I wrote `RETURN-E1.md` at E1c without reading the tool's trailer, and named no marker.
- *What it cost.* All 30 readers ended with a marker of their own, and the dispatch judged 0 returns valid and 30 rooms exhausted (`_fleet_raw/E1/DONE`; handover events, 2026-10-27T22:40:16Z, rc=2). The PI's decision and one leg of validation saved the returns (`defects.jsonl` lines 121 and 122).

**1.3 Readers after the D3c interview: J's ruling and stage E1.**
- *J* (the head): no labelers and no readers for the rest of the run.
- *Stage E1* (lines 5 and 6): "the reconstruction readers on the routine reader model, sent by the dispatch".
- *What happened.* The handler dispatched them (handover events, 2026-10-27T22:27:44Z and 22:29:17Z). I read the stage's own fleet as outside the ruling. That reading is mine; I did not ask.
- *What it cost.* Nothing in the work. But the ruling and the stage disagree, and the record does not say which one governs.

**1.4 What the reconstruction is compared against: the design note and stage E1.**
- *The design note* (lines 130 to 132): the global model plus the adaptations, "rebuilt and compared with the room model by a reader"; "the blind `case.md` and the informed `model-10.md` are kept as a pair".
- *Stage E1* (lines 172 to 176): the reader scores the skeleton against the coder's `case.md`, claim by claim, "never `model-D.md`".
- *What I did.* I followed the stage.
- *What it cost.* The coder's account covers the room's whole week, so 42 of the 200 lines I read for the causes of a low score were the room's business off the canvas (`audit-E1/reconstruction_causes.json`). A room model written in the global vocabulary would not hold them. The fidelity of 0.871 therefore measures how well the skeleton preserves the coder's account, not the room model the design note names.

**1.5 In-sample or out-of-sample: the design note and METHOD.md.**
- *The design note* (lines 346 to 349, J's decision 6): "The return at stage 10 is in-sample at the second-order tier and out-of-sample below it; the methods say so."
- *METHOD.md* (lines 167 and 168): in-sample at the tier the model was built from, with uncited concepts and quotes "used as additional in-sample checks, never called out-of-sample". Stage E1 (line 156) says the same of uncited concept ids.
- *What I did.* I followed METHOD.md and called every figure in-sample.
- *What it cost.* Nothing in the work. But the paper must choose, and the two documents give it opposite words.

**1.6 The room forms after the projection: stage D4 and J.**
- *Stage D4* (line 155): "Do not recut branches after seeing it", meaning the chunk-share comparison.
- *J* (26 October, the head): six room forms, cut by changes and codes after the projection, ruled "not a recut". Then QE1-001 (27 October, 18:45 Berlin): "I would not change the structure of the journey for bookkeeping."
- *What I did.* I followed J and recorded the forms as not a recut.
- *What it cost.* The E1 check first counted 82 D4 snaps as ordering errors, which took a question and a change to the check. And the forms were cut with the projection and the chunk-share tree in the folder. The audit lists that as a place the canvas may have shaped the work without a declaration (`audit-E1.md`, section 1, part 2).

**1.7 Whose answer it was: the first messages and the answer files.**
- *The first messages* say "The principal investigator answered your questions" for every answer: for QC1-003 (C1a-06), QD6-001 (D6a-02) and QD6-002 (D6a-03) as for the rest (`out/_analysis/e2_first_messages.txt`).
- *The answer files* say otherwise. QC1-003 is "the handler's ruling under J's delegation ... J is away and will see it when he returns". QD6-001 and QD6-002 are "Handler's view, given on J's instruction ...; J has not seen this" (`out/_answers/`).
- *What I did.* I followed the answer files, and the head carries "QC1-003 (the handler, for J)".
- *What it cost.* Little in the work. But a message that overstates who ruled weakens the record of who answers for each ruling, which is the proposal's own promise (`handling/proposal.md` line 25: "we decide which accounts enter the model and answer for them").

**1.8 The E1 dispatch: the PI's message and the harness's record.**
- *The PI's message at E1d* (27 October, 22:51Z; `_transcripts/leg-E1.E1d-7800c4df…jsonl`): the dispatch ran "on deepseek/deepseek-v4.1-flash direct (the @preset/cheap reader in arm.json returned HTTP 400 at the probe ...)".
- *The harness log*: "dispatch E1 gateway deepseek/deepseek-v4.1-flash x1" at 22:29:17Z, after the first dispatch on "@preset/cheap" at 22:27:44Z failed (rc=1). `_fleet_raw/E1/arm.json` gives route "gateway".
- *The inconsistency is a word with two readings.* "Direct" can mean the model named directly instead of the preset alias, which the log bears out, or a route other than the gateway, which it does not. I took the second reading into the audit, and corrected it at E1e from `arm.json` (`defects.jsonl` line 124). The misreading was at least as much mine as the message's.
- *What it cost.* One wrong word in the audit and one reassembly.

**1.9 The unit of analysis: J's rule and the second readers' standard.**
- *J* (the head): "Keep the room, or groups of rooms, as the unit."
- *The field analyst's second reading at C5*, supplied for the account, tested each sentence against a package of quotes.
- *What I did* (C5.C5d, turn 6, answer 3). I accepted 94 pieces of its advice and, in passes 7 and 8, applied its standard to the model's own statements: "'The room judges it has too few hands' became 'single members voice the judgment'. That demoted the unit of the study." J named the drift, and pass 9 restored the room in three places.
- *What it cost.* Three passes, and "one demotion I know of stands" (the same answer).

**1.10 The note's length: the A1 hook and J's intent.**
- *The hook*, before 09:01 Berlin on 7 October, refused room notes over 350 words, so 562 notes were cut (`handback-A1.md`, "The restore").
- *J's later ruling* made about 350 words "a guide, not a limit". The check now reports a long note as a warning (`tools/checks/stage_A1.py` lines 94 and 95).
- *What I did.* I cut the notes to pass the hook, then restored them from the handler's recovered lines.
- *What it cost.* The restore took five legs, A1b-49 to A1b-53, over 447 rooms (`handback-A1.md`).

**1.11 The local measure: J's ruling and J's later question.**
- *J's ruling after D3c* barred the readers that would validate local adaptations (the head).
- *At D6b* (turn 49, question 5) the interview asked: "Why was the prior.md section 3 measure not computed?"
- *My answer* (D6b, turn 51): its validated half needed what the ruling had barred. But the other half, element reach, "is computable with the files we have, in about a leg". So the question was fair for that half. I computed it only at E1a (88.46 per cent of themes with a coordinating turn).

**1.12 The head's ceiling: the design note and CLAUDE.md.**
- *The design note* (line 214): a head of "about 1,500 words".
- *CLAUDE.md* (line 22): "The head is at most 3,000 words."
- *What I did.* I followed CLAUDE.md.
- *What it cost.* Little. At 3,000 words the head carried J's rulings and left less room for the state of the argument (`experience-E1.md`, section 1).

## 2. What made the work harder

**2.1 Dispatches without a dry run.** The harness log shows the pattern.
- B4, C2, C5 and D2 each ran a dry run before the dispatch, and each returned rc=0.
- B2 had 3 dry runs in 14 dispatch lines, and 6 of its 11 recorded outcomes were rc=1 or rc=2.
- B3 had 4 dispatches, 2 of them rc=2.
- E1 had no dry run, and both its dispatches failed: rc=1 at 22:27:48Z and rc=2 at 22:40:16Z.
- D3 also had no dry run, and its one dispatch returned rc=0. A dry run is therefore neither needed nor enough for success: B2 ran three and still failed. But the four later stages that ran one before their single dispatch all succeeded, and E1, which ran none, failed twice.

At B2 the failures meant rounds rebuilt by hand and a failed round set aside (QB2-005, QB2-006). At E1 they meant 30 exhausted rooms (1.2).

**2.2 Tools that did not do what their help or the stage said.**
- `mem.py diary --last 5` served an older diary part once the diary passed nine parts (`handback-A1.md`, instrument item 1). J's ruling 7 of 7 October fixed it.
- `mem.py theme` prints the working placements, so the stage's stranger test could not be blind (`handback-B1.md`, instrument item 1). `mem.py scheme` served the shipped line without members (item 2).
- `packets.py` did not build B2's later rounds under J's rulings, so my own builders did (`handback-B2.md`, "The packets").
- `handoff.py` prints the payload figures only after it writes the folder, against D1's order (`handback-D1.md`).
- `probe.py` could not read 283 of the 300 answer files, which were written in bold (`audit-E1.md`, section 1, part 5).
- No verb served the package's canvas manifest (`handback-A1.md`, instrument item 2).

**2.3 Checks that refused what had been ruled, or were themselves wrong.**
- QD1-001: "an element may sit in two or more dimensions, so the list is right and the check was wrong".
- QB2-011: "the three shapes were the handler's, not yours".
- QB3-002: `vlib.store_themes` counted the withdrawn split's children.
- QC4-001: "the handler put field/ in the wrong place".
- QD6-001: the check refused the form letters J had ruled, and D6a-01 closed paused (`PAUSES-D6`, 03:51:35Z).
- QD6-002: the trusted tree hash was missing, and D6a-02 closed paused (04:19:57Z).
- QE1-001: the 82 snaps (1.6).

Each cost a question, and usually a pause. Each was settled by a change to the check. In each answer the handler said plainly whether the check or I was at fault.

**2.4 The command guard.** It refused:
- `cut` after a read or a helper (`handback-D1.md`; D6a-03 and D6a-05 in `handback-D6.md`; E1b-08 and E1d in `notes-E1.md`);
- a shell variable (`handback-D5-room-forms.md`, slips);
- Python's `|=` (D6a-10);
- `diff` with process substitution (D6a-09).

At A1, "some denials named no rule" (`handback-A1.md`, instrument item 8). No refusal changed a result, but each one meant rewriting a command as a script. The rules grew into a list the head had to carry ("Rules kept").

**2.5 A field that could not tell rooms apart.** The labelers' local status gives every room "unresolved" and every grade "composes-with-residue" (D3.D3c, turn 41, question 3; turn 43: all 705 rooms and all 1,882 lines). The effective manifest gives the same for all 705 (`audit-E1.md`, section 5). With J's ruling against further readers, nothing could validate a local adaptation. So local adequacy, one of `prior.md` section 3's two grounds, could not be established. The composition line reads unresolved for that reason.

**2.6 A vocabulary that nearly barred an outcome.** The return produced 11 contradict lines at the first return and 4 at the re-check, out of about 95,700 (D6.D6b, turn 51, question 4). "Replace" was unreachable at the forms, so they could not show the level below contradicting the level above. They showed it only as restrictions: 43 to 63 per cent of each form's restrict lines on arrows say the arrow fails (`handback-D6.md`).

**2.7 Work undone by a later ruling.**
- At B2b-r2-p2 I split six bags into children, and J withdrew the split (`handback-B2.md`; "No one cuts the bags", J, 12:24 Berlin).
- The A1 notes the hook had cut were restored over five legs (1.10).
- J's first ruling of 7 October, which arrived after A1c had closed (2026-10-06T23:54:12Z), sent me back to read the case account and brief of 702 rooms (legs A1b-20 to A1b-48). That one corrected a cut of mine (section 4).

**2.8 Answers given in forks the run could not keep.** Every interview ran "in a copy of your folder ... nothing you do here reaches it" (each interview's opening turn). The checks I ran in interviews entered the run only through J's later rulings, or through a leg that redid them:
- A11 cannot fail, and the kind agreement is kappa 0.08 (D3.D3c, turn 43);
- the count measures point to 4 or 6, not 8 (D4.D4a-05, turn 63);
- the threshold table, and E's restrictions held at matched size (D6.D6b, turn 51), redone at D6a-09 and D6a-10 (`handback-D6.md`).

The cost was repeated work, and findings that sit outside the ledgers except as rulings.

**2.9 Long legs and compaction.** The diary holds 157 notes that begin "compacted", 51 of them at D3 over its 60 legs (`audit-E1/experience_facts.json`). Each compaction cost re-orientation, and some cost errors: at E1d I typed two counts from memory after one (diary, E1d, 23:08:00).

**2.10 A frozen model reported with its known faults.** After QD4-001 every file that reports the model must state P05's bound and A11's withdrawal in full beside it (the head; `audit-E1.md`, the composition result). The cost of 1.1 therefore recurs in every report.

## 3. What helped, and what I would keep

**3.1 Rulings that set a method in one sentence.**
- QD3-002 (J): "the analyst is doing induction. At this point they can place these codes where they see fit" (`out/_answers/QD3-002.md`). It ended a run of questions about rules, and returned the placing of codes to the evidence.
- QC2-002 (J): "the criterion is a guide, not the judge, and a rise in residue is not a failure". Pass 5 could then keep the changes the evidence supported without chasing a number.
- QB4-001 (J): "The point is to try to adjudicate." It stopped me adding themes to rulings, so a ruling became a choice among the placements.
- QD3-001 (J): "no default decision". Every line of the return was ruled with a reason (`handback-D3.md`).
- J on drift (16 October, 19:08 Berlin, the head): a ruling rule changes only by a dated amendment that says whether it applies backwards. It kept the rules stable across 157 compactions. The one time I widened a rule without such an amendment (D6a-04), the next interview caught it (D6.D6b, turn 51, question 6).
- *I would keep them* because each was short, came from the evidence in front of J, and closed a question for good.

**3.2 The interviews as checks.** J's questions found faults I had not looked for:
- A11 cannot fail as it stands (D3.D3c, turn 41, question 2);
- the kind of add and restrict lines agrees at kappa 0.08 (question 5), which became J's ruling not to rely on it;
- what the clustering read, whether it followed J's brief, and why its scores rose with k (D4.D4a-05, turn 61);
- how far the forms' cells depend on the thresholds, which led to correcting "without contradicting" at D6a-09 (D6.D6b, turn 49, question 4; `handback-D6.md`);
- the medoid as a poor choice for a polyfaceted form (D6.D6a-16, turn 47, question 1).

J's standing question also asked each time what support would help (C4.C4a turn 61, C5.C5d turn 4, C5.C5d-p2 turn 82, each question 6). *I would keep the interviews* because they were the run's only human reading of the reasoning itself, and they asked for counts and ids, not impressions.

**3.3 A handler who said whose fault it was.** The answers named the handler's own errors plainly: "the three shapes were the handler's, not yours" (QB2-011); "the list is right and the check was wrong" (QD1-001); "the handler put field/ in the wrong place" (QC4-001). The checks changed the same day. *I would keep this,* because an analyst who cannot tell a tool's fault from its own will distrust either the tool or itself.

**3.4 The record and the memory tools.**
- The head and the diary carried the run across 157 compactions: "The compaction in D6a-04 lost nothing written, because the diary and head carried the state" (D6.D6b, turn 51, question 6).
- `validate.py --open` and the close-check caught errors before a leg could close. At E1d the first assembly of the audit failed on wording, and it was fixed before the close (diary, E1d, 23:15:48).
- `cite.py` and the store let the audit resolve 3,218 of 3,230 cited quotes to their concepts (`audit-E1.md`, sections 6 and 7).
- The ledger tools and `rebuild.py` gave the effective ledger as one served object at E1.
- *I would keep all of these* as they are. They are why a stranger can rerun almost every figure.

**3.5 The first message that names the answered questions.** At the next leg's start, the harness wrote "The principal investigator answered your questions ...: read them with python3 tools/mem.py asks <id> before your first write, and revisit the work that rested on your assumption" (37 of the 56 first messages with an addition, `out/_analysis/e2_first_messages.txt`). It told me exactly when an assumption needed revisiting. *I would keep it,* with the attribution corrected (1.7).

**3.6 The PI's decision at E1d.** The decision was to validate the returns from the raw files, drop only a final marker line and record that I did, log the mismatch as a defect of the instrument, and not re-dispatch (`_transcripts/leg-E1.E1d-…jsonl`). It was bounded and stated its rule, and it named the fault as the instrument's. *I would keep that form* for any salvage: state the rule, record what was dropped, file the defect.

**3.7 What the design note's discipline did reach.**
- The packet ceiling is asserted in `packets.py`, and the E1 packets ran from 29,610 to 47,848 bytes, under 50 KB.
- The counts rule (rule 19) let the audit recompute 361 count phrases in the handbacks and find 2 wrong (`audit-E1.md`, section 1, part 2).
- The rule to state the method question in the contract kept the run's purpose in every head.

## 4. Freedom given and taken

**What freedom means here.** METHOD.md says "The researcher is still the instrument" (line 151). Stage E1 names Gioia, Corley and Hamilton's "instruction to think at both levels at once" (lines 208 and 209), which the fourth-order cut at C1 departed from. The stage asks me to judge freedom also by Gioia, Anand and Hamilton. No text of that work is in this folder or on the shelf I read, so I cannot say what it asks, and I do not cite it. Below, freedom is the researcher's freedom to see, name, place, cut and revise categories on the evidence. Freedom is taken where a ruling, a rule or a check decided in my place.

**4.1 Freedom given.**
- *The tiers above the coders were mine.* Rule 11: "Recutting is allowed at every tier you built" (`CONTRACT-aggregator.md` line 372). I built the third-order and fourth-order themes, the dimensions, the model and its arrows, and the names. I ruled the readers' splits: 163 at the first return and 161 at the re-check (`verdicts-D.jsonl`).
- *J gave the induction back when the rules crowded it:*
  - "the analyst is doing induction ... they can place these codes where they see fit" (QD3-002);
  - "But you know these rooms" (QD3-006);
  - "But they should be able to decide on this" (QD3-008);
  - "Whatever the agent feels more comfortable with" (lone B1 themes, the head);
  - "the criterion is a guide, not the judge" (QC2-002).
- *J asked about support rather than prescribing it.* Each interview's last question asked what support would raise my confidence (3.2).

**4.2 Freedom taken, and whether rightly.**
- **Rulings add no theme** (QB4-001; J's rulings of 06:45 and 06:47 Berlin, the head). This took the ruler's freedom to see a theme no reader placed. *Right.* A ruling decides among readings; a theme only the ruler saw cannot be checked by the fleet the design relies on. J named the motive he suspected ("the analyst trying to be nice"). The record cannot confirm or refute it.
- **No one cuts the bags** (J, 12:24 Berlin). This withdrew my split of six bags at B2b-r2-p2. *Mostly right.* The bag is the coders' unit, and the design gives that tier to the coders (`design-note.md` lines 31 to 38). The cost is real: at C1 a room such as greenlattice t03 has most of its acts listed beside one placement (`handback-C1.md`).
- **My two amendments reverted** (QD4-001). *Right on procedure, costly in substance.* A model changed at D4 is no longer the model the 705 rooms were re-checked against, and rule 11 places amendments at D3. But the arrow that cannot fail stays in the model. The better course was the one I named at D3c: "a D3 amendment leg before D4 opens" (D3.D3c, turn 43). The record does not say why it was not taken.
- **The room forms were designed by J.** J set the method (D4.D4a-05, turn 61, question 3): arrows counted through their third-order theme; three levels counting equally; mix, not number; no weight for one-room changes; no broad form; a count from 4 to 8. J then ruled the six forms (the head). *Partly right.* The theory question asks for forms, and the 35 facet branches did not give them. But the forms are leans of a continuum (cut stability about 0.21, `handback-D5-room-forms.md`), and my count measures pointed to 4 or 6, not 8 (D4.D4a-05, turn 63). The choice was J's to make, and the head reports it as J's.
- **No second coder on my solo reads, and no further readers** (the head, J's rulings for stage D and after D3c). I asked for a second reader or coder three times:
  - C4.C4a, turn 63: "one targeted pass on the declaration prose ... with a second reader";
  - C5.C5d, turn 6, answer 6: "A second coder on border talk";
  - C5.C5d-p2, turn 83, answer 6: "a second coder on my solo reads".
  
  The reason given was that "Codex did not read all rooms, so its evidence is thin". *Defensible, but costly.* The reason concerns one candidate coder's coverage, not the value of a second reading. Several findings rest on my coding alone (F-014; A04's border reading, whose one second coding gave kappa 0.19), and local validation could not be established (2.5).
- **Do not rely on the kind of add and restrict lines** (kappa 0.08, the head). The ruling rests on evidence I produced. *Right.*
- **The fixed thresholds and declared rules** (the floors, the 1.5 lean, the stopping rules; "the thresholds are the design's heuristic; the rule is unchanged", the PI's clarification of 8 October, the head). They fixed in advance what Gioia's approach leaves to judgment. *Mostly right for this design.* Every script declared its rule before it ran, which is why the audit could rerun the figures. Where a criterion would have decided against the evidence, QC2-002 gave judgment back.

**4.3 Where the handling was right and I was wrong.**
- **A1's reading route.** I cut the stage's reading of every room through its forest, case account and brief, and logged the cut late (`departures.jsonl` line 5). J's first ruling of 7 October sent me back to read the case account and brief of 702 rooms (`handback-A1.md`).
- **The unit at C5.** I applied the second readers' sentence standard to the model's own statements, and demoted the room. J named the drift (C5.C5d, turn 6, answer 3).
- **The kind of a line.** I relied on it until J's question showed kappa 0.08 (D3.D3c, turns 41 and 43).
- **The forms' placement and count.** I placed rooms by Ward on their whole mix, not by J's rule; 243 of 684 rooms would land elsewhere under J's rule. The scores I offered for 8 groups rise with any count (D4.D4a-05, turn 63). J's "Did they follow our method?" and "That was not the case for us" were right.
- **The branch rule at D6a-04.** I widened it as a licence, not as the dated amendment J's rule on drift requires (D6.D6b, turn 51, question 6).
- **The rooms for the tellings.** J's "A mediod is not representative of a polyfaceted cluster" was right. My nearest-the-centre rule picked rooms that mix forms (D6.D6a-16, turn 50, answer 1).
- **The E1 return specification.** I wrote it without reading the packet's trailer (1.2). The tool's line was there to be read.
- **The E1 route.** I took an ambiguous word into the audit without checking `arm.json` (1.8).

**On balance.** I was given the freedom the method asks for at the tiers I built, and J returned it more than once when rules crowded it. It was taken mainly at three points: the coders' unit, the model's freeze, and the forms. At the first two, taking it protected the design, at a cost to the model. At the third, J's design answered the theory question that my facets did not, with forms weaker than their names. The freedom that was refused, a second reader, is the one I would build into the next instrument rather than leave to a request.
