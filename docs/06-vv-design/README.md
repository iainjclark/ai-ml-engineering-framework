# 06 --- V&V Design

> **How will we demonstrate that the system satisfies its requirements and intended use?**

## Purpose

Plan how the system will be checked against its requirements and intended use, including what evidence will count as acceptable.

## When Should It Be Created

Create this before testing or validation begins, early enough for evidence needs to influence design, data collection and implementation.

## When Should It Be Updated

Update it when requirements, risks, design, intended use, available data or evidence needs materially change.

## Inputs

Use requirements, stakeholder needs, architecture, risks, controls, assumptions, intended-use scenarios and available test or validation data.

## Activities

Define what will be checked, how, under what conditions, using which data, and against what acceptance criteria. Cover important failure cases.

## Outputs / Artefacts

Produce a V&V Plan describing the V&V strategy, scope, methods, responsibilities and governance.

Maintain planned verification and validation activities in `VVRegister.xlsx`,
including their targets, methods, conditions, data, acceptance criteria and
planned evidence. Actual evidence is linked when activities are executed in
`09-v&v-evidence`.

The structure of the V&V Plan used in this framework is adapted from the
Verification and Validation Plan Outline in Appendix I of the NASA Systems
Engineering Handbook, simplified for lightweight AI/ML engineering practice.
Kossiakoff et al. and Sommerville provide supporting guidance on test planning
and software testing respectively.

## Traceability

-   Give each planned verification or validation activity a stable ID,
    for example: verification (`VER-001`) and validation (`VAL-001`).
-   Trace every V&V activity to the requirement, stakeholder
    expectation, risk control or assurance claim it is intended to
    evaluate.
-   Define the method, conditions, data, acceptance criteria and
    required evidence before execution where practicable.
-   Distinguish verification of specified requirements from validation
    of stakeholder needs and intended use.
-   Link executed activities and results to the corresponding records in
    `09-v&v-evidence`.
-   The purpose is to show **what evidence will count as adequate proof
    before the results are known**.

## References - Core

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

\[4\] INCOSE, *Systems Engineering Handbook: A Guide for System Life Cycle
Processes and Activities*, 5th ed. Hoboken, NJ, USA: John Wiley & Sons,
2023. 

\[5\] H. Washizaki, ed., *Guide to the Software Engineering Body of
Knowledge (SWEBOK Guide)*, Version 4.0a. Los Alamitos, CA, USA: IEEE
Computer Society, 2025. 

## References - Optional / Specialist

\[6\] W. L. Oberkampf and C. J. Roy, *Verification and Validation in Scientific
Computing*. Cambridge, UK: Cambridge University Press, 2010, Chapter 2,
“Fundamental Concepts and Terminology,” pp. 21–75; Chapter 10, “Model
Validation Fundamentals,” pp. 371–405; Chapter 11, “Design and Execution
of Validation Experiments,” pp. 409–465.

\[7\] B. J. Taylor, ed., *Methods and Procedures for the Verification and
Validation of Artificial Neural Networks*. New York, NY, USA: Springer, 2006.

