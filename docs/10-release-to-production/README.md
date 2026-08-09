# 10 --- Release to Production

> **Is there sufficient evidence to justify putting this version into
> production?**

## Purpose

Decide whether a specific controlled version has enough evidence and acceptable remaining risk to justify operational use.

## When Should It Be Created

Create this for each proposed production release after the required evidence is available and before deployment is authorised.

## When Should It Be Updated

Update it if the release scope, baseline, evidence, open risks, conditions, deployment plan or approval decision changes.

## Inputs

Use the approved baseline, V&V evidence, open risks, accepted residual risks, operational controls, deployment plan and rollback plan.

## Activities

Review readiness, evidence and open issues. Confirm deployment and rollback arrangements, then approve, conditionally approve or reject release.

## Outputs / Artefacts

Produce a release record identifying the approved baseline, supporting evidence, remaining risks, conditions, authority and decision.

## Traceability

-   Give each production release a stable ID, for example: releases
    (`REL-001`), and identify the exact approved baseline.
-   Link the release decision to applicable requirements, V&V evidence,
    open risks, accepted residual risks, operational controls and
    rollback arrangements.
-   Record the accountable release authority and the basis for approval,
    conditional approval or rejection.
-   Link deployment and rollback procedures to the configuration items
    and versions they control.
-   Preserve the release record so the deployed state can be
    reconstructed later.
-   The purpose is to show **why a specific system version was judged
    ready for operational use and who accepted the remaining risk**.

## References

\[1\] National Aeronautics and Space Administration, *NASA Systems
Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC,
USA: NASA, 2016, Section 5.5, "Product Transition", pp. 106--112.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer,
*Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ,
USA: John Wiley & Sons, 2011, Chapter 14, "Production", pp. 483--503.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA:
Pearson, 2016, Sections 8.3--8.4, "Release testing" and "User testing",
pp. 245--254; Section 25.4, "Release management", pp. 750--756.
