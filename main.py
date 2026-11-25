"""Warning label press: inks the label, proofreads it, presses it to output."""
STAMP = "onebug-11251142-wl3"
import json
import os
import shutil
from pathlib import Path

PRESS = Path(__file__).resolve().parent
SHEET_MAX = 160
LABEL = ("WARNING: this human believes the five-minute task will take five minutes. "
         "The manufacturer is not liable for the resulting evening.")


def proofread(text):
    print_line = text.strip()
    if len(print_line) > SHEET_MAX:
        return False, len(print_line)
    return bool(print_line), len(print_line)


def run_press():
    plate = PRESS / "entry.txt"
    inked, chars = proofread(plate.read_text(encoding="utf-8"))
    if inked:
        bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
        if bay:
            Path(bay).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(plate, Path(bay) / "entry.txt")
    print(json.dumps({"inked": inked, "stamp": STAMP, "chars": chars, "sheet_max": SHEET_MAX}))


if __name__ == "__main__":
    run_press()
