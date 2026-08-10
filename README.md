# AI/ML Engineering Framework

A lightweight engineering framework for the development, assurance,
deployment and operational review of AI/ML systems.

The framework adapts established systems engineering, software engineering
and applied mathematical practice to AI/ML development, providing a
traceable lifecycle from stakeholder need and requirements through decision
analysis, architecture, risk, verification and validation, configuration
control, production release and post-implementation review.

## Proof of Concept I - Petrol Price Predictor

It will be illustrated using a live petrol-price prediction model, with
GitHub Actions supporting automated inference, monitoring, drift detection
and controlled rollback.

## Proof of Concept II - Interactive Assurance Demonstrator

A web interface is planned over the end-to-end petrol-price example, including its production monitoring and model-drift evidence.

This evidence-grounded AI assistant allows users to ask engineering and project management questions about the system in natural language. In effect, it provides a lightweight form of “management as a service” (MaaS) over the engineering evidence.

Example questions might include:

- What are the highest current risks?
- Why was this model approved for release?
- What changed in the latest baseline?
- Which requirements have not yet been verified?
- Is the model currently showing evidence of drift?
- What evidence supports a particular requirement or control?

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
