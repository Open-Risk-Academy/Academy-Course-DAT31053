# (c) 2019 - 2023 Open Risk (https://www.openriskmanagement.com)
#
# This code is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of the course. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

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
