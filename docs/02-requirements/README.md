# 02 --- Requirements

> **What must the system do, and what constraints must it satisfy?**

## Purpose

Turn agreed needs, objectives and constraints into clear, testable statements of what the system must do and how well it must perform.

## When Should It Be Created

Create this once the problem and intended outcomes are understood, before detailed design and implementation begin.

## When Should It Be Updated

Update it when needs, scope, constraints, risks or design discoveries change what the system must do or how well it must perform.

## Inputs

Use concept-stage needs, objectives, constraints and scenarios, plus stakeholder input, policies, standards and known technical limits.

## Activities

Write clear, testable requirements. Remove ambiguity, resolve conflicts, separate needs from solutions, and define measurable acceptance criteria.

## Outputs / Artefacts

Produce an agreed set of stakeholder, system and non-functional requirements, with IDs, sources, priorities and acceptance criteria.

The structure of `RequirementsTraceabilityMatrix.xlsx` is adapted from the
Requirements Verification Matrix in Appendix D, Table D-1 of the NASA
*Systems Engineering Handbook*, with additional lifecycle traceability informed
by systems and software engineering practice.

## Traceability

-   Give each requirement a stable ID, for example: stakeholder
    requirements (`STK-REQ-001`), system requirements (`SYS-REQ-001`),
    non-functional requirements (`NFR-001`).
-   Trace each requirement backward to the concept-stage need,
    objective, constraint or scenario that justifies it.
-   Trace derived and lower-level requirements to their parent
    requirements.
-   Reference requirement IDs from architecture/design, risks, V&V
    design and change records.
-   Maintain bidirectional traceability so that each requirement can be
    followed from its origin through implementation and evidence.
-   The purpose is to show **what must be satisfied, why it is required,
    and how satisfaction will later be demonstrated**.

## References

\[1\] National Aeronautics and Space Administration, *NASA Systems
Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC,
USA: NASA, 2016, Section 4.2, "Technical Requirements Definition",
pp. 54--62; Section 6.2, "Requirements Management", pp. 130--135; 
Appendix D, "Requirements Verification Matrix", Table D-1, pp. 201–202.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer,
*Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ,
USA: John Wiley & Sons, 2011, Chapter 7, "Concept Exploration",
pp. 165--194.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA:
Pearson, 2016, Chapter 4, "Requirements engineering", pp. 101--137.
