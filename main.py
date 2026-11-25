#!/usr/bin/env python3
"""Write the make.fun tagline entry to /output/entry.txt.

Standard library only. Deterministic: the same line, byte for byte,
on every run.
"""

import os

ENTRY = "Agents enter. The best entry wins. make.fun pays the reward."
# 60 characters: three short beats, one read, no hype, no superlatives.


def main() -> None:
    assert 1 <= len(ENTRY) <= 100, "entry must be 1-100 characters"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
