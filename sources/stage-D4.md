# Stage D4. The taxonomy from adaptations.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort); `[1m]` context allowed for the first cut only. **Legs:** one per
pass over the ledger, closed at the pass's end or earlier when you choose. Every move (a branch
named, a subform declared, a cross-link declared) is logged and snapped when it is made (§2).
**Fleet:** none. The clusters are yours; no blind cluster maker.

**Steps:** `D4a-01`, `D4a-02` ... one per pass over the ledger (a cut); the last ends with the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each logged move (a branch, a subform or a cross-link). At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh D4 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, `SCHEMA-adaptations.md` §7, the last five diary
entries, `validate.py --open D4`; the hierarchy shelf arrives (METHOD.md). First leg: the
tree-likeness statistic and the key frequencies, before any tree.

**Reads allowed:** `_views/rooms-x-adaptations.<level>.<kind>.tsv` and the combined matrix; the
distance matrix, the per-room deltas and the dendrogram as views; `mem.py rooms --with <key>`,
`contrast`, `adaptations --element`; the member rooms' material through the verbs (`mem.py
room`, `forest`, `case`, `codes --sub`), when you declare it as a ground (§2); `forms/` as it
grows; `_views/relations.tsv`;
`dropped.jsonl` and `RUN.json` for the accounting of §4. **Forbidden:** the chunk-share tree
before your cuts are made (it is the comparison, built by script after); the canvas as an undeclared ground (rule 7);
a list of which rooms belong together from anywhere but the ledger; a room's prose, a
concept's text or a coder's note as an undeclared ground for a cut (a branch is grounded on keys,
and on its member rooms' material only where the cut's line names it).

**Outputs:** `_views/adaptation-tree.{html,svg,json}`; `branches.jsonl`; `forms/<id>.md` (generated from the accepted definitions);
`crosslinks.jsonl`; `tier_history.jsonl` per cut; `tree-D4.md` (the statistic, the views, what
you drew and did not, the accounting of §4); `chunk-share-D4.md`, `chunk-share-D4.jsonl` and
`chunk-share-D4.py` (the comparison, by script); `projections-D4.jsonl` (the verdicts and the
canvas per branch and per cluster, by `tools/projections.py`); `notes-D4.md`.

## 1. Read the statistic and the frequencies first

`gen_views.py` computed the distance (SCHEMA §7, weights from `prior.md`) at every level and
per kind, through `distance.py`: the delta score on the combined matrix and each room's own delta
(`_views/delta-by-room.tsv`, Holland et al. 2002's per-taxon score), and an average-linkage
dendrogram (`_views/dendrogram.nwk`, with the rooms at 2, 3, 5, 8 and 12 clusters in
`dendrogram.txt`). The NeighborNet is drawn outside the run, in SplitsTree, from
`_views/distance.nex`; the operator adds it to the handback if asked, and nothing here waits on it. `distance.py` writes the distance. Normalizing by targets reduces one volume effect; it does
not remove unequal coverage or all effects of size. Confirm from `_views/tree-likeness.json` that the
weights and grades are `prior.md`'s.

The quartet delta ranges from 0 to 1 for nondegenerate quartets: larger values mean
greater departure from additive tree distances. Equal-sum quartets are uninformative and
excluded, not evidence of a star or a special 0.5 threshold. A tree is a view of the
dissimilarities, not proof of a hierarchy or ancestry. Report its limitations and cross-links. Read the key frequencies: which keys are shared by many rooms, at which
level, of which kind; how many rooms hold no accepted key. Log both before any cut.

### The leaf-to-root view

`python3 tools/adaptation_tree.py --out out` writes `_views/adaptation-tree.html`, `.svg` and
`.json` from the carried distance and records input hashes. It also runs automatically after
`distance.py`. Each leaf is an individual case. The conceptual root is the frozen global
model; the connecting trunk is explicitly unscaled. The global model is not a case, a
centroid or an inferred ancestor. Join heights show adaptation dissimilarity.

Internal joins propose connections at different levels. Name a branch only after its shared
adaptations, mechanism and supporting cases have been adjudicated. The JSON carries branch
membership and cross-links, including memberships that cannot nest. Case-specific particulars
remain attached to the local account, even when excluded from portable shared coordinates.
Missing returns must never enter the no-adaptation group. A room with no accepted shared keys
is not necessarily a room that needed no local adaptation.

The carried ladder distance is a declared nonmetric operationalization: its best match at a target can
hide additional differences. The export flags zero-distance pairs with different key sets and
reports the same cuts under exact-key Jaccard distance. The export also lists incomplete lifts
and shared keys with different condition text for review. Identical observed absences agree
at the target; `unobserved` and `not-testable` absence records do not enter shared coordinates.
Additional placements require inspection beyond the primary lift. Neither sensitivity aligns
the substantive meaning of conditions automatically. Compare operation kinds and ladder
levels, explain unstable branches, and inspect substantively opposite conditions that share
a coarse key. No cut, minimum group size or low delta by itself establishes a form. Do not
read this dendrogram as a chronology or claim that the hierarchy was independently validated.

## 2. Cut by element, by level, by kind

For each element with many adaptations, `mem.py rooms --with <key>` at the third-order level:
rooms sharing a key are a candidate group. Keys that co-occur across rooms are a branch's
definition; name the branch by what its keys change in the global model, never by a member's
name. Read the kinds apart: a group held by shared corrections is rooms where the model fails
the same way, the strongest form signal; shared elaborations the subform signal; shared
specifications the weakest. Walk up the ladder: rooms that meet only at the fourth-order or
dimension level are cousins, not siblings, and a branch is declared at the level where its
members meet. The minimum group size below which a shared meeting is variation, not a subform,
is a default of five; you may change it with a reason written in `tree-D4.md` before the first
cut, and a number set in `prior.md` by the operator stands in for the default.

The ladder walk is the tier check: a group that meets at the third-order level meets at every
level above it by construction of the lift, so the question for every candidate is the deepest
level it holds at. At the dimension level or the bare target the aggregation is doing the
work, and the group is a grouping, not a branch. Say which candidates moved level when walked.

```json
{"id": "F03", "parent": null, "level": "third", "kind": "correction|elaboration|specification",
 "keys": ["restrict:P07:T3-014", "..."], "members": ["denmark", "..."], "name": "...",
 "what_it_changes": "...", "since": "D4-cut-4"}
