# 10 — RESEARCH QUESTIONS

Derived from gaps G1–G6 (`05`) and the architecture (`09`). Each RQ is tagged with the gap it addresses and the candidate direction(s). Tag [RESEARCH GAP] for still-open questions.

## RQ1 — Integration of control allocation into the model-based (flatness/NDI) control law with robustness under saturation/rate/degradation  [G1, D1/D2/D7]
> Can control allocation be embedded *inside* a flatness/NDI control law (rather than as a downstream block) such that provable robustness margins hold under actuator saturation, rate limits, and partial degradation/failure for an over-actuated aerospace vehicle?
- Sub-Q: How should CA feasibility constraints enter the nominal stability proof? How to guarantee graceful degradation (reconfiguration without destabilising the baseline loop)?

## RQ2 — Physically-structured, data-informed residual that preserves interpretability  [G2, D3]
> Can aerodynamic/model uncertainty be learned as a *physically-structured* residual augmentation of the nominal flatness/NDI model — rather than a black box — while retaining closed-loop stability and an interpretability argument?
- Sub-Q: Hybrid first-principles + sparse/parametric/SINDy identification — what structure guarantees interpretability AND accuracy? How to bound the residual (UQ) for certification?

## RQ3 — L1-inspired uncertainty compensation inside the embedded-allocation loop  [G5, D2]
> Can an L1-inspired (decoupling/low-pass) adaptive augmentation of a flatness/NDI over-actuated controller operate *with* an embedded CA under saturation/rate/degradation, preserving the L1 transient/robustness guarantee?
- Sub-Q: Where to inject the L1 law (virtual / pseudo-control / allocation level)? How does L1 bandwidth interact with CA rate? (links to RQ6)

## RQ4 — Certification / interpretability argument for the unified loop  [G3, D4/D5]
> How can GP/set-membership UQ of the structured residual be combined with the L1 robustness margin and CA μ-analysis into a single, certification-oriented interpretability/assurance argument for the integrated loop?
- Sub-Q: What is the minimal acceptable assurance case for aviation certification of such an adaptive, data-informed loop (formal proof vs assurance case)?

## RQ5 — Multi-fidelity validation methodology  [G4, D4]
> What systematic multi-fidelity validation pipeline (analytical nonlinear model → data-enhanced representation → HIL/experiment) with quantified uncertainty transfer best supports the certification argument for the integrated architecture?

## RQ6 — Co-design of adaptation bandwidth and control allocation under actuator constraints  [G6, D7]
> How does L1/adaptive bandwidth interact with control-allocation rate and degradation dynamics, and how should they be co-designed so that adaptation does not fight the allocator (or vice-versa) during saturation/rate-limited/degraded operation?

## Cross-cutting hypothesis [HYPOTHESIS]
The *integrated assembly* (flatness/NDI + L1-inspired + embedded CA + structured residual + certification/multi-fidelity) yields, for over-actuated autonomous aerospace vehicles, superior verified robustness, graceful degradation, and certifiability compared with (i) robust H∞+CA baselines (Lovera B9/B10), (ii) MRAC+adaptive-CA baselines (Falconí, B7/B8), and (iii) CBF safety baselines (Hafner 2026) — while remaining interpretable. This is the central PhD claim to be tested.

See `11_validation_strategy.md` (how each RQ is tested) and `12_three_year_roadmap.md`.
