# 08 --- V&V Evidence

> **Did the system actually satisfy its requirements and intended use?**

## Purpose

Record what verification and validation actually showed, including failures, uncertainty and whether agreed acceptance criteria were met.

## When Should It Be Created

Create evidence records as planned V&V activities are performed, using the approved methods, conditions and acceptance criteria.

## When Should It Be Updated

Update them when activities are repeated, corrected or extended, or when findings are resolved or new evidence changes the conclusion.

## Inputs

Use the V&V plan, controlled system baseline, approved data, test procedures, acceptance criteria and records of actual execution conditions.

## Activities

Perform the planned checks and record actual results, conditions, deviations, failures and uncertainty. Compare results with acceptance criteria.

## Outputs / Artefacts

Produce V&V evidence records showing what was tested or validated, what happened,
whether it passed and what remains unresolved.

Maintain executed verification and validation evidence in `VVEvidenceRegister.xlsx`,
giving each evidence item a stable `EVID-###` identifier and recording the
corresponding V&V activity, configuration, actual conditions, results,
acceptance outcome, deviations, supporting artefacts and disposition.

Use `RequirementsTraceabilityMatrix.xlsx` to maintain verification traceability
from requirements through planned verification activities to evidence
(`REQ ↔ VER ↔ EVID`).

Use `ValidationTraceabilityMatrix.xlsx` to maintain validation traceability from
stakeholder needs or benefits through planned validation activities to evidence
(`BEN / NEED ↔ VAL ↔ EVID`).

The structure of `ValidationTraceabilityMatrix.xlsx` is adapted from the
Validation Requirements Matrix in Appendix E, Table E-1 of the NASA
*Systems Engineering Handbook*, with additional lifecycle traceability informed
by systems and software engineering practice.

The structure of the V&V Evidence Register is adapted primarily from
Table 5.3-1, "Example information in Verification Procedures and Reports",
of the NASA *Systems Engineering Handbook*, simplified for lightweight
AI/ML engineering practice. Kossiakoff et al. provide supporting guidance
on test reporting, analysis, deficiencies and evaluation.

## Traceability

- Give each evidence item a stable `EVID-###` identifier.
- Link each `EVID-###` item to the corresponding `VER-###` or `VAL-###`
  activity defined in `06-v&v-design`.
- Trace verification evidence back through `VER-###` to the requirement
  being verified.
- Trace validation evidence back through `VAL-###` to the stakeholder
  need, benefit or intended use being validated.
- Link results to relevant risk controls or assurance claims where applicable.
- Record actual conditions, data/configuration versions, results,
  deviations, failures and disposition.
- Preserve failed and inconclusive results as part of the engineering
  record; do not retain only successful evidence.
- Link unresolved findings to change records, risks, decisions or
  release constraints.
- The purpose is to show **what was actually demonstrated, under what
  conditions, and whether the pre-defined acceptance criteria were met**.

## References

\[1\] National Aeronautics and Space Administration, *NASA Systems
Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC,
USA: NASA, 2016, Sections 5.3--5.4, "Product Verification" and "Product
Validation", pp. 88--106; Table 5.3-1, "Example information in Verification
Procedures and Reports", p. 94; Appendix E, "Creating the Validation Plan
with a Validation Requirements Matrix", Table E-1, pp. 203--204.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer,
*Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ,
USA: John Wiley & Sons, 2011, Chapter 13, "Integration and Evaluation",
pp. 443--478.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA:
Pearson, 2016, Chapter 8, "Software testing", pp. 226--254.

## References - Optional / Specialist

\[4\] W. L. Oberkampf and C. J. Roy, *Verification and Validation in Scientific
Computing*. Cambridge, UK: Cambridge University Press, 2010, Chapter 7,
“Solution Verification,” pp. 250–284; Chapter 12, “Model Accuracy Assessment,”
pp. 469–548; Chapter 13, “Predictive Capability,” pp. 555–665.
