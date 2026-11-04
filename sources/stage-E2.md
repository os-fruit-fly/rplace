# Stage E2. Formalizing: feedback.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** two, one per step, each closed at its end or earlier
when you choose. **Fleet:** none.

**Steps:** `E2a` the handling; `E2b` the next instrument, the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each section of `handling-E2.md`, and after each part of the next
instrument. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick
up, your working hypothesis and the next item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh E2 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, the last five diary entries, `validate.py --open E2`.
First leg only: `experience-E1.md`, `handback-E1.md`, `handling/proposal.md`,
`handling/design-note.md`.

**Reads allowed:** everything in `out/`, `_transcripts/`, `_probe/` and `_snap/`; `handling/`
whole: the interview transcripts in `handling/interviews/`, the harness log in
`handling/harness-log/` (with every first message the harness sent, in `first-messages/`); the
package and the store through the verbs; every document you were given. **Forbidden:** changing
any earlier file (rule 18); anything that is not the handling or the next instrument.

**Outputs:** `handling-E2.md`; `next-instrument-E2.md`; `notes-E2.md`; `handback-E2.md`; the
interview brief `out/interview/E2b.md`.

## Why this stage exists

E1 audited the run and your account of it. This stage audits the other side: what you were told,
by whom, and what it did to the work; and then it asks you, having done the whole thing, to
design the instrument that should have been. The next version of this instrument is written from
this file, E1's experience and the handbacks.

## 1. The handling (step E2a)

`handling/` arrives with this stage, placed by the handler: `proposal.md`, the study's proposal as it stands now, updated since you began;
`design-note.md`, why this instrument is built as it is; `interviews/`, the transcript of every
interview the principal investigator held with you, with `interviews.tsv`; and `harness-log/`,
the handover events, the pauses, the forced closes and every first message the harness sent.

Three parties spoke to you during the run: the principal investigator (in interviews, and in
reply files), the handler (the harness's messages, the answers to your questions, the pauses and
forced closes), and the instrument's author (the contract, the standing instructions, the stage
files, the tools' messages, and the design note you now read for the first time). Audit what
they said, not what you did; your own work was the subject of E1's experience. `handling-E2.md` has
four sections, each point cited to a file, a line, a transcript turn or a diary entry:

- **Where what you were told was inconsistent**: between two documents, between a document and
  a tool, between a stage file and the handler, between what the principal investigator said in
  an interview and what the instrument then asked. For each: what each side said, which you
  followed, and what following it cost.
- **What made the work harder**: an instruction you could not carry out as written, a ceiling or
  a count that fought the material, a tool that did not do what its help said, a cut in the
  wrong place, a reply that arrived too late, anything that sent you back.
- **What helped**: what you would keep, and why.
- **Freedom given and taken**: where you were free to judge as Gioia, Corley and Hamilton and
  Gioia, Anand and Hamilton ask of the researcher, and where that freedom was taken; whether
  taking it was right.

A point you cannot cite is stated as such, never dressed as a finding. Where the handling was
right and you were wrong, say so.

## 2. The next instrument (step E2b)

`next-instrument-E2.md`: read `handling/proposal.md` whole first. Then theorize the instrument
you would build to deliver that proposal next time, from what this run taught you: what the
proposal claims and what this instrument could and could not deliver of it; the stages you would
keep, cut, merge or add, and where the stops and the interviews should fall; the division of
labour between you, the fleets, the handler and the principal investigator; the tools you would
want; what should be fixed in advance and what should be left to judgement; and the one thing
not to change. It is a design argument, not a wish list: give each change the evidence from this
run that motivates it, and the risk it brings. Where the proposal itself should change in the
light of the run, say so.


## Moments to log

Each section of the handling finished; the proposal read; each part of the next instrument
drafted; the one thing not to change named.

## Final message

Three sentences: the inconsistency in the handling that cost most; the first change you would
make to the instrument; the one thing not to change.

## Close

`done.sh E2` at the end of `E2a`; at the end of `E2b`, `handback-E2.md`, the head, the closing
diary line, then the interview.

**Interview point.** `E2b` writes `out/interview/E2b.md` (under 800 words: what you did, what you
found, what surprised you, what you doubt, and the three questions you would most like to be
asked) and closes with `done.sh E2 --cut interview`: the whole run, how you were handled, and the
instrument you would build next. The principal investigator may talk with you here, in a
fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief
under the leg, the stage, the step and the minute, and refuses the cut without the brief and the
handback.
