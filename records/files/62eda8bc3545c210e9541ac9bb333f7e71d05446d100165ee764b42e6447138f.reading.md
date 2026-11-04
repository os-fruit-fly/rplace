# The recall probes (stage E1)

Written at E1b-05, 27 October 2026. At every leg's close the harness asked five questions, to be answered from memory without opening a file:
- **goal:** the method question;
- **open:** the open distinctions, by slug;
- **rooms:** the last three rooms opened;
- **changed:** the element or theme changed, and why;
- **next:** the next comparison.

It stored the answers and the expected values in `out/_probe/NN-L.json`. There are 300 answer files, over 16 stages.

The sources:
- `audit-E1/probes_score.py` (E1a) gives each file's status as filed, and re-reads it by `probe.py`'s own rules.
- `audit-E1/probes_notes.py` (E1b-05) sorts each wrong re-read answer. It is a **note** where the head, the diary or the question files held the answer at the close. It is a **defect** where none did.
- **n/a**, where nothing on record could check the answer, is counted apart and never as recall.

I did not rerun `probe.py --score`. It writes into `_probe/`, which is the harness's, and it would score against the question files as they stand now, not as they stood at each close.

## As filed, and re-read

As filed, `probe.py` found "missing" for most answers, because 283 of the 300 answer files write `- **goal:** ...` in bold markdown, and its matching rule reads only a bare `goal: ...` line. The re-read strips the marks and applies the same rule to the same expected values. The filed score is the record; the re-read says how much of it was the parse.

| question | filed: right, wrong, missing, n/a | re-read: right | re-read: wrong, a note | re-read: wrong, a defect | n/a |
|---|---|---|---|---|---|
| goal | 17, 0, 283, 0 | 298 | 2 | 0 | 0 |
| open | 0, 0, 161, 139 | 26 | 135 | 0 | 139 |
| rooms | 6, 9, 158, 127 | 48 | 111 | 14 | 127 |
| changed | 0, 0, 63, 237 | 50 | 9 | 4 | 237 |
| next | 0, 0, 23, 277 | 11 | 12 | 0 | 277 |

**The test for a note.**
- goal: the head states the method question at every close.
- open: every expected slug is a file in `_questions/`.
- rooms: every expected room is named in the stage's diary.
- changed: an expected id is named in the stage's diary.
- next: the expected text's first six words are in the diary.

For rooms, the declared test read only the leg's own diary lines, and gave 24 notes and 101 defects. But the expected rooms repeat across legs that opened nothing: A1b-20 to A1b-26 all expect predators, Russiaclan and winnipegjets. The harness's value is therefore the last three rooms on record, not the leg's own. Read over the stage's diary up to the close, 111 are notes and 14 defects. Both counts are in `probes_notes.json`; its first run, the declared rule alone, is kept as `.superseded-1`.

## The recall failures that are defects (18)

These are misses that neither the head nor the diary nor the question files answered at the close:
- **rooms**, 14: B1b-01, B1b-03 to B1b-08, B1b-17 to B1b-19, B1b-19-p2, B1b-20, B1b-21 and D5a-33. At B1 the rooms were opened through `mem.py room` and recorded in the read log, but the diary names no room for these legs, so the head and the diary could not answer.
- **changed**, 4: D4a-06, D4a-07, D4a-08 and D6a-01. The diary of those legs names none of the expected ids.

All 18 are recall failures of the record, the memory a later leg reads. They are not faults in the work the legs did.

## By stage (re-read; rooms by the declared test)

Each cell gives right, wrong as a note, wrong as a defect, and n/a.

| stage | goal | open | rooms | changed | next |
|---|---|---|---|---|---|
| A1 | 57, 0, 0, 0 | 0, 0, 0, 57 | 19, 2, 36, 0 | 0, 0, 0, 57 | 0, 1, 0, 56 |
| B1 | 44, 0, 0, 0 | 0, 0, 0, 44 | 18, 1, 24, 1 | 15, 4, 0, 25 | 2, 4, 0, 38 |
| B2 | 12, 0, 0, 0 | 0, 0, 0, 12 | 0, 0, 0, 12 | 3, 0, 0, 9 | 0, 0, 0, 12 |
| B3 | 3, 0, 0, 0 | 0, 0, 0, 3 | 0, 0, 0, 3 | 0, 0, 0, 3 | 0, 1, 0, 2 |
| B4 | 12, 0, 0, 0 | 0, 0, 0, 12 | 0, 0, 0, 12 | 0, 0, 0, 12 | 0, 0, 0, 12 |
| C1 | 11, 0, 0, 0 | 0, 0, 0, 11 | 0, 0, 0, 11 | 2, 0, 0, 9 | 0, 0, 0, 11 |
| C2 | 7, 0, 0, 0 | 5, 2, 0, 0 | 6, 0, 1, 0 | 3, 3, 0, 1 | 0, 0, 0, 7 |
| C3 | 3, 0, 0, 0 | 0, 3, 0, 0 | 0, 0, 0, 3 | 2, 0, 0, 1 | 0, 0, 0, 3 |
| C4 | 1, 0, 0, 0 | 0, 1, 0, 0 | 0, 0, 0, 1 | 1, 0, 0, 0 | 0, 0, 0, 1 |
| C5 | 21, 0, 0, 0 | 17, 4, 0, 0 | 2, 0, 15, 4 | 11, 1, 0, 9 | 0, 0, 0, 21 |
| D1 | 1, 0, 0, 0 | 0, 1, 0, 0 | 0, 0, 0, 1 | 0, 0, 0, 1 | 0, 0, 0, 1 |
| D2 | 1, 0, 0, 0 | 0, 1, 0, 0 | 0, 0, 0, 1 | 0, 0, 0, 1 | 0, 0, 0, 1 |
| D3 | 57, 1, 0, 0 | 0, 58, 0, 0 | 1, 21, 16, 20 | 11, 0, 0, 47 | 7, 3, 0, 48 |
| D4 | 8, 0, 0, 0 | 3, 5, 0, 0 | 0, 0, 0, 8 | 2, 1, 3, 2 | 0, 0, 0, 8 |
| D5 | 42, 0, 0, 0 | 1, 41, 0, 0 | 2, 0, 9, 31 | 0, 0, 0, 42 | 0, 3, 0, 39 |
| D6 | 18, 1, 0, 0 | 0, 19, 0, 0 | 0, 0, 0, 19 | 0, 0, 1, 18 | 2, 0, 0, 17 |

**What the probes show.**
- The method question was carried at every close, and stated right in 298 of 300 re-read answers.
- The open distinctions and the last rooms were the weakest recall. Most of those misses (open 135, rooms 111) are notes: the record held what the session's memory did not.
- What the record lost is narrow: the rooms of 13 B1 legs and one D5 leg, and the changes of three D4 legs and the first D6 leg. The harness drew its expected values from the run's own files, so these were recorded somewhere, but not in the head or the diary, which a later leg reads first.
