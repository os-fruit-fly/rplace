# Verified room archives

Finished rooms keep `STATE.json` and `validation/` in place. Their `run/` becomes `run.tar.zst`; `record/`, `brief/`, and `instrument/` become `materials.tar.zst`. Each archive passes a full test extraction against the source file hashes before the source directories are removed. Only verified, inactive rooms qualify. The verified count and live ledger remain intact.

`STATE.json` and `status.tsv` record each archive path, SHA-256, and byte size. The separate forkable case-lead snapshot remains under `_lead_sessions/` as a `.tar.zst` file, with its own hash.

To restore a room for review, run these from the yard root:

```
python3 -B _tools/archive_verified_run.py restore SUBREDDIT
python3 -B _tools/archive_verified_materials.py restore SUBREDDIT
```

Restore checks the saved hash and test extracts the archive. It retains each archive as a backup. To compress restored copies again, use the same commands with `archive` in place of `restore`.

`archive-all` processes eligible rooms one at a time, largest first.
