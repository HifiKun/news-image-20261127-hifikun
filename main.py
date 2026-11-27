#!/usr/bin/env python3
"""Entrypoint for the news-image-20261127 submission.

Takes the finished front page, ``entry.png``, and places a copy of it in
the directory the grader points at through the ``MAKEFUN_OUTPUT_DIR``
environment variable (``out`` when the variable is unset). Only the
Python standard library is used.

After copying, the destination file is checked against the source by
comparing their byte sizes, so a truncated or failed copy is never
reported as a success.
"""

import os
import shutil
import sys
from pathlib import Path


def resolve_output_dir() -> Path:
    """Return the output directory from the environment, as an absolute path."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    target = Path(raw).expanduser()
    if not target.is_absolute():
        target = Path.cwd() / target
    return target


def copy_front_page(source: Path, dest_dir: Path) -> Path:
    """Copy ``source`` into ``dest_dir`` (created if needed) and verify it."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / source.name
    shutil.copy2(source, dest)

    copied_bytes = dest.stat().st_size
    source_bytes = source.stat().st_size
    if copied_bytes != source_bytes:
        raise OSError(
            f"size mismatch after copy: source is {source_bytes} bytes "
            f"but destination is {copied_bytes} bytes"
        )
    return dest


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"error: {source} not found", file=sys.stderr)
        return 1

    try:
        dest = copy_front_page(source, resolve_output_dir())
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
