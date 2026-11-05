#!/usr/bin/env python3
"""Reorganise the Layer B venue corpora into Layer A's raw24 shape.

WHY THIS SHAPE. Layer A settled on a flat `<sub>.jsonl` + `<sub>.manifest.json`
per venue covering the whole 24-day span, records sorted by created_utc, with
`kind` kept and **`segment` dropped**. Its raw_policy states the reason:

    fields_dropped_by_us: ["segment (our own annotation, holding the superseded
    w1 boundary)"]
    segments_are_views.note: "filter on created_utc. Do NOT write these cuts to
    disk again - a boundary stored in a filename is a defect."

That is not cosmetic. Carrying `segment` cost this project real errors: the
placer-share table in atlas-vs-the-1801 was wrong by an order of magnitude
because a segment label was read as a time window, and the during-window record
count differs by 12,333 depending on which you trust. Dropping the field makes
the mistake unavailable.

OUTPUT   <out>/<sub>.jsonl          all records, sorted by created_utc
         <out>/<sub>.manifest.json  Layer A manifest schema

SCOPE    Venues the atlas already put in Layer A/30_data/raw24 are SKIPPED --
         19 of them. Layer A's copy is assembled from its own collection passes
         and is canonical; a second copy here would silently diverge. Pass
         --keep-atlas to override.

MEMORY   Segment files are concatenations of a sorted post run and a sorted
         comment run, so they are not globally sorted. Rather than load a whole
         venue, each file is split into monotone runs and heapq-merged. Peak
         memory is one record per run, not one venue.

RESUMABLE  A venue whose manifest already exists is skipped. Safe to run in
           slices, or under `timeout`, or repeatedly.

USAGE   python3 flatten_to_raw24.py --from-dir raw24/_collected --out raw24 [--atlas-raw24 DIR] [--limit N]
        (in data/: --from-dir reads 12_collect_subreddits.py's <sub>_<segment>.jsonl files directly;
         the study assembled from the zipped copies of those files, --root keeps that route)
"""
import argparse, collections, glob, heapq, json, os, sys, time, zipfile

SPAN_LO, SPAN_HI = 1490371200, 1492448400          # 24.04 days
OPEN, FRZ = 1490976000, 1491238800
WINDOW_REVISION = "w2-2026-07-29"
# Root is derived from this file's own location (<root>/Layer B/code/collect/),
# so the script runs the same from the Cowork bridge or from a normal terminal.
H = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "..", "..", ".."))
ZD = H + "/Layer B/data/venue_corpora/_incoming"
ASSEMBLED_FROM = "Layer B venue_corpora/_incoming"


def monotone_runs(fh):
    """Yield lists of (created_utc, raw_line) — each list already ascending."""
    run, last = [], -1
    for raw in fh:
        i = raw.find(b'"created_utc":')
        if i < 0:
            continue
        j = i + len(b'"created_utc":')
        while j < len(raw) and raw[j] in b' "':
            j += 1
        k = j
        while k < len(raw) and 48 <= raw[k] <= 57:
            k += 1
        if k == j:
            continue
        t = int(raw[j:k])
        if t < last:
            yield run
            run = []
        run.append((t, raw))
        last = t
    if run:
        yield run


