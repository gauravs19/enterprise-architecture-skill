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
- [The theory — frameworks in practice](#the-theory--frameworks-in-practice)
- [The mental model — four frameworks, four altitudes](#the-mental-model--four-frameworks-four-altitudes)
- [The four frameworks](#the-four-frameworks)
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

## The theory — frameworks in practice

There's a large gap between how EA frameworks are marketed and how they're used. Almost no
organization runs TOGAF or Zachman "by the book" — full-ceremony adoption usually collapses
under its own weight. What survives contact with reality is **selective borrowing**:

| Framework | What practitioners actually keep |
|---|---|
| **Zachman** | The mental model (what/how/where/who/when/why × audience), not the 36-cell grid. A 30-minute lens, not a study project. |
| **TOGAF** | ADM as a scoping *checklist*; **Baseline → Target → Gap → Roadmap** as the transformation backbone; the governance vocabulary (ARB, principles, waivers). |
| **FEAF / DoDAF** | Only if you sell into government/defense — the RFP will name them. |
| **Capability maps** (BIZBOK) | Probably the most-used single EA artifact in real life — the one page executives actually read. |
| **C4 / ArchiMate / arc42 + ADRs** | Where the hands-on value lives — this skill's four. arc42 + ADRs have the best value-to-ceremony ratio in the whole space. |

Where frameworks genuinely earn their keep: **M&A integration** (two of everything — what to
kill?), **cloud migration programs** (baseline/target/gap keeps multi-year work coherent),
**vendor/platform decisions** (ADRs make them defensible two years later), **regulatory
traceability** (requirement → capability → app → deployment), and **fighting shadow-IT
sprawl** (a maintained app landscape is the only way anyone knows what exists).

**Frameworks are scaffolding, not the building** — the value is a handful of living artifacts
(a capability map, an application landscape, a decision log, a roadmap), not framework
compliance.

→ **Full write-up with four worked case studies and the six EA anti-patterns:**
[Frameworks in practice](https://gauravs19.github.io/enterprise-architecture-skill/frameworks-in-practice.html)

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

## The four frameworks

| Framework | Zoom level | The one habit it gives you | Skill reference |
|---|---|---|---|
| **C4 + Structurizr DSL** | One system: Context → Container → Component (→ Code) | Diagrams as code in the repo; 5–20 elements per view, every arrow labelled | [`references/c4-structurizr.md`](references/c4-structurizr.md) |
| **ArchiMate 3.x** | The enterprise: capabilities → apps → technology | Realization/serving links that answer "what breaks if we retire this app?" | [`references/archimate.md`](references/archimate.md) |
| **TOGAF ADM** | The engagement: phases + governance | Baseline → Target → Gap → Roadmap; TIME portfolio scoring; tailor rigor to stakes | [`references/togaf-adm.md`](references/togaf-adm.md) |
| **arc42 + ADR/MADR** | The documentation: 12 sections + decision log | ADRs at decision time with options *and trade-offs*; LEAN/ESSENTIAL/THOROUGH detail knob | [`references/arc42.md`](references/arc42.md) · [`references/adr-madr.md`](references/adr-madr.md) |

Each framework is explained in full — origin, structure, worked examples, what practitioners
actually keep — in the **[frameworks-in-practice guide](https://gauravs19.github.io/enterprise-architecture-skill/frameworks-in-practice.html)**.
For "which framework should I use?" questions, the skill itself loads
[`references/choosing-frameworks.md`](references/choosing-frameworks.md).

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
│   ├── review-rubric.md           # quality attributes, severity scheme, verdict format
│   └── choosing-frameworks.md     # "which framework?" — verdicts, pay-off situations, anti-patterns
├── assets/templates/              # ADR, arc42 section, Structurizr workspace starters
├── scripts/
│   └── ea_lint.py                 # cross-artifact consistency checker
├── evals/                         # test prompts + assertions
└── docs/                          # GitHub Pages site + example outputs
```

## License

MIT — see [LICENSE](LICENSE).
