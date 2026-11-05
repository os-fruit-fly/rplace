#!/usr/bin/env python3
"""Build aggregate/ -- venues assembled from PLACER content, not venue sweeps.

TWO VENUE CORPORA, AND THEY ANSWER DIFFERENT QUESTIONS.

  raw24/      what a community said. Every record by every author, collected by
              sweeping the subreddit. 23,367 venues.
  aggregate/  what the PLACERS said, wherever they said it. Every record written
              by one of the 1,101,801 placer accounts, grouped by the subreddit
              it landed in. Built from users/, not from a venue sweep.

The second reaches places the first cannot: a placer writing in a subreddit
nobody ever collected still shows up here. It is also the honest denominator for
anything placer-side -- raw24 mixes placers with the whole community, which is
exactly the dilution the atlas note is about.

FORMAT matches raw24 exactly, so the two are comparable file for file:
`<sub>.jsonl` sorted by created_utc plus `<sub>.manifest.json`, `kind` kept and
`segment` dropped.

MEMORY AND DISK. Grouping ~19M records by subreddit cannot be held at once, and one open
file handle per subreddit exceeds the fd limit. So: pass 1 shards every record
into SHARDS buckets by hash(subreddit); pass 2 loads one shard at a time,
groups, sorts, writes, then DELETES that shard. Peak memory is one shard; peak
disk is roughly one copy of the corpus rather than two.

SOURCES. users/<bb>/<username>.jsonl, the flat layout. Run flatten_users.py
first; this refuses to run against the old sweep/ + tail/ trees rather than
silently building an aggregate from half the accounts.

USAGE   python3 build_aggregate.py            # full build, resumable per shard
        python3 build_aggregate.py --shards 96
        (in data/: --users defaults to data/users, --out to data/venues-placers)
"""
import argparse, collections, glob, hashlib, json, os, shutil, sys, time, zipfile

SPAN_LO, SPAN_HI = 1490371200, 1492448400
OPEN, FRZ = 1490976000, 1491238800
DATA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))     # data/
H = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "..", "..", ".."))
USERS = H + "/Layer B/data/users"
OUT = H + "/Layer B/data/aggregate"
TMP = H + "/Layer B/data/aggregate/_shards"


def sources():
    """The flat users/ layout written by flatten_users.py -- users/<bb>/<name>.jsonl.
    Run that first; this reads nothing from the old sweep/ and tail/ trees."""
    n = 0
    for p in sorted(glob.glob(USERS + "/??/*.jsonl")):
        n += 1
        yield ("f", p, None)
    if n == 0:
        sys.exit("no users/<bb>/<name>.jsonl found in %s -- run users/organise_users.py first" % USERS)


def shard_pass(nshards):
    done = os.path.join(TMP, "_pass1.done")
    if os.path.exists(done):
        print("pass 1 already complete", flush=True); return
    os.makedirs(TMP, exist_ok=True)
    fhs = [open(os.path.join(TMP, "s%03d.jsonl" % i), "w", encoding="utf8")
           for i in range(nshards)]
    n = kept = 0; nextmark = 2000000
    t0 = time.time(); zf = None; zname = None
    for kind, path, member in sources():
        if kind == "f":
            fh = open(path, "rb")
        else:
            if path != zname: zf = zipfile.ZipFile(path); zname = path
            fh = zf.open(member)
        with fh:
            for raw in fh:
                n += 1
                try: r = json.loads(raw)
                except Exception: continue
                t = r.get("created_utc")
                if not isinstance(t, int) or t < SPAN_LO or t >= SPAN_HI: continue
                sub = r.get("subreddit")
                if not sub: continue
                r["kind"] = r.get("kind") or ("post" if r.get("title") is not None
                                              else "comment")
                r.pop("segment", None)
                i = int(hashlib.md5(sub.lower().encode()).hexdigest()[:8], 16) % nshards
                fhs[i].write(json.dumps(r, separators=(",", ":"),
                                        ensure_ascii=False) + "\n")
                kept += 1
        if n >= nextmark:
            nextmark += 2000000
            print(f"  pass1 {n:,} records read, {kept:,} kept, "
                  f"{time.time()-t0:.0f}s", flush=True)
    for f in fhs: f.close()
    open(done, "w").write(str(kept))
    print(f"pass 1 done: {n:,} read, {kept:,} in window, {time.time()-t0:.0f}s",
          flush=True)