def build(sub, members, out_dir):
    mpath = os.path.join(out_dir, f"{sub}.manifest.json")
    if os.path.exists(mpath):
        return None
    runs = []
    for zp, name in members:
        if zp is None:                      # a plain file from --from-dir
            with open(name, "rb") as fh:
                for r in monotone_runs(fh):
                    runs.append(r)
            continue
        with zipfile.ZipFile(zp).open(name) as fh:
            for r in monotone_runs(fh):
                runs.append(r)
    n = posts = comments = outside = 0
    first = last = None
    per_day = collections.defaultdict(lambda: {"posts": 0, "comments": 0})
    used = collections.Counter()
    outside_examples = []
    seen = set()
    tmp = os.path.join(out_dir, f".{sub}.jsonl.part")
    with open(tmp, "wb") as o:
        for t, raw in heapq.merge(*runs, key=lambda x: x[0]):
            try:
                r = json.loads(raw)
            except Exception:
                continue
            rid = r.get("id")
            if rid in seen:                     # a venue re-collected twice
                continue
            seen.add(rid)
            if t < SPAN_LO or t >= SPAN_HI:
                outside += 1
                if len(outside_examples) < 5:
                    outside_examples.append({"id": rid, "created_utc": t})
                continue
            kind = r.get("kind") or ("post" if r.get("title") is not None else "comment")
            r["kind"] = kind
            r.pop("segment", None)              # Layer A policy, see docstring
            used["during" if OPEN <= t < FRZ else ("pre" if t < OPEN else "after")] += 1
            d = str((t - SPAN_LO) // 86400)
            if kind == "post":
                posts += 1; per_day[d]["posts"] += 1
            else:
                comments += 1; per_day[d]["comments"] += 1
            if first is None:
                first = t
            last = t
            o.write(json.dumps(r, separators=(",", ":"), ensure_ascii=False).encode()
                    + b"\n")
            n += 1
    os.replace(tmp, os.path.join(out_dir, f"{sub}.jsonl"))
    man = {
        "sub": sub, "window_revision": WINDOW_REVISION,
        "after": SPAN_LO, "before": SPAN_HI,
        "window_utc": ["2017-03-24T16:00:00+00:00", "2017-04-17T17:00:00+00:00"],
        "span_days": 24.04, "n_records": n, "n_posts": posts, "n_comments": comments,
        "first_utc": first, "last_utc": last,
        "sources_used": dict(used), "sources_missing": [],
        "complete_span": bool(n), "records_outside_span": outside,
        "outside_examples": outside_examples,
        "per_day": {k: per_day[k] for k in sorted(per_day, key=int)},
        "segments_are_views": {
            "pre": [SPAN_LO, OPEN], "during": [OPEN, FRZ], "after": [FRZ, SPAN_HI],
            "note": "filter on created_utc. Do NOT write these cuts to disk again "
                    "- a boundary stored in a filename is a defect."},
        "raw_policy": {
            "fields_from_api": "kept byte-for-byte, unprojected",
            "fields_written_by_us": ["kind (only where the source file lacked it)"],
            "fields_dropped_by_us": ["segment (our own annotation, holding the "
                                     "superseded w1 boundary)"],
            "scrubbing": "none", "pseudonyms": "none", "projection": "none"},
        "assembled_from": ASSEMBLED_FROM,
        "assembled_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    json.dump(man, open(mpath, "w"))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None,
                    help="vault root; defaults to three levels above this file")
    ap.add_argument("--out", default=None)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--from-dir", default=None,
                    help="a folder of <sub>_<segment>.jsonl files written by 12_collect_subreddits.py")
    ap.add_argument("--atlas-raw24", default=None,
                    help="a raw24 folder whose venues are canonical and skipped (default: Layer A's, under --root)")
    ap.add_argument("--keep-atlas", action="store_true",
                    help="also assemble venues Layer A already holds "
                         "(off by default -- Layer A's copy is canonical)")
    a = ap.parse_args()
    global H, ZD
    if a.root:
        H = os.path.abspath(a.root)
        ZD = H + "/Layer B/data/venue_corpora/_incoming"
    global ASSEMBLED_FROM
    if a.from_dir:
        ASSEMBLED_FROM = "12_collect_subreddits.py output, " + os.path.basename(os.path.abspath(a.from_dir))
    if not a.out:
        a.out = H + "/Layer B/data/raw24"
    os.makedirs(a.out, exist_ok=True)

    # group members BY VENUE ACROSS ALL ZIPS -- 36 venues (AskReddit, funny,
    # politics, worldnews ...) were collected in slices and live in several.
    loc = collections.defaultdict(list)
    if a.from_dir:
        for p in sorted(glob.glob(os.path.join(a.from_dir, "*.jsonl"))):
            b = os.path.basename(p)
            if b.startswith("_"):
                continue
            loc[b[:-len(".jsonl")].rsplit("_", 1)[0]].append((None, p))
    for zp in ([] if a.from_dir else sorted(glob.glob(ZD + "/*.zip"))):
        try:
            names = zipfile.ZipFile(zp).namelist()
        except Exception:
            continue
        for m in names:
            if m.endswith(".jsonl"):
                loc[m.rsplit("_", 1)[0]].append((zp, m))
    # The atlas venues already exist in Layer A/30_data/raw24 in exactly this
    # shape. Assembling them again here would create a second, divergent copy of
    # the same venue -- Layer A's is assembled from its own collection passes
    # (prefill/pre/during/after) and is the canonical one. Skip them.
    atlas = {os.path.basename(q)[:-len(".manifest.json")].lower()
             for q in glob.glob((a.atlas_raw24 or H + "/Layer A/30_data/raw24") + "/*.manifest.json")}
    if not a.keep_atlas:
        drop = [s for s in loc if s.lower() in atlas]
        for s in drop:
            del loc[s]
        print(f"excluded {len(drop)} atlas venues held by Layer A: "
              f"{', '.join(sorted(drop))}", flush=True)
    print(f"{len(loc):,} venues to assemble -> {a.out}", flush=True)

    t0 = time.time(); done = recs = 0
    for sub in sorted(loc):
        r = build(sub, loc[sub], a.out)
        if r is None:
            continue
        done += 1; recs += r
        if done % 50 == 0:
            print(f"  {done:,} venues, {recs:,} records, {time.time()-t0:.0f}s",
                  flush=True)
        if a.limit and done >= a.limit:
            break
    print(f"PASS END +{done:,} venues, {recs:,} records, {time.time()-t0:.0f}s",
          flush=True)


if __name__ == "__main__":
    main()
