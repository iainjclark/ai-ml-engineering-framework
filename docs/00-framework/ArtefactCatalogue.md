# Framework Artefact Catalogue

This catalogue describes the reusable engineering artefacts supplied or
anticipated by the framework. It is not a checklist that every project must
complete. Record the selected profile, required artefacts and justified
exclusions in `FrameworkTailoringRecord.md`.

Use `ArtefactCatalogue.yaml` in each project as the machine-readable inventory
of the artefacts actually selected and produced. Use `TraceabilityLinks.csv` as
the corresponding relationship edge list.

## Lean AI/ML Engineering Practice Pack

| # | Working artefact | Content it may absorb | Primary IDs |
|---:|---|---|---|
| 1 | Concept and Benefits Brief | Concept, needs and benefits | `NEED-`, `BEN-` |
| 2 | System / ML Requirements Specification | Functional, ML and non-functional requirements | `REQ-` |
| 3 | Requirements Traceability Matrix | Needs, benefits, requirements, V&V and evidence | `NEED-`, `BEN-`, `REQ-`, `VER-`, `VAL-`, `EVID-` |
| 4 | Design and Decision Record | Trade study, architecture and decision record | `DEC-`, `ADD-` |
| 5 | Data and Model Record | Provenance, quality, features, training and model card | `DATA-`, `DQA-`, `FEAT-`, `MODEL-`, `TRAIN-` |
| 6 | Risk and Assurance Register | Risks, controls and assurance claims | `RISK-`, `CTRL-`, `ASSUR-` |
| 7 | V&V Pack | Plan, procedures, evidence and summary | `VER-`, `VAL-`, `TEST-`, `EVID-`, `VVSR-` |
| 8 | Release / Deployment Readiness Record | Release decision, baseline and rollback | `REL-`, `CFG-` |
| 9 | Operational Assurance Record | Monitoring, drift, intervention and review | `MON-`, `PIR-` |

## Full AI/ML Engineering Practice Pack

| Area | Artefact | Primary IDs / objects |
|---|---|---|
| Framework | Framework Tailoring Record | `TAILOR-` |
| Framework | Artefact Catalogue | `CAT-`, controlled artefact IDs |
| Framework | Traceability Links | typed relationships between IDs |
| Concept | Concept of Operations | `NEED-`, `OBJ-`, `CON-`, scenarios |
| Concept | Stakeholder and Operational Needs Register | `NEED-` |
| Concept | Benefits Register | `BEN-` |
| Requirements | System / ML Requirements Specification | `REQ-` |
| Requirements | Requirements Traceability Matrix | `NEED-`, `BEN-`, `REQ-`, `VER-`, `VAL-`, `EVID-` |
| Decision | Decision Analysis / Trade Study | `DEC-` |
| Design | Architecture and Design Description | `ADD-` |
| Decision | Engineering Decision Record / ADR | `DEC-` |
| Data and model | Data Provenance Record | `DATA-` |
| Data and model | Data Quality Assessment | `DQA-` |
| Data and model | Feature / Transformation Specification | `FEAT-` |
| Data and model | Model Engineering Record / Model Card | `MODEL-`, `TRAIN-` |
| Risk and assurance | Risk Register | `RISK-` |
| Risk and assurance | Control Register | `CTRL-` |
| Risk and assurance | Assurance Claims Register / Assurance Case | `ASSUR-` |
| V&V | V&V Plan and Register | `VER-`, `VAL-` |
| V&V | V&V Procedure / Test Specification | `TEST-` |
| V&V | V&V Evidence / Test Record | `EVID-` |
| V&V | V&V Summary Report | `VVSR-` |
| Configuration | Configuration / Baseline Record | `CFG-` |
| Configuration | Change Request and Impact Assessment | `CHG-` |
| Release | Release / Deployment Readiness Record | `REL-` |
| Operation | Monitoring, Drift and Intervention Plan | `MON-` |
| Operation | Post-Implementation Review | `PIR-` |

Profiles may add specialist artefacts for predictive ML, GenAI/RAG, agentic
AI or high-consequence systems. Keep crosswalks to external standards optional
and versioned so that the core remains system-focused and lightweight.
