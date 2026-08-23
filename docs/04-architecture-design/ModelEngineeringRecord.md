# Model Engineering Record / Model Card

Typical usage: `MODEL-001.md`, `MODEL-002.md`, ...

Use this record for the engineering definition and lifecycle history of
a model. Use `TRAIN-###` identifiers for material training runs or
trained model instances where individual traceability is useful.

## Document Control

Model Record ID: `MODEL-###`\
System / Project:\
Model Name:\
Model Version:\
Status: Proposed / Development / Validated / Released / Retired\
Date:\
Owner:\
Approved by:

## 1. Purpose and Intended Use

State what the model is intended to do, who or what uses its outputs,
and the operational decision or system function it supports.

Record:

-   intended use
-   intended users / consuming systems
-   prediction, classification, ranking, estimation or other task
-   unit of prediction / analysis
-   important out-of-scope or prohibited uses
-   relevant `REQ-###`, `BEN-###`, `NEED-###` and `DEC-###` references

## 2. Model Context and Interfaces

Describe where the model sits within the system architecture and how it
interacts with surrounding components.

Record:

-   upstream inputs and data sources
-   feature / transformation dependencies
-   invocation mechanism or interface
-   outputs and their meaning
-   downstream consumers
-   important runtime or platform dependencies

Reference the applicable `ADD-###`, `DATA-###`, `DQA-###` and
(if used) `FEAT-###` artefacts rather than duplicating their detailed content.

## 3. Model Definition

Describe the model sufficiently to identify what has been engineered.

Record, where applicable:

-   model family / algorithm
-   target or outcome definition
-   principal input features
-   output form
-   objective / loss function
-   important hyperparameters
-   decision threshold(s)
-   calibration method
-   random seed / determinism controls
-   software framework and material dependencies

Explain important modelling choices through references to `DEC-###`
records where appropriate.

## 4. Training and Model Build

Describe how the model is produced.

Record:

-   training dataset / snapshot reference
-   training period or observation window
-   train / validation / test split method
-   temporal or grouping constraints
-   sampling / weighting approach
-   preprocessing and feature pipeline
-   class-imbalance treatment, where relevant
-   tuning / model-selection method
-   leakage controls
-   reproducibility information
-   code version / commit
-   execution environment
-   resulting model artefact / checksum / registry reference

### Training Run Record

Use a stable `TRAIN-###` identifier for a material training run where
individual traceability is useful.

  -------------------------------------------------------------------------
  Training Run  Date        Data /      Code /      Resulting   Notes
                            Snapshot    Config      Model       
                                                    Version     
  ------------- ----------- ----------- ----------- ----------- -----------
  `TRAIN-###`                                                   

  -------------------------------------------------------------------------

Routine experimental runs do not need individual records unless they
materially support a decision, V&V claim or released model.

## 5. Performance and Engineering Characteristics

Summarise the model characteristics that matter for its intended use.

Record only metrics that are relevant to the requirements and decision
context, for example:

-   predictive performance
-   calibration
-   uncertainty
-   robustness / sensitivity
-   latency / throughput
-   resource consumption
-   stability across important segments or operating conditions
-   comparison with baseline or incumbent approach

  -----------------------------------------------------------------------
  Characteristic /  Requirement /     Result            Evidence
  Metric            Criterion                           
  ----------------- ----------------- ----------------- -----------------
                    `REQ-###`                           `EVID-###`

  -----------------------------------------------------------------------

Detailed test results should remain in the V&V evidence rather than
being reproduced here.

## 6. Assumptions, Limitations and Failure Modes

Record the assumptions and limitations that materially affect safe or
effective use of the model.

Consider:

-   population / domain assumptions
-   data coverage limitations
-   extrapolation limits
-   known weak segments or conditions
-   sensitivity to missing, delayed or erroneous inputs
-   concept or data drift
-   proxy variables or confounding
-   uncertainty not represented in the output
-   failure modes and foreseeable misuse

Reference relevant `RISK-###` and `CTRL-###` records.

## 7. Verification and Validation

Identify the V&V activities needed to establish that the model is fit
for its intended use.

Reference:

-   `VER-###`
-   `VAL-###`
-   `EVID-###`
-   `VVSR-###`, where used

Summarise the current V&V status and any unresolved findings. Do not
duplicate the detailed V&V records.

## 8. Operational Use and Monitoring

Describe the model-specific conditions that must be maintained in
operation.

Record, where applicable:

-   required input/data conditions
-   inference threshold or decision policy
-   monitoring metrics
-   drift indicators
-   performance indicators
-   alert or intervention thresholds
-   retraining / review triggers
-   fallback or degraded mode
-   rollback / replacement conditions

Reference relevant `REL-###` and `MON-###` records.

## 9. Model Version History

Preserve material changes to the model and its engineering basis.

  -------------------------------------------------------------------------
  Model       Date        Training Run  Change      Reason /    Status
  Version                                           Decision    
  ----------- ----------- ------------- ----------- ----------- -----------
                          `TRAIN-###`               `DEC-###`   

  -------------------------------------------------------------------------

Create a new model version when a change materially affects behaviour,
evidence, assumptions, interfaces or operational use. Do not rewrite
historical released-model records to make them describe a later model.

## 10. Traceability

Give each engineered model a stable `MODEL-###` identifier and material
training runs stable `TRAIN-###` identifiers where useful.

Trace the model backward to the requirements and decisions that define
its purpose and design, and to the data and transformations from which
it is produced.

Trace the model forward to the V&V evidence, release decision and
operational monitoring that establish and maintain fitness for use.

A typical path is:

`REQ-###` → `DEC-###` → `DATA-###` / `DQA-###` / `FEAT-###` (if used) →
`MODEL-###` / `TRAIN-###` → `VER-###` / `VAL-###` → `EVID-###` →
`REL-###` → `MON-###`

The purpose is to show **what model was engineered, why it was designed
that way, what data and training process produced it, what evidence
supports its use, and under what conditions it remains fit for
purpose**.

## 11. References

See the `04-architecture-design/README.md` for the systems-engineering
guidance informing this template.

For specific project models, cite the requirements, decision records,
data records, feature specifications, technical references, software
documentation, V&V evidence and other sources actually used to engineer
and assess the model.
