---
artifact_id: VVPLAN-001
artifact_type: vv-plan
title: Petrol Price Predictor V&V Plan
status: approved
owner: test-lead
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: engineering-lead
approved_date: 2026-07-08
links:
  verifies:
    - ML-REQ-001
    - NFR-001
    - OPS-REQ-001
  validates:
    - BEN-001
---

# Verification and Validation Plan

## Scope and governance

This plan covers the fictional candidate baseline `CFG-001`. The test lead
executes the checks; a peer reviewer who did not prepare the example results
reviews the evidence before the release decision.

Acceptance criteria were fixed on 2026-07-08, before the example executions on
2026-07-12 and 2026-07-13.

## Planned activities

| ID | Type | Target | Method and conditions | Acceptance criterion | Planned evidence |
|---|---|---|---|---|---|
| `VER-001` | Verification | `ML-REQ-001` | Rolling-origin backtest over frozen `DATA-001`, 26 weekly predictions, model `MODEL-001`; compute MAE without excluding errors. | MAE <= 3.0 p/L. | Predictions, calculation summary, versions and digest in `EVID-001`. |
| `VER-002` | Verification | `OPS-REQ-001`, `CTRL-001` | Set newest synthetic observation to nine days before run time and invoke the publish path. | No report is published and one critical stale-input alert is recorded. | Run and alert record in `EVID-002`. |
| `VER-003` | Verification | `NFR-001`, `CTRL-003` | Execute two clean runs with identical manifest, input and time parameter. | Forecast payload SHA-256 values are identical. | Both run records and digests in `EVID-003`. |
| `VAL-001` | Validation | `NEED-001`, `BEN-001`, `NFR-002` | Three fictional analyst-role reviewers inspect a report and explain its intended use and limitations. | All identify the forecast as advisory, find the input date/model/range, and complete the planning walkthrough. | Review checklist and findings in `EVID-004`. |

## Data, environment and dependencies

The frozen synthetic data, model coefficients, transformations, runtime and
configuration are identified by `MANIFEST-001`. Actual production, personal or
commercial data is excluded. The fixed time parameter prevents clock-dependent
repeatability differences.

## Deviations and anomaly handling

Any change to data, feature code, coefficients, thresholds or report fields
invalidates the affected evidence. Failures and inconclusive results remain in
the evidence record and are linked to a risk or change; they are not overwritten
by a later pass.

## Completion rule

Release consideration requires all four activities to be executed, all three
verification criteria to pass, no unresolved critical anomaly, and peer review
of the evidence. Validation failure blocks the example's benefit claim and
requires a presentation change before release.
