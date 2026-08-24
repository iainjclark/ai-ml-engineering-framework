# Concept of Operations (CONOPS)

Typical usage: `ConceptOfOperations.md` or, where multiple concepts are
maintained, `CONOPS-001.md`, `CONOPS-002.md`, ...

## Document Control

CONOPS ID: `CONOPS-###`\
System / Project:\
Concept / Version:\
Status: Draft / Under Review / Approved / Superseded\
Date:\
Owner:\
Approved by:

## 1. Purpose

Describe the proposed operational capability in plain language.

Explain:

-   what problem or opportunity is being addressed
-   why a new or changed AI/ML capability is being considered
-   who will use, operate, support or be affected by it
-   what operational outcome the concept is intended to enable

Keep this section focused on **what the system is for and how it is
expected to be used**, rather than prescribing detailed design.

Reference relevant `BEN-###`, `PC-###` and `NEED-###` records where they
already exist.

## 2. Operational Context

Describe the environment in which the capability is expected to operate.

Consider, where relevant:

-   organisation / business process
-   users and operators
-   upstream and downstream systems
-   external services or data providers
-   physical or technical operating environment
-   regulatory, policy or contractual context
-   operational timing, frequency or availability expectations
-   important organisational or human dependencies

A simple system-context diagram may be included where it helps
communicate the concept.

## 3. Stakeholders and Operational Roles

Identify the principal stakeholders and their relationship to the
proposed capability.

  -----------------------------------------------------------------------
  Stakeholder /     Operational       Interaction /     Related Need
  Role              Interest          Responsibility    
  ----------------- ----------------- ----------------- -----------------
                                                        `NEED-###`

  -----------------------------------------------------------------------

Include only stakeholders that materially affect the operational
concept. Detailed stakeholder needs may be maintained in the Stakeholder
& Operational Needs Register.

## 4. Current Situation

Briefly describe how the relevant activity is performed today.

Record:

-   current process or system
-   important pain points or limitations
-   manual activities
-   existing models, tools or decision processes
-   known constraints
-   reason for considering change

This section provides the baseline against which the proposed
operational concept can be understood.

## 5. Proposed Operational Concept

Describe how the proposed capability is expected to work from an
operational perspective.

Explain:

-   what initiates the process
-   what information enters the system
-   what the AI/ML capability does at a high level
-   what outputs are produced
-   who or what receives those outputs
-   where human judgement, approval or intervention occurs
-   what happens when the system cannot produce an acceptable result
-   how the capability fits into the wider operational workflow

Avoid committing prematurely to algorithms, platforms or implementation
details unless they are genuine constraints on the concept.

## 6. Operational Scenarios

Use a small number of representative scenarios to make the concept
concrete.

### Scenario 1 --- Normal Operation

**Scenario ID:** `CON-###`\
**Actors:**\
**Trigger:**\
**Preconditions:**

**Operational flow:**

1.  ...
2.  ...
3.  ...

**Expected outcome:**

### Scenario 2 --- Exception / Degraded Operation

**Scenario ID:** `CON-###`\
**Actors:**\
**Trigger:**\
**Preconditions:**

**Operational flow:**

1.  ...
2.  ...
3.  ...

**Expected outcome / fallback:**

Add further scenarios only where they expose materially different
operational needs, constraints or failure behaviour.

## 7. Operational Objectives and Success

State the important operational objectives of the concept.

  -----------------------------------------------------------------------
  Objective ID      Operational       Success Indicator Related Benefit /
                    Objective         / Measure         Need
  ----------------- ----------------- ----------------- -----------------
  `OBJ-###`                                             `BEN-###` /
                                                        `NEED-###`

  -----------------------------------------------------------------------

Objectives should describe useful operational outcomes rather than
implementation features.

## 8. Operational Needs and Constraints

Summarise the needs and constraints that materially shape the concept.

Examples may include:

-   response time or availability
-   data availability or freshness
-   human review requirements
-   explainability or auditability
-   privacy, security or safety
-   regulatory obligations
-   deployment environment
-   integration constraints
-   operating cost
-   skills / support availability
-   acceptable degraded modes

Use stable `NEED-###` identifiers where individual traceability is
useful. Detailed needs should be maintained in the Stakeholder &
Operational Needs Register rather than duplicated here.

## 9. Assumptions and Dependencies

Record assumptions on which the operational concept depends.

  ID   Assumption / Dependency   Consequence if False   Owner / Source
  ---- ------------------------- ---------------------- ----------------
                                                        

Material assumptions should later be reflected in requirements, risks,
decisions or V&V activities where appropriate.

## 10. Operational Risks and Limitations

Identify major concept-level risks, limitations or foreseeable misuse
that should influence subsequent engineering.

Do not reproduce the Risk Register. Summarise the issues that are
important to understanding whether the concept is viable and reference
`RISK-###` records where available.

Consider:

-   inappropriate reliance on model outputs
-   unsuitable or unavailable data
-   operation outside the intended domain
-   automation bias
-   failure or degradation of dependent services
-   unacceptable latency or availability
-   inability to monitor performance
-   inability to intervene safely

## 11. Boundaries and Out-of-Scope Uses

State clearly what the proposed capability does **not** cover.

Include:

-   excluded users or populations
-   excluded decisions or use cases
-   operating conditions outside the concept
-   responsibilities retained by humans or other systems
-   capabilities intentionally deferred

Clear boundaries help prevent later requirements and design work from
silently expanding the intended system.

## 12. Transition to Engineering

Record the principal engineering work that follows from this concept.

Reference or identify:

-   stakeholder / operational needs requiring elaboration
-   benefits to be realised
-   requirements to be derived
-   decisions or trade studies required
-   architecture/design questions
-   major risks requiring treatment
-   V&V questions that must eventually be answered

A typical traceability path is:

`CONOPS / CON-###` → `NEED-###` → `BEN-###` → `REQ-###` → `DEC-###` →
design → `VER-###` / `VAL-###` → `EVID-###`

The CONOPS should establish **the operational problem, intended
capability and operating context**. It should not attempt to replace the
requirements specification or architecture/design description.

## 13. Open Questions

Record unresolved concept questions that materially affect subsequent
work.

  ID   Question   Owner   Resolution / Related Decision
  ---- ---------- ------- -------------------------------
                          `DEC-###`

Remove resolved questions or preserve their resolution through the
appropriate controlled engineering artefact.

## 14. References

See the `01-concept/README.md` for the systems-engineering references
and guidance informing this template.

For specific projects, cite the business case, policies, operational
procedures, stakeholder material, existing-system documentation,
data-source documentation and other sources actually used to define the
operational concept.
