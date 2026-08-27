# 07 — CANDIDATE RESEARCH DIRECTIONS

Generated after two adversarial passes (`06` §A–E). Each direction is classified:
**VERY STRONG** (core PhD candidate) / **STRONG** / **MEDIUM** (supporting contribution) / **WEAK** / **REJECT** (off-topic or already solved). All tag [RESEARCH GAP] or [INFERENCE]; evidence tags [POLIMI PDF], [LITERATURE].

The adversarial pressure (Gahlawat L1-GP/CL1-GP; B1 SINDy-CA; Falconí MRAC+ACA; B7/B8 adaptive-CA; B9/B10 Lovera H∞+CA; B11 DI+CA FTC) means **NO component is novel alone**; novelty is the *integrated, certification-facing assembly* of the CALL's exact method set for the host group's over-actuated thrust-vectoring UAV. **[INFERENCE]**

---

## D1 — Integrated flatness/NDI + L1-inspired + embedded CA + structured residual, with certification-facing validation  [VERY STRONG — PRIMARY]
- **Core:** A unified, interpretable, model-based control architecture for OVER-ACTUATED autonomous aerospace vehicles that (i) uses a **flatness/NDI nominal core** (host group's established strength, [LITERATURE] S1–S4), (ii) **embeds control allocation in the control law** with saturation/rate/degradation handling (not downstream, [POLIMI PDF]), (iii) augments uncertainty compensation via an **L1-inspired/adaptive** mechanism and a **physically-structured data-informed residual** (first-principles + sparse/parametric identification, preserving the model), and (iv) is backed by an **interpretability/certification argument** + **multi-fidelity validation**.
- **Why it survives adversarial check:** every close paper misses ≥1 required element — B1 (SINDy-CA) lacks flatness/NDI core AND L1-inspired AND certification; Falconí/B7/B8 use MRAC/H∞/SMC not L1-inspired; B9/B10 (host group) use H∞/μ-analysis not flatness+L1+structured-residual; Gahlawat lacks CA/over-actuation. The CALL explicitly bundles these methods and asks for a PhD to "develop" them → primary-source motivation. **[POLIMI PDF]**
- **Risk:** integration complexity; must show each block adds value over the strong baselines (Lovera H∞+CA, Delft INCA, Gahlawat L1-GP). Mitigated by the certification/multi-fidelity differentiator.
- **Maps to:** G1+G2+G3+G4+G5+G6 (the synthesis gap).

## D2 — L1-inspired adaptive augmentation of the host group's flatness/NDI controller with embedded degradation-aware CA  [STRONG — primary sub-direction]
- A focused slice of D1: keep the flatness/NDI nominal core; add an **L1-inspired** (not MRAC) adaptive loop whose decoupling/low-pass robustness property ([LITERATURE] Hovakimyan 2011) compensates fast residual uncertainty while an **embedded CA** (saturation/rate/degradation) distributes the compensated command. Differentiator vs Falconí (MRAC+ACA): the L1 *decoupling principle* gives a verifiable robustness margin without PE; vs Lovera H∞+CA: adds online data-informed adaptation with guaranteed transient.
- **Maps to:** G5, G1, G6.

## D3 — Physically-structured data-informed residual that PRESERVES the interpretable model + feeds a certifiable stability margin  [STRONG — primary sub-direction]
- Learn residual/aerodynamic uncertainty as a **structured, physically-interpretable** augmentation (hybrid first-principles + sparse/parametric/SINDy-style identification, NOT black-box GP), with UQ (GP or set-membership) feeding a verifiable stability margin. Differentiator vs Gahlawat L1-GP (black-box GP, CA-free) and vs B1 (SINDy effectiveness-only, no L1/flatness core). 
- **Maps to:** G2, G3.

## D4 — Multi-fidelity validation & certification-oriented assurance methodology for the integrated loop  [MEDIUM — backbone contribution]
- A systematic methodology linking analytical nonlinear models → data-enhanced representations → HIL/experiments, with quantified uncertainty transfer and a coherent certification-facing assurance argument (combining L1 robustness margin + μ-analysis on allocation + residual UQ). Closest: arXiv:2205.04590 (DRL verification only). 
- **Maps to:** G4, G3. Essential for PhD deliverable credibility.

## D5 — Interpretability / certification framework for the unified loop  [MEDIUM — theoretical contribution]
- Formalise *how* to certify the assembly: L1 low-pass robustness bound + structured-residual UQ bound + CA feasibility/μ-analysis → a single verifiable stability/performance statement. Builds on Jacklin (2009) certification-gap agenda and Dawson (2023) safe-learning survey. 
- **Maps to:** G3, G4.

## D6 — Trajectory–control co-design exploiting allocation nullspace under actuator degradation  [MEDIUM — supporting]
- Use over-actuation nullspace (within the embedded CA) to reduce actuator load, avoid downwash/efficiency loss, and manage degradation, co-designed with the trajectory generator — addressing "trajectory generation/control interaction" from the topic. Builds on Su et al. (D7), downwash-aware CA (B5), receding-horizon nullspace (B4). 
- **Maps to:** G1, G6, topic "trajectory–control interaction".

## D7 — Degradation-aware embedded CA co-designed with adaptation bandwidth  [MEDIUM — supporting]
- Health-weighted allocation + predictive reallocation integrated with L1/adaptive compensation so degradation is seen by BOTH allocation and adaptation; co-design of adaptation bandwidth vs allocation rate. Addresses G6 (sparsely treated) and the "actuator degradation and failures" topic item. 
- **Maps to:** G6, G1, G5.

## D8 — CBF / safe-set safety layer as a BASELINE/COMPETITOR (NOT a direction)  [WEAK / REJECT as primary]
- CBF-pseudo (Hafner 2026), CBF FEP (Autenrieb 2025), INDI+CBF (Traas 2026) are competing safety paradigms, not the topic's method set. Keep as **baseline to compare against**, not as the proposed direction. **[INFERENCE]**

## D9 — Pure data-driven / RL / black-box learning control  [REJECT]
- Off-topic: the CALL explicitly emphasises *interpretable model-based* methods (flatness/NDI/feedback-linearisation/robust/adaptive/L1). Black-box RL contradicts the interpretability/certifiability requirement. **[POLIMI PDF]**

---

## Summary of recommended structure
- **Primary direction = D1** (integrated assembly). 
- D2, D3 are the two indispensable technical pillars of D1. 
- D4, D5 provide the certification/multi-fidelity differentiator that survives the adversarial check. 
- D6, D7 are high-value supporting contributions (also strengthen experimental relevance). 
- D8, D9 are explicitly excluded/baseline-only.

See `08_ranked_directions.md` (prioritisation + decision), `09_research_architecture.md` (block diagram), `10_research_questions.md`, `11_validation_strategy.md`, `12_three_year_roadmap.md`.
