#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes one kind, funny fortune for a houseplant to /output/entry.txt.
The fortune must be a single line of 1-120 characters.
"""

from pathlib import Path

FORTUNE = (
    "This week, the sun will find your shyest leaf, and you will lean "
    "toward the window like it overheard gossip."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} chars, must be 1-120"
    assert "\n" not in text, "fortune must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
