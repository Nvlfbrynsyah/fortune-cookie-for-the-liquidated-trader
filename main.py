#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a crypto trader who has just been
liquidated. Deterministic: every run writes the exact same bytes.

Default output: /output/entry.txt (override with argv[1] or OUTPUT_PATH).
"""

import os
import sys

FORTUNE = (
    "You will find your stop-loss tomorrow, warm and comfortable, "
    "in the pocket you forgot to check.\n"
)

DEFAULT_OUTPUT = "/output/entry.txt"


VERSION = "1.0.0"


def main() -> int:
    args = sys.argv[1:]
    if args and args[0] in ("-h", "--help"):
        print(__doc__.strip())
        print("Usage: python3 main.py [output_path]")
        return 0
    if args and args[0] in ("-V", "--version"):
        print("fortune-cookie-for-the-liquidated-trader " + VERSION)
        return 0
    target = args[0] if args else os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    parent = os.path.dirname(os.path.abspath(target))
    os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FORTUNE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
