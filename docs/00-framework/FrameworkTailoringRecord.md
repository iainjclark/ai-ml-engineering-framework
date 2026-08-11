---
artifact_id: TAILOR-###
artifact_type: framework-tailoring-record
title: TODO
status: draft
owner: TODO
version: 0.1
baseline: TODO
approved_by: null
approved_date: null
links: {}
---

# Framework Tailoring Record

Use this record to decide how much engineering control the project needs. Make
the decision before omitting artefacts, and revisit it when the system or its
operating context materially changes.

## 1. Project and Decision Scope

**Project / system:** TODO
**Tailoring decision ID:** `TAILOR-###`
**Decision owner:** TODO
**Assessment date:** YYYY-MM-DD
**Target release / baseline:** TODO

Summarise the capability, intended users, affected people, operating context and
the boundary covered by this decision.

## 2. System Characteristics

| Factor | Selection | Rationale / evidence |
|---|---|---|
| System type | Deterministic software / Predictive ML / GenAI or RAG / Agentic / Hybrid | TODO |
| Operational consequence | Low / Moderate / High / Critical | TODO |
| Reversibility of outcomes | Readily reversible / Partly reversible / Difficult or impossible | TODO |
| Effects on people | None / Informational / Consequential rights, access, safety, employment, credit or similar | TODO |
| Data sensitivity | Public / Internal / Confidential / Personal / Special-category or highly sensitive | TODO |
| Degree of autonomy | Advisory / Prepares actions / Executes with approval / Executes autonomously | TODO |
| Technical complexity | Low / Moderate / High | TODO |
| Model uncertainty | Low / Moderate / High / Not yet known | TODO |
| External dependencies | None / Data / Model / Service / Tooling / Multiple | TODO |
| Change rate | Infrequent / Periodic / Continuous | TODO |

## 3. Regulatory, Contractual and Organisational Context

List applicable jurisdictions, policies, contracts, standards, regulator or
customer expectations, and any independent-assurance obligations. State `None
identified` only after an explicit check.

| Context ID | Obligation or constraint | Source | Owner | Affected artefacts |
|---|---|---|---|---|
| `CON-001` | TODO | TODO | TODO | TODO |

## 4. Selected Framework Profile

**Base pack:** Lean / Full
**Specialist profiles:** Predictive ML / GenAI-RAG / Agentic AI /
High-consequence / None
**Overall rationale:** TODO

## 5. Artefact Applicability

Record every candidate artefact from the selected pack and profiles. `Optional`
means it may be added later; `Not applicable` requires a rationale.

| Artefact type | Disposition | Owner | Due / trigger | Rationale or exclusion basis |
|---|---|---|---|---|
| Concept and Benefits Brief | Required / Optional / Not applicable | TODO | TODO | TODO |
| System / ML Requirements Specification | Required / Optional / Not applicable | TODO | TODO | TODO |
| Decision Analysis | Required / Optional / Not applicable | TODO | TODO | TODO |
| Architecture and Design Description | Required / Optional / Not applicable | TODO | TODO | TODO |
| Data and Model Record | Required / Optional / Not applicable | TODO | TODO | TODO |
| Risk and Assurance Register | Required / Optional / Not applicable | TODO | TODO | TODO |
| V&V Pack | Required / Optional / Not applicable | TODO | TODO | TODO |
| Release Readiness Record | Required / Optional / Not applicable | TODO | TODO | TODO |
| Monitoring and Intervention Plan | Required / Optional / Not applicable | TODO | TODO | TODO |
| Post-Implementation Review | Required / Optional / Not applicable | TODO | TODO | TODO |

Add rows for any split or profile-specific artefacts.

## 6. Required Controls and Approval Depth

Define the required review independence, evidence retention, configuration
control, approval authority, human-approval gates and audit/logging depth.

| Control dimension | Tailored requirement | Rationale |
|---|---|---|
| Review independence | TODO | TODO |
| Evidence retention | TODO | TODO |
| Release authority | TODO | TODO |
| Human approval gates | TODO | TODO |
| Logging and audit | TODO | TODO |
| Rollback / recovery | TODO | TODO |

## 7. Reassessment Triggers

Revisit this decision when any applicable trigger occurs:

- intended use, users or affected population changes;
- consequences, autonomy or data sensitivity increases;
- a new jurisdiction, contract or policy applies;
- an external model, dataset, tool or provider changes;
- a material incident, control failure or unexpected model behaviour occurs;
- release scope or system boundary materially changes; or
- the scheduled review date is reached.

**Scheduled review date:** YYYY-MM-DD

## 8. Approval

**Decision:** Approved / Approved with conditions / Rejected
**Conditions:** TODO / None
**Approved by:** TODO
**Role / authority:** TODO
**Approval date:** YYYY-MM-DD
**Evidence / record:** TODO
