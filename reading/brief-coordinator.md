# Reading copy: brief-coordinator

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/brief-coordinator.md), SHA-256 `0276e9a00b18f373de3f949debda16e9e40b9a8f0db07d9eeaf4d32af9ca92ab`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# Brief coordinator runbook

1.  Inspect `python3 _tools/brief_queue.py list --limit 10`. Work only on queued ranks in that order.
2.  Keep at most six active writers. When one writer completes, handle that single rank immediately, then refill its slot. Do not wait for a batch.
3.  Writers are always fresh agents: `gpt-5.6-sol`, high reasoning, `fork_context:false`. Read `BRIEF-WRITER-PROMPT.md` afresh and state the exact `rooms/<subreddit>/brief` directory in the launch message.
4.  For writers: `prepare`, spawn, `start`. At completion run `finish --rank N --message ...`, inspect returned JSON, then close the accepted worker.
5.  A `finish` process exit of zero can still return `status: retry`. Retry only that rank with a fresh Sol writer. For an interrupted worker use `recover --rank N --error ...`, close it, then start a fresh writer.
6.  For a `work: harness` rank with zero pre-week items, run `prepare` and `finish` without a writer, then refill the resulting slot.
7.  Never use a resumed production writer. Never process event coding or excluded prior-run rooms. Do not use the legacy sync script while this moved yard is canonical.
8.  At completion, confirm 395 verified, no running or queued ranks, run the brief validation and reader tests with `PYTHONPATH=_tools python3 -m unittest _tools/test_brief_validation.py _tools/test_brief_reader.py`, then pause the scheduler.
