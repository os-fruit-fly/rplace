#!/usr/bin/env python3
"""
Collect the subreddit corpora round 1 discovered but nobody has ever fetched.

THE GAP THIS FILLS
------------------
Layer A holds 740 subreddit corpora, drawn from the atlas — communities that claimed
canvas territory. Round 1 read 5.8% of the during-window author records and found
728 subreddits carrying canvas writing, of which **331 are not among the 740**. They
include most of the faction venues: BlueCorner, SwedenOnPlace, EuropePlace, osuplace,
FightTheVoid, PlaceCurators, FlagAlliance, CKCrusaders, ParahumansPlace, RedCorner,
purplecorner, PlaceIreland, ColorDefenseForce, ockytop. The atlas could not see them
because they claimed no territory of their own — they were where the claiming was
organised.

Output matches Layer A's convention exactly — `<sub>_<segment>.jsonl` plus
`<sub>_<segment>.meta.json`, records verbatim with `kind` and `segment` injected — so
these corpora slot in beside the existing 740 rather than forming a parallel format.

THE SIZE TRAP, AND THE CAP
--------------------------
The discovered list is not all small faction subs. It also contains r/AskReddit,
r/AdviceAnimals, r/woahdude, r/oddlysatisfying, r/vexillology — base-rate giants
where round 1 found a handful of canvas records among thousands of unrelated ones.
Collecting those wholesale over a 25-day span would be gigabytes for four canvas
records, and it would be the same mistake as ranking hubs by volume.

So: work is ordered **smallest expected first** (by canvas writers ascending is the
wrong proxy; by whether the name looks canvas-native is unreliable; so the honest
mechanism is a hard record cap). Any subreddit exceeding CAP records is abandoned
mid-collection, its partial output deleted, and it is written to `_capped.jsonl` for
thread-level treatment instead — fetching only the specific threads known to carry
canvas records. A capped subreddit is a decision recorded, not a silent truncation.

RATE
----
The author sweep is running concurrently at conc 5. This runs at conc 2 so the two
together stay near the measured ceiling; the latency-adaptive pacer backs off on 422
either way. If the author sweep finishes first, conc can be raised.
"""
import argparse, collections, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))   # data/_lib: the shared transport
from importlib import import_module
_a = import_module("10_collect_authors")          # reuse the verified transport
Session, walk, segment_of, utc = _a.Session, _a.walk, _a.segment_of, _a.utc
SPAN_LO, SPAN_HI = _a.SPAN_LO, _a.SPAN_HI
PRE_START, OPEN, FRZ, AFTER_END = _a.PRE_START, _a.OPEN, _a.FRZ, _a.AFTER_END

CAP = 60_000            # records; above this the subreddit is a base-rate giant
# --cap overrides it, and --cap 0 removes it: the census communities, the 740 the atlas names among them,
# were collected uncapped (by collect_v6), so a giant such as r/leagueoflegends is collected whole.
BATCH = 10              # subreddits per checkpoint


def collect_one(sess, sub, outdir):
    t0 = time.time()
    g0 = len(sess.gaps)
    posts = walk(sess, "posts/search", SPAN_LO, SPAN_HI, subreddit=sub)
    if CAP and len(posts) > CAP:
        return {"sub": sub, "status": "capped", "n_posts": len(posts),
                "note": f"posts alone exceed CAP={CAP}"}
    comments = walk(sess, "comments/search", SPAN_LO, SPAN_HI, subreddit=sub)
    if CAP and len(posts) + len(comments) > CAP:
        return {"sub": sub, "status": "capped",
                "n_posts": len(posts), "n_comments": len(comments),
                "note": f"total exceeds CAP={CAP}"}

    recs = []
    for kind, obj in (("post", posts), ("comment", comments)):
        for r in obj.values():
            r["kind"] = kind
            r["segment"] = segment_of(r["created_utc"])
            recs.append(r)
    recs.sort(key=lambda r: (r["created_utc"], r["kind"], r["id"]))

    seg = collections.Counter(r["segment"] for r in recs)
    written = {}
    for s in ("pre", "during", "after"):
        rs = [r for r in recs if r["segment"] == s]
        p = os.path.join(outdir, f"{sub}_{s}.jsonl")
        tmp = p + ".part"
        with open(tmp, "w") as f:
            for r in rs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(tmp, p)
        written[s] = len(rs)
        meta = {
            "sub": sub, "segment": s,
            "after": {"pre": PRE_START, "during": OPEN, "after": FRZ}[s],
            "before": {"pre": OPEN, "during": FRZ, "after": AFTER_END}[s],
            "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "collector": "12_collect_subreddits rev-a", "api": _a.API,
            "limit": "auto", "projection": None,
            "n_posts": sum(1 for r in rs if r["kind"] == "post"),
            "n_comments": sum(1 for r in rs if r["kind"] == "comment"),
            "n_records": len(rs),
            "span_fetched": [SPAN_LO, SPAN_HI],
            "span_note": "one continuous fetch per subreddit, split by segment label",
            "source": "discovered by Layer B round 1; not in the atlas-derived 740",
        }
        json.dump(meta, open(os.path.join(outdir, f"{sub}_{s}.meta.json"), "w"), indent=1)

    # verification: the line counts on disk must equal what we думали we wrote
    bad = []
    for s, n in written.items():
        p = os.path.join(outdir, f"{sub}_{s}.jsonl")
        actual = sum(1 for _ in open(p))
        if actual != n:
            bad.append(f"{s}: wrote {n}, file has {actual}")
    wrong_sub = sorted({r.get("subreddit") for r in recs
                        if (r.get("subreddit") or "").lower() != sub.lower()})
    out_of_span = sum(1 for r in recs if not (SPAN_LO <= r["created_utc"] < SPAN_HI))
    card = {"sub": sub, "n_records": len(recs),
            "n_posts": sum(1 for r in recs if r["kind"] == "post"),
            "n_comments": sum(1 for r in recs if r["kind"] == "comment"),
            "pre": seg.get("pre", 0), "during": seg.get("during", 0),
            "after": seg.get("after", 0),
            "seconds": round(time.time() - t0, 1),
            "checks": {"line_mismatch": bad, "wrong_subreddit": wrong_sub,
                       "out_of_span": out_of_span,
                       "new_gaps": len(sess.gaps) - g0}}
    card["status"] = ("failed" if (bad or wrong_sub or out_of_span
                                  or card["checks"]["new_gaps"])
                      else ("empty" if not recs else "ok"))
    return card


