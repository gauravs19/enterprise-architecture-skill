#!/usr/bin/env python3
"""
ea_lint.py — lightweight cross-artifact consistency checker for the
enterprise-architecture skill.

It does NOT validate diagram syntax (Structurizr/PlantUML/Mermaid have their own
renderers for that). It checks the *connective tissue* between artifacts — the
things that silently rot in architecture docs:

  1. Stable EA IDs (ea:org:system:kind:name) that are referenced but never defined.
  2. ADR hygiene: numbering gaps/dupes, missing Status, accepted ADRs never linked
     from any doc, "superseded by" pointing at a non-existent ADR.
  3. arc42 quality goals / scenarios that are vague (no measurable response).
  4. arc42 §9 (decisions) that links no ADRs while ADRs exist.
  5. Orphan diagram source files (.dsl/.puml/.mmd) never referenced from any doc.

Usage:
    python ea_lint.py <path>           # a dir (recursed) or a single file
    python ea_lint.py <path> --strict  # exit 1 if any Major+ findings

Output: findings grouped by severity. Advisory by default (exit 0).
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

SEVERITY_ORDER = ["CRITICAL", "MAJOR", "MINOR", "SUGGESTION"]

EA_ID_RE = re.compile(r"\bea:[a-z0-9_-]+:[a-z0-9_-]+:[a-z0-9_-]+:[a-z0-9_-]+\b", re.I)
ADR_FILE_RE = re.compile(r"^(\d{3,4})[-_].+\.md$", re.I)
SUPERSEDED_RE = re.compile(r"superseded by\s+ADR[-\s]?(\d{3,4})", re.I)
STATUS_RE = re.compile(r"^\s*[-*]?\s*status:\s*(.+)$", re.I | re.M)
# vague quality words used without a number/unit nearby
VAGUE_QUALITY_RE = re.compile(
    r"\b(fast|scalable|secure|reliable|performant|user-friendly|robust|flexible|"
    r"high[- ]performance|highly available)\b",
    re.I,
)
NUMBER_NEARBY_RE = re.compile(
    r"\b\d+\s?(ms|s|sec|seconds|minutes|min|%|percent|rps|qps|tps|users|"
    r"requests|concurrent|p\d{2}|gb|mb|tb)\b",
    re.I,
)
DIAGRAM_EXTS = {".dsl", ".puml", ".plantuml", ".mmd"}


class Finding:
    def __init__(self, severity: str, rule: str, message: str, where: str = ""):
        self.severity = severity
        self.rule = rule
        self.message = message
        self.where = where

    def __str__(self) -> str:
        loc = f" ({self.where})" if self.where else ""
        return f"[{self.rule}] {self.message}{loc}"


def gather_files(root: Path):
    md_files, diagram_files = [], []
    paths = [root] if root.is_file() else sorted(root.rglob("*"))
    for p in paths:
        if not p.is_file():
            continue
        if p.suffix.lower() == ".md":
            md_files.append(p)
        elif p.suffix.lower() in DIAGRAM_EXTS:
            diagram_files.append(p)
    return md_files, diagram_files


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def check_ea_ids(md_files, findings):
    """EA IDs referenced but never 'defined'. Heuristic: an ID is 'defined' if it
    appears at the start of a line, in a heading, in a table's first cell, or with
    a 'define'/'id:' marker. Otherwise it's only referenced."""
    defined, referenced = set(), {}
    for p in md_files:
        text = read(p)
        for m in EA_ID_RE.finditer(text):
            ident = m.group(0).lower()
            line_start = text.rfind("\n", 0, m.start()) + 1
            prefix = text[line_start:m.start()]
            is_def = (
                prefix.strip() in ("", "#", "##", "###", "-", "*", "|", "> ")
                or re.search(r"(id|define[ds]?|urn)\s*[:=|]\s*$", prefix, re.I)
            )
            if is_def:
                defined.add(ident)
            referenced.setdefault(ident, str(p))
    for ident, where in referenced.items():
        if ident not in defined:
            findings.append(Finding(
                "MINOR", "ea-id-undefined",
                f"EA ID '{ident}' is referenced but never defined "
                f"(no line/heading/table-cell defines it)", where))