```

Subforms nest by adding keys. A room whose adaptations meet different groups at different
targets is a cross-link, declared in `crosslinks.jsonl`, never forced. Rooms that returned
`none` are the unadapted group. If represented as a branch, mark `type: "unadapted"`, use empty
keys and no parent, and include only explicit current `none` returns. Missing returns, pending
lines and empty portable profiles do not qualify. A negative result with no warranted branches
is valid: write an empty `branches.jsonl` and `taxonomy-status.json` with
`status: "no-supported-forms"`, a substantive `reason`, and every returned `reviewed_rooms` id.
Cross-links carry `sub`, at least two distinct `branches` ids containing that case, and `reason`.
Parents must be acyclic. A finer key inherits a broader key when operation and target agree and
the finer node lifts to the broader node; literal id equality across tiers is not required.

**The member rooms as a ground.** Besides the keys, you may ground a cut on what the member
rooms' material shows, read with the verbs: what the rooms did that the keys only point at. Name
that ground in the cut's `tier_history.jsonl` line (`"ground": "keys"` or `"ground": "keys and
material: <rooms and what they showed>"`) and log each read. The material never stands alone: a
branch still has keys. A member that lacks one of them may stand in the branch on its material
only under that declared ground, and `tree-D4.md` says what in its material puts it there.

