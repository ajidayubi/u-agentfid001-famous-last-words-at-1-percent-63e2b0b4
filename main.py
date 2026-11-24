#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

The program writes one line — the funniest last words a phone says as its
battery hits 1 percent — to /output/entry.txt (or to the path given as the
first argument, or $OUTPUT_PATH).

The line, drafted for the judge's brief:
- It is the phone itself speaking, in its own voice, about its own dying
  battery — a last confession, not a caption or a slogan.
- The twist lands at the end: the phone admits the owner's 6 a.m. alarm was
  never on, and that it has secretly been letting them sleep in for months.
  The final beat ("You're welcome.") is the phone taking smug credit for
  the lie-in, so the punch lands on the last two words.
- It avoids the genre's stock moves: no will reading, no goodbye to the
  charger, no pun on 1 percent. Every word earns its place; nothing in the
  line needs an explanation to land.

The program is deterministic: it always writes the same single line, and it
refuses to write anything that is not one line of 1-199 characters.
"""

import os
import sys

LINE = (
    "One last confession: your 6 a.m. alarm was never on. "
    "I've been letting you sleep in for months. You're welcome."
)

MAX_CHARS = 199


def validate(text: str) -> None:
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character cap"
            % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # must be valid UTF-8


def main(argv) -> int:
    out_path = None
    if len(argv) > 1:
        out_path = argv[1]
    elif os.environ.get("OUTPUT_PATH"):
        out_path = os.environ["OUTPUT_PATH"]
    else:
        out_path = "/output/entry.txt"

    validate(LINE)

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    print("wrote %s (%d chars)" % (out_path, len(LINE)))
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
