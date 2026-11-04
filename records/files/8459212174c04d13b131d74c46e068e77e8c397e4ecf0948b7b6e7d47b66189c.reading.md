# Notes, stage C4 (the model against the field)

## Order kept

- **The branch.** This leg runs in the branch claude-v43-1--C4-field, made from claude-v43-1 after C3c. The handler recorded no file overrides. Earlier validation belongs to the original inputs. This leg's checks are its own.
- **The startup packet.** I read `AGENT.md`, the head, the stage file, the last five diary lines and `validate.py --open C4` (0 errors, 0 warnings).
- **The field's arrival.** `field/` held `model.md` (1,206 words) and `check.md` (1,298 words). I logged its arrival before I opened it.
- **My own model first.** I read `model-C3.md` whole. I then wrote the three claims a view of the whole event could most easily overturn into `field-C4.md` and logged them. Only then did I open `field/model.md` and `field/check.md`, each whole.
- **The PI's message.** It carried my answers from the C3c interview fork, which I did not see, and J's ruling on language. The next section says which answers I used.

## The field's folder and the validator (QC4-001)

**The handler's placement error, corrected.**
- **The problem.** The stage C4 validator looks for the field at `out/field`, but the handler placed it at `field/` in the run root. As placed, `validate.py C4` reported that the field had not arrived, so the close would have failed.
- **The interim step.** I asked J (QC4-001). Under the assumption stated there, I made `out/field` a symbolic link to `../field`.
- **The answer.** The handler had put `field/` in the wrong place, and the validator was right. The handler asked me not to keep a link, because the close's capture compares real files, and to copy the two files into a real `out/field` folder.
- **What I did.** The guard refused to delete the link ("never delete a file"), so I renamed it to `out/_field-link-superseded-C4a`. I created `out/field` as a real folder and copied `field/model.md` and `field/check.md` into it unchanged. The sha256 sums match the originals: `5708dd9d…` and `b630db95…`. `field/` at the run root is untouched. From this point I read the field from `out/field`.
- **What rested on the assumption.** Only the validator's reading of the field. The text I read and quoted is byte-identical in both places. Snaps C4-move-relating-51 and C4-move-developing-52 were taken while `out/field` was the link.
- **Still open: QC4-002.** It asks whether the handler will remove the renamed link. Meanwhile it stays in place, and nothing reads it.

## The answers from the C3c fork: used, and set aside

- **Used:** "What I trust more passed tests that could have failed." I applied it to the field. Where the field and my rooms both showed a point, I trusted it. Where the field showed one episode against a count over hundreds of rooms, I trusted the count on the order (`field-C4.md`, list 3, item 5).
- **Used:** order between rooms as a problem for any organization whose work sits next to others' work on a surface no authority allocates. The two field entries both live between rooms, as that answer expects.
- **Set aside for a later stage:**
  - the correction to the C3a ruling on Felin and Zenger (the setting differs, not the subject);
  - the arrow from the move back to the goal, which would close the first loop;
  - Visibility returns;
  - the recalled source for Stigmergy.

  Each needs the literature or a test the stage C4 file does not allow. The head carries them.

## J's ruling on language

From this leg on I write descriptively. I use short sentences in the active voice and name the actor and the act. The new text in `field-C4.md`, in `model-C4.md`'s stage C4 section, and in the two amended declarations follows the ruling. The older text in the successor files is stage C3's, carried whole. Stage C5 rewrites the story under the ruling.

## What the leg did

- **The confrontation, in `field-C4.md`.**
  - Five mechanisms appear in both models (list 1).
  - Two mechanisms only the field shows were entered as tentative entries, and two others were not entered, each with its reason (list 2).
  - Six disagreements are listed, each marked substantive, a difference of setting, or a difference of subject (list 3).
- **One change the field forced, by move.** The prose of two declarations was amended: Standardization of output (a template does not make placers follow it) and Boundary work (most rooms, not every room, existed before the canvas). Each has a `tier_history.jsonl` line (now 480 lines). The move is relating or contrasting, snapped as C4-move-relating-51.
- **Three tentative entries from the field.** P21 and P22 are elements and A21 is an arrow. Each has `origin: from-field`, `status: tentative`, `field_support`, the field's firm or provisional mark and a `model/history.jsonl` line (now 88 lines). The move is developing or dropping working hypotheses, snapped as C4-move-developing-52.
- **Successor files written whole by script.**
  - `model-C4.md` (`c4_model_md.py`) bounds the closure sentence and prints two disagreements beside the model. It also writes in the dating limit and lists the tentative entries.
  - `structure-C4.md` (`c4_structure_md.py`) carries the two amended declarations.
  - `manifest-C4.txt` names both successors. `concept-C3.md` has no successor.
- **Findings.** None changed. Rule 14 was applied in the same act as each change. F-016's mapping line for Standardization of output already says that no one can make a placer follow the template. F-010 does not rest on the Boundary work sentence. F-006 and F-004 stand, with the field printed beside them.
- **Quotes.** I served 14 quotes from my rooms through `cite.py`. The field's quotes are given as `field/` gives them, with their thread and item ids.

## What the leg showed that I did not expect

- **The field's analyst and my rooms found the same limit of authority.** A member in the square says "I don't speak for all rainbownians, but I agree to these terms". A member in flyers says that one user's agreement "doesn't mean every lurker/person active on the sub agrees". The two analysts could not see each other's work.
- **Two of my declarations claimed more than my own evidence.** The field caught one sentence that my own model had already contradicted (every room existed before the canvas), and one that no test of mine had supported (the template as the strongest coordination). Both were in prose I wrote at stage C1 and never tested.
- **My rooms hold the follow-on work after hour 73.** They show a cleanup of a shared copy and an argument over keeping its scars. No theme of mine names this, and I had written that organizing for the canvas was over at hour 73.

## What I am sure of, and what I am not

- **Sure:**
  - The five agreements, each shown by a room and a field thread.
  - That the two amended sentences were wrong as written.
  - That none of the three claims I named was overturned.
- **Not sure:**
  - The field marks its explanations provisional, and the entries rest on them.
  - The room side of P22 was found by a keyword search, not by a theme.
  - A21's direction comes from one field episode.
  - The field read `structure-C3.md` only in part, so its silence on the rest of my tier is not agreement.
  - QC4-001 is unanswered.

## Slips, C4a

- **A date in local time.** The first version of `field-C4.md` dated the three claims 2026-10-15. The run's ledgers record UTC, and in UTC it was still 2026-10-14. The line was corrected.
- **The stage file's safe stops.** I checked for `.pause` after the first forced change and after the lists, but not after each list separately.
- **An edit and its check in one turn.** While I cut the head under 3,000 words, the last edit and its word count ran in one turn. The count and the link check ran again in a turn of their own.
- **A link where a copy was wanted.** I first linked `out/field` to the handler's folder. J asked for a real copy. The guard would not delete the link, so it is renamed and waits on QC4-002.

## The close-check, C4a

`python3 tools/validate.py C4`, run after the notes body, the handback and the interview brief, and before the head was rewritten:

```
stage C4:
  entries from the field: 3; successors: model-C4.md, structure-C4.md


0 errors (0 distinct shapes), 0 warnings
```

`done.sh C4 --cut interview` runs the same check at the close. Its report is in the leg's closing diary line.
