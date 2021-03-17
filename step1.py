import geojson as gs

# Create a Point with some arbitrary coordinates
p1 = gs.Point((-100.8, 45.24))
print(type(p1))

# Create a geojson representation of that point
# Note the sorting of keys and indentation choice
p1_json = gs.dumps(p1, sort_keys=True, indent=4)
print(p1_json)
