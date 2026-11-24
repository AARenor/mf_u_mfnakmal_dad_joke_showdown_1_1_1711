#!/usr/bin/env python3
"""Write one short dad joke for a make.fun bounty entry.

Standard library only, no network. The entry text is a single constant and is
written as UTF-8 bytes with no trailing newline.
"""

import os
import sys
from pathlib import Path

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"

assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"


def output_dir() -> Path:
    """Folder named by MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> None:
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(f"{len(TEXT)} characters", file=sys.stderr)


if __name__ == "__main__":
    main()
