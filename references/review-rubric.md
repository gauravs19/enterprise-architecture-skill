# Architecture Review & Assessment Rubric

Reviewing architecture means assessing a design against **objective quality attributes and
principles**, not personal taste, and returning findings the team can act on. A review that
says "looks good" or "I'd do it differently" is worthless. A good review gives evidence,
severity, and a concrete fix.

## Quality attributes (ISO/IEC 25010 + operational)

Assess the architecture against the attributes that matter *for this system* (don't grade
every system on every attribute — a batch job doesn't need sub-200ms latency). For each
relevant attribute, ask "does the design credibly achieve this, and how would we know?"

| Attribute | Ask | Common smells |
|---|---|---|
| **Functional suitability** | Does the structure actually support the required behavior? | Missing capability, awkward workarounds |
| **Performance efficiency** | Latency/throughput/resource targets met? Where are the bottlenecks? | Synchronous chains, N+1, no caching strategy, unbounded growth |
| **Compatibility / Interoperability** | Clean interfaces? Versioning? | Tight coupling, shared DB between services, no contract |
| **Usability / Operability** | Can it be operated, observed, supported? | No logging/metrics/tracing, no health checks, manual ops |
| **Reliability / Availability** | Failure handling, redundancy, recovery (RTO/RPO)? | Single points of failure, no retries/timeouts, no backups |
| **Security** | AuthN/Z, data protection, attack surface, secrets? | Secrets in code, no authz boundary, unencrypted PII, trust of input |
| **Maintainability** | Modularity, coupling/cohesion, testability, clarity? | Big ball of mud, circular deps, no tests, leaky abstractions |
| **Portability / Scalability** | Scale out? Cloud/infra portability? | Stateful where it should be stateless, vertical-only scaling |

Operational lenses to add: **cost** (is the design economical to run?), **evolvability**
(can it absorb the likely next change?), **data/privacy & compliance**, and
**team/Conway's-law fit** (does the structure match team boundaries?).

## EA principles to check (beyond per-system quality)

- **Separation of concerns / appropriate coupling** — boundaries align with change axes.
- **Single source of truth for data** — no conflicting masters; clear data ownership.
- **Explicit, versioned interfaces** between components/teams.
- **Standards over snowflakes** — reuse platform capabilities vs one-off builds.
- **Reversibility** — significant, hard-to-undo choices are recorded (ADRs) and justified.
- **Simplicity / YAGNI** — complexity is paid for by a real, present requirement, not a
  hypothetical. Over-engineering is a finding too.
- **Alignment to business capability** — components trace to a capability/goal they serve.

## The review process

1. **Establish what you're reviewing and against what.** Get the design (diagrams/docs/code)
   and the key requirements & quality goals. If quality goals are missing or vague, that's
   itself a Major finding — you can't assess fitness without them.
2. **Walk the structure top-down** (context → containers → components, or capability → app →
   tech). For each, probe the relevant quality attributes above.
3. **Look for what's *missing*, not just what's wrong** — the absent error path, the
   unhandled failure, the unscaled component, the undocumented decision. Omissions are the
   highest-value review findings.
4. **Categorize each finding by severity** and attach evidence + a concrete remediation.
5. **Give an overall verdict** and the top 3 things to fix first.

## Severity scheme

| Severity | Meaning | Examples |
|---|---|---|
| **Critical** | Will fail / breach in production; must fix before proceeding | SPOF on the critical path, plaintext secrets/PII, no auth on sensitive API, data-loss risk |
| **Major** | Serious risk to a key quality goal; fix before scaling/GA | No observability, synchronous coupling that won't meet latency SLO, missing quality goals |
| **Minor** | Real but bounded; fix when convenient | Inconsistent naming, missing index, light test coverage in a non-critical path |
| **Suggestion** | Improvement / future-proofing; optional | Consider extracting a module, document this decision as an ADR, simplify X |

## Output format (use this structure)

```markdown
# Architecture Review — <system / scope>
**Reviewed:** <what artifacts> · **Against:** <requirements / quality goals> · **Date:** <date>

## Verdict
<Approved | Approved with changes | Needs revision> — <one-sentence justification>

## Top priorities (fix first)
1. <the single most important thing>
2. …
3. …

## Findings

### 🔴 Critical
- **<title>** — <finding>. *Evidence:* <where/why in the design>. *Fix:* <concrete action>.

### 🟠 Major
- **<title>** — … *Evidence:* … *Fix:* …

### 🟡 Minor
- …

### 🔵 Suggestions
- …

## What's done well
<2–4 genuine strengths — balanced reviews get acted on; all-negative ones get defended against>

## Recommended follow-ups
- <e.g. "Record the datastore choice as an ADR" → hand off to Mode 2>
- <e.g. "Redraw the container diagram to show the message queue" → Mode 1>
```

## Common mistakes (in doing the review)

- **Taste masquerading as assessment** — "I prefer X" without tying to a quality attribute.
  Every finding must trace to an attribute, principle, or requirement.
- **No severity / no evidence / no fix** — a finding without all three isn't actionable.
- **Only listing problems** — note real strengths; it makes the critique credible and
  adopted.
- **Grading every system on every attribute** — assess against *this* system's actual
  quality goals; ignore irrelevant ones explicitly.
- **Reviewing the diagram instead of the architecture** — a pretty diagram can hide a SPOF;
  read for what *isn't* shown.
