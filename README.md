# 🌌 Symbolic Curvature Residuals in Gravitational Wave Detection

## 🔬 Objective

This project investigates symbolic curvature tensors as a complementary diagnostic to General Relativity (GR) for analyzing gravitational wave detection asymmetries across LIGO-class observatories. Using a field-inspired approximation of Earth's gravitational structure, we compute and compare the effective curvature traversed by gravitational waves arriving at:

- LIGO Hanford
- LIGO Livingston
- Virgo

Our aim is to test whether path-dependent field differences — not instrument error — may explain detection discrepancies.

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

These serve as falsifiability metrics: if GR is sufficient, these residuals should remain small across all 3-detector consensus events.

---

## 🧪 Results

### GW170817 – Control Case (3-Detector Agreement)

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0200       | ±0.00077       |
| Livingston | 0.0200       | ±0.00055       |
| Virgo      | 0.0268       | ±0.00026       |

Residuals between tensors:  
**∆ Max** ≈ 0.0068 (diagonal), 0.0013 (off-diagonal)  
✅ Consistent with shared field geometry.

---

### GW170814 – Test Case (3-Detector Divergence)

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0200       | ±0.00176       |
| Livingston | 0.1100       | ±0.00368       |
| Virgo      | 0.0250       | ±0.00068       |

Residuals between tensors:  
**∆ Max** ≈ 0.09 (diagonal), 0.0054 (off-diagonal)  
⚠️ Indicates possible curvature path skew contributing to detection divergence.

---

### GW190412

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0100       | ±0.00083       |
| Livingston | 0.0150       | ±0.00116       |
| Virgo      | 0.0200       | ±0.00099       |

**∆ Max** ≈ 0.01 (diagonal), 0.00033 (off-diagonal)  
✅ Moderate, generally aligned field geometry.

---

### GW190521_074359

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0150       | ±0.00130       |
| Livingston | 0.0100       | ±0.00071       |
| Virgo      | 0.0150       | ±0.00130       |

**∆ Max** ≈ 0.005 (diagonal), 0.00059 (off-diagonal)  
✅ High alignment between Hanford and Virgo; minor skew at Livingston.

---

### GW190521_030229

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0358       | ±0.00289       |
| Livingston | 0.0150       | ±0.00114       |
| Virgo      | 0.0100       | ±0.00083       |

**∆ Max** ≈ 0.0258 (diagonal), 0.00206 (off-diagonal)  
⚠️ Strong gradient present; Hanford likely sampled symbolic curvature spike.

---

### GW190727_060333

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0100       | ±0.00086       |
| Livingston | 0.0150       | ±0.00116       |
| Virgo      | 0.0200       | ±0.00034       |

**∆ Max** ≈ 0.01 (diagonal), 0.0015 (off-diagonal)  
⚠️ Suggests symbolic curvature asymmetry particularly between Livingston and Virgo.

---

### GW190828_065509

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0200       | ±0.00020       |
| Livingston | 0.0889       | ±0.00522       |
| Virgo      | 0.0100       | ±0.00085       |

**∆ Max** ≈ 0.0789 (diagonal), 0.00607 (off-diagonal)  
⚠️ Significant symbolic curvature divergence at Livingston; supports path dependency hypothesis.

---

### GW190929_012149

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0402       | ±0.00021       |
| Livingston | 0.0705       | ±0.00578       |
| Virgo      | 0.0100       | ±0.00084       |

**∆ Max** ≈ 0.0605 (diagonal), 0.00599 (off-diagonal)  
⚠️ Strong divergence between Livingston and other detectors.

---

### GW190930_133541

| Detector   | Diagonal Avg | Max Skew Term |
|------------|--------------|----------------|
| Hanford    | 0.0100       | ±0.00086       |
| Livingston | 0.0150       | ±0.00105       |
| Virgo      | 0.0150       | ±0.00008       |

**∆ Max** ≈ 0.005 (diagonal), 0.00113 (off-diagonal)  
✅ Well-aligned diagonals; minor skew suggests local field distortion.

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

In control events like GW170817, heatmaps should be mostly faint. In divergent events (e.g., GW170814), you'll observe strong skew terms and magnitude gaps.

---

## 📜 Citation / Credit

This project is part of ongoing research into the Omega Time Rotation (OTR) framework, developed by [Juan Hua Xu](https://github.com/JuanHuaXu) and collaborators.

---

## 📜 License

MIT License. See `LICENSE` file.

