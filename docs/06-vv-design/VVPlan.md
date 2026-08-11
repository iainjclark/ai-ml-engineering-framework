# Verification & Validation Plan

> **How will we demonstrate that the system satisfies its requirements
> and intended use?**

This template is adapted from the Verification and Validation Plan
Outline in Appendix I of the *NASA Systems Engineering Handbook*,
simplified for lightweight AI/ML engineering practice.

## 1. Purpose and Scope

State what system, model, release or baseline this V&V Plan covers.

Describe the purpose of the planned verification and validation
activities and any important exclusions or limitations.

**System / project:** TODO\
**Baseline / version:** TODO\
**Plan owner:** TODO\
**Approval authority:** TODO\
**Date / status:** TODO

## 2. Applicable and Reference Information

Identify the controlled engineering information needed to understand and
execute this plan.

Typical inputs include:

-   stakeholder needs and intended-use statements;
-   system and ML requirements;
-   architecture and design descriptions;
-   data and model records;
-   risks and controls;
-   applicable standards, policies and constraints; and
-   relevant configuration or baseline information.

Where possible, refer to controlled artefacts rather than duplicating
their content here.

## 3. System and Intended-Use Context

Briefly describe the system being evaluated, its intended users and
operating environment, and the system boundary relevant to V&V.

Identify any architecture, interfaces, datasets, models or operational
conditions that materially affect the planned V&V activities.

## 4. V&V Approach

### 4.1 Verification

Verification asks whether the engineered system satisfies its specified
requirements.

Give each planned verification activity a stable identifier:

`VER-001`, `VER-002`, ...

For each activity, define the target, method, conditions, data,
acceptance criteria and evidence required before execution where
practicable.

### 4.2 Validation

Validation asks whether the system is suitable for stakeholder needs and
its intended use.

Give each planned validation activity a stable identifier:

`VAL-001`, `VAL-002`, ...

For each activity, define the stakeholder need, benefit or intended-use
claim being evaluated, the method and conditions of evaluation, and what
evidence would constitute adequate support.

### 4.3 Methods

Select methods appropriate to the claim being evaluated. These may
include:

-   test;
-   analysis;
-   inspection or review;
-   demonstration;
-   simulation;
-   comparison with reference data; and
-   operational or user evaluation.

Use combinations of methods where one method alone would not provide
adequate evidence.

## 5. Planned Verification Activities

Planned (and completed) verification activities are maintained in the `VER` sheet of
`VVRegister.xlsx`.

## 6. Planned Validation Activities

Planned (and completed) validation activities are maintained in the `VAL` sheet of
`VVRegister.xlsx`.

Validation criteria should reflect intended use and stakeholder
expectations, rather than merely restating technical requirements.

## 7. V&V Environment, Data and Dependencies

Describe resources needed to execute the plan, where material. This may
include:

-   datasets and reference data;
-   test or simulation environments;
-   software, models and configuration baselines;
-   instrumentation or monitoring;
-   human reviewers or domain specialists; and
-   external systems, services or interfaces.

Record important assumptions and dependencies that could affect the
validity or repeatability of the results.

## 8. Roles and Responsibilities

Identify who is responsible for planning, executing, reviewing and
approving V&V activities and evidence.

Where independence is important, state what level of independent review
is required.

## 9. Evidence and Traceability

Record executed results in the V&V evidence artefacts under
`09-vv-evidence`.

Maintain traceability sufficient to answer questions such as:

-   Which requirement or intended-use claim does this activity evaluate?
-   What method and acceptance criteria were agreed before execution?
-   What evidence was produced?
-   Did the evidence satisfy the acceptance criteria?
-   What risks, changes or follow-up actions arose from the result?

Typical traceability chains include:

`REQ-003` → `VER-004` → `EVID-005`

`BEN-001` → `VAL-002` → `EVID-009`

`RISK-003` → `CTRL-003` → `VER-007` → `EVID-016`

The Requirements Traceability Matrix and Validation Traceability Matrix
may be used to maintain these relationships.

## 10. Deviations, Changes and Re-V&V

Record material deviations from this plan and assess their impact.

Update the plan when requirements, risks, design, intended use,
available data, acceptance criteria or evidence needs materially change.

Where a controlled change affects previously accepted evidence, identify
which verification or validation activities must be repeated.

## 11. Completion and Approval

Before V&V is considered complete, confirm that:

-   planned activities have been executed or formally dispositioned;
-   required evidence has been recorded and reviewed;
-   acceptance criteria have been evaluated;
-   failures, anomalies and unresolved risks are visible;
-   required re-verification or re-validation has been identified; and
-   the evidence is sufficient to support the relevant release or
    assurance decision.

**V&V conclusion:** TODO\
**Open issues / exceptions:** TODO\
**Reviewed by:** TODO\
**Approved by:** TODO\
**Date:** TODO

## References

\[1\] National Aeronautics and Space Administration, *NASA Systems
Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC,
USA: NASA, 2016, Sections 5.3--5.4, "Product Verification" and "Product
Validation", pp. 88--106; Appendix I, "Verification and Validation Plan
Outline", p. 216 onward.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer,
*Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ,
USA: John Wiley & Sons, 2011, Section 4.5, "Testing throughout System
Development", pp. 103--106; Section 13.2, "Test Planning and
Preparation", pp. 450--455.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA:
Pearson, 2016, Chapter 8, "Software testing", pp. 226--254.
