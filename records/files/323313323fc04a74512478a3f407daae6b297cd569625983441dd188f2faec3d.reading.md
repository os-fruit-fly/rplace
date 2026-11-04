# Handback, stage E2: the handling and the next instrument

Written at E2b, 28 October 2026.

## The final message

The inconsistency in the handling that cost most was over where P05's bound was to be written:
- J planned at the D3c interview that D4 would write it;
- the contract's rule 11 and the D4 close-check allow model changes only at D3, and J ruled the same day against any further re-check;
- the amendments made at D4 were reverted.

So the frozen model keeps a clause that fails in nine rooms and an arrow that cannot fail, both held outside it.

The first change I would make is to seal about a tenth of the rooms before the analyst reads any of them and return the frozen model to them last. That makes composition below the population testable out of sample at every tier the analyst built.

The one thing not to change is the return to every room, line by line, each line ruled with a reason and cited to the room's own concepts.

## What the stage delivers

- **`handling-E2.md`** (E2a). Four sections, every point cited:
  - 12 inconsistencies, each with what each side said, what I followed and what it cost;
  - 10 things that made the work harder;
  - 7 that helped;
  - freedom given and taken, with eight places where the handling was right and I was wrong.
- **`next-instrument-E2.md`** (E2b). Eight parts:
  1. what the proposal claims and what this instrument delivered;
  2. five changes that make the test of composition decidable;
  3. the stages, stops and interviews;
  4. the division of labour, with five gates for J;
  5. the tools;
  6. what to fix in advance and what to leave to judgment;
  7. where the proposal should change;
  8. the one thing not to change.
- **`notes-E2.md`**, with sections E2a and E2b.
- **The interview brief**, `out/interview/E2b.md`.
- **Two read scripts** in `out/_analysis/`, with their outputs: `e2_interviews.py` (the interviews from their opening turns) and `e2_first_messages.py` (the harness's additions to the standard leg message).

## The main findings, in brief

**The handling.**
- **Where it worked:** short rulings that settled a method; interviews that found faults I had not looked for; a handler who named its own errors.
- **Where it cost:**
  - a plan for a later stage that the contract and the checks forbade;
  - a return specification that one document froze, a stage file left to me, and a tool contradicted;
  - answers announced as the PI's when the handler had written them;
  - interview findings that could not reach the run.
- **Where the handling was right and I was wrong:** A1's reading route, the unit at C5, the forms' placement and count, the tellings' rooms, the E1 specification and the E1 route.

**The next instrument.**
- This instrument delivered a traceable census model and a population-level composition.
- It did not deliver a decidable test below the population, the proposal's division of learning, or a human audit.
- The design answers each:
  - a hold-out returned to last;
  - local adequacy computed by a tool;
  - a second ruler built in;
  - a vocabulary that can say an arrow fails;
  - amendments on a schedule;
  - five gates where J decides;
  - an audit stage.

**The proposal.** Eight lines should change. The largest is the division of learning (lines 19 to 21 and 25): the run's significance judgments were the analyst's, so either the next instrument builds the gates or the paper describes the run as it was. The PlaceNL example is stronger told with its bound.

## What I did not do as the stage file says

- **Gioia, Anand and Hamilton.** Section 1 asks me to judge freedom by their account. No text of it is in the folder or on the shelf I read, so I did not cite it, and said so in `handling-E2.md`.
- **Messages sent during legs.** `CONTROL/` is read-denied, so the handling of mid-leg messages rests on my own transcripts and diary. Talk with J outside the interview transcripts is not on file.
- **Costs in money.** The next instrument does not price its changes. `RUN.json` gives tokens and legs, not money, for the analyst's sessions.

## What is wrong with the instrument, or unclear

- **The design note is v38 (2026-09-22); the run's tooling is v43.** The note numbers the stages 01 to 18, and the run names them A1 to E2. I read it as the design's intent. Where the note and the run's files disagree, `handling-E2.md` says which I followed. The handling folder's README allows the note to be replaced "if the design changed", and it was not.
- **The E2 close-check checks only the shape:** four headings, one citation, and the word "proposal". A handling audit with one cited point would pass. That is by design, and stated in the check's docstring.
- **The interview transcripts carry each forked leg's whole conversation first.** The interview proper is the last two to four turns. A tool that served the interview alone would save the next reader a script.

## Slips at E2b

- **None in a figure written to a file.** Every count in the next-instrument file was checked by script or against its source before it was written:
  - the 9 rooms with no coordinating turn;
  - the 317 legs and 22 days;
  - the design note's line numbers;
  - the D6 threshold table;
  - PlaceNL in the analysed set.
- **One contraction in the next-instrument file sits inside a quotation of my own interview words.** It stays as quoted.

## Licences exercised at E2b

- I treated the proposal's division of learning as an aim the instrument failed to build, not as a claim the run refutes.
- I chose one first change (the hold-out) over the others, since it is the only change that makes a test out of sample at the analyst's tiers.
- I priced no change in money, and named the cost in legs and tokens from the record.

## For the next version

Write it from `next-instrument-E2.md`, `handling-E2.md`, `experience-E1.md` and the handbacks. Its section 2 holds the changes to the test, its section 4 the gates, and its section 5 the tools. Each names the failure on record that motivates it, so the author can check every change against the evidence before adopting it.
