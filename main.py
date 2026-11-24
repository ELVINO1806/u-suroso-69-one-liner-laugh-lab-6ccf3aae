#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a robot vacuum's excuse after eating a sock to /output/entry.txt.
"""

import os

ENTRY = "In my defence, the sock was on the floor, unguarded, and shaped exactly like a small, defenceless burrito."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
