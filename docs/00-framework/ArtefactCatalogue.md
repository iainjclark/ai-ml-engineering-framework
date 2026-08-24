Note: The sequential indices used below to identify engineering artefacts
are independent of the ten lifecycle stage numbers under `/docs`. Artefact
numbers identify items in the practice pack; stage numbers identify where
engineering activities are performed.


## Lean ML/AI Engineering Practice Pack

| # | Core working artefact | Primary IDs / objects | Absorbs / covers |
|---:|---|---|---|
| 1 | Benefits Register | `BEN-` | Benefits |
| 2 | System / ML Requirements Specification | `REQ-` | System and ML requirements |
| 3 | Requirements Traceability Matrix | `BEN ↔ REQ ↔ VER ↔ EVID` | Requirements traceability |
| 4 | Decision Record | `DEC-` | Decision analysis + trade study + ADR / decision log |
| 5 | Architecture & Design Description | `ADD-` | Architecture + design |
| 6 | Data Provenance Record | `DATA-` | Data provenance |
| 7 | Data Quality Assessment | `DQA-` | Data quality |
| 8 | Model Engineering Record / Model Card | `MODEL-`, `TRAIN-` | Model + training record |
| 9 | Risk Register | `RISK-`, `CTRL-` | Risks + identified controls |
| 10 | V&V Plan & Register | `VER-`, `VAL-` | V&V plan + planned activities |
| 11 | V&V Evidence / Test Record | `EVID-` | Executed V&V evidence |
| 12 | Release / Deployment Record | `REL-` | Release decision |
| 13 | Monitoring, Drift & Intervention Record | `MON-` | Monitoring + drift + intervention |

## Full ML/AI Engineering Practice Pack

| # | Artefact | Primary IDs / objects |
|---:|---|---|
| | **Concept & requirements** | |
| 0a | Concept of Operations (CONOPS) | `NEED-`, `CON-`, scenarios |
| 0b | Project Charter | Scope, stakeholders, constraints |
| 0c | Stakeholder Needs Register | `NEED-` |
| 1 | Benefits Register | `BEN-` |
| 2 | System / ML Requirements Specification | `REQ-` |
| 3 | Requirements Traceability Matrix | `NEED ↔ BEN ↔ REQ ↔ VER ↔ EVID` |
| | **Decision & design** | |
| 4 | Decision Record | `DEC-` |
| 5 | Architecture & Design Description | `ADD-` |
| | **Data & model engineering** | |
| 6 | Data Provenance Record | `DATA-` |
| 7 | Data Quality Assessment | `DQA-` |
| 7a | Data Transformation (ETL) & Feature Engineering Specification | `ETL-`, `FEAT-` |
| 8 | Model Engineering Record / Model Card | `MODEL-`, `TRAIN-` |
| | **Risk & assurance** | |
| 9 | Risk Register | `RISK-`, `CTRL-` |
| 9a | Control Register | `CTRL-` |
| 9b | Assurance Claims Register  | `ASSUR-`, Register of assurance claims from which assurance cases can be constructed |
| | **Verification & validation** | |
| 10 | V&V Plan & Register | `VER-`, `VAL-` |
| 10a | V&V Procedure / Test Specification | `TEST-` |
| 11 | V&V Evidence / Test Record | `EVID-` |
| 11a | V&V Summary Report | `VVSR-` |
| 11b | Validation Traceability Matrix | `REQ ↔ VAL ↔ EVID` |
| | **Production & operation** | |
| 12 | Release / Deployment Record | `REL-` |
| 12a | Configuration / Baseline Record | `CFG-` |
| 12b | Change Request / Bug Fix & Impact Assessment | `CHG-`, `BUG-` |
| 12c | Milestone Change Log | Milestones, baseline/change history |
| 13 | Monitoring, Drift & Intervention Record | `MON-` |
| 13a | Post-Implementation Review / Operational Review | `PIR-` |

### Control identification

In the Lean Pack, controls may be recorded directly in the Risk Register and
given stable `CTRL-###` identifiers where individual traceability is useful.

A separate Control Register is not required for lightweight use of the framework.
Where more extensive control management is warranted, a standalone Control
Register is available in the Full Pack, should it be useful.

### ETL and feature engineering

In the Lean Pack, data transformation and feature engineering may be documented
within `ADD-###` or `DATA-###` rather than a separate specification. A standalone
ETL & Feature Engineering Specification is available in the Full Pack where
pipeline complexity warrants it.
