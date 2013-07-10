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

try:
    from configparser import ConfigParser
except ImportError:  # pragma: no cover
    from ConfigParser import ConfigParser

import os


def parse_config(path):
    config = {}

    configp = ConfigParser()
    try:
        configp.read(path)
    except:
        return config

    for section in configp.sections():
        config_section = {}
        for option in configp.options(section):
            value = configp.get(section, option)
            if "," in value:
                value = [entry.strip('"').strip()
                         for entry in value.split(",")]
            else:
                value = value.strip('"').strip()
            config_section[option] = value
        config[section] = config_section

    return config


def get_config_section(bundle, section):
    config = parse_config(os.path.join("/var/lib/bcfg2/etc/",
                                       "%s.ini" % bundle))
    return config[section]
