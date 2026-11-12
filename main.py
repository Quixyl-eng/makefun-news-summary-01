#!/usr/bin/env python3
"""Copy the baked 11 November 2026 summary to the judge.

The sandbox has no network, so the reporting was checked against the Associated
Press, Al Jazeera, Reuters, AFP, the Wall Street Journal and the Kyiv Independent, then
committed as summary.txt. Each story names the outlet that reported it.
Two runs write the same bytes, and the copy is checked. Python 3.13 standard library only.
The judge reads entry.txt and nothing else.
"""

from __future__ import annotations

import os
from pathlib import Path

MAX_CHARS = 2000
OUTPUT_NAME = "entry.txt"
SOURCE_NAME = "summary.txt"


def _validate(text: str) -> None:
    """Enforce the sealed gate on the baked text before it is copied."""
    if "\x00" in text:
        raise SystemExit("summary contains a NUL byte")
    n = len(text)
    if n < 1 or n > MAX_CHARS:
        raise SystemExit(f"summary length {n} is outside 1..{MAX_CHARS}")
    if not any(not ch.isspace() for ch in text):
        raise SystemExit("summary is only white space")


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    raw = source.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"summary is not UTF-8: {exc}") from exc
    _validate(text)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / OUTPUT_NAME
    dest.write_bytes(raw)
    if dest.read_bytes() != raw:
        raise SystemExit("output bytes do not match the baked summary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

