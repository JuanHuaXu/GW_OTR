import argparse
import numpy as np
from gw_path_tracer import trace_path

# Detector info: (Name, Latitude, Longitude, Elevation in km)
DETECTORS = {
    "Hanford":    (46.455, -119.408, 0.142),
    "Livingston": (30.563, -90.774, 0.010),
    "Virgo":      (43.631, 10.504, 0.030)
}

def main(ra, dec, timestamp, output_prefix="GW"):
    print(f"\nComputing symbolic curvature tensors for {output_prefix}...\n")

    tensors = {}

    for name, (lat, lon, elev) in DETECTORS.items():
        print(f"→ {name}")
        tensor, _ = trace_path(ra, dec, lat, lon, elev, timestamp)
        tensors[name] = tensor
        print(np.round(tensor, 6), "\n")

        np.save(f"{output_prefix}_{name}_tensor.npy", tensor)
        np.savetxt(f"{output_prefix}_{name}_tensor.txt", tensor, fmt="%.8e")

    # Pairwise residuals
    def tensor_diff(A, B):
        return A - B

    print("\nResiduals (Tensor Differences):\n")
    pairs = [("Hanford", "Livingston"), ("Hanford", "Virgo"), ("Livingston", "Virgo")]

    for a, b in pairs:
        diff = tensor_diff(tensors[a], tensors[b])
        print(f"Δ {a} – {b}:\n", np.round(diff, 8), "\n")
        np.save(f"{output_prefix}_delta_{a}_{b}.npy", diff)
        np.savetxt(f"{output_prefix}_delta_{a}_{b}.txt", diff, fmt="%.8e")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Symbolic curvature tensor analysis for gravitational wave events.")
    parser.add_argument("--ra", type=float, required=True, help="Right ascension (deg)")
    parser.add_argument("--dec", type=float, required=True, help="Declination (deg)")
    parser.add_argument("--timestamp", type=str, required=True, help="UTC timestamp (e.g., '2017-08-17T12:41:04')")
    parser.add_argument("--prefix", type=str, default="GW", help="Output file prefix")

    args = parser.parse_args()
    main(args.ra, args.dec, args.timestamp, args.prefix)

