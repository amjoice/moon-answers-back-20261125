#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry.

One line in the Moon's own voice, answering four billion years of wishes,
howls and 2 a.m. promises, written to /output/entry.txt.

Standard library only: the grading sandbox is plain python:3.13-slim.
"""

import os

ENTRY = (
    "I've heard every wish, howl, and 2 a.m. promise for four billion years, "
    "and my answer is: no \u2014 the only wish that ever came true was the asteroid."
)


def write_entry(entry: str, out_dir: str) -> str:
    """Validate the line, write it to <out_dir>/entry.txt, and return the path."""
    if not 1 <= len(entry) <= 240:
        raise SystemExit("entry must be 1 to 240 characters")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(ENTRY, out_dir)


if __name__ == "__main__":
    main()
