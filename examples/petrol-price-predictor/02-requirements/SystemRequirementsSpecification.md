---
artifact_id: SRS-001
artifact_type: system-requirements-specification
title: Petrol Price Predictor Requirements
status: approved
owner: engineering-lead
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: product-owner
approved_date: 2026-07-03
links:
  derived_from:
    - NEED-001
    - NEED-002
    - NEED-003
    - BEN-001
---

# System / ML Requirements Specification

## Scope

These requirements cover the fictional batch predictor, static report and
release `petrol-demo-v0.1.0`.

### SYS-REQ-001 — Weekly forecast

**Requirement:** The system shall make a seven-day-ahead price estimate and
uncertainty range available by 08:00 UTC each Monday when valid input is
available.
**Source:** `NEED-001`, `BEN-001`
**Acceptance criterion:** A controlled scheduled run creates a timestamped
report containing both values before 08:00 UTC.
**Priority:** Must

### ML-REQ-001 — Predictive performance

**Requirement:** The selected model shall achieve a mean absolute error no
greater than 3.0 pence per litre on the frozen 26-week rolling-origin example
backtest.
**Source:** `BEN-001`
**Acceptance criterion:** `VER-001` records MAE <= 3.0 using `DATA-001` and
`MODEL-001`.
**Priority:** Must

### NFR-001 — Repeatability

**Requirement:** The same controlled inputs and baseline shall produce the same
forecast value and report payload.
**Source:** `NEED-002`
**Acceptance criterion:** Two clean executions of `CFG-001` have identical
forecast JSON SHA-256 values.
**Priority:** Must

### NFR-002 — Advisory presentation

**Requirement:** Every report shall identify the data date, model version,
generation time, uncertainty range and the statement `Advisory — human review
required`.
**Source:** `ASM-002`, `RISK-002`
**Acceptance criterion:** Inspection confirms all five fields in the report.
**Priority:** Must

### OPS-REQ-001 — Input freshness gate

**Requirement:** The system shall not publish a forecast when the newest input
observation is more than eight days old at the scheduled run time.
**Source:** `NEED-003`, `RISK-001`
**Acceptance criterion:** `VER-002` injects a nine-day-old observation, records
no published report and records a critical alert.
**Priority:** Must

## Quality and change control

The five requirements are singular, testable and traced to planned V&V. A
change to intended use, horizon, units, threshold or human-review role requires
impact assessment and re-approval of this specification.