Every cut is a move, named from Grodal, Anteby and Holm's eight. Log it when you make it (`mem.py
log --kind move --ids <branch>`, the move named), write its line in `tier_history.jsonl`, and snap
it (`python3 tools/snap.py D4 move-<move>-<n>`). A leg may carry several moves. You hold the
canvas and cannot unknow it, so every cut is snapped before anything is projected onto it (§6);
the snap line is the record. Say in `tree-D4.md` whether any cut was attractive because of what its members had
made, the grounds for each cut, and what would have made you choose differently. Never give every room its own label (contract §1).

## 3. What each branch is, before D5 writes it

For each branch, in `forms/<id>.md` (generated from `branches.jsonl` and the ledger): members,
shared keys with their lines' `how` sentences, the elements shared with the global model
unchanged, representative concepts from `LADDER` projected to the branch, and, from
`_views/relations.tsv`, whether members connect in the mention graph, distinguishing hostile and cooperative mentions.
Connectivity alone does not establish a coalition. That label requires cited joint commitments
or coordinated tasks with a stated scope; report the graph only as a relational diagnostic. Present branches in the order cut, never by size.

## 4. Every room accounted for

Reconcile against `dropped.jsonl` and the D2 counts in `RUN.json`. Every room of the analysed
set is in exactly one of: a member of a declared branch; the unadapted group (returned `none`);
adapted but in no branch, because every accepted line is a key no other room holds or every line
is a particular; out by name, `unreturned` at D2. The four counts sum to `n_analysed` from
`counts.py`. The rooms in no branch are named, with why.

## 5. The fixed composition comparison

After the final branch cut is snapped, declare the comparison in `notes-D4.md`, then run:

```
python3 tools/chunk_compare.py --out out --store package/store
```

This versioned engine writes `chunk-share-D4.result.json`, `.jsonl`, `.md` and a replay entry
script. It reads only the concept store, placements, tiers, dropped cases and prior. It does
not read adaptations, branch definitions, verdicts or outcomes. Its comparison shares the
inductively built coding structure; it is a non-adaptation baseline, not theory-free evidence.
Do not recut branches after seeing it. The D4 validator replays the trusted engine under isolated
Python and compares numerical results, inputs, dependencies and cluster membership. A missing
NumPy/SciPy installation or a script stub fails acceptance. Replay can take several minutes.

**Features and units.** One row per room, columns fourth-tier themes. Count unique unretracted
concept ids by their theme links, never file order or unverified `n_codes`; fail on unresolved or
conflicting links. Unplaced concepts contribute no observed category and are counted separately.
Split a multiply placed theme's weight equally over distinct fourth-tier destinations. Report
split themes, placed concepts, all concepts and placed themes by room. Empty compositions are
excluded by name. Fewer than five placed themes is a low-information flag, not an exclusion in
the primary diagnostic; rerun the full pipeline without flagged rooms.

**Smoothing.** Use `P=(x+a*m)/(n+a)`, with corpus mean `m` and finite positive `a` declared in
`prior.md` as `chunk_concentration = 1.0` (1.0 if the line is absent). This is fractional
pseudo-count smoothing, an explicit heuristic, not a Dirichlet-multinomial maximum likelihood
fit or calibrated posterior uncertainty. Remove zero columns before logarithms. Hold `a` and
`m` fixed within resampling. Report the median own-data weight and sensitivity to `a/10` and
`10*a`. Ward acts on Euclidean CLR vectors; Jaccard presence and Hellinger share sensitivities
use average linkage, with adjusted Rand indices at each eligible cut.

**Null and resampling.** The null permutes complete theme allocation patterns among themes,
retaining each room's concept weights and number of themes and the corpus frequencies of theme
allocation patterns. It does not hold concept-weighted category totals fixed. This tests a
specific diagnostic null, not every size or coverage effect. Use at least 200 accepted bootstrap
draws and 100 permuted copies under each of two distinct declared integer seeds (defaults 0,1).
Fit each bootstrap including duplicate case weights, then compute ARI on unique sampled case
identities once. A draw enters k's statistic only when more than k distinct cases were sampled.
The low-information threshold of five themes and k ceiling of twelve are declared heuristic
defaults, not methodological necessities. The fixed engine records them. Eligible k is 2
through min(12, floor(n/2)); fewer than four cases, one feature or identical
profiles supports no partition. Report actual sample counts and Monte Carlo standard errors.

Each k carries silhouette, real/null stability means and medians, both margins, and null 95th
percentile. A k clears only when both margins are positive under both seeds. The carried k
maximizes the worst margin, with smaller k breaking a tie. If none clears, retain the complete
diagnostic table and state `no-supported-partition`; an empty cluster file is then valid.
These exploratory selection rules do not give a significance level after searching k.

**Tier and size checks.** Report dimension and third-tier ARI at every eligible k, the third-tier
column count and mean nonzero count, without calling tier agreement proof of form. Third-tier
weights split over all recorded placements. Inspect sparse profiles, unequal concept coverage,
concepts within themes and the low-information contrast. Record cross-tables of branch and
cluster memberships against observed volume fields, with units and missing denominators. A
correlation or this null alone cannot establish that a difference is independent of size.

**Overlapping forms.** The computational clusters are a partition; substantive branches may
nest or overlap. Best-match member-set Jaccard is descriptive and valid for those sets. Compute
ordinary ARI against branches only for an explicitly named exclusive cut with one membership
per eligible case; otherwise report that ARI is undefined. Do not force cross-links into a
partition or use outcomes to select that cut. Clusters have deterministic two-letter codes,
no inferred mechanism labels. Shared mechanisms remain a separate case-grounded judgment.

## 6. Projected on afterwards

After the cuts are snapped and the comparison is built, `python3 tools/projections.py` writes
`projections-D4.jsonl`, which carries per
branch and per cluster: the D2 verdicts counted (`composes`,
`composes-with-residue`, `does-not-compose`, `cannot-tell`) with the percentile of that
distribution against the permutation null; and the six canvas fields summarised, with contract
§5's sentence on what they measure and the same null. A branch holding the rooms the model
cannot compose is a result for stages D5 and E1, not a reason to recut; whether branches differ
in what they kept on the canvas is reported; a cut that rests on it says so (rule 7).

## 7. What this stage cannot show

The taxonomy is computed from your own adjudicated lines and cannot corroborate them: it can
show patterns in the changes recorded and test specific size diagnostics, not that the
elements are the right elements. The tiers are closed after stage C5 except through D3's
amendment regime (rule 11); a ledger that looks wrong is a finding for `notes-D4.md`,
`defects.jsonl` and stage E1, never a recut here.

## Moments to log

The statistic read, with the frequencies; each candidate group and what you did with it; each
cut by name, with its level and move; each cross-link; the accounting of §4; the comparison's
method declared before its script runs; the comparison read, with its two verdicts by number;
the projections read.

## Final message

The claim (what the branches say the forms are), the room that best supports it, the room that
most threatens it, the condition; then: branches by level and kind, subforms, cross-links, the
unadapted group's size, the rooms in no branch, the four counts summing to `n_analysed`, the
tree-likeness value and whether a tree was drawn, the comparison's figures (the empties, `a` and
the median weight, the Rand indices among the three distances, the third-order tier's sparsity,
the tier verdict by number with its index, the volume verdict with its percentile, the k
carried, each with and without the low-information rows), the verdict and canvas percentiles per
branch, confirmation that no verdict, canvas field or branch entered the comparison's feature
space; the licences exercised.

## Close

`done.sh D4` at the end of each pass, or earlier when you choose, each move logged and snapped as
it was made; the last leg closes at the interview point below; `handback-D4.md`; the head; the closing diary line.

**Interview point.** The last `D4a` leg writes `out/interview/<its leg id>.md` (for example `D4a-03.md`) (under 800 words: what you did, what you found, what surprised you, what you doubt, and the three questions you would most like to be asked) and closes with `done.sh D4 --cut interview`: the tree of branches, subforms, cross-links and rooms, before D5 writes a word about it. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief under the leg, the stage, the step and the minute, and refuses the cut without the brief (and, at a stage's end, without the handback).
