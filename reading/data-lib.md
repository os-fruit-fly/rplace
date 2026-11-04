# Reading copy: data-lib

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/data-lib.md), SHA-256 `3e022e8978de1e7211705a5f189050c8d8880542a90d91c322c2ba898e2f4583`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# Shared by the collectors

- `10_collect_authors.py`: the arctic-shift collector for accounts, and the transport `12_collect_subreddits.py` reuses: pacing on observed latency, back-off on the API's time-outs, every failed request kept in a gaps ledger, only an empty page ends a walk. Its header gives the reason for each rule.
- `rplace_window.py`: the event window, the one place its boundaries are defined, with how they were derived from the pixel record.
