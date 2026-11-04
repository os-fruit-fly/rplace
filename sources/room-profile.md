# The siblings' file profile

Target length: under 3,400 words. Fourth version, 7 October 2026: `names.jsonl`, and the data structure's sixth column (J). Third version, the same day: counts in three modes, the organizing-end record, typed episode kinds, prompts beyond codes, the form-pass check replaced and the hour-73 boundary as global A1 has it (J: "go ahead", 7 October). Second version, 5 October 2026: the waived checks named, confidence rows typed, one form for IDs in prose, v32's own theme IDs for r/place, and Part II's fields typed, after Codex's runtime answer (`RUNTIME-codex.md`, blockers 3 and 8), its field review (`REVIEW-field-codex.md`, findings 4, 6 and 7), an independent check, Codex's recheck (quotes stay strings), and an audit on 6 October (the global checkers read through maps).

The case aggregator and the field model write the global aggregator's files. This profile says, for each file, which global definition binds, where the file lives, which IDs it uses, and the few fields a sibling adds or replaces. Everything not named here is the global definition, field for field. A validator built from this profile wraps the global validators; it relaxes no global check except the ones the tables of waived checks and of file names name.

## IDs, and how they leave

| Object | Inside a sibling | Global form |
|---|---|---|
| first-order concept | `c0042` | `sub:c0042` |
| coder theme | `t07` (rooms); `t01` on (r/place, v32's IDs, given at emission) | `sub:t07` |
| gate (r/place, before emission) | `g01` | none: `theme_map.jsonl` ties it to its coder theme |
| residue (r/place) | the coder theme marked `residue: true` in `theme_map.jsonl`, known by that mark alone | its coder theme ID, never read as a kind |
| `T4` theme | `T4-001` | `T4-001` |
| dimension | `D01` | `D01`, as C2 writes it |
| element, arrow, loop | `P01`, `K01`, `C01`, `R01`, `A01`, `L01` | the same |
| finding, proposition, form-pass finding | `F-001`, `N01`, `FP-01` | the same |
| episode, phase | `E-01`, `PH-01` | none |
| group, interaction (r/place) | `G-001`, `I-001` | none |
| reader findings (r/place, R6) | `RD1-01`, `RD2-01` | none |

Rooms have no legs: where a global field asks for a leg, a room writes its stage (`R4`), so `since` is `R4-pass-3`. Each revision of a finding carries `rev`, a sequence the controller stamps per finding, and `supersedes` names the exact earlier revision, as `F-003@R4#2` (the global check still reads the ID before `@`); a forward reference, a cycle or a reference to a revision marked lost is refused, and the references survive export and rollback. r/place writes its legs. Inside a sibling every ID is bare. When a file leaves, the controller prefixes every local ID and every reference to one, recursively through nested fields, with the room's name (`denmark:c0042`; `sub:` in the tables above stands for it) or `field:` (r/place). Reddit's item, thread and author IDs are source IDs, never prefixed. An unprefixed local reference in an exported file is an export error.

**IDs in prose.** In Markdown files an ID is written in backticks, as `T4-002`, and only that form counts as a reference. The exporter prefixes a backticked token only when it matches an ID domain above and resolves inside the sibling; a backticked token that matches a domain and does not resolve is an export error. Quotations are never changed, in any file and whatever they contain: a `text` or `quote` field, a span inside quotation marks, and a Markdown blockquote are copied byte for byte.

## Waived global checks

The validator does not run `stage_C1.py` or `stage_C2.py` whole: they assume rooms, a third order, `sub:code` IDs and the global stage and file names. It reuses their checks on quotes, counts, references, loops, order and the critic's return, over the sibling's files through the table of file names below, and replaces the checks in this table. A global check neither reused nor replaced is listed in the validator's report as not run, never skipped in silence. Each row has a passing and a failing fixture.

| Global check | Why it does not apply | What the sibling checks instead |
|---|---|---|
| C1: each `T4` theme's members are third-order themes (`T3-`) | the siblings have no third order | members are coder themes, or the codes of one split coder theme; never both a coder theme and its own codes; every member resolves |
| C1: `assignments_final.jsonl` places third-order themes; C1 §9's file set | the same | `assignments.jsonl` has exactly one row per coder theme, or per code of a split one; each `T4` in `to` exists |
| C1 and C2: the fourth-order themes partition the tier below, no member in two | the tier below is the coder themes, placed under rule 0 | a coder theme may sit in two or three `T4` themes, each extra placement in `multiplacement_log.jsonl` with its `why_not_one`; otherwise no member in two |
| C2: `evidence.codes` are `sub:code_id` of the global store | one case's own codes | bare `c` IDs resolving in the sibling's `codes.jsonl` |
| C1 and C2: `tier_history.jsonl` and history lines carry stage `C1` or `C2` | the siblings' own stages | read R3's `T4` cuts (merging, relating) as C1, and R3's dimension lines and other moves, and R4, as C2; R5 as C3; R6 as C5. r/place's legs carry their stage |
| C2: `FP-` IDs resolve in `form_pass-C1.md` | the file's sibling name | `FP-` IDs resolve in `form_pass.md` |
| C2: `subs` and `sampled_against[{sub, ...}]` name rooms | one room, or the square | `units[{unit, id}]` and `sampled_against[{unit, id, why_chosen, found}]`, one sampling unit per arrow, every `id` in its register |
| C2: `support[{sub, code, quote}]`, `support_transition[{sub, thread, ...}]` name a room | the sibling is the sub | the same fields without `sub` |
| C2: an element's `tier` is a third-order theme, a `T4` theme, a dimension or an `FP-` finding | no third order | a coder theme in the third order's place |
| C2: `early_late`, the onset contrast across rooms | one onset | `live_aftermath`, below |
| C2: loop events carry `sub` | the sibling is the sub | events carry `arrow, code, item, hour, clock`; every event dated, in order |
| C2 §5: `story_rooms-pN.jsonl` | no rooms | `story_episodes-pN.jsonl`, and `story_phases-pN.jsonl` for r/place, one line per episode or phase |
| fields that ask for a leg | rooms have stages | `stage` in place of `leg` (rooms); `since` and `supersedes` on stages; `supersedes` resolves to one exact earlier revision |
| C3: legs 1 and 2 | no shelves held | not run; `literature-C3.md` says so |
| C5: `data_structure-C5.md`'s third-order column | no third order | six columns (below) |
| E1: `claims-E1.md` | the siblings' own close | `claims.md`, same fields; r/place adds its audit scripts |
| B3 §1.5 and §3.6 (r/place, Part I): a distinct supporting concept for each extra theme | a code is one concept | `spans`: verbatim substrings of the code's quote that meet each gate; an extra gate needs words of its own |
| C2: the critic's error kinds are `quote`, `contradiction`, `count`, `loop`, `order` | r/place's critic also checks levels and sides | r/place adds `level`, `one-sided` and `room-side`; rooms use the five |
| C2: `within_case.md` names three rooms | one case | it names up to three episodes (rooms) or episodes or phases (r/place), as many as the record holds, as the global check's `min(3, available)` allows; `within_case.jsonl` types each kind, with an episode or the reason it is unavailable |
| C1: `form_pass-C1.md` contains the words "never enters the arithmetic" | a word is no check | no gate and no prevalence count names an `FP-` ID; the coverage of a sweep may be reported |

**File names.** Where a global check reads a file, the sibling's file stands in its place:

| Global file | Sibling file |
|---|---|
| `scheme_v2.jsonl` (the third-order scheme) | the coder themes: the coding's `themes.jsonl`, with `theme_map.jsonl` for r/place |
| `assignments_final.jsonl` | `assignments.jsonl` |
| `form_pass-C1.md` | `form_pass.md` |
| `notes-C2.md` (the criterion, the stop, the answers to the critic) | `notes-R4.md` |
| `notes-C3.md` (the restated prior, the read count) | `notes-R5.md` |
| `data_structure-C5.md`, `claims-E1.md` | `data_structure.md`, `claims.md` |
| `story_rooms-pN.jsonl` | `story_episodes-pN.jsonl` (and `story_phases-pN.jsonl`, r/place) |
| `fourth/fourth.md`, `within_case.md`, `model/story-pN.md`, `RETURN-C2.md`, `_packets-C2/`, `review-C2.md` | the same names; `fourth.md` lists at its foot the coder themes no `T4` theme took |

## The structure

| File (sibling path) | Global definition | Sibling differences |
|---|---|---|
| `fourth/fourth.jsonl` | C1 §8: `id,name,gloss,declared,source,disconfirm,members,prose`, `recalled` for borrowed names before C3; C2 part A: `changed,mistaken_for,in_model,pass`, and `"dimension": []` with a reason where no dimension gathers it | `members` as the table above. Added: `gate{condition, discriminator, varies, is_not, decide_when_both, gate_parts}`, which rule 0 places by. The field adds `field_level` and `square_only` (true where only the square could show it) |
| `dimensions.jsonl` | C2 part A: `id,label,members,construct{status,source,changed,mistaken_for,disconfirm_elsewhere,gloss},question,confidence,pass` | `members` are `T4` IDs. `confidence` keeps its global meaning (`clear|arguable`). The field adds `field_level` |
| `assignments.jsonl` | C1 §9, `assignments_final.jsonl` | One row per coder theme, or per code of a split one: `from` (`t07` or `c0042`), `to` (a list of one to three `T4` IDs under rule 0, or empty), `status` (`placed`, `contextual`, `out-of-scope`, `unresolved`), `reason`, `move`. The residue is split code by code, each code with its own status and reason. No coder theme is rewritten |
| `multiplacement_log.jsonl` | rule 0 | the same, keyed by coder theme |
| `structure.md`, `form_pass.md` | C2 part A; C1 §7 | the same; form-pass findings stay in prose, outside the arithmetic |
| `tier_history.jsonl` | rule 11: the move, `was`, `prompted_by`, why | `stage` in place of `leg` for rooms; the controller's stamp (below) |

## The model

| File | Global definition | Sibling differences |
|---|---|---|
| `model/elements.jsonl` | SCHEMA-adaptations §1: `id,kind,statement,tier,dimension,evidence{findings,codes},since,status`; C2's range and bound references | `tier` is a `T4` ID, a dimension, an `FP-` ID, or a coder theme in the third order's place; `evidence.codes` are local `c` IDs. The field adds `field_level`, `groups`, `group_evidence` and `room_side` (below) |
| `model/arrows.jsonl` | C2 §4, every field, with `counterexample_response` where a counterexample exists | `sampled_against` and `units` as the table of waived checks says. `support[{code, quote}]` and `support_transition[{thread, items, codes, interval_min}]` drop `sub`. `live_aftermath` in place of `early_late`. The field adds `field_level`, `groups`, `group_evidence`, `room_side`. C3's `mechanism_source` and `mechanism_C2` only where the Puranam paper supplies a mechanism through an abductive read |
| `model/loops.jsonl` | C2 §4: `id,level,arrows,events[...],mechanism,alternative,why_not_alternative` | `level` keeps its global meaning and is always `within-room`; events as the table above; hours are the forest's hours since the canvas opened, comparable with the global. The field adds `field_level` |
| `model/history.jsonl` | C2: one line per element change with the move and the leg, and §6's stamp | `stage` and, for r/place, `leg`; the controller's stamp: `utc`, codes read, threads read, tokens read. `prompted_by` names what prompted the change: codes, coder themes, `FP-` findings, or critic items by their ID in `RETURN-C2.md`; at R5 a paper, as `"<author year>"`, with C3's `abductive: true`. An `FP-` finding may prompt a change and never joins a tier |
| `concept.md`, `model.md`, `model/story-pN.md` | C2 parts B and C, §5 | the same |
| `story_episodes-pN.jsonl`, `story_phases-pN.jsonl` | C2 §5, `story_rooms-pN.jsonl` | one line per episode or phase in place of per room |
| `saturation.jsonl` | §6, one line per pass | the same |

**Group fields (r/place).** On an element or arrow at `group` level, `groups` holds exactly one `G` ID; at `inter-group` level, two or more; at `person` and `field` level, `groups` is empty or names the groups the claim is about. `group_evidence[{group, codes}]` has one entry per named group, each with at least one code whose item a member of that group wrote or that reports that group's act. `room_side` is a list with one entry per named group, `{group, answerable, what_a_room_would_show, why_not}`: `answerable` is `yes`, `partly` or `no`; `what_a_room_would_show` is required unless `no`; `why_not` is required unless `yes`.

**Counts and samples.** `tool.py count` makes every count, in one of three modes (room contract, "What a count is for"), and a file that states one carries `{mode, unit, n, denominator: {unit, n, of}, receipt}`. *Coverage*: matched IDs over a named population, with no gate. *Prevalence*: the claim's ID and its own gate text; carries, had the opportunity and does not, and had no opportunity, summing to the testable units; units that are not testable (rule 6) are listed and counted beside them, never as zero. *Aftermath*: global A1's share (`organizing_end.json`). Every count states its window's endpoints and lists the units at a boundary. The count unit is one of codes, coded items, threads or authors, and groups for r/place. A deleted or unknown author is excluded and counted, never one author. `of` says which set, as "r/place's live codes". Groups are counted from `groups.jsonl` only. A sampling unit (`sampled_against`, `units`) is one of `episode`, `phase` or `group` (r/place) or `episode` (rooms), and is never mixed with a count unit in one figure.

**`live_aftermath`**, on each strong arrow (global C2 asks `early_late` of strong arrows), is `{live, aftermath, spans_73}`, counted in the arrow's sampling unit by the hour of the evidence the arrow cites from each unit: at or before hour 73, live; strictly after hour 73, aftermath, as global A1 counts. A unit whose cited evidence falls on both sides counts once on each side, and its ID is listed in `spans_73`.

## The literature, the account and the record

| File | Global definition | Sibling differences |
|---|---|---|
| `literature-C3.md`, `mapping-C3.jsonl` | C3 §1 and §5: `fourth,problem,why,cannot_do`; problem one of division, allocation, reward, information, none | legs 1 and 2 do not run; the field adds `field_level` |
| `propositions.jsonl` | C5: `id,statement,rests_on,theorised,finding,carried_by,rival` | the field adds `field_level`; a proposition `both` names its primary in its paragraph, as C5 asks |
| `data_structure.md` | C5 | six columns: quote, first-order concept, coder theme as coded (its label), the name given at R3 (empty where none), `T4` theme, dimension. Each quote row keeps its attribution: community, author, hour and code ID. The residue and how rows were chosen are stated |
| `findings.jsonl` | rule 14, every field | `stage` is the sibling's stage; `rev` and `supersedes` as above; `evidence` refers to local IDs and registers |
| `departures.jsonl` | rule 10 | the same |
| `claims.md` | E1's claims | the same; r/place adds its audit scripts |

## The sibling's own files

| File | Fields |
|---|---|
| `names.jsonl` (R3, optional) | one line per named coder theme: `theme` (its ID), `label` (the coded label, byte for byte), `name`, `declared` (`borrowed`, `adapted` or `coined`), `source` (`"<author year>"`; empty if coined), `recalled` (true until R5 checks a borrowed name), `disconfirm`, `move`. No global stage reads it, no exported global field carries a `name`, and the comparison export of `data_structure.md` drops the name column |
| `episodes.jsonl` | `id`, `start_hour`, `end_hour` (forest hours since the canvas opened), `statement`, `codes`, `threads`, `bracket` (the rule that cut it) |
| `organizing_end.json` (rooms at R2, r/place at FA) | global A1's line for this room: `organizing_end_hour`, `last_coordinating_code`, `aftermath_share`, `coordinating_turns`, `turns_after_73`, `aftermath_coordinating_codes`, `work_remained` (`kept`, `lost` or `silent`), `work_remained_codes`, and `count_receipt`. Turns are distinct coded items strictly after hour 73; with none, `aftermath_share` is null and `unavailable` says so. Silence is an unknown outcome, never `lost` |
| `within_case.jsonl` | three lines, one per kind: `kind` (`ordinary`, `unpredicted`, `stopped_early`), `episode` (an `E-` ID, or a `PH-` ID for r/place, or null), `unavailable` (null, or why the record holds none) |
| `phases.jsonl` (r/place) | `id`, `start_hour`, `end_hour`, `name`, `statement`, `rule` (the phase rule applied), `evidence` |
| `groups.jsonl` (r/place) | `id`, `canonical` (one name), `aliases` (every other name, in the participants' spelling), `subreddits`, `called` (what participants call it), `first_hour`, `last_hour`, `quotes` |
| `interactions.jsonl` (r/place) | `id`, `groups` (two or more), `word` (the participants' word for the meeting), `start_hour`, `end_hour`, `reported_by` (`one-side`, `both-sides`, `third-party`), `quotes` |
| `scheme.jsonl` (r/place) | `id` (`g01`), `name`, `condition`, `discriminator`, `varies`, `is_not`, `decide_when_both`, `gate_parts`, `family` |
| `theme_map.jsonl` (r/place) | `gate` (`null` for the residue), `theme` (v32's ID, or `null` for a gate no code reached), `label`, `n_codes`, `residue`, and on the residue's line `n_unresolved` and `n_no_gate` |
| `disagreements.jsonl` (r/place, FD) | B4 §7's line, with `code` in place of `sub` and `theme_id`, gates in place of third-order themes, and `lost[{gate, would_carry}]`: the gates a multiple placement ruled to one did not keep |
| the critic's return | global C2 §6's: `RETURN-C2.md`, the packet under `_packets-C2/` with the instruction verbatim, the return line with `served` (the sha256 of `model.md` served) and `errors[{kind, ...}]`, `review-C2.md` with one rival partition of the coder themes; kinds as the table of waived checks says |
| `families.jsonl` (r/place) | `id`, `name`, `gates` (the `g` IDs it holds, in scheme order) |
| `recovery.jsonl` (the controller's) | one line per resumption: `utc`, `snapshot`, `identity`, `state`, `token`, `recall` (questions, answers, score), `result` (`pass` or `stopped`) |
| `evidence.jsonl` (r/place's package) | `id` (the field ID it supports), `code`, `quote`, `cite`: one line per code the package refers to anywhere |
| `reader-1.jsonl`, `reader-2.jsonl` (r/place, R6) | one line per finding: `id`, `kind`, `object` (or empty for the account as a whole), `finding`, `evidence{codes}`, `severity` |
| `confidence.jsonl` | one line per object: `kind` (`room`, `model`, `T4`, `dimension`, `element`, `arrow`), `id` (the object's bare ID; empty for `room` and `model`), `grade` (`high|medium|low`; for `room`, `something_to_explain`: `yes|partly|no`), `why`, `would_change_it` (not for `room`), `evidence{codes, episodes}`. Sealed by the controller with the model's version hash; never edited after |

**Quotes.** A `quote` is always the verbatim string, as the global files and checks have it (C2's `support[{code, quote}]` included): the source's text between the code's offsets, resolved through `cite`. Where a sibling file needs the citation too, it sits beside the quote, never inside it: `cite{item, start, end, thread, hour, author}`, with the source's item and thread IDs unprefixed. A `quotes` list in a sibling's own file (`groups.jsonl`, `interactions.jsonl`) holds `{code, quote, cite}` objects.

## What the validator checks beyond the global checks

- Every ID matches its domain above, and every reference resolves inside the sibling.
- Every waived check's replacement, as its table row says.
- Every `names.jsonl` theme resolves, and its `label` equals the coded label.
- `assignments.jsonl` has exactly one row per coder theme, or per code of a split one, and each `T4` in `to` exists.
- Every `sampled_against` entry names one declared sampling unit, and an arrow uses one unit; every stated count resolves to its receipt, mode, unit and denominator.
- `confidence.jsonl` has a line for every `T4` theme, dimension, element and arrow, and its hash matches the sealed copy.
- r/place: the group fields as above; group counts come from `groups.jsonl`; `theme_map.jsonl` covers every gate and every emitted theme, with at most one residue.
- No file holds a canvas field or an atlas reference.
- On export, every local reference is prefixed, no source ID is, and every quotation is byte-identical to its source.

What no validator checks: whether an arrow's mechanism is right, whether the groups were drawn well, whether a room really could answer a room-side statement, and whether a reader understood what it was served. Those stay with the critic, the readers and J.
