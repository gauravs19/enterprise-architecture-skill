# TOGAF ADM

TOGAF (The Open Group Architecture Framework) is a **method**, not a notation. Its core is
the **ADM — Architecture Development Method**: a cycle of phases for delivering an
architecture change with governance. Use it to *structure an engagement*, decide *what
deliverables to produce*, and *govern* the work. It pairs naturally with ArchiMate (the
notation for the models TOGAF asks you to produce) and ADRs (the decisions you record).

> Don't ceremonially run all phases for a small change. TOGAF is meant to be *tailored* —
> scale the rigor to the stakes. For a one-team service, a light pass through Vision →
> Architectures → Roadmap is plenty. For an enterprise transformation, do it properly.

## The ADM cycle

```
        Preliminary (set up the practice: principles, frameworks, tools)
                              │
   ┌──────────────────────── A. Architecture Vision ───────────────────────┐
   │                                                                        │
 H. Architecture          B. Business Architecture                         │
    Change Mgmt                      │                                       │
   │                     C. Information Systems Architecture                │
 G. Implementation               (Data + Application)                       │
    Governance                       │                                       │
   │                     D. Technology Architecture                         │
 F. Migration Planning              │                                       │
   │                     E. Opportunities & Solutions                      │
   └───────────────────── (Requirements Mgmt at the centre) ───────────────┘
```

**Requirements Management** sits at the hub — every phase feeds and is checked against
requirements.

## The phases, and what each produces

| Phase | Purpose | Key deliverables / outputs |
|---|---|---|
| **Preliminary** | Establish the architecture capability | Architecture principles, governance, tailored framework, tool selection |
| **A. Vision** | Scope, stakeholders, value, get buy-in | Statement of Architecture Work, Architecture Vision, stakeholder map, high-level value |
| **B. Business** | Target business architecture | Capability map, value streams, org/process models, business services, gaps |
| **C. Information Systems** | Data + Application architecture | Application landscape, data models, app/data gaps, integration |
| **D. Technology** | Tech/platform architecture | Technology architecture, infra/platform standards, tech gaps |
| **E. Opportunities & Solutions** | Group gaps into deliverable work | Work packages, candidate solutions, implementation & migration strategy, Transition Architectures |
| **F. Migration Planning** | Sequence & cost the roadmap | Architecture Roadmap, Implementation & Migration Plan, prioritized projects |
| **G. Implementation Governance** | Govern delivery to the architecture | Architecture Contracts, compliance reviews, governance decisions |
| **H. Change Management** | Manage change & decide re-architecting | Change requests, impact assessments, triggers for a new cycle |
| **Requirements Mgmt** | Continuous req handling across all phases | Requirements repository, change log |

## Foundational concepts you'll reference

- **Baseline vs Target architecture** — every phase produces a *current state* and a
  *desired state*; the difference is the **gap analysis**, which feeds the roadmap. Always
  frame B/C/D as Baseline → Target → Gaps.
- **Transition Architectures** — intermediate, deliverable states between Baseline and
  Target (you rarely jump in one step). These become the **plateaus** in ArchiMate.
- **Architecture Building Blocks (ABBs)** vs **Solution Building Blocks (SBBs)** — abstract
  capabilities vs concrete products/components that implement them.
- **Architecture Repository / Continuum** — where all artifacts live and get reused, from
  generic foundation architectures to organization-specific ones.
- **Architecture principles** — durable rules (e.g. "buy before build", "data is an
  asset") with statement / rationale / implications. Set in Preliminary, applied
  throughout. Record significant principle-level choices as ADRs.

## Using TOGAF in this skill (Mode 4)

When the user wants to *run or structure* an architecture engagement, or model the
enterprise:

1. **Frame the work with Vision (Phase A)** — capture scope, stakeholders, drivers, and a
   one-paragraph vision before drawing anything. Most failed architecture efforts skipped
   this.
2. **Walk B → C → D top-down**, each as Baseline → Target → Gaps, producing **ArchiMate**
   models (capability map and business services for B; application/data landscape for C;
   technology nodes for D). Draw the **realization links** between them.
3. **Turn gaps into work packages (E)** and sequence them into a **roadmap with
   Transition Architectures / plateaus (F)**.
4. **Record decisions as ADRs** and durable rules as **architecture principles**.

### Portfolio rationalization (TIME model)

When assessing an application portfolio, score each app on **business value** and
**technical fit**, then place it in the TIME quadrant and recommend an action:

| | Low technical fit | High technical fit |
|---|---|---|
| **High business value** | **Migrate** (re-platform / re-architect) | **Invest** (enhance, strategic) |
| **Low business value** | **Eliminate** (retire/replace) | **Tolerate** (keep, minimal spend) |

Present this as a table per application with the two scores, the quadrant, and a one-line
rationale + recommended next step. This is the most common concrete EA deliverable a
business actually asks for.

## Common mistakes

- **Treating TOGAF as a notation** — it's a process; ArchiMate is the notation. Produce
  the *models* in ArchiMate/C4, use TOGAF to decide *which* models and *why*.
- **Running every phase ceremonially** for a small change — tailor it.
- **Skipping Vision** — diving into diagrams without agreed scope/stakeholders/value.
- **Target with no Baseline or no Gaps** — the deliverable is the *delta and roadmap*, not
  a pretty future-state picture.
- **No governance loop** — producing architecture nobody is held to (Phase G exists for a
  reason).
