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

import glob
import os

from genshi.template import TemplateError


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


def get_config_section(repo, metadata, bundle, section):
    path = os.path.join(repo, "etc", "%s.ini" % bundle)

    if not os.path.exists(path):
        raise TemplateError("Missing config file: %s" % path)

    paths = [path]

    for conffile in sorted(glob.glob("%s.G*" % path)):
        try:
            group = conffile.split(".G")[-1].split("_", 1)[-1]
        except:
            # Invalid filename syntax
            continue

        if group in metadata.groups:
            paths.append(conffile)

    if os.path.exists("%s.H_%s" % (path, metadata.hostname)):
        paths.append("%s.H_%s" % (path, metadata.hostname))

    config = {}
    for entry in paths:
        conf = parse_config(entry)
        if section not in conf:
            continue

        config.update(conf[section])

    if not config:
        raise TemplateError("Missing config section: %s" % section)

    return config
