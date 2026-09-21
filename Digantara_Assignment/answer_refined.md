# Assessment – Astrodynamics Engineer

## 1. Question 1 – Seven-Day LEO Orbit Prediction

### 1.1 Mathematical model and justification

A two-body/Keplerian model is a useful baseline, but it is inadequate for a high-fidelity seven-day LEO prediction because the dominant perturbations are not captured. I would build the force model as a hierarchy and stop when the residual error is within the prediction-error budget:

- **Two-body baseline** (point-mass gravity with Earth's μ) – useful for a first-cut orbit and for defining the reference motion.
- **Non-spherical Earth gravity** – J2 is the first-order representation of oblateness and drives the secular drift in Ω and ω; higher-degree/order terms can be added when the altitude, required accuracy, and computational budget justify them. The required gravity fidelity should come from the error budget rather than a fixed rule.
- **Atmospheric drag** – often a major perturbation in LEO, with its importance depending strongly on altitude, ballistic coefficient, attitude, and space-weather conditions. It is a leading source of secular decay and along-track error.
- **Third-body (Sun/Moon) and solar radiation pressure (SRP)** – for a typical LEO spacecraft over seven days these are generally secondary to Earth gravity and drag, but they may be retained when the accuracy requirement, area-to-mass ratio, or mission conditions warrant the additional fidelity.

The state is propagated by numerical integration with appropriate step-size/control settings, e.g. an adaptive Runge–Kutta method; fixed-step multistep methods such as Gauss–Jackson are also common in operational orbit propagation. This fidelity captures the dominant error sources while staying practical for operations.

### 1.2 Are the six elements sufficient? Additional parameters

The six classical elements describe the instantaneous orbit, but meaningful propagation also requires an epoch, a reference frame, a time standard, a gravitational model/μ, the perturbation model, and spacecraft and environmental parameters. They are not sufficient on their own.

I separate the inputs into what is **required baseline** versus **optional/higher-fidelity**:

**Required baseline:** defined inertial frame and epoch; Earth's μ; selection of the gravity-field fidelity; a time system; the spacecraft mass and an effective area-to-mass ratio with a drag coefficient; and an atmospheric density model with its inputs.

**Spacecraft (as applicable):** mass; effective drag area / area-to-mass ratio; drag coefficient C_d; attitude or an effective cross-sectional model (drag depends on orientation); SRP coefficient / optical properties if SRP is modeled; spacecraft dimensions if size affects the analysis.

**Environment:** Earth gravity model (a spherical-harmonic field); an empirical atmospheric density model with space-weather inputs (e.g., F10.7 solar flux, Kp/Ap); Earth orientation parameters (EOP) for inertial↔Earth-fixed transformations; Sun/Moon ephemerides only if third-body gravity is included; time/epoch information.

**Uncertainty:** initial-state covariance; and, where relevant, uncertainty in C_d and atmospheric density.

Only the baseline set is mandatory for the chosen high-fidelity model; the optional items are needed only when the corresponding perturbation is actually included.

### 1.3 Coordinate systems and transformations

I use three frames in practice:

- **Inertial frame** (GCRF/ICRF) – the natural frame for orbit dynamics and for expressing the orbital elements.
- **Earth-fixed frame** (ITRF) – needed for Earth-relative quantities: ground tracks, ground-station visibility, and aligning the atmosphere model.
- **Local/orbital RSW (radial/along-track/cross-track)** – useful for interpreting errors and the conjunction geometry.

The orbital elements themselves must be associated with a defined reference frame and epoch; converting them to Cartesian state uses the standard perifocal-to-inertial rotation with a, e, i, Ω, ω, ν.

The inertial-to-Earth-fixed transformation is **time-dependent** and cannot be captured by a single fixed rotation. It is built from the precession/nutation treatment, Earth rotation (via the Earth Rotation Angle / Greenwich sidereal time), and polar motion, all driven by EOP and a consistent time scale (including UT1 where required). Earth-fixed-to-topocentric supports ground-station and observer-site calculations. The key engineering point is that the rotation must be recomputed at each epoch from the current EOP, not applied as a constant matrix.

### 1.4 Prediction-accuracy methodology

Meaningful metrics are: position error ||r_pred − r_ref||, velocity error, and the RSW decomposition (radial/along-track/cross-track), plus the full state-error norm and covariance. I distinguish four angles:

- **Numerical-integration accuracy:** step-size refinement and integrator-tolerance convergence tests.
- **Dynamic-model accuracy:** compare different gravity/drag fidelity levels and run sensitivity to C_d and density.
- **Prediction accuracy:** compare the predicted state to a trusted orbit (e.g., GPS/SLR-derived) when available.
- **Uncertainty consistency:** propagate the covariance (state-transition or Monte Carlo) and check whether actual errors are consistent with the predicted uncertainty.

Drag changes orbital energy and mean motion, producing accumulating phase and along-track errors over multi-day propagation; this is why along-track error matters most for conjunction analysis. The error should be assessed throughout the propagation interval, not only at the seven-day endpoint.

## 2. Question 2 – Conjunction and Collision Avoidance

### 2.1 Closest approach (time and distance) and numerical method

The two satellites are given at different epochs: satellite 1 at t1 and satellite 2 at t2 > t1. Each is therefore initialized at its own epoch and propagated to a common time interval before relative motion is evaluated:

1. Convert each element set to Cartesian state in a common inertial frame, each at its own epoch.
2. Propagate satellite 1 from t1 and satellite 2 from t2 using the same time scale, dynamics model, reference frame, and force-model fidelity.
3. Over the common time interval around the expected conjunction, form the relative position ρ(t) = r1(t) − r2(t) and minimize d(t) = ||ρ(t)||.
4. The time that minimizes d(t) is the TCA; the corresponding value is the minimum miss distance.

At an interior minimum, d/dt[ρ²] = 2 ρ·ρ̇ = 0, i.e. **ρ · v_rel = 0** (with a second-order check confirming a local minimum).

In practice I do not rely on a single fixed sampling. I use a **coarse temporal screening** to bracket the candidate minimum, then a **one-dimensional local refinement** (e.g., Brent's method or a root-solve on ρ·v_rel), verify it is a local minimum, and recompute with the accurate propagator.

### 2.2 Evasive / collision-avoidance maneuver methodology

A practical maneuver-analysis workflow:

1. Define the baseline conjunction (TCA, miss distance, risk).
2. Decide whether mitigation is required against the mission/operator-defined minimum separation or risk threshold.
3. Choose decision variables: maneuver epoch, ΔV magnitude, and ΔV direction.
4. Generate candidate maneuvers (impulsive-burn sensitivities across radial/along-track/cross-track and timing).
5. Propagate each maneuvered trajectory with the same dynamics.
6. Recompute TCA, miss distance, and conjunction risk for each candidate.
7. Enforce operational constraints.
8. Evaluate robustness to maneuver-execution and navigation uncertainty.
9. Check for secondary/future conjunctions introduced by the maneuver.
10. Select the maneuver by a cost/risk trade-off (smallest adequate ΔV with acceptable risk).

The best direction and timing depend on orbital geometry, time to TCA, relative velocity, the required change in relative position at TCA, the ΔV budget, and operational constraints – an optimized direction is not uniformly radial/along-track/cross-track. Constraints and trade-offs include available ΔV, propellant, thrust capability, maneuver timing, attitude restrictions, navigation and execution error, mission/orbit-maintenance limits, recovery needs, and future conjunctions.

### 2.3 Nominal miss distance versus collision risk

The deterministic minimum distance (minimum ||r1 − r2||) does **not** by itself quantify collision risk when state uncertainty is significant. For a high-quality assessment I would use the position/velocity covariance, propagate the relative-state uncertainty, and compute a probability of collision (Pc) or an equivalent risk metric, accounting for the conjunction geometry, spacecraft size, and a combined hard-body radius where appropriate. The maneuver decision should be driven by this uncertainty-aware risk, not by the nominal miss distance alone.

## 3. Assumptions

- Earth-centered LEO orbit.
- Initial orbital elements are known at specified epochs and in a defined reference frame.
- No unmodeled maneuvers occur during nominal propagation.
- Consistent force and reference-frame models are used for both spacecraft.
- Required environmental data (gravity, atmosphere, space weather, EOP) are available at the chosen fidelity.
- The conjunction is analyzed over an interval containing the expected TCA.
- Spacecraft state uncertainty is represented when risk assessment is required.

## Conclusion

For seven-day LEO prediction I use numerical propagation with Earth's gravity field beyond the point-mass term and atmospheric drag, adding higher-fidelity terms only as the error budget demands; the six classical elements are insufficient without frame, epoch, physical, and environmental data. Conjunction analysis requires consistent propagation of both objects, each from its own epoch, to a local minimum of relative distance (ρ·v_rel = 0), and collision avoidance should be decided on uncertainty-aware risk with a constrained, cost-balanced maneuver.
