import numpy as np
from scipy.spatial.transform import Rotation as R
from scipy.interpolate import RegularGridInterpolator
from astropy.coordinates import EarthLocation, SkyCoord, AltAz
from astropy.time import Time
import astropy.units as u
from scipy.interpolate import interp1d

# Load PREM500 data (columns: radius, density, ...)
prem_data = np.genfromtxt('PREM500.csv', delimiter=',', skip_header=1)
radius_km = prem_data[:, 0] / 1000  # Convert to km
density = prem_data[:, 1]  # kg/m^3

# Interpolation function for density
density_interp = interp1d(radius_km[::-1], density[::-1], kind='cubic', bounds_error=False, fill_value="extrapolate")

def path_weighted_kernel(lat, lon, elev, ra, dec, timestamp, steps=100):
    """
    Compute PREM-weighted symbolic curvature accumulation along the GW path.
    """
    location = EarthLocation(lat=lat*u.deg, lon=lon*u.deg, height=elev*u.m)
    obstime = Time(timestamp)
    skycoord = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
    altaz = skycoord.transform_to(AltAz(obstime=obstime, location=location))

    # Path direction vector
    az_rad = altaz.az.rad
    alt_rad = altaz.alt.rad
    direction = np.array([
        np.cos(alt_rad) * np.sin(az_rad),
        np.cos(alt_rad) * np.cos(az_rad),
        np.sin(alt_rad)
    ])

    # Normalize direction
    direction /= np.linalg.norm(direction)

    # Path tracing: from ~20000 km above surface down to -6000 km
    path_length_km = 26000
    start_pos = np.array([0, 0, 6371 + path_length_km])  # Earth center at origin, starting above surface
    dz = -path_length_km / steps

    curvature_accum = np.zeros((3, 3))

    for step in range(steps):
        pos = start_pos + step * dz * direction  # km
        radius_from_center = np.linalg.norm(pos)
        r_km = radius_from_center

        # Get density at this radius
        rho = density_interp(r_km)

        # Define a synthetic kernel as a diagonal tensor scaled by density
        kernel = rho * np.eye(3)

        curvature_accum += kernel * abs(dz)

    return curvature_accum / steps

# Load symbolic curvature field
symbolic_tensor = np.load("symbolic_curvature_tensor.npy")

# Grid axes
lat_axis = np.arange(-90, 91, 1)
lon_axis = np.arange(-180, 181, 1)
depth_axis = np.array([0, 50, 100, 200, 500, 1000, 2000, 2890])  # km

# Create interpolators for each component of 3x3 tensor
interpolators = {}
for i in range(3):
    for j in range(3):
        interpolators[(i, j)] = RegularGridInterpolator(
            (lat_axis, lon_axis, depth_axis),
            symbolic_tensor[..., i, j],
            bounds_error=False, fill_value=0
        )

def get_symbolic_tensor(lat, lon, depth):
    """Interpolates the symbolic curvature tensor at a point"""
    point = np.array([lat, lon, depth]).reshape(1, -1)  # Force 2D input
    return np.array([[interpolators[(i, j)](point)[0] for j in range(3)] for i in range(3)])

def trace_path(ra, dec, lat, lon, elev, timestamp, steps=100):
    """
    Wrapper function for symbolic curvature tensor computation using PREM-based kernel.
    Signature matches the original trace_path function used in comparison scripts.
    """
    tensor = path_weighted_kernel(lat, lon, elev, ra, dec, timestamp, steps)
    return tensor, None  # Maintains compatibility with code expecting (tensor, path)

