# RETURN-B3: the return specification for the stage B3 fleet

Frozen with the stage file. The packet builder serves it, the brief cites it, and the validator's schema is read from it.

## Rule 0, in the contract's words

Rule 0. **Single placement, exception on the record.** A second-order theme carries one third-order theme: the one whose gate its material satisfies best; where more than one gate is satisfied, the theme's `decide_when_both` field decides. A second placement only where one cannot carry the material, and never silently: it needs its own distinct supporting concept, a written `why_not_one` in terms of what the single placement would fail to carry, a named dispensable one, and a line in `multiplacement_log.jsonl`. Three at most; beyond three, place one and record `item-is-a-bag`. An unjustified extra is a defect. The log is a measurement: recurring `(primary, additional)` pairs are boundaries the scheme has not drawn, and stage C1 reads that table first.

## How you read

Read the index page whole first. Open a family's page before you place anything into it, and list the families you opened in `families_opened`. Your batch opens with a sibling block for each of its rooms: the labels of all that room's second-order themes, so you can see what a theme is not. Then the items, interleaved across rooms, each numbered by position. Some items are marked as flagged bags: place them from the concepts, not from the coder's grouping. Your packet is complete in itself.

## What you return, in this order

**1. The prediction line**, first, before any placement: the pair of third-order themes you expect to find hardest to tell apart in this batch, and one sentence why.

```json
{"agent": "a017", "predicted_confusion": ["T3-007", "T3-011"], "why": "one sentence"}
```

**2. The return line**, one JSON line per item, in position order, and nothing else between the lines.

- `sub`, `theme_id`: the item's heading, `<sub>/<theme_id>`, copied exactly: the room's name, then the item's id (`T2-` and five digits, such as `T2-08479`).
- `batch`: the batch name on the packet's title line (such as `B017`). `agent`: your reader id as given to you. `replicate`: the replicate given on the title line. `position`: the item's number in the batch.
- `third_order`: the theme ids you place the item on, primary first. One id, unless rule 0's exception holds; never more than three.
- `multi`: true when `third_order` holds more than one id.
- `why`: for each id in `third_order`, what about THIS item put it there rather than its nearest neighbour.
- `confidence`: `clear` or `arguable`.
- `read`: `whole` (you read the label, the note and every concept) or `theme-block` (the label and note, and the concepts in part). No other value.
- `exemplar_read`: null. No exemplar is served at this stage.
- `families_opened`: the family ids whose pages you read the full tests of before placing this item.
- `bag`: true only when more than three themes would be needed and at least one theme beyond the one placed has three concepts of its own. Then `third_order` holds one id and `why` names the others. A bag with no other theme at the three-concept floor is not flagged a bag: `bag` false, `also_present` `{}`.
- `t_start`, `t`: when you began and finished the item (ISO time, as you can tell it).
- `support`: the concept ids your placement rests on, copied exactly from the item's own concept lines (`C` and seven digits, such as `C0781518`). Cite only concepts listed under the item you are placing; an id from another item, or one you do not see in the packet, is an error.
- `also_present`: `{}` unless `bag` is true. For a bag, the themes beyond the one placed that have at least three concepts of its own, twenty themes at most, each with those concept ids: `{"T3-…": ["C…", "C…", "C…"]}`. Twenty is a bound, not a goal: name only the themes you find at the floor; you need not reach twenty. A theme with fewer than three concepts of its own is not listed. `support` holds the concepts behind the placed theme; a theme in `also_present` never repeats the placed one.
- `multiplacement_log`: `[]` when `multi` is false. When `multi` is true, one record per theme beyond the first, the line rule 0 owes to `multiplacement_log.jsonl`:

**3. The multiplacement record**, on the same line, inside `multiplacement_log`:

```json
{"sub": "...", "theme_id": "T2-.....", "key": "<sub>/<theme_id>", "batch": "B017", "agent": "a017", "replicate": 2, "position": 23, "primary": "T3-007", "additional": "T3-011", "why_not_one": "what this material carries that T3-007's gate does not reach", "why_this_one": "what in the material satisfies T3-011's gate, and its distinct supporting concept", "support_primary": ["C0781518"], "support_additional": ["C0781527"], "dispensable": "which of the two you would drop if forced to one, and what would be lost"}
```

Four rules on it:
- **Distinct support.** The additional theme needs its own supporting concept id; the same concept twice is the same reading twice, and is refused.
- **`why_not_one` is about the material, not the scheme.** "Both gates are satisfied" is not a justification, since `decide_when_both` settles that case; it must name what the single placement would fail to carry.
- **`dispensable` is compulsory and may not be `null`.**
- **No line carries more than three themes.** A third requires its own record and its own `why_not_one` against both the others. Beyond three, place one, set `bag` true, and name the others under `also_present` as above.

**4. The second pass.** After your last item, read your whole batch again and write one line per position, in position order, after all your first lines and before the end marker, each naming the line it revises: `{"pass": 2, "revises": 23, "batch": "B017", "agent": "a017", "third_order": ["T3-007"], "changed": false, "why_changed": null}`. When you would now place the item differently, `changed` is true, `third_order` holds the new placement and `why_changed` says what made you change it. The second pass never overwrites the first: your first lines stand as written.

**5. The end marker and the confirmation.**

```json
{"sub": "...", "theme_id": "T2-.....", "batch": "B017", "agent": "a017", "replicate": 2, "position": 23, "third_order": ["T3-007"], "multi": false, "why": {"T3-007": "what about THIS theme put it here rather than its nearest neighbour"}, "confidence": "clear|arguable", "read": "whole|theme-block", "exemplar_read": null, "families_opened": ["G03", "G09"], "bag": false, "t_start": "...", "t": "...", "support": ["C0781518"], "also_present": {}, "multiplacement_log": []}
END-OF-RETURN
```

After your last line, write the end marker `END-OF-RETURN` on a line of its own. Confirm that you reached the end of the packet by writing that marker; a return without it is a partial return and is reissued.
