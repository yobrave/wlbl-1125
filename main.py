"""Warning label for humans, affixed with industrial glue."""
import os
import sys

LABEL = ("WARNING: Ships with unearned confidence. Do not install "
         "updates before 10 a.m.; may argue with mirrors and lose to "
         "them.")
STICKER = "wl2"
GLUE = "industrial"
SURFACE = "forehead"


def affix(base):
    base = base or "output"
    os.makedirs(base, exist_ok=True)
    p = os.path.join(base, "entry.txt")
    raw = (LABEL + "\n").encode("utf-8")
    with open(p, "wb") as f:
        f.write(raw)
    with open(p, "rb") as f:
        return f.read().decode("utf-8").strip()


stuck = affix(os.environ.get("MAKEFUN_OUTPUT_DIR"))
if stuck != LABEL:
    sys.exit("label peeling, re-glue")
print(STICKER, GLUE, len(stuck), "chars affixed")
print("surface:", SURFACE, "warranty intact")
