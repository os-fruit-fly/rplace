---
title: "SCHEMA-adaptations, v38: elements, operations, the ledger, adjudication, views, reconstruction, the handoff"
given: from the return (D1), beside the contract
---

<!-- INDEX -->
| section | lines | words |
|---|---|---|
| 1. Elements of the global model | 29 to 61 | 322 |
| 2. Operations | 62 to 110 | 587 |
| 3. The ledger line | 111 to 137 | 237 |
| 4. Validation at ingest | 138 to 158 | 201 |
| 5. The room model | 159 to 174 | 183 |
| 6. Adjudication | 175 to 200 | 207 |
| 7. What is built from the ledger | 201 to 234 | 436 |
| 8. Reconstruction | 235 to 246 | 116 |
| 9. The handoff folder (stage D1) | 247 to 267 | 195 |
| 10. Decisions taken, and their consequences | 268 to 296 | 264 |
<!-- /INDEX -->

# The adaptation schema

Everything downstream of the return (adjudication, the taxonomy, the branch descriptions, the
reconstruction test, the element views) works only if an adaptation is a typed operation on a
named element of the global model, with evidence, and not a paragraph. This document fixes the
types. It is deliberately small: five element kinds, seven operations, one ledger line, one
adjudication line, and the files derived from them.

## 1. Elements of the global model

The model the analyst builds at stages C2 to C5 is stored in `model/elements.jsonl`, one line per
element, and `model/arrows.jsonl`. Five kinds:

| kind | prefix | what it is | example statement |
|---|---|---|---|
| process | P | something the organizations do, as a verb phrase over time | recruiting placers from outside the subreddit through a template post |
| condition | K | a state under which a process runs or a claim holds | the artwork borders a hostile neighbour |
| claim | C | a statement relating processes, conditions and outcomes | where K04 holds, P07 starts before the first attack, not after |
| role | R | a position members take that the model names | the template keeper |
| arrow | A | a sequence or dependence between elements | P03 precedes P07 |

Element line:

```json
{"id": "P07", "kind": "process", "statement": "...", "tier": "T4-003", "dimension": "D2",
 "evidence": {"findings": ["F-031"], "codes": ["asoiaf:c0042", "denmark:c0117"]},
 "since": "C2-pass-3", "status": "standing"}
```

