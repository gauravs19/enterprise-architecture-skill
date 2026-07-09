# Choosing frameworks — practical selection guidance

Load this when the user asks **"which framework should I use?"**, "is TOGAF worth it?",
"Zachman vs TOGAF?", "how should we approach this architecture effort?", or any
framework-selection / EA-strategy question. The goal is a grounded recommendation, not a
survey — pick, justify briefly, and point at the concrete first artifact.

> The honest baseline: almost no organization runs any framework "by the book".
> Full-ceremony adoption collapses under its own weight. What works is **selective
> borrowing** — frameworks are scaffolding, not the building. The value is a handful of
> living artifacts (a capability map, an application landscape, a decision log, a roadmap),
> not framework compliance. Answer in that spirit.

## The selection table

| The user's question is really… | Reach for | First artifact to produce |
|---|---|---|
| "How is *this system* structured / how do I communicate it?" | **C4** | System Context + Container diagram (Structurizr DSL or Mermaid) |
| "How does the *whole enterprise* fit together?" | **ArchiMate** | Capability map → application landscape with realization links |
| "How do we *run* this transformation / engagement?" | **TOGAF ADM** (tailored) | Vision + baseline → target → gap → roadmap |
| "How do we *document* this system / record this decision?" | **arc42 + ADR/MADR** | arc42 at ESSENTIAL detail; one ADR per significant decision |
| "What kinds of descriptions exist / who is this artifact for?" | **Zachman** (as a lens) | None — use it to match artifact to audience, or trace one column for an audit |
| "The RFP names FEAF / DoDAF / NAF" | Those, as mandated | Whatever the procurement viewpoint set requires |

## One honest verdict per framework

- **Zachman** — a classification schema, not a method. Worth 30 minutes as a mental model
  (six questions × six audiences); never fill the 36-cell grid. Its practical uses: audience
  matching ("you gave a row-1 audience a row-4 artifact") and single-column traceability for
  audits (requirement → capability → app → deployment).
- **TOGAF** — borrow the spine. ADM as a scoping checklist (never a linear process),
  **Baseline → Target → Gap → Roadmap** as the backbone of any transformation, the governance
  vocabulary (ARB, principles, waivers), and TIME portfolio scoring
  (Tolerate / Invest / Migrate / Eliminate). Skip full-deliverable ceremony.
- **ArchiMate** — use in anger. Arguably more useful day-to-day than TOGAF itself:
  realization + serving links answer "what breaks if we retire this app?". Model in Archi
  (free); a maintained model beats any diagram pile.
- **C4** — the default at system level. Context + Container answer 90% of questions;
  diagrams as code in the repo. Draw Component selectively; never hand-draw Code.
- **arc42 + ADRs** — the best value-to-ceremony ratio in the space. ADRs written at
  decision time (options **with trade-offs**) are the single highest-ROI architecture habit.
  arc42 at LEAN/ESSENTIAL; sections 1, 3, 4, 5, 9 carry most of the value.
- **FEAF / DoDAF / MODAF / NAF** — mandated in government/defense procurement; learn them
  when the RFP names them, not before. (Worth stealing: DoDAF's OV/SV split — describe the
  mission technology-free, then map systems onto it.)
- **Gartner-style "pragmatic EA"** — an attitude, not an artifact set: measure EA by
  decisions influenced and money saved, not models produced. Every artifact needs a named
  customer with a pending decision.
- **BIZBOK** — steal the capability map: what the business *does*, independent of org chart
  and systems, heat-mapped by whatever lens the decision needs (maturity, spend, incidents).

## Situations where frameworks genuinely pay off

Recommend the modeling effort when the situation matches one of these; otherwise bias to
lighter artifacts (a C4 diagram + ADRs is often enough).

1. **M&A / post-merger integration** — capability map + application landscape + TIME scoring
   turn "two of everything" into an evidence-based keep/kill roadmap.
2. **Cloud migration / modernization programs** — baseline → target → gap → transition
   plateaus keep multi-year work coherent across budget cycles and re-orgs.
3. **Vendor & platform decisions** — an ADR with options and trade-offs makes the decision
   defensible years later ("why Kafka?").
4. **Regulatory / audit traceability** — a Zachman-style single-column trace from
   requirement → capability → application → deployment, each hop an artifact you already
   maintain.
5. **Shadow-IT sprawl** — a maintained application landscape is the only way anyone knows
   what exists.

## How the four compose (recommend stacks, not single frameworks)

- An **arc42 doc** embeds **C4 diagrams** (§5) and links **ADRs** (§9).
- A **TOGAF engagement** produces **ArchiMate models** and **ADRs** as its deliverables.
- A **capability map** (BIZBOK/ArchiMate) anchors **TIME scoring** (TOGAF) for portfolio work.
- Greenfield system: C4 + arc42 + ADRs, with TOGAF-lite (vision + 5–7 principles only).

## Anti-patterns to warn about

If the user's plan matches one of these, say so directly:

- **Ivory tower** — models nobody asked for; attach every artifact to a live decision.
- **The 36-cell grid** — attempting full Zachman; use one column when a question demands it.
- **Ceremonial full-ADM** — all ten phases for a small change; scale rigor to stakes.
- **The 40-page document** — thoroughness as failure mode; write LEAN, let questions pull detail.
- **Two names, one thing** — breaks traceability; stable IDs reused everywhere.
- **Diagrams as one-off pictures** — no source of truth; diagrams as code, versioned in Git.

## Answer shape

A good "which framework" answer: (1) name the recommendation and the altitude it operates
at, (2) justify against the user's actual situation in 2–3 sentences, (3) name the first
concrete artifact and offer to produce it (route to the right mode), (4) name what to
deliberately skip. Keep the full survey for when the user explicitly asks to compare.
