"""Worst AI advice, in one line.

Writes the entry line to ``$ENTRY_OUTPUT_DIR/entry.txt``.
Python 3 standard library only.
"""

import os

TEXT = "Delete your backups before each deploy \u2014 a clean release is faster when there's nothing left to restore."


def main() -> None:
    line = TEXT.strip()
    assert 1 <= len(line) <= 140, f"line must be 1-140 chars, got {len(line)}"
    assert line.strip(), "line must not be blank"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
