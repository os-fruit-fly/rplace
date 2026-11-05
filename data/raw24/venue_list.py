#!/usr/bin/env python3
"""venue_list.py: which venues to collect whole: every subreddit a placer wrote in while the canvas was open.

    python3 raw24/venue_list.py [--placers venues-placers] [--out raw24/venues.txt]      (from data/)

Reads each `venues-placers/<sub>.jsonl` (build_aggregate.py's output) and keeps the subreddits holding at
least one placer's record in the 73 hours the canvas was open (2017-03-31 16:00 to 2017-04-03 17:00 UTC),
fewest placer records first. The study's frame, 24,082 venues, was drawn in stages; by its notes of 27 August
2026, 23,941 venues hold placer text inside the canvas window, which is what this rule selects.
"""
import argparse, glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(DATA, "_lib"))
from rplace_window import OPEN, FRZ  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--placers", default=os.path.join(DATA, "venues-placers"))
    ap.add_argument("--out", default=os.path.join(HERE, "venues.txt"))
    a = ap.parse_args(argv)
    keep = []
    for p in sorted(glob.glob(os.path.join(a.placers, "*.jsonl"))):
        n = 0
        for line in open(p, encoding="utf-8"):
            t = json.loads(line).get("created_utc")
            if isinstance(t, int) and OPEN <= t < FRZ:
                n += 1
        if n:
            m = json.load(open(p[:-len(".jsonl")] + ".manifest.json"))
            keep.append((m["n_records"], m["sub"]))
    keep.sort()
    open(a.out, "w").write("".join(s + "\n" for _, s in keep))
    print("%d venues with placer writing during the canvas -> %s" % (len(keep), a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
