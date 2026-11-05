#!/usr/bin/env python3
"""build_pixels.py: the hourly pixel series per community, pixels.csv, which the aggregator's canvas step reads.

    python3 pixels-hourly/build_pixels.py                      (from data/; about 1 minute)
    python3 pixels-hourly/build_pixels.py --lists-from-raw24 raw24/
    python3 pixels-hourly/build_pixels.py --lists-from-raw24 raw24/ --activity pixels-hourly/ROOMS.tsv

One row per community per hour, hours -16 to 72 from the canvas opening (2017-03-31 16:00 UTC):
    sub, hour_since_open, px_in_region_any, px_by_pre_members, px_by_window_members

A placement counts for a community if it lands in the community's region: the union of the atlas
artworks that link to it. Regions overlap, and a contested pixel counts for every community that
claims it, so a rate per community is sound and a sum across communities is not.
    px_in_region_any      every placement in the region
    px_by_pre_members     placements there by people who posted in the subreddit in the 168 hours
                          before the opening
    px_by_window_members  placements there by people who posted in it from the opening to seven
                          days after the freeze
A member is matched to a placer by hashing the username as the record does,
base64(sha1(username)); the join runs one way only, from a known name to its placements.

INPUTS
    --record  pixels/place_tiles_sha1.csv   the pixel record (pixels/get_pixels.sh)
    --atlas   atlas/atlas_2017.json         the run's atlas
    --pre     pixels-hourly/_pre_progress.jsonl   one line per community: "sub" and "authors"
    --win     pixels-hourly/_win_progress.jsonl   (names) or "hashes"; the study's two lists are
                                                  not public (pixels-hourly/LINK.md)
The communities are those in the --pre list: the 763 of the census the lists were made for.

--lists-from-raw24 DIR first writes both lists from raw24 (DIR/<sub>.jsonl), hashes only, with the
study's rule: authors inside the span, less [deleted], [removed] and AutoModerator. Accounts
deleted since the study's collection are missing from a raw24 collected later, so its lists can
be a little shorter than the study's.

--activity ROOMS.tsv writes only the table of each room's activity in the week before the
opening, for the rooms in ROOMS.tsv, from the --pre list's counts: posts, comments and distinct
posters, the first record, and whether the room existed before the canvas or was founded
during the event (first record between opening and freeze). Stage D4 reads it as
data/activity-week-before.csv; it is written beside pixels.csv, and the handler's build_canvas.py
copies it, cut to the frame, into the run's DROPS/D4/data/. No usernames.

Made from the study's five steps (p1_keys.py to p5_emit.py, 27 August 2026; archived in
Layer A/61_sandboxes/Sandboxes/Gioia v28/_session-2026-08-27/device-scripts/), in one file:
the regions are drawn as p3_regions.py drew them, the counts made as p5_emit.py made them.
"""
import argparse, base64, csv, hashlib, json, os, sys, time
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.dirname(HERE)
OPEN = 1490976000; FRZ = 1491238800; END = FRZ + 7 * 86400; PRE0 = OPEN - 168 * 3600
EXCLUDE = {"[deleted]", "[removed]", "AutoModerator"}
# Four atlas links that name no census community, resolved by hand in the study: a typo, an r/
# folded into a name, a link that postdates the event, and a dormant namesake.
ALIAS = {"hyperlightdrifer": "hyperlightdrifter", "r2007scape": "2007scape",
         "protectthet": "ockytop", "chelsea": "chelseafc"}


def h64(name):
    return base64.b64encode(hashlib.sha1(name.encode()).digest()).decode()


def lists_from_raw24(raw, subs, pre_out, win_out):
    with open(pre_out, "w", encoding="utf-8") as fp, open(win_out, "w", encoding="utf-8") as fw:
        for s in subs:
            pre, win = set(), set(); n = posts = comments = 0; first = None
            p = os.path.join(raw, s + ".jsonl")
            if os.path.exists(p):
                for line in open(p, encoding="utf-8"):
                    r = json.loads(line); a = r.get("author"); t = int(r.get("created_utc", 0))
                    n += 1; first = t if first is None else min(first, t)
                    if PRE0 <= t < OPEN:
                        if r.get("kind") == "post" or "title" in r: posts += 1
                        else: comments += 1
                    if not a or a in EXCLUDE:
                        continue
                    if PRE0 <= t < OPEN: pre.add(a)
                    elif OPEN <= t <= END: win.add(a)
            fp.write(json.dumps({"sub": s, "have_file": int(os.path.exists(p)), "n_all": n,
                "posts_week_before": posts, "comments_week_before": comments,
                "distinct_posters_week_before": len(pre), "first_record_utc": first,
                "existed_before_window": first is not None and first < OPEN,
                "founded_during_event": first is not None and OPEN <= first <= FRZ,
                "hashes": sorted(h64(a) for a in pre)}) + "\n")
            fw.write(json.dumps({"sub": s, "hashes": sorted(h64(a) for a in win)}) + "\n")
    print("lists from raw24:", len(subs), "communities")


