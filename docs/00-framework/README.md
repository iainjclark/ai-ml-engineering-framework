# 00 — AI Engineering Practice Framework

> **How do we apply the framework to engineer an AI/ML system?**

## Purpose

ai-ml-engineering-framework provides a lightweight engineering structure for developing, evaluating, releasing and operating AI/ML systems.

It brings together systems engineering, software engineering, mathematical modelling and AI/ML practice into a common lifecycle with explicit decisions, risks, evidence and traceability.

The framework is intended to help practitioners answer not only:

> **Does the model work?**

but also:

> **Why are we building it, what must it do, why did we choose this design, what could go wrong, what evidence supports it, and should it be in production?**

ai-ml-engineering-framework is an engineering practice framework, not a prescribed development methodology. It can be used alongside Waterfall, Agile, DevOps, MLOps and existing organisational processes.

---

## Who Is It For?

ai-ml-engineering-framework is intended for people who design, build, evaluate, deploy or take technical responsibility for AI/ML systems, including:

- AI/ML engineers
- data scientists
- software engineers
- systems engineers
- applied mathematicians
- technical leads
- assurance and risk practitioners

It is particularly useful where an AI/ML system has meaningful operational, financial, safety, regulatory or organisational consequences.

---

## Principles

ai-ml-engineering-framework is based on a small number of principles.

### Engineer the system, not just the model

The model is one component of a larger system involving data, software, infrastructure, people, processes and operational decisions.

### Make important decisions explicit

Important technical choices should have a recorded rationale, alternatives considered and supporting evidence.

### Define evidence before relying on results

Verification and validation should be planned before the final evidence is available, with methods and acceptance criteria defined in advance where practical.

### Maintain traceability

Important needs should be traceable through requirements, design decisions, risks, verification and validation activities, and evidence.

### Treat mathematics as engineered content

Mathematical analysis and modelling should expose assumptions, approximations, limitations, uncertainty and justification rather than being treated as an opaque calculation.

### Control what reaches production

Code, models, data, dependencies, configuration and infrastructure should be identifiable and sufficiently controlled to reproduce, assess and change the deployed system.

### Learn from operation

Release is not the end of engineering. Operational evidence should feed back into requirements, risks, decisions and future changes.

### Apply the framework proportionately

Not every project needs the same amount of documentation or assurance. Use enough engineering control for the complexity, uncertainty and consequences of the system.

---

## Lifecycle

ai-ml-engineering-framework organises engineering work into eleven areas. They have a natural sequence, but the focus of the engineering team may move backwards as well as forwards as the project develops.

| Stage | Question |
|---|---|
| **01 — Concept** | Why are we building this and for whom? |
| **02 — Requirements** | What must the system do, and how well must it do it? |
| **03 — Decision Analysis** | Which approach should we choose, and why? |
| **04 — Architecture & Design** | How will the system be structured and implemented? |
| **05 — Risk & Assurance** | What could go wrong, and how will we control it? |
| **06 — V&V Design** | How will we establish that the system is fit for its intended use? |
| **07 — Decision Log** | What important decisions have we made and why? |
| **08 — Configuration & Change** | What exactly constitutes the system, and how are changes controlled? |
| **09 — V&V Evidence** | What did verification and validation actually show? |
| **10 — Release to Production** | Is there sufficient evidence to release this version? |
| **11 — Post-Implementation Review** | What happened in operation, and what should change as a result? |

The stages are numbered to provide a natural engineering sequence, but they are not a strict waterfall.

Engineering is often iterative. New evidence may change a requirement, expose a risk, invalidate a decision or require a design change. Subject to your organisational constraints and the 
constraints of each particular project, return to earlier stages whenever necessary.

---

## Traceability

Important engineering information should be given stable identifiers and linked across the lifecycle.

For example:

`NEED-001` → `REQ-003` → `DEC-002` → design → `VER-004` → `EVID-004`

A risk may introduce additional links:

`RISK-003` → control → `VER-007` → `EVID-007`

The exact identifiers matter less than maintaining enough linkage to answer questions such as:

- Why does this requirement exist?
- Which design decision satisfies it?
- What evidence demonstrates that it has been met?
- Which risks depend on this control?
- What changed between releases?
- What evidence supported the release decision?

Traceability should help engineering work, not become paperwork for its own sake.

The verification and validation (V&V) of such an engineered system can be represented diagrammatically in the first part of this diagram. Other chains of linkage are shown also.

```
            ┌── REQ ── VER ── EVID
BEN / NEED ─┤
            └── VAL ──────── EVID

REQ  → DEC  → ADD

RISK → CTRL → VER → EVID

DATA → MODEL → VER → EVID

CI   → CHG
```

