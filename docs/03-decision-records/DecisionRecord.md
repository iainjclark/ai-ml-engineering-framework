# Decision Record

Typical usage: `DEC-001.md`, `DEC-002.md`, ...

## Document Control

Decision ID: `DEC-###`\
System / Project:\
Version:\
Status: Proposed / Approved / Superseded / Rejected\
Date:\
Owner:\
Approved by:

## Decision

State the engineering decision clearly and concisely.

**Decision:** We will ...

## Context

Describe the problem, need or engineering choice that requires a
decision.

Explain why the decision matters and identify the part of the system,
project or lifecycle that it affects.

Reference relevant `REQ-###`, `BEN-###`, `NEED-###`, `RISK-###`,
`CTRL-###`, `DATA-###`, `MODEL-###` or other lifecycle identifiers where
applicable.

## Decision Drivers and Constraints

Record the criteria, assumptions and constraints that materially affect
the decision.

Examples may include:

-   requirements and stakeholder needs
-   performance or technical constraints
-   risk and assurance considerations
-   cost and schedule
-   data availability and quality
-   operational environment
-   maintainability and support
-   security, privacy, legal or regulatory obligations
-   existing architecture or technology constraints

## Alternatives Considered

### Option 1 --- \[Name\]

**Description:**

**Advantages:**

-   ...

**Disadvantages / Risks:**

-   ...

**Evidence / References:**

### Option 2 --- \[Name\]

**Description:**

**Advantages:**

-   ...

**Disadvantages / Risks:**

-   ...

**Evidence / References:**

### Option 3 --- \[Name, if required\]

**Description:**

**Advantages:**

-   ...

**Disadvantages / Risks:**

-   ...

**Evidence / References:**

Add or remove options as appropriate. Record credible alternatives
rather than creating artificial options simply to complete the template.

## Analysis and Trade-offs

Compare the alternatives against the decision drivers and available
evidence.

Record the important trade-offs, uncertainties and assumptions. Use a
formal trade study, scoring model, experiment or other supporting
analysis where the importance or complexity of the decision warrants it.

Supporting calculations, tables, notebooks or other evidence may be
linked rather than reproduced here.

## Rationale

Explain why the selected option is preferred.

The rationale should make clear how the evidence and trade-offs led to
the decision, including any important disadvantages or residual
uncertainty that have been accepted.

## Consequences

Record the material consequences of the decision.

**Expected benefits:**

-   ...

**Costs / disadvantages:**

-   ...

**Risks introduced or changed:**

-   ...

**Follow-up actions:**

-   ...

## Verification and Review

Describe how the consequences or assumptions underlying this decision
will be checked, where appropriate.

Reference planned verification or validation activities (`VER-###`,
`VAL-###`) and resulting evidence (`EVID-###`) where applicable.

State any event, evidence or threshold that should trigger
reconsideration of the decision.

## Status and Supersession

**Status:** Proposed / Approved / Superseded / Rejected

**Supersedes:** `DEC-###` / None

**Superseded by:** `DEC-###` / None

Do not rewrite historical decision records merely because the preferred
engineering choice later changes. Preserve the original record and link
it to the superseding decision.

## Decision History

Record material events affecting the decision after it was made. Do not record
routine project activity here.

| Date | Event / New Evidence | Impact on Decision | Action / Reference |
|---|---|---|---|
| YYYY-MM-DD | | None / Review / Supersede | |

## Traceability

Give each material engineering decision a stable `DEC-###` identifier.

Trace the decision backward to the requirements, needs, benefits,
constraints, risks or other evidence that created the need for the
decision.

Trace the selected outcome forward to architecture and design
(`ADD-###`), controls, implementation, V&V activities and other
artefacts that depend on the decision.

The purpose is to show **what was decided, what alternatives were
considered, why the decision was made, and what evidence supported it**.

## References

See the `03-decision-records/README.md` for the engineering references
and guidance informing this template. For specific project decisions,
cite the technical evidence, standards, analyses and other sources
actually used to make the decision.
