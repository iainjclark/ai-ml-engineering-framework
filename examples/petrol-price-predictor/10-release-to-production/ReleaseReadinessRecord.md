---
artifact_id: REL-001
artifact_type: release-readiness-record
title: Petrol Price Predictor Release Readiness
status: approved
owner: release-owner
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: demonstration-release-authority
approved_date: 2026-07-15
links:
  releases:
    - CFG-001
  supported_by:
    - EVID-001
    - EVID-002
    - EVID-003
    - EVID-004
---

# Release Readiness Record

This is a fictional worked-example decision, not production authorisation.

## Scope and baseline

**Release:** `REL-001` / `petrol-demo-v0.1.0`
**Environment:** fictional static demonstration
**Baseline:** `CFG-001`
**Manifest:** `MANIFEST-001`
**Included:** weekly batch estimate, range, advisory report, evidence logging.
**Excluded:** live data, transactions, autonomous action and real operational use.

## Readiness assessment

| Criterion | Result | Evidence / basis |
|---|---|---|
| Scope and baseline identified | Pass | `CFG-001`, `MANIFEST-001` |
| Required V&V complete | Pass | `EVID-001` through `EVID-004` |
| Controls verified | Pass | `CTRL-001` / `EVID-002`; `CTRL-003` / `EVID-003`; `CTRL-002` / `EVID-004` |
| Residual risks accepted | Pass | `RISK-001` through `RISK-003`, accepted by the demonstration release authority |
| Monitoring ready | Pass | `MON-001` defines timeliness, freshness, error and intervention thresholds |
| Rollback ready | Pass for example | Restore the prior static report and suppress stale output |
| Operational ownership | Pass | service-owner and escalation roles are identified in `MON-001` |

## Evidence freshness

All four evidence items are valid only for `CFG-001`, were executed on
2026-07-12 or 2026-07-13, peer-reviewed on 2026-07-14, and carry explicit retest
triggers in `EVIDREC-001`. No evidence is superseded.

## Open risks and conditions

No critical anomaly is open. The release is conditioned on preserving advisory
human review, using synthetic data only, and blocking publication on stale
input. A change to those conditions requires new tailoring and release review.

## Deployment and rollback

The example deployment publishes the static report. Failure, missing output or
a critical freshness alert preserves the previous report with its original
timestamp and prevents a new report from appearing. The service owner may stop
publication; only the release authority may approve a changed baseline.

## Decision

**Decision:** Approved for the fictional worked example with the conditions
above.
**Approved baseline:** `CFG-001`
**Authority:** demonstration-release-authority
**Date:** 2026-07-15
**Post-release review:** `PIR-001` after eight example runs or a critical event.
