# V&V Procedure / Test Specification

Typical usage: `TEST-001.md`, `TEST-002.md`, ...

Use this record where a verification or validation activity requires
enough procedural detail to be repeatable and independently reviewable.

## Document Control

Test Specification ID: `TEST-###`\
System / Project:\
Related V&V Activity: `VER-###` / `VAL-###`\
Version / Baseline:\
Status: Draft / Under Review / Approved / Executed / Superseded\
Date:\
Owner:\
Approved by:

## 1. Purpose

State what this procedure establishes and why the test is required.

Reference the applicable requirement, risk, control, model, decision or
validation objective rather than reproducing it.

## 2. Scope

Define:

-   system, component, model or data product under test
-   behaviours or properties covered
-   relevant operating conditions
-   exclusions and limitations

## 3. Test Basis and Traceability

  -----------------------------------------------------------------------
  Item                                Reference
  ----------------------------------- -----------------------------------
  Requirement(s)                      `REQ-###`

  V&V activity                        `VER-###` / `VAL-###`

  Risk / Control                      `RISK-###` / `CTRL-###`

  Model / Data / Feature              `MODEL-###` / `DATA-###` /
                                      `ETL-###` / `FEAT-###`

  Decision                            `DEC-###`
  -----------------------------------------------------------------------

## 4. Test Environment and Configuration

Record the configuration needed to reproduce the test:

-   system / model version
-   code commit / tag
-   data snapshot
-   configuration
-   software dependencies
-   execution environment
-   hardware or platform where material
-   external services / interfaces
-   random seed or determinism controls

Reference controlled configuration records where available.

## 5. Inputs and Preconditions

State the required inputs, fixtures, datasets, initial state and
preconditions.

Identify any synthetic, sampled, masked or otherwise specially prepared
test data.

## 6. Procedure

Describe the procedure at sufficient detail for a competent practitioner
to repeat it.

1.  ...
2.  ...
3.  ...

Where the procedure is automated, reference the executable test code or
pipeline rather than duplicating implementation detail.

## 7. Expected Results and Acceptance Criteria

  Check / Measure   Expected Result / Criterion   Requirement / Basis
  ----------------- ----------------------------- ---------------------
                                                  `REQ-###`

Acceptance criteria should be defined before execution wherever
practicable.

## 8. Evidence to Capture

Identify the evidence that must be retained, for example:

-   test output
-   logs
-   metrics
-   plots
-   screenshots
-   generated reports
-   hashes / checksums
-   exception records
-   reviewer observations

Executed evidence should be registered as `EVID-###`.

## 9. Exceptions and Deviations

Record any permitted procedural deviations, tolerances or known
limitations.

Unexpected deviations during execution should be preserved with the
resulting evidence rather than silently corrected.

## 10. Result Recording

After execution, record or reference:

Test date:\
Executor:\
Result: Pass / Fail / Partial / Inconclusive\
Evidence: `EVID-###`\
Defect / Issue / Change reference:\
Comments:

Detailed evidence should remain in the V&V Evidence / Test Record.

## 11. References

See the Stage 06 V&V guidance and applicable project requirements,
architecture, model, risk, control and configuration records.