`tier` links the element to the fourth-order theme it belongs to; `dimension` to the aggregate
dimension. `status` is standing, bounded, withdrawn or candidate (a proposed element accepted at D3
and not yet instantiated in a second room); a bounded element carries the condition ids that
bound it. Every change to an element is a line in `model/history.jsonl` with the move
(one of Grodal, Anteby and Holm's eight) and the leg. Ids are never reused; a withdrawn id stays
withdrawn.

The id vocabulary the labelers receive at the return (D1 to D3) is the projection of `elements.jsonl` and
`arrows.jsonl` at the model version hash written into the handoff: for an element id, kind,
statement, tier and dimension; for an arrow id, kind, from, to and mechanism (and its statement
where it has one); and `status: tentative` on an entry stage C4 took from the field. Nothing else.

## 2. Operations

Seven operations. The labeler chooses the operation; the kind (specification, elaboration,
correction) follows from it and is not chosen. The aggregator may reclassify at D3, and the
reclassification is logged.

| op | fields | meaning | kind |
|---|---|---|---|
| `instantiate` | element, source, how | the element operates here in this way: who, with what, at what moment | specification |
| `absent` | element, why, observation | `observed-absent` or `not-needed` with evidence; `unobserved` or `not-testable` marks evidence limits | evidenced absence is specification or a warranted correction; unknown states support neither |
| `add-condition` | element, condition | the element operates here only under a condition the model leaves open | elaboration |
| `add-step` | element, statement | a finer process inside the element that the model does not name | elaboration |
| `link` | from, to, kind | a sequence or dependence the room needs and the model lacks | elaboration |
| `restrict` | element, condition | the element fails here unless the condition holds, and the model says otherwise | correction |
| `contradict` | element, statement | the room's record contradicts the element as stated | correction |

The operations are this instrument's operationalization of Fisher and Aguinis (2017): `instantiate` and
`absent` are vertical contrasting (the theory applied at another level of detail); `add-condition`
and `restrict` are new construct specification of a condition; `add-step` is construct splitting;
`link` is structuring specific and sequence relations; `contradict` and `propose` are horizontal
contrasting. Busse, Kach and Wagner (2017) motivate exploring boundaries through construct refinement,
moderators and mediators. Our two correction codes distinguish discrepancies, not mandatory
outcomes: adjudication may bound, refine, extend or replace a formulation. 

**Source and target nodes .** Every operation names a target in the model (an
element id, or a dimension id for `link`) and, where it adds anything, a source in the room's own
ladder: a second-order theme id of the room (`denmark:t07`) or a code id. `add-condition` and
`restrict` give the condition as a source theme id; `add-step` gives the finer process as a source
theme id; `link` connects a source theme to a target element or dimension; `instantiate` and
`absent` name the target and cite codes. Free text lives only in `how`. Two labelers can no longer
describe one adaptation in two vocabularies, because they point at nodes.

At ingest each source node is lifted through `assignments_final.jsonl` as it stands at the
model version the handoff carries (stage C1's placements, re-decided by every logged recut since):
second-order theme → third-order theme → fourth-order theme → dimension. The lifted path is stored
on the line (`"lift": ["denmark:t07", "T3-014", "T4-003", "D2"]`, with `null` at a level the theme
was never placed at). An unplaced second-order theme lifts to nothing above itself; those are the
lines from which D3 mints new third-order themes when several rooms' unplaced themes point at the
same target.

An eighth form, `propose`, is not an operation on an element: it names something the room needed
that no element covers. It carries a statement and evidence and is unattached until D3, where it may become a
shared candidate element or a locally validated particular. Unshared does not mean false.

Relational adaptations use the same operations with a `relation` field naming the other room
(`"relation": "placenl"`), so "defence delegated to a named neighbour" is `instantiate` on the
defence process with a relation. Naming another room in `relation` does not make the line a
particular; naming the room itself in `condition` does (§4).

## 3. The ledger line

`adaptations.jsonl`, one line per adaptation, written by `ingest.py` from the labelers' returns,
never by hand:

```json
{"id": "denmark-007", "sub": "denmark", "op": "add-condition", "element": "P07",
 "source": "denmark:t07", "lift": ["denmark:t07", "T3-014", "T4-003", "D2"],
 "condition": "the artwork is under attack from two sides at once",
 "statement": null, "how": "explains why denmark recruited outside placers on night two and not before",
 "evidence": {"codes": ["denmark:c0117", "denmark:c0118"], "transitions": ["denmark:t-C5"]},
 "relation": null, "portable": true, "kind": "elaboration",
 "origin": "labeler", "model_version": "sha256:…", "labeler_run": "codex-2026-11-…"}
```

Required for every line: `sub`, `op`, `element` (or `propose` with `statement`), at least one
code id in `evidence.codes`, `how` as one sentence, `model_version`. `source` (a theme or code id of the room) is required for every op except `absent`, and for
`contradict` it may be a code id rather than a theme; for `instantiate` it is the theme that shows
the element operating, so that instantiations carry a key and enter the distance as
specifications; `condition` and `statement` are the source theme's label copied for reading, not
free text, except that `contradict` and `propose` may state in words what no theme names; `from`, `to` for `link` are source and target. `kind`, `portable` and `lift` are
computed at ingest.

A room with nothing to adapt returns one line: `{"sub": ..., "op": "none", "how": "the global
model explains this room as stated", "evidence": {"codes": [...]}}`, with evidence for the fit.
Silence is a missing return, not a verdict.

## 4. Validation at ingest

`ingest.py D` accepts a room's return only if every line passes:

1. Schema: the fields in §3, the op in §2, no extra fields.
2. Element ids exist in the model at `model_version`, and are not withdrawn. A return against a
   stale version is rejected whole and reissued with the current packet.
3. Code ids exist in the room's `codes.jsonl` in the store, and are not retracted. A transition id
   exists in the room's forest.
4. `how` is one sentence (one terminal stop; under 40 words).
5. Portability: `condition` and `statement` contain no subreddit name from the census and no
   proper name from the room's lines in the analyst's `lexicon-A1.md`, except in `relation`. A line that fails is kept with
   `portable: false` and is a particular by construction (contract rule 12).
6. The return carries the end marker from `RETURN-D.md` and the room's line count matches its
   header.

Rejected returns go back through the handler with the failing rule named. Completion comes
before any limit: the handler returns every room it can, and marks a room `unreturned` only when
it cannot. Counts of accepted, reissued and unreturned rooms go into `RUN.json` at the close of
D2.

## 5. The room model

`rooms/<sub>/model-D.md`, written by the labeler beside the ledger, is `case.md` rewritten in the
model's vocabulary. Its sections are the aggregate dimensions, in the model's order. Inside a
section the labeler writes prose, and every claim carries either an element id in brackets
(`[P07]`) or a `[new: …]` marker for what no element covers, and a code citation (`[c0117]`) from
the room's own codes. The file ends with a grade the labeler writes, `composes`, `composes-with-residue` or
`does-not-compose`, and one sentence of why. The grade is the labeler's; the verdict, with its
fourth value `cannot-tell`, is the fleet's (FLEET.md), and the two are reported side by side. The lead's grade concerns the adapted local explanation; the fleet
verdict concerns the fixed global model. The return also requires `local_status: validated |
unresolved | insufficient-evidence` and a `## Local exceptions` section linking discrepancies
to evidence and adaptations. Local validation is distinct from portability.

`ingest.py` checks the room model for the same id and code validity as the ledger, and that
every adaptation line's element appears in the room model at least once.

## 6. Adjudication

`adjudications.jsonl`, one line per adaptation, written by the analyst at D3 through
`mem.py adjudicate`:

```json
{"adaptation": "denmark-007", "decision": "accept", "kind": "elaboration",
 "reason": "the condition is stated without the room, and asoiaf-011 meets it",
 "pair": "asoiaf-011", "change": "h-0412", "leg": "D3-P07"}
```

`decision` is accept, modify, reject, particular or pending. `modify` carries the rewritten
condition or statement in a `revised` field, which passes the same portability check as the
labeler's line, and the original stays in the ledger. A supported portable line with no shared warrant is `particular`. A line with insufficient evidence remains `pending` and unresolved at D3 close; pending lines are
counted as such. `pair` names the second
room whose accepted line meets the same candidate correction. Recurrence prompts a reasoned shared-warrant assessment, not automatic model revision; `change` names the logged revision or explicit scope decision when one is made. `kind` here is the analyst's, and differs from the ledger's when the analyst
reclassifies.

D3 reads by element: `mem.py adaptations --element P07` returns every accepted-or-pending line
touching P07 across rooms, sorted by op. One leg per element group, one hundred lines per packet
at most. After the elements, the `propose` lines: each becomes a candidate element (an
`elements.jsonl` line with `since: D3` and status `candidate`) or a particular.

## 7. What is built from the ledger

All generated by `gen_views.py` at leg close; none hand-edited.

- `rooms-x-elements.tsv`: rows rooms, columns elements, cell the op or blank. The view D3 reads
  before any element.
- `rooms-x-adaptations.tsv`: one matrix per ladder level and per kind, plus the combined one. A
  key at level L is `op:target:<node at L>` from the line's lift, for accepted and modified lines
  at the model version frozen at D3's close (every line is re-lifted to that version before
  stage D4; rooms whose elements changed at D3 were re-checked). Particulars and pending lines
  are excluded. The distance, written once so nobody re-derives it:
  - For rooms i and j, let T be the set of targets touched by either room's lines. For each
    target t in T, let L be the deepest ladder level at which some line of i and some line of j
    on t have the same lifted node (3, 4, dimension, or the bare target), and let w(L) be 4, 2, 1,
    0.5; if only one room touches t, the term is 0.
  - Let g be the operation agreement over the two lines that met at L: 1 for the same op, 0.5
    for ops of the same kind, 0 for different kinds, and -1 for `instantiate` against `absent`
    or `add-condition` against `contradict` on that target. Where several pairs of lines meet at
    L, take the pair with the largest g.
  - Similarity S(i, j) = sum over t in T of w(L_t) times g_t, divided by 4 times |T|, so S lies
    in [-1, 1]. Dividing by |T| removes the mass effect: a room with more lines gains no closeness
    from having more. Distance d = (1 - S) / 2: 0 for identical fully comparable adaptation profiles, 0.5 for rooms
    that share no target (unrelated), 1 for rooms whose lines oppose each other everywhere.
    Rooms whose line sets are both empty (`none`) have d = 0 with each other and 0.5 with every
    adapted room. Explicit observed-absent or not-needed lines on the same target contribute the deepest-level same-op weight without requiring a source lift. Unobserved and not-testable lines remain in local accounts but are excluded from shared distances. Missing lift entries never become shared None keys; partially comparable non-absence profiles can retain nonzero distance even when their raw sets match. `tools/distance.py` computes it.
  - Per-kind matrices use only lines of that kind; the tree-likeness statistic (Gray, Bryant and
    Greenhill 2010) is computed on the combined level-3 matrix. The weights and grades are
    declared in `prior.md` before stage D4 opens and are not changed after.
- `exception-report-D.md`: per room, particulars against accepted shared lines; per element,
  the count of rooms adapting it by op; the sentence the stage file requires when all of a room's
  adaptations are particulars.
- `forms/<id>.md` at stage D4: a branch as the set of shared keys, its members, and the analyst's
  description of what the branch does differently.

## 8. Reconstruction

`rebuild.py <sub>` uses the effective adjudicated ledger. It includes accepted, modified and supported particular lines in local reconstruction. It lists pending lines as unresolved, never asserted support. The latest accepted room return replaces that room's earlier ledger even if its new ids list is empty. Original ledgers and model versions remain available.

Recheck ids include a digest of the line content and model version: `R-<sub>-<digest>-NNN`. An unchanged return is idempotent; a changed return cannot inherit an earlier line's adjudication. Prior recheck rows remain in the ledger and the latest accepted manifest selects current ids. Superseded compile files and local account copies remain under `return-history/`.

`adaptation-returns.jsonl` records each accepted return with `sub`, `phase` (`initial` or `recheck`), `status: accepted`, `model_version`, `ids`, `local_status` and `local_grade`. An old local return carries forward to a changed model only when D3 explicitly marks the room unaffected with a reason; all affected cases return to their original leads. The skeleton reports the current model hash, return version and local version status.

An `absent` line produces `no` only for `observed-absent`. `not-needed`, `unobserved` and `not-testable` retain their own meanings. Legacy unspecified absence is conservatively unobserved. Unknown states never enter shared adaptation distances as negative evidence.

At E1 a fresh reader receives the skeleton and the coder's blind `case.md` with the room's second-order themes, never `model-D.md`. Score all warranted claims, record evidence limits, and report reconstruction fidelity by branch and by historical global verdict. This is an in-sample preservation and composition check, not independent truth estimation.

## 9. The handoff folder (stage D1)

`out/handoff-D/` written by `handoff.py D`:

- `RETURN-D.md`: the return specification, verbatim in every task, the schema of §3 and §5, the
  end marker, the reissue rule.
- `VOCABULARY.json`: the id vocabulary at the model version hash.
- `MODEL.md`: the global model as prose with ids, the account from stage C5 cut to the ceiling
  the labeler's context allows, plus the wiki pages for the elements the room's second-order
  themes were placed under.
- `LADDER.md`: the coding table, quote to aggregate dimension, with representative codes for every
  tier the model uses, projected for the dimensions and elements in `MODEL.md` .
- `tasks/<sub>/TASK.md`: the labeler's instruction: read the coder documents, rewrite `case.md`
  in the model's vocabulary, write the ledger; the room's `case.md`, `codes.jsonl`,
  `themes.jsonl`, `brief.md`, `forest.md`; the placements of the room's
  second-order themes; the two outputs and where they go.
- `HANDLER.md`: the adaptation handler's brief: dispatch order (by size ascending, so failures
  surface early), how to run a labeler in Codex, the return path `DROPS/D/<sub>/`, the reissue
  rule, and what never to do (no access to `out/` beyond the folder, no edits to the vocabulary,
  no merging of rooms).

