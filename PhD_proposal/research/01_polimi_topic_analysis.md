# 01 — POLIMI TOPIC ANALYSIS (from supplied PDFs)

All substantive claims below are tagged **[POLIMI PDF]** (from `SCHEDA_5736_IAER...pdf`, the research topic description form). The other PDF (`5736_5512_APPLICATION...pdf`) is purely administrative and is used only for format/deadline facts.

## A. Exact research-topic title **[POLIMI PDF]**
"ADVANCED CONTROL DESIGN METHODS FOR AUTONOMOUS AEROSPACE VEHICLES"
- PhD programme: INGEGNERIA AEROSPAZIALE / AEROSPACE ENGINEERING — 42nd cycle.
- Thematic Research Field exactly as above. **[POLIMI PDF]**

## B. Research motivation **[POLIMI PDF]**
- Autonomous aerospace vehicles must operate in "complex, uncertain, and dynamically changing environments" while keeping performance, safety, reliability. **[POLIMI PDF]**
- Difficult because dynamics are affected by: nonlinearities, aerodynamic uncertainties, actuator limitations, configuration changes, environmental disturbances, imperfect modelling. **[POLIMI PDF]**
- Classical flight control remains essential but must be "extended and integrated with advanced nonlinear, robust, adaptive, and data-informed methods." **[POLIMI PDF]**

## C. Research objectives **[POLIMI PDF]**
- Develop advanced flight control methodologies for autonomous aerospace systems. **[POLIMI PDF]**
- Emphasis: nonlinear control, robustness to modelling uncertainty, adaptive compensation mechanisms, systematic integration of uncertain/data-enhanced models within control architectures. **[POLIMI PDF]**
- Exploit model-based approaches (NDI, feedback linearisation, flatness-based control, adaptive, robust, control allocation) together with methods that exploit experimental/operational data to improve modelling, estimation, and compensation of uncertain aerodynamic/dynamic effects. **[POLIMI PDF]**
- Central goal: control architectures that exploit available physical models while systematically accounting for uncertainty, limited model fidelity, and available data. **[POLIMI PDF]**
- Preserve interpretability and certifiability while improving performance/adaptability vs purely fixed-model designs. **[POLIMI PDF]**
- Consider interaction between high-level trajectory generation and low-level control, with attention to actuator constraints, redundancy, allocation of control effort. **[POLIMI PDF]**
- Expected outcome: a coherent methodological framework for design, analysis, and validation of advanced flight controllers, supporting different levels of model fidelity (analytical nonlinear → data-enhanced), applicable to simulation and experimental platforms available in the research group. **[POLIMI PDF]**

## D. Methods explicitly mentioned **[POLIMI PDF]**
- Nonlinear dynamic inversion (NDI)
- Feedback linearisation
- Flatness-based control ("flatness-based design")
- Adaptive control
- Robust control
- Control allocation

## E. Techniques explicitly mentioned **[POLIMI PDF]**
- Robust and adaptive control "including L1-inspired architectures"
- Uncertainty compensation; robustness margins; adaptation bandwidth; implementation constraints
- Control allocation treated as PART of the control architecture, not a separate post-processing block
- Data-informed modelling and compensation (uncertainty-aware, complementary role)
- Identification of residual dynamics; refinement of uncertain aerodynamic/dynamic terms; assessment of model uncertainty
- Nonlinear simulation, comparative analysis, experimental testing
- Multi-fidelity / different levels of model fidelity

## F. Uncertainty sources (explicit) **[POLIMI PDF]**
"Uncertainty may arise from aerodynamic effects, parameter variations, actuator dynamics, disturbances, configuration changes, operational conditions, or modelling assumptions." **[POLIMI PDF]**

## G. Actuator issues (explicit) **[POLIMI PDF]**
- Actuator dynamics and limitations
- Saturation, rate limits, efficiency criteria
- Degradation or failures
- Redundancy / over-actuation: "redundant or over-actuated aerospace platforms"
- Allocation of control effort must respect above constraints and be reflected in design and validation. **[POLIMI PDF]**

## H. Control-allocation issues (explicit) **[POLIMI PDF]**
- Allocation is to be considered as part of the control architecture, rather than a separate post-processing block, so actuator constraints and vehicle capabilities are reflected in design and validation. **[POLIMI PDF]**
- For redundant/over-actuated platforms, controller must translate desired forces/moments into actuator commands while respecting saturation, rate limits, efficiency, degradation/failures. **[POLIMI PDF]**

## I. Data-informed modelling requirements (explicit) **[POLIMI PDF]**
- "Data-informed modelling and compensation methods may be used in a complementary and uncertainty-aware role." **[POLIMI PDF]**
- Experimental/simulation/operational data may support: identification of residual dynamics, refinement of uncertain aerodynamic/dynamic terms, assessment of model uncertainty. **[POLIMI PDF]**
- Emphasis: control schemes that preserve the physical structure and interpretability of model-based designs, while exploiting available information to improve prediction, compensation, robustness assessment. **[POLIMI PDF]**