def emit_pass(nshards):
    t0 = time.time(); venues = 0; recs = 0
    for i in range(nshards):
        mark = os.path.join(TMP, "s%03d.done" % i)
        sp = os.path.join(TMP, "s%03d.jsonl" % i)
        if os.path.exists(mark) or not os.path.exists(sp): continue
        by = collections.defaultdict(list)
        with open(sp, encoding="utf8") as fh:
            for line in fh:
                try: r = json.loads(line)
                except Exception: continue
                by[r["subreddit"]].append((r["created_utc"], line))
        rows_n = list(by)
        for sub, rows in by.items():
            rows.sort(key=lambda x: x[0])
            seen = set(); out = []
            posts = comments = 0
            per_day = collections.defaultdict(lambda: {"posts": 0, "comments": 0})
            for t, line in rows:
                rid = None
                try: rid = json.loads(line).get("id")
                except Exception: pass
                if rid in seen: continue
                seen.add(rid); out.append(line)
                k = "post" if '"kind":"post"' in line else "comment"
                d = str((t - SPAN_LO) // 86400)
                if k == "post": posts += 1; per_day[d]["posts"] += 1
                else: comments += 1; per_day[d]["comments"] += 1
            if not out: continue
            safe = sub.replace("/", "_")
            with open(os.path.join(OUT, safe + ".jsonl"), "w", encoding="utf8") as o:
                o.writelines(out)
            first = rows[0][0]; last = rows[-1][0]
            json.dump({
                "sub": sub, "built_from": "users/ (placer archives)",
                "window_revision": "w2-2026-07-29",
                "after": SPAN_LO, "before": SPAN_HI, "span_days": 24.04,
                "n_records": len(out), "n_posts": posts, "n_comments": comments,
                "first_utc": first, "last_utc": last,
                "per_day": {k2: per_day[k2] for k2 in sorted(per_day, key=int)},
                "segments_are_views": {"pre": [SPAN_LO, OPEN], "during": [OPEN, FRZ],
                    "after": [FRZ, SPAN_HI],
                    "note": "filter on created_utc. Do NOT write these cuts to disk."},
                "raw_policy": {"fields_from_api": "kept byte-for-byte, unprojected",
                    "fields_written_by_us": ["kind (only where the source lacked it)"],
                    "fields_dropped_by_us": ["segment"],
                    "scope": "records by placer accounts only -- NOT the whole venue"},
                "assembled_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }, open(os.path.join(OUT, safe + ".manifest.json"), "w"))
            venues += 1; recs += len(out)
        open(mark, "w").write("ok")
        by = None
        try: os.remove(sp)          # free it now, not after all 64 are done
        except OSError: pass
        print(f"  shard {i+1}/{nshards}: {len(rows_n):,} venues, "
              f"{venues:,} total, {time.time()-t0:.0f}s", flush=True)
    print(f"pass 2 done: {venues:,} venues, {recs:,} records", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shards", type=int, default=64)
    ap.add_argument("--keep-shards", action="store_true")
    ap.add_argument("--users", default=os.path.join(DATA, "users"), help="users/<bb>/<name>.jsonl")
    ap.add_argument("--out", default=os.path.join(DATA, "venues-placers"))
    a = ap.parse_args()
    global USERS, OUT, TMP
    USERS, OUT = os.path.abspath(a.users), os.path.abspath(a.out)
    TMP = os.path.join(OUT, "_shards")
    os.makedirs(OUT, exist_ok=True)
    shard_pass(a.shards)
    emit_pass(a.shards)
    if not a.keep_shards and os.path.isdir(TMP):
        shutil.rmtree(TMP)
        print("removed temporary shards", flush=True)


if __name__ == "__main__":
    main()
