import numpy as np

def spherical_dist(pos1, pos2, r=3958.75):
    pos1 = pos1 * np.pi / 180
    pos2 = pos2 * np.pi / 180
    cos_lat1 = np.cos(pos1[..., 0])
    cos_lat2 = np.cos(pos2[..., 0])
    cos_lat_d = np.cos(pos1[..., 0] - pos2[..., 0])
    cos_lon_d = np.cos(pos1[..., 1] - pos2[..., 1])
    return r * np.arccos(cos_lat_d - cos_lat1 * cos_lat2 * (1 - cos_lon_d))


cities = [line.rstrip('\n') for line in open('nhl_geocoded.dat')]
coords = np.array([[float(x) for x in c.split(',')] for c in cities])

distmat = spherical_dist(coords[:, None], coords)
with open('nhl_distmatrix.csv', 'w') as f:
    f.write("\n".join(",".join(map(str, x)) for x in distmat))
