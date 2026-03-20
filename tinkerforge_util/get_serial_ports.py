#
# Tinkerforge Util
# Copyright (C) 2026 Matthias Bolte <matthias@tinkerforge.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
#

import collections
from tinkerforge_util.base58 import base58_encode

SerialPort = collections.namedtuple('SerialPort', 'path description uid opaque')


def get_serial_ports(vid=None, pid=None, opaque=None):
    # import serial.tools.list_ports only if the function is actually use to avoid
    # importing it for nothing on system that might not have serial.tools.list_ports
    import serial.tools.list_ports

    ports = []

    for info in serial.tools.list_ports.comports():
        if info.vid == None or info.pid == None:
            continue  # ignore non-USB based serial ports

        if vid != None and info.vid != vid:
            continue  # no VID match

        if pid != None and info.pid != pid:
            continue  # no PID match

        path = info.device
        description = info.device
        uid = None

        if info.serial_number == None:
            serial_number = ''
        else:
            serial_number = info.serial_number.lower()  # ignore case, because Windows reports the serial number as all uppercase

        if info.vid == 0x10c4 and info.pid == 0xea60 and serial_number.startswith('tinkerforge_'):
            parts = serial_number.split('_')
            product_name = ' '.join([x.capitalize() for x in parts[1:-2]]).replace('Esp32', 'ESP32')
            uid = base58_encode(int(parts[-1]))
            description += f' - {product_name} [{uid}]'
        elif info.description != 'n/a' and info.description != info.name:
            if info.description == 'RED Brick - CDC Abstract Control Model (ACM)':
                description += ' - RED Brick (ACM)'
            else:
                description += f' - {info.description}'

        ports.append(SerialPort(path, description, uid, opaque))

    return ports
