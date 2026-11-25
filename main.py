#!/usr/bin/env python3
"""Monday Morning Punchlines - entry writer.

Writes the tournament-winning one-liner to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Standard library only; never writes into the repository itself.
The winning line is exactly 46 characters; a length guard below
rejects any accidental change to that text.
Why this line won the tournament (criteria in priority order):
1. Monday: the weekend-vs-Monday handover is squarely on topic.
2. Punchline: "Monday ate me" lands as a dark, funny kicker.
3. Surprise: a farewell note from the weekend is an unexpected frame.
4. Economy: 46 characters, every word doing work, no wasted setup.
5. Freshness: no tired alarm/coffee Monday cliche; the note format is new.
It tied 4-1 with H5/H8 in the round-robin and won the exact-tie rule
(fewer bytes) plus a head-to-head win over Hermes' top pick H5.
"""

import os

ENTRY = "My weekend left a note: 'Gone. Monday ate me.'"


def main():
    assert len(ENTRY) == 46, f"entry length changed: {len(ENTRY)}"
    assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