def activity(pre, rooms_tsv, out):
    P = {}
    for line in open(pre, encoding="utf-8"):
        d = json.loads(line); d.pop("authors", None); d.pop("hashes", None); P[d["sub"]] = d
    low = {k.lower(): k for k in P}
    rooms = [l.split("\t")[0] for l in open(rooms_tsv, encoding="utf-8").read().splitlines()[1:] if l.strip()]
    cols = ["posts_week_before", "comments_week_before", "distinct_posters_week_before",
            "first_record_utc", "existed_before_window", "founded_during_event"]
    miss = [r for r in rooms if r not in P and r.lower() not in low]
    if miss: sys.exit("no counts for %d rooms: %s" % (len(miss), ", ".join(miss[:10])))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["sub"] + cols)
        for r in sorted(rooms, key=str.lower):
            d = P[r if r in P else low[r.lower()]]
            w.writerow([r] + [int(d[c]) if isinstance(d[c], bool) else d[c] for c in cols])
    print("activity: %d rooms -> %s" % (len(rooms), out))


def read_list(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        d = json.loads(line)
        if "hashes" in d: out[d["sub"]] = d["hashes"]
        else:
            a = d.get("authors") or []
            out[d["sub"]] = [h64(x) for x in a] if isinstance(a, list) else []
    return out


def credits(path=os.path.join(DATA, "atlas", "credits_beyond_links.csv")):
    """atlas id -> communities credited by the canvas or a description, not by a link (atlas/README.md)"""
    out = {}
    if os.path.exists(path):
        for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
            if r["atlas_id"]:
                out.setdefault(str(r["atlas_id"]), []).append(r["sub"])
    return out


def regions(atlas, census):
    low = {s.lower(): s for s in census}
    for k, v in ALIAS.items():
        if v.lower() in low: low[k] = low[v.lower()]
    extra = credits(); sub_px = {}
    # regions no atlas entry outlines (data/atlas/derived_regions.json), for the communities credited with them
    dr = os.path.join(DATA, "atlas", "derived_regions.json")
    for reg in (json.load(open(dr, encoding="utf-8")).values() if os.path.exists(dr) else []):
        if reg["sub"].lower() in low:
            sub_px.setdefault(low[reg["sub"].lower()], []).append(
                np.array([y * 1000 + x for x, y in reg["pixels"]], dtype=np.int32))
    for e in json.load(open(atlas, encoding="utf-8")):
        names = list(e.get("links", {}).get("subreddit", [])) + extra.get(str(e["id"]), [])
        tgt = sorted({low[s.lower()] for s in names if s.lower() in low})
        for poly in (e["path"].values() if tgt else []):
            pts = [(int(round(p[0])), int(round(p[1]))) for p in poly]
            if len(pts) < 3: continue
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            x0, x1 = max(0, min(xs)), min(999, max(xs)); y0, y1 = max(0, min(ys)), min(999, max(ys))
            if x1 < x0 or y1 < y0: continue
            im = Image.new("1", (x1 - x0 + 1, y1 - y0 + 1), 0)
            ImageDraw.Draw(im).polygon([(p[0] - x0, p[1] - y0) for p in pts], fill=1)
            yy, xx = np.nonzero(np.array(im, dtype=bool))
            pid = (yy + y0).astype(np.int32) * 1000 + (xx + x0).astype(np.int32)
            for t in tgt: sub_px.setdefault(t, []).append(pid)
    subs = sorted(sub_px)
    P = [np.unique(np.concatenate(sub_px[s])) for s in subs]
    PID = np.concatenate(P); SID = np.concatenate([np.full(p.size, i, np.int16) for i, p in enumerate(P)])
    o = np.lexsort((SID, PID))
    return subs, PID[o], SID[o]


def read_record(path):
    T, X, Y, K = [], [], [], []
    try:
        import pandas as pd
        for ch in pd.read_csv(path, header=None, names=["ts", "h", "x", "y", "c"], chunksize=2_000_000,
                              dtype={"ts": np.int64, "h": str, "x": np.int32, "y": np.int32, "c": np.int16}):
            T.append(ch.ts.to_numpy()); X.append(ch.x.to_numpy()); Y.append(ch.y.to_numpy())
            K.append(ch.h.to_numpy().astype("S28"))
    except ImportError:
        t, x, y, k = [], [], [], []
        for r in csv.reader(open(path, newline="")):
            t.append(int(r[0])); k.append(r[1]); x.append(int(r[2])); y.append(int(r[3]))
        T, X, Y, K = [np.array(t)], [np.array(x)], [np.array(y)], [np.array(k, "S28")]
    return np.concatenate(T), np.concatenate(X), np.concatenate(Y), np.concatenate(K)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", default=os.path.join(DATA, "pixels", "place_tiles_sha1.csv"))
    ap.add_argument("--atlas", default=os.path.join(DATA, "atlas", "atlas_2017.json"))
    ap.add_argument("--pre", default=os.path.join(HERE, "_pre_progress.jsonl"))
    ap.add_argument("--win", default=os.path.join(HERE, "_win_progress.jsonl"))
    ap.add_argument("--lists-from-raw24", metavar="DIR")
    ap.add_argument("--out", default=os.path.join(HERE, "pixels.csv"))
    ap.add_argument("--activity", metavar="ROOMS_TSV")
    ap.add_argument("--activity-out", default=os.path.join(HERE, "activity-week-before.csv"))
    a = ap.parse_args(argv); t0 = time.time()
    if os.path.exists(a.pre):
        census = [json.loads(l)["sub"] for l in open(a.pre, encoding="utf-8")]
    elif a.lists_from_raw24:        # the communities of the census: CENSUS.csv, the sub column of the study's coder/census/MASTER-census.csv
        cp = os.path.join(HERE, "CENSUS.csv")
        census = [r["sub"] for r in csv.DictReader(open(cp, encoding="utf-8"))]
    else:
        sys.exit("no member lists: the study's are not public (pixels-hourly/LINK.md); pass --lists-from-raw24 raw24/")
    if a.lists_from_raw24:
        a.pre, a.win = a.pre + ".raw24", a.win + ".raw24"
        lists_from_raw24(a.lists_from_raw24, census, a.pre, a.win)
    if a.activity:
        activity(a.pre, a.activity, a.activity_out)
        return 0
    subs, pid_r, sid_r = regions(a.atlas, census); NS = len(subs)
    print("communities %d, with a region %d; pixel-community pairs %d over %d pixels"
          % (len(census), NS, pid_r.size, np.unique(pid_r).size), flush=True)
    cnt = np.bincount(pid_r, minlength=1_000_000).astype(np.int64)
    start = np.zeros(1_000_001, np.int64); np.cumsum(cnt, out=start[1:])
    ts, x, y, key = read_record(a.record)
    ok = (x >= 0) & (x < 1000) & (y >= 0) & (y < 1000); N = int(ok.sum())
    pid = y[ok].astype(np.int64) * 1000 + x[ok]
    hour = np.floor((ts[ok] / 1000.0 - OPEN) / 3600.0).astype(np.int64)
    uniq, uid = np.unique(key[ok], return_inverse=True); uid = uid.ravel().astype(np.int64)
    H0, H1 = int(hour.min()), int(hour.max()); NH = H1 - H0 + 1
    print("placements on the canvas %d, off it %d; hours %d to %d" % (N, int((~ok).sum()), H0, H1), flush=True)
    idx = {s: i for i, s in enumerate(subs)}

    def pairs(lists):
        P = []
        for s, hs in lists.items():
            if s not in idx or not hs: continue
            k = np.array(hs, "S28"); p = np.searchsorted(uniq, k); p2 = np.minimum(p, uniq.size - 1)
            hit = (p < uniq.size) & (uniq[p2] == k)
            P.append(p[hit].astype(np.int64) * NS + idx[s])
        return np.unique(np.concatenate(P)) if P else np.empty(0, np.int64)
    PP, WP = pairs(read_list(a.pre)), pairs(read_list(a.win))

    def isin(v, arr):
        p = np.searchsorted(arr, v); p2 = np.minimum(p, arr.size - 1)
        return (p < arr.size) & (arr[p2] == v)
    A = np.zeros(NS * NH, np.int64); B = np.zeros(NS * NH, np.int64); C = np.zeros(NS * NH, np.int64)
    for s in range(0, N, 2_000_000):
        e = min(s + 2_000_000, N); p = pid[s:e]; c = cnt[p]; tot = int(c.sum())
        if not tot: continue
        rep = np.repeat(np.arange(e - s, dtype=np.int64), c)
        pos = np.repeat(start[p], c) + np.arange(tot, dtype=np.int64) - np.repeat(np.cumsum(c) - c, c)
        sb = sid_r[pos].astype(np.int64); cell = sb * NH + (hour[s:e][rep] - H0)
        A += np.bincount(cell, minlength=NS * NH)
        pk = uid[s:e][rep] * NS + sb
        B += np.bincount(cell[isin(pk, PP)], minlength=NS * NH)
        C += np.bincount(cell[isin(pk, WP)], minlength=NS * NH)
    A, B, C = (M.reshape(NS, NH) for M in (A, B, C))
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sub", "hour_since_open", "px_in_region_any", "px_by_pre_members", "px_by_window_members"])
        for i, s in enumerate(subs):
            for h in range(NH):
                w.writerow([s, H0 + h, int(A[i, h]), int(B[i, h]), int(C[i, h])])
    print("in region %d, by pre members %d, by window members %d -> %s  (%.0f s)"
          % (A.sum(), B.sum(), C.sum(), a.out, time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
