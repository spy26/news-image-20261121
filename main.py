"""news-image-20261121 entry: copy the built image to the output dir.

The image (entry.png, JPEG bytes, 1024x1024) sums up Saturday 21
November 2026's world news: Russian missiles landing in Poland (NATO
soil) lead, with the massive Kyiv strikes, the Wall Street AI sell-off
in correction territory, the COP31 talks running into overtime with no
deal, and Cyclone Akvan's landfall in Odisha in the strip below. This
program only copies those bytes to /output/entry.png (or
$MAKEFUN_OUTPUT_DIR/entry.png); it reads nothing else and uses no
network, so two runs write identical bytes.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if os.path.isfile(out_dir):
        print(f"error: output path {out_dir!r} is a file, not a directory",
              file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(SOURCE, "rb") as src:
        magic = src.read(2)
        if magic != b"\xff\xd8":
            print("error: entry.png is not a JPEG (bad magic bytes)",
                  file=sys.stderr)
            return 1
    shutil.copyfile(SOURCE, dest)
    size = os.path.getsize(dest)
    if size > 1048576:
        print(f"error: entry is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as f:
        want = hashlib.sha256(f.read()).hexdigest()
    with open(dest, "rb") as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if want != got:
        print("error: copied bytes differ from entry.png", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({size} bytes, sha256 {got[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
