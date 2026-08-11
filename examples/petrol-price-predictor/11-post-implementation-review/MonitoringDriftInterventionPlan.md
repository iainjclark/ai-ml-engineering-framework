---
artifact_id: MON-001
artifact_type: monitoring-drift-intervention-plan
title: Petrol Price Predictor Monitoring Plan
status: approved
owner: service-owner
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: demonstration-release-authority
approved_date: 2026-07-15
links:
  monitors:
    - CFG-001
  mitigates:
    - RISK-001
    - RISK-002
---

# Monitoring, Drift and Intervention Plan

## Scope and ownership

This plan covers the fictional static-report service at `CFG-001`. The service
owner reviews each run; the engineering lead investigates model/data findings;
the demonstration release authority decides whether a changed baseline may be
released.

## Metric catalogue

| ID | Definition | Window / slices | Warning | Intervention | Owner |
|---|---|---|---|---|---|
| `MET-001` | Report available before 08:00 UTC Monday / scheduled runs | Rolling eight runs | < 100% | < 90% | service-owner |
| `MET-002` | Run time minus newest input observation time, in days | Every run | > 7 days | > 8 days | service-owner |
| `MET-003` | Mean absolute forecast error in p/L once example outcomes are available | Rolling 8 outcomes; overall only because the synthetic example has no meaningful subgroups | > 2.7 | > 3.0 | engineering-lead |
| `MET-004` | Reports containing all advisory metadata fields / published reports | Rolling eight reports | < 100% | < 100% | product-owner |

`MET-003` uses the same unit and direction as `ML-REQ-001`, but its shorter
operational window is an alert signal rather than a replacement V&V criterion.

## Drift and data quality

The ingest component checks schema, date uniqueness, numeric range and freshness
on every run. A simple population-stability comparison of the latest eight
synthetic observations against `DATA-001` is reviewed monthly. Because the
worked dataset is small, drift statistics are treated as investigation signals,
not proof of a causal or performance change.

## Alerts and intervention

| Severity | Condition | Immediate action | Authority / follow-up |
|---|---|---|---|
| Advisory | `MET-003` > 2.7 p/L or drift signal | Annotate dashboard and investigate within five working days. | engineering-lead; record finding. |
| Warning | A Monday report is late or metadata is incomplete | Preserve prior report, notify analyst and correct before next run. | service-owner; open `CHG-###` if baseline changes. |
| Critical | Input age > 8 days, `MET-003` > 3.0 p/L, invalid schema or digest mismatch | Publish nothing new; mark service unavailable for planning. | service-owner stops publication; release authority decides restart after evidence review. |

No automatic retraining or model substitution is permitted. Data, feature,
model or threshold changes require impact assessment, repeat V&V and a new
release decision. A change to autonomous or consequential use first requires
reassessment of `TAILOR-001`.

## Evidence and review

Run records preserve the baseline, input date, run time, output digest, alerts
and later observed error. Evidence is retained with the example history. Review
occurs after eight runs, quarterly thereafter, and after any critical event,
control failure or intended-use change.

## Stop and retirement criteria

Stop routine publication if the analyst role is unavailable, advisory wording
is removed, critical telemetry is missing, or the error threshold is breached.
Retire the demonstration when its teaching purpose is no longer maintained or a
replacement example is approved and traceably supersedes `CFG-001`.
