# AI/ML Engineering Framework

A lightweight engineering framework for the development, assurance,
deployment and operational review of AI/ML systems.

The framework adapts established systems engineering, software engineering
and applied mathematical practice to AI/ML development, providing a
traceable lifecycle from stakeholder need and requirements through decision
analysis, architecture, risk, verification and validation, configuration
control, production release and post-implementation review.

## Proof of Concept I - Petrol Price Predictor

**PoC I:** *Demonstrates application of the framework across the operational ML lifecycle.*

The framework will be illustrated using a live petrol-price prediction model, with
GitHub Actions supporting automated inference, monitoring, drift detection
and controlled rollback.

A fully populated, fictional engineering-record example is available in
[`examples/petrol-price-predictor`](examples/petrol-price-predictor/README.md).
It demonstrates tailoring, typed traceability, release evidence and operational
feedback before the live implementation is introduced.

## Proof of Concept II - Interactive Assurance Demonstrator

**PoC II:** *Demonstrates interrogation and traceability of the resulting engineering evidence.*

A web interface is planned over the end-to-end petrol-price example, including its production monitoring and model-drift evidence.

This evidence-grounded AI assistant allows users to ask engineering and project-management questions about the system in natural language. In effect, it provides a lightweight management interface over the engineering evidence, giving users direct access to the current status of the project together with its evidenced history.

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

# Foundational References

\[1\] National Aeronautics and Space Administration, *NASA Systems Engineering Handbook*, Rev. 2, NASA/SP-2016-6105 Rev. 2. Washington, DC, USA: NASA, 2016.

\[2\] A. Kossiakoff, W. N. Sweet, S. J. Seymour, and S. M. Biemer, *Systems Engineering: Principles and Practice*, 2nd ed. Hoboken, NJ, USA: John Wiley & Sons, 2011.

\[3\] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA: Pearson, 2016
