# Change Request & Impact Assessment

Typical usage: `CHG-001.md`, `CHG-002.md`, ...

Use this record for a material proposed change to a controlled AI/ML
system, model, data pipeline, configuration or engineering baseline.

## Document Control

Change ID: `CHG-###`\
System / Project:\
Status: Proposed / Under Assessment / Approved / Rejected / Implemented
/ Closed\
Date Raised:\
Raised by:\
Owner:\
Decision Authority:

## 1. Change Summary

**Title:**

Describe the proposed change in concise terms.

## 2. Reason for Change

State why the change is being proposed.

Possible triggers include:

-   defect or incident
-   monitoring / drift finding
-   changed requirement
-   data-source change
-   model improvement
-   security / risk treatment
-   dependency or platform change
-   operational feedback
-   regulatory / policy change

Reference the initiating `MON-###`, `RISK-###`, `REQ-###`, `DEC-###`,
issue or other evidence where applicable.

## 3. Current Baseline

Identify the controlled state before the change:

-   baseline / release
-   model version
-   code version
-   data / feature configuration
-   relevant infrastructure / dependencies

Reference `CFG-###` and `REL-###` where available.

## 4. Proposed Change

Describe what will change.

Identify affected:

-   requirements
-   architecture / design
-   data sources or provenance
-   ETL / features
-   model / training
-   interfaces
-   controls
-   configuration
-   deployment
-   monitoring

Avoid embedding implementation detail where controlled source code or
design records are authoritative.

## 5. Impact Assessment

  Area                      Impact   Related IDs / Evidence
  ------------------------- -------- ---------------------------
  Requirements                       `REQ-###`
  Architecture / Design              `ADD-###` / `DEC-###`
  Data / DQA                         `DATA-###` / `DQA-###`
  ETL / Features                     `ETL-###` / `FEAT-###`
  Model / Training                   `MODEL-###` / `TRAIN-###`
  Risk / Controls                    `RISK-###` / `CTRL-###`
  V&V                                `VER-###` / `VAL-###`
  Operations / Monitoring            `MON-###`

Include schedule, cost, security, privacy, safety or regulatory impacts
where material.

## 6. Risk Assessment

State any new or changed risks introduced by the change and whether
existing controls remain adequate.

Reference the Risk and Control Registers rather than duplicating
detailed entries.

## 7. V&V and Evidence Required

Identify the verification, validation and regression evidence required
before the changed baseline can be accepted.

Reference or create applicable `VER-###`, `VAL-###`, `TEST-###` and
`EVID-###` records.

## 8. Implementation and Rollback

Summarise:

-   implementation approach
-   migration / transition considerations
-   compatibility issues
-   rollback or recovery approach
-   monitoring required after implementation

## 9. Decision

**Decision:** Approve / Approve with Conditions / Reject / Defer

**Date:**

**Authority:**

**Conditions / Rationale:**

Approval authorises implementation of the proposed change. It does not
by itself authorise operational release of the resulting baseline.

## 10. Completion and Baseline Update

Implementation date:\
Implemented by:\
Resulting baseline / version: `CFG-###`\
V&V evidence: `EVID-###`\
Release decision: `REL-###`\
Post-change monitoring: `MON-###`

Record any material deviation from the approved change.

## 11. References

Reference the initiating evidence, affected engineering artefacts,
configuration baseline, V&V evidence and release records used to assess
and control the change.
