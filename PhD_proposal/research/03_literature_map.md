# 03 — LITERATURE MAP

Organised into research streams. Each entry: authors (year), title, venue, DOI/URL if known, method, relevance. Verification status noted. Source tag **[LITERATURE]** unless marked otherwise. See `bibliography.md` for the consolidated verified list.

## STREAM A — Nonlinear model-based flight control (NDI / FL / flatness)
- Enns, D. (1994). "Dynamic inversion: an evolving methodology for flight control design." *Int. J. Control*, 59(1). DOI:10.1080/00207179408923070. Foundational NDI. **VERIFIED.**
- McLain, Beard, Leishman, Ferrin (2011). "Differential Flatness Based Control of a Rotorcraft For Aggressive Maneuvers." IROS. Hardware hexacopter, flatness feedforward + LQR. **PARTIAL (DOI NOT VERIFIED).**
- Nguyen et al. (2016). "Flatness-based nonlinear control strategies for trajectory tracking of quadcopter systems." arXiv:1609.08428. Flatness + FL. **VERIFIED (arXiv).**
- Aircraft 6-DoF flatness / dynamic soaring: Cambridge Aeronautical Journal (flatness of 6DoF aircraft). **PARTIAL.**
- Invernizzi, Lovera (2018). "Trajectory tracking control of thrust vectoring UAVs." *Automatica*, 95:180–186. **DOI NOT YET VERIFIED — flag in sources_to_verify.md.**
- Invernizzi, Lovera, Zaccarian (2018). "Geometric trajectory tracking with attitude planner for vectored-thrust VTOL UAVs." ACC 2018. DOI:10.23919/ACC.2018.8431708. **VERIFIED.**
- Invernizzi, Lovera, Zaccarian (2019). "Integral ISS-based cascade stabilization for vectored-thrust UAVs." CDC 2019. **PARTIAL.**
- Invernizzi, Giurato, Gattazzo, Lovera (2021). "Comparison of Control Methods for Trajectory Tracking in Fully Actuated UAVs." *IEEE TCST*. Experimental tilt-arm quadrotor. **DOI NOT YET VERIFIED — flag.**

## STREAM B — Robust / adaptive nonlinear control
- Buffington, J.M., Enns, D.F. (1996/1998). Control allocation influences zero-dynamics of inversion-based control. **KEY: motivates integrated CA.** **PARTIAL (citations seen, DOIs not verified).**
- Sieberling, Chu, Mulder (2010). "Robust Flight Control Using INDI and Angular Acceleration Prediction." *JGCD*, 33(6):1732–1742. DOI:10.2514/1.49978. **VERIFIED.**
- Wang, van Kampen, Chu, Lu (2019). "Stability Analysis for Incremental Nonlinear Dynamic Inversion Control." *JGCD*, 42(5):1116–1129. DOI:10.2514/1.G003791. **VERIFIED.**
- "Robust Stability and Performance Analysis of Incremental Dynamic-Inversion-Based Flight Control Laws." *JGCD* (recent). DOI:10.2514/1.G006576 (from search). **PARTIAL — verify.**
- "Advancements in incremental nonlinear dynamic inversion and its components: A survey on INDI – Part II." *Chinese J. of Aeronautics*, 2025. DOI:10.1016/j.cja.2025.103591. **VERIFIED.**
- Pollack, T.S.C. (2024). *Advances in Dynamic Inversion-based Flight Control Law Design* (PhD thesis, TU Delft). DOI:10.4233/uuid:28617ba0-461d-48ef-8437-de2aa41034ea. **VERIFIED.**

