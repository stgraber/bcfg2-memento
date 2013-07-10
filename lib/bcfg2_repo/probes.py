# Written by Stephane Graber <stgraber@ubuntu.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from genshi.template import TemplateError


def get_probe_as_dict(metadata, probe):
    if probe not in metadata.Probes:
        raise TemplateError("Missing result for probe: %s" % probe)

    values = {}
    for value in metadata.Probes[probe].strip().split(","):
        parts = value.split("=", 1)
        if len(parts) < 2:
            continue

        values[parts[0]] = parts[1]

    return values
