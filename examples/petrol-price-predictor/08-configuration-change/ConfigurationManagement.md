---
artifact_id: CFG-001
artifact_type: configuration-record
title: Petrol Price Predictor Configuration
status: approved
owner: release-owner
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: demonstration-release-authority
approved_date: 2026-07-15
links:
  implements:
    - ADD-001
  selected_by:
    - DEC-001
---

# Configuration Management Record

## Authoritative source

This worked example is controlled in the framework repository. References below
beginning with `EXAMPLE` are intentionally illustrative and must not be mistaken
for an actual released Git commit, tag, registry object or production system.

## Example controlled baseline

| Item | Example value |
|---|---|
| Baseline ID | `CFG-001` |
| Release | `EXAMPLE-petrol-demo-v0.1.0` |
| Git commit | `EXAMPLE-NOT-A-GIT-COMMIT` |
| Git tag | `EXAMPLE-NOT-A-GIT-TAG` |
| Data | `DATA-001`, synthetic-series-v1 |
| Feature definition | `FEAT-001`, lag1-lag4-mean4-v1 |
| Model | `MODEL-001`, regularised-linear-v1 |
| Training record | `TRAIN-001`, frozen-example-backtest-v1 |
| Runtime | `EXAMPLE-python-3.x-locked` |
| Manifest | `MANIFEST-001` |

## Change control

A change to input definition, feature calculation, model coefficients, runtime,
report schema, monitoring threshold or intended use requires a `CHG-###` impact
assessment. The assessment identifies affected requirements, risks, decisions
and V&V. Baselines are changed only through reviewed commits in a real project.

`CHG-001` is opened by `PIR-001` to clarify uncertainty wording in the next
example revision. It does not alter `CFG-001`, which remains preserved as the
reviewed fictional baseline.

## Release traceability

`REL-001` is the explicit fictional release decision for `CFG-001`.
`MANIFEST-001` identifies the controlled item versions, example-format hashes,
V&V evidence, rollback record and monitoring plan.
