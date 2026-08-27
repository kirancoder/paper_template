# 12 — THREE-YEAR RESEARCH ROADMAP

Aligned to the PRIMARY direction D1 (`08`), architecture (`09`), questions (`10`), validation (`11`). Year labels Y1–Y3; milestones Mx. Tag [HYPOTHESIS] for planned contributions; dates are relative to a 42° cycle start (~late 2026).

## YEAR 1 — Foundations, nominal core, baselines (months 1–12)
- **M1 (m1–3):** Literature consolidation; reproduce host-group flatness/NDI controller (S1–S4) on simulation; implement in-house baselines: H∞+CA (B9/B10), MRAC+ACA (Falconí), CBF (Hafner), Gahlawat L1-GP, B1 SINDy-CA. **[LITERATURE]**
- **M2 (m4–6):** Build high-fidelity over-actuated 6-DoF simulation (or adopt group model). Implement **embedded CA** inside the flatness/NDI loop (saturation/rate/degradation-aware), establishing RQ1 nominal results. **[HYPOTHESIS]**
- **M3 (m7–9):** **Structured residual identification** (hybrid first-principles + sparse/parametric) from simulated+group data; UQ; address RQ2. Compare interpretability/accuracy vs black-box GP. **[HYPOTHESIS]**
- **M4 (m10–12):** First integration: flatness/NDI + structured residual + embedded CA; stability proof (no L1 yet). Deliverable: conference paper on integrated interpretable model-based+CA architecture (establishes baseline novelty vs B11/B9/B10).
- *Year-1 checkpoint:* nominal architecture + residual ID + baselines ready.

## YEAR 2 — L1-inspired augmentation, certification framework, multi-fidelity (months 13–24)
- **M5 (m13–15):** Add **L1-inspired adaptive augmentation** inside the embedded-CA loop (RQ3); prove robustness/transient margin with CA-in-the-loop. **[HYPOTHESIS]**
- **M6 (m16–18):** **Certification/interpretability framework** (RQ4): combine L1 margin + residual UQ + CA μ-analysis into one verifiable statement; draft assurance case. **[HYPOTHESIS]**
- **M7 (m19–21):** **Multi-fidelity methodology** (RQ5): analytical→data-enhanced→HIL; quantify uncertainty transfer. Begin HIL on group real-time target. **[HYPOTHESIS]**
- **M8 (m22–24):** **Co-design of adaptation bandwidth & allocation** (RQ6, D7) + trajectory–control nullspace co-design (D6). Deliverable: journal paper on L1-inspired+embedded-CA+structured-residual with certification margin; conference paper on multi-fidelity validation.
- *Year-2 checkpoint:* full integrated architecture + certification argument + HIL.

## YEAR 3 — Experimental validation, adversarial benchmarking, thesis (months 25–36)
- **M9 (m25–27):** **Flight-test campaign** on group over-actuated UAV / tilt-rotor / octorotor testbed: nominal tracking, induced degradation/failure, graceful recovery; certifiable-margin monitoring. **[HYPOTHESIS]**
- **M10 (m28–30):** **Adversarial benchmarking** vs all baselines (B9/B10, Falconí, Hafner, Gahlawat, B1, B11); multi-fidelity closure of certification margin. Deliverable: journal paper (experimental) + assurance-case white paper.
- **M11 (m31–33):** Consolidate; write thesis chapters; refine contributions vs CALL requirements ([POLIMI PDF]).
- **M12 (m34–36):** Thesis submission & defence prep. Final deliverable: PhD thesis "Interpretable, model-based, over-actuated control with embedded allocation, L1-inspired adaptive compensation, and structured data-informed residual — a certifiable, multi-fidelity-validated architecture."

## Risk register
- **Integration complexity** → mitigate by incremental Y1→Y3 stacking (nominal→residual→L1→certification→experiment).
- **Experimental platform access** → mitigate: if thrust-vectoring UAV unavailable, use octorotor/tilt-rotor over-actuated proxy (validated by B6/B5/D8).
- **Certification acceptance** → mitigate: target *assurance case + verifiable margin* (realistic) rather than full authority certification.
- **Adversarial obsolescence** → mitigate: continuous literature watch (the field is fast — B1, Hafner, Traas all 2025–2026); emphasise the assembly + certification differentiator, which has not been closed.

## Success criteria (mapping to CALL)
1. Interpretable model-based (flatness/NDI) core — ✓ CALL item.
2. Embedded CA (sat/rate/degradation) — ✓ CALL "control allocation as part of architecture".
3. L1-inspired / adaptive compensation — ✓ CALL "L1-inspired architectures / adaptive".
4. Physically-structured data-informed residual — ✓ CALL "data-informed modelling / residual-dynamics".
5. Interpretability/certifiability argument — ✓ CALL "interpretability / certifiability".
6. Multi-fidelity validation — ✓ CALL "different levels of model fidelity".
7. Over-actuated aerospace vehicle + experimental validation — ✓ CALL "over-actuated / redundant / actuator failures".

See `00_session_state.md` for live status; `07`–`11` for supporting detail.
