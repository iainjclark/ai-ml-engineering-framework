---
artifact_id: DECLOG-001
artifact_type: decision-record
title: Forecast Method Decision Record
status: approved
owner: engineering-lead
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: demonstration-release-authority
approved_date: 2026-07-05
links:
  records:
    - DEC-001
---

# Decision Record

| Field | Value |
|---|---|
| Decision ID | `DEC-001` |
| Decision | Use the fixed regularised linear autoregression for baseline `CFG-001`. |
| Status | Accepted |
| Date | 2026-07-05 |
| Authority | demonstration-release-authority |
| Supporting analysis | `03-decision-analysis/DecisionAnalysis.md` |
| Rationale | Highest base-case weighted score; passes the fictional performance criterion while remaining deterministic and inspectable. |
| Conditions | Freeze transformations and coefficients; repeat V&V after data, feature, model or intended-use change. |
| Affected items | `ADD-001`, `MODEL-001`, `TRAIN-001`, `CFG-001`, `VER-001`, `VER-003` |
| Supersedes | None |
| Superseded by | None |

This record preserves the authoritative outcome. The analysis retains the
alternatives, uncertainty and sensitivity that informed it.
