# enterprise-architecture — a Claude Code Agent Skill

A unified **enterprise & software architecture** skill for [Claude Code](https://docs.anthropic.com/en/docs/claude-code),
grounded in four open-source standards instead of one. It helps Claude produce architecture
work the way the standards intend it: **diagrams as code, documentation as code, decisions
as records, and one traceable model underneath.**

🌐 **Live site & eval examples:** https://gauravs19.github.io/enterprise-architecture-skill/

| Framework | Answers | Used for |
|---|---|---|
| **C4 model + Structurizr DSL** | "How is *this system* built?" | Context / Container / Component diagrams |
| **ArchiMate 3.x** | "How does the *enterprise* fit together?" | Capabilities → apps → technology |
| **TOGAF ADM** | "How do we *deliver* the change?" | Engagement structure, roadmaps, portfolio |
| **arc42 + ADR/MADR** | "How do we *write it down*?" | System docs & decision records |

---

## Contents

- [Why this exists](#why-this-exists)
- [The mental model — four frameworks, four altitudes](#the-mental-model--four-frameworks-four-altitudes)
- [The four frameworks in depth](#the-four-frameworks-in-depth)
- [The four modes](#the-four-modes)
- [Traceability — one model under everything](#traceability--one-model-under-everything)
- [Install](#install)
- [Usage](#usage)
- [The consistency linter](#the-consistency-linter)
- [Eval results](#eval-results)
- [Repository layout](#repository-layout)
- [License](#license)

---

## Why this exists

The open-source ecosystem has excellent single-purpose skills — C4+ArchiMate plugins,
arc42 toolkits, ADR generators — but **none unify all four frameworks, and none cover
TOGAF or architecture *review*.** This skill fills that gap: one skill that picks the right
framework at the right altitude, produces everything as code, and keeps a single traceable
model under every diagram, doc, and decision.

## The mental model — four frameworks, four altitudes

These frameworks are **not competitors** — they answer different questions. Knowing which
one fits the question is most of the skill.

- **C4** zooms into *one system*.
- **ArchiMate** zooms out to the *enterprise*.
- **TOGAF** is the *method* for changing it.
- **arc42 / ADR** is how you *narrate* it.

They compose: an arc42 doc embeds C4 diagrams and links ADRs; a TOGAF engagement produces
ArchiMate models and ADRs as deliverables.

---

## The four frameworks in depth

### C4 model + Structurizr DSL
*Simon Brown's model — open source.*

Describes **one software system** at four zoom levels, like Google Maps for your codebase.
Most systems only need the first two or three.

- **Best for:** communicating a single system/service, onboarding engineers, diagrams that
  live in the repo and render anywhere.
- **Levels:** **Context** (system + users + neighbours) → **Container** (deployable units:
  apps, DBs, brokers — *not* Docker containers) → **Component** (building blocks inside a
  container) → **Code** (rarely needed; the IDE does it better).
- **Hygiene built in:** 5–20 elements per view, every external dependency shown, every
  relationship labelled with intent + protocol, a title and a legend.
- **Produces:** **Structurizr DSL** (the model-of-record — define elements once, render many
  views), **Mermaid C4** (zero-tooling inline rendering), or **C4-PlantUML** (for
  Kroki/PlantUML pipelines).

→ Reference: [`references/c4-structurizr.md`](references/c4-structurizr.md)

### ArchiMate 3.x
*The Open Group standard — modelled in the free Archi tool.*

The standard language for **enterprise** architecture: how business, applications, and
technology fit together across many systems.

- **Best for:** cross-system and enterprise-wide views, capability maps, application
  landscapes, business ↔ IT alignment.
- **Layers:** Motivation · Strategy · Business · Application · Technology (+ Implementation
  & Migration), each crossed with **aspects** (active structure / behavior / passive
  structure).
- **The two relationships you'll use constantly:** **Realization** (up across layers — "X
  makes Y real") and **Serving** (down — "X is used by Y"). Getting these right is what
  makes a model read correctly.
- **Viewpoints:** pick the predefined selection for the stakeholder's concern — Layered,
  Capability Map, Application Cooperation, Application Usage, Technology, Motivation.
- **Produces:** Archi models (`.archimate` / Open Group Exchange Format); Mermaid/PlantUML
  approximations for quick sharing (clearly labelled as approximations).

→ Reference: [`references/archimate.md`](references/archimate.md)

### TOGAF ADM
*The Open Group — a method, not a notation.*

The **Architecture Development Method** is a cycle of phases for delivering an architecture
change with governance. Use it to *structure an engagement* and decide *which* models to
produce; ArchiMate draws them and ADRs record the decisions.

- **Best for:** running/governing an architecture engagement, roadmaps and transition
  planning, application-portfolio rationalization.
- **Phases:** Preliminary → A. Vision → B. Business → C. Information Systems (Data + App) →
  D. Technology → E. Opportunities & Solutions → F. Migration Planning → G. Implementation
  Governance → H. Change Management, with **Requirements Management** at the hub.
- **Core idea:** every phase is **Baseline → Target → Gaps**; the gaps feed a roadmap of
  **Transition Architectures** (plateaus).
- **Portfolio rationalization (TIME):** score each app on business value × technical fit →
  **Tolerate / Invest / Migrate / Eliminate** with a recommended next step.
- **Tailor it.** Don't ceremonially run all phases for a small change — scale the rigor to
  the stakes.

→ Reference: [`references/togaf-adm.md`](references/togaf-adm.md)

### arc42 + ADR / MADR
*Open documentation template + decision records, docs-as-code.*

A lightweight, battle-tested **template** (12 sections, each answering one question) plus
**decision records** that capture the *reasoning* behind significant choices.

- **arc42's 12 sections:** Introduction & Goals · Constraints · Context & Scope ·
  Solution Strategy · Building Block View · Runtime View · Deployment View · Crosscutting
  Concepts · **Architecture Decisions** · Quality Requirements · Risks & Technical Debt ·
  Glossary.
- **Detail knob:** write to **LEAN / ESSENTIAL / THOROUGH** so you produce the right amount
  — a 40-page doc nobody reads is a failure, not thoroughness.
- **Measurable quality goals:** "fast" becomes "place-order responds in <200ms p95 at 1000
  concurrent users." Vague adjectives are rejected.
- **ADR / MADR:** one architecturally-significant decision per record — context, decision
  drivers, options *with pros & cons*, the chosen outcome justified against the drivers, and
  consequences (good **and** bad). Immutable; superseded by new ADRs, never rewritten.
- **Produces:** Markdown docs-as-code with embedded C4 diagrams, numbered ADR files, and a
  decision log linked from §9.

→ References: [`references/arc42.md`](references/arc42.md) · [`references/adr-madr.md`](references/adr-madr.md)

---

## The four modes

The skill routes any architectural request to one of four modes — you don't have to name a
framework.

| Mode | Trigger phrasings | What you get |
|---|---|---|
| **1. Diagram** | "draw / diagram / visualize", "container diagram", "Structurizr workspace" | C4 / Structurizr / Mermaid / PlantUML at the right altitude |
| **2. Document** | "document this system", "write an ADR", "arc42 docs", "design doc / RFC" | arc42 sections or an ADR/MADR with the trade-offs captured |
| **3. Review / assess** | "review my architecture", "is this design sound?", "what are the risks?" | Severity-graded findings (evidence + fix) and a verdict |
| **4. Model the enterprise** | "map our capabilities", "application landscape", "capability → app → tech" | ArchiMate model + TOGAF structure, with realization links |

**Mode 3** grades against **ISO/IEC 25010** quality attributes (performance, security,
reliability, maintainability, …) plus EA principles, and returns findings categorized
**Critical / Major / Minor / Suggestion**, each with evidence and a concrete remediation,
then a verdict (Approved / Approved-with-changes / Needs-revision) — not personal taste.

→ Review rubric: [`references/review-rubric.md`](references/review-rubric.md)

---

## Traceability — one model under everything

Give every architectural element a **stable, human-readable ID** and reuse it across
diagrams, docs, and ADRs. This is what turns a pile of pictures into an actual model.

- ID scheme (URN-style): `ea:{org}:{system}:{kind}:{name}`
  - e.g. `ea:acme:checkout:container:payment-api`, `ea:acme:enterprise:capability:billing`
  - `kind` ∈ person, system, external, container, component, capability, app, node, decision …
- When a repo exists, persist these in an `architecture/` folder (one file per significant
  artifact, or a Structurizr workspace as the model-of-record) so they're diff-able and
  greppable, and reference the same ID from the arc42 doc and the ADRs.
- Before inventing a new element, check whether it already exists under another name and
  reuse the ID. **Two names for one thing** is the most common EA documentation defect.

---

## Install

**Option A — clone** into your Claude Code skills directory:

```bash
git clone https://github.com/<you>/enterprise-architecture-skill \
  ~/.claude/skills/enterprise-architecture
```

**Option B — plugin marketplace** (no clone needed). In Claude Code:

```
/plugin marketplace add gauravs19/enterprise-architecture-skill
/plugin install enterprise-architecture@gauravs19-skills
```

**Option C — download the packaged skill:** grab
[`enterprise-architecture.skill`](https://gauravs19.github.io/enterprise-architecture-skill/enterprise-architecture.skill)
(or from the [latest release](https://github.com/gauravs19/enterprise-architecture-skill/releases))
and install it through Claude Code.

Claude Code discovers it automatically — the skill folder must be named
`enterprise-architecture` (that's the skill's invocation name); the repo it comes from can
be named anything.

## Usage

Just ask in plain language — the skill triggers itself and picks the framework + mode:

```
draw the container diagram for this checkout service
write an ADR for choosing Kafka over RabbitMQ for our order events
review this architecture — is it sound for 50k daily users?
map our business capabilities to the apps that realize them
create a Structurizr workspace for the payments platform
document this service with arc42 at ESSENTIAL detail
```

Each response states **which framework and view** it's producing, so you learn the map as
you go — part of the skill's job is to make you fluent in the frameworks, not just hand you
artifacts.

## The consistency linter

`scripts/ea_lint.py` checks the connective tissue *between* artifacts (it doesn't validate
diagram syntax — renderers do that). It flags:

- EA IDs referenced but never defined
- ADR numbering gaps, missing `Status`, and dangling "superseded by ADR-XXXX"
- accepted ADRs not linked from any doc
- vague (unmeasurable) quality goals
- empty arc42 decision sections
- orphan diagram source files never referenced from a doc

```bash
python scripts/ea_lint.py path/to/docs/architecture
python scripts/ea_lint.py path/to/docs/architecture --strict   # exit 1 on Major+ findings
```

Findings are grouped by severity. It's **advisory** — it reports, it doesn't rewrite your
intent.

## Eval results

The skill was tested with the [`skill-creator`](https://docs.anthropic.com/en/docs/claude-code)
eval loop — each prompt run **with the skill** and as a **baseline**, graded against
objective assertions:

| Test case | Baseline | With skill | What the skill changed |
|---|---|---|---|
| C4 diagram | 3 / 5 | **5 / 5** | Real C4 notation (Context + Container) + a Structurizr source-of-truth. Baseline drew a generic flowchart. |
| ADR | 4 / 5 | **5 / 5** | Correct MADR format (status, drivers, options, consequences). Baseline wrote good analysis, not an ADR. |
| Review | 6 / 6\* | **6 / 6** | Both strong. \*Globally-installed skills are discoverable, so the baseline used the skill anyway — not a clean baseline. |

The skill's main value is forcing the **right artifact in the right format**. Because
installed skills are globally discoverable, the measured gap is a *conservative lower bound*.
The actual example outputs are in [`docs/examples/`](docs/examples/) and rendered on the
[live site](https://gauravs19.github.io/enterprise-architecture-skill/).

## Repository layout

```
enterprise-architecture/
├── SKILL.md                       # router: pick framework + mode, shared workflow
├── references/
│   ├── c4-structurizr.md          # C4 levels, Structurizr DSL, Mermaid/PlantUML
│   ├── archimate.md               # layers, element catalog, relationships, viewpoints
│   ├── togaf-adm.md               # 10 ADM phases, deliverables, TIME portfolio model
│   ├── arc42.md                   # 12 sections + LEAN/ESSENTIAL/THOROUGH detail knob
│   ├── adr-madr.md                # ADR & MADR templates and conventions
│   └── review-rubric.md           # quality attributes, severity scheme, verdict format
├── assets/templates/              # ADR, arc42 section, Structurizr workspace starters
├── scripts/
│   └── ea_lint.py                 # cross-artifact consistency checker
├── evals/                         # test prompts + assertions
└── docs/                          # GitHub Pages site + example outputs
```

## License

MIT — see [LICENSE](LICENSE).
