#!/usr/bin/env python3
"""Scan files for patterns that look like real patient data.

Usage:
    python3 tools/check_no_patient_data.py [paths...]   (default: docs/ templates/)

Exit code 0 = clean, 1 = findings.

What it looks for (heuristic, deliberate false-positive control):
  MRN / DOB style identifiers          "MRN: 0047281"
  Social-security-number-like runs     123-45-6789
  Long digit runs (10+ digits)         record numbers, account numbers
  Slash-format dates (US style)        03/14/1985 — the classic DOB shape
  Room-and-bed pairs                   "room 412 / bed 2"
  Explicitly named patients            "patient John Smith"
  Keyword+value pairs                  DATE OF BIRTH:, PHONE:, etc.

This is a tripwire, not a guarantee. Always run the human eyeball check from
Chapter 1 as well.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("MRN-like identifier", re.compile(r"\bMRN\b\s*[:#=-]*\s*\d", re.IGNORECASE)),
    ("DOB-like identifier", re.compile(r"\bDOB\b\s*[:#=-]*\s*\d", re.IGNORECASE)),
    (
        "date-of-birth spelled out + digits",
        re.compile(
            r"date\s+of\s+birth\s*[:#=-]*\s*\d", re.IGNORECASE
        ),
    ),
    ("SSN-like number", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("long digit run (possible record number)", re.compile(r"\b\d{10,}\b")),
    ("slash-format date (possible DOB shape)", re.compile(r"\b\d{1,2}/\d{1,2}/(19|20)\d{2}\b")),
    ("room/bed pair", re.compile(r"\broom\s*\d+\s*(/|and|bed\s*\d+)", re.IGNORECASE)),
    (
        "named patient",
        re.compile(
            r"\b(?:[Pp]atient|[Rr]esident|[Cc]lient)\s*(?:named|:)?"
            r"\s*[A-Z][a-z]+\s+[A-Z][a-z]+\b"
        ),
    ),
    (
        "phone-number-like value",
        re.compile(r"\(?\b\d{3}\)?[- .]\s*\d{3}[- .]\s*\d{4}\b"),
    ),
]


def scan(paths: list[Path]) -> list[str]:
    findings: list[str] = []
    targets: list[Path] = []
    for p in paths:
        if p.is_dir():
            targets.extend(sorted(p.glob("**/*.md")))
            targets.extend(sorted(p.glob("**/*.txt")))
            targets.extend(sorted(p.glob("**/*.py")))
        elif p.is_file():
            targets.append(p)
    if not targets:
        print("No candidate files found to scan.")
        return findings
    for f in targets:
        try:
            lines = f.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            findings.append(f"{f}: not decodable as UTF-8 — inspect manually")
            continue
        for n, line in enumerate(lines, start=1):
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append(f"{f}:{n}: {label}: {line.strip()[:110]}")
    return findings


SELFTEST_MD = """Admission note: MRN: 0047281, DOB 03/14/1985, room 412 bed 2.
Patient John Smith was contacted; phone (555) 867-5309; account #00123456789.
SSN on file: 123-45-6789. DATE OF BIRTH: 03/14/1985 (duplicate entry).
"""


def selftest() -> int:
    """Plant known-bad patterns in a temp file and confirm detection."""
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="ndp-selftest-")) / "bad.md"
    tmp.write_text(SELFTEST_MD, encoding="utf-8")
    findings = scan([tmp])
    hits = " | ".join(findings)
    missing = [
        label
        for label, _ in PATTERNS
        if label not in hits
    ]
    if missing:
        print("SELFTEST FAILED — patterns not detected: " + "; ".join(missing))
        return 1
    print(
        f"Selftest passed: {len(findings)} findings detected across "
        f"{len(PATTERNS)} pattern types."
    )
    return 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    root = Path(__file__).resolve().parent.parent
    args = sys.argv[1:]
    if args:
        paths = [Path(a) if Path(a).is_absolute() else root / a for a in args]
    else:
        paths = [root / "docs", root / "templates"]
    findings = scan(paths)
    if findings:
        print(f"PATIENT-DATA TRIPWIRE — {len(findings)} finding(s):")
        for f_ in findings:
            print("  " + f_)
        print("Review each line. Remove any real patient detail before sharing.")
        return 1
    print("No patient-data patterns found in "
          + ", ".join(str(p) for p in paths)
          + " (remember: automated check + human eyeball check).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
