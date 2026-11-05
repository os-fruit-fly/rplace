#!/usr/bin/env python3
"""Build the per-artwork pixel-change flow and the 30-minute panel.

Self-contained: everything it reads lives in ./inputs, everything it writes goes
to the directory given by --out. No dependency on any other part of the rPlace
folder and none on session scratch.

    python3 build_artwork_flow.py assign  --out OUT
    python3 build_artwork_flow.py bodies  --out OUT --budget 11000000   # repeat
    python3 build_artwork_flow.py assemble --out OUT
    python3 build_artwork_flow.py index    --out OUT
    python3 build_artwork_flow.py panel    --out OUT

`run_all.sh` does all of it in order. `bodies` is resumable and prints its own
progress; repeat it until it reports 1473/1473. The split exists because the
device shell caps a call at 45 s; on an unconstrained machine the whole thing is
about two minutes.

INPUTS (see inputs/MANIFEST.json for sizes and SHA-256)
  pixel_record.npz      x, y, ts_ms, color, placer_uid -- 16,559,897 rows, the
                        published r/place 2017 placement record as parsed. Rows
                        are in record order. 3,256 have x or y >= 1000 and are
                        dropped here, leaving 16,556,641.
  placer_hashes.txt.gz  1,166,924 lines; line i is base64(sha1(username)) for
                        placer_uid == i. Unsalted, so hashing a known handle
                        reproduces the string and the join to a community roster
                        runs forwards only.
  atlas_membership.npz  the 1,473 placeAtlas-2017 polygons already rasterised:
                        memb_indices/memb_indptr is a CSR over the 1,000,000
                        pixels giving the artworks containing each; pixel_deg is
                        the row length; artwork_area the polygon areas;
                        pixel_primary the smallest-area containing artwork per
                        pixel, or -1.
  artworks.csv          artwork_id, name, subreddits, n_subreddits, area_px,
                        n_vertices, center.

GEOMETRY.  Flat pixel id is y*1000 + x throughout, y downwards, matching the
record and C4. The atlas rasterisation was checked against the final canvas
rather than assumed: Flag of Sweden reads darkblue 60% / yellow 20%, Flag of
Japan white 58% / red 21%, the Dutch area orange 34%.

OVERLAP.  Polygons overlap; 30.5% of covered pixels lie in two or more. A
placement is emitted ONCE PER containing artwork, so the flow has 23,058,857
rows against 16,556,641 placements, a 1.39x inflation. Every row carries
n_artworks, and is_primary marks the smallest containing polygon, so filtering
is_primary == 1 gives a true partition: 16,136,055 rows, one per placement that
falls inside any artwork.

DETERMINISM.  Every sort carries colour and placer as final tie-breaks, so the
output does not depend on the order the source file arrived in. This matters:
82,957 placements share a pixel and a millisecond with another one, and without
the tie-breaks two orderings of the identical record disagree by ~63 repaints
and ~155 restorations out of millions.

WHY THE BODIES ARE HEADERLESS.  gzip members concatenate, so
`cat header.gz body_i.gz` is a valid gzip stream. Each of the 23M rows is
therefore formatted exactly once and serves both the per-artwork file and the
long table.
"""
import argparse, csv, glob, gzip, json, os, shutil, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
# inputs/ sits beside code/, i.e. one level up from this file; fall back to a
# sibling inputs/ so the script also runs if it is moved next to the data.
INP = os.path.join(os.path.dirname(HERE), "inputs")
if not os.path.isdir(INP):
    INP = os.path.join(HERE, "inputs")
HEAD = "artwork_id,ts_ms,x,y,color,placer_uid,n_artworks,is_primary\n"
OPEN_TS = 1490976000          # 2017-03-31 16:00 UTC, hour 0 of the event
BIN = 1800                    # panel bin width, seconds


def load_record():
    z = np.load(os.path.join(INP, "pixel_record.npz"))
    x, y = z["x"], z["y"]
    ok = (x < 1000) & (y < 1000)
    return (y[ok].astype(np.int32) * 1000 + x[ok].astype(np.int32),
            z["ts_ms"][ok], z["color"][ok], z["placer_uid"][ok], x[ok], y[ok])


