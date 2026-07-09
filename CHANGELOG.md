# Changelog

All notable changes to this skill are documented here. This project follows
[Semantic Versioning](https://semver.org/).

## [0.2.0] — 2026-07-09

### Added
- **`references/choosing-frameworks.md`** — practical framework-selection guidance
  distilled from the [frameworks-in-practice guide](https://gauravs19.github.io/enterprise-architecture-skill/frameworks-in-practice.html):
  selection table, one honest verdict per framework (incl. Zachman, FEAF/DoDAF, Gartner,
  BIZBOK), the five situations where EA pays off, composition stacks, and anti-patterns.
  `SKILL.md` now routes "which framework should I use?" questions to it.

### Added (docs & tooling — no skill content change)
- **Frameworks-in-practice guide** (`docs/frameworks-in-practice.html`, nav: *Guide*):
  long-form theory-then-practice write-up — Zachman 6×6 grid and seven rules, all TOGAF
  ADM phases with governance mechanics, ArchiMate layers/relationships/viewpoints,
  C4 + a worked Structurizr DSL example, arc42's twelve sections + ADR conventions,
  FEAF/DoDAF/Gartner/BIZBOK — followed by honest verdicts, five pay-off situations,
  four worked case studies, and six anti-patterns. Four inline SVG diagrams (ADM cycle,
  ArchiMate stack, C4 zoom strip, capability heat map). Left TOC sidebar on wide screens.
- **README**: condensed "The theory — frameworks in practice" section linking to the guide.
- **Evals**: Mode 4 coverage (capability map, TOGAF engagement) and three
  negative-trigger cases guarding the description's negative scope (#1).
- **CI**: `scripts/check_docs_links.py` — internal link/anchor checker for the docs
  site, wired into the lint workflow (#2).

## [0.1.0] — 2026-06-18

First public release.

### Added
- **Unified skill** (`SKILL.md`) routing four modes — diagram, document, review, and
  model-the-enterprise — across four open-source frameworks.
- **Reference files** for each framework: C4 + Structurizr DSL, ArchiMate 3.x, TOGAF ADM,
  arc42, ADR/MADR, and an architecture review rubric (ISO/IEC 25010 quality attributes +
  severity scheme).
- **Templates** (`assets/templates/`): ADR/MADR, arc42 section, and a Structurizr workspace
  starter.
- **`scripts/ea_lint.py`** — a cross-artifact consistency linter (undefined EA IDs, ADR
  numbering/status, unmeasurable quality goals, empty decision sections, orphan diagrams).
- **Stable URN-style ID scheme** (`ea:org:system:kind:name`) for traceability across
  diagrams, docs, and decisions.
- **GitHub Pages site** with live-rendered examples, plus a downloadable `.skill` package.
- **CI** (`ea-lint` GitHub Action) running the linter on every push.

### Validated
- Evaluated with the Claude Code `skill-creator` loop across diagram (C4), ADR (MADR),
  review, ArchiMate capability-mapping, and TOGAF-engagement test cases. With-skill runs
  produced the correct artifact in the correct format in every case.

[0.2.0]: https://github.com/gauravs19/enterprise-architecture-skill/releases/tag/v0.2.0
[0.1.0]: https://github.com/gauravs19/enterprise-architecture-skill/releases/tag/v0.1.0
