---
artifact_id: CON-001
artifact_type: concept-benefits-brief
title: Petrol Price Predictor Concept and Benefits
status: approved
owner: product-owner
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: engineering-lead
approved_date: 2026-07-02
links:
  identifies:
    - NEED-001
    - BEN-001
---

# Concept and Benefits Brief

## Problem and intended outcome

A fictional procurement analyst currently prepares a weekly fuel-cost planning
range manually. The process is repeatable but time-consuming and gives no
consistent record of which data and forecast were used.

The proposed demonstration produces one seven-day-ahead petrol-price estimate
and an uncertainty range each Monday. It is decision support only: the analyst
retains responsibility for planning and may disregard the output.

## Stakeholders and actors

| ID | Stakeholder / actor | Need or interest |
|---|---|---|
| `NEED-001` | Procurement analyst | Receive a timestamped weekly estimate before the planning meeting. |
| `NEED-002` | Engineering lead | Reproduce the estimate from an identified data, model and code baseline. |
| `NEED-003` | Service owner | Detect stale inputs and suppress misleading output. |

## Benefit

| ID | Benefit | Measure | Target | Review point |
|---|---|---|---|---|
| `BEN-001` | More consistent weekly planning preparation | Share of weekly planning cycles with a reviewed forecast available by 08:00 Monday | At least 90% over eight example runs | `PIR-001` |

## Boundary and intended use

In scope: ingesting a synthetic weekly price series, validating freshness,
producing an estimate and range, publishing a static report, and recording run
metadata. Out of scope: live price scraping, purchasing, supplier selection,
autonomous actions and forecasts beyond seven days.

## Assumptions and constraints

- `ASM-001`: the input series uses a stable pence-per-litre definition.
- `ASM-002`: an analyst reviews each report before relying on it.
- The demonstration uses no personal or confidential data.
- Missing or stale input must stop publication rather than be silently imputed.
- All numerical results in this worked example are illustrative.

## Success and stop conditions

Success requires the forecast to meet `ML-REQ-001`, the stale-data control to
pass, and analysts to interpret the advisory status correctly. Stop or redesign
if use becomes autonomous or consequential, if the input definition changes, or
if operational error exceeds the intervention threshold in `MON-001`.
