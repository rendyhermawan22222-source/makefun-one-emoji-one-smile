#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt and verifies it.
The chosen emoji is U+1F972 SMILING FACE WITH TEAR: a real smile with a
single tear — happy tears, the warmth of being moved by a kindness.
"""

import os
import sys

EMOJI = "\U0001F972"  # 🥲 SMILING FACE WITH TEAR
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    stripped = content.strip()
    if content != EMOJI + "\n":
        print(f"verification failed: entry.txt is {content!r}", file=sys.stderr)
        return 1
    if len(stripped) != 1:
        print(f"verification failed: expected one emoji, got {len(stripped)} chars",
              file=sys.stderr)
        return 1

    print(f"wrote {EMOJI} (U+1F972) to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
