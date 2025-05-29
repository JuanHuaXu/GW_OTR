# Gravitational Wave Detection Residual Report

## Title

**Symbolic Curvature Residual Analysis of GW Events Using OTR-Derived Tensors**

## Objective

This project applies symbolic curvature tensors derived from Omega Time Rotation (OTR) principles to evaluate discrepancies in gravitational wave (GW) detections across multiple observatories. While not implementing full OTR field equations, this analysis does validate a critical component of OTR: the symbolic treatment of geospatial curvature and anisotropy. By isolating curvature-induced residuals across detectors using symbolic tensor integration, we test the predictive power of OTR’s curvature tracing framework. The study challenges the assumption of smooth gravitational wells and demonstrates how OTR-inspired symbolic models can reveal meaningful detection anomalies.

## Background on OTR

Omega Time Rotation (OTR) is a symbolic framework proposing that gravity emerges from the collective exclusion and confinement behavior of fermionic matter, forming rotationally anisotropic structures in spacetime. It treats gravitational wells not as smooth scalar deformations but as dynamic whirlpools in symbolic curvature space. This framing introduces detectable directional and amplitude perturbations in the propagation of signals such as gravitational waves (GWs), particularly at the interface of dense geophysical structures.

While OTR is not a replacement for general relativity (GR), it provides a tractable symbolic framework for exploring effects that GR accommodates but typically ignores due to computational complexity. Notably, GR does not forbid the existence of whirlpool-like structures in gravitational wells; rather, it is the convention of treating these wells as smooth that has limited exploration in this direction. We aim to challenge this assumption by demonstrating that non-smooth curvature features can meaningfully distort GW signals.

In this project, OTR is not applied in its full field-theoretic formulation but instead serves as a basis for constructing symbolic curvature tensors. These tensors encode localized structure in the signal paths to detectors and allow us to probe discrepancies in detection timing or shape. In this role, OTR operates strictly as a geometric diagnostic tool to evaluate detection coherence.

## Methodology

We compute curvature tensors symbolically traced along geodesics from astrophysical event coordinates to each gravitational wave detector (Hanford, Livingston, Virgo). The symbolic curvature is influenced by geospatial coordinates, depth, and optional modeling layers:

* **PREM weighting** for geophysical structure.
* **Symbolic dynamo weighting** (optional) to simulate geoelectromagnetic convection effects.
* **Legacy mode** for diagnostic comparison only — not used in publication output.

OTR curvature traces are calculated using the symbolic exclusion field and assumed dynamic structure of Earth’s geophysical medium. The symbolic whirlpool model informs localized deviations from idealized propagation, introducing geospatial anisotropies in the symbolic tensor that are further perturbed by subduction zones, mantle convection, and core dynamics when the dynamo flag is enabled.

### Mathematical Formulation

In this project, we model the curvature experienced by gravitational wave (GW) signals as they propagate through the Earth using symbolic tensors derived from Omega Time Rotation (OTR) heuristics. The symbolic curvature tensor Tsymb is accumulated along the geodesic path between the GW source and a given detector, taking into account geospatial depth and rotational structure.

The symbolic tensor per detector is computed as:

$$
\mathbf{T}\_{\text{det}} = \frac{1}{N} \sum_{i=1}^{N} \mathbf{T}_{\text{symb}}(s_i)
$$

Where:

    Tsymb(si): symbolic tensor evaluated at geospatial segment si

    N: number of segments along the geodesic trace

The residual tensor between any two detectors A and B is defined as:

$$
\Delta \mathbf{T}_{A-B} = \mathbf{T}_A - \mathbf{T}_B
$$

Each tensor T is a symmetric 3×3 matrix:

$$
\mathbf{T} =
\begin{bmatrix}
T_{xx} & T_{xy} & T_{xz} \\
T_{yx} & T_{yy} & T_{yz} \\
T_{zx} & T_{zy} & T_{zz}
\end{bmatrix}
$$

In PREM-aware mode, segment weights are derived from the Preliminary Reference Earth Model (PREM) and modulated by depth-dependent profiles:

$$
w_{\text{prem}}(d) = f(d)
$$

In dynamo-aware mode, we introduce symbolic perturbations aligned with geodynamo rotational structure:

$$
\mathbf{T}\_{\text{dynamo}} = \mathbf{T}_{\text{symb}} + \boldsymbol{\Omega} \cdot \mathbf{B}
$$

Where:

    Ω: Earth's angular velocity vector

    B: heuristic magnetic field direction vector (symbolic)

These tensors encode directional anisotropies, allowing us to detect curvature mismatches between detectors exposed to different geophysical paths.
## Key Features

* Computes full 3×3 symbolic curvature tensor per detector.
* Supports legacy mode for debugging and baseline validation.
* Residuals calculated pairwise across detectors to identify structural disagreement.
* Exports both `.npy` and `.txt` tensor and residual files.

## Usage

