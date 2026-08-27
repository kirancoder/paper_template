# 02 — TECHNICAL FIELD MAP

Scope: advanced control design for autonomous aerospace vehicles. Purpose: classify each branch as foundational / mature / active / fragmented, and identify combinations that are promising for a defensible PhD aligned with the Polimi topic. Sources tagged **[LITERATURE]** (external) or **[INFERENCE]** (synthesis). The Polimi wording is in `01_polimi_topic_analysis.md`.

## 1. Nonlinear flight dynamics
- Foundational. 6-DoF rigid-body + aerodynamic models; aerospace standard. **[LITERATURE]**
- Over-actuated / thrust-vectoring vehicles add actuator-orientation states (tilt servos) → richer but more coupled. **[LITERATURE]** (Invernizzi/Lovera/Zaccarian thrust-vectoring UAVs; tilt-rotor allocation work 2021–2024)

## 2. Nonlinear dynamic inversion (NDI)
- Foundational & mature as a design paradigm. Enns 1994 "Dynamic inversion: an evolving methodology" established it for flight control. **[LITERATURE]**
- Classical NDI embeds an onboard model; gives automatic gain-scheduling and modularity, but is model dependent. **[LITERATURE]**
- Incremental NDI (INDI): sensor-based variant using angular-acceleration measurements, far more robust to aerodynamic variation, repeatedly flight-tested (Sieberling 2010, Grondman 2018 passenger aircraft, TU Delft). **[LITERATURE]**
- INDI known weakness: reduced robust-stability margin to singular perturbations (transport delays, elastic modes); active TU Delft research (Pollack 2024 thesis; "Robust Stability and Performance Analysis…", JGCD). **[LITERATURE]**

## 3. Feedback linearisation (FL)
- Foundational, textbook. Closely related to NDI; exact linearisation via state feedback. **[LITERATURE]**
- Well established; main limitations: requires precise model, suffers under model uncertainty unless augmented (robust/adaptive). **[LITERATURE]**

## 4. Flatness-based control (differential flatness)
- Foundational (Fliess, Lévine, Martin, Rouchon 1990s); powerful for trajectory generation AND feedback linearising control. **[LITERATURE]**
- Aerospace applications: 6-DoF aircraft flatness + optimal trajectory (dynamic soaring), quadcopters (Nguyen 2016), rotorcraft aggressive maneuvers (McLain/Beard 2011 hardware). **[LITERATURE]**
- Polimi group's concrete strength: flatness/geometric control of thrust-vectoring (under/over-actuated) UAVs — Invernizzi/Lovera/Zaccarian, Automatica 2018; ACC 2018; CDC 2019; IEEE TCST 2021 experimental comparison on tilt-arm quadrotor. **[LITERATURE]**

## 5. Robust nonlinear control
- Mature toolbox: small-gain/iISS, robust synthesis, H∞, structured singular value (μ) for clearance. TU Delft applies μ-analysis to INDI robustness. **[LITERATURE]**
- Mature for LTI; for nonlinear flight control, robust margins often evaluated via linearisation + μ. **[LITERATURE]**

## 6. Adaptive control
- Mature (MRAC, Lyapunov-based). Long history in aerospace; gain-scheduled baselines effectively adaptive. **[LITERATURE]**
- Known gap: certification of adaptive flight control still unresolved (Jacklin 2009 NASA; see §25). **[LITERATURE]**

## 7. L1 adaptive control / L1-inspired architectures
- Established by Cao & Hovakimyan; key feature: a low-pass filter separates adaptation bandwidth from robustness, giving verifiable V&V-friendly structure. Flight-tested on NASA AirSTAR GTM (Gregory et al. 2010/2012) and Calspan Learjet (Ackerman 2021). **[LITERATURE]**
- Recent extension (Ackerman 2021 dissertation): nonlinear-reference L1 augmenting a geometric trajectory-tracking baseline on multirotors — directly bridges L1 + geometric/flatness + over-actuated UAV, the Polimi domain. **[LITERATURE]** → highly relevant.
- "L1-inspired" (topic wording) suggests architectures that keep the L1 decoupling-of-adaptation-from-robustness principle rather than literal MRAC. **[INFERENCE]**

## 8. Uncertainty representation
- Bounded/parametric (robust), stochastic (GP), or data-driven residual. Mature individually; combining physical interpretability + quantification is active. **[INFERENCE]**

## 9. Aerodynamic uncertainty
- Pervasive; addressed by robust control, INDI, GP residual learning, L1. Still a dominant source of model error. **[LITERATURE]**

## 10. Disturbance rejection
- Active; ESO, integral-ISS, disturbance observers, ILC with GP (Buelta 2021). **[LITERATURE]**

## 11. Actuator dynamics
- Often neglected or first-order lag. INDI/INCA embed actuator dynamics; D-INCA/AD-INCA (TU Delft) explicitly model first-order discrete actuator dynamics in the allocator and adapt online after failures. **[LITERATURE]**

## 12. Actuator saturation
- Standard in control allocation (QP/LP with box constraints). Well handled in CA; interaction with nonlinear inversion still studied. **[LITERATURE]**

## 13. Actuator rate limits
- Handled in CA (rate-constrained LP/QP, direct CA, differential allocation). Real-time flight-demonstrated. **[LITERATURE]**

