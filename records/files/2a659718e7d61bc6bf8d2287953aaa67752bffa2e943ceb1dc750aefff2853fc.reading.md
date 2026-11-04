# RETURN-C5: the return specification for stage C5's three readers

Frozen with the stage file. The dispatch serves it beside each of the packets `C5-reader-1`, `C5-reader-2` and `C5-reader-3`, and the validator's schema is read from it. One reader, one packet, one return.

## What you return

One JSON line, then the end marker on a line of its own. Nothing else, before or after.

- `reader`: your reader id as given to you.
- `served`: the sha256 of `account.md`, copied exactly from the packet's first page (64 lowercase hex characters).
- `claims`: five to nine claims you take `account.md` to make, each in your own words, one sentence each.
- `relations`: the relations between elements you take the account to claim, each as a short phrase with the ids, such as `"A03 acts on P04"` or `"P05 comes before P08"`. An empty list if you take it to claim none.
- `could_not_follow`: each sentence you could not follow, and each term a reader would not accept as plain words, quoted exactly from the packet. An empty list if there is none.
- `unsupported`: in a few sentences, the claims of the account you cannot find the evidence for in the packet, and any room you can name that the account does not fit. An empty string if there is none.
- `rooms`: one object for each of the three rooms you were given, each with:
  - `sub`: the room's name as the packet gives it, without `r/`;
  - `fits`: `true` if the account describes what happened there, `false` if it does not;
  - `instead`: one paragraph. Where the account fits, say which of its parts you saw in the room. Where it does not, say what the room did instead.
- `declarations`: one object for each sentence served to you under "The sentences in question", each with:
  - `id`: the declaration's id as the packet gives it (`T4-NNN` or `DNN`);
  - `sentence`: the sentence, copied exactly;
  - `stands`: `true` if the sentence stands under the rule you were given, `false` if it does not;
  - `why`: one sentence: what supports it (a count, a finding id, a setting fact), or which part of the rule it fails.
- `codes`: one object for each record served to you under "The records to code", each with:
  - `record`: the record's citation, copied exactly (`sub/cNNNN`);
  - `code`: exactly one of `M`, `MP`, `P` or `O`, by the code definitions you were given.

```json
{"reader": "...", "served": "<sha256 of account.md>", "claims": ["..."], "relations": ["A03 acts on P04"], "could_not_follow": ["quoted"], "unsupported": "...", "rooms": [{"sub": "...", "fits": true, "instead": "..."}], "declarations": [{"id": "T4-005", "sentence": "...", "stands": true, "why": "..."}], "codes": [{"record": "sub/c0001", "code": "M"}]}
END-OF-RETURN
```

A disagreement is never a verdict: your reading decides nothing.

After your line, write the end marker `END-OF-RETURN` on a line of its own. Confirm that you reached the end of the packet by writing that marker; a return without it is a partial return and is reissued.
