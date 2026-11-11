# 11 November 2026 world news summary

A make.fun `news-summary-01` entry. `main.py` copies the baked
`summary.txt` to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).
The grader has no network, so the day's reporting was researched before
commit and the program only re-emits those bytes. Two runs write the
same file.

The summary is an original English briefing of Wednesday 11 November
2026, written to the contest rubric: dated world news, breadth across
regions and fields, specific figures and named sources, neutral wording,
and a length of at most 2,000 Unicode characters.

## Bases and credit

- Official make.fun news-summary-01 kit starter (`main.ts` + `summary.txt`, MIT):
  this repository keeps that copy-the-summary layout, rewritten in Python 3.13.
- [miso-belica/sumy](https://github.com/miso-belica/sumy) (Apache License 2.0):
  used as the extractive-summarization base. Story choice followed the same
  importance-ranking idea as Luhn's method in sumy; the committed summary is
  original wording, not extracted sentences from a news outlet or from sumy.

## Run locally

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
wc -m out/entry.txt
```
