---
artifact_id: DEC-001
artifact_type: decision-analysis
title: Forecast Method Selection
status: approved
owner: engineering-lead
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: demonstration-release-authority
approved_date: 2026-07-05
links:
  derived_from:
    - SYS-REQ-001
    - ML-REQ-001
    - NFR-001
  affects:
    - ADD-001
---

# Decision Analysis — Forecast Method Selection

## Decision

Select the forecasting method for the fixed, fictional demonstration baseline.
The method must satisfy the predefined error threshold without undermining
repeatability, operational simplicity or analyst explanation.

## Alternatives

| Option | Description | Key trade-off |
|---|---|---|
| A | Seasonal-naive forecast using the observation from four weeks earlier | Simplest, but least accurate in the example backtest. |
| B | Regularised linear autoregression using lag and rolling-mean features | Balanced accuracy, repeatability and explainability. |
| C | Gradient-boosted trees using the same features | Best fitted accuracy, but more complexity and sensitivity for this small example. |

## Criteria and evidence

Scores use 1 (poor) to 5 (strong). Weights were agreed before the final
recommendation. Numerical results are fictional example evidence.

| Criterion | Weight | A | B | C | Evidence / rationale |
|---|---:|---:|---:|---:|---|
| Rolling-origin accuracy | 45% | 3 | 4 | 5 | Example MAE: 2.9, 2.4 and 2.2 p/L respectively. |
| Repeatability | 20% | 5 | 5 | 3 | A and B use deterministic fixed calculations; C adds library and tuning sensitivity. |
| Operational simplicity | 15% | 5 | 4 | 3 | A is simplest; B adds fixed feature calculation; C adds more model controls. |
| Explainability | 20% | 5 | 4 | 3 | A is direct, B exposes coefficients, C needs more explanation. |
| **Weighted score / 100** | **100%** | **82** | **84** | **78** | `sum(weight × score) / 5` |

## Assumptions and uncertainty

- `ASM-001` (medium confidence): the synthetic series is representative enough
  to demonstrate the workflow, not real-world accuracy.
- The 0.2 p/L example difference between B and C is not treated as material
  given the small frozen dataset.
- Increasing the accuracy weight to 60% makes C the preferred option. That
  sensitivity is a trigger to revisit this decision if a real dataset or
  higher-consequence use is introduced.

## Recommendation and outcome

**Recommendation:** Option B, regularised linear autoregression.
**Rationale:** It has the highest base-case score, passes `ML-REQ-001`, produces
deterministic outputs and avoids complexity that is not justified for the
worked example.
**Conditions:** Freeze transformations and coefficients in `CFG-001`; monitor
error; revisit after a data or intended-use change.
**Decision:** Accepted by the demonstration release authority on 2026-07-05.
**Supersession:** None.
