import geojson as gs
import math

# Create a LineString object

dr = 0.03
dth = 0.3
r0 = 0.1
theta0 = -1
coords = []
for j in range(10):
    theta = theta0 + j * dth
    r = r0 + j * dr
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    coords.append((x, y))

ls1 = gs.geometry.LineString(coords)

# Create a displaced copy of the LineString

coords = gs.utils.coords(ls1)
new_coords = []
for tuple in coords:
    new_coords.append((tuple[0], tuple[1]+0.1))

ls2 = gs.geometry.LineString(new_coords)

# Create a Multistring object

ml = gs.geometry.MultiLineString([ls1, ls2])
ml_json = gs.dumps(ml, sort_keys=True, indent=4)
print(ml_json)
