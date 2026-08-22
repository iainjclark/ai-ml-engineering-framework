# 03 --- Decision Records

> **What alternatives exist, what did we decide, and why?**

## Purpose

Maintain an authoritative current and historical record of important engineering
decisions, together with the alternatives considered, evaluation criteria,
analysis, evidence, assumptions, uncertainties and rationale for the selected
outcome.

The intent is to preserve both how a decision was reached and what was ultimately
decided in a single controlled record.

## When Should It Be Created

Create a decision record when making a material engineering choice where credible
alternatives exist and the outcome affects requirements, risk, performance,
architecture, design, implementation, cost, schedule or operation.

Create the record early enough for the analysis to inform the decision rather than
being reconstructed after the decision has already been made.

## When Should It Be Updated

Update the record when new evidence, requirements, risks, constraints or
alternatives materially affect the decision, or when the decision is approved,
rejected, deferred, changed or superseded.

Do not silently overwrite earlier decisions. Preserve the engineering history and
identify the relationship between superseded and superseding decisions.

## Inputs

Use relevant requirements, constraints, risks, assumptions, technical evidence,
costs, data, architecture/design information, operational considerations,
lessons from comparable work and the authority responsible for the decision.

## Activities

Define the decision or problem requiring resolution and identify credible
alternatives and evaluation criteria. Compare the alternatives using appropriate
evidence and analysis, recording important assumptions, uncertainties and
trade-offs.

Record the selected outcome, rationale, consequences, decision authority, date
and status, together with the engineering information affected by the decision.

The depth of analysis should be proportionate to the significance of the
decision.

## Outputs / Artefacts

Maintain important engineering decisions as controlled decision records, giving
each decision a stable `DEC-###` identifier.

Each decision record should capture, where relevant, the decision or problem,
alternatives considered, evaluation criteria, analysis and evidence, assumptions
and uncertainties, trade-offs, selected outcome, rationale, consequences,
decision authority, date and status.

The same decision record contains both the analysis of credible alternatives and
the final engineering decision. A separate decision log is therefore not required
for lightweight use of the framework.

## Traceability

- Give each important engineering decision a stable identifier, for example
  `DEC-001`.
- Link the decision to the requirements, constraints, risks, assumptions and
  other information that establish the decision context or criteria.
- Record the alternatives considered, evaluation criteria, evidence,
  uncertainties and trade-offs supporting the decision.
- Reference `DEC-###` from architecture/design elements, controls,
  configuration items, changes or other engineering artefacts that depend
  on the decision.
- Record the decision date, owner/authority and status.
- Where a decision changes, preserve the earlier record and identify the
  superseding decision rather than rewriting history.
- The purpose is to show **what was decided, why it was decided, what
  alternatives were considered, what engineering information depends on
  the decision, and the rationale and evidence available when the decision
  was made**.

## References

\[1\] National Aeronautics and Space Administration, *NASA Systems
Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC,
USA: NASA, 2016, Section 6.8, "Decision Analysis", pp. 160--170.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer,
*Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ,
USA: John Wiley & Sons, 2011, Chapter 9, "Decision Analysis and
Support", pp. 255--312.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA:
Pearson, 2016, Section 6.1, "Architectural design decisions",
pp. 171--173.

## References - Optional / Specialist

\[4\] S. D. Howison, *Practical Applied Mathematics: Modelling, Analysis, 
Approximation*. Cambridge, UK: Cambridge University Press, 2005,
Part I, “Modelling techniques,” Chapters 1–3, pp. 3–49.
