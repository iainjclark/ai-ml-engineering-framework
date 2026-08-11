---
artifact_id: PIR-001
artifact_type: post-implementation-review
title: Petrol Price Predictor Post-Implementation Review
status: approved
owner: product-owner
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: demonstration-release-authority
approved_date: 2026-08-11
links:
  reviews:
    - CFG-001
    - REL-001
    - MON-001
  triggers:
    - CHG-001
---

# Post-Implementation Review

All outcomes below are fictional values that complete the worked lifecycle.

## Scope

**Operational period:** 2026-07-20 to 2026-08-10
**Trigger:** Eight example runs represented in the demonstration dataset
**Participants:** product-owner, service-owner, engineering-lead and one peer
reviewer
**Question:** Did `CFG-001` provide a timely, interpretable advisory output while
its controls operated as intended?

## Outcomes

| Outcome | Expected | Fictional actual | Assessment |
|---|---|---|---|
| `BEN-001` forecast availability | At least 90% of planning cycles | 8 of 8 reports available before 08:00 UTC | Met |
| Operational error | `MET-003` <= 3.0 p/L | Rolling MAE 2.6 p/L after eight delayed outcomes | Met; above advisory threshold on the final window |
| Freshness control | No report from input older than eight days | One eight-day input generated a warning; no input exceeded the blocking threshold | Met |
| Advisory interpretation | Analyst recognises human-review role | All represented review checklists did; one asked for plainer interval wording | Met with improvement |
| Reproducibility | Digest stable for controlled reruns | No mismatch represented | Met |

## Incidents, drift and unexpected behaviour

No critical incident or control failure is represented. The final `MET-003`
window rose from 2.3 to 2.6 p/L: below the intervention threshold but sufficient
for an advisory investigation. The synthetic input showed a small level shift;
the limited window cannot establish concept drift.

## Risks, controls and assumptions

| ID | Finding | Current assessment |
|---|---|---|
| `RISK-001` / `CTRL-001` | Freshness warning occurred and was visible. | Control appears effective; retain thresholds. |
| `RISK-002` / `CTRL-002` | Advisory role was understood, but uncertainty wording can be clearer. | Residual risk remains acceptable; improve copy via `CHG-001`. |
| `ASM-001` | Stable input definition remained true in the example period. | Continue monitoring; reassess on schema or source change. |

## Lessons

- `LESSON-001`: recording the monitoring formula and threshold beside the
  release evidence prevents an operational metric from being confused with the
  26-week V&V result.
- `LESSON-002`: a warning below the release criterion is useful for early
  investigation, but a small synthetic window should not be labelled as proven
  drift.
- `LESSON-003`: the human-review label is more useful when paired with plain
  language explaining the interval.

## Actions

| ID | Action | Owner | Due | Creates / updates | Status |
|---|---|---|---|---|---|
| `CHG-001` | Replace `uncertainty interval` with plain-language range wording and rerun `VAL-001`. | product-owner | 2026-09-01 | `NFR-002`, `CTRL-002`, report configuration | Open |
| `ACT-002` | Investigate the represented level shift without changing the released model. | engineering-lead | 2026-08-25 | Monitoring finding | Open |

## Recommendation and approval

**Recommendation:** Continue the fictional demonstration with `CFG-001`; do not
retrain automatically. Complete `CHG-001` through normal change, V&V and release
control.
**Approved by:** demonstration-release-authority
**Approval date:** 2026-08-11
**Next review:** On completion of `CHG-001`, after another eight represented
runs, or after a critical event.
