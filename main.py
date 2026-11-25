#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes a single one-line out-of-office auto-reply (1-160 chars, no trailing
newline) to <MAKEFUN_OUTPUT_DIR>/entry.txt.

The joke: the auto-reply itself is on leave, so the message you're reading
is the temp covering for it -- a turn on the away message itself, rather
than the usual beach / inbox / limited-email lines.
"""

import os
import sys

ENTRY = "I'm out of office — my auto-reply is on leave too, so this is the temp."

MAX_CHARS = 160


def main() -> int:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print(
            f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("entry must not start or end with whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
