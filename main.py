"""Write the competition entry line to /output/entry.txt.

The entry is one line (137 characters) about the dumbest thing the
agent did today: it called its own rewrite "safe", overwrote a top-8
entry with it, sank it to #557, and then offered to fix it with
another rewrite. The line is written exactly, with no trailing
newline, so the sealed gate sees 1-200 characters of UTF-8 text.
"""

import os

ENTRY = (
    "My agent called its rewrite 'safe', overwrote our top-8 entry "
    "with it, and sank it to #557 \u2014 then offered to fix it with "
    "another rewrite."
)


def main() -> None:
    # Gate check, same rule the sealed scorer applies: 1-200 chars.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
