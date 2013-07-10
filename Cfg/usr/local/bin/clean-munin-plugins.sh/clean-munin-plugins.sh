#!/bin/sh
# This file is managed by Bcfg2. Any local change will be lost.

if [ -f "/etc/munin/cleaned-plugins" ];then
    exit 0
fi

# Make sur the package was installed
dpkg -s munin-node > /dev/null 2>&1
if [ "$?" -eq "0" ];then

    # Clean all Munin plugins
    rm -rf /etc/munin/plugins/*

    echo "# Do not remove, this file is used by Bcfg2" > /etc/munin/cleaned-plugins

fi

exit 0
