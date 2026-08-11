# 04 --- Architecture & Design

> **How will the system be structured and how will it work?**

## Purpose

Describe how the system will be structured and how its parts, data and interfaces will work together to satisfy the requirements.

## When Should It Be Created

Create this once key requirements and major design choices are understood, before implementation becomes difficult to change.

## When Should It Be Updated

Update it when requirements, interfaces, components, data flows, dependencies or major technical decisions materially change.

## Inputs

Use requirements, decision analyses, constraints, risks, existing systems, interface needs and relevant technical standards.

## Activities

Define components, responsibilities, interfaces and data flows. Check that the design covers requirements, risks and important failure modes.

## Outputs / Artefacts

Produce architecture diagrams and design descriptions showing components, interfaces, data flows, dependencies and key design choices.

Use `ArchitectureDesignDescription.md` to record the boundary, components,
interfaces, human actors, data and model flows, trust boundaries, failure modes,
observability, fallback and recovery for an `ADD-###` artefact.

## Traceability

-   Give important architecture and design descriptions stable IDs,
    for example (`ADD-001`).
-   Trace architecture and design elements back to the requirements they
    satisfy and the decisions that selected them.
-   Trace derived requirements and interface constraints to the design
    elements that generated them.
-   Reference relevant risks, assumptions and V&V activities from the
    affected design elements.
-   Maintain enough linkage to show the path: requirement → decision →
    architecture/design → implementation → V&V evidence.
-   The purpose is to show **how the proposed technical solution
    satisfies the requirements and where each important design choice
    came from**.

## References

\[1\] National Aeronautics and Space Administration, *NASA Systems
Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC,
USA: NASA, 2016, Sections 4.3--4.4, "Logical Decomposition" and "Design
Solution Definition", pp. 62--76.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer,
*Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ,
USA: John Wiley & Sons, 2011, Chapter 8, "Concept Definition",
pp. 197--252; Chapter 12, "Engineering Design", pp. 409--442.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA:
Pearson, 2016, Chapter 5, "System modeling", pp. 138--166; Chapter 6,
"Architectural design", pp. 167--195.
