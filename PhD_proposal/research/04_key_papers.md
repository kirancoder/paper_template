# 04 — KEY PAPERS (deep annotations)

Selected ~30 highest-value references. For the PRIORITY set I answer the 18 sub-questions (research Q, formulation, model, architecture, uncertainty, adaptation/robust, actuators, constraints, allocation, data-driven, stability, validation, baselines, result, limitations, unrealistic assumptions, extension, relevance). Remaining papers are in the compact registry at the end. All tagged **[LITERATURE]**.

---

## PRIORITY 1 — Invernizzi, Lovera (2018) "Trajectory tracking control of thrust vectoring UAVs." Automatica 95:180–186.
1. RQ: stabilize/steer underactuated vectored-thrust UAVs with position as primary objective.
2. Formulation: hybrid/nonlinear control via attitude planner (virtual control for position; attitude as secondary).
3. Model: 6-DoF rigid body + thrust-vectoring actuators; control model simplified (no actuator dynamics in design).
4. Architecture: inner–outer loop with attitude planner producing reference attitude + heading; position stabilizer.
5. Uncertainty: robust to bounded disturbances via iISS cascade tools; not data-driven.
6. Adaptation/robust: integral Input-to-State Stability cascade; quasi-time-optimal position stabilizer.
7. Actuators: thrust vectoring (servos tilt thrusters); actuator dynamics NOT in design model (tested with them in sim).
8. Constraints: actuation constraint (thrust along fixed axis); handles through planner.
9. Allocation: not explicitly a CA module; thrust-vectoring geometry handled in planner/force mapping.
10. Data-driven: none.
11. Stability: rigorous iISS cascade proof, almost-global/regional guarantees.
12. Validation: nonlinear simulation on hexacopter multibody model with actuator dynamics + aero.
13. Baselines: nested-saturations stabilizers.
14. Result: improved transient vs nested saturations; global position stabilization.
15. Limitations: no explicit CA optimisation, no degradation/fault, no data refinement, design model ignores actuator dynamics.
16. Unrealistic assumption: perfect attitude/angular info; linear/known actuator model.
17. Extension: integrate explicit CA + robustness to failures + data residual. **HIGHLY relevant to topic.**
18. Relevance: **CORE** — this is the host group's method; the PhD should build the uncertainty/data/CA-integration layer on/around it.

## PRIORITY 2 — Invernizzi, Lovera, Zaccarian (2018) ACC "Geometric trajectory tracking with attitude planner for vectored-thrust VTOL UAVs." DOI:10.23919/ACC.2018.8431708.
1–18 (similar to P1 but trajectory tracking + attitude planner with heading tracking; differential-inclusions stability; multibody hexacopter with actuator dynamics+aero in tests). Adds explicit attitude-planner concept that later ties to CA. **ESSENTIAL** for understanding the group's trajectory/control interaction view. Limitations same: no CA module, no data, no faults.

## PRIORITY 3 — Sieberling, Chu, Mulder (2010) "Robust Flight Control Using INDI and Angular Acceleration Prediction." JGCD 33(6). DOI:10.2514/1.49978.
INDI foundation: sensor-based (angular acceleration measurement) NDI; reduced model dependence; robust to aero variation. Architecture: INDI pitch/roll/yaw rate control. Uncertainty: regular perturbations handled; singular perturbations (delay) weakness. Actuators: first-order lag. Validation: sim + later flight. Limitation: robust-stability margin to singular perturbations; synchronisation effect. **ESSENTIAL** baseline for any INDI-based direction.

## PRIORITY 4 — Wang, van Kampen, Chu, Lu (2019) "Stability Analysis for Incremental Nonlinear Dynamic Inversion Control." JGCD 42(5). DOI:10.2514/1.G003791.
First rigorous stability proof for INDI (Lyapunov + ISS-like). Establishes conditions (time-scale separation, bounded angular accel error). Limitation: assumptions on angular-accel estimation quality; singular-perturbation fragility remains. **ESSENTIAL** theoretical baseline.