def main():
    global CAP
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--conc", type=int, default=2)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--cap", type=int, default=CAP,
                    help="records above which a subreddit is set aside (default %(default)s); 0 = no cap")
    a = ap.parse_args()
    CAP = a.cap

    os.makedirs(a.out, exist_ok=True)
    lock = os.path.join(a.out, "_lock")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, f"{os.getpid()}\n".encode()); os.close(fd)
    except FileExistsError:
        sys.exit(f"another subreddit collector holds {lock} "
                 f"(pid {open(lock).read().strip()})")
    try:
        subs = [l.strip() for l in open(a.list) if l.strip()]
        if a.limit:
            subs = subs[:a.limit]
        ck = os.path.join(a.out, "_checkpoint.json")
        import hashlib
        list_sha = hashlib.sha256("\n".join(subs).encode()).hexdigest()[:16]
        prev = json.load(open(ck)) if os.path.exists(ck) else {}
        if prev.get("list_sha") and prev["list_sha"] != list_sha:
            sys.exit(f"{a.out} was started with another list ({prev.get('list')}, {prev['list_sha']}); "
                     f"this list is {list_sha}. Use a new --out, or remove {ck} to start this folder over.")
        start = prev.get("next_index", 0)
        idx_p = os.path.join(a.out, "_subs_index.jsonl")
        gaps_p = os.path.join(a.out, "_gaps.jsonl")
        cap_p = os.path.join(a.out, "_capped.jsonl")
        print(f"{len(subs):,} subreddits; resuming at {start:,}; conc={a.conc}; "
              f"span {utc(SPAN_LO)} -> {utc(SPAN_HI)}; CAP={CAP:,}", flush=True)
        t_run = time.time()
        from concurrent.futures import ThreadPoolExecutor
        for base in range(start, len(subs), BATCH):
            chunk = subs[base:base + BATCH]
            sess = Session(floor=0.0)
            t0 = time.time()
            with ThreadPoolExecutor(max_workers=a.conc) as ex:
                cards = list(ex.map(lambda s: collect_one(sess, s, a.out), chunk))
            with open(idx_p, "a") as f:
                for c in cards:
                    f.write(json.dumps(c, ensure_ascii=False) + "\n")
            with open(gaps_p, "a") as f:
                for g in sess.gaps:
                    f.write(json.dumps(g) + "\n")
            with open(cap_p, "a") as f:
                for c in cards:
                    if c["status"] == "capped":
                        f.write(json.dumps(c) + "\n")
            json.dump({"next_index": base + len(chunk), "list": os.path.basename(a.list),
                       "list_sha": list_sha}, open(ck, "w"))
            st = collections.Counter(c["status"] for c in cards)
            done = base + len(chunk)
            rate = (done - start) / max(1e-9, time.time() - t_run)
            print(f"[{done:>4}/{len(subs)}] ok={st.get('ok',0)} empty={st.get('empty',0)} "
                  f"capped={st.get('capped',0)} failed={st.get('failed',0)} "
                  f"recs={sum(c.get('n_records',0) for c in cards):,} "
                  f"{len(chunk)/(time.time()-t0):.2f} sub/s "
                  f"eta {(len(subs)-done)/max(rate,1e-9)/60:.0f} min", flush=True)
        print("SUBREDDIT SWEEP COMPLETE", flush=True)
    finally:
        os.unlink(lock)


if __name__ == "__main__":
    main()