## STREAM C — L1 adaptive / L1-inspired
- Hovakimyan, Cao, Kharisov, Xargay, Gregory (2011). "L1 Adaptive Control for Safety-Critical Systems." *IEEE Control Systems Magazine*, 31(5):54–104. **DOI NOT YET VERIFIED — flag (likely 10.1109/MCS.2011.942030).**
- Gregory, Xargay, Cao, Hovakimyan (2010). "Flight Test of an L1 Adaptive Controller on the NASA AirSTAR Flight Test Vehicle." AIAA 2010-8015. DOI:10.2514/6.2010-8015. **VERIFIED.**
- Ackerman, K.A. (2021). *L1 Adaptive Control for Manned Flight and Multirotor Applications* (dissertation, UIUC). L1 augmenting geometric baseline on multirotor; nonlinear-reference L1 with matched+unmatched uncertainty, LPV feedforward. **KEY BRIDGE.** **PARTIAL (dissertation PDF seen).**

## STREAM D — Control allocation & over-actuated systems
- Johansen, T.A., Fossen, T.I. (2013). "Control allocation—A survey." *Automatica*, 49(5):1087–1103. DOI:10.1016/j.automatica.2013.01.035. **VERIFIED — DEFINITIVE.**
- Oppenheimer, Doman, Bolender (2006). "Control Allocation for Over-actuated Systems." MED 2006. DOI:10.1109/MED.2006.328750. **VERIFIED.**
- Härkegård, O. "Dynamic control allocation using constrained quadratic programming." *JGCD*. **PARTIAL.**
- Bodson, M. (2002). "Evaluation of Optimization Methods for Control Allocation." *JGCD*. **PARTIAL.**
- Su, Yu, Gerber, Ruan, Tsao (2021). "Nullspace-Based Control Allocation of Overactuated UAV Platforms." *IEEE RA-L*, 6:8094–8101. **PARTIAL (DOI seen 10.1109/LRA.2021... not captured).**
- Pollack, van Kampen (2023). "Multi-objective Design and Performance Analysis of Incremental Control Allocation-based Flight Control Laws." AIAA 2023-1249. DOI:10.2514/6.2023-1249. **VERIFIED.**
- TU Delft INCA / D-INCA / AD-INCA (Matamoros & de Visser 2018; adaptive INCA ICE aircraft; "Adaptive dynamic incremental nonlinear control allocation" thesis). **PARTIAL.**
- "Allocation for Omnidirectional Aerial Robots: Incorporating Power Dynamics." arXiv:2412.16107. Experimental differential allocation + actuator dynamics. **VERIFIED (arXiv).**
- "Fast Real-Time Control Allocation Applied to Over-Actuated Quadrotor Tilt-Rotor." *J. Intell. Robot. Syst.*, 2021. DOI:10.1007/s10846-021-01411-4. **VERIFIED.**
- "Real-Time Nonlinear Control Allocation Framework for Vehicles with Highly Nonlinear Effectors." *J. Intell. Robot. Syst.*, 2023. DOI:10.1007/s10846-023-01865-8. SQP, flight-tested, avoids linearisation oscillations. **VERIFIED.**

## STREAM E — Fault / degradation-aware control
- L1 AirSTAR: graceful degradation under 75–125% stability loss + failures. **VERIFIED (NASA).**
- AD-INCA: online actuator-dynamics adaptation after failures. **PARTIAL.**
- Downwash-aware nullspace CA (over-actuated UAV, simulation+experiment). **PARTIAL.**

## STREAM F — Data-informed model refinement / residual dynamics
- Kulathunga, Hanheide, Klimchik (2024). "Residual dynamics learning for trajectory tracking for multi-rotor aerial vehicles." *Scientific Reports*, 14:1858. DOI:10.1038/s41598-024-51822-0. SGP residual between planner and low-level. **VERIFIED.**
- "Model incremental learning of flight dynamics enhanced by sample management." 2025 (ScienceDirect; journal unclear — likely Aerospace Science & Technology / Chinese J. Aeronautics). GP + baseline + learning-guidance, convergence proof. **PARTIAL — verify journal/DOI.**
- Buelta et al. (2021). "A Gaussian process iterative learning control for aircraft trajectory tracking." *IEEE TAES*. DOI:10.1109/TAES.2021.3098133. **VERIFIED.**
- "Online learning-based MPC with GP models and stability guarantees." *Int. J. Robust Nonlinear Control*. DOI:10.1002/rnc.5361. ISS + constraint satisfaction. **VERIFIED.**

