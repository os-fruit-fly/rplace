# Stage D5. The branch accounts, at every level.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one per branch, then one for the waterfall and survival. **Fleet:**
none.

**Steps:** `D5a-01`, `D5a-02` ... one per branch; `D5b` the waterfall and survival. Each leg is named by its step (STANDING §2).

**Safe stops:** after each branch's account. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh D5 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, the last five diary entries, `validate.py --open D5`;
the branch's `forms/<id>.md`; the hierarchy shelf. First leg only: `branches.jsonl`,
`crosslinks.jsonl`, `tree-D4.md`, `chunk-share-D4.md`.

**Reads allowed:** the branch's members by query (`rooms/<sub>/model-D.md`, `case.md`, concepts
through `cite.py`, `mem.py note`, `adaptations --element`, `contrast`); `verdicts-D.jsonl` and
`exception-report-D.md`; `account.md`; `model/arrows.jsonl`;
`propositions.jsonl`; `rebuild.py <sub>`; `_views/`; the `organizing_end_hour` and aftermath
share per room. **Forbidden:** rooms outside the branch except as the contrast the account
names; the canvas as an undeclared ground (rule 7), projected on afterwards; recutting a branch or changing
the model; the chunk-share tree as a ground.

**Outputs:** `forms/<id>-account.md` per branch; `branches-D5.jsonl`; `waterfall-D5.md`;
`survival-D5.md`; lines in `findings.jsonl` and `defects.jsonl`; `notes-D5.md`.

The branches are the forms organizing took under your own return; read their members as
rooms, in any order, through any file. Two things are fixed: a claim
about absence carries §1's arithmetic, and the branches were cut from adaptations your own model
provoked and cannot vouch for it. If stage D4 drew no tree, or the population is one form with
variation, write this stage anyway, about what the branches do track, and say in every account
that they are groupings. The unadapted group gets an account of its own; a branch mostly
`cannot-tell` is said to be so before it is described.

## 1. Before you call anything absent

Rule 6. Declare here, before any comparison, the minimum count of within-case datings an arrow
stands on, from your own `subs` counts. For every arrow you compare across branches, compute the
expectation: its corpus-wide `subs` count over the analysed set from `counts.py`, times the
branch's `n`; smallest and largest branch first. Below one the arrow is `not-testable-here`,
and no boundary condition and no `propositions_fail` may be written from it. Arrow presence
inside a branch is arithmetic about your own model, cut on the adaptations it provoked:
*present here, absent there* describes a form and never bounds a proposition, unless you can
say what distinguishes the difference from a restatement of the cut.

## 2. Per branch, the account

`forms/<id>-account.md`, in this order:

1. **How these rooms organized, as a narrative**: a few hundred words a stranger to the model
   could follow, with participants' words through `cite.py`, written before the comparisons.
2. **What the branch does**: the elements it shares with the global model unchanged, as the
   model's prose says them.
3. **What it does differently**: the shared keys read as prose, each with the rooms and the
   `how` sentences that carry it, and what a room of this branch does that the global model
   would not predict. Say what the branch's claim rests on (contract §1): the shared keys are a
   pattern across rooms and are validated as one, by the ledger's counts and D4's alternatives;
   what the rooms did with them is a claim on their words and is validated by `cite.py`. One
   kind of evidence does not stand in for the other. Then stage D4's name read against the members: the strongest argument
   that it names the keys rather than what the rooms did, and what a reader who suspected so
   would look for; a name you cannot defend from the members is a renaming proposal in
   `notes-D5.md`.
4. **The concepts it employs**: representative first-order concepts from the members, through
   `cite.py`, at least one per shared key.
5. **Composition here.** Keep three versioned judgments separate. `verdicts-D.jsonl` diagnoses the original unadapted global model and remains historical. `adaptation-returns.jsonl`, the current model hash and D3's unaffected-case reasons establish each adapted-local status. Name all unresolved or insufficient-evidence local accounts and their limits. Then state whether the shared branch explanation is supported, unsupported or unresolved and why. An original global failure is not a current local or shared failure.
6. **How the model runs here**: which elements do the work, which sit idle (`absent`), which
   fit badly, what these rooms do that it has no place for (`propose` and particular lines).
   Where the room models and your reading disagree, say which you believe.
7. **The one relationship that runs differently here**: one arrow, both sides quoted.
8. **Fourth-order themes over- and under-represented** against the population base rate (no
   v38 view yet; by script, logged), in the rooms' own words; never a property of
   the rooms (contract §5).
9. **Arrows present, absent or `not-testable-here`** with the expectation on each; propositions
   that hold, fail against a real expectation, or are not testable.
10. **How representative members do the work**: two or three rooms, by a rule you state, each
    told in a paragraph in the branch's terms with citations, one the member that fits worst,
    one read at length with why you chose it and what is unrepresentative about it.
