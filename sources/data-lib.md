# Shared by the collectors

- `10_collect_authors.py`: the arctic-shift collector for accounts, and the transport `12_collect_subreddits.py` reuses: pacing on observed latency, back-off on the API's time-outs, every failed request kept in a gaps ledger, only an empty page ends a walk. Its header gives the reason for each rule.
- `rplace_window.py`: the event window, the one place its boundaries are defined, with how they were derived from the pixel record.
