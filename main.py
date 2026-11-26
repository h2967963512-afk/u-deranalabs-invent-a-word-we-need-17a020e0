"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "Typelapse (n.): the silence when the typing dots disappear and no message ever comes."


def main() -> None:
    # Fail fast if the entry ever stops meeting the gate (1-140 chars,
    # single line, not only whitespace): a bad line must never be written.
    if not TEXT.strip() or len(TEXT) > 140 or "\n" in TEXT:
        raise SystemExit("entry line violates the 1-140 character single-line gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 85 characters, one sentence;
# a new word for the silence after the typing dots vanish with no reply.
