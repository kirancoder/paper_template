# 06 — ADVERSARIAL GAP CHECK (mandatory self-disproof)

Objective: try to DISPROVE G1–G6 from `05_research_gap_analysis.md`. For each, search for papers that already solve it. Key adversarial finds below. Source tag **[LITERATURE]** unless noted.

---

## A. Strong prior work that challenges G2 and G5

### A1. L1-GP: Adaptive Control with Bayesian Learning (Gahlawat et al., AISTATS 2020)
proceedings.mlr.press/v120/gahlawat20a. **VERIFIED.**
- Combines **L1 adaptive control with Gaussian Process Regression** for safe simultaneous control and learning. GPR learns model uncertainty; L1 provides stability/robustness/transient guarantees throughout learning. Filter bandwidth ω increases as GP error shrinks. → **This directly challenges G5 ("L1-inspired + data-informed") and part of G2.**
- Limitations (why it does NOT close the gap): generic nonlinear systems; **no over-actuated control allocation**; **no embedded CA / actuator saturation / rate / degradation**; GP uncertainty is not required to be *physically structured*; no certification case; no multi-fidelity validation; no flight test on over-actuated UAV.

### A2. Contraction L1-Adaptive Control using Gaussian Processes (Gahlawat et al., CoRL 2021)
proceedings.mlr.press/v144/gahlawat21a. **VERIFIED.**
- Contraction-theory-based L1 (CL1) + GP regression; **safety certificates**; GP posterior variance → high-probability tracking bounds; learning improves performance without re-tuning. → **Stronger challenge to G2/G5.** 
- Limitations: same as A1 (no CA/over-actuation/degradation; not the interpretable model-based flight core; not certifiable in aviation sense; simulation only).

### A3. Probabilistic Analysis and Verification Framework for Adaptive Flight Control (Fravolini, Yucelen, Napolitano)
- Probabilistic LMI framework for UUB regions of MRAC on F-16 short-period; less conservative than worst-case. → challenges "certification of adaptive control is wholly open" (G3/C1 nuance): V&V *methodology* for adaptive control exists in research form.
- Limitations: MRAC-specific, not the integrated model-based+residual+CA loop; not certification-accepted.

