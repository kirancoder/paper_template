# 00 — SESSION STATE

## Workspace / scope
- Working dir: `/media/D/git_repos/paper_template/PhD_proposal`
- Scope restriction: ONLY `PhD_proposal/**`. Parent repo, `paper_template/`, `GNC_paper/`, `.git/` are OFF-LIMITS.
- Source PDFs:
  1. `SCHEDA_5736_IAER_ADVANCED_CONTROL_DESIGN_METHODS_FOR_AUTONOMOUS.pdf` — the research topic DESCRIPTION (PRIMARY technical source).
  2. `5736_5512_APPLICATION_...pdf` — administrative call text (deadlines, format). NOT a research source.
- `AGENTS.md` — instructions, not a research source.

## Current phase
ALL PHASES COMPLETE (00–12 + bibliography + sources_to_verify). Research notebook is self-contained. Awaiting user instruction to (a) write the final proposal (user-only task per scope), (b) deepen any section, or (c) verify remaining DOIs in `sources_to_verify.md`.

## Completed phases
- [x] PASS 1 / PHASE 1: read both supplied PDFs, extract requirements (`01`).
- [x] `02_technical_field_map.md`, `03_literature_map.md`, `bibliography.md`, `sources_to_verify.md`.
- [x] `04_key_papers.md`, `05_research_gap_analysis.md`.
- [x] `06_adversarial_gap_check.md` (TWO passes: Gahlawat L1-GP/CL1-GP; then B1–B12 SINDy-CA, Falconí, Lovera H∞+CA, DI+CA FTC, etc.).
- [x] `07_candidate_research_directions.md`, `08_ranked_directions.md`, `09_research_architecture.md`, `10_research_questions.md`, `11_validation_strategy.md`, `12_three_year_roadmap.md`.

## In progress
- None. Optional: verify remaining unverified DOIs (Invernizzi 2018/2021, Hovakimyan 2011, Fliess, Buffington&Enns, Su RA-L, "Model incremental learning" journal, "Robust Stability and Performance Analysis of IDI" full citation) listed in `sources_to_verify.md`.

## Current strongest research hypothesis (REVISED after adversarial check, [RESEARCH GAP])
The defensible PhD direction is **NOT** a generic "L1 + GP" (already done by Gahlawat et al. 2020/2021) and **NOT** a generic "CBF safety + CA" (done by Hafner et al. 2026). The genuine gap is: a **unified, interpretable, model-based (flatness/NDI) control architecture for OVER-ACTUATED autonomous aerospace vehicles** that (i) embeds control allocation in the control law with saturation/rate/degradation handling, (ii) uses L1-inspired/adaptive compensation + a **physically-structured** data-informed residual-dynamics module (preserving the interpretable model), and (iii) is backed by an interpretability/certification argument + multi-fidelity validation. Differentiators: over-actuation + embedded CA + degradation + structured residual + multi-fidelity certification vs Gahlawat (CA-free, simulation-only) and vs Delft INCA (not interpretable-certifiability facing).

## Competing hypotheses
- H2: L1-adaptive + NDI with integrated allocation and actuator-degradation handling.
- H3: Data-informed residual-dynamics learning on top of a flatness/NDI nominal controller with certifiable stability.
- H4: Multi-fidelity / trajectory–control co-design for over-actuated vehicles.

## Unresolved questions
- What exactly is Invernizzi's group currently publishing (last 3–5 yrs)? Need literature search.
- Is "flatness + over-actuation + allocation" already mature in his group, leaving the genuine gap at the data-informed/certifiable uncertainty layer?
- What experimental platforms does the group actually have (fixed-wing UAV? hexrotor? tiltrotor?)? Need to find.

## Literature still needed
- Invernizzi publications (flatness, over-actuation, allocation).
- Seminal flatness-based control (Fliess, Lévine, Martin, Rouchon; Dell'Angelo, Buccieri, Mullhaupt; Sarras, Zheng).
- NDI / dynamic inversion flight control (Enns, Bugajski, Meyer; Härkegård; Tjanaka, Stepanyan).
- L1 adaptive control (Cao, Hovakimyan; later aerospace applications).
- Control allocation surveys (Johansen, Fossen; Oppenheimer, Doman; Härkegård; Petersen, Alleyne).
- Data-informed / learning-based flight control with guarantees (incremental nonlinear control, GP, SINDy residual dynamics, physics-informed).
- Certifiability of learning-based aerospace control (Lewis, richard, chowdhary, taylor).

## Papers already examined
- None external yet (only the two PDFs).

## Suspected research gaps (to verify)
- G1: Integration of control allocation INTO the nonlinear (flatness/NDI) control law rather than as downstream optimization, under actuator saturation/rate/degradation, with guaranteed robustness margins.
- G2: Uncertainty-aware data-informed residual-dynamics refinement that preserves the physical/interpretable structure of the nominal model-based controller (so certifiability is retained).
- G3: Adaptation bandwidth vs. control-allocation interaction (L1-inspired) under realistic actuator constraints.
- G4: Multi-fidelity validation methodology linking analytical nonlinear models → data-enhanced representations → experiments, with quantified uncertainty.

## Gaps that have been challenged
- G2 (wide "L1+GP+stability"): PARTIALLY DISPROVED by Gahlawat L1-GP/CL1-GP (2020/2021). NARROWED.
- G2 (narrowed "structured+CA+failure"): **FURTHER challenged** by B1 (SINDy interpretable CA + failure, 2026), B6 (MRAC+adaptive CA flight-tested), B7/B8 (adaptive-CA stability), B11 (DI+CA FTC).
- G5 (L1-inspired + embedded CA + over-actuated): not disproved; but adaptive+CA+degradation+flight-test IS done (Falconí, Lu, NASA) via MRAC/H∞/SMC — so differentiator must be **L1-inspired** (not MRAC/H∞) + **flatness/NDI core** + **certification**.
- G1/G5 (DI+CA FTC): DONE by B11 (EuroGNC 2019) and host-group H∞+CA (B9/B10). Differentiator = the L1-inspired + data-informed structured residual + certification assembly.
- **Final gap framing:** the *integrated, certification-facing assembly* of the CALL's exact method set (flatness/NDI + L1-inspired + embedded CA + physically-structured data-informed residual + interpretability/certifiability + multi-fidelity validation) for the host group's over-actuated thrust-vectoring UAV. No single paper delivers this assembly.

## Next research actions
1. `07_candidate_research_directions.md` (5–10 directions, classified) — IN PROGRESS.
2. `08_ranked_directions.md`.
3. `09_research_architecture.md` (block diagram + math structure).
4. `10_research_questions.md` (RQ1–RQ6).
5. `11_validation_strategy.md` (analytical/data/experimental + multi-fidelity).
6. `12_three_year_roadmap.md`.