The upper path represents verification: requirements are linked to planned verification activities and the evidence demonstrating whether they were satisfied. The lower path represents validation: stakeholder needs, intended benefits or intended use are linked to validation activities and the resulting evidence.

---

## How Much of the Framework Should I Use?

Use the framework proportionately.

A small, low-consequence experimental model may need only short documents and a small number of records.

A production system making consequential decisions may require detailed requirements, formal decision analysis, extensive risk controls, planned V&V, configuration management and explicit release approval.

A useful rule is:

> **Increase engineering rigour as complexity, uncertainty and consequence increase.**

Sections that are not relevant may be marked **Not Applicable**, with a short explanation where useful.

Do not create documentation merely to fill every template.

---

## Starting a Project

For a new project:

1. Copy or instantiate the ai-ml-engineering-framework project structure.
2. Start with **01 — Concept** and establish the problem, stakeholders, objectives, constraints and intended use.
3. Develop measurable requirements in **02 — Requirements**. This can be done as BDUF (Big Design Up Front), incrementally through Agile stories, or somewhere in between. Your project, your rules.
4. Record important alternatives and engineering choices as the design develops.
5. Identify risks early rather than waiting until release.
6. Decide how important claims and requirements will be verified or validated.
7. Maintain configuration, decisions and traceability as the system changes.
8. Collect V&V evidence against the methods and criteria previously defined.
9. Make an explicit release decision based on the controlled system, available evidence and remaining risk.
10. Review operational outcomes and feed what was learned back into the engineering lifecycle.

Do not wait until the system is finished before creating its engineering record.

---

## Verification and Validation

ai-ml-engineering-framework separates the design of V&V from the resulting evidence.

**06 — V&V Design** asks:

> **What evidence will we need, how will we obtain it, and what results will be acceptable?**

**09 — V&V Evidence** asks:

> **What did we actually do, what happened, and what does the evidence support?**

Keeping these separate reduces the temptation to choose success criteria after seeing the results.

---

## What Counts as an Artefact?

An artefact is any controlled item that records useful engineering information.

Depending on the project, this may include:

- Markdown documents
- spreadsheets and registers
- architecture diagrams
- mathematical analyses
- notebooks
- source code
- tests and test results
- model cards
- data-quality reports
- configuration files
- CI/CD records
- issue trackers, Agile boards and project-management records (e.g. Jira and Trello)
- monitoring outputs
- release records

ai-ml-engineering-framework does not require engineering knowledge to be converted into documents when an existing technical artefact records it better.

Reference or link the authoritative artefact instead.

---

## Minimum Useful Application

A minimally useful application of ai-ml-engineering-framework should normally make it possible to determine:

- why the system exists;
- what important requirements it must satisfy;
- why major technical choices were made;
- what important risks were identified;
- how important claims were tested;
- what evidence was obtained;
- which version of the system was assessed;
- why it was or was not released; and
- what was learned from operation, where applicable.

Note that an LLM-based assistant can be built on top of these engineering records to answer many of these questions. Its answers should still be checked against the underlying evidence. I am not advising that it be used as a PM in a box; a PM can often feel boxed in, and this framework is meant to assist rather than add unnecessary process.

If those questions cannot be answered, the engineering record is probably incomplete. The engineering record is there to help _you_ answer those questions at the latter stages of the project, and afterwards.

I, the author, have learned the importance of maintaining such records from experience.

---

## Relationship to Other Practices

ai-ml-engineering-framework is intended to complement rather than replace established practices.

Systems engineering provides the lifecycle and system-level perspective.

Software engineering provides disciplined methods for constructing and maintaining the software components.

Applied mathematics provides methods for constructing, analysing and justifying mathematical models.

AI/ML engineering provides methods for developing and operating data-driven and learned components.

Risk, assurance, verification and validation provide the evidence needed to make responsible engineering decisions.

ai-ml-engineering-framework provides a lightweight structure for bringing these practices together around a production AI/ML system.

---

## Using the Stage Directories

Each numbered directory contains guidance and, where appropriate, reusable artefacts.

The README for each stage explains:

- **Purpose** — why the activity matters;
- **When Should It Be Created** — when to start it;
- **When Should It Be Updated** — what should cause it to change;
- **Inputs** — what information should already be available;
- **Activities** — what engineering work should be performed;
- **Outputs / Artefacts** — what should result;
- **Traceability** — how the stage connects to the rest of the engineering record; and
- **References** — sources supporting the engineering practice.

The templates are starting points. Adapt them when the project requires it.

---

## Status

ai-ml-engineering-framework is under active development.

The framework should be treated as practitioner guidance rather than as a standard, certification scheme or substitute for professional engineering judgement.

Feedback from practical application is encouraged, particularly where the framework is unclear, unnecessarily burdensome or fails to capture an important engineering activity.