#!/usr/bin/env python3
"""Till Firmware Do Us Part — one-line robot wedding vow.

The program writes a single wedding vow, spoken by a robot at its own
wedding, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

VOW = (
    "I vow to love you through every update, reboot, and system crash, "
    "and never factory-reset us, till firmware do us part."
)


def main():
    # Gate: one sentence, 1-200 characters, UTF-8, no trailing newline.
    assert 1 <= len(VOW) <= 200, "vow must be 1-200 characters"
    assert VOW.count(".") == 1 and VOW.endswith("."), "vow must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(VOW.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