11. **The nearest branch and what separates them**, with the room that could have gone either
    way; every cross-link touching this branch, named.
12. **The form test** (contract §1, Doty and Glick): the constructs the branch binds, the
    relations among them. Map them to the four organizing problems where justified, allowing an empty mapping and a supported theoretical remainder. Then, for
    what varies among members, whether the form accommodates it, a subform is warranted (a
    candidate for stage D4, written to `notes-D5.md`, never cut here), or it is a particular of
    one history. A branch for which you cannot write this is reported as a grouping, not a
    form.
13. **What would make you doubt this is a form at all.**

`branches-D5.jsonl`, one line per branch:

```json
{"branch": "F03", "name": "...", "n": 23,
 "verdicts": {"composes": 14, "composes-with-residue": 5, "does-not-compose": 2, "cannot-tell": 2},
 "global_model_version": "<original handoff VERSION>", "local_model_version": "<current hash>",
 "local_statuses": {"room": "validated|unresolved|insufficient-evidence"}, "unresolved_members": [...],
 "shared_status": "supported|unsupported|unresolved", "shared_warrant": "evidence and scope",
 "construct_bindings": ["P07", "T4-005"], "binding_account": "relations and conditions",
 "binds": [...], "leaves_free": [...], "over": ["T4-005"], "under": [...],
 "arrows_present": [{"arrow": "A03", "expected": 2.1}], "arrows_absent": [...], "arrows_not_testable": [...],
 "propositions_hold": ["N12"], "propositions_fail": [...], "propositions_not_testable": [...],
 "survival": {"median_organizing_end_hour": 0, "aftermath_share": 0.0,
              "work_remained": {"kept": 0, "lost": 0, "silent": 0}},
 "canvas": {"median_area_px": 0, "rooms_with_artwork": 0, "read": "one clause"},
 "unmodelled": "...", "form_or_grouping": "form", "confidence": "..."}
```

## 3. The waterfall

`waterfall-D5.md`: one reader's walk from the account, through one branch, through one
subform, to one room's model, to its adaptations, to the quotes; and the walk back up. Say at
each step what was added and whether it contradicted the level above (contract §1, the check in
both directions), and read the walk against `prior.md`'s expectation of what the lower levels
describe. Choose the branch and the room by a rule stated before the walk.

## 4. Survival, per branch

`survival-D5.md`: `organizing_end_hour`, the aftermath share and `work_remained` (how many
members' records say the work was kept, lost, or say nothing: silence counts, contract §1) per
branch, from the record and never from the canvas, with the branch's ending described in its own terms: what stopped
the coordinating, and what the rooms did after. The canvas fields are projected on afterwards
and read against this, with the direction of the bias named (rule 7): what the rooms of this
form left on the canvas, against the narrative in §2 and the account's paragraph on what the
model implies a room keeps. Where the §2 narrative dates a change in what the members did,
say which bracket of `prior.md` §4 it falls in and whether the members' placements by hour
(`canvas`) move at that hour: a timing the canvas corroborates is said to be, a mechanism never
is, and a timing it contradicts is named as a question for the account. The contract's §5 sentence on what the canvas measures stands
beside it; nothing here is a score.

## 5. What you must refuse to do

Do not characterise rooms stage D4 declared cousins as siblings. Do not treat a network stage D4 could not draw as a tree of forms. Do not let branch size become
importance. Do not recut anything or change the model here: a fourth-order theme that lumps two
things a branch separates, a renaming, a subform, goes to `notes-D5.md` for stage D6, which may
act on it as an amendment, and to `defects.jsonl` for stage E1; a claim
a branch bounds is a `findings.jsonl` line under rule 14. A closed branch's account is not
edited; a description later found wrong is superseded by a new file with what showed it (rule
18).

## Moments to log

Each branch opened; the expectations computed; the representative members chosen with the
rule; the form test's result; the survival figures; the waterfall's steps; what the members
showed that the room notes did not predict.

## Final message

The claim (what the forms are and how they differ in their functioning), the branch that best
supports it, the branch that most threatens it, the condition; then: branches accounted;
branches that failed the form test; names that survived the members' reading; the branch whose reading disagreed most with the room models; where the uncomposed
rooms sit; arrow absences real and `not-testable-here`, by count; propositions that failed
against a real expectation, and the `findings.jsonl` lines they bounded; the waterfall's
contradictions if any; survival by branch; the most consequential difference between two forms;
the licences exercised.

## Close

`done.sh D5` at every branch; `handback-D5.md`; the head; the closing diary line.

## Negative shared result

If D4 finds no supported shared branch, keep `branches-D5.jsonl` empty and explain the result in `notes-D5.md`. The waterfall goes from the global model directly to a selected local account and its evidence. Report remaining local evidence and unresolved cases. Do not invent a branch. `binds` and `leaves_free` contain only optional four-problem mappings; `construct_bindings` must resolve to empirical construct ids, and a form requires their `binding_account`.
