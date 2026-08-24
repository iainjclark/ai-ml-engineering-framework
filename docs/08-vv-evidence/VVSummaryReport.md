# V&V Summary Report

Typical usage: `VVSR-001.md`, `VVSR-002.md`, ...

Use this report to summarise the body of verification and validation
evidence for a defined system or release baseline.

## Document Control

V&V Summary Report ID: `VVSR-###`\
System / Project:\
Baseline / Release:\
Status: Draft / Under Review / Approved / Superseded\
Date:\
Owner:\
Approved by:

## 1. Purpose and Scope

State what system, model, release or baseline this report assesses and
the V&V decision it is intended to support.

## 2. V&V Basis

Summarise the applicable:

-   requirements and acceptance criteria
-   intended use and operational context
-   V&V Plan
-   V&V Register
-   test specifications, where used
-   relevant risks and controls

Reference source artefacts rather than duplicating them.

## 3. V&V Coverage

  Area / Requirement   Planned Activity        Evidence     Result / Status
  -------------------- ----------------------- ------------ -----------------
  `REQ-###`            `VER-###` / `VAL-###`   `EVID-###`   

Identify material gaps in coverage explicitly.

## 4. Verification Summary

Summarise whether the engineered system was built in accordance with its
specified requirements and design.

Cover material findings such as:

-   functional behaviour
-   interfaces
-   data / feature implementation
-   model implementation
-   performance requirements
-   configuration / reproducibility
-   operational and deployment behaviour

## 5. Validation Summary

Summarise whether the system is fit for its intended operational use.

Cover, where relevant:

-   performance on representative data
-   robustness and sensitivity
-   important population / segment behaviour
-   calibration / uncertainty
-   operational scenarios
-   human interaction
-   limitations and foreseeable misuse
-   evidence supporting intended-use claims

## 6. Findings, Exceptions and Residual Issues

  -----------------------------------------------------------------------
  ID / Reference    Finding /         Significance      Disposition /
                    Exception                           Owner
  ----------------- ----------------- ----------------- -----------------
                                                        

  -----------------------------------------------------------------------

Distinguish accepted limitations from unresolved defects or missing
evidence.

## 7. Risk and Assurance Implications

Summarise how the V&V evidence affects relevant:

-   `RISK-###`
-   `CTRL-###`
-   `ASSUR-###`

Identify controls or assurance claims whose effectiveness or adequacy is
not supported by the available evidence.

## 8. Overall Assessment

**Assessment:** Satisfactory / Satisfactory with Conditions /
Unsatisfactory / Inconclusive

Summarise:

-   evidence supporting the assessment
-   important limitations
-   unresolved items
-   conditions on use or release
-   further V&V required

## 9. Recommendation

**Recommendation:** Proceed / Proceed with Conditions / Do Not Proceed /
Further Evidence Required

State the engineering basis for the recommendation.

This report summarises V&V evidence; release authority remains with the
applicable `REL-###` decision.

## 10. References

Reference the V&V Plan/Register, `TEST-###`, `EVID-###`, traceability
matrices, requirements, risk/control records and other evidence used in
the assessment.
