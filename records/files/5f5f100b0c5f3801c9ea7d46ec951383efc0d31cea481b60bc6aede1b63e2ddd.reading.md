# Notes, stage E2

## E2a: the handling

**The close-check report of E1e** (`_closes/` for E1e): 0 errors, 0 warnings. `validate.py --open E2` at this leg's start: 0 errors, 0 warnings, the five declared inputs present.

**What I read.**
- The first-leg reads, whole: `handling/proposal.md` (127 lines) and `handling/design-note.md` (349 lines, v38, 2026-09-22, with J's decisions of 24 September). `experience-E1.md` and `handback-E1.md` are mine, written at E1e.
- The nine interviews, through `out/_analysis/e2_interviews.py`. It prints each transcript's dialogue from the turn that opens "This is an interview", because each transcript first holds the forked leg's whole conversation. The output is `out/_analysis/e2_interviews.txt` (106,192 bytes). The first run, which printed the whole transcripts, is kept as `e2_interviews.superseded-1.txt`. The interviews hold J's opening questions and my answers, two to four turns each.
- The harness log: the handover events, the three pause files, and the 314 first messages through `out/_analysis/e2_first_messages.py` (`e2_first_messages.txt`): 56 messages carry an addition and 258 none; 37 additions announce answered questions. The dispatch outcomes by stage were counted by a one-line script.
- The answer files, the contract, METHOD.md, the stage files, the tools and the checks, by line, as each point needed them.

**What this leg wrote.** `handling-E2.md`, in four sections, each point cited:
1. **Inconsistent**, 12 points. The costliest was where P05's bound was to be written: J's plan at D3c against rule 11, the D4 check and J's own ruling against a further re-check. It ended in moves 198, 199 and 203 and two held proposals.
2. **Harder**, 10 points. Among them: dispatches without a dry run; tools against their help; checks that refused rulings; the guard; a local status that separates no room; a vocabulary that barred replacement; interview findings that could not reach the run.
3. **Helped**, 7 points. Among them: one-sentence rulings; the interviews as checks; a handler who named its own faults; the record and the memory tools; the first message naming answers; the PI's E1d decision.
4. **Freedom**, given, taken and judged, with eight places where the handling was right and I was wrong.

**What I could not read or cite.**
- `CONTROL/` is read-denied, so the messages sent during legs are known only from my transcripts and diary.
- Talk with J outside the interview transcripts is not on file.
- No text of Gioia, Anand and Hamilton is in the folder or on the shelf I read, so I did not cite it.

**Licences exercised at E2a.**
- I read the design note as the design's intent, since it predates the run's tooling (v38 against v43) and numbers the stages differently.
- I read each interview from its opening turn, not the forked leg's conversation before it.
- I judged each taking of freedom as right, mostly right, partly right, or defensible but costly, and said why.

**Slips at E2a.**
- **Five figures or claims in the draft went past the record**, and each was corrected before its section was logged, one Edit per turn:
  - the history lines of 1.1 (ten, not two);
  - the design note's line numbers in 1.4;
  - the dispatch pattern in 2.1, which first said every stage that ran a dry run succeeded, though B2 ran three and failed;
  - the count of first messages announcing answers (37, not 34);
  - my paraphrase of stage E1's Gioia sentence, replaced by its words.
- **One correction of substance.** In 1.8, the transcript showed that the PI's "direct" has a reading the harness log bears out, so the misreading was mine as much as the message's.
- **One command was refused** with no rule named. It held a `grep` pattern of equals signs, which I take to be the cause, and it ran once the pattern was changed.

## E2b: the next instrument, the handback and the interview

**The close-check report of E2a** (`_closes/` for E2a): 0 errors, 1 warning (`next-instrument-E2.md` not yet written). `validate.py --open E2` at this leg's start: 0 errors, 0 warnings.

**What this leg did.**
- It read `handling/proposal.md` whole first, as section 2 asks.
- It wrote `next-instrument-E2.md` in eight parts, each logged when drafted:
  1. the proposal's claims against what this instrument delivered;
  2. five changes that make the test of composition decidable;
  3. the stages, stops and interviews;
  4. the division of labour;
  5. the tools;
  6. what to fix in advance and what to leave to judgment;
  7. where the proposal should change;
  8. the one thing not to change.
- It wrote `handback-E2.md` and the interview brief `out/interview/E2b.md` (681 words).

**What it found.**
- **What was and was not delivered.** The instrument delivered a traceable census model and a population-level composition. It did not deliver a decidable test below the population, the proposal's division of learning, or a human audit.
- **The first change:** a hold-out of about a tenth of the rooms, sealed before A1 and returned to last. It answers J's reason for no holdout: the B3 fleet already places second-order themes into the frozen scheme.
- **The one thing not to change:** the return to every room, line by line, each line ruled with a reason and cited to the room's concepts.
- **The proposal.** Eight places should change. The largest is the division of learning. The PlaceNL example is accurate at 68 rooms and stronger told with its bound.

**Checked before writing:**
- 9 rooms without a coordinating turn (`notes-A1.md` line 678);
- 317 legs over 22 days (`RUN.json`);
- PlaceNL in the analysed set;
- the design note's line numbers (192 and 193, 235 to 244, 283, 298 to 303, 310);
- the D6 threshold table (D6.D6b, turn 51).

**Licences exercised at E2b.**
- I read the proposal's division of learning as an aim the instrument did not build, not as a claim the run refutes.
- I chose the hold-out as the first change because it alone tests the analyst's tiers out of sample.
- I priced no change in money.

**Slips at E2b.** None in a figure written to a file. One contraction in the next-instrument file is inside a quotation of my own interview words, and stays.
