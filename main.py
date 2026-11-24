#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line, under 200 characters, that reads as a hilarious
autocorrect fail and nothing else, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure standard library. Deterministic: the same line every run.
"""

import os

ENTRY = "I'll bring the Satan to Thanksgiving dinner, see you at 6!"


def validate(text: str) -> None:
    """Quality gate: the gate scorer needs 1-199 chars, one line, not blank."""
    if not text or text.strip() != text or len(text) > 199:
        raise ValueError("entry must be 1-199 non-blank characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
