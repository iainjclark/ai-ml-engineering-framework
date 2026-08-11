---
artifact_id: TAILOR-001
artifact_type: framework-tailoring-record
title: Petrol Price Predictor Framework Tailoring
status: approved
owner: engineering-lead
version: 1.0
baseline: petrol-demo-v0.1.0
approved_by: demonstration-release-authority
approved_date: 2026-07-01
links:
  governs:
    - CFG-001
---

# Framework Tailoring Record

## Decision scope

This decision covers the fictional petrol-price predictor demonstration and its
worked engineering record. The service supplies an advisory weekly forecast to
a procurement analyst; it cannot transact or update itself.

## System characteristics

| Factor | Assessment | Rationale |
|---|---|---|
| System type | Predictive ML | A fixed statistical model produces a numeric forecast. |
| Operational consequence | Moderate | A poor estimate could influence planning, but a person retains the decision. |
| Reversibility | Readily reversible | No orders or external changes are performed by the system. |
| Effects on people | Informational | The demonstration does not determine rights, access, employment or safety outcomes. |
| Data sensitivity | Public-equivalent synthetic data | No personal, confidential or live commercial data is used. |
| Autonomy | Advisory | It produces a report only. |
| Complexity | Low | Batch ingestion, fixed transformations, one model and a static report. |
| External dependencies | Data source and CI scheduler | Both are represented as fictional demonstration dependencies. |
| Jurisdictions | UK demonstration context | No compliance claim is made. |

## Selected profile

**Base pack:** Lean
**Specialist profile:** Predictive ML, tailored to the small fictional example

The lean profile is proportionate because the system is advisory, reversible,
low-complexity and uses synthetic data. Data/model content is described inside
the architecture record; risks and controls share one CSV; V&V results share one
evidence record.

## Artefact applicability

| Artefact | Disposition | Owner | Rationale |
|---|---|---|---|
| Concept and Benefits Brief | Required | product-owner | Establish purpose and intended use. |
| Requirements Specification | Required | engineering-lead | Define measurable behaviour and guardrails. |
| Decision Analysis | Required | engineering-lead | Model approach materially affects evidence and operations. |
| Architecture and Design Description | Required | engineering-lead | Make data flow, boundaries and fallback visible. |
| Separate data/model records | Not applicable | engineering-lead | Combined into `ADD-001` for this lean synthetic example. |
| Risk and Control Register | Required | risk-owner | Three material demonstration risks are tracked. |
| V&V Plan and Evidence Record | Required | test-lead | Predefine checks and preserve results. |
| Decision Record | Required | engineering-lead | Preserve the authoritative selected option. |
| Configuration Record | Required | release-owner | Identify the fictional demonstration baseline. |
| Release Readiness Record and Manifest | Required | release-owner | Make the release decision explicit. |
| Monitoring and Intervention Plan | Required | service-owner | Define stale-data and performance responses. |
| Post-Implementation Review | Required | product-owner | Demonstrate lifecycle feedback. |
| GenAI / RAG profile | Not applicable | engineering-lead | No foundation model or retrieval system is used. |
| Agentic AI profile | Not applicable | engineering-lead | The system cannot select tools or execute actions. |
| High-consequence profile | Not applicable | release-authority | The fictional advisory use is reversible and not consequential to people. |

## Control depth

| Dimension | Tailored requirement |
|---|---|
| Review independence | Peer review of requirements, V&V evidence and release decision. |
| Evidence retention | Retain with the demonstration baseline in Git. |
| Release authority | A role separate from the implementation role. |
| Human approval | Analyst decides whether and how to use each forecast. |
| Logging | Preserve run time, input date, baseline and output. |
| Rollback | Restore the prior static report and suppress a stale forecast. |

## Reassessment triggers

Reassess if live or personal data is introduced, the system begins executing
procurement actions, intended users or jurisdictions change, a model/provider is
substituted, or an incident shows higher consequences than assumed.

**Scheduled review:** 2026-10-01
**Decision:** Approved for the fictional worked example
**Approved by:** demonstration-release-authority
**Approval date:** 2026-07-01
