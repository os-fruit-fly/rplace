# The next instrument (stage E2)

Written at E2b, 28 October 2026, after reading `handling/proposal.md` whole. This is a design argument for the instrument I would build to deliver that proposal next time. Each change names the evidence from this run that motivates it, and the risk it brings. The evidence is cited to files, interview turns, the harness log and the diary, as in `handling-E2.md`. I write as the analyst who ran this instrument from A1 to E2. I hold the run's record, not its memory (`experience-E1.md`, section 1).

## 1. What the proposal claims, and what this instrument could and could not deliver

The proposal makes six claims an instrument must carry. For each, here is what this run delivered and what it did not.

**1.1 A baseline that later models are judged against** (lines 9 and 31: "later models are judged by what they add to the baseline").
- *Delivered.* A frozen model (46384686…) with 45 elements and 21 arrows, re-checked in all 705 rooms. Every move is snapped, every line is ruled with a reason, and every quote resolves to a concept (3,218 of 3,230, `audit-E1.md`, sections 6 and 7).
- *Not delivered: a way to judge a later model against it.*
  - The model changed inside the run, from e15f9647… to 46384686…. The fixed-global verdicts moved from 201 to 630 rooms composing.
  - My own interview answer called that rise "partly circular": the fifteen candidates came from the same rooms' proposals (D3.D3c, turn 43, answer 2).
  - Within one run, then, the instrument could not separate a better model from a model that had absorbed its rooms' residue. A later model would face the same problem.

**1.2 Composition from a census of 705** (line 9: "LLMs let us compose knowledge from a census of 705 curated communities").
- *Delivered.* At the population level the model composes in the return's terms: 630 of 705 rooms compose and 56 with residue, and none fails.
- *Not delivered.* `composition_status: unresolved` (`audit-E1.md`, the composition result).
  - The forms compile rather than compose, and only 2 of 35 branches explain their members jointly.
  - At the leaf the shared account holds (fidelity 0.871, none contradicted), but local adequacy is not established.
  - The reason is in the instrument, not the rooms. The labelers' local status separates no room (D3.D3c, turn 43, answer 3), and no reader was left to validate an adaptation (`handling-E2.md`, 2.5).
- *A smaller point on the census.* The proposal says that 705 communities "show evidence of coordination" (line 17). Under the run's coordinating-turn rule, 9 rooms have none (`notes-A1.md` line 678). `prior.md` section 3 therefore counts 696.

**1.3 Each case's full record kept, and departures found by coders** (lines 19 and 23).
- *Delivered.* The store keeps every concept in the participants' words, and every coder quote was found in its item (a share of 1.000 in the handler's check of 80 rooms). The return gave every room's departures as ruled lines: 95,736 of them, of which 72 are accepted corrections (`handback-D3.md`).
- *Not delivered, or delivered weakly.*
  - The coders' case accounts are the weaker record: 0.6573 of their quoted strings were found in the room's corpus.
  - The departures came almost only as restrictions. The return produced 11 contradict lines at the first return and 4 at the re-check (D6.D6b, turn 51, answer 4), so a departure that replaces an element could hardly be recorded.

**1.4 A division of learning: coders find departures, people judge their significance** (lines 19 to 21 and 25: "The agent codes and composes; we decide which accounts enter the model and answer for them").
- *Not delivered as written.* In this run an LLM analyst built every tier above the coders. It ruled the 324 splits of the verdict readers, wrote the model, and judged which departures entered it. J ruled at named points, through 53 answers and nine interviews (`experience-E1.md`, section 11). But the judgment of significance, line by line, was the model's.
- *Where the people did decide, the record shows they mattered.* J's rulings reverted two amendments, set the forms' method, and barred reliance on a label that agreed at kappa 0.08 (`handling-E2.md`, 4.2). The proposal's division is right as an aim. This instrument did not build it.

