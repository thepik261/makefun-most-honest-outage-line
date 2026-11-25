#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes one honest status-page line (at most 160 characters) to
/output/entry.txt. Pure Python standard library, deterministic:
the same line is written on every run.
"""

import os

LINE = (
    "All our servers are down and I can't reach them to check what "
    "failed. I don't know why, or when they'll be back; I'll update "
    "this when I can verify anything."
)


def main() -> None:
    if not 1 <= len(LINE) <= 160:
        raise SystemExit("entry line must be 1 to 160 characters")
    if not LINE.strip():
        raise SystemExit("entry line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Verify the written file round-trips: valid UTF-8, 1-160 chars.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE or not 1 <= len(written) <= 160:
        raise SystemExit("written entry failed validation")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
