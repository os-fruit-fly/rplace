# RETURN-B2: the return specification for the stage B2 pilot

Frozen with the stage file. The packet builder serves it, the brief cites it, and the validator's schema is read from it.

## Rule 0, in the contract's words

Rule 0. **Single placement, exception on the record.** A second-order theme carries one third-order theme: the one whose gate its material satisfies best; where more than one gate is satisfied, the theme's `decide_when_both` field decides. A second placement only where one cannot carry the material, and never silently: it needs its own distinct supporting concept, a written `why_not_one` in terms of what the single placement would fail to carry, a named dispensable one, and a line in `multiplacement_log.jsonl`. Three at most; beyond three, place one and record `item-is-a-bag`. An unjustified extra is a defect. The log is a measurement: recurring `(primary, additional)` pairs are boundaries the scheme has not drawn, and stage C1 reads that table first.

## What you return

One JSON line per item in the packet, in packet order, and nothing else between the lines. Read the index page whole first. Open a family's page before you place anything into it, and list the families you opened in `families_opened`.

- `sub`, `theme_id`: the item's heading, `<sub>/<theme_id>`, copied exactly: the room's name, then the item's id (`T2-` and five digits, such as `T2-08479`).
- `batch`: the packet name (the name on the packet's title line, such as `P03-r3-1`). `agent`: your reader id as given to you. `replicate`: 1. `position`: the item's number in the packet.
- `third_order`: the theme ids you place the item on, primary first. One id, unless rule 0's exception holds; never more than three.
- `multi`: true when `third_order` holds more than one id.
- `why`: for each id in `third_order`, what about THIS item put it there rather than its nearest neighbour.
- `confidence`: `clear` or `arguable`.
- `read`: `whole` (you read the label, the note and every concept) or `theme-block` (the label and note, and the concepts in part).
- `exemplar_read`: null. No exemplar is served at this stage.
- `families_opened`: the family ids whose pages you opened for this item.
- `t_start`, `t`: when you began and finished the item (ISO time, as you can tell it).
- `support`: the concept ids your placement rests on, copied exactly from the item's own concept lines (`C` and seven digits, such as `C0781518`). Cite only concepts listed under the item you are placing; an id from another item, or one you do not see in the packet, is an error.
- `multiplacement_log`: null when `multi` is false. When `multi` is true, this is the line rule 0 owes to `multiplacement_log.jsonl`: `{"primary": "T3-…", "additional": ["T3-…"], "codes": ["C…"], "why_not_one": "what the single placement would fail to carry", "dispensable": "T3-…"}`. The check leg copies it into the pilot's record. It never enters the run's own `multiplacement_log.jsonl` from stage B1.
- `item_is_a_bag`: true only when more than three themes would be needed and at least one theme beyond the one placed has three concepts of its own. Then `third_order` holds one id and `why` names the others. A bag with no other theme at the three-concept floor is not flagged a bag: `item_is_a_bag` false, `also_present` `{}`.
- `also_present`: `{}` unless `item_is_a_bag` is true. For a bag, the themes beyond the one placed that have at least three concepts of its own, twenty themes at most, each with those concept ids: `{"T3-…": ["C…", "C…", "C…"]}`. Twenty is a bound, not a goal: name only the themes you find at the floor; you need not reach twenty. A theme with fewer than three concepts of its own is not listed. `support` holds the concepts behind the placed theme; a theme in `also_present` never repeats the placed one.

```json
{"sub": "...", "theme_id": "T2-.....", "batch": "P03-r3-1", "agent": "...", "replicate": 1, "position": 23, "third_order": ["T3-007"], "multi": false, "why": {"T3-007": "what about THIS theme put it here rather than its nearest neighbour"}, "confidence": "clear|arguable", "read": "whole|theme-block", "exemplar_read": null, "families_opened": ["G03", "G09"], "t_start": "...", "t": "...", "support": ["C0781518"], "multiplacement_log": null, "item_is_a_bag": false, "also_present": {}}
END-OF-RETURN
```

After your last line, write the end marker `END-OF-RETURN` on a line of its own. Confirm that you reached the end of the packet by writing that marker; a return without it is a partial return and is reissued.
