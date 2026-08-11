# Petrol Price Predictor — Worked Golden Path

This directory is a compact, end-to-end example of applying the framework to a
weekly petrol-price decision-support service.

All organisations, data, results, hashes and approvals in this example are
**fictional and illustrative**. They demonstrate a controlled engineering
record; they are not evidence for a real production system or a claim about
actual petrol prices.

## Scenario

The example system produces a weekly seven-day-ahead UK petrol-price estimate
from a synthetic, non-personal time series. A procurement analyst may use the
estimate as one input to planning, but the system does not place orders or make
autonomous decisions.

The tailored lean pack follows this chain:

```text
BEN-001 -> SYS-REQ-001 -> DEC-001 -> ADD-001 -> VER-001 -> EVID-001
                              |
RISK-001 -> CTRL-001 ---------+-------------> VER-002 -> EVID-002

CFG-001 -> REL-001 -> MON-001 -> PIR-001
```

`00-framework/ArtefactCatalogue.yaml` is the inventory. The relationship graph
is in `00-framework/TraceabilityLinks.csv`.

## Reading order

1. Start with the tailoring record and concept brief.
2. Follow the stable IDs through requirements, decision analysis and design.
3. Compare the V&V plan with the later evidence record.
4. Inspect the exact release decision and operational monitoring plan.
5. Finish with the post-implementation review and its feedback actions.

The example deliberately combines risk and control information in a CSV because
the tailoring decision selected a lean pack. A full-profile project would split
these into independently controlled registers.