## J. Interpretability requirements (explicit) **[POLIMI PDF]**
- "preserve the physical structure and interpretability of model-based designs" **[POLIMI PDF]**
- "define control architectures that can exploit available physical models while systematically accounting for uncertainty... This includes the development of methods able to preserve interpretability and certifiability, which are crucial in aerospace applications." **[POLIMI PDF]**
- Educational objective: distinguish when nominal model-based is sufficient, when robust/adaptive required, when data/uncertainty info provides measurable benefits. **[POLIMI PDF]**

## K. Safety / certification relevance (explicit) **[POLIMI PDF]**
- Certifiability "crucial in aerospace applications." **[POLIMI PDF]**
- "Particular emphasis will be placed on interpretability, validation, safety, and the relation between performance improvement and certification-oriented constraints." **[POLIMI PDF]**
- Safety-critical aerospace applications awareness is an educational objective. **[POLIMI PDF]**

## L. Validation expectations (explicit) **[POLIMI PDF]**
- Methods evaluated through nonlinear simulation, comparative analysis, and, where appropriate, experimental testing on available aerospace platforms. **[POLIMI PDF]**
- Favour modular architectures accommodating different vehicle configurations and levels of model fidelity. **[POLIMI PDF]**

## M. Experimental expectations (explicit) **[POLIMI PDF]**
- "experimental testing on available aerospace platforms" (qualified by "where appropriate"). **[POLIMI PDF]**
- "applicable to both simulation environments and experimental platforms available in the research group." **[POLIMI PDF]**

## N. Model-fidelity considerations (explicit) **[POLIMI PDF]**
- Framework should support "different levels of model fidelity, from analytical nonlinear models to data-enhanced representations." **[POLIMI PDF]**
- Multi-fidelity is implied by "different levels of model fidelity" and "limited model fidelity." **[POLIMI PDF]**

## O. Trajectory-generation / control interaction (explicit) **[POLIMI PDF]**
- "The research will also consider the interaction between high-level trajectory generation and low-level control, with special attention to actuator constraints, redundancy, and allocation of control effort." **[POLIMI PDF]**

## P. Expected methodological framework (explicit) **[POLIMI PDF]**
- An "integrated methodological framework for the design, analysis, and validation of advanced flight control systems." **[POLIMI PDF]**
- Starting point: nonlinear dynamics of the vehicle, using NDI/feedback linearisation/flatness to obtain interpretable control architectures; on this basis introduce robustness, adaptation, actuator management, uncertainty compensation. **[POLIMI PDF]**
- Modular architectures accommodating different vehicle configurations and fidelity levels. **[POLIMI PDF]**

## Q. Relevant educational / research competencies (explicit) **[POLIMI PDF]**
- Flight dynamics, nonlinear systems, advanced control: feedback linearisation, NDI, flatness-based control, robust/adaptive control for uncertain systems, L1-inspired architectures. **[POLIMI PDF]**
- Control allocation for redundant/over-actuated systems; optimisation tools for constrained actuator management; actuator limitations; redundancy management; degradation/failure scenarios. **[POLIMI PDF]**
- Data-informed modelling and uncertainty representation (complementary tools for model refinement, uncertainty assessment, controller validation). **[POLIMI PDF]**
- Implementation: MATLAB/Simulink, modelling of aerospace vehicle dynamics, numerical simulation, controller tuning, performance assessment, robustness analysis, experimental validation. **[POLIMI PDF]**
- Critical assessment of paradigms; interpretability, validation, safety, certification-oriented constraints. **[POLIMI PDF]**

## Research group facts **[POLIMI PDF]**
- Research directors named: **Davide Invernizzi**. **[POLIMI PDF]**
- Composition: 1 Full Professor, 1 Associate Professor, 0 Assistant Professors, 4 PhD Students. **[POLIMI PDF]**
- Department: Dipartimento di Scienze e Tecnologie Aerospaziali (DAER), Politecnico di Milano, via La Masa 34, Milano. **[POLIMI PDF]**

## Administrative facts (from APPLICATION PDF, not a research source)
- Call: 42° ciclo, 1 position, scholarship ~1600 €/month net, +800 €/month for up to 6 months abroad. **[POLIMI PDF – application]**
- Deadline: 18/09/2026 14:00 (Italian time). **[POLIMI PDF – application]**
- Research project report: 4,000–8,000 characters (excluding bibliography/figures), single PDF ≤ 3 MB. **[POLIMI PDF – application]**
- Evaluation: curriculum max 45 pts; research proposal max 55 pts; suitability requires ≥60/100 and topic judged suitable. **[POLIMI PDF – application]**
- AI use prohibited for generating original text; only correction of candidate-written text allowed (must be declared). **[POLIMI PDF – application]**

## Terminology note (do not replace)
The PDF uses: nonlinear dynamic inversion, feedback linearisation, flatness-based control, robust/adaptive control, L1-inspired architectures, control allocation, residual dynamics, model refinement, multi-fidelity, interpretability, certifiability. Use these exact terms in the proposal; do not silently substitute "MPC", "RL", etc. where the PDF did not invoke them (though MPC/RL may appear in literature as baselines).
