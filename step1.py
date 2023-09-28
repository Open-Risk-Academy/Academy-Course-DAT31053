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

# Create a Point with some arbitrary coordinates
p1 = gs.Point((-100.8, 45.24))
print(type(p1))

# Create a geojson representation of that point
# Note the sorting of keys and indentation choice
p1_json = gs.dumps(p1, sort_keys=True, indent=4)
print(p1_json)
