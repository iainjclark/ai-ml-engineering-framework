# 04 --- Architecture & Design

> **How will the system be structured and how will it work?**

## Purpose

Describe how the system will be structured and how its parts, data and interfaces will work together to satisfy the requirements.

## When Should It Be Created

Create this once key requirements and major design choices are understood, before implementation becomes difficult to change.

## When Should It Be Updated

Update it when requirements, interfaces, components, data flows, dependencies or major technical decisions materially change.

## Inputs

Use requirements, decision analyses, constraints, risks, existing systems, interface needs and relevant technical standards, source data assets, 
source systems and applicable data-use constraints.

## Activities

Define components, responsibilities, interfaces and data flows. Check that the design covers requirements, risks and important failure modes.

## Outputs / Artefacts

Produce architecture diagrams and design descriptions showing components, interfaces, data flows, dependencies and key design choices.
Where significant external or source data is used, maintain a Data Provenance Record (DATA-###) identifying its origin, intended use,
acquisition context, version, restrictions, classification and project ownership.

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
-   Trace significant source data assets (DATA-###) to the requirements, 
    design elements, data-quality assessments and downstream models or 
	analyses that depend on them.

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

\[4\] OASIS, *Data Provenance Metadata Version 1.0*, Committee Specification Draft 02,
30 June 2026. https://docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.html 