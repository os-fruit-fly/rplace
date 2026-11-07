# Historical context for this study

Updated 28 October 2026. These notes describe the recorded study. The contracts stay as published, and the notes authorize no run.

## Publications and closure

The run finished at E2b on 28 October 2026. Final publication `f27566528a5102d944c6ddc3d2e2e98b839cbab8` records all 18 stages closed. The earlier catalog baseline, `c070d990be88234ccd74101d4104160e71a28c5e`, ends during D3. Its accepted checkpoints and proofs are unchanged; later records name their own commits.

Final stage boundaries are D4a-08, D5a-41, D6a-18, E1e and E2b. D5b and D6b closed earlier, before further work in those stages. They stay available as historical legs; the final versions are the ones above. A checkpoint that also closes a stage appears once. [Read the completed run](study.html).

Every checkpoint displays its source commit and commit date. Saved-state dates have their own basis, or say "not recorded". A commit date marks when files were committed, and a stage closes on its own record. For D3c, the [checkpoint metadata](../history-evidence/D3c-checkpoint.json), [validation receipt](../history-evidence/D3c-validation.json) and [stage close marker](../history-evidence/D3-FINISHED.txt) support the dated status. The metadata hash matches the admitted checkpoint.

The [C5d-p2 account](../records/aggregator--claude-v43-1--C4-field--C5.C5d-p2.html), saved on 15 October, is partly superseded. D3 revised R01 and P05, bounded A21 and added fifteen candidates. The [D3 handback](../records/aggregator--claude-v43-1--C4-field--D3.D3c.html#07-handback-D3) records those revisions. The [final D6 account](../records/aggregator--claude-v43-1--C4-field--D6.D6a-18.html) and E1/E2 audits now document the later account and its limits.

## C4 and the Field agent's unfinished analysis

The Field agent had not finished its analysis when it supplied its reading and comments to C4. We clarified this on 29 October 2026. The saved C4 account calls the supplied material a field model; it was an interim reading, and the Field agent's full account was not complete. C4's close records how the aggregator handled the interim material.

[Read what that comparison changed](../stages/C4.html#what-v43-received). The saved files and their wording are intact. A comparison with the completed Field account is still pending.

## Models and lineage

The canonical instruction says to restore the original community coder on its recorded model and effort. This study used dated operational decisions, kept in [handler decision rows 155 and 248](../history-evidence/handler-decisions.tsv). On 15 October, J specified a gpt-5.6-sol resume followed by gpt-6.1-sol medium for the return. On 21 October, the re-check was corrected to gpt-6.1-sol medium; the earlier 5.6 launch wording was superseded. The [correction message](../history-evidence/D3-model-correction.md) records why `resumed_with` is unreliable as a description of an answer turn.

This website review inspected the D2 archives of all 14 shared communities. Each archive hash matched its custody receipt. In each, the source proof names the same archive used for the shared coding close; the native fork identifies its original session and boundary ordinal; and the D2 turn contexts record gpt-6.1-sol, medium. So `run.json`'s `model=6.1` describes these returns, and `resumed_with=5.6` is historical metadata that says nothing about the model of their answers.

The verified relationship for these communities is:

```text
Original coding close
  +-- R6: same original session continued for the local model
  +-- D2: fork from the coding close for the global return
        +-- D3: same D2 session ID in the re-check return record
```

D2 did not fork from R6, and the D2 branch never held the later R6 local model, although both share a source. The D3 records name gpt-6.1-sol and the same D2 session IDs. They omit effort; medium was prescribed, and this website review did not check it in those D3 transcripts. The review inspected the native histories of these 14 communities only, out of 705, and its findings cover those 14.

| Shared community | D2 source and native-turn evidence |
|---|---|
| r/PlaceNL | [Fork, source archive and turn settings](../history-evidence/PlaceNL-D2-lineage.json) |
| r/thenetherlands | [Fork, source archive and turn settings](../history-evidence/thenetherlands-D2-lineage.json) |
| r/cirkeltrek | [Fork, source archive and turn settings](../history-evidence/cirkeltrek-D2-lineage.json) |
| r/norge | [Fork, source archive and turn settings](../history-evidence/norge-D2-lineage.json) |
| r/norway | [Fork, source archive and turn settings](../history-evidence/norway-D2-lineage.json) |
| r/sweden | [Fork, source archive and turn settings](../history-evidence/sweden-D2-lineage.json) |
| r/greece | [Fork, source archive and turn settings](../history-evidence/greece-D2-lineage.json) |
| r/czech | [Fork, source archive and turn settings](../history-evidence/czech-D2-lineage.json) |
| r/armenia | [Fork, source archive and turn settings](../history-evidence/armenia-D2-lineage.json) |
| r/indonesia | [Fork, source archive and turn settings](../history-evidence/indonesia-D2-lineage.json) |
| r/placehearts | [Fork, source archive and turn settings](../history-evidence/placehearts-D2-lineage.json) |
| r/mindcrack | [Fork, source archive and turn settings](../history-evidence/mindcrack-D2-lineage.json) |
| r/blackmirror | [Fork, source archive and turn settings](../history-evidence/blackmirror-D2-lineage.json) |
| r/Goodboye | [Fork, source archive and turn settings](../history-evidence/Goodboye-D2-lineage.json) |

Table: The 14 shared communities: where each return came from, and the evidence for its model

These are selected metadata fields from the agents' records. Their member hashes and archive hashes identify the evidence kept. Reading them starts no agent.

## Instruction versions

The canonical source copies on this site are unchanged. Historical checkpoints keep the files they held. A stage-file hash shows that a file was saved; whether the aggregator read it, and whether a later instruction followed, needs other evidence.

### B1

Saved card SHA-256: `246c890d13c93007d92a27d29c76be7814281d946bc014c23dc96496e0819f97`. Current canonical card SHA-256: `a2b733dded3046ba611c65e979beb597ef8ef26e8b625dea28469a254219f8a0`. [Saved card](../history-evidence/saved-STAGE-B1-coding-third-order-scheme.md); [current canonical card](../sources/stage-B1.md). The saved hash is confirmed in all three shared B1 checkpoints.

### B4

Saved card SHA-256: `bb5cc6a5690643e43d2e8a600efb4c750fc499bf2c2abea6c90a94861f0e1357`. Current canonical card SHA-256: `7fb68adfcd6a1dab15368728559d3eb3c91162c555a8a69b26a53571dfd16ebe`. [Saved card](../history-evidence/saved-STAGE-B4-coding-adjudication-and-freeze.md); [current canonical card](../sources/stage-B4.md). The saved hash is confirmed in all three shared B4 checkpoints.

B1b-32, B1d-07 and B1e predate the 11 October amendment. B1e closed at 14:49Z; decision row 75 follows at 15:51Z. The 16:25Z delivery puts the gate and member re-check changes into the next B2 leg. Those later checks apply from B2 on, and B1 is judged under the rules it ran with.

Decision row 96 introduced B4's three-placement rule on 12 October. The 21:19Z handler delivery explicitly opens B4a-01 under that amendment. The saved notes record its use. A further ruling changed packet 4 from item 401 and sent earlier affected rulings back at B4a-05. So the B4a-07, B4b-p4 and B4c checkpoints follow those changes, and the delivered amendments are recorded in the handler's deliveries; the original stage-file hash does not include them. This review did not reconstruct every tool read of every intermediate leg.

Evidence: [exact selected decision rows](../history-evidence/handler-decisions.tsv), [dated handler deliveries](../history-evidence/amendment-deliveries.jsonl), and notes-B4 at the B4c source commit. The delivery's label can name the outgoing leg; its text names the incoming leg.

## Release access

These reading pages are public. Saved reading pages, their Markdown and JSONL downloads, and the PlaceNL example use the pixel stream's participant IDs: `base64(SHA1(username))`, case kept, with no salt. These are linkable pseudonyms. Quoted text and comment IDs can still lead back to the source record.

Original checkpoint bundles and transcripts are in the public research repository. Three legacy manual pages containing participant handles link to their originals in the research repository. Original research files keep their verified bytes. Reading manifests list the hashes of original sources apart from those of the derived copies.

Reviewer sign-in works in a browser. Online answers are limited to a private pilot. Chat Locally is available with a supported model account and runtime.

[Machine-readable history and evidence hashes](../history.json). New records extend the catalog; earlier checkpoint identities, accepted bundles and source recipes are unchanged. Additional runtime proofs, when available, name the exact executable tested.
