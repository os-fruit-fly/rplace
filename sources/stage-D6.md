# Stage D6. The retelling: the model with its forms inside it.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one per aggregate dimension (or per group of
fourth-order themes, if you judge that a better unit), then one for the whole telling and the
figure; each leg closes at its end or earlier when you choose. **Fleet:** none.

**Steps:** `D6a-01`, `D6a-02` ... one per aggregate dimension (or group of fourth-order themes); `D6b` the telling and the figure, the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each dimension's section is written and logged; after the figure; after
each amendment is logged and snapped. At a safe stop, check for `.pause` (`ls .pause`); if it is
there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh D6 --pause`.

**Startup packet:** `_head.md`, this file, the last five diary entries, `validate.py --open D6`.
First leg only: `account.md` (stage C5), `branches.jsonl`, `crosslinks.jsonl`, `tree-D4.md`,
every `forms/<id>-account.md` from stage D5, and `notes-D5.md` (the lumps, renamings and
subforms stage D5 left for you to act on or decline, each answered in `notes-D6.md`).

**Reads allowed:** everything you have written; the model (`model/elements.jsonl`,
`model/arrows.jsonl`, `MODEL-D1.md`); the ledger and the verdicts; the rooms and their concepts
through the verbs (`mem.py room`, `forest`, `case`, `compare`, `cite.py`); the canvas, declared
where it shapes a sentence (rule 7). Nothing is forbidden to you here.

**Outputs:** `retelling-D6.md`; `fractal-D6.jsonl`; `figure-D6.md` (the figure as text: a
mermaid or dot source you can render, with a legend); empty `amendments-D6.jsonl`; `proposals-D6.jsonl` (empty if none);
`notes-D6.md`; `handback-D6.md`; the interview brief, `out/interview/D6b.md`.

## Why this stage exists

Stage C5 told the global model. Stages D1 to D4 returned it to every room and cut the forms
organizing took from what the rooms did to it. Stage D5 wrote one account per branch. None of
them tells the model again with the forms inside it, and that telling is the answer to the
theory question: what forms organizing takes, how they differ in their functioning, and which of
them keep the work alive. Write it now, from the top down, so that a reader can walk from an
aggregate dimension to a form to a room and back, and at every step see the level below
specify the one above without contradicting it (fractal specification, contract §2).

## 1. Dimension by dimension

For each aggregate dimension, in the order you choose: what it is in the global model, in one
paragraph; then, for each fourth-order theme under it, what each branch does to it. A branch
**specifies** the element (adds detail that holds in its rooms), **restricts** it (it holds only
under a condition the branch names), **replaces** it (the branch does the work another way), or
**leaves it untouched**. Write one line per element and branch in `fractal-D6.jsonl`:

```json
{"element": "P07", "branch": "F03", "relation": "specifies|restricts|replaces|untouched",
 "how": "one sentence", "evidence": {"codes": ["denmark:c0117"], "rooms": ["denmark", "sweden"]},
 "canvas": false}
```

Name two or three rooms per branch that show it best, and one that shows it least well. Where a
branch's rooms disagree at this element, describe the evidence and alternatives. It may be local variation, unresolved evidence, or a candidate subform or crosslink. Any new structural claim goes in `proposals-D6.jsonl` as unvalidated.

## 2. The telling

`retelling-D6.md` tells the whole model again, with the forms inside it, in the model's terms.
It says which forms kept the work alive to the freeze and after it, from the record
(`organizing_end_hour`, the aftermath share and `work_remained` read beside each form, silence
counted; the canvas only as the outcome, the use declared), which did not, and what in the
model separates them. It says what the unadapted group is, and what the rooms the model could
not compose have in common, if anything. It names every branch by its id at least once.

## 3. The figure

`figure-D6.md`: the stage C5 figure with the forms drawn inside it, at the level where they
differ. As many elements and forms as the telling needs; no fixed count.

## 4. New substantive proposals

The D3 model and D4 tree remain unchanged here. A new explanatory insight is a proposal, not an applied amendment. Write `proposals-D6.jsonl` with `id`, `what`, `change`, `why`, `evidence`, `affected_rooms`, `base_model_version` and `status: unvalidated`. Keep these proposals separate from the validated retelling and figure. `amendments-D6.jsonl` remains empty. A proposal can enter a later model only through a supported affected-case return to the original leads and a new validation cycle; the current run never inherits D3 validation for it. E1 reports the proposals and their unvalidated status.

## Moments to log

Each dimension finished; each unvalidated proposal; the figure drawn; the telling finished.

## Final message

Three sentences: the answer to the theory question as this run found it; the form you are most
and least sure of; what the retelling changed in the model, or that it changed nothing.

## Close

`done.sh D6` at the end of each leg; paste the close-check report into `notes-D6.md`;
`handback-D6.md`; the head; the closing diary line.

**Interview point.** `D6b` writes `out/interview/D6b.md` (under
800 words: what you did, what you found, what surprised you, what you doubt, and the three
questions you would most like to be asked) and closes with `done.sh D6 --cut interview`: the model re-told with its forms inside it, the answer to the theory
question. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run);
the run goes on from the cut either way.
