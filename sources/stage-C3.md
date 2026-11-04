# Stage C3. The model against the literature.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one per shelf pass (contradicting work; resembling work, with the
concept; the four problems), closed at the pass's end or earlier when you choose; every recut
the literature forces is logged and snapped when it is made (§6). **Fleet:** none.

**Steps:** `C3a` the contradicting shelf; `C3b` the resembling shelf; `C3c` the four problems (§1's claim put to the structure), the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each logged recut, and after each shelf pass. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh C3 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, the last five diary entries, `validate.py --open C3`.
First leg: the explanation shelf arrives, its read tier shipped with this stage and its
on-request tier listed one line each (`mem.py shelf --list`, `mem.py shelf <name>`); `prior.md`,
read before anything else; `concept.md`; `notes-A1.md`, opened only at §7.

**Reads allowed:** every shelf that has arrived (nothing served once is taken away); `model/`,
`model.md`, `structure.md`, `dimensions.jsonl`, `fourth/fourth.jsonl`, `concept.md`,
`findings.jsonl`, `prior.md`; the store through `mem.py` (`where`, `codes --third`, `after`);
rooms by query for a check, and rooms whole through the verbs for an abductive read (§1);
quotes through `cite.py`. **Forbidden:** rewriting the story (that
is C5); opening `field/`, which arrives at stage C4; renaming a third-order theme after a construct (contract §1); a change from a read of the
corpus that is not flagged `abductive` with the paper that prompted it (§1); the canvas as an undeclared ground (rule 7).

**Outputs:** `literature-C3.md`; `findings.jsonl` lines with literature ids; `mapping-C3.jsonl`;
mechanisms rewritten in `model/arrows.jsonl`, each a `model/history.jsonl` line; wherever this
stage changes something, `model-C3.md`, `structure-C3.md` and `concept-C3.md`, each a whole
file superseding the stage C2 file (rule 18; a file holding only what changed is read
downstream as the whole thing), and `manifest-C3.txt`, one line per stage C2 file saying
whether it has a stage C3 successor, which stage C5 reads first; a recut is not a superseding
file: the tier file is amended and the superseded line goes to `tier_history.jsonl`, as stage
C2 says; when the third-order tier is recut, `scheme_v2.jsonl` and `assignments_final.jsonl` rewritten
(`mem.py mint`, then `mem.py reassign`, as stage C2 says); `notes-C3.md`.

## 1. The sequence, and the log point

**Nothing is read against the explanation literature before this stage** (contract §4). Within
it, **read `prior.md` first**, and restate in `notes-C3.md` what you expected; read after a
conclusion has formed, it can no longer tell a finding from a prior. Then, before you open the
shelf, re-read `METHOD.md`'s first section and every shelf already held (`mem.py shelf`): the
v35 analyst had forgotten the method shelf by the time the next arrived, and an explanation
read on a forgotten foundation is a relabelling waiting to happen.

**Record where the read logs stand before you open the shelf**: the line counts of
`_cite_reads-C3.jsonl` and `_mem_reads-C3.jsonl`, in `notes-C3.md` and logged. Count them
yourself; `cite.py`'s sequence counter resets when the tool is constructed. From there on, **a read of the rooms prompted by a paper is an abductive read, and it may add
or change a theme or an arrow**, as Gioia, Corley and Hamilton cycle between the data and the
literature. Log it before you read (`mem.py log --kind abductive`, the paper and what it made you
look for). A change it makes carries `"abductive": true` and `"prompted_by": "<author year>"` on
its `model/history.jsonl` or `tier_history.jsonl` line, and is listed in `literature-C3.md`, so
a reader can tell what the rooms showed unprompted from what a paper made you find. A read to
check a quote or a count is not abductive and carries no flag. The log records what was served
and not why, so it cannot tell a check from an abductive read you did not log; say so in
`literature-C3.md`.

**If a work changes what a claim rests on, write a switch record** (Günther, Joshi and
Constantinides 2026, p. 872; contract §1, two kinds of claim), one paragraph in
`literature-C3.md` per switch: the work and the cue that triggered it; what moved (a claim that
rested on the rooms' words now rests on a pattern across rooms, or the reverse; a name that was
the participants' now the literature's); which earlier work is redone or rechecked, with the leg
that does it; what differs in the output; why the state after the switch serves the claim
better; and the `findings.jsonl` line that supersedes the earlier one (rule 14). A reading that
leaves every claim resting where it rested is not a switch and gets no record; this stage's
planned reading is the design, never a switch.

**Say in `notes-C3.md`, first**, that the literature is read after the model and not through
it; it is the design, not a departure, and no `departures.jsonl` line is written for it. Then
say whether the substitution worked: whether knowing the contract's §1 frame and not building
with it was a distinction you could hold while writing the scheme and adjudicating its
placements.

## 2. How to cite

Mark every claim about the literature one of two ways: **`verified`**, you opened it on the
shelf in this session and can quote it; **`recalled`**, you are working from what you know, with
author, year and the claim you are attributing, so a reader can check it. A work on the
on-request tier is `recalled` until served. **Do not invent a reference, a title, a year or a
quotation, and do not attach a real author to a claim you are not sure they made.** Where you
are unsure, write *I believe this literature holds X but cannot verify it here* and carry on.

## 3. Leg 1: work that contradicts the model

Work that reports the opposite of what you found, or that explains your phenomenon with
something you did not use. For each: the two claims, one sentence each; what in the record
decides between them, with a room and a quote through `cite.py` or a transition; and which of
three things is true: the accounts
disagree about the world, they disagree about the setting, or they are about different things
and one of you has the wrong name for it. Say which. Then whether the disagreement bounds your
claim (a condition, rule 16, written into the finding) or the work's (a scope this material
falls outside). A contradiction you cannot decide from the record is reported as open, with
what would decide it.

