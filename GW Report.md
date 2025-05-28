# Gravitational Wave Detection Residual Report

## Title

**Symbolic Curvature Residual Analysis of GW Events Using OTR-Derived Tensors**

## Objective

This project evaluates discrepancies between gravitational wave detections across multiple observatories using symbolic curvature tensors derived from Omega Time Rotation (OTR) principles. Unlike the broader Mutual Entanglement Substrate Theory (MEST), this tool does not aim to validate or implement full OTR. Instead, it uses symbolic tensor differentials as a diagnostic lens to assess detection congruence and potential signal distortion.

## Background on OTR

Omega Time Rotation (OTR) is a symbolic framework proposing that gravity emerges from the collective exclusion and confinement behavior of fermionic matter, forming rotationally anisotropic structures in spacetime. It treats gravitational wells not as smooth scalar deformations but as dynamic whirlpools in symbolic curvature space. This framing introduces detectable directional and amplitude perturbations in the propagation of signals such as gravitational waves (GWs), particularly at the interface of dense geophysical structures.

While OTR is not a replacement for general relativity (GR), it provides a tractable symbolic framework for exploring effects that GR accommodates but typically ignores due to computational complexity. Notably, GR does not forbid the existence of whirlpool-like structures in gravitational wells; rather, it is the convention of treating these wells as smooth that has limited exploration in this direction. We aim to challenge this assumption by demonstrating that non-smooth curvature features can meaningfully distort GW signals.

In this project, OTR is not applied in its full field-theoretic formulation but instead serves as a basis for constructing symbolic curvature tensors. These tensors encode localized structure in the signal paths to detectors and allow us to probe discrepancies in detection timing or shape. In this role, OTR operates strictly as a geometric diagnostic tool to evaluate detection coherence.

## Methodology

We compute curvature tensors symbolically traced along geodesics from astrophysical event coordinates to each gravitational wave detector (Hanford, Livingston, Virgo). The symbolic curvature is influenced by geospatial coordinates, depth, and optional modeling layers:

* **PREM weighting** for geophysical structure.
* **Symbolic dynamo weighting** (optional) to simulate geoelectromagnetic convection effects.
* **Legacy mode** for baseline comparison without weighting layers.

## Key Features

* Computes full 3×3 symbolic curvature tensor per detector.
* Supports legacy mode to reproduce pre-PREM behavior.
* Residuals calculated pairwise across detectors to identify structural disagreement.
* Exports both `.npy` and `.txt` tensor and residual files.

## Usage

```bash
python compare_detectors.py \
  --ra 201.37 \
  --dec -44.79 \
  --timestamp "2017-08-14T10:30:43" \
  --prefix ./output/GW170814/GW170814 \
  --legacy-symbolic \
  --dynamo-aware
```

## Interpretation

Tensor deltas are examined for amplitude and directional coherence. Significant disparities may suggest:

* Detector misalignment or sensitivity bias
* Localized geophysical curvature impact
* Residual symbolic distortion in the signal path

These findings are especially relevant in the context of events where detector agreement is partial or inconsistent. Symbolic curvature residuals derived from OTR help model how signal path interactions—such as through dynamic gravitational wells—could alter waveform features en route.

## Output Format

Each run produces:

* `<prefix>_<detector>_tensor.npy`
* `<prefix>_<detector>_tensor.txt`
* `<prefix>_delta_<detector1>_<detector2>.npy`
* `<prefix>_delta_<detector1>_<detector2>.txt`

## Status

All symbolic differential tensors are computed in real units. Precision is set to `%.8e` to ensure numerical transparency. This project is not intended to derive cosmological conclusions but to provide diagnostic insight into tensor residual behavior under OTR curvature models.

## Repository

[https://github.com/JuanHuaXu/GW\_OTR](https://github.com/JuanHuaXu/GW_OTR)

This project is standalone; not part of the MEST framework. It utilizes symbolic OTR mechanisms purely as a comparative diagnostic framework for evaluating gravitational wave detection coherence.

---

For further theoretical background on OTR or symbolic curvature tracing, please consult the internal OTR documentation or reach out to the framework maintainers.