## 14. Control allocation (CA)
- Mature survey: Johansen & Fossen 2013, Automatica. **[LITERATURE]**
- Methods: pseudoinverse, daisy-chaining, direct, LP/QP, nullspace-based (Su 2021), incremental nonlinear CA (INCA, TU Delft), nonlinear CA (SQP flight-tested 2023). **[LITERATURE]**
- KEY tension noted in literature: CA is "usually decoupled from high-level motion control design, but interactions should be studied when actuator dynamics significant or allocation influences zero-dynamics of inversion-based control (Buffington & Enns 1996/1998)." **[LITERATURE]** → this matches the topic's demand that allocation be PART of the architecture, not a downstream block.

## 15. Redundant / over-actuated control
- Active & practically important: NextGen transports, thrust-vectoring UAVs, tilt-rotors, ICE tailless aircraft. Nullspace used for secondary objectives (drag, power, efficiency, downwash avoidance). **[LITERATURE]**

## 16. Actuator degradation / failure
- Fault-tolerant CA (weight/effortor-model adaptation, reconfiguration), INCA adaptation (AD-INCA), L1 handling stability degradation/failures (AirSTAR). Mature as separate topic. **[LITERATURE]**

## 17. Fault-tolerant control
- Large mature field; CA-based reconfiguration is standard. **[LITERATURE]**

## 18. Data-informed modelling
- Active & fast-growing: GP, SINDy, NN, incremental learning. "Composite model = physics nominal + learned residual" is the dominant interpretable pattern. **[LITERATURE]** (Kulathunga 2024 SGP residual; GP-MPC with guarantees; model incremental learning 2025)

## 19. Residual-dynamics learning
- Central to topic. Pattern: learn g(z) (often input-affine B_d·g) on top of nominal. GP gives UQ. SGP for real-time. **[LITERATURE]**
- Mostly demonstrated in simulation; some hardware (Chowdhary GP adaptive flight tests; tilt-rotor ILC experiments). **[LITERATURE]**

## 20. Hybrid model-based + data-driven control
- Active. Composing first-principles + residual learning preserves interpretability. **[LITERATURE]** This is exactly the topic's "preserve physical structure and interpretability" requirement.

## 21. Uncertainty quantification
- GP naturally provides UQ; used for chance-constrained MPC. Less common in adaptive/CA loops. **[LITERATURE]**

## 22. Multi-fidelity modelling
- Topic wants "analytical nonlinear → data-enhanced." Literature: multi-fidelity verification of learning-based aviation (arXiv:2205.04590, mixed-fidelity Bayesian optimisation / RL). **[LITERATURE]** Still emerging for control-design validation.

## 23. Trajectory / control interaction
- Flatness naturally couples planning+control (inverse map). Topic wants explicit attention to actuator constraints/redundancy at this interface. **[INFERENCE]**

## 24. Interpretable learning
- Topic emphasis. Physics-based + residual is interpretable by construction. Neural certificates (Dawson 2023 survey) give formal safety but are less "physically interpretable." Trade-off exists. **[LITERATURE]**

## 25. Safety / certification-oriented control
- Open grand challenge. Jacklin (NASA 2009): certification gaps for adaptive flight control (no plan, no V&V tools for stability/convergence, metrics). L1 argued V&V-friendly. Learned certificates (Dawson 2023) and design-time/run-time assurance frameworks (arXiv:2205.04590) are recent but largely for DRL/decision-making, not for the model-based+residual flight-control loop the topic describes. **[LITERATURE]** → a genuine gap: certification-oriented treatment of the specific "flatness/NDI + integrated CA + data-informed residual" loop.

## 26. Simulation & experimental validation
- INDI, L1, flatness, CA all have flight/hardware demonstrations (NASA AirSTAR, Calspan, TU Delft passenger aircraft, Polimi tilt-arm quadrotor, tilt-rotor experiments 2021–2024). The Polimi group HAS experimental platforms. **[LITERATURE]**

---

## Combination analysis (where is the promising PhD space?)

| Combination | Maturity | Promise for PhD |
|---|---|---|
| NDI/FL + robust (no data) | Mature | Low novelty alone |
| Flatness + over-actuation (no uncertainty/data) | Mature in Polimi group | Low novelty alone (group already does it) |
| INDI + CA (INCA) | Active, TU Delft strong | Medium; risk of duplicating Delft |
| L1 + geometric/flatness baseline (multirotor) | Emerging (Ackerman 2021) | Medium-High; bridges topic methods |
| Data-informed residual + model-based control | Active, but mostly MPC/RL framing | High if kept model-based & interpretable |
| CA integrated INTO inversion loop + actuator constraints + degradation | Partial (Buffington&Enns, INCA) | **High** — matches topic's explicit "allocation as part of architecture" |
| Certifiable/interpretable data-informed residual on over-actuated aerospace vehicle | Fragmented; certification literature separate from flight-control loop | **High** — genuine gap |
| Multi-fidelity validation methodology for the above | Emerging | **High supporting contribution** |

**Preliminary conclusion [INFERENCE]:** The most defensible PhD space is NOT any single mature branch, but the *integration* layer the topic explicitly names: a physically-interpretable model-based core (flatness/NDI, consistent with the Polimi group's strength) + control allocation embedded in the architecture (not downstream) + robust/adaptive/L1-inspired uncertainty compensation that respects actuator saturation/rate/degradation + a *structured* data-informed residual-dynamics module that preserves interpretability and admits uncertainty quantification + a multi-fidelity validation/certification argument. This integration, and especially its certification/interpretability treatment for over-actuated aerospace vehicles, appears genuinely open.

See `05_research_gap_analysis.md` and `06_adversarial_gap_check.md` for challenge of this conclusion.
