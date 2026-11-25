#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry.

Writes one line, in the voice of the Moon answering four billion years of
wishes, howls and 2 a.m. promises, to /output/entry.txt.

Standard library only: the grading sandbox is plain python:3.13-slim.
"""

import os

ENTRY = (
    "I've heard every wish, howl, and 2 a.m. promise for four billion years, "
    "and my answer is: no \u2014 the only wish that ever came true was the asteroid."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 240:
        raise SystemExit("entry must be 1 to 240 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
