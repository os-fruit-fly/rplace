# RETURN-C2: the return specification for stage C2's reviewer

Frozen with the stage file. The dispatch serves it beside the packet `C2-reviewer`, and the validator's schema is read from it. One reader, one packet, one return.

## What you return

One JSON line, then the end marker on a line of its own. Nothing else, before or after.

- `agent`: your reader id as given to you.
- `served`: the sha256 of the model file served, copied exactly from the packet's first page (64 lowercase hex characters).
- `errors`: one object per error you find, each with:
  - `kind`: exactly one of `quote` (a quote that does not show what it is said to show), `contradiction`, `count` (a count that cannot be right), `loop` (a loop no room runs the whole way round), `order` (an arrow whose instance does not show the order claimed);
  - `where`: the page and the place, such as `model-p3-sections.md, A16` or `story-p3.md, What sends a room back`;
  - `what`: what is wrong, in one or two sentences, citing the words, ids or numbers.
  An empty list if you find none.
- `partition`: your one partition of the third-order themes into fourth-order themes, different from the analyst's in `tiers.md`. One object per group, each with `label` (its name), `members` (the third-order theme ids, `T3-NNN`, copied from `tiers.md`) and `holds` (what holds the members together, in one sentence). Each third-order theme in `tiers.md` appears in exactly one group or in `unplaced`.
- `unplaced`: the third-order themes you leave outside every group, `[{"id": "T3-NNN", "why": "one clause"}]`, or `[]`.
- `differs`: one or two sentences on how your partition differs from the analyst's, and why yours meets the criterion in `tiers.md`.

```json
{"agent": "...", "served": "<sha256 of the model file served>", "errors": [{"kind": "quote|contradiction|count|loop|order", "where": "...", "what": "..."}], "partition": [{"label": "...", "members": ["T3-001", "T3-023"], "holds": "..."}], "unplaced": [{"id": "T3-017", "why": "..."}], "differs": "..."}
END-OF-RETURN
```

A disagreement is never a verdict: your reading decides nothing.

After your line, write the end marker `END-OF-RETURN` on a line of its own. Confirm that you reached the end of the packet by writing that marker; a return without it is a partial return and is reissued.