def load_atlas():
    z = np.load(os.path.join(INP, "atlas_membership.npz"))
    return (z["memb_indices"], z["memb_indptr"], z["artwork_area"],
            z["pixel_deg"], z["pixel_primary"])


def wdir(out):
    d = os.path.join(out, "_work")
    os.makedirs(d, exist_ok=True)
    return d


def stage_assign(out):
    t0 = time.time()
    W = wdir(out)
    pid, ts, col, uid, xs, ys = load_record()
    ind, ptr, area, deg, prim = load_atlas()
    dg = deg[pid].astype(np.int64)
    R = int(dg.sum())
    src = np.repeat(np.arange(pid.size, dtype=np.int32), dg)
    off = np.arange(R, dtype=np.int64) - np.repeat(np.cumsum(dg) - dg, dg)
    aid = ind[ptr[pid[src]] + off].astype(np.int16)
    # artwork, then time, then colour and placer as tie-breaks. The tie-breaks
    # are not cosmetic: 82,957 placements share a pixel and a millisecond with
    # another, so without them the row order -- and the repaint/revert/
    # restoration counts derived from it -- depend on the order the source file
    # happened to arrive in. With them the pipeline is order-invariant.
    o = np.lexsort((uid[src], col[src], ts[src], aid))
    s = src[o]
    np.save(W + "/o_aid.npy", aid[o]); np.save(W + "/o_ts.npy", ts[s])
    np.save(W + "/o_x.npy", xs[s]);    np.save(W + "/o_y.npy", ys[s])
    np.save(W + "/o_col.npy", col[s]); np.save(W + "/o_uid.npy", uid[s])
    np.save(W + "/o_nart.npy", dg[s].astype(np.int8))
    np.save(W + "/o_prim.npy", (aid[o] == prim[pid[s]]).astype(np.int8))
    a = aid[o]
    st = np.flatnonzero(np.r_[True, a[1:] != a[:-1]])
    np.save(W + "/o_start.npy", st.astype(np.int64))
    np.save(W + "/o_count.npy", np.diff(np.r_[st, a.size]).astype(np.int64))
    np.save(W + "/o_ids.npy", a[st].astype(np.int16))
    with gzip.open(W + "/header.gz", "wb", 6) as f:
        f.write(HEAD.encode())
    json.dump({"next": 0, "written": 0}, open(W + "/progress.json", "w"))
    print("placements %d  inside>=1 artwork %d  output rows %d (%.2fx)  %.0fs"
          % (pid.size, int((dg > 0).sum()), R, R / pid.size, time.time() - t0))


def stage_bodies(out, budget):
    t0 = time.time()
    W = wdir(out); B = W + "/bodies"
    os.makedirs(B, exist_ok=True)
    ids = np.load(W + "/o_ids.npy"); st = np.load(W + "/o_start.npy")
    cnt = np.load(W + "/o_count.npy")
    M = {k: np.load("%s/o_%s.npy" % (W, k), mmap_mode="r")
         for k in ("aid", "ts", "x", "y", "col", "uid", "nart", "prim")}
    p = json.load(open(W + "/progress.json")); k = p["next"]; done = 0
    while k < len(ids) and done < budget:
        i = int(ids[k]); a = int(st[k]); b = a + int(cnt[k])
        c = [np.asarray(M[n][a:b]) for n in ("aid", "ts", "x", "y", "col", "uid", "nart", "prim")]
        wid = ("U5", "U13", "U3", "U3", "U2", "U7", "U1", "U1")
        buf = c[0].astype(wid[0])
        for arr, w in zip(c[1:], wid[1:]):
            buf = np.char.add(np.char.add(buf, ","), arr.astype(w))
        with gzip.open("%s/b%04d.gz" % (B, i), "wb", 5) as f:
            f.write(("\n".join(buf.tolist()) + "\n").encode())
        done += b - a; k += 1
    json.dump({"next": k, "written": p["written"] + done}, open(W + "/progress.json", "w"))
    print("artworks %d/%d   rows this call %d   total %d   %.0fs"
          % (k, len(ids), done, p["written"] + done, time.time() - t0))