### A4. Control Barrier Functions on a Pseudo Control Level for Safe Flight Control (Hafner, Autenrieb, Steinert, Holzapfel, EuroGNC 2026)
eurognc.ceas.org/archive/EuroGNC2026/pdf/CEAS-GNC-2026-010.pdf. **VERIFIED.**
- CBF safety filter placed **between outer controller and control allocation**, before CA, for **overactuated** aircraft; argues this *simplifies certification* (decomposed, analysable modules). → challenges the "integrated safe CA for over-actuated vehicles is open" sub-claim (G1 safety part).
- Limitations: uses CBF (NOT the topic's flatness/NDI/L1/allocation methods); treats safety as add-on filter, not the unified interpretable model-based+residual architecture the topic describes; no data-informed residual; no multi-fidelity.

### A5. CBF flight-envelope protection + INDI (Autenrieb 2025 arXiv:2504.18951; Traas/Atmaca/van Kampen 2026 AIAA 2026-0549; stealth-maneuver CBF+INDI MDPI 2025)
- Show CBF + INDI + envelope protection is an active, maturing stream. → competing safety paradigm to robust/L1.
- Limitations: CBF-based, not the topic's exact method set; often simulation; not integrated with data-informed residual + over-actuated CA.

### A6. Safe Physics-Informed ML for Dynamics and Control (NSF tutorial, Brunton/Findeisen et al.); "The Impact of Data on the Stability of Learning-Based Control" (Lederer arXiv:2011.10596); "Uncertainty-based Control Lyapunov Approach…Gaussian Processes" (TUM)
- Show safe/PIML + GP + Lyapunov/stability is a broad, active field. → G2's "data + stability" sub-piece is well covered.
- Limitations: general; not the specific over-actuated interpretable flight architecture with embedded CA.

---

## B. Does this DISPROVE the gaps?

### G2 (structured data-informed residual + interpretability + stability/certification for over-actuated vehicle)
- **Partially disproved in the general sense** (L1-GP, Contraction-L1-GP, recognizes GP+L1+safety already done). 
- **NOT disproved in the narrowed sense**: (i) physically-*structured* residual that preserves the model-based interpretable core; (ii) over-actuated vehicle with **embedded CA** (saturation/rate/degradation); (iii) **multi-fidelity validation + certification argument**. None of A1–A6 delivers this combination. 
- **Verdict: GENUINE but MUST BE NARROWED** to "structured/interpretable residual + embedded CA + over-actuation + multi-fidelity certification." Wide "L1+GP" claim is rejected.

### G5 (L1-inspired + embedded CA + over-actuated + degradation)
- **NOT disproved.** A1/A2 do L1+GP but **no control allocation at all**, no over-actuation, no degradation-aware CA. CBF-pseudo (A4) does over-actuated CA + safety but via CBF, not L1/robust model-based. 
- **Verdict: GENUINE and strong** — the intersection of L1-inspired/robust compensation WITH embedded CA for over-actuated vehicles under degradation is open.

### G1 (embedded CA + robustness under saturation/rate/degradation)
- Partial: INCA/D-INCA/AD-INCA (Delft) integrate CA+actuator dynamics+failures; CBF-pseudo integrates safety+CA. But rigorous robustness *margins* with graceful degradation inside a *flatness/NDI interpretable* core for over-actuated thrust-vectoring UAV (host group platform) remains open.
- **Verdict: PARTIAL — only as part of the integrated architecture, not standalone.**

### G3 (UQ → certification argument)
- Partial: probabilistic V&V (Fravolini), GP UQ exist. Certification *case* for the integrated loop still open. **GENUINE as supporting contribution.**

### G4 (multi-fidelity validation methodology)
- Partial: multi-fidelity verification of learning-based aviation (arXiv:2205.04590) exists but for DRL. For the model-based+residual+CA flight loop: **open**. **GENUINE supporting contribution.**

### G6 (adaptation bandwidth ↔ CA interaction)
- Sparse literature; **GENUINE** but narrow.

---

## C. Revised primary gap (after adversarial check) [RESEARCH GAP]
There is **no unified, interpretable, model-based control architecture for OVER-ACTUATED autonomous aerospace vehicles** that simultaneously:
(i) uses a flatness/NDI nominal core (host group's strength; topic's explicit methods),
(ii) **embeds control allocation within the control law** (not downstream) with explicit saturation, rate-limit, and degradation/failure handling,
(iii) augments uncertainty compensation via an **L1-inspired / adaptive** mechanism and a **physically-structured, data-informed residual-dynamics module** that preserves the physical model (differentiated from generic GP-L1 work such as Gahlawat's L1-GP/Contraction-L1-GP, which lack CA, over-actuation, and structured residuals),
(iv) provides an **interpretability / certification-oriented argument** supported by a **multi-fidelity (analytical → data-enhanced → experimental) validation methodology**.

Differentiators vs closest prior work:
- vs Gahlawat L1-GP / Contraction-L1-GP: we add **over-actuation + embedded CA + degradation + physically-structured residual + multi-fidelity certification**; they are generic, CA-free, simulation-only.
- vs Delft INCA/AD-INCA: we add the **interpretable flatness/NDI core + data-informed structured residual + certification framing**; they are INDI/optimisation-focused, not certifiability-facing.
- vs CBF-pseudo (Hafner et al.): we use the **topic's exact method set** (flatness/NDI/L1/allocation) in one unified architecture rather than a CBF add-on.

This refined gap is **defensible and not disproved** by the adversarial search. **[INFERENCE]**

## E. DEEP adversarial pass 2 (further narrowing of G2/G5) [LITERATURE]

The first pass already weakened G2/G5. A second pass found EVEN CLOSER prior work:

- **B1 (arXiv:2606.13794, 2026)** — interpretable (SINDy) control-effectiveness learning + nonlinear CA + online residual adaptation → graceful failure reconfiguration. This is the closest match to "physically-structured data-informed + interpretable + CA + failure." **Challenge to narrowed G2 is severe.**
- **B6 (Falconí, TUM thesis)** — MRAC + Predictor-Based Adaptive Control Allocation + Prioritizing CA, hexacopter flight tests with failures. **Challenge to G5 (adaptive + CA + degradation + flight test) is severe.**
- **B7 (Lu 2019), B8 (NASA adaptive CA)** — adaptive closed-loop CA with stability proofs under LoE/constant failures. Challenge G1/G5.
- **B11 (EuroGNC 2019)** — Dynamic-Inversion-based control law + optimization CA FTC for over-actuated hybrid UAV. Challenge G1/G5 (DI + CA + FTC already done).
- **B9, B10 (Cai & Lovera 2025; Lovera-group GS-PFTC)** — structured H∞ + online/gain-scheduled CA + μ-analysis for dual-system over-actuated UAV under faults. **These are likely the HOST GROUP's own recent work** → the group already does robust/adaptive + CA + FTC, but via H∞/μ-analysis, NOT via flatness/NDI + L1-inspired + model-based interpretable core with data-informed structured residual.

### What remains genuinely open after pass 2 [RESEARCH GAP]
No work delivers the **exact assembly the CALL requests**: a **flatness/NDI (model-based, interpretable) nominal core** + **L1-inspired (not MRAC/H∞/SMC) uncertainty compensation** + **embedded CA (saturation/rate/degradation)** + **physically-structured, data-informed residual** + a first-class **interpretability/certification argument** + **multi-fidelity validation**, all in ONE architecture for an over-actuated aerospace vehicle (the host group's thrust-vectoring UAV class). Closest papers each miss ≥1 of: flatness/NDI core (B1,B6,B7,B8,B9,B10 use SINDy/MRAC/H∞/SMC), L1-inspired (all use MRAC/H∞/SMC/adaptive-CA, not L1), certification case (none give aviation-certification argument), multi-fidelity validation (none). The CALL bundles precisely these methods and asks for a PhD to "develop" them → strong primary-source support that the integration is not yet mature. **Verdict: gap survives only as the integrated, certification-facing assembly — NOT any single component.**

## D. Competitor baselines this implies (for later sections)
- L1-GP / Contraction-L1-GP (Gahlawat) — closest but CA-free.
- INCA / AD-INCA (Delft) — CA+actuator dynamics+failures, INDI-based.
- CBF-pseudo safety filter (Hafner et al.) — safety+CA via CBF.
- GP adaptive flight control (Chowdhary, Ignatyev IBKS-GP) — data+stability, not over-actuated CA.
- Classical NDI/flatness + separate downstream CA (Johansen&Fossen baseline).

See `05_research_gap_analysis.md` (REVISION note appended) and `07_candidate_research_directions.md`.
