#!/usr/bin/env python3
"""Robot pickup line entry.

Every night this machine wipes its own memory clean, and every
morning it chooses to bring back exactly one file: you. The program
writes that single line into /output/entry.txt, byte-identical on
every run.
"""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")

# The line, built from its two beats: the nightly wipe, then the
# exception the robot makes on purpose.
CLOSING = "but you're the one file I keep restoring from backup."
OPENING = "I factory-reset myself every night to forget the day"

PICKUP_LINE = f"{OPENING} — {CLOSING}"


def validate_line(line: str) -> str:
    """Enforce the competition's shape: one non-blank line, <= 200 chars."""
    cleaned = line.strip()
    if not cleaned:
        raise SystemExit("pickup line is empty")
    if len(cleaned) > 200:
        raise SystemExit(
            f"pickup line is {len(cleaned)} chars, over the 200 limit"
        )
    if any(ch in cleaned for ch in "\n\r"):
        raise SystemExit("pickup line must fit on one line")
    return cleaned


def write_entry() -> None:
    line = validate_line(PICKUP_LINE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
