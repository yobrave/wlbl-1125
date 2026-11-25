"""wl6: label press. Ink one line of human safety advice onto the output."""
import json
import os
import sys
from pathlib import Path

STOCK = 160
PRESS = "wl6-label-press-r6"


def read_plate(root: Path) -> str:
    return root.joinpath("entry.txt").read_text(encoding="utf-8").strip()


def ink(level: int, body: str) -> bool:
    return 1 <= level <= STOCK and body != "" and not body.isspace()


def press(body: str, target: Path) -> str:
    target.mkdir(parents=True, exist_ok=True)
    sheet = target / "entry.txt"
    sheet.write_bytes(body.encode("utf-8"))
    return str(sheet)


def main():
    root = Path(__file__).resolve().parent
    body = read_plate(root)
    level = len(body)
    good = ink(level, body)
    where = press(body, Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")) if good else None
    print("VERDICT", json.dumps({"press": PRESS, "good": good, "level": level, "stock": STOCK, "where": where}))
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
