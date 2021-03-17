import geojson as gs

# Create a list of random points with a bounding box around the [0, 0] point
point_list = []
for i in range(10):
    p = gs.utils.generate_random("Point", boundingBox=[-1.4, -1.4, 1.4, 1.4])
    point_list.append(p)

mp = gs.geometry.MultiPoint(point_list)
mp_json = gs.dumps(mp, sort_keys=True, indent=4)
print(mp_json)
