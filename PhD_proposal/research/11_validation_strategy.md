# 11 — VALIDATION STRATEGY

How each Research Question (`10`) and the architecture (`09`) is validated. Emphasis: the **multi-fidelity** + **certification-facing** dimension is the unique differentiator that survives the adversarial check ([LITERATURE] D4, C3; [INFERENCE]).

## A. Analytical / theoretical validation
- **Stability & robustness proofs:** Lyapunov/ISS for the flatness/NDI + L1-inspired + structured-residual loop; explicit treatment of CA as an in-the-loop constraint (not a separate block). L1 low-pass decoupling margin ([LITERATURE] Hovakimyan 2011).
- **Certification margin:** combine (i) L1 robustness bound, (ii) structured-residual UQ bound ρ (GP/set-membership), (iii) CA feasibility/μ-analysis → verifiable stability/performance statement (addresses RQ4). Build on Jacklin (2009) certification-gap agenda and Dawson (2023) safe-learning survey.
- **Comparison baselines (mandatory):** (a) host-group H∞+CA (Lovera B9/B10), (b) MRAC+adaptive-CA (Falconí, B7/B8), (c) CBF safety (Hafner 2026), (d) DI+CA FTC (B11), (e) Gahlawat L1-GP/CL1-GP, (f) B1 SINDy-CA. Show the integrated assembly's added value (RQ cross-cutting hypothesis).

## B. Data-informed / system-identification validation
- **Structured residual identification:** collect high-fidelity / flight data from the host group's over-actuated UAV; fit hybrid first-principles + sparse/parametric (SINDy-style) residual; verify interpretability + accuracy vs black-box GP (Kulathunga D1, B3). 
- **UQ:** GP or conformal/set-membership bounds on residual; demonstrate UQ feeds the certification margin (RQ2, RQ4).
- **Multi-fidelity model build:** analytical nonlinear model → data-enhanced (residual-augmented) model → validate mismatch reduction (RQ5).

## C. Simulation validation (high-fidelity, non-linear)
- **High-fidelity nonlinear 6-DoF simulation** of an over-actuated vehicle (thrust-vectoring UAV / tilt-rotor / octorotor class). Scenario set: nominal tracking; aggressive maneuvers; actuator saturation; rate limiting; partial loss-of-effectiveness; stuck/failed actuator; simultaneous faults.
- **Monte-Carlo** over aerodynamic/parametric uncertainty + fault cases; compare metrics (tracking error, control effort, degradation graceful-recovery time, certification-margin satisfaction rate) vs baselines.
- **Stress tests inspired by adversaries:** replicate B1's aggressive-maneuver benchmark and B6's fault-injection cases to position relative to SINDy-CA and MRAC+ACA.

## D. Experimental validation (host group platform) [feasibility depends on group assets]
- **Platform:** over-actuated thrust-vectoring / multirotor UAV available to the group (per [LITERATURE] S1–S4 experimental heritage). If a thrust-vectoring UAV is unavailable, an octorotor/tilt-rotor over-actuated testbed (cf. B6, D8, downwash-aware B5) is a valid proxy.
- **HIL (Hardware-In-the-Loop):** real-time implementation of the embedded CA + L1 + residual on the group's real-time target; fault injection at the allocator.
- **Flight tests:** nominal trajectory tracking; induced actuator degradation/failure (software fault injection or physical limiting); demonstrate graceful degradation and certifiable-margin monitoring. Compare against the group's existing flatness/NDI controller (S1–S4) and H∞+CA (B9/B10) as in-house baselines.
- **Multi-fidelity closure:** show that the certification margin predicted at analytical/data-enhanced fidelity is conserved (with quantified inflation) at experimental fidelity (RQ5).

## E. Certification / interpretability deliverables
- An **assurance case** (goal–argument–evidence) for the integrated loop, plus (where attainable) a formal verifiable stability statement. This is the defensible contribution vs all adversaries. **[RESEARCH GAP]**

See `12_three_year_roadmap.md` for sequencing of A–E across the PhD.
