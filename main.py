#!/usr/bin/env python3
"""Emit the baked 11 November 2026 world-news summary to the judge.

This is a program/v1 entry for make.fun news-summary-01. The sandbox has
no network and installs nothing, so the day's reporting was gathered in
advance and committed beside this file as summary.txt. The program only
copies those bytes to MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The copy is deliberately boring: two runs must write identical files,
and the judge reads exactly those bytes. Validation uses the Python 3.13
standard library only.

Credit: the official make.fun news-summary-01 kit starter
(main.ts copying summary.txt, MIT) is the layout this program extends.
Story selection was ranked, in the build notes, with the same
sentence-importance idea as Luhn's method in miso-belica/sumy
(https://github.com/miso-belica/sumy, Apache-2.0). The emitted text
itself is original wording, not a sentence extract from any outlet or
from sumy.
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
