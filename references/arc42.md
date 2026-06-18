# arc42 — Architecture Documentation

arc42 is a lightweight, battle-tested **template** for documenting software/system
architecture. Twelve sections, each answering a specific question. It's documentation as
code: plain Markdown/AsciiDoc in the repo, diagrams embedded as C4/PlantUML.

## The detail-level knob

Don't write the same depth for every section or every system. Pick a target level with the
user (or infer from the stakes) and write to it:

- **LEAN** — a one-pager / a few paragraphs per relevant section. Startups, internal tools,
  early-stage. Skip sections that don't apply (say so explicitly rather than padding).
- **ESSENTIAL** — the default. Each section has real content; diagrams in §3, §5, §6, §7;
  decisions recorded. Good for most production systems.
- **THOROUGH** — full treatment, all sections, multiple views, quality scenarios,
  risk register. Regulated/critical/large systems.

A 40-page document nobody reads is a failure mode, not thoroughness. Write the minimum that
lets a new engineer become productive and a reviewer assess soundness.

## The discover → generate → validate loop

For each section: **ask the few questions you genuinely need**, generate to the target
detail level, then self-check against the section's purpose. Don't invent facts — if
something is unknown, mark it `TODO` / `(to be decided)` rather than fabricating.

## The 12 sections

| # | Section | Question it answers | Watch out for |
|---|---|---|---|
| 1 | **Introduction & Goals** | What must the system do? Top quality goals? Stakeholders? | Quality goals must be **measurable** (see below) |
| 2 | **Constraints** | What limits the design? (tech, org, legal, conventions) | Distinguish real constraints from preferences |
| 3 | **Context & Scope** | What's in scope; who/what does it talk to? | This is a **C4 System Context** diagram + external interfaces table |
| 4 | **Solution Strategy** | The big decisions in a nutshell | Key tech choices, top patterns, how quality goals are met — short |
| 5 | **Building Block View** | Static structure, decomposed | **C4 Container/Component**; one diagram per level of zoom |
| 6 | **Runtime View** | How do building blocks collaborate at runtime? | Sequence/flow for the few important scenarios, not all |
| 7 | **Deployment View** | What runs on what infrastructure? | Nodes, environments; C4 deployment or ArchiMate tech layer |
| 8 | **Crosscutting Concepts** | Recurring patterns/rules (security, logging, errors, i18n, persistence) | The "how we do X everywhere" section |
| 9 | **Architecture Decisions** | Why the important choices were made | **Link ADRs here** (see adr-madr.md); don't duplicate |
| 10 | **Quality Requirements** | Quality tree + concrete scenarios | Scenarios with stimulus → measurable response |
| 11 | **Risks & Technical Debt** | Known risks and debt, with mitigation | Be honest; this section builds trust |
| 12 | **Glossary** | Domain & technical terms | Kills the "two names for one thing" problem |

### Measurable quality goals (§1.2 and §10)

Reject vague adjectives. Turn "must be fast / secure / scalable" into **quality scenarios**:

- ❌ "The system should be fast."
- ✅ "Under 1000 concurrent users, the checkout API responds to *place order* in <200ms at
  the 95th percentile."
- ✅ "A new developer can set up the dev environment and run the test suite in under 30
  minutes following the README."

Scenario shape: **(source) stimulus → (under) environment/condition → (system) response →
response measure.** This is what makes §10 reviewable and ties to the review rubric.

## Structure on disk

```
docs/architecture/
├── 01-introduction-goals.md
├── 02-constraints.md
├── 03-context-scope.md          # embeds context.puml / .dsl
├── ...
├── 09-decisions.md              # links to ../decisions/NNNN-*.md (ADRs)
├── 10-quality.md
├── diagrams/                    # .puml / .dsl / .mmd — referenced, not inlined
└── decisions/                   # ADRs (see adr-madr.md)
```

Keep diagrams as separate files referenced from the Markdown (renderable independently,
diffs stay clean) when a repo exists; inline them otherwise.

## Common mistakes

- **Padding every section equally** — pick a detail level; mark non-applicable sections
  "not applicable because …" instead of waffling.
- **Vague quality goals** — see above; always measurable scenarios.
- **Duplicating decisions** — §9 *links* ADRs, it doesn't restate them.
- **Prose where a diagram belongs** — §3/§5/§7 are diagram-first.
- **Stale docs** — keep it in the repo next to the code so it's reviewed in PRs; that's the
  whole point of docs-as-code.

A starter skeleton lives in `assets/templates/arc42-section.md`.
