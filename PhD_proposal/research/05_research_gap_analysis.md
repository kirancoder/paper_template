# 05 — RESEARCH GAP ANALYSIS

Central question (intersection): nonlinear model-based control + uncertainty + robust/adaptive compensation + actuator constraints + control allocation + data-informed model refinement + interpretability/validation, for autonomous aerospace vehicles. All gaps tagged **[RESEARCH GAP]** (proposed, requires evidence) and justified by **[LITERATURE]**.

Recall the host group's established strength (Invernizzi/Lovera/Zaccarian): flatness/geometric control of over-actuated thrust-vectoring UAVs with experimental validation — but WITHOUT formal robust/adaptive/L1 uncertainty compensation, WITHOUT data-informed residual refinement, WITHOUT explicit certifiability, and WITHOUT degradation-aware allocation. **[LITERATURE]**

---

## G1 — Control allocation embedded in the model-based control law (not downstream) WITH guaranteed robustness under saturation, rate, and degradation
- **Statement [RESEARCH GAP]:** A unified, interpretable architecture in which CA is an integral block of a flatness/NDI controller for over-actuated aerospace vehicles, with provable robustness margins under actuator saturation, rate limits, and degradation/failure — is not established for the thrust-vectoring/over-actuated UAV class the host group works on.
- **Supporting [LITERATURE]:** Johansen&Fossen (2013) explicitly note CA is "usually decoupled from high-level motion control design, but interactions should be studied when actuator dynamics significant or allocation influences zero-dynamics of inversion-based control" (Buffington&Enns 1996/98). Topic wording demands CA "as part of the control architecture, rather than a separate post-processing block." **[POLIMI PDF]**
- **Contradicting [LITERATURE]:** TU Delft INCA / D-INCA / AD-INCA DO integrate CA with actuator dynamics and failure adaptation (Pollack 2024; adaptive INCA ICE aircraft). So the *concept* of integrated CA exists.
- **Assessment:** NOT a fully open gap in general, but OPEN for the specific combination: flatness/geometric *interpretable* core (not INDI) + over-actuated thrust-vectoring UAV + degradation-aware CA + embedded-in-stability-proof. Differentiation from Delft is feasible. **Verdict: PARTIAL / sharpened gap.**

## G2 — Physically-structured data-informed residual-dynamics refinement that PRESERVES interpretability AND admits a closed-loop stability / certification argument
- **Statement [RESEARCH GAP]:** A method that learns residual/aerodynamic uncertainty as a *structured*, physically-interpretable augmentation of the nominal model-based controller for over-actuated aerospace vehicles, with (i) closed-loop stability guarantees and (ii) a certification/interpretability argument, is missing.
- **Supporting [LITERATURE]:** Composite "nominal + B_d·g(z)" pattern is common (GP-MPC review arXiv:2502.02310; Kulathunga 2024 SGP residual; model incremental learning 2025). But: Kulathunga is simulation-only with no closed-loop stability proof and black-box-ish residual; GP-MPC (Maiworm, DOI 10.1002/rnc.5361) gives ISS but is MPC-framed, not the interpretable model-based flight loop the topic describes; Chowdhary GP adaptive has guarantees+flight test but is not over-actuated-UAV/CA-integrated and not certification-facing.
- **Contradicting [LITERATURE]:** Chowdhary (2014) + Grande/Chowdhary/How (2014) show GP adaptive control with stability + flight test; Maiworm shows online GP-MPC ISS. So "data + stability" exists in forms.
- **Assessment:** The gap is the *intersection*: structured/interpretable residual + closed-loop stability + certification-facing + over-actuated vehicle + integrated with CA. This intersection is NOT covered. **Verdict: GENUINE, strong PhD candidate.**

## G3 — Uncertainty quantification from data-informed refinement feeding an interpretability/certification argument
- **Statement [RESEARCH GAP]:** Using GP-style UQ of the learned residual to produce interpretable, certification-oriented assurance (e.g., bounded residual → verifiable stability margin) for the flight-control loop is not established.
- **Supporting [LITERATURE]:** GP gives natural UQ; chance-constrained MPC uses it; but tying UQ to *certification* of an adaptive/CA flight loop is open. Jacklin (2009) documents certification gaps for adaptive control.
- **Contradicting:** L1's low-pass structure already gives a verifiable robustness argument (Hovakimyan 2011) — but without data-informed residual.
- **Assessment:** GENUINE as a *supporting* contribution; strengthens G2.

## G4 — Multi-fidelity validation methodology linking analytical nonlinear → data-enhanced → experiment
- **Statement [RESEARCH GAP]:** A systematic multi-fidelity validation/certification methodology for the integrated (model-based + residual + CA) flight-control loop, with quantified uncertainty transfer across fidelity levels, is missing.
- **Supporting [LITERATURE]:** Topic wants "different levels of model fidelity, from analytical nonlinear models to data-enhanced representations." **[POLIMI PDF]** Multi-fidelity verification of learning-based aviation exists (arXiv:2205.04590) but targets DRL/decision-making, not the model-based+residual loop.
- **Contradicting:** Standard V&V, HIL, μ-analysis exist for non-learning loops.
- **Assessment:** GENUINE supporting contribution; high value for a PhD deliverable and for the host group's experimental pipeline.

