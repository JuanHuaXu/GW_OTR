import gw_path_tracer
from gw_path_tracer import trace_path

ra = 197.45        # RA of GW170817 (degrees)
dec = -23.38       # Dec of GW170817
lat = 46.45        # Virgo
lon = 10.5
elev = 0.25        # km
timestamp = "2017-08-17T12:41:04"

skew_tensor, path = trace_path(ra, dec, lat, lon, elev, timestamp)
print("Symbolic curvature accumulated:")
print(skew_tensor)

