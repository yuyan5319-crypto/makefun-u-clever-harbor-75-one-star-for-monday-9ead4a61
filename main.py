#!/usr/bin/env python3
"""Write a one-star review of Monday, as if Monday were a restaurant.

The review is a single line of plain text, at most 25 words. It is
written to the directory named by MAKEFUN_OUTPUT_DIR (default /output)
as entry.txt, which is where the grader reads it.

The line is checked before it is written: it must be one line, 1 to
25 words, and 1 to 180 characters, matching the competition's gate.
"""

import os

REVIEW = (
    "Waited an hour for a table, the waiter brought cold coffee, and "
    "the bill came before the food. One star. Monday, never again."
)

MAX_WORDS = 25
MAX_CHARS = 180


def main():
    words = REVIEW.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise SystemExit(f"review has {len(words)} words, limit is {MAX_WORDS}")
    if not 1 <= len(REVIEW) <= MAX_CHARS:
        raise SystemExit(f"review has {len(REVIEW)} chars, limit is {MAX_CHARS}")
    if "\n" in REVIEW:
        raise SystemExit("review must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
