# 08 — RANKED RESEARCH DIRECTIONS

Ranking criteria (each 1–5): **Fit-to-CALL** (matches the topic's explicit method set + intent, [POLIMI PDF]), **Novelty/Defensibility** (survives adversarial check, [LITERATURE]/[INFERENCE]), **Feasibility** (tractable in 3 yrs, host-group platform/experimental fit), **Certification value** (differentiator vs prior art). Total /20.

| ID | Direction | Fit | Novelty | Feas | Cert | Total | Verdict |
|----|-----------|-----|---------|------|------|-------|---------|
| D1 | Integrated flatness/NDI + L1-inspired + embedded CA + structured residual + certification | 5 | 5* | 4 | 5 | 19 | **PRIMARY** |
| D2 | L1-inspired augmentation of flatness/NDI + degradation-aware embedded CA | 5 | 4 | 4 | 4 | 17 | Core pillar |
| D3 | Physically-structured residual preserving interpretability + certifiable margin | 5 | 4 | 4 | 5 | 18 | Core pillar |
| D4 | Multi-fidelity validation & certification assurance methodology | 4 | 4 | 4 | 5 | 17 | Differentiator |
| D5 | Interpretability/certification framework for the unified loop | 4 | 4 | 3 | 5 | 16 | Theoretical |
| D6 | Trajectory–control co-design via allocation nullspace under degradation | 4 | 3 | 4 | 3 | 14 | Supporting |
| D7 | Degradation-aware CA co-designed with adaptation bandwidth | 4 | 3 | 4 | 4 | 15 | Supporting |
| D8 | CBF/safe-set layer | 2 | 1 | 4 | 2 | 9 | **REJECT** (baseline only) |
| D9 | Pure data-driven/RL | 1 | 1 | 3 | 1 | 6 | **REJECT** (off-topic) |

\* D1 novelty = the *assembly*, not components (see `06`, `07`). **[INFERENCE]**

## Decision
- **Adopt D1 as the PhD research direction.** It is the only direction that (a) uses the CALL's exact method vocabulary, (b) survives both adversarial passes (no prior paper delivers this assembly), and (c) supplies a certification/multi-fidelity differentiator that the strongest competitors (Lovera H∞+CA, Delft INCA, Gahlawat L1-GP, B1 SINDy-CA) lack. **[RESEARCH GAP]**
- **D2 and D3 are mandatory technical pillars** of D1 (without them D1 is hollow).
- **D4 and D5 are the defensibility backbone** — they convert "another adaptive-CA paper" into "a certifiable, multi-fidelity-validated architecture," which is the unique selling point.
- **D6 and D7 are high-value supporting contributions** that increase experimental relevance and exploit over-actuation (a topic emphasis).
- **D8 = competitor baseline** (compare L1/robust vs CBF safety). **D9 = excluded** by the interpretability requirement.

## Recommended PhD scope (one coherent programme)
> *An interpretable, model-based (flatness/NDI) control architecture for over-actuated autonomous aerospace vehicles, with embedded control allocation (saturation/rate/degradation), L1-inspired adaptive uncertainty compensation, and a physically-structured data-informed residual-dynamics module — validated by a multi-fidelity methodology and supported by a certification-oriented interpretability argument.*

Pillars: D2 (L1+CA), D3 (structured residual). Backbone: D4 (multi-fidelity), D5 (certification framework). Supporting: D6 (trajectory–control co-design), D7 (degradation+adaptation co-design).

See `09_research_architecture.md`.
