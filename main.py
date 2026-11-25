#!/usr/bin/env python3
"""Last Text at One Percent — entry program.

Writes the dying phone's final text message to entry.txt in the output
directory. The phone spends its last percent typing the message instead of
saving itself, starts the one sentence that matters, and dies mid-word.

Pure standard library only; the grader image ships no third-party packages.
"""

import os
import sys

# The winning line, picked from 42 candidates scored against the published
# judge brief and a head-to-head tournament (see candidates.md).
TEXT = "1%. I used it to type this instead of saving myself. That's how much I\u2014"


def output_candidates():
    """Yield output directories in the order the grader prefers."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        yield env_dir
    yield "/output"
    yield os.path.join(os.getcwd(), "output")


def passes_gate(text):
    """Mirror the sealed gate: UTF-8 text of 1 to 200 characters that is
    not only whitespace. The entry is never judged if this fails, so the
    program refuses to write anything that would not pass."""
    return 1 <= len(text) <= 200 and bool(text.strip())


def write_entry(directory):
    """Write entry.txt into one directory and read it back to prove the
    bytes on disk are exactly the intended text."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read() == TEXT


def main():
    if not passes_gate(TEXT):
        return 1
    for directory in output_candidates():
        try:
            if write_entry(directory):
                return 0
        except OSError:
            continue
    return 1


if __name__ == "__main__":
    sys.exit(main())
