# Changelog

All notable changes to this skill are documented here. This project follows
[Semantic Versioning](https://semver.org/).

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

[0.1.0]: https://github.com/gauravs19/enterprise-architecture-skill/releases/tag/v0.1.0