**1.5 The checkpoint interview** (line 25: "The agent answers from the state it held when it decided").
- *Delivered in part.* Nine interviews ran on forks, and they were the run's best checks (`handling-E2.md`, 3.2).
- *Not delivered as claimed.*
  - The state an interview resumes is the leg's compacted context and its files, not the moment of decision. The diary records at least 157 compactions. In one interview I said, "I don't hold the C5d interview itself" (C5.C5d-p2, turn 83).
  - What an interviewed agent gives is a reconstruction checked against its record. That is worth having, but it is not the decision context.
  - Nothing found in an interview reached the run except through a later ruling (`handling-E2.md`, 2.8).

**1.6 Triangulation: quotes resolved, 300 communities coded twice, human audits, two comparison models, an outside witness** (lines 27 and 29).
- *Delivered:*
  - the quote resolution, for codes and partly for case accounts;
  - one theory-free comparison, the chunk-share tree;
  - one outside witness, the field analyst at C4, who confirmed the account of authority and corrected three of my sentences (`handback-C4.md`).
- *Not delivered in this run:*
  - the double coding of 300 rooms;
  - any human audit at any tier (`audit-E1.md`, sections 6 and 7, the standing departures).
- *A warning from the comparison that was built.* It sorted the rooms largely by how much the coders coded (silhouette 0.024, `handback-D4.md`). A clustering on term frequencies, as the proposal plans, will do the same unless it holds size.

**In one sentence.** This instrument delivered a traceable census model and a population-level composition. It did not deliver a decidable test of composition below the population, the proposal's division of learning, or the human audit. Those three are the design problem.

## 2. Making the test of composition decidable

**2.1 Hold rooms out, and return to them last.** This is the first change I would make.
- *The change.* Before A1, seal a seeded sample of about 10 per cent of the rooms (about 70), stratified by record size and onset. The coders code them as usual. The analyst never reads them. After B2's freeze the B3 fleet places their second-order themes into the frozen scheme, and a tool routes them up the frozen tiers. After the model and the forms are frozen, a hold-out return stage puts the frozen model to them: the same labelers, the same verdict readers, and the reconstruction.
- *The evidence.*
  - Every test in this run is in-sample (`audit-E1.md`, the methods paragraph).
  - The rise from 201 to 630 composing rooms is partly the model absorbing its own rooms' residue (D3.D3c, turn 43, answer 2).
  - The reconstruction's skeleton was built from each room's own lines, so a high fidelity was expected (`audit-E1/section-09.md`).
  - J's reason for no holdout was that held-out rooms "would need placement into the scheme before they could be routed up the table" (`design-note.md` lines 346 to 349). The B3 fleet already does that placement, with agreement 0.786 and gold fidelity 0.645 (`audit-E1.md`, section 1, part 3).
- *What it settles.* The hold-out is in-sample at the coders' tier and out-of-sample at every tier the analyst built. Those are the tiers whose composition the method question asks about. It also settles the wording conflict between the design note and METHOD.md (`handling-E2.md`, 1.5).
- *The risk.*
  - The census claim weakens: about 635 rooms build the model.
  - Rare forms lose members: form F had 56 rooms, and a tenth of it is small.
  - The fleet's placement error enters the test.
  
  To limit this, report the hold-out result beside the in-sample one, and report the fleet's placement agreement on the held-out rooms with it.