## STREAM G — Hybrid model-based + data-driven control
- Composite model g_nom + B_d·g(z) pattern (GP-MPC review, Scampicchio et al. 2025 arXiv:2502.02310). **VERIFIED (arXiv).**
- Chowdhary et al. (2014). "Bayesian Nonparametric Adaptive Control Using Gaussian Processes." *IEEE TNNLS*, 26(3):537–550. DOI:10.1109/TNNLS.2014.2319052. **VERIFIED.**
- Grande, Chowdhary, How (2014). "Experimental Validation of Bayesian Nonparametric Adaptive Control Using Gaussian Processes." *J. Aerospace Information Systems*. DOI:10.2514/1.I010190. **VERIFIED.**

## STREAM H — Uncertainty-aware learning / control
- GP-UQ → chance-constrained MPC; tube-MPC with GP (Soloperto, Bastani). **PARTIAL.**
- Maiworm et al. ISS guarantees for online GP-MPC. **VERIFIED.**

## STREAM I — Safety / interpretability / certification
- Jacklin, S. (2009). "Closing the Certification Gaps in Adaptive Flight Control." NASA. Certification gaps for adaptive control. **VERIFIED (NASA NTRS).**
- Dawson, Gao, Fan (2023). "Safe Control With Learned Certificates…" *IEEE T-RO*. DOI:10.1109/TRO.2022.3232542. Neural Lyapunov/barrier survey. **VERIFIED.**
- Brunke et al. (2022). "Safe Learning in Robotics…" *Annual Reviews in Control*. DOI:10.1146/annurev-control-042920-020211. **VERIFIED.**
- Mandal et al. (2024). "Safe and Reliable Training of Learning-Based Aerospace Controllers." IEEE. Design-for-verification + neural Lyapunov barrier. **PARTIAL.**
- "A Verification Framework for Certifying Learning-Based Safety-Critical Aviation Systems." arXiv:2205.04590. Mixed/multi-fidelity verification. **VERIFIED (arXiv).**
- Richards, Berkenkamp, Krause (2018). "The Lyapunov neural network." CoRL. **PARTIAL.**

## STREAM J — Integrated trajectory–control architecture
- Flatness couples planning/control by construction; topic wants actuator constraints/redundancy at this interface. **[INFERENCE]**
- Geometric/flatness + attitude planner + CA for thrust-vectoring UAV (Invernizzi group). **VERIFIED (stream A).**

---

## Cross-stream assessments (answering the "what is missing" question)

1. **Well established:** NDI/FL/flatness theory; CA methods (LP/QP/nullspace/INCA); L1 flight tests; GP residual learning in simulation; certification *problem statement* for adaptive control.
2. **Still difficult:** (a) CA truly embedded in the inversion/control law with guaranteed robustness under saturation+rate+degradation; (b) data-informed residual that preserves interpretability AND admits a certification/stability argument in the *closed loop*; (c) multi-fidelity validation linking analytical→data-enhanced→experiment with quantified uncertainty; (d) bridging the certification literature (mostly DRL/decision-making) to the model-based+residual flight-control loop.
3. **Dominant assumptions:** static (or simple first-order) effector models in CA; perfect attitude/angular-accel sensing for INDI; bounded/known uncertainty for robust; offline-trained or i.i.d. GP; separable CA.
4. **Common validation weakness:** most data-informed flight work is simulation-only; few close the loop with stability proof + real experiment + certification argument simultaneously.
5. **Methods that fail under realistic aerospace constraints:** naive MRAC (conservatism/robustness gaps), pure MPC (compute + certifiability), black-box NN (interpretability/certification), static CA ignoring actuator dynamics under aggressive maneuvers (oscillations, flight-tested 2023).

These weaknesses feed `05_research_gap_analysis.md`.