## PRIORITY 5 — Pollack (2024) TU Delft thesis "Advances in Dynamic Inversion-based Flight Control Law Design." DOI:10.4233/uuid:28617ba0-461d-48ef-8437-de2aa41034ea.
Multivariable H∞ analysis of inversion strategies; INDI robust stability/performance; multi-objective INCA for input-redundant plants. **ESSENTIAL** — most complete recent treatment of NDI/INDI + CA integration. Limitation: CA secondary objectives are optimisation-based, not deeply coupled to stability proof; certification not addressed. Directly competes with any NDI/INCA direction → must differentiate (e.g., certifiability / over-actuated UAV / data-informed layer).

## PRIORITY 6 — Johansen & Fossen (2013) "Control allocation—A survey." Automatica 49(5). DOI:10.1016/j.automatica.2013.01.035.
Definitive CA taxonomy: pseudo-inverse, LP/QP, nullspace, nonlinear CA. Explicitly states CA "usually decoupled from high-level control, but interactions should be studied when actuator dynamics significant or allocation influences zero-dynamics of inversion-based control." **ESSENTIAL** for the "allocation as part of architecture" claim. Limitation: survey, not a method; static effector model assumption.

## PRIORITY 7 — Hovakimyan et al. (2011) "L1 Adaptive Control for Safety-Critical Systems." IEEE CSM 31(5).
L1 architecture: reference model + adaptive law + low-pass filter that decouples adaptation bandwidth from robustness; guarantees (tracking, transient, robustness) with verifiable structure. **ESSENTIAL** for "L1-inspired." Limitation: originally LTI/linear-parameterisation; nonlinear-reference extension is recent (Ackerman 2021). Flight tests on AirSTAR + Learjet show graceful degradation under failures/stability loss. Directly supports certification-friendly adaptive control.

## PRIORITY 8 — Ackerman (2021) PhD dissertation "L1 Adaptive Control for Manned Flight and Multirotor Applications."
KEY BRIDGE: nonlinear-reference L1 augmenting a *geometric* (flatness-like) trajectory-tracking baseline on multirotor; compensates matched+unmatched uncertainty; LPV feedforward compensator for variational dynamics; incremental-stability-based proof. **ESSENTIAL** — proves L1 + geometric/flatness + over-actuated multirotor is a live, recent, citable direction. Limitation: no explicit control allocation module, no actuator-degradation CA, no data-informed residual (uses adaptation not data learning), certification only implicit. **This is the closest existing work to the proposed PhD — must differentiate clearly (see adversarial check 06).**

## PRIORITY 9 — Kulathunga, Hanheide, Klimchik (2024) "Residual dynamics learning… multi-rotor." Scientific Reports 14:1858. DOI:10.1038/s41598-024-51822-0.
Data-informed residual (SGP) between high-level planner and low-level controller; learns velocity residual; integrates into NMPC; reduces nominal model error ~2×. **ESSENTIAL** for "residual-dynamics identification." Limitation: simulation only; black-box-ish residual (not physically structured); no stability proof in closed loop; no actuator/CA coupling; no certification.

## PRIORITY 10 — Chowdhary et al. (2014) "Bayesian Nonparametric Adaptive Control Using Gaussian Processes." IEEE TNNLS 26(3). DOI:10.1109/TNNLS.2014.2319052 + Grande/Chowdhary/How (2014) J. Aerospace Info Systems DOI:10.2514/1.I010190 (experimental).
GP-based adaptive control with stability guarantees; flight-test validated. **ESSENTIAL** evidence that GP + adaptive + flight test is feasible. Limitation: mostly conventional aircraft, not over-actuated UAV, not integrated with CA, certification not addressed.

