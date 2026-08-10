# 08 --- Configuration & Change

> **What exactly is the controlled system, and what has changed?**

## Purpose

Define exactly what makes up a controlled system version and manage changes so deployed states can be understood and reproduced.

## When Should It Be Created

Create this once system items need controlled versions, and before a baseline is relied on for formal testing or release. When do you need a controlled version? Probably earlier than you think.

## When Should It Be Updated

Update it whenever controlled code, models, data, dependencies, configuration, infrastructure or documentation change materially. Review it at a cadence appropriate to the project’s scale, risk and rate of change.

## Inputs

Use versioned code, models, data, dependencies, configuration, infrastructure, documentation, change requests and approval records.

## Activities

Identify controlled items and baselines. Assess proposed changes, their impacts and required checks, then record approval and implementation.

## Outputs / Artefacts

Maintain configuration records, baselines and change records that show what changed, why, who approved it and what checks were required.

The configuration and change management artefacts are informed by Sommerville’s treatment of configuration management (Chapter 25), with the 
structure of `MilestoneChangeLog.xlsx` informed in part by the example change request form in Figure 25.15.

## Traceability

-   Give controlled configuration items and change records stable IDs,
    for example: configuration items (`CI-001`) and changes (`CHG-001`).
-   Identify the versions of code, models, data, dependencies,
    configuration, infrastructure and documentation that constitute a
    controlled baseline.
-   Link each approved change to its rationale, affected requirements,
    decisions, risks, design elements and required regression/V&V
    activities.
-   Preserve the relationship between released baselines and the
    evidence used to approve them.
-   Maintain enough history to reconstruct what was deployed at any
    material point in time.
-   The purpose is to show **what version of the system existed, why it
    changed, who authorised the change, and what evidence supported
    it**.

## References

\[1\] National Aeronautics and Space Administration, *NASA Systems
Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC,
USA: NASA, 2016, Section 6.5, "Configuration Management", pp. 143--150.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer,
*Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ,
USA: John Wiley & Sons, 2011, Section 12.6, "CM", pp. 436--439.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA:
Pearson, 2016, Chapter 25, "Configuration management", pp. 730--756.
