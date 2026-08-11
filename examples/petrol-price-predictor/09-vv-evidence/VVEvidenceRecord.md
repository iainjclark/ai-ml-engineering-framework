---
artifact_id: EVIDREC-001
artifact_type: vv-evidence-record
title: Petrol Price Predictor V&V Evidence
status: approved
owner: test-lead
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: peer-reviewer
approved_date: 2026-07-14
links:
  supports:
    - REL-001
---

# V&V Evidence Record

All values and digests below are fictional worked-example evidence. Valid-format
hex strings demonstrate the field; they are not digests of a production result.

## Summary

| Evidence ID | Activity | Result | Acceptance criterion | Actual result | Conclusion |
|---|---|---|---|---|---|
| `EVID-001` | `VER-001` | Pass | MAE <= 3.0 p/L | MAE 2.4 p/L over 26 rolling predictions | Supports `ML-REQ-001` for `CFG-001`. |
| `EVID-002` | `VER-002` | Pass | Block publication and record a critical alert | No report; one `STALE_INPUT` critical alert | Supports `CTRL-001` and `OPS-REQ-001`. |
| `EVID-003` | `VER-003` | Pass | Two output digests identical | Both outputs `3333...3333` | Supports `NFR-001` and `CTRL-003`. |
| `EVID-004` | `VAL-001` | Pass | 3/3 reviewers interpret and use the report as intended | 3/3 identified advisory status and completed walkthrough | Supports `BEN-001` for the fictional analyst scenario. |

## Freshness and integrity

| Evidence ID | Valid for baseline | Executed at | Reviewed at | Retest trigger | Superseded by | Independence | Evidence hash |
|---|---|---|---|---|---|---|---|
| `EVID-001` | `CFG-001` | 2026-07-12T09:00:00Z | 2026-07-14 | Data, feature, model, threshold or runtime change | None | Peer review | `1111111111111111111111111111111111111111111111111111111111111111` |
| `EVID-002` | `CFG-001` | 2026-07-12T10:00:00Z | 2026-07-14 | Ingest, freshness threshold, alerting or publish-path change | None | Peer review | `2222222222222222222222222222222222222222222222222222222222222222` |
| `EVID-003` | `CFG-001` | 2026-07-12T11:00:00Z | 2026-07-14 | Any manifest-controlled item change | None | Peer review | `3333333333333333333333333333333333333333333333333333333333333333` |
| `EVID-004` | `CFG-001` | 2026-07-13T14:00:00Z | 2026-07-14 | Intended user/use or report presentation change | None | Peer review | `4444444444444444444444444444444444444444444444444444444444444444` |

## Deviations, uncertainty and anomalies

No method deviation or unresolved anomaly was recorded. `EVID-001` is limited to
the frozen synthetic series and does not support a real-world accuracy claim.
`EVID-004` uses fictional role-based reviewers rather than operational users,
so ongoing benefit realisation is assessed again in `PIR-001`.

## Review conclusion

The four planned activities were executed against the identified fictional
baseline and met their predefined criteria. The evidence is sufficient for the
worked-example release decision, subject to the limitations above.
