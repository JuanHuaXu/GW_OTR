import numpy as np

# Earth grid resolution
LAT_RES = 1      # degrees
LON_RES = 1      # degrees
DEPTH_LEVELS = [0, 50, 100, 200, 500, 1000, 2000, 2890]  # in km (up to core-mantle boundary)

# Grid dimensions
latitudes = np.arange(-90, 91, LAT_RES)
longitudes = np.arange(-180, 181, LON_RES)
depths = np.array(DEPTH_LEVELS)

# Initialize curvature tensor grid: shape = [lat, lon, depth, 3x3]
symbolic_curvature = np.zeros((len(latitudes), len(longitudes), len(depths), 3, 3))

# Simplified symbolic exclusion profile by depth (tunable)
def exclusion_density(depth_km):
    if depth_km < 100:
        return 1.0  # crust
    elif depth_km < 500:
        return 3.0  # mantle transition
    elif depth_km < 2000:
        return 5.0  # lower mantle
    else:
        return 8.0  # near core

# Populate curvature tensor field
for i, lat in enumerate(latitudes):
    for j, lon in enumerate(longitudes):
        for k, depth in enumerate(depths):
            rho_ex = exclusion_density(depth)
            rot_term = np.sin(np.radians(lat)) * rho_ex * 0.1  # symbolic whirlpool proxy

            # Build a toy symbolic tensor
            S = np.array([
                [rho_ex,      0,       rot_term],
                [0,       rho_ex,     -rot_term],
                [rot_term, -rot_term, rho_ex]
            ])
            symbolic_curvature[i, j, k] = S

# Save tensor field to disk
np.save("symbolic_curvature_tensor.npy", symbolic_curvature)
print("✅ Symbolic curvature tensor saved. Shape:", symbolic_curvature.shape)

