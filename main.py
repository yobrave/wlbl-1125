import filecmp
import json
import os

STICKER = "wl3-human"
ROOF = 160


def label(blob):
    for row in blob.replace("\r", "").split("\n"):
        if row.strip():
            return row
    return ""


def affix(line, root):
    shell = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(shell, exist_ok=True)
    tag = os.path.join(shell, "entry.txt")
    ink = line.encode("utf-8")
    with open(tag, "wb") as press:
        press.write(ink)
    with open(tag, "rb") as proof:
        if proof.read() != ink:
            raise IOError("label peeled off")
    return tag


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as panel:
    line = label(panel.read())

if not line.strip() or len(line) > ROOF:
    print(json.dumps({"label": "misprint", "size": len(line)}))
    raise SystemExit(1)
tag = affix(line, root)
echo = tag + ".echo"
with open(echo, "wb") as copier:
    copier.write(line.encode("utf-8"))
if not filecmp.cmp(tag, echo, shallow=False):
    raise IOError("echo differs")
os.remove(echo)
print(json.dumps({"label": "applied", "size": len(line), "roof": ROOF, "sticker": STICKER, "on": os.path.basename(tag)}))
