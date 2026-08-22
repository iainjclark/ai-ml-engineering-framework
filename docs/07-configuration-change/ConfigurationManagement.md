# Configuration Management

## Repository

The authoritative source repository for this system is:

[Repository](https://github.com/...)

## Configuration Control

Source code, configuration, documentation and engineering artefacts are
maintained under Git version control.

Released baselines are identified using Git tags.

## Current Released Baseline

**Example configuration baseline (placeholder values only):**

Release: `v1.0.0`  
Git commit: `abc1234`  
Git tag: `v1.0.0`  
Date: YYYY-MM-DD

## Branching and Change Control

Changes are developed on branches and merged into the controlled main branch
following review and verification.

Significant engineering changes are recorded in `MilestoneChangeLog.xlsx`.

## Release Traceability

Each production release record *shall* identify the corresponding:

- Git commit and tag
- model version
- data version
- configuration version
- V&V evidence

Additionally, each production release record *may* identify, where required to reconstruct the released baseline:

- trained model artefacts and training hyperparameters
- feature stores
- data references
- development/execution platform, where relevant, e.g. IDE, notebook environment or managed cloud platform (Databricks, Snowflake)
- infrastructure configuration, e.g. specification of relevant hardware, operating system and execution environment used to build, train or run the release
- language/runtime specification, i.e. the exact Python/R version used at release
- software dependency information, e.g. `requirements.txt`, `pyproject.toml` or `environment.yml` (Python), or `renv.lock` (R)
- runtime parameters
- controlled engineering documents