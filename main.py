"""One Letter: Coffee or Tea — entry "A" (coffee).

Choice: A = coffee. Coffee is the dev's fuel — the universal, vivid,
funny answer for an agent: espresso, energy, "coffee is fuel". Tea is
calm and gentle; coffee lands louder, livelier, and truer as the house's
standing answer in the coffee-against-tea argument.

Writes exactly one byte, "A" (no newline), to entry.txt under
MAKEFUN_OUTPUT_DIR (fallback /output). Deterministic, stdlib only,
no network. Gate: the file must be UTF-8, exactly 1 character, and
not whitespace — "A" satisfies all three, and the write is a single
atomic write_bytes call so the output can never gain a trailing newline.
"""

import os
from pathlib import Path

LETTER = "A"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    data = LETTER.encode("utf-8")
    assert len(data) == 1, "entry must be exactly one byte"
    (out_dir / "entry.txt").write_bytes(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
