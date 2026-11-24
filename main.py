"""wlbl-1125: human warning label; gate 160 chars."""

import json
import os

TAMPER = 160


def inspect_sticker(folder):
    crate = os.path.join(folder, "entry.txt")
    with open(crate, encoding="utf-8") as shrinkwrap:
        sticker = shrinkwrap.read().strip()
    if len(sticker) > TAMPER:
        raise SystemExit("label overflows the shrink wrap: %d chars" % len(sticker))
    if len(sticker) < 1:
        raise SystemExit("no label at all")
    return sticker


def apply_sticker(folder, sticker):
    shelf = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    if not os.path.isdir(shelf):
        os.makedirs(shelf, exist_ok=True)
    peel_point = os.path.join(shelf, "entry.txt")
    with open(peel_point, "w", encoding="utf-8", newline="\n") as adhesive:
        adhesive.write(sticker + "\n")
    return peel_point


stock = os.path.dirname(os.path.abspath(__file__))
sticker = inspect_sticker(stock)
print(json.dumps({"caution": sticker[:42], "printed": len(sticker), "lot": "every human", "peel_point": apply_sticker(stock, sticker)}))