## G5 — L1-inspired (or robust/adaptive) uncertainty compensation respecting actuator constraints WITHIN an integrated allocation loop, for over-actuated vehicles
- **Statement [RESEARCH GAP]:** An L1-inspired augmentation of a flatness/geometric over-actuated controller that (a) keeps the adaptation/robustness decoupling principle, (b) operates with an embedded CA respecting saturation/rate/degradation, and (c) preserves interpretability, is not established for this vehicle class.
- **Supporting [LITERATURE]:** Ackerman (2021) bridges L1 + geometric baseline + multirotor (KEY), but: no explicit CA module, no degradation-aware allocation, fixed-wing/multirotor not over-actuated thrust-vectoring with allocation. L1 AirSTAR shows degradation handling but separate CAS, not embedded CA.
- **Contradicting:** L1 + geometric exists (Ackerman); INDI+CA exists (Delft).
- **Assessment:** The narrowed gap (L1-inspired + embedded CA + over-actuated + degradation) is OPEN. **Verdict: GENUINE, strong.**

## G6 — Interaction between adaptation bandwidth and control allocation under realistic actuator constraints
- **Statement [RESEARCH GAP]:** How adaptation bandwidth (L1/adaptive) interacts with CA when actuators saturate/rate-limit/degrade — and how to co-design them — is sparsely treated.
- **Supporting:** INDI literature notes synchronisation effect (robust stability vs singular perturbations); CA literature notes interactions under actuator dynamics. But co-design of adaptation + allocation bandwidth is open.
- **Assessment:** GENUINE but narrower; best as a sub-contribution of G1/G5.

---

## Synthesis of the PRIMARY gap [RESEARCH GAP] (proposed)
For over-actuated autonomous aerospace vehicles, there is no unified, interpretable, model-based control architecture that simultaneously:
(i) uses a flatness/NDI nominal core (consistent with the host group's strength and the topic's explicit methods),
(ii) embeds control allocation within the control law (not as a downstream block) respecting saturation, rate limits, and degradation/failure,
(iii) augments uncertainty compensation via an L1-inspired/adaptive mechanism and a physically-structured, data-informed residual-dynamics module that preserves the physical model, and
(iv) provides an interpretability/certification argument supported by a multi-fidelity (analytical → data-enhanced → experimental) validation methodology.

This is coherent (not over-combined): the nominal interpretable core is preserved; data refines it; L1/robust handles fast residual uncertainty; CA is embedded for actuators. Each block maps to explicit topic wording. **[INFERENCE]**

## Which gaps can support a PhD?
- G2 (+G3): YES — theoretically meaningful, multiple papers, experimentally testable on group's UAV.
- G5 (+G1, G6): YES — bridges topic's L1-inspired + allocation + over-actuation.
- G4: YES as the validation backbone / strong supplementary contribution.
- G1 alone: NO (partly matured by Delft) — only as part of the integrated architecture.
- "Pure MPC/data-driven": NO — off-topic (topic emphasises model-based interpretable methods).

See `06_adversarial_gap_check.md` for the mandatory attempt to DISPROVE G2/G5.

---

## REVISION NOTE (after adversarial check — do NOT overwrite above; supersedes the PRE-adversarial conclusions)

The adversarial search (`06`) surfaced **Gahlawat et al. 2020 "L1-GP"** and **Gahlawat et al. 2021 "Contraction L1-Adaptive Control using Gaussian Processes"**, which already combine L1 adaptive control with Gaussian Process learning AND provide stability/safety certificates. This **partially disproves the WIDE form of G2/G5**. Therefore the prior "GENUINE, strong" verdicts on G2/G5 must be NARROWED, not abandoned:

- **G2** remains genuine ONLY in the narrowed form: **physically-STRUCTURED residual + over-actuated EMBEDDED CA + degradation + multi-fidelity certification**. Generic "L1+GP+stability" is closed (Gahlawat).
- **G5** remains genuine and strong: Gahlawat's L1-GP/CL1-GP contain **no control allocation, no over-actuation, no degradation-aware allocation** — the intersection "L1-inspired + embedded CA + over-actuated + degradation" is still open.
- **G1** (safety sub-piece) is further challenged by **Hafner et al. 2026 CBF-on-pseudo-control-before-CA** (overactuated + safety + certifiability argument) but via CBF, not the topic's flatness/NDI/L1/allocation method set.

**Updated PRIMARY gap (defensible, not disproved):** a unified, interpretable, model-based (flatness/NDI) control architecture for OVER-ACTUATED autonomous aerospace vehicles that (i) embeds CA with saturation/rate/degradation, (ii) uses L1-inspired/adaptive + **physically-structured** data-informed residual, and (iii) is backed by interpretability/certification argument + multi-fidelity validation. Differentiators vs Gahlawat (CA-free, simulation-only), vs Delft INCA (not certifiability-facing), vs CBF-pseudo (different method set). **[RESEARCH GAP]**

### RE-REVISION after DEEP adversarial pass 2 (do NOT overwrite above)
Pass-2 literature (see `bibliography.md` B1–B12, `06` §E) shows the narrowed gap is under even stronger pressure:
- B1 (SINDy interpretable effectiveness + nonlinear CA + failure reconfiguration, 2026) challenges "structured/interpretable + CA + failure."
- B6 (Falconí TUM: MRAC + adaptive CA + flight-tested FTC) and B7/B8 (adaptive-CA stability proofs) challenge "adaptive + CA + degradation + flight test."
- B11 (DI-based law + optimization CA FTC) and B9/B10 (Lovera group: structured H∞ + online CA + μ-analysis) show the host group / close peers already do robust/adaptive + CA + FTC — but via H∞/μ-analysis / MRAC / SMC / SINDy, **NOT via the flatness/NDI + L1-inspired + model-based interpretable core the CALL specifies**, and **none provides a certification case or multi-fidelity validation methodology**.
**Final defensible framing:** The gap is the *integrated, certification-facing assembly* of the CALL's exact method set (flatness/NDI + L1-inspired + embedded CA + physically-structured data-informed residual + interpretability/certifiability + multi-fidelity validation) for the host group's over-actuated thrust-vectoring UAV. No single paper delivers this assembly; the CALL itself motivates it. **[RESEARCH GAP]**
