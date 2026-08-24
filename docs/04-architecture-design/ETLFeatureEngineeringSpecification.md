# Feature / Transformation Specification

Typical usage: `ETL-001.md`, `ETL-002.md`, ...

Use this record for the data transformation definition and lifecycle history of
model precursors; use `FEAT-###` identifiers for feature engineering definition 
and lifecycle history.

## Document Control

Specification ID: `FEAT-###`\
System / Project:\
Model / Pipeline:\
Version / Baseline:\
Status: Draft / Under Review / Approved / Superseded\
Date:\
Owner:\
Approved by:

## 1. Purpose

Define the engineered features and transformations used to convert
source data into model-ready inputs or other derived data products.

The specification should make material feature engineering
**understandable, reproducible and traceable** without duplicating
source-data, implementation or V&V records.

Reference relevant `REQ-###`, `DEC-###`, `ADD-###`, `DATA-###`,
`DQA-###` and `MODEL-###` records where available.

## 2. Scope

State what this specification covers.

Identify:

-   dataset(s), pipeline(s) or model(s) to which it applies
-   transformation boundary
-   important upstream inputs
-   downstream consumers
-   transformations explicitly outside scope

## 3. Feature / Transformation Register

Give each material engineered feature or transformation a stable
`FEAT-###` identifier where individual traceability is useful.

  -------------------------------------------------------------------------------------------
  FEAT-ID      Feature /        Source       Definition / Output     Purpose    Related IDs
               Transformation   Field(s) /   Logic        Type /                
                                Data                      Unit                  
  ------------ ---------------- ------------ ------------ ---------- ---------- -------------
  `FEAT-###`                    `DATA-###`                                      `REQ-###` /
                                                                                `DEC-###` /
                                                                                `MODEL-###`

  -------------------------------------------------------------------------------------------

The definition should be precise enough for an independent practitioner
to understand what the transformation is intended to do. Where
implementation code is authoritative, reference the code rather than
reproducing it in full.

## 4. Transformation Sequence and Dependencies

Describe any ordering or dependency between transformations that
materially affects the resulting data.

For example:

`source data` → `cleaning` → `normalisation` → `aggregation` →
`derived feature` → `model input`

Record important dependencies such as:

-   transformations that must occur before others
-   shared intermediate variables
-   joins or aggregations
-   windowing or lag construction
-   fitted preprocessing parameters
-   external reference data
-   model-specific preprocessing

A diagram may be used where it communicates the pipeline more clearly
than text.

## 5. Data Handling Rules

Record transformation rules that materially affect data meaning or model
behaviour.

Consider, where applicable:

-   missing-value treatment
-   invalid-value handling
-   categorical encoding
-   scaling / normalisation
-   clipping / winsorisation
-   outlier treatment
-   date / time handling
-   unit conversions
-   joins and keys
-   aggregation
-   filtering / exclusions
-   imputation
-   text / image / signal preprocessing

Reference `DQA-###` evidence where a transformation is motivated by an
identified data-quality condition.

## 6. Temporal and Leakage Controls

For predictive or time-dependent systems, describe how the feature
pipeline prevents information unavailable at prediction time from
entering model inputs.

Record, where relevant:

-   observation time
-   prediction / decision time
-   target availability
-   lag definitions
-   rolling-window boundaries
-   train / validation / test cut-offs
-   point-in-time joins
-   future-information exclusions
-   leakage checks

Reference relevant `RISK-###`, `CTRL-###`, `VER-###` or `VAL-###`
records.

## 7. Fitted Transformations

Identify transformations whose behaviour depends on parameters learned
or estimated from data.

Examples include:

-   scalers
-   imputers
-   encoders
-   dimensionality reduction
-   feature selection
-   learned embeddings
-   vocabulary construction

For each material fitted transformation, record:

  --------------------------------------------------------------------------
  FEAT-ID        Fitted On      Parameters /   Version /      Application
                                Artefact       Evidence       Rule
  -------------- -------------- -------------- -------------- --------------
  `FEAT-###`                                                  

  --------------------------------------------------------------------------

Parameters fitted using training data should be applied consistently to
validation, test and operational data unless an explicitly controlled
alternative is justified.

## 8. Assumptions, Constraints and Limitations

Record assumptions or limitations that materially affect feature
validity.

Consider:

-   expected units and ranges
-   source-system semantics
-   population / domain assumptions
-   data freshness
-   sampling frequency
-   availability at inference time
-   stability of categories or codes
-   dependency on external mappings
-   sensitivity to missing or delayed inputs
-   extrapolation beyond observed ranges

Reference relevant risks or requirements rather than duplicating them.

## 9. Implementation and Configuration

Identify where the transformations are implemented and how the
implementation is controlled.

Record, where applicable:

-   source-code location
-   module / function / SQL object
-   configuration file
-   pipeline / workflow
-   code commit / tag
-   dependency version
-   transformation artefact version
-   execution environment

The specification describes the intended engineering behaviour;
controlled implementation and configuration records establish the exact
executable state.

## 10. Verification and Validation

Identify how the feature and transformation implementation will be
checked.

Consider:

-   unit tests for transformation logic
-   schema / type checks
-   boundary and edge cases
-   missing / invalid input behaviour
-   numerical checks
-   point-in-time / leakage tests
-   reproducibility
-   consistency between training and inference pipelines
-   comparison against independently calculated results where useful

Reference `VER-###`, `VAL-###` and `EVID-###` rather than duplicating
detailed test evidence.

## 11. Change and Version History

Record material changes that affect feature meaning, behaviour,
assumptions or model compatibility.

  --------------------------------------------------------------------------
  Version / Date FEAT-ID(s)     Change         Reason /       Impact /
                                               Decision       Related IDs
  -------------- -------------- -------------- -------------- --------------
                 `FEAT-###`                    `DEC-###`      `MODEL-###` /
                                                              `CHG-###`

  --------------------------------------------------------------------------

Changes to material transformations should be assessed for impact on
trained models, V&V evidence, release status and operational monitoring.

## 12. Traceability

A typical feature-engineering traceability path is:

`REQ-###` / `DEC-###` → `DATA-###` / `DQA-###` → `FEAT-###` →
`MODEL-###` / `TRAIN-###` → `VER-###` / `VAL-###` → `EVID-###`

Where feature changes affect a released system:

`FEAT-###` → `CHG-###` → `MODEL-###` → V&V → `REL-###`

The purpose is to show **where a feature came from, what transformation
was applied, why it exists, how it is implemented, and what evidence
supports its correct use**.

## 13. References

See the `04-architecture-design/README.md` for the systems-engineering
guidance informing this template.

For specific projects, cite source-data documentation, data
dictionaries, decision records, algorithms, technical references, code,
configuration and other sources actually used to define the feature and
transformation pipeline.
