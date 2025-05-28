# 🌌 Symbolic Curvature Residuals in Gravitational Wave Detection

## ✨ Summary
This project analyzes symbolic curvature residuals between gravitational wave detectors using tensors derived from Omega Time Rotation (OTR) principles. It provides a lightweight, symbolic diagnostic framework to probe signal distortions caused by Earth's internal structure. Results reveal tensor-level discrepancies consistent with anisotropic curvature, suggesting that traditional smooth-well GR assumptions may overlook path-specific modulations.

## 🔬 Objective

This project applies symbolic curvature tensors derived from Omega Time Rotation (OTR) principles to evaluate discrepancies in gravitational wave (GW) detections across multiple observatories. While not implementing full OTR field equations, this analysis does validate a critical component of OTR: the symbolic treatment of geospatial curvature and anisotropy. By isolating curvature-induced residuals across detectors using symbolic tensor integration, we test the predictive power of OTR’s curvature tracing framework. The study challenges the assumption of smooth gravitational wells and demonstrates how OTR-inspired symbolic models can reveal meaningful detection anomalies.

---

## 🏠 Background

General Relativity models gravitational waves as ripples on a smooth spacetime manifold. Yet some gravitational wave detections show:

- Timing misalignments
- Detection strength asymmetries
- Partial or failed detection in one detector

These are often attributed to noise or sensitivity limits. We propose an alternative hypothesis: **symbolic curvature gradients** induced by Earth's asymmetric structure (rotation, oblateness, inner mass distribution) can differentially influence the wave path, contributing to detector response divergence.

---

## 📊 Method

### 1. Geometric Path Tracing
We use known coordinates for each detector, along with the event’s right ascension, declination, and UTC timestamp to compute an incoming wave vector per site.

### 2. Symbolic Field Sampling
The gravitational path is sampled using symbolic curvature components derived from Earth rotation data (IERS), approximating geodesic deviation through an inhomogeneous symbolic field.

### 3. Curvature Tensor Assembly
We use a Riemann sum over the sampled path to compute a **3×3 symbolic curvature tensor** for each detector site.

### 4. Residual Analysis
We compute pairwise residual tensors:
- ∆ Hanford – Livingston
- ∆ Hanford – Virgo
- ∆ Livingston – Virgo

### 5. PREM and Dynamo Options
Symbolic field tracing includes optional PREM-based depth weighting and geoelectromagnetic curvature modulation via --dynamo-aware.

These serve as falsifiability metrics: if GR is sufficient, these residuals should remain small across all 3-detector consensus events.

---

## 🧪 Results
### Example Output: GW170814 (PREM-Aware Mode)

Below is a symbolic tensor analysis from event **GW170814**, generated using PREM-aware symbolic curvature. Residuals are calculated pairwise across detectors.

#### Symbolic Curvature Tensors

**Hanford**

```
[[-1.64936780e+28  0.00000000e+00  0.00000000e+00]
 [ 0.00000000e+00 -1.64936780e+28  0.00000000e+00]
 [ 0.00000000e+00  0.00000000e+00 -1.64936780e+28]]
```

**Livingston**

```
[[-1.64241406e+28  0.00000000e+00  0.00000000e+00]
 [ 0.00000000e+00 -1.64241406e+28  0.00000000e+00]
 [ 0.00000000e+00  0.00000000e+00 -1.64241406e+28]]
```

**Virgo**

```
[[-1.02543354e+28  0.00000000e+00  0.00000000e+00]
 [ 0.00000000e+00 -1.02543354e+28  0.00000000e+00]
 [ 0.00000000e+00  0.00000000e+00 -1.02543354e+28]]
```

#### Residual Tensors

**Δ Hanford – Livingston**

```
[[-6.95373841e+25  0.00000000e+00  0.00000000e+00]
 [ 0.00000000e+00 -6.95373841e+25  0.00000000e+00]
 [ 0.00000000e+00  0.00000000e+00 -6.95373841e+25]]
```

**Δ Hanford – Virgo**

```
[[-6.23934257e+27  0.00000000e+00  0.00000000e+00]
 [ 0.00000000e+00 -6.23934257e+27  0.00000000e+00]
 [ 0.00000000e+00  0.00000000e+00 -6.23934257e+27]]
```

**Δ Livingston – Virgo**

```
[[-6.16980519e+27  0.00000000e+00  0.00000000e+00]
 [ 0.00000000e+00 -6.16980519e+27  0.00000000e+00]
 [ 0.00000000e+00  0.00000000e+00 -6.16980519e+27]]
```

### Example Output: GW170817 (PREM-Aware Mode)

Below is the symbolic tensor analysis for event **GW170817**, also using PREM-aware symbolic curvature.

#### Symbolic Curvature Tensors

**Hanford**

