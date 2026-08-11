---
artifact_id: REL-###
artifact_type: release-readiness-record
title: TODO
status: draft
owner: TODO
version: 0.1
baseline: TODO
approved_by: null
approved_date: null
links:
  releases: []
  supported_by: []
  accepts: []
---

# Release Readiness Record

## 1. Release Scope

**Release ID:** `REL-###`
**System / service:** TODO
**Candidate version:** TODO
**Target environment:** TODO
**Proposed deployment window:** TODO
**Release owner:** TODO
**Release authority:** TODO

Describe included capability, excluded capability and material changes from the
previous released baseline.

## 2. Controlled Baseline

Reference `ReleaseManifest.yaml`. Confirm that code, model, data, configuration,
dependencies, infrastructure and controlled engineering records are uniquely
identified and retrievable.

**Baseline ID:** `CFG-###`
**Manifest integrity hash:** TODO
**Reproduction / restore check:** Pass / Fail / Not applicable — rationale

## 3. Readiness Criteria

| Criterion | Required | Result | Evidence / owner | Exception or condition |
|---|---|---|---|---|
| Scope and baseline approved | Yes | Pass / Fail | TODO | TODO |
| Required V&V complete | Yes | Pass / Fail | TODO | TODO |
| Controls verified | Yes | Pass / Fail | TODO | TODO |
| Residual risks accepted | Yes | Pass / Fail | TODO | TODO |
| Security and privacy checks complete | Tailored | Pass / Fail / N/A | TODO | TODO |
| Monitoring and alerting ready | Yes | Pass / Fail | TODO | TODO |
| Deployment and rollback rehearsed | Tailored | Pass / Fail / N/A | TODO | TODO |
| Operational ownership confirmed | Yes | Pass / Fail | TODO | TODO |

## 4. Evidence Review and Freshness

Record freshness explicitly so evidence from an obsolete configuration is not
silently reused.

| Evidence ID | Claim / criterion | Result | Valid for baseline | Executed at | Reviewed at | Retest trigger | Superseded by | Independence level | Evidence hash |
|---|---|---|---|---|---|---|---|---|---|
| `EVID-###` | TODO | Pass / Fail / Inconclusive | `CFG-###` | YYYY-MM-DDThh:mm:ssZ | YYYY-MM-DD | TODO | None | Self / Peer / Independent | SHA-256 |

## 5. Open Risks, Anomalies and Conditions

| ID | Description | Severity / residual risk | Disposition | Accountable owner | Due / expiry |
|---|---|---|---|---|---|
| `RISK-###` / `ANOM-###` | TODO | TODO | Accept / Mitigate / Block / Condition | TODO | TODO |

Explicitly identify who accepts each residual risk and within what authority.

## 6. Deployment, Rollback and Recovery

**Deployment procedure:** TODO
**Rollback procedure:** TODO
**Rollback trigger:** TODO
**Last rehearsal / verification:** TODO
**Maximum acceptable recovery time:** TODO
**Data reconciliation after rollback:** TODO

## 7. Operational Readiness

Confirm monitoring coverage, thresholds, on-call ownership, incident route,
support documentation, user communication, capacity/resource limits and any
human oversight arrangements.

## 8. Release Decision

**Decision:** Approve / Approve with conditions / Reject
**Decision rationale:** TODO
**Conditions and expiry:** TODO / None
**Approved baseline:** `CFG-###` / None
**Approved by:** TODO
**Authority / role:** TODO
**Decision date:** YYYY-MM-DD

## 9. Post-Release Checks

| Check | Timing | Owner | Success / rollback criterion | Evidence destination |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

Link the deployed release with `deployed_as` and `releases` relationships in
`TraceabilityLinks.csv`.
