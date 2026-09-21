# Assessment – Astrodynamics Engineer

## 1. Question 1 – Seven-Day LEO Orbit Prediction

### 1.1 Mathematical model and justification

A two-body/Keplerian model is a useful baseline, but it is inadequate for a high-fidelity seven-day LEO prediction because the dominant perturbations are not captured. I would build the force model as a hierarchy and stop when the residual error is within the prediction-error budget:

- **Two-body baseline** (point-mass gravity with Earth's μ) – useful for a first-cut orbit and for defining the reference motion.
- **Non-spherical Earth gravity** – J2 is the first-order representation of oblateness and drives the secular drift in Ω and ω; a higher-degree/order gravity field is retained when the altitude, required accuracy, and computational budget justify it. The required degree/order should come from the error budget, not a fixed rule.
- **Atmospheric drag** – dominant below a few hundred km and a leading source of secular decay and along-track error.
- **Third-body (Sun/Moon) and solar radiation pressure (SRP)** – for a typical LEO spacecraft over seven days these are secondary compared with Earth gravity and drag, but they should not be called universally negligible; include them when the required accuracy, area-to-mass ratio, or mission conditions warrant the additional fidelity.

The state is propagated by numerical integration (e.g., a fixed-step Runge–Kutta or a Gauss–Jackson integrator with adaptive tolerance) using a consistent μ and the selected force model. This is the right fidelity because it captures the dominant error sources while staying practical for operations.

### 1.2 Are the six elements sufficient? Additional parameters

The six classical elements describe the instantaneous orbit only when their **reference frame, epoch, gravitational parameter/model, and conventions** are also defined. For high-fidelity propagation they are not sufficient on their own.

I separate the inputs into what is **required baseline** versus **optional/higher-fidelity**:

**Required baseline:** defined inertial frame and epoch; Earth's μ; selection of the gravity-field fidelity; a time system; the spacecraft mass and an effective area-to-mass ratio with a drag coefficient; and an atmospheric density model with its inputs.

**Spacecraft (as applicable):** mass; effective drag area / area-to-mass ratio; drag coefficient C_d; attitude or an effective cross-sectional model (since drag and SRP depend on orientation); SRP coefficient / optical properties if SRP is modeled; spacecraft dimensions if size affects the analysis.

**Environment:** Earth gravity model (e.g., a spherical-harmonic field); atmospheric density model (e.g., NRLMSISE-00 or equivalent); space-weather inputs for density (F10.7 solar flux, Kp/Ap); Earth orientation parameters (EOP) for inertial↔Earth-fixed transformations; Sun/Moon ephemerides if third-body gravity is included; time/epoch information.

**Uncertainty:** initial-state covariance; and, where relevant, uncertainty in C_d and atmospheric density.

### 1.3 Coordinate systems and transformations

I use three frames in practice:

- **Inertial frame** (GCRF/ICRF) for orbit propagation and for expressing the orbital elements.
- **Earth-fixed frame** (ITRF) for relating the spacecraft to the rotating Earth – ground tracks, ground-station visibility, and aligning the atmosphere model.
- **Local/orbital RSW (radial/along-track/cross-track)** frame for decomposing errors and the conjunction geometry.

The orbital elements must have a defined reference frame and epoch; transforming them to Cartesian state is the standard perifocal-to-inertial rotation using a, e, i, Ω, ω, ν.

The inertial-to-Earth-fixed transformation is **time-dependent** and cannot be captured by a single fixed rotation. It is built from the precession/nutation treatment, Earth rotation (via the Earth Rotation Angle / Greenwich sidereal time), and polar motion, all driven by EOP and a consistent time scale (including UT1). Earth-fixed-to-topocentric supports ground-station and observer-site calculations. The important engineering point is that the rotation must be recomputed at each epoch from the current EOP, not applied as a constant matrix.

### 1.4 Prediction-accuracy methodology

Meaningful metrics are: position error ||r_pred − r_ref||, velocity error, and the RSW decomposition (radial/along-track/cross-track), plus the full state-error norm and covariance. I distinguish four angles:

- **Numerical-integration accuracy:** step-size refinement and integrator-tolerance convergence tests.
- **Dynamic-model accuracy:** compare different gravity/drag fidelity levels and run sensitivity to C_d and density.
- **Prediction accuracy:** compare the predicted state to a trusted orbit (e.g., GPS/SLR-derived) when available.
- **Uncertainty consistency:** propagate the covariance (state-transition or Monte Carlo) and check whether actual errors are consistent with the predicted uncertainty.

Atmospheric drag lowers orbital energy and mean motion, producing an accumulating phase/along-track error that can become significant over multi-day propagation; this is why along-track error matters most for conjunction analysis. The error should be examined over the full propagation interval, not only at the seven-day endpoint.

## 2. Question 2 – Conjunction and Collision Avoidance

### 2.1 Closest approach (time and distance) and numerical method

The two satellites are given at different epochs: satellite 1 at t1 and satellite 2 at t2 > t1. My workflow is:

1. Convert each element set to Cartesian state in a common inertial frame, each at its own epoch.
2. Propagate satellite 1 from t1 and satellite 2 from t2 using the same time scale, dynamics model, reference frame, and force-model fidelity.
3. Over the common time interval around the expected conjunction, form the relative position ρ(t) = r1(t) − r2(t) and minimize d(t) = ||ρ(t)||.
4. The time that minimizes d(t) is the TCA; the corresponding value is the minimum miss distance.

At an interior minimum, d/dt[ρ²] = 2 ρ·ρ̇ = 0, i.e. **ρ · v_rel = 0** (with a second-order check confirming a local minimum).

In practice I do not rely on a single fixed sampling. I use a **coarse temporal screening** to bracket the candidate minimum, then a **one-dimensional local refinement** (Brent's method or golden-section on d(t), or a root-solve on ρ·v_rel), verify it is a local minimum, and recompute with the accurate propagator.

### 2.2 Evasive / collision-avoidance maneuver methodology

A practical maneuver-analysis workflow:

1. Define the baseline conjunction (TCA, miss distance, risk).
2. Decide whether a maneuver is required against the mission/operator-defined minimum separation or risk threshold.
3. Choose decision variables: maneuver epoch, ΔV magnitude, and ΔV direction.
4. Generate candidate maneuvers (impulsive-burn sensitivities across radial/along-track/cross-track and timing).
5. Propagate each maneuvered trajectory with the same dynamics.
6. Recompute TCA, miss distance, and conjunction risk for each candidate.
7. Check operational constraints.
8. Evaluate robustness to maneuver-execution and navigation uncertainty.
9. Check for secondary/future conjunctions introduced by the maneuver.
10. Select the maneuver by a cost/risk trade-off (smallest adequate ΔV with acceptable risk).

The best direction and timing depend on orbital geometry, time to TCA, relative velocity, the required change in relative position at TCA, the ΔV budget, and operational constraints – an optimized direction is not always radial. Constraints and trade-offs include available ΔV, propellant, thrust capability, maneuver timing, attitude restrictions, navigation and execution error, mission/orbit-maintenance limits, recovery needs, and future conjunctions.

### 2.3 Nominal miss distance versus collision risk

The deterministic minimum distance (minimum ||r1 − r2||) does **not** by itself quantify collision risk when state uncertainty is significant. For a high-quality assessment I would use the position/velocity covariance, propagate the relative-state uncertainty, and compute a probability of collision (Pc) or an equivalent risk metric, accounting for the conjunction geometry and spacecraft dimensions. The maneuver decision should be driven by this uncertainty-aware risk, not by the nominal miss distance alone.

## 3. Assumptions

- Earth-centered LEO orbit.
- Initial orbital elements are known at specified epochs and in a defined reference frame.
- No unmodeled maneuvers occur during nominal propagation.
- Consistent force and reference-frame models are used for both spacecraft.
- Required environmental data (gravity, atmosphere, space weather, EOP) are available at the chosen fidelity.
- The conjunction is analyzed over an interval containing the expected TCA.
- Spacecraft state uncertainty is represented when risk assessment is required.

## Conclusion

For seven-day LEO prediction I use numerical propagation with Earth's gravity field beyond the point-mass term and atmospheric drag, adding higher-fidelity terms only as the error budget demands; the six classical elements are insufficient without frame, epoch, physical, and environmental data. Conjunction analysis requires consistent propagation of both objects to a local minimum of relative distance (ρ·v_rel = 0), and collision avoidance should be decided on uncertainty-aware risk with a constrained, cost-balanced maneuver.

