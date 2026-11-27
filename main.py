#!/usr/bin/env python3
"""Place the front-page image where the grader expects it.

The image lives in this repository as entry.png (1024x1024, drawn
by draw_front.py). The grader runs this program with Python's
standard library only, in a container with no network, and expects
the image at $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png
when the variable is unset). This script just copies the file there.
"""
import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT = "/output"


def place_image() -> int:
    repo_dir = Path(__file__).resolve().parent
    source = repo_dir / IMAGE_NAME
    if not source.is_file():
        print(f"missing {IMAGE_NAME} beside {__file__}", file=sys.stderr)
        return 1
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / IMAGE_NAME
    target.write_bytes(source.read_bytes())
    print(f"placed {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(place_image())
