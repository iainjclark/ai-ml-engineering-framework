# AI/ML Engineering Framework

A practical lightweight framework for the development, assurance, deployment and operational review of AI/ML systems.

It adapts established practice [1, 2, 3] from systems engineering, software engineering and applied mathematics into a traceable AI/ML lifecycle.
It lets you get on with the work while preserving enough information and context so that when you are asked any of the sample engineering questions below,
you have the information at hand — **with evidence**.

The repository combines a staged set of technical artefacts with suggested Python utilities for evidence capture, diagnostics and operational assurance.

## Engineering Lifecycle

The framework organises AI/ML engineering work into ten areas that I have found work well in my projects.
I've trimmed it down a lot from [1, 2, 3] because it doesn't need to be rocket science.

| Stage | Engineering question |
|---|---|
| **01 — Concept** | Why are we building this and for whom? |
| **02 — Requirements** | What must the system do, and how well must it do it? |
| **03 — Decision Records** | Which approach should we choose, what alternatives exist, what did we decide, and why? |
| **04 — Architecture & Design** | How will the system be structured and implemented? |
| **05 — Risk & Assurance** | What could go wrong, and how will we control it? |
| **06 — V&V Design** | How will we establish that the system is fit for its intended use? |
| **07 — Configuration & Change** | What exactly constitutes the system, and how are changes controlled? |
| **08 — V&V Evidence** | What did verification and validation actually show? |
| **09 — Release to Production** | Is there sufficient evidence to release this version? |
| **10 — Post-Implementation Review** | What happened in operation, and what should change as a result? |

## AI-Assisted Project Management

Sample LLM prompts under `/prompts` help you create and maintain the engineering artefacts with machine assistance. 
Depending on the degree of LLM integration in your organisation, you may find this useful.
This can remove much of the administrative burden while leaving the engineering judgement and oversight with you.

Detailed guidance and reusable engineering artefacts for these stages are in `/docs`, though
realistically, Stage **00 — Framework** is the best place to start.

## System Diagnostics

The framework also includes lightweight utilities for capturing execution-environment and software provenance.

From the command line:

```bash
python -m src.diagnostics
```

or from Python/Jupyter:

```python
from src.diagnostics import capture_diagnostics, format_diagnostics
print(format_diagnostics(capture_diagnostics()))
```

Example output:

```text
System:    LENOVO 20L8S4CA00
Compute:   Intel Core i7-8650 (8th Gen) | 4 cores / 8 threads | NVIDIA GeForce MX150 | 2.0 GB VRAM
Memory:    40 GB RAM
Storage:   WDC PC SN720 SDAQNTW-512G-1001 | 512 GB | NVMe
OS:        Windows 10 (10.0.19045)
Runtime:   CPython 3.12.13 | AMD64 | 64-bit
AI Stack:  scikit-learn 1.9.0 | PyTorch 2.12.1+cu126 | TensorFlow 2.21.0
```


<!--
Planned diagnostic capabilities:

### Leakage Diagnostics
- train/test leakage
- temporal leakage
- target leakage
- feature leakage

### Data Quality Diagnostics
- missingness
- schema violations
- distribution anomalies

### Model Diagnostics
- performance
- calibration
- residual/error behaviour

### Drift Diagnostics
- input drift
- prediction drift
- outcome/performance drift

### Operational Diagnostics
- inference health
- latency
- failures

Add sections to the rendered README only when executable functionality exists.
-->


## Proof of Concept - Petrol Price Predictor

**PoC:** *Demonstrates application of the framework across the operational ML lifecycle.*

The framework will be illustrated using a live petrol-price prediction model, with
GitHub Actions supporting automated inference, monitoring, drift detection
and controlled rollback.

<!--
## Proof of Concept II - Interactive Assurance Demonstrator

**PoC II:** *Demonstrates interrogation and traceability of the resulting engineering evidence.*

A web interface is planned over the end-to-end petrol-price example, including its production monitoring and model-drift evidence.

The planned evidence-grounded AI assistant will allow users to ask engineering and project-management questions about the system in natural language. 
In effect, this will provide a lightweight management interface over the engineering evidence, giving users direct access to the current status of the project together with supporting evidence and history.

Example questions one might ask the AI assistant:

- "What are the highest current risks?"
- "Which requirements have not yet been verified?"
- "Is the model currently showing evidence of drift?"
- "What evidence supports a particular requirement or control?"

### Candidate Technologies Under Consideration

| Platform | Fit /20 | Best use here |
|---|---:|---|
| Streamlit Community Cloud | 19 | Best first public demo |
| Render + Streamlit/FastAPI | 18 | Best when more production-like control is required |
| Hugging Face Spaces | 17 | Strong AI/demo visibility, especially with Gradio/Streamlit |
| Vercel + separate Python API | 15 | Polished web application, but greater engineering overhead |
| GitHub Pages | 10 | Suitable for documentation, but limited for a live Python/chatbot backend |

Assistant responses should be grounded in, and traceable to, the controlled
engineering artefacts rather than acting as an independent source of truth.

The interactive layer is optional; the underlying engineering framework remains 
usable independently of any AI assistant.
-->

## Foundational References

\[1\] National Aeronautics and Space Administration, *NASA Systems Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC, USA: NASA, 2016.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer, *Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ, USA: John Wiley & Sons, 2011.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA: Pearson, 2016