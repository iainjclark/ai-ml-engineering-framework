# 05 --- Risk & Assurance

> **What can go wrong, and how will we control it?**

## Purpose

Identify what could prevent acceptable outcomes, decide how those risks will be controlled, and define what evidence will support confidence.

## When Should It Be Created

Create this early enough for risks to influence requirements, design and planning, then keep it active throughout the lifecycle.

## When Should It Be Updated

Update it when risks, controls, assumptions, evidence, incidents, system changes or the operating environment materially change.

## Inputs

Use requirements, architecture, assumptions, operational scenarios, prior incidents, known hazards, security concerns and stakeholder tolerances.

## Activities

Identify and assess material risks. Choose controls, assign owners, define evidence of control effectiveness, and assess remaining risk.

For AI/ML systems, consider risks arising from the data, model and its use,
including training-data and model vulnerabilities, performance differences
across relevant populations or conditions, privacy, fairness and other
responsible-ML concerns [1].

## Outputs / Artefacts

Maintain the risk register, controls and assurance claims, including owners, evidence needs, status and accepted residual risks.

## Traceability

-   Give each material risk a stable ID, for example: risks
    (`RISK-001`), controls (`CTRL-001`) and assurance claims
    (`ASSUR-001`).
-   Trace risks to the requirements, design elements, assumptions,
    interfaces or operational scenarios that give rise to them.
-   Link each risk to its prevention, mitigation, detection, recovery or
    acceptance controls.
-   Link controls to the V&V activities and evidence used to demonstrate
    that they are effective.
-   Record residual risk and any accountable acceptance decision before
    release.
-   The purpose is to show **what could prevent the system from
    succeeding or operating acceptably, and what evidence supports the
    controls**.

## References

\[1\] C. Chen, N. R. Murphy, K. Parisa, D. Sculley, and T. Underwood,
*Reliable Machine Learning: Applying SRE Principles to ML in Production*.
Sebastopol, CA, USA: O'Reilly Media, 2022, Chapter 3, "Basic Introduction
to Models", pp. 43--63, in particular the discussion of model and training
vulnerabilities; Chapter 6, "Fairness, Privacy, and Ethical ML Systems",
pp. 107--135.

\[2\] National Aeronautics and Space Administration, *NASA Systems
Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC,
USA: NASA, 2016, Section 6.4, "Technical Risk Management", pp. 138--143.

\[3\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer,
*Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ,
USA: John Wiley & Sons, 2011, Section 5.4, "Risk Management",
pp. 120--128; Chapter 10, "Advanced Development", pp. 317--354.

\[4\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA:
Pearson, 2016, Section 22.1, "Risk management", pp. 644--651; Chapters
10--14, pp. 285--434, as applicable to dependability, safety, security
and resilience.
