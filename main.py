"""wl2: safety warning label entry; gate cap 160 chars, valid only when new text fits."""
import json
import os
import sys

LABEL_MAX = 160


def read_label(repo_dir):
    with open(os.path.join(repo_dir, "entry.txt"), encoding="utf-8") as fh:
        return fh.read().strip()


def write_label(out_dir, label):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(label)
    return path


def verify(label):
    return len(label) >= 1 and len(label) <= LABEL_MAX


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    text = read_label(root)
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    path = write_label(out, text)
    good = verify(text)
    print(json.dumps({"label": good, "chars": len(text), "where": path}))
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
