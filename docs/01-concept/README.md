# 01 --- Concept

> **Why are we building this and for whom?**

## Purpose

Explain the problem, who it affects, the outcome sought, and why it matters. Avoid assuming a particular solution too early.

## When Should It Be Created

Create this at the start of significant work, before any detailed requirements or specific design decisions are locked in.

## When Should It Be Updated

Update it when the problem, users, objectives, scope, constraints or operating context materially change.

## Inputs

Use records of stakeholder discussions, business goals, current processes, known constraints, relevant data and operational experience.

## Activities

Clarify the problem, users, needs, objectives, constraints, scope and key usage scenarios. Challenge assumptions and record open questions.

## Outputs / Artefacts

Capture the agreed needs, objectives, constraints, scenarios, scope, assumptions and unresolved questions for later engineering work.

## Traceability

- Give important concept-stage items stable IDs, for example:
  - stakeholder needs (`NEED-001`), objectives (`OBJ-001`), constraints (`CON-001`), operational scenarios (`SCN-001`)
- Reference these IDs when creating requirements.
- Reference the relevant requirements in later design decisions, risks and V&V activities.
- Maintain enough linkage to trace:
  - forward: need → requirement → design → V&V evidence
  - backward: V&V evidence → design → requirement → original need
- The purpose is to contextualise **why each important engineering requirement, decision and test exists**.

## References

\[1\] National Aeronautics and Space Administration, *NASA Systems Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC, USA: NASA, 2016, Section 2.2, "An Overview of the SE Engine by Project Phase", pp. 8--24; Section 4.1, "Stakeholder Expectations Definition", pp. 45--53; Appendix S, "Concept of Operations Annotated Outline", pp. 251--253.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer, *Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ, USA: John Wiley & Sons, 2011, Chapter 6, "Needs Analysis", pp. 139--164.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA: Pearson, 2016, Section 19.2, "Conceptual design", pp. 563--566.