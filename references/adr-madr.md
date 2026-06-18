# Architecture Decision Records (ADR / MADR)

An ADR captures **one architecturally significant decision** and, crucially, *the reasoning
and the options considered* — the context a future reader cannot reconstruct from the code.
A decision is "architecturally significant" if it's costly to reverse, affects structure,
non-functional qualities, dependencies, or interfaces.

> The value of an ADR is the **trade-off**, not the answer. "We chose Postgres" is trivia;
> "we chose Postgres over DynamoDB because our access patterns are relational and we valued
> ad-hoc querying over single-digit-ms scale we don't need yet" is architecture.

## Two formats — pick one and stay consistent

### MADR (Markdown Any Decision Records) — recommended default

Richer; makes the options explicit. Use for non-trivial decisions.

```markdown
# NNNN. <short decision title in imperative, e.g. "Use Kafka for order events">

- Status: proposed | accepted | rejected | deprecated | superseded by ADR-XXXX
- Date: YYYY-MM-DD
- Deciders: <names/roles>
- Tags: <area, e.g. messaging, data>

## Context and Problem Statement

<2–4 sentences. What's the situation and the question we must answer? What forces are at
play? Link the driving requirement or quality goal.>

## Decision Drivers

- <driver / force / constraint 1, e.g. "must handle 10k events/s">
- <driver 2, e.g. "team has no Kafka ops experience">

## Considered Options

1. <Option A>
2. <Option B>
3. <Option C>

## Decision Outcome

Chosen option: "<Option X>", because <justification tied to the drivers>.

### Consequences

- Good: <positive consequence>
- Good: <positive consequence>
- Bad: <negative consequence / cost / new risk we accept>
- Neutral: <follow-on work, things to revisit>

## Pros and Cons of the Options

### <Option A>
- Good: <…>
- Bad: <…>

### <Option B>
- Good: <…>
- Bad: <…>

## More Information

<links: related ADRs, the arc42 §9 entry, splikes/benchmarks, the PR>
```

### Nygard (lightweight) — for fast, small decisions

The original minimal form. Five headings:

```markdown
# NNNN. <title>

## Status
Accepted

## Context
<the forces: technical, political, social, project-local>

## Decision
<what we will do, in active voice: "We will …">

## Consequences
<what becomes easier or harder as a result — both directions>
```

## Conventions

- **Numbering:** zero-padded sequential, `0001-`, `0002-`. Filenames:
  `NNNN-kebab-case-title.md` in `docs/decisions/` (or `docs/adr/`).
- **Immutable:** once accepted, don't rewrite an ADR. To change a decision, write a **new**
  ADR and set the old one's status to `superseded by ADR-XXXX` (and link back).
- **One decision per record.** If you're tempted to use "and" in the title, it's two ADRs.
- **Status lifecycle:** proposed → accepted → (later) deprecated / superseded. `rejected`
  is valuable too — record decisions you *considered and declined*, with why.
- **Link from arc42 §9** (Architecture Decisions) rather than duplicating the content.
- **Keep an index** — `docs/decisions/README.md` listing number, title, status, date —
  or generate it with the `adr-tools` CLI (open source) if the user uses it.

## When to write one (and when not)

Write an ADR for: choosing a datastore / messaging / framework, defining a module boundary
or API contract, adopting a cross-cutting pattern (auth, error handling), a build-vs-buy
call, a significant trade-off between quality attributes.

Skip it for: reversible, local, low-stakes choices (variable naming, a single function's
implementation). ADR sprawl devalues the record; reserve them for decisions worth the
reader's time.

A copy of the MADR template is in `assets/templates/adr-madr.md`.
