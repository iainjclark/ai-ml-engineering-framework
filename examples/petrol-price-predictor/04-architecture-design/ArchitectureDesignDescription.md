---
artifact_id: ADD-001
artifact_type: architecture-design-description
title: Petrol Price Predictor Architecture
status: approved
owner: engineering-lead
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: test-lead
approved_date: 2026-07-06
links:
  derived_from:
    - DEC-001
  satisfies:
    - SYS-REQ-001
    - NFR-001
    - NFR-002
    - OPS-REQ-001
  mitigates:
    - RISK-001
    - RISK-002
---

# Architecture and Design Description

## Context and boundary

The fictional service consumes one synthetic weekly price series and publishes
one static advisory report. The scheduler, source and report store are external
to the application boundary. No purchase or supplier system is connected.

```text
[Synthetic source] -> [ingest + freshness gate] -> [feature builder]
                    -> [fixed model] -> [report renderer] -> [analyst]
                                      -> [run/evidence log]
```

| Actor / system | Interaction | Trust / responsibility boundary |
|---|---|---|
| Synthetic data source | Supplies dated pence-per-litre observations | Input is untrusted until schema and freshness checks pass. |
| CI scheduler | Starts a weekly run | May trigger execution but cannot approve model/config changes. |
| Procurement analyst | Reviews the static report | Retains decision responsibility; cannot modify the controlled baseline. |
| Service owner | Receives alerts and may suppress output | Owns operational response, not release approval. |

## Components

| ID | Component | Responsibility | Input | Output |
|---|---|---|---|---|
| `COMP-001` | Ingest and validation | Validate date, numeric range, uniqueness and freshness. | `DATA-001` | Validated observations or blocking alert. |
| `COMP-002` | Feature builder | Compute fixed lag-1, lag-4 and four-week mean features. | Validated observations | Ordered feature vector. |
| `COMP-003` | Model runner | Apply frozen `MODEL-001` coefficients and interval method. | Feature vector | Estimate and range. |
| `COMP-004` | Report renderer | Add advisory text, data/model versions and timestamps. | Estimate, range and run metadata | Static forecast report. |
| `COMP-005` | Evidence logger | Preserve run state, alert state and output digest. | Component events | Append-only run record. |

## Data and model record

`DATA-001` is a frozen, synthetic, non-personal weekly series in pence per
litre. Its permitted use is demonstration and testing only. Validation rejects
duplicate dates, non-numeric values, values outside 50–300 p/L and observations
newer than the run time.

`MODEL-001` is the regularised linear method selected by `DEC-001`. Training
record `TRAIN-001` identifies the frozen example backtest window, lag features,
regularisation setting and coefficients. No online learning occurs. Any data,
feature or coefficient change creates a new configuration baseline and repeats
`VER-001` and `VER-003`.

## Trust boundaries and controls

| Boundary | Concern | Control |
|---|---|---|
| Source to ingest | Malformed or stale observations | `CTRL-001` schema and freshness gate; fail closed. |
| Controlled baseline to scheduler | Unreviewed code/model substitution | `CTRL-003` version-pinned manifest and protected review. |
| Report to analyst | Output treated as a guaranteed or autonomous decision | `CTRL-002` advisory label, range and source/model metadata. |

The example contains no credentials, interactive API or personal data. A real
deployment would add authenticated storage, secrets management and provider
controls before release.

## Failure, fallback and recovery

| Failure | Detection | Safe behaviour | Recovery |
|---|---|---|---|
| Stale or malformed input | `COMP-001` validation | Publish nothing; raise critical alert. | Correct source and rerun under the same baseline. |
| Model/report error | Non-zero run status or missing digest | Retain the last report marked with its original timestamp. | Roll back to the last approved baseline. |
| Threshold breach in operation | `MON-001` delayed-outcome check | Add warning and suspend routine reliance pending review. | Investigate, change through `CHG-###`, revalidate and release. |

## Observability

Each run records baseline ID, input date, run time, validation outcome, forecast,
range, report digest and alert severity. `MON-001` also tracks report timeliness,
data age and rolling MAE when delayed example outcomes become available.

## Traceability

| Design element | Satisfies / mitigates | Verified by |
|---|---|---|
| `COMP-001` | `OPS-REQ-001`, `RISK-001` | `VER-002` |
| `COMP-002` + `COMP-003` | `ML-REQ-001`, `NFR-001` | `VER-001`, `VER-003` |
| `COMP-004` | `SYS-REQ-001`, `NFR-002`, `RISK-002` | `VAL-001` |
| `COMP-005` | `NFR-001`, `RISK-003` | `VER-003` |