## 4. Leg 2: work that resembles the model

### 4a. Distant fields, and the mechanisms

**This is the pass that supplies mechanisms.** Take your model's arrows, particularly the ones
whose `mechanism` you found hardest to write, and ask what other literature describes the same
move, going deliberately outside organization studies. For each match: what the distant work
holds the mechanism to be, and whether it fits here. For each resembling work: what it names that
you named differently (the fourth-order theme or dimension, its declaration updated under §6);
what it explains that yours does not, and the reverse.

**Where it fits, rewrite that arrow's `mechanism` in `model/arrows.jsonl` and in `model-C3.md`,
keep the stage C2 sentence beside it as `mechanism_C2`, mark the arrow `mechanism_source:
from-literature` with the work named, and write the `model/history.jsonl` line.** Stage C5
takes each mechanism from the arrow that grounds it; one left only in `literature-C3.md` is
invisible downstream. Re-read `mechanism_fails_if` against the new sentence; a mechanism no
observation here could show failing makes the arrow theorised, listed apart.

Where the distant work predicts something here you have not looked for, that is an abductive
read (§1), logged before you read. Test it, record the result either way, and say whether it
qualified, bounded, added or changed an arrow or a theme. If you decline the read, say why.

### 4b. The concept

Stage C2 named a concept and guessed at its nearest existing referent from recollection. Test
the guess against the shelf, the difference stated so a reader could test it. Three outcomes:

- **It survives.** The literature has no adequate referent. Say what the nearest three are and
  how each falls short.
- **It is a relabelling.** Adopt the existing name, rename the concept as borrowed, and say what
  your material adds, usually a setting, a boundary, or a mechanism the original did not have;
  the finding says so.
- **It is a relabelling and adds nothing.** Then the study produced a description and the model
  stands without a named concept at its centre. Write that; stage C5's propositions do not
  depend on a concept surviving.

If this pass changes the concept, write `concept-C3.md` whole and leave `concept.md` standing.

## 5. Leg 3: the four problems, put to the structure

The contract's §1 claim is that every group with a goal must solve four problems, task
division, task allocation, reward provision and information provision, whether or not anyone
says so. The definition assumes a goal; establish from evidence whether each group inherited,
negotiated, contested or changed its goal (Felin and Zenger 2016 and 2017 put
that gap, the chosen problem, at the centre of strategy). Put the claim to your structure and model as they stand; **do not revise them to accommodate
it**, and be specific enough to be wrong.

**The one written operation** (contract §1): for every fourth-order theme, which of the four
problems it is a way of handling, or none, one line in `mapping-C3.jsonl` with a clause of why;
the mapped set is the match, the unmapped set the remainder, and each mapped problem carries
the sentence saying what this material's version of it cannot do. A fourth-order theme that
already carries one of the four's names under its declaration answers this pass by
construction; say so first, and what the pass asks of it is that sentence, and whether the
frame's version would have cut the theme where you did. Treat the remainder as a candidate extension. Test whether it is a different mechanism,
a renamed instance, a change of level or an evidence gap. An empty remainder is allowed.

```json
{"fourth": "T4-003", "problem": "division|allocation|reward|information|none",
 "why": "...", "cannot_do": "..."}
```

Two limits. Your evidence is talk and the claim is about arrangements: a group can allocate
work perfectly and never write a word about it, and the contract's §5 holds you to organizing
*done in public*. And there is no denominator: you have the share of coded records that maps
onto each problem, confounded as §5 describes, not the share of groups that solved it.

