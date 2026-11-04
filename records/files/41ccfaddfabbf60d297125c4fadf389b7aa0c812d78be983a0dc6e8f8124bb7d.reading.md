# Claims against their evidence (stage E1, section 1)

Written at E1b-04, 27 October 2026. Contract section 1 names two kinds of claim:
- a **pattern** claim rests on counts across rooms, with their denominators;
- a **words** claim rests on what members wrote, through exemplars that resolve and the return's verdicts.

For every proposition (`propositions.jsonl`) and every branch (`branches-D5.jsonl`), this table gives:
- the kind declared;
- the evidence named;
- the rival;
- whether the validation the claim received is of its kind.

A claim validated with the other kind's evidence would be a defect. No claim is.

The sources:
- `audit-E1/claims.py` (E1a) lays out the fields.
- `audit-E1/claims_returns.py` (E1b-04) counts the return's verdicts on each arrow. It reads the last ruling in `adjudications.jsonl` of every return line on the arrow, from both the first return and the re-check, and counts the accepted lines by op.
- The arrows' `support` quotes were resolved against the store at this leg: 57 quotes, all of which resolve.

The model is the D3 freeze, `46384686…`. The held proposals for P05 and A11 are not part of it.

## The propositions

An arrow's order count reads "holds of both". "Both" is the number of rooms carrying both of its elements. "Holds" is the number in which the first concept of the one comes before the first concept of the other. The null is the 95th percentile of 500 shuffles within each room (seed 20261014). The return's accepted lines are summed over the proposition's arrows.

| id | kind declared | evidence named (arrow: holds of both, share, null p95; finding) | rival | return, accepted lines (instantiate, restrict, absent) | validation of its kind? |
|---|---|---|---|---|---|
| N01 | pattern | A02 64 of 89, 0.719, 0.539; A01 81 of 126, 0.643, 0.571; A03 148 of 190, 0.779, 0.389; no finding | The order is how threads are made: the call is a title, the reports are comments under it. | 1,095; 622; 1,203 | Yes. Counts with denominators, every null beaten; 9 support quotes resolve. |
| N02 | pattern | A04 235 of 401, 0.586, 0.539; A13 171 of 240, 0.713, 0.642; A19 87 of 121, 0.719, 0.678; F-008 (inferred, standing) | Neighbours were there from the first post, so the talk comes with the spot. | 218; 885; 2,099 | Yes. Every null beaten; A19 is thin, as stated. |
| N03 | both | A15 93 of 129, 0.721, 0.550; A16 82 of 104, 0.788, 0.606; A17 95 of 172, 0.552, 0.477; A18 56 of 68, 0.824, 0.676; F-014 (read, bounded: refusals give a reason in 23 of 38, acceptances in 2 of 14) | Restraint is coded only when there is an attack call to refuse (A16 partly constitutive). | 729; 737; 2,494 | Yes, both kinds. The order counts beat their nulls, and the words come from 80 seeded reply pairs read for reasons. |
| N04 | pattern | A07 139 of 182, 0.764, 0.434; A08 225 of 289, 0.779, 0.609; A09 113 of 145, 0.779, 0.628; F-004 (inferred, standing) | The order is the clock's: celebrations and records cluster at the end in every room. | 230; 773; 1,802 | Yes, but the rival names the clock and none of the three arrows is read against the hour-73 bracket. |
| N05 | pattern | A20 132 of 155, 0.852, 0.594; before hour 73 (rulings): 102 of 118, 0.864, 0.644; F-010 (inferred, bounded) | A removal needs a post to remove (A20 partly constitutive). | 79; 247; 778 | Yes, and the one arrow read against a bracket of prior.md section 4. |
| N06 | pattern | A06 160 of 203, 0.788, 0.655; F-005 (inferred, standing) | The members who run scripts are the members who keep the work. | 63; 279; 918 | Yes. |
| N07 | both (theorised, thin) | A11 111 of 185, 0.600, 0.670, **not beaten**; A12 no order count; F-021 (inferred, standing); F-023 (read: 25 of 31 written acceptances bare) | Members decided their organization in chats off the record. | 712 (A12 691); 955 (A11 627); 948 | **The pattern half is not established**, as the proposition says (theorised, thin). The words half rests on read replies and on the return instantiating A12 in 691 accepted lines. The return restricts A11 far more than it instantiates it (627 against 21); that is the held proposal to withdraw it. It is not validated with the other kind's evidence. |
| N08 | pattern (thin) | A10 11 of 21, 0.524, 0.429; F-019 (read: after doubt and a loss, 10 moved and 11 gave up) | Rooms move by a coalition's plan, and the judgment of too few hands is written after. | 44; 457; 729 | Yes, on 21 rooms, as stated thin. |
| N09 | pattern (thin) | A05 106 of 158, 0.671, 0.658; A14 138 of 214, 0.645, 0.636; F-020 (read) | Sparing is tacit and comes first; help comes with the neighbour, not with the border. | 517; 508; 1,138 | Yes, narrowly: both shares sit just above their nulls. A05's mechanism is theorised, as stated. |

