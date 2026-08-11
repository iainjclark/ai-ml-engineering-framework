---
artifact_id: DEC-###
artifact_type: decision-analysis
title: TODO
status: draft
owner: TODO
version: 0.1
baseline: TODO
approved_by: null
approved_date: null
links:
  derived_from: []
  affects: []
  mitigates: []
---

# Decision Analysis

## 1. Decision Statement

**Decision required:** TODO
**Decision deadline:** YYYY-MM-DD
**Decision authority:** TODO
**Scope / boundary:** TODO

State the choice to be made without embedding a preferred solution.

## 2. Drivers and Constraints

Reference the requirements, benefits, risks, assumptions, constraints and
earlier decisions that establish why this choice matters.

| ID | Driver or constraint | Effect on this decision |
|---|---|---|
| `REQ-###` | TODO | TODO |

## 3. Alternatives

Include the status quo where it is credible. Record why any plausible option was
screened out before detailed scoring.

| Option | Description | Key dependencies | Screen-in decision |
|---|---|---|---|
| A | TODO | TODO | Include / Exclude — rationale |
| B | TODO | TODO | Include / Exclude — rationale |

## 4. Evaluation Method

Define criteria and weights before scoring where practical. Weights should total
100%. State the scoring scale and how uncertainty is represented.

**Scoring scale:** 1 (poor) to 5 (strong)
**Weighted score:** `sum(weight × score) / 5`
**Treatment of uncertainty:** TODO

| Criterion | Weight | Definition | Evidence source |
|---|---:|---|---|
| TODO | 0% | TODO | TODO |
| **Total** | **100%** | | |

## 5. Evidence and Assumptions

| Ref | Evidence or assumption | Quality / confidence | Valid until | Owner |
|---|---|---|---|---|
| `EVID-###` / `ASM-###` | TODO | High / Medium / Low | YYYY-MM-DD / event | TODO |

## 6. Comparative Assessment

| Criterion | Weight | Option A score | Option A rationale | Option B score | Option B rationale |
|---|---:|---:|---|---:|---|
| TODO | 0% | 0 | TODO | 0 | TODO |
| **Weighted total** | **100%** | **0** | | **0** | |

Describe qualitative trade-offs, cost and schedule effects, operational
consequences, failure modes and any criteria that should not be collapsed into a
single score.

## 7. Uncertainty and Sensitivity

Test whether reasonable changes to uncertain evidence, weights or scores change
the ranking. Record important unknowns and the value of obtaining more evidence
before deciding.

| Scenario | Change tested | Preferred option | Material observation |
|---|---|---|---|
| Base case | As scored | TODO | TODO |
| Sensitivity case | TODO | TODO | TODO |

## 8. Recommendation

**Recommended option:** TODO
**Rationale:** TODO
**Conditions / follow-up work:** TODO
**Risks introduced or changed:** TODO
**Confidence:** High / Medium / Low

## 9. Decision Outcome

Complete this section when the authority decides, or link to the corresponding
record in `07-decision-log`.

**Outcome:** Accepted / Rejected / Deferred / Superseded
**Selected option:** TODO
**Authority:** TODO
**Decision date:** YYYY-MM-DD
**Rationale for divergence from recommendation:** TODO / Not applicable
**Supersedes / superseded by:** TODO / None

## 10. Traceability

Update `TraceabilityLinks.csv` with the relationships established by this
analysis, including `derived_from`, `satisfies`, `mitigates`, `affects` and
`supersedes` as applicable.
