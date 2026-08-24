# Post-Implementation Review / Operational Review

Typical usage: `PIR-001.md`, `PIR-002.md`, ...

Use this review after deployment, or periodically during operation, to
assess what actually happened and what should change as a result.

## Document Control

Review ID: `PIR-###`\
System / Project:\
Release / Baseline:\
Review Period:\
Status: Draft / Under Review / Approved / Closed\
Date:\
Owner:\
Approved by:

## 1. Purpose and Scope

State why the review is being performed and the operational period,
release, model or capability covered.

## 2. Operational Context

Summarise material facts needed to interpret operational performance:

-   deployed release / model version
-   operating environment
-   user population / consuming systems
-   material changes during the review period
-   relevant data or workload conditions

Reference controlled release and configuration records.

## 3. Intended Outcomes and Expectations

Summarise the outcomes and criteria against which operation is being
reviewed.

Reference:

-   `BEN-###`
-   `REQ-###`
-   `MODEL-###`
-   `REL-###`
-   relevant operational objectives or acceptance criteria

## 4. Operational Evidence

Summarise the evidence generated during operation.

  --------------------------------------------------------------------------
  Area / Monitor Evidence /     Expected /     Observed       Status
                 Metric         Threshold                     
  -------------- -------------- -------------- -------------- --------------
  `MON-###`                                                   

  --------------------------------------------------------------------------

Detailed time-series, logs and automated monitoring evidence should
remain in their native evidence locations.

## 5. Model and Data Performance

Review, where applicable:

-   realised model performance
-   calibration / error behaviour
-   drift
-   data quality
-   data freshness
-   feature stability
-   performance across important segments
-   changes in operating population or conditions

Reference `MON-###`, `DQA-###` and supporting evidence.

## 6. Operational Performance

Review relevant system-level behaviour such as:

-   availability
-   latency / throughput
-   reliability
-   resource usage
-   failed jobs / exceptions
-   interface or dependency failures
-   support burden
-   manual intervention

## 7. Incidents, Interventions and Exceptions

  Reference           Event / Finding   Response   Outcome
  ------------------- ----------------- ---------- ---------
  `MON-###` / other                                

Record material interventions, overrides, rollbacks, retraining
decisions or unexpected uses.

## 8. Benefits and User / Stakeholder Outcomes

Assess whether the capability is delivering the intended operational or
organisational benefit.

Reference `BEN-###` and stakeholder needs where appropriate.

Record material feedback from users, operators, owners or affected
stakeholders.

## 9. Risk, Controls and Assurance

Review whether:

-   known risks remain acceptable
-   new risks have emerged
-   controls operated as intended
-   control effectiveness has changed
-   assurance claims remain supported
-   operating assumptions remain valid

Reference `RISK-###`, `CTRL-###` and `ASSUR-###`.

## 10. Lessons Learned

Record what has been learned from actual operation.

Consider:

-   assumptions that proved correct or incorrect
-   design choices that worked well or poorly
-   missing requirements
-   unnecessary complexity
-   monitoring gaps
-   V&V gaps
-   operational practices worth retaining

Keep lessons specific enough to influence future engineering.

## 11. Recommended Actions

  Action   Reason   Owner   Priority   Related ID
  -------- -------- ------- ---------- ------------------------------------
                                       `CHG-###` / `RISK-###` / `MON-###`

Material changes should enter the controlled change process rather than
being implemented solely from this review.

## 12. Overall Operational Assessment

**Assessment:** Performing as Intended / Acceptable with Actions /
Material Concerns / Withdraw or Replace

Summarise:

-   whether the system remains fit for intended use
-   material limitations
-   unresolved concerns
-   conditions for continued operation

## 13. Review Decision

**Decision:** Continue / Continue with Actions / Modify / Retrain / Roll
Back / Retire / Further Review Required

**Authority:**

**Date:**

**Rationale / Conditions:**

Where the decision requires a system change, raise or reference
`CHG-###`.

## 14. References

Reference monitoring records, operational evidence,
release/configuration records, incidents, V&V evidence, risk/control
records, stakeholder feedback and other material used in the review.
