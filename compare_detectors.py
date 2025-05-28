import argparse
import numpy as np
from astropy.coordinates import EarthLocation
from datetime import datetime
from gw_path_tracer import trace_path, trace_path_legacy


def dynamo_weight(lat, lon, depth_km, time):
    """
    Simple symbolic dynamo weight model:
    - Uses sinusoidal lat-long dependence to mimic core convection rolls.
    - Applies depth damping and daily magnetic variation modulated by time.
    """
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    t = datetime.fromisoformat(time).timestamp()  # seconds since epoch

    # Simulate magnetic dipole component and variation
    magnetic_variation = np.sin(lat_rad) * np.cos(2 * lon_rad + t * 1e-5)
    depth_decay = np.exp(-depth_km / 1000.0)  # decay with depth
    return 1 + 0.01 * magnetic_variation * depth_decay


def compare_event(event_ra, event_dec, timestamp, prefix, use_prem=True, use_dynamo=False):
    detectors = {
        "Hanford": EarthLocation(lat=46.455, lon=-119.408, height=142.554),
        "Livingston": EarthLocation(lat=30.563, lon=-90.774, height=-6.574),
        "Virgo": EarthLocation(lat=43.63, lon=10.5, height=51.884),
    }

    tensors = {}
    for name, loc in detectors.items():
        lat = loc.lat.deg
        lon = loc.lon.deg
        depth_km = loc.height.to_value('km')

        if use_prem:
            tensor, _ = trace_path(event_ra, event_dec, lat, lon, depth_km, timestamp)
        else:
            tensor, _ = trace_path_legacy(event_ra, event_dec, lat, lon, depth_km, timestamp)

        if use_dynamo:
            weight = dynamo_weight(lat, lon, depth_km, timestamp)
            tensor *= weight

        tensors[name] = tensor
        print(f"\n→ {name}")
        print(np.round(tensor, 6))
        np.save(f"{prefix}_{name}_tensor.npy", tensor)
        np.savetxt(f"{prefix}_{name}_tensor.txt", tensor, fmt="%.8e")

    # Compute residuals
    names = list(tensors.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            A, B = names[i], names[j]
            delta = np.round(tensors[A] - tensors[B], 8)
            print(f"\n∆ {A} – {B}:")
            print(delta)
            np.save(f"{prefix}_delta_{A}_{B}.npy", delta)
            np.savetxt(f"{prefix}_delta_{A}_{B}.txt", delta, fmt="%.8e")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ra", type=float, required=True, help="RA of the GW source")
    parser.add_argument("--dec", type=float, required=True, help="Dec of the GW source")
    parser.add_argument("--timestamp", type=str, required=True, help="UTC timestamp of the GW event")
    parser.add_argument("--prefix", type=str, required=True, help="Output file prefix")
    parser.add_argument("--legacy-symbolic", action="store_true", help="Disable PREM weighting")
    parser.add_argument("--dynamo-aware", action="store_true", help="Apply symbolic dynamo field adjustment")
    args = parser.parse_args()

    print(f"\nComputing symbolic curvature tensors for {args.prefix}...\n")
    compare_event(
        args.ra,
        args.dec,
        args.timestamp,
        args.prefix,
        use_prem=not args.legacy_symbolic,
        use_dynamo=args.dynamo_aware
    )