## PRIORITY 11 — Dawson, Gao, Fan (2023) "Safe Control With Learned Certificates…" IEEE T-RO. DOI:10.1109/TRO.2022.3232542.
Survey of neural Lyapunov/barrier/contraction for safe learning. **ESSENTIAL** for interpretability/certification stream. Limitation: neural certificates are data/optimisation artefacts, not physically interpretable in the topic's sense; gap remains for *physics-preserving* certifiable residual control.

## PRIORITY 12 — Jacklin (2009) NASA "Closing the Certification Gaps in Adaptive Flight Control."
Authoritative statement that adaptive control certification lacks plan, V&V tools, convergence metrics. **ESSENTIAL** for the certification gap. Supports the claim that certifiability of the integrated loop is open.

---

## COMPACT REGISTRY (remaining selected papers)

- **Invernizzi et al. (2019) CDC** iISS cascade stabilisation — extension of P1/P2; IMPORTANT.
- **Invernizzi et al. (2021) IEEE TCST** experimental comparison of fully-actuated UAV controllers (tilt-arm quadrotor) — IMPORTANT (host-group experiment).
- **"Robust Stability and Performance Analysis of IDI-Based FCS" JGCD (DOI 10.2514/1.G006576)** μ-analysis of INDI robust stability — IMPORTANT.
- **Grondman et al. (2018) AIAA 2018-0385** INDI flight test on passenger aircraft — IMPORTANT (real flight).
- **Pollack & van Kampen (2023) AIAA 2023-1249** multi-objective INCA (drag/power) — IMPORTANT.
- **Adaptive D-INCA / AD-INCA (TU Delft)** actuator-dynamics + failure adaptation in allocator — IMPORTANT.
- **Gregory et al. (2010) AIAA 2010-8015** L1 AirSTAR flight test — ESSENTIAL (L1 experiment).
- **Buelta et al. (2021) IEEE TAES** GP iterative learning control for aircraft trajectory tracking — IMPORTANT.
- **Maiworm et al. (Int. J. Robust Nonlinear Control, DOI 10.1002/rnc.5361)** online GP-MPC with ISS guarantees — IMPORTANT.
- **"Model incremental learning of flight dynamics enhanced by sample management" (2025)** GP + baseline + learning-guidance, convergence proof — IMPORTANT (pending verification).
- **Su et al. (2021) IEEE RA-L** nullspace-based CA of over-actuated UAV — IMPORTANT.
- **"Allocation for Omnidirectional Aerial Robots…" arXiv:2412.16107** differential allocation + actuator/power dynamics, experiment — IMPORTANT.
- **"Fast Real-Time CA… Over-Actuated Quadrotor Tilt-Rotor" J Intell Robot Syst 2021, DOI 10.1007/s10846-021-01411-4** — IMPORTANT.
- **"Real-Time Nonlinear CA… Highly Nonlinear Effectors" J Intell Robot Syst 2023, DOI 10.1007/s10846-023-01865-8** SQP CA flight-tested — IMPORTANT.
- **Brunke et al. (2022) Annual Reviews in Control, DOI 10.1146/annurev-control-042920-020211** safe learning review — SUPPORTING.
- **"Verification Framework for Certifying Learning-Based Aviation Systems" arXiv:2205.04590** multi-fidelity verification — IMPORTANT.
- **Oppenheimer, Doman, Bolender (2006) MED, DOI 10.1109/MED.2006.328750** CA for over-actuated systems — IMPORTANT.
- **Bodson (2002) JGCD** evaluation of CA optimisation methods — SUPPORTING.
- **"Survey of Optimal CA for Aerial Vehicle Control" Drones 2023, DOI 10.3390/drones12070282** — IMPORTANT (norm comparison).
- **McLain/Beard (2011) IROS** flatness rotorcraft hardware — SUPPORTING.
- **Nguyen et al. (2016) arXiv:1609.08428** flatness quadcopter — SUPPORTING.

See `bibliography.md` for consolidated entries and `sources_to_verify.md` for unverified DOIs.