## 10. Decisions taken, and their consequences

1. **Evidence states are distinct.** A room need not use every global element. Only evidenced absence or lack of need supports a negative assertion. Silence and untestability are unresolved evidence, never a contradiction. An evidenced absence challenges a universal claim only after its scope and evidence are examined.
2. **Completion over reissue.** No reissue limit as a rule; the handler's job is to get every room
   returned and to check that the returns work, and `ingest.py` reports what fails and why. A
   room is `unreturned` only if the handler says so, and the count is reported.
3. **Proposed elements enter the model in the same run.** At D3 a `propose` line that the
   analyst accepts becomes an element and the model is rewritten with it. Then a re-check: a
   few of the rooms whose evidence produced the change are sent back through the labeler against
   the revised model, in a small second handoff (`handoff-D/recheck/`), and their new returns
   say whether the rewrite fixed what the evidence pointed at. The re-check rooms and their
   before-and-after ledgers are reported at 18.
4. **The labeler's packet carries the whole ladder.** Beside the wiki pages of the elements its
   themes were placed under, the labeler receives the coding table with representative codes for
   every tier the model uses: quote, first-order concept, second-order theme, third-order theme,
   fourth-order theme, aggregate dimension, projected for the dimensions and elements in
   `MODEL.md`. A labeler that sees only its own codes cannot understand an aggregate dimension,
   so it cannot say what the model fails to explain. `handoff.py` builds this projection from
   `_views/data-structure.tsv`.