**2.2 Compute local adequacy as a tool, inside the return.**
- *The change.* `prior.md` section 3's measure, run by a tool at D3's close. Element reach is computed per room. Each room's accepted adaptations are then validated by a critique from that room's coder checkpoint (the design note's coder review, lines 164 to 172): each adaptation holds, does not hold, or cannot be told, with codes. That is done on a seeded sample of rooms large enough to give a rate with an interval.
- *The evidence.*
  - The measure was declared and never computed, and the composition line could only read unresolved (`audit-E1.md`, the composition result).
  - The labelers' local status gave all 705 rooms the same value (D3.D3c, turn 43, answer 3).
  - The element-reach half took one script at E1a: 4,759 of 5,380 themes with a coordinating turn are reached, and 297 of 696 rooms in full.
- *The risk.* The coder that validates its room's adaptations shares its own reading of the room, so the check is circular at the room level. And checkpoints exist only where the coder kept them (design-note line 171). A sample keeps the cost bounded, and the circularity must be stated.

**2.3 A second ruler, built in rather than asked for.**
- *The change.* On a seeded share of the analyst's rulings at D3, and of its placements at B1 and C1, a second ruler rules blind. The second ruler is a person, or an analyst of another model family. Disagreements go to J with both readings, and agreement is reported per op and per tier.
- *The evidence.*
  - The kind of add and restrict lines agreed at kappa 0.08 (D3.D3c, turn 43, answer 5).
  - The one second coding run on my reads gave kappa 0.19 (A04's bound).
  - I asked for a second reader three times and was refused (`handling-E2.md`, 4.2).
  - The run had no human check at any tier.
- *The risk.* Cost and time. A second model shares architecture-level habits with the first. Disagreement without a tie-break stalls the work, so the tie-break is fixed in advance: J decides, and the record keeps both readings.

**2.4 A return vocabulary that can say an arrow fails.**
- *The change.* Split "restrict" into three ops:
  - *holds narrower here*, a scope;
  - *fails here*, the room did otherwise;
  - *the record cannot show it*, an evidence state, not a change.
  
  Seed gold items for each into the labelers' brief.
- *The evidence.*
  - The return held 15 contradict lines in about 95,700 (D6.D6b, turn 51, answer 4).
  - 43 to 63 per cent of each form's restrict lines on arrows say the arrow fails (`handback-D6.md`).
  - Form E's restrict lines most often say the record cannot show the order: 113 of 304 (D6.D6b, turn 51, answer 2).
  
  The forms could not show a level contradicting the one above, and the reconstruction could not tell an omitted particular from a failed arrow without my reading (`audit-E1/section-09.md`).
- *The risk.* Readers may call "fails" on thin records. The evidence states already in SCHEMA-adaptations.md (unobserved, not testable) are the guard, and the gold items calibrate them.

**2.5 Amendments on a schedule, and held proposals tested on the hold-out.**
- *The change.* After D3's ruling, one amendment leg. Every correction met in two rooms becomes an amendment, the affected rooms are re-checked, and then the model is frozen. J's views on amendments arrive as rulings before the freeze, never as plans for a later stage that the checks forbid. After the freeze, a change is a held proposal, and the hold-out return (2.1) tests it.
- *The evidence.* The costliest inconsistency of the handling: J planned that D4 would write P05's bound, which the contract and the D4 check forbid. The amendments then made at D4 were reverted, and the model kept a clause that fails in nine rooms and an arrow that cannot fail (`handling-E2.md`, 1.1). At D3c I named the alternative: "a D3 amendment leg before D4 opens" (D3.D3c, turn 43).
- *The risk.* An insight that comes late waits. That is the right cost. A held proposal tested on rooms the analyst never read is worth more than an amendment tested on the rooms that suggested it.

## 3. The stages, the stops and the interviews

**3.1 What I would keep.**
- **A1, every room read whole, through the forest, the coder's account and the brief.** When I cut the reading route, J's ruling sent me back to read the account and brief of 702 rooms (`handback-A1.md`). The full reading is the census's foundation, and the design note already keeps it (line 310).
- **B1 to B4, the scheme and its transmission tests.** They told me where the written scheme does not decide. Exchanges between rooms decide worst (`handback-B4.md`).
- **C1 to C5, the model's loop, with the hostile reader, the literature, the field and the account.** The hostile reader found nine errors (`handback-C2.md`). The field corrected three of my sentences (`handback-C4.md`).
- **D1 to D3, the return to every room** (section 6).
- **E1 and E2.**

**3.2 What I would cut or merge.**
- **The dimension tier, as a tier the analyst maintains.** It does no work in the account, the arrows or the branches (`audit-E1.md`, sections 6 and 7). I would generate the dimensions from the fourth-order themes as a reporting layer, which keeps the Gioia figure the paper needs.
  - *Risk:* a tier the analyst does not maintain may be read as an afterthought. The methods paragraph must say what it is.
- **D4 and D5 into one forming stage, with its method agreed in writing before the first cut.** In this run:
  - the 35 facet branches did not give the forms the theory question asks for;
  - J asked whether they could be joined (D4.D4a-03, turn 123);
  - J then set a method I did not follow to the letter (D4.D4a-05, turn 63: 243 of 684 rooms would land elsewhere under J's rule);
  - the count I offered was favoured by measures that rise with any count;
  - the forms were cut again under J's ruling.
  
  One stage would fix the forming method, the count criterion (a count-neutral measure, such as the gap between merge heights or stability on matched subsamples) and the placement rule before any cut. It would then cut once.
  - *Risk:* a method fixed early may not fit what the ledger shows. A dated amendment, as J's rule on drift asks, is the outlet.
- **The tellings' rooms chosen by coverage of the form's own cells, not by nearness to the centre.** J's "A mediod is not representative of a polyfaceted cluster" was right, and my nearest-the-centre rule picked rooms that mix forms (D6.D6a-16, turns 47 and 50).

**3.3 What I would add.**
- **A hold-out return stage** after the forms are frozen and before the audit (2.1).
- **A human audit stage** before E1, which the design note promised and this run did not build (`design-note.md` lines 298 to 303). It would sample, source first:
  - accepted and rejected ruled lines;
  - branch and form memberships;
  - the account's quotes.
  
  It reports its agreement with the analyst.
  - *Risk:* cost in human hours. The sample is small and seeded, and the audit's scripts serve it.

**3.4 Where the stops and the interviews should fall, and what they should leave behind.** In this run, interviews fell where a leg happened to close: C4a, C5d twice, D3c, D4a-03, D4a-05, D4a-06, D6b and D6a-16 (`handling/interviews/interviews.tsv`). Their findings could not reach the run except through later rulings (`handling-E2.md`, 2.8). I would fix five interviews, each at a decision:
1. after C2's first full pass of the model, before the account;
2. after D3's ruling, before the amendment leg (2.5);
3. before the forming cut, on the method (3.2);
4. after the hold-out return, on what held;
5. at E2.

Each interview ends with a ruling file the next leg must read: who ruled, what, and whether it applies backwards. A finding made in a fork then enters the run as a dated ruling. The D3c interview is the evidence. It came after the freeze was decided and before D4 opened, and the plan it carried for P05 could not be carried out (`handling-E2.md`, 1.1).
- *Risk:* fixed interviews can come too early or too late for a surprise. The pause protocol stays for unplanned questions.

**3.5 Shorter legs where the reading is heaviest.** D3 took 60 legs, 55.7 million output tokens and 51 logged compactions, more than a third of the run's output (`audit-E1/experience_facts.json`). After compactions I typed figures from memory (diary, E1d, 23:08:00). Legs bounded by element groups and closed by state on disk, as the design note already argues (lines 235 to 244), would bring fewer compactions and fewer such slips.
- *Risk:* more legs mean more orientation, and the head must carry the state.

## 4. The division of labour

The proposal's division of learning is right: the agent codes and composes, and people decide which accounts enter the model and answer for them (lines 19 to 21 and 25). This run did not build it (1.4). I would build it at five gates, and leave the rest of the work where it was.

- **The coders** keep the first two tiers and the case accounts, run once per room and sealed from each other. Two model families code a seeded 300 rooms, as the proposal plans (line 27). Their agreement is reported as agreement, not reliability. Each coder's checkpoint is kept, so its room's adaptations can be put back to it (2.2).
- **The fleets** test transmission (B2 to B4), label the return (D2), give verdicts and read the reconstruction. They are a prosthesis, never a judge (METHOD.md lines 150 to 152). Nothing in this run argues for more fleets. It argues for dispatches tested before they run (5.1).
- **The analyst** builds tiers three and four, the model and its arrows. It rules every return line with a reason, proposes amendments and forms, and writes the accounts. It does not decide what enters the standing model at a gate. It prepares that decision.
- **The principal investigator** decides at five gates, each prepared as a decision file with options, as the QD questions were:
  1. the scheme's freeze;
  2. each candidate element's entry into the standing model;
  3. the amendment set before the model's freeze (2.5);
  4. the forming method and the forms (3.2);
  5. the wording of the composition verdict.
  
  *The evidence:* in this run J's rulings at points like these were the decisive ones: QD3-011 (freeze 46384686), QD4-001 (the amendments held), and the six room forms. What the run lacked was not J's judgment but a schedule for it.
  *The risk:* J becomes a bottleneck. Five gates, each a short file with options, keep the load bounded. The run's 53 answers show the form already works.
- **The handler** runs the tools, the dispatches and the messages. Every message names its author, and none says "the principal investigator answered" for a handler's ruling (`handling-E2.md`, 1.7). Every fact in a message points to its record, as a dispatch's route should point to `arm.json` (1.8). A change to a check is recorded as a dated amendment, with the ruling it serves.
- **A human auditor**, J or a colleague, reads the audit sample (3.3).

## 5. The tools I would want

Each tool answers a failure on record.

5.1 **One source for the packet, its return specification and the validator's schema.** `packets.py` would emit `RETURN-NN.md` verbatim, with its end marker. A dry run would push one packet through one reader and the validator before every dispatch. *Evidence:* the E1 trailer and specification disagreed, and all 30 returns failed (`handling-E2.md`, 1.2). The four later stages that ran one dry run before a single dispatch all succeeded, and E1, which ran none, failed twice (2.1 there). *Risk:* a dry run costs one reader's time per dispatch, which is small.

5.2 **A local-adequacy tool** for `prior.md` section 3's measure, run at D3's close (2.2).

5.3 **A ruling file read at every leg's start.** `rulings.jsonl` would hold the id, author, date, text, the provision it overrides, and whether it applies backwards. `validate.py --open` would print the new ones, and a check would accept a shape a ruling allows by the ruling's id, not by an edit to the check's code. *Evidence:* the checks refused what J had ruled at D6a-01, D6a-02 and E1 (QD6-001, QD6-002, QE1-001), and each needed a code change. The design note already asks that an override name the provision it overrides (line 283).

5.4 **The head's history kept as text,** every version, snapped. *Evidence:* E1 asks for every head in order, and only the last one exists (`handback-E1.md`).

5.5 **The manifest as JSON lines, appended by a tool.** *Evidence:* the stage's last manifest line had to be written by copying a whole new list over the file (`handback-E1.md`). The E1 dispatch and the D3 re-check wrote no entry (`defects.jsonl` line 125).

5.6 **Small fixes, each from a recorded failure:**
- `probe.py` reading markdown answers (283 of 300 unread, `audit-E1.md`, section 1, part 5);
- `mem.py theme` with a blind mode (`handback-B1.md`);
- a guard that names the rule it applies (`handback-A1.md`, instrument item 8);
- a reconstruction that scores the skeleton against both the coder's account and the room model, and reports both (`handling-E2.md`, 1.4).

## 6. What to fix in advance, and what to leave to judgment

**The principle.** Fix what decides whether a claim passes. Leave to judgment what the claim is.

The run shows why both halves matter. A threshold fixed after seeing the data can carry the result. At D6, 70 to 72 of the forms' 72 changed cells keep their lean at a ratio of 1.0 to 1.2, 27 at a ratio of 1.5, and 20 at 1.5 with a floor of 15 per cent (D6.D6b, turn 51, answer 4). Rules declared before their scripts ran are what let the audit rerun the figures (`audit-E1.md`, section 1). On the other side, when a sentence-level standard was applied to the model's own statements, it demoted the room, the unit of the study (C5.C5d, turn 6, answer 3). And J had to say twice that the induction was mine: QD3-002, and "the criterion is a guide, not the judge" (QC2-002).

**Fixed in advance, in the stage files, by the instrument's author and J:**
- the hold-out, its seed and its strata (2.1);
- the composition tests: `prior.md` section 3's measures, computed by tools, with their denominators (2.2);
- the return vocabulary and its gold items (2.4);
- the amendment schedule and what a held proposal is (2.5);
- the forming method, the count criterion and the placement rule (3.2);
- the rules for choosing rooms to tell (3.2);
- every threshold that decides a claim, with a required sensitivity table at two other values;
- the audit's scripts and sample (3.3);
- the dispatch protocol (5.1).

**Left to judgment, and recorded with reasons:**
- the categories at tiers three and four, their cuts and their names;
- the model's elements and arrows, and their mechanisms;
- each ruling on a return line;
- which rooms to read deeply for the stories;
- the interpretation of what the rooms did;
- when to ask J.

*The risk.* A design that fixes too much becomes the straitjacket the proposal warns of (line 15, after Gioia and colleagues). A design that fixes too little lets a threshold carry the result. The line I draw is the one this run drew where it worked: rules fixed before the scripts that test, judgment in the categories they test.

## 7. Where the proposal itself should change

- **Line 17, "705 of which show evidence of coordination".** Under the run's coordinating-turn rule, 696 rooms hold a coordinating turn and 9 do not (`notes-A1.md` line 678). Either define the evidence differently or say 696.
- **Lines 19 to 21 and 25, the division of learning.** The proposal says people judge theoretical significance and decide which accounts enter the model. In this run an LLM analyst made those judgments line by line, and J ruled at named points (1.4). Either build the five gates (section 4) or describe the run as it was: an LLM aggregator whose judgments people ruled on at key points and did not audit by sample.
- **Line 23, the PlaceNL example.** It is accurate as far as it goes: accepted P05 lines in 68 rooms carry the mechanism (`notes-D3.md` line 1755, where the history line says 67). But the revised clause was then found to fail in nine rooms. In six, the keepers read the change from its shape; in three, informed members hold it (F-024). The bound is a held proposal outside the frozen model. Told with its bound, the example shows composition working in both directions: a revision from recurring exceptions, then a limit from the rooms where it fails. That is a stronger example than the revision alone.
- **Line 25, the checkpoint interview.** The agent answers from its saved context and its files. After compaction, the context is a summary, not the moment of decision (1.5). The proposal should say that answers are reconstructions checked against the record, and that this is what makes them testable.
- **Line 27, "an estimate of inter-model reliability".** The instrument bars calling its fleet figures reliability (FLEET.md section 2, restated in `audit-E1.md`, section 1, part 3). "Inter-model agreement" says what two coders' overlap measures.
- **Line 27, "human audits can test selected cross-case inferences".** This run had none. Either the next instrument builds the audit (3.3), or the sentence should read as a plan.
- **Line 27, the term-frequency comparison.** This run's comparison built without the ledger sorted the rooms largely by how much the coders coded (silhouette 0.024, `handback-D4.md`). The plan should name a null that holds record size, as the design note asks (lines 192 and 193).
- **Lines 9 and 31, later models judged by what they add.** That needs a scoring protocol fixed before the next model is built, and rooms the current model never saw. The hold-out (2.1) gives both.
- **Line 29, the cost.** The composition run, from A1 to E2a, took 317 legs over 22 days, 6 to 28 October (`RUN.json`), and 154.5 million output tokens to E1d (`audit-E1/experience_facts.json`). D3 alone wrote more than a third. The cost line should be computed from `RUN.json`, and the hold-out and the second ruler added to it.

## 8. The one thing not to change

**The return to every room, line by line, each line ruled with a reason and cited to the room's own concepts.**
- *Why it stays.*
  - It is the one part of this instrument that every other part rests on. The model's revisions came from it, the branches and the forms were cut from it, and the reconstruction's skeleton was built from it.
  - The audit could rerun almost every figure because of it, and 3,218 of 3,230 cited quotes resolve to their concepts (`audit-E1.md`, sections 6 and 7).
  - The proposal's own example, the keepers who repair a planned change away, exists because 68 rooms' lines carried the same mechanism.
  - The proposal's promise of accumulation needs exactly this: room-level lines a later model can be scored against, and a ledger that says why each line stood.
- *What it costs.* D3 was more than a third of the run's output (3.5).
- *Why that cost is still the one to pay.* Every change above (the hold-out, the local-adequacy tool, the second ruler, the vocabulary, the gates) is a change to how this ledger is tested or read. None of them works without it.