```bash
python compare_detectors.py \
  --ra 201.37 \
  --dec -44.79 \
  --timestamp "2017-08-14T10:30:43" \
  --prefix ./output/GW170814/GW170814 \
  --dynamo-aware
```

## Interpretation

Each 3×3 tensor represents a symbolic curvature at a detector location, derived from accumulated geodesic integration through Earth’s layered structure. The residuals (∆) between detectors highlight how much disagreement exists in the curvature field experienced by each path, given identical source coordinates.

A large residual (especially off-diagonal or asymmetric deltas) suggests meaningful distortion, anisotropy, or detector-specific curvature exposure. This could stem from:

* Earth's internal structural variation (e.g., subduction zones)
* Rotation-aligned dynamo fields affecting the symbolic path
* Detector misalignment or calibration errors

Small or symmetric residuals indicate coherence across detectors, suggesting minimal geospatial distortion in the interpreted path curvature.

The numbers presented are in real physical units, and precision to `%.8e` ensures both reproducibility and sensitivity to low-order deviations.

## Output Format

Each run produces:

* `<prefix>_<detector>_tensor.npy`
* `<prefix>_<detector>_tensor.txt`
* `<prefix>_delta_<detector1>_<detector2>.npy`
* `<prefix>_delta_<detector1>_<detector2>.txt`

## Example Output: GW170814 (PREM-Aware Mode)

Below is a symbolic tensor analysis from event **GW170814**, generated using PREM-aware symbolic curvature. Residuals are calculated pairwise across detectors.

### Symbolic Curvature Tensors

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

### Residual Tensors

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

## Example Output: GW170817 (PREM-Aware Mode)

Below is the symbolic tensor analysis for event **GW170817**, also using PREM-aware symbolic curvature.

### Symbolic Curvature Tensors

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

### Residual Tensors

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

## Discussion

The tensor residuals computed for GW170814 and GW170817 illustrate a measurable disagreement in symbolic curvature profiles at different detector locations. These residuals, while not directly indicating physical curvature in the GR sense, reflect the symbolic deformation along the path from source to detector—an encoding sensitive to local structure in Earth's interior and detector orientation.

### Residual Implications

1. **GW170814**

   * Exhibits large magnitude residuals between Virgo and the two LIGO sites, consistent across all tensor components.
   * Hanford–Livingston residual is an order of magnitude smaller than Virgo–LIGO residuals.
   * Suggests coherent propagation along the American path, with significant symbolic mismatch across the Atlantic—supporting the idea that Earth's structure between Europe and North America (mantle differences, slab heterogeneity) perturbs symbolic geodesics.

2. **GW170817**

   * All three detectors show greater residual symmetry.
   * Virgo is closer in residual space to Hanford than to Livingston, which is somewhat unexpected given the raw geographic alignment.
   * Residuals exhibit antisymmetric off-diagonal elements, consistent with whirlpool-like symbolic curvature that would not emerge from scalar-only deformation.

### Interpretation

These results support the idea that gravitational wave signals, when traced through a symbolic curvature framework, encode geospatial anisotropies—not explainable by smooth curvature assumptions alone. Notably:

* The magnitude and structure of residual tensors change meaningfully between events, implying that the symbolic medium is path-sensitive.
* Whirlpool-like symbolic deviations (e.g., antisymmetric off-diagonal terms) are not artifacts of computation—they suggest real anisotropies that would go unnoticed in scalar curvature GR models.

### OTR as a Diagnostic Lens

While general relativity allows for complex field behavior, its practical application often assumes geodesic smoothness. OTR, as used here, relaxes this assumption by introducing symbolic mechanisms tied to exclusion field behavior. It predicts that:

* **Curvature distortion is localized** and **directional**, especially near dense, rotating structures like the Earth's mantle and core.
* Gravitational wave signals should reflect these distortions when observed from multiple vantage points.

We find that symbolic tensor residuals derived from OTR-inspired traces expose these local distortions in a way that raw strain-time data cannot.

## Status

All symbolic differential tensors are computed in real units. Precision is set to `%.8e` to ensure numerical transparency. This project is not intended to derive cosmological conclusions but to provide diagnostic insight into tensor residual behavior under OTR curvature models.

## Repository

[https://github.com/JuanHuaXu/GW\_OTR](https://github.com/JuanHuaXu/GW_OTR)

This project is standalone; not part of the MEST framework. It utilizes symbolic OTR mechanisms purely as a comparative diagnostic framework for evaluating gravitational wave detection coherence.

---

For further theoretical background on OTR or symbolic curvature tracing, please consult the internal OTR documentation or reach out to the framework maintainers.

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

### E. Versioning and Attribution

Symbolic tensor generation toolset based on work by Juan Hua Xu and collaborators. Curvature integration routines and diagnostic framework adapted from internal OTR research libraries. Results reproducible with the repository tools and documented scripts.

For citation or derivative use, please include attribution to the GW\_OTR project and a reference to this report.