def check_adrs(md_files, findings):
    adrs = {}  # number -> (path, text)
    for p in md_files:
        m = ADR_FILE_RE.match(p.name)
        # treat files under a decisions/adr folder, or matching NNNN-*.md, as ADRs
        in_adr_dir = any(seg.lower() in ("adr", "adrs", "decisions") for seg in p.parts)
        if m and (in_adr_dir or "## decision" in read(p).lower()):
            num = int(m.group(1))
            adrs[num] = (p, read(p))

    if not adrs:
        return  # no ADRs — nothing to check

    # numbering gaps & status
    nums = sorted(adrs)
    for n in range(nums[0], nums[-1] + 1):
        if n not in adrs:
            findings.append(Finding(
                "MINOR", "adr-numbering-gap",
                f"ADR number {n:04d} is missing (sequence {nums[0]:04d}-{nums[-1]:04d})"))
    for num, (p, text) in adrs.items():
        if not STATUS_RE.search(text):
            findings.append(Finding(
                "MAJOR", "adr-no-status",
                f"ADR {num:04d} has no Status field", str(p)))
        for sm in SUPERSEDED_RE.finditer(text):
            target = int(sm.group(1))
            if target not in adrs:
                findings.append(Finding(
                    "MAJOR", "adr-superseded-missing",
                    f"ADR {num:04d} is 'superseded by ADR-{target:04d}' which does "
                    f"not exist", str(p)))

    # accepted ADRs never linked from any non-ADR doc
    non_adr_text = "\n".join(
        read(p) for p in md_files if not ADR_FILE_RE.match(p.name))
    for num, (p, text) in adrs.items():
        status_m = STATUS_RE.search(text)
        status = (status_m.group(1).lower() if status_m else "")
        if "accepted" in status:
            stem = p.stem
            if stem not in non_adr_text and p.name not in non_adr_text:
                findings.append(Finding(
                    "SUGGESTION", "adr-unlinked",
                    f"Accepted ADR {num:04d} ('{stem}') isn't linked from any other "
                    f"doc (link it from arc42 §9)", str(p)))


def check_quality_goals(md_files, findings):
    for p in md_files:
        name = p.name.lower()
        if not any(k in name for k in ("quality", "goal", "introduction", "10-", "01-")):
            continue
        for i, line in enumerate(read(p).splitlines(), 1):
            if VAGUE_QUALITY_RE.search(line) and not NUMBER_NEARBY_RE.search(line):
                # ignore lines that are clearly prose guidance, not a goal statement
                if len(line.strip()) < 8:
                    continue
                findings.append(Finding(
                    "MINOR", "vague-quality-goal",
                    f"Quality wording without a measurable number: "
                    f"\"{line.strip()[:80]}\"", f"{p}:{i}"))


def check_decisions_section(md_files, findings):
    has_adrs = any(
        ADR_FILE_RE.match(p.name) and
        any(s.lower() in ("adr", "adrs", "decisions") for s in p.parts)
        for p in md_files)
    if not has_adrs:
        return
    for p in md_files:
        if re.search(r"(09[-_]|decision)", p.name, re.I) and "decision" in p.name.lower():
            text = read(p).lower()
            if not re.search(r"adr[-\s]?\d", text) and "decisions/" not in text:
                findings.append(Finding(
                    "MINOR", "decisions-section-empty",
                    "arc42 decisions section links no ADRs although ADRs exist",
                    str(p)))


def check_orphan_diagrams(md_files, diagram_files, findings):
    all_md = "\n".join(read(p) for p in md_files)
    for d in diagram_files:
        if d.name not in all_md and d.stem not in all_md:
            findings.append(Finding(
                "SUGGESTION", "orphan-diagram",
                f"Diagram source '{d.name}' is not referenced from any doc", str(d)))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="architecture dir (recursed) or a single file")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any CRITICAL/MAJOR findings")
    args = ap.parse_args()

    # Make output encoding-safe on Windows consoles (cp1252 can't render emoji).
    use_emoji = True
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        use_emoji = False

    root = Path(args.path)
    if not root.exists():
        print(f"error: path not found: {root}", file=sys.stderr)
        return 2

    md_files, diagram_files = gather_files(root)
    if not md_files and not diagram_files:
        print("No .md or diagram files found to check.")
        return 0

    findings: list[Finding] = []
    check_ea_ids(md_files, findings)
    check_adrs(md_files, findings)
    check_quality_goals(md_files, findings)
    check_decisions_section(md_files, findings)
    check_orphan_diagrams(md_files, diagram_files, findings)

    print(f"ea_lint: scanned {len(md_files)} doc(s) and "
          f"{len(diagram_files)} diagram source(s) under {root}\n")

    if not findings:
        print("✓ No consistency issues found.")
        return 0

    by_sev = {s: [f for f in findings if f.severity == s] for s in SEVERITY_ORDER}
    if use_emoji:
        icons = {"CRITICAL": "🔴", "MAJOR": "🟠", "MINOR": "🟡", "SUGGESTION": "🔵"}
    else:
        icons = {"CRITICAL": "[!]", "MAJOR": "[*]", "MINOR": "[-]", "SUGGESTION": "[~]"}
    for sev in SEVERITY_ORDER:
        items = by_sev[sev]
        if not items:
            continue
        print(f"{icons[sev]} {sev} ({len(items)})")
        for f in items:
            print(f"  - {f}")
        print()

    print(f"Total: {len(findings)} finding(s). "
          "These are advisory — review with the user; don't auto-'fix' intent.")

    if args.strict and (by_sev["CRITICAL"] or by_sev["MAJOR"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