Answer in seven parts, in `literature-C3.md`:

1. **What you expected**, quoted from `prior.md` rather than remembered: which of those things
   you found, whether any turned up only where the material was thin, and what `prior.md` holds
   that your structure has no room for.
2. **What in your structure speaks to the claim**, fourth-order theme by fourth-order theme from
   the mapping, with counts and rule 5's gate, and for each whether the material put it there or
   you did.
3. **What your structure carries that the claim has no place for**, the remainder, if any. Explain why it extends the framework. Be specific, and quote through `cite.py`.
4. **Which of the four your structure reaches richly, which thinly, and which not at all**, and
   for each thin or absent one whether the limit is in the material, in the coders' selection,
   or in your own pruning. Where one comes back nearly empty, take a side: did these rooms not
   solve that problem, or can your instrument not see it? Say which you think and why. Stage
   E1's account of what the study cannot say inherits this paragraph directly.
5. **The goal.** Where in the structure and the model the making of a goal sits, its contest and
   its change, and what its setting did to the four problems; a finding, never a premise, and
   if the structure has no place for it, say so as a finding about the structure.
6. **Whether your material supports the claim, contradicts it, or is silent**, with §5's
   warning on every count: a claim about what is *absent* here is a claim about small rooms
   writing in public, and every absence claim is marked weak.
7. **Whether the claim is answerable with this material at all.** *The structure does not speak
   to this* is a complete answer.

## 6. Keep the construct declarations current

Where the shelf shows a construct is borrowed or adapted rather than coined, or mistaken for a
construct you had not named, amend its `construct` block (stage C2 §2) and log the event, with
the sentence saying what this material's version cannot do wherever the name is borrowed; the
third-order themes stay descriptive and do not change here (contract §1). Record what changed
in `structure-C3.md`.

**You may recut fourth-order themes and dimensions here, and the third-order tier too, under
rule 11** (a third-order recut is written as stage C2 says: `scheme_v2.jsonl` and `mem.py reassign`), and stage C2's rule on the dimension tier holds through every recut: no number is
set, a fourth-order theme may gather under no dimension, the dimensions hold apart pairwise, and
collapsing to one is examined with its candidates and runner-up, never an automatic failure or an
answer; a recut that empties the tier is reported the same way. Every `findings.jsonl` line a
recut touches is re-examined in the same act (rule 14). A literature that shows a fourth-order
theme holding two things the field keeps apart means the cut was wrong. Amend the rule first,
append the event to `tier_history.jsonl` with its move and one clause of reason, amend the tier
file, re-place what the amendment touches yourself under the amended rule, redraw whatever
depended on it, and log the move (`mem.py log --kind move`) and snap it (`python3 tools/snap.py
C3 move-<move>-<n>`) as you make it.

**What changes, and what does not.** A finding changed by a recut says in `findings.jsonl` what
changed it (rule 13). Nothing in the model is withdrawn because a work says otherwise; it is
bounded, or the disagreement is printed beside it.

## 7. Stage A1's three sentences

Read them now, from `notes-A1.md`, for the first time since. Say in `notes-C3.md` which of this
stage's conclusions you would have reached anyway and which the material forced.

## Moments to log

The log point; each work read and what it did to which claim, `verified` or `recalled`; the
abductive read, with its paper and what it changed or did not, or its refusal; each switch
record, or that none was needed; each mapping line; each declaration amended; each recut by
move; the three sentences read.

## Final message

The claim (what the literature changed about the model), the room that best supports the
model's side, the room that most threatens it, and the condition that separates them. Then:
works contradicting and how each resolved; works resembling; the one distant field that supplied
a mechanism; findings bounded and changed; declarations updated and names changed; whether the
concept survived; how much of `prior.md` came true; fourth-order themes mapped to each problem
and the size of the remainder; files with a stage C3 successor; citations `verified` and
`recalled`; the log point at which this stage began; the licences exercised and not
(METHOD.md).

## Close

`done.sh C3` at the end of every pass, or earlier when you choose, every recut logged and
snapped as it was made; paste the close-check report into
`notes-C3.md`; `handback-C3.md`; the head; the closing diary line.

**Interview point.** `C3c` writes `out/interview/C3c.md` (under 800 words: what you did, what you found, what surprised you, what you doubt, and the three questions you would most like to be asked) and closes with `done.sh C3 --cut interview`: the model read against the literature: what it borrowed, what it contradicts, what no paper has. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief under the leg, the stage, the step and the minute, and refuses the cut without the brief (and, at a stage's end, without the handback).