**The bracket each sits in** (prior.md section 4):
- The order counts run over the whole record. The pre-event week, placement (hours 0 to 73) and aftermath (73 to 97) are counted together.
- Only A20 (N05) is also read inside a bracket, before hour 73.
- Every counted arrow but A12 and A21 carries the onset contrast's early and late counts (`early_late`).

**Not done, against prior.md section 3:**
- No arrow's order test was run at held size, although section 3 says the population pattern is "supported by a pattern that holds in counts over the analysed set and at held size". The one finding tested at held size is F-009 (the play frame does not delay the canvas work).
- The order was read against section 4's brackets for A20 alone.
- Both gaps are recorded in `defects.jsonl` (line 114).

## The branches

Every branch rests on its shared key in the ledger for membership, and on its account's quotes for what it is. The 35 accounts cite 38 to 89 concepts each, and those resolved at E1b-01. The kind of each warrant is therefore both, as prior.md section 3 asks of forms and subforms. "Form" means the branch passed D5's form test; "grouping" means its members share the key but no condition was stated that explains them jointly. Local validation is established for none.

| branch | rooms | form or grouping | shared warrant | verdicts: composes, with residue, cannot tell, does not compose | account's cited concepts |
|---|---|---|---|---|---|
| F01 | 103 | grouping | unresolved | 54, 49, 0, 0 | 63 |
| F02 | 33 | grouping | unresolved | 18, 15, 0, 0 | 46 |
| F03 | 18 | grouping | unresolved | 9, 9, 0, 0 | 48 |
| F04 | 13 | grouping | unresolved | 4, 9, 0, 0 | 59 |
| F05 | 12 | grouping | unresolved | 6, 6, 0, 0 | 46 |
| F06 | 8 | grouping | unresolved | 5, 3, 0, 0 | 56 |
| F07 | 59 | grouping | unresolved | 21, 38, 0, 0 | 48 |
| F08 | 50 | grouping | unresolved | 21, 29, 0, 0 | 44 |
| F09 | 54 | **form** | **supported** | 22, 32, 0, 0 | 53 |
| F10 | 38 | grouping | unresolved | 16, 22, 0, 0 | 38 |
| F11 | 43 | grouping | unresolved | 18, 25, 0, 0 | 50 |
| F12 | 22 | grouping | unresolved | 9, 13, 0, 0 | 52 |
| F13 | 9 | grouping | unresolved | 2, 7, 0, 0 | 46 |
| F14 | 7 | grouping | unresolved | 4, 3, 0, 0 | 53 |
| F15 | 42 | grouping | unresolved | 20, 22, 0, 0 | 47 |
| F16 | 35 | grouping | unresolved | 13, 22, 0, 0 | 46 |
| F17 | 36 | grouping | unresolved | 12, 23, 1, 0 | 59 |
| F18 | 15 | grouping | unresolved | 4, 11, 0, 0 | 53 |
| F19 | 14 | grouping | unresolved | 6, 7, 1, 0 | 46 |
| F20 | 10 | grouping | unresolved | 2, 7, 1, 0 | 74 |
| F21 | 32 | grouping | unresolved | 21, 10, 0, 1 | 68 |
| F22 | 30 | grouping | unresolved | 13, 17, 0, 0 | 67 |
| F23 | 30 | grouping | unresolved | 8, 22, 0, 0 | 71 |
| F24 | 27 | grouping | unresolved | 12, 15, 0, 0 | 67 |
| F25 | 27 | grouping | unresolved | 15, 11, 0, 1 | 62 |
| F26 | 23 | grouping | unresolved | 10, 13, 0, 0 | 58 |
| F27 | 27 | grouping | unresolved | 9, 18, 0, 0 | 79 |
| F28 | 22 | grouping | unresolved | 11, 11, 0, 0 | 67 |
| F29 | 25 | grouping | unresolved | 8, 17, 0, 0 | 65 |
| F30 | 24 | grouping | unresolved | 7, 17, 0, 0 | 66 |
| F31 | 22 | grouping | unresolved | 12, 10, 0, 0 | 70 |
| F32 | 21 | **form** | **supported** | 5, 16, 0, 0 | 86 |
| F33 | 23 | grouping | unresolved | 10, 13, 0, 0 | 89 |
| F34 | 22 | grouping | unresolved | 9, 13, 0, 0 | 78 |
| F35 | 18 | grouping | unresolved | 8, 10, 0, 0 | 83 |

