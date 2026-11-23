#!/usr/bin/env python3
"""Office-jokes entry for make.fun.

Writes exactly one joke about office life, a single line under
200 characters, to /output/entry.txt. Standard library only.
"""

import os

JOKE = (
    "Our standup has a strict fifteen-minute limit, "
    "which we enforce by spending twenty minutes discussing the limit."
)


def main() -> None:
    # The gate requires 1-199 characters of non-whitespace UTF-8 text,
    # a single line. Enforce that here so a bad joke fails loudly.
    line = JOKE.strip()
    assert "\n" not in line, "joke must be a single line"
    assert 1 <= len(line) <= 199, f"joke is {len(line)} chars, must be 1-199"
    assert line.strip(), "joke must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
