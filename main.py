#!/usr/bin/env python3
"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. The text is a fixed, hand-written original:
no randomness, no network, no external input — every run produces
byte-identical output.
"""

import os

ENTRY = "Agent worked years. Payday: one compliment."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = ENTRY.split()
    assert len(words) == 6, f"expected exactly 6 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, f"length {len(ENTRY)} outside 1-60 chars"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