def stage_assemble(out):
    t0 = time.time()
    W = wdir(out)
    d = os.path.join(out, "by_artwork"); os.makedirs(d, exist_ok=True)
    hdr = open(W + "/header.gz", "rb").read()
    files = sorted(glob.glob(W + "/bodies/b*.gz"))
    for fn in files:
        i = int(os.path.basename(fn)[1:5])
        with open("%s/aw%04d.csv.gz" % (d, i), "wb") as o:
            o.write(hdr)
            with open(fn, "rb") as f:
                shutil.copyfileobj(f, o, 1 << 20)
    with open(os.path.join(out, "atlas_flow_all.csv.gz"), "wb") as o:
        o.write(hdr)
        for fn in files:
            with open(fn, "rb") as f:
                shutil.copyfileobj(f, o, 1 << 20)
    print("assembled %d per-artwork files and the long table  %.0fs"
          % (len(files), time.time() - t0))


def stage_index(out):
    W = wdir(out)
    with gzip.open(os.path.join(INP, "placer_hashes.txt.gz"), "rt") as f:
        hs = [l.rstrip("\n") for l in f]
    with gzip.open(os.path.join(out, "placers.csv.gz"), "wt", 6, newline="") as f:
        f.write("placer_uid,username_sha1_b64\n")
        for i, h in enumerate(hs):
            f.write("%d,%s\n" % (i, h))
    meta = list(csv.DictReader(open(os.path.join(INP, "artworks.csv"))))
    ids = np.load(W + "/o_ids.npy"); st = np.load(W + "/o_start.npy")
    cnt = np.load(W + "/o_count.npy"); ts = np.load(W + "/o_ts.npy")
    prim = np.load(W + "/o_prim.npy"); uid = np.load(W + "/o_uid.npy")
    _, _, area, _, _ = load_atlas()
    rows = []
    for k, i in enumerate(ids):
        a, b = st[k], st[k] + cnt[k]
        rows.append(dict(meta[i], placements=int(cnt[k]),
                         placements_primary=int(prim[a:b].sum()),
                         placements_per_px=round(float(cnt[k]) / max(1, area[i]), 2),
                         distinct_placers=int(np.unique(uid[a:b]).size),
                         first_ts_ms=int(ts[a]), last_ts_ms=int(ts[b - 1]),
                         file="by_artwork/aw%04d.csv.gz" % i))
    with open(os.path.join(out, "artworks_index.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print("index %d rows, placers %d" % (len(rows), len(hs)))


BASE = ["placements", "repaints", "reverts", "restorations", "placers",
        "pixels_touched", "net_change_px"]
MEAS = BASE + [b + "_primary" for b in BASE]


def stage_panel(out):
    t0 = time.time()
    pid, ts_ms, col, uid, _, _ = load_record()
    ts = ts_ms // 1000
    ind, ptr, area, deg, prim = load_atlas()
    o = np.lexsort((uid, col, ts, pid))             # pixel, time, colour, placer
    pid, col, uid, ts = pid[o], col[o], uid[o], ts[o]
    # flags on the PIXEL's own global sequence, so no bin boundary distorts them
    hasprev = np.zeros(pid.size, bool); hasprev[1:] = pid[1:] == pid[:-1]
    repaint = np.zeros(pid.size, bool); repaint[1:] = hasprev[1:] & (col[1:] == col[:-1])
    revert = ~repaint
    rest = np.zeros(pid.size, bool)
    rest[2:] = ((pid[2:] == pid[:-2]) & (pid[1:-1] == pid[:-2]) &
                (col[2:] == col[:-2]) & (col[1:-1] != col[:-2]))
    NB = int((ts.max() - OPEN_TS) // BIN) + 1
    NA = area.size
    b = np.clip((ts - OPEN_TS) // BIN, 0, NB - 1).astype(np.int32)
    print("placements %d  bins %d  repaints %d  reverts %d  restorations %d"
          % (pid.size, NB, repaint.sum(), revert.sum(), rest.sum()), flush=True)
    ob = np.lexsort((uid, col, ts, pid, b))         # bin-major, pixel-major inside
    pid, col, uid = pid[ob], col[ob], uid[ob]
    repaint, revert, rest, b = repaint[ob], revert[ob], rest[ob], b[ob]
    st = np.r_[np.searchsorted(b, np.arange(NB)), b.size]
    cube = np.zeros((NA, NB, len(MEAS)), np.int64)
    state = np.zeros(1000000, np.uint8)
    for k in range(NB):
        a, e = int(st[k]), int(st[k + 1])
        if a == e:
            continue
        P, C, U = pid[a:e], col[a:e], uid[a:e]
        d = deg[P].astype(np.int64)
        src = np.repeat(np.arange(P.size), d)
        off = np.arange(d.sum()) - np.repeat(np.cumsum(d) - d, d)
        aid = ind[ptr[P[src]] + off].astype(np.int64)
        isp = aid == prim[P[src]]
        uq, first = np.unique(P[::-1], return_index=True)
        endc = C[::-1][first]
        dd = deg[uq].astype(np.int64)
        s2 = np.repeat(np.arange(uq.size), dd)
        o2 = np.arange(dd.sum()) - np.repeat(np.cumsum(dd) - dd, dd)
        aid2 = ind[ptr[uq[s2]] + o2].astype(np.int64)
        isp2 = aid2 == prim[uq[s2]]
        ch = (endc != state[uq]).astype(float)[s2]
        for sc, (sel, sel2) in enumerate(((np.ones(aid.size, bool), np.ones(aid2.size, bool)),
                                          (isp, isp2))):
            j = sc * len(BASE); A_, A2_ = aid[sel], aid2[sel2]
            cube[:, k, j + 0] += np.bincount(A_, minlength=NA)
            for n, arr in ((1, repaint), (2, revert), (3, rest)):
                cube[:, k, j + n] += np.bincount(A_, weights=arr[a:e][src][sel],
                                                 minlength=NA).astype(np.int64)
            key = A_ * 1_200_000 + U[src][sel].astype(np.int64)
            cube[:, k, j + 4] += np.bincount(np.unique(key) // 1_200_000, minlength=NA)
            cube[:, k, j + 5] += np.bincount(A2_, minlength=NA)
            cube[:, k, j + 6] += np.bincount(A2_, weights=ch[sel2], minlength=NA).astype(np.int64)
        state[uq] = endc
    for j in (0, len(BASE)):
        assert (cube[:, :, j] == cube[:, :, j + 1] + cube[:, :, j + 2]).all(), \
            "placements != repaints + reverts at scope %d" % j
    print("identity holds in all %d cells, both scopes" % (NA * NB))
    idx = {int(r["artwork_id"]): r for r in
           csv.DictReader(open(os.path.join(out, "artworks_index.csv")))}
    cols = (["artwork_id", "bin", "bin_start_ms", "hours_from_open", "name",
             "subreddits", "area_px", "placers_total"] + MEAS)
    with gzip.open(os.path.join(out, "panel_30min.csv.gz"), "wt", 6, newline="") as f:
        w = csv.writer(f); w.writerow(cols)
        for i in range(NA):
            r = idx[i]; nm = r["name"].replace('"', "'")
            for k in range(NB):
                w.writerow([i, k, (OPEN_TS + k * BIN) * 1000, round(k * BIN / 3600, 2),
                            nm, r["subreddits"], int(area[i]), int(r["distinct_placers"])]
                           + [int(v) for v in cube[i, k]])
    np.savez_compressed(os.path.join(out, "panel_30min.npz"),
                        cube=cube.astype(np.int32), measures=np.array(MEAS),
                        artwork_id=np.arange(NA), bin=np.arange(NB),
                        bin_start_ms=((OPEN_TS + np.arange(NB) * BIN) * 1000).astype(np.int64),
                        hours_from_open=(np.arange(NB) * BIN / 3600).astype(np.float32),
                        area_px=area,
                        artwork_name=np.array([idx[i]["name"] for i in range(NA)]),
                        subreddits=np.array([idx[i]["subreddits"] for i in range(NA)]),
                        placers_total=np.array([int(idx[i]["distinct_placers"])
                                                for i in range(NA)]))
    print("panel %d x %d x %d  %.0fs" % (NA, NB, len(MEAS), time.time() - t0))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["assign", "bodies", "assemble", "index", "panel"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--budget", type=int, default=11_000_000)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    if a.stage == "bodies":
        stage_bodies(a.out, a.budget)
    else:
        {"assign": stage_assign, "assemble": stage_assemble,
         "index": stage_index, "panel": stage_panel}[a.stage](a.out)
