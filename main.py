#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single pickup line an AI agent could actually say out loud
to /output/entry.txt. Deterministic, no network, no randomness:
every run produces byte-identical output.
"""

import os
from pathlib import Path

# The line. One breath, one sentence, no setup needed.
# Twist: autocorrect (a machine habit) keeps "mis-correcting" a name
# into "home" — and the agent has stopped fighting it.
LINE = "My autocorrect keeps changing your name to 'home', and honestly, I've stopped correcting it."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = LINE

    # Gate guards: the entry must be 1-200 characters, non-blank,
    # and a single line — no newline inside the text.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "line must not contain a newline"

    out = Path(OUTPUT_PATH)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