The verdicts are the first return's. `branches-D5.jsonl` names no proposition that a branch holds or fails.

## prior.md section 3's declaration, against what each level rests on

- **The population pattern.**
  - *Declared:* counts with their denominators; the order on the clock against section 4's brackets; the onset contrast; the organizing end under section 5; support at held size; the words secondary.
  - *Rests on:* counts with their denominators and an order beating a within-room null, for 18 of the 20 arrows the propositions rest on. A11 is not beaten, and A12 has no count; A21 is in no proposition and has no null test. The onset contrast's counts are recorded for 19 of the 20, all but A12, and the organizing end is A1's field.
  - *Not done:* the held-size test, and the brackets for every arrow but A20.
  - *The words:* the 57 support quotes, secondary as declared.
- **The forms and subforms.**
  - *Declared:* both kinds, the shape primary for membership and the words primary for what the form is.
  - *Rests on:* just that. The keys of D4 give membership, and the accounts' cited concepts give the words.
  - *Status:* two of 35 branches pass the form test; 33 are groupings, reported as such.
  - *The six room forms of D4a-05 to D4a-08:* they rest on the same two kinds, by changes and codes, with their accounts (`room-form-*-account.md`).
- **The particular histories.**
  - *Declared:* the words primary: a dated sequence of the room's own turns that the model's elements reach.
  - *Rests on:* the room models of D2 and D3 and the coders' case accounts.
  - *The element-reach half* of section 3's local measure was computed at E1a (`audit-E1/element_reach.py`). Of 5,380 second-order themes that hold a coordinating turn, in 696 rooms, 4,759 are reached by a standing element (88.46 per cent), or 5,239 with the candidates (97.38 per cent). 297 rooms are reached in full, or 581 with the candidates.
  - *Not computed:* the other half, a validated adaptation or a theme listed as unresolved with its reason. So local validation is not established.
- **The method question's verdict** is the work of section 3 of the audit.

## The switch records of `literature-C3.md`, against the findings they superseded

| record | what moved | findings it supersedes | against the ledger |
|---|---|---|---|
| Leg 1 (C3a), "Switch records" | none: "F-006 rested on a count across rooms and still does; the bound is another count across rooms." | none | Holds. F-006's C3a line is a bound of the C2 line (`supersedes` "F-006@C2a-01", a form other than the bare id the later lines use), with no change of kind. |
| Leg 2 (C3b), "Switch record: the concept" | The concept's name, from a coinage ("the one-line enrolment") to the literature's ("the preferred acceptance"). Its form claim, from exemplars to a pattern across rooms (F-014). Its function claim, put to a pattern, which failed (F-015). | none, as it says: the concept was in `concept.md`, in no finding | Holds. F-014 and F-015 are C3b lines with no `supersedes`. F-014 was later bounded at C5c-11 by a line that supersedes it by its bare id. |