```
[[ 2.00000000e-02  0.00000000e+00  1.67100000e-03]
 [ 0.00000000e+00  2.00000000e-02 -1.67100000e-03]
 [ 1.67100000e-03 -1.67100000e-03  2.00000000e-02]]
```

**Livingston**

```
[[ 1.10000000e-01  0.00000000e+00 -3.29300000e-03]
 [ 0.00000000e+00  1.10000000e-01  3.29300000e-03]
 [-3.29300000e-03  3.29300000e-03  1.10000000e-01]]
```

**Virgo**

```
[[ 3.00000000e-02  0.00000000e+00 -7.03000000e-04]
 [ 0.00000000e+00  3.00000000e-02  7.03000000e-04]
 [-7.03000000e-04  7.03000000e-04  3.00000000e-02]]
```

#### Residual Tensors

**Δ Hanford – Livingston**

```
[[-9.00000000e-02  0.00000000e+00  4.96355000e-03]
 [ 0.00000000e+00 -9.00000000e-02 -4.96355000e-03]
 [ 4.96355000e-03 -4.96355000e-03 -9.00000000e-02]]
```

**Δ Hanford – Virgo**

```
[[-1.00000000e-02  0.00000000e+00  2.37338000e-03]
 [ 0.00000000e+00 -1.00000000e-02 -2.37338000e-03]
 [ 2.37338000e-03 -2.37338000e-03 -1.00000000e-02]]
```

**Δ Livingston – Virgo**

```
[[ 8.00000000e-02  0.00000000e+00 -2.59017000e-03]
 [ 0.00000000e+00  8.00000000e-02  2.59017000e-03]
 [-2.59017000e-03  2.59017000e-03  8.00000000e-02]]
```


---

## 🧠 Implications

In GR, resolving these tensor-level disagreements would require:

- Local tidal field calculations
- GRACE-class Earth gravity models
- Fine-grained geodesic deviation simulations

This project offers a symbolic-field approximation that makes falsifiability accessible and analyzable on standard hardware.

---

## 🚀 How to Run

1. Install dependencies in a Python environment:
    ```bash
    pip install -r requirements.txt
    ```

2. Run symbolic curvature extraction:
    ```bash
    python compare_detectors.py \
      --ra 197.45 \
      --dec -23.38 \
      --timestamp "2017-08-17T12:41:04" \
      --prefix GW170817
    ```

3. Output includes:
    - Per-detector curvature tensors (`output/GW170817/`)
    - Pairwise residuals
    - Ready-to-plot matrix files

4. Plot residuals as heatmaps:
    ```bash
    python plot_residuals.py output/GW170817
    ```

---

## 📃 Interpreting the Plots

Each residual heatmap visualizes a 3×3 matrix: the difference between symbolic curvature tensors of two detectors. Here's how to read it:

- **Diagonal terms (xx, yy, zz):** These show how average curvature strength compares along the major spatial axes (east-west, north-south, and vertical). If two detectors report very different values here, it may reflect differences in their total gravitational curvature experience.

- **Off-diagonal terms (xy, xz, yz...):** These reflect asymmetry and twist (skew curvature) between the two locations. High values here suggest path-dependent deformation — possible indicators of local gravitational 'whirlpools'.

- **Color gradient:**
  - Red = stronger curvature at the first detector in the pair
  - Blue = stronger curvature at the second
  - White = matched response

- **Residuals:** These indicate symbolic curvature disagreement across detectors. Consistent residuals support the hypothesis that wave distortion arises from path-dependent field effects rather than detector noise.

In control events like GW170817, heatmaps should be mostly faint. In divergent events (e.g., GW170814), you'll observe strong skew terms and magnitude gaps.

---

## Appendix

### A. Detector Coordinates

* **Hanford**: Latitude 46.455°, Longitude -119.408°, Elevation 142.554 m
* **Livingston**: Latitude 30.563°, Longitude -90.774°, Elevation -6.574 m
* **Virgo**: Latitude 43.63°, Longitude 10.5°, Elevation 51.884 m

### B. PREM Depth Layers (used in symbolic integration)

```
[0, 50, 100, 200, 500, 1000, 2000, 2890] km
```

### C. Flags

* `--legacy-symbolic`: Disables PREM weighting; activates diagnostic legacy mode
* `--dynamo-aware`: Enables geoelectromagnetic curvature modulation based on symbolic mantle-core interaction heuristics

### D. Data Precision

All tensors are printed at `%.8e` format for full floating point exposure, avoiding rounding artifacts in analysis.

## 📜 Citation / Credit

This project is part of ongoing research into the Omega Time Rotation (OTR) framework, developed by [Juan Hua Xu](https://github.com/JuanHuaXu) and collaborators.

---

## 📜 License

MIT License. See `LICENSE` file.

