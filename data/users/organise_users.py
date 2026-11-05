#!/usr/bin/env python3
"""organise_users.py: the collected accounts into the layout the other scripts read.

    python3 users/organise_users.py [--from users/_collected] [--out users]      (from data/)

The collector (_lib/10_collect_authors.py) writes one file per account in rank folders,
`_collected/r000000-000999/<username>.jsonl`. This moves each into `users/<bb>/<username>.jsonl`, where
<bb> is the first two characters of the lowercased username (non-alphanumerics as "_", padded to two), the
layout the study's users/ store has and build_aggregate.py reads, and writes `users/_users.csv`: username,
path, bucket, bytes. Files are moved, not copied; a name already in place is left alone and reported.
Resumable.
"""
import argparse, csv, glob, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def bucket(name):
    s = "".join(c if c.isalnum() else "_" for c in name.lower())
    return (s + "__")[:2]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="src", default=os.path.join(HERE, "_collected"))
    ap.add_argument("--out", default=HERE)
    a = ap.parse_args(argv)
    moved = kept = 0
    for p in sorted(glob.glob(os.path.join(a.src, "r*-*", "*.jsonl"))):
        u = os.path.basename(p)[:-len(".jsonl")]
        d = os.path.join(a.out, bucket(u)); t = os.path.join(d, u + ".jsonl")
        if os.path.exists(t):
            kept += 1; continue
        os.makedirs(d, exist_ok=True); shutil.move(p, t); moved += 1
    rows = []
    for p in sorted(glob.glob(os.path.join(a.out, "??", "*.jsonl"))):
        rows.append((os.path.basename(p)[:-6], os.path.relpath(p, a.out), os.path.basename(os.path.dirname(p)), os.path.getsize(p)))
    with open(os.path.join(a.out, "_users.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["username", "path", "bucket", "bytes"]); w.writerows(rows)
    print("moved %d, already in place %d; %d accounts in %s/_users.csv" % (moved, kept, len(rows), a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
