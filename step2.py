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

# Create a list of random points with a bounding box around the [0, 0] point
point_list = []
for i in range(10):
    p = gs.utils.generate_random("Point", boundingBox=[-1.4, -1.4, 1.4, 1.4])
    point_list.append(p)

mp = gs.geometry.MultiPoint(point_list)
mp_json = gs.dumps(mp, sort_keys=True, indent=4)
print(mp_json)
