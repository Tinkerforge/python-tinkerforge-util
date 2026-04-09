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

import re

__all__ = [
    'none',
    'bold',
    'underline',
    'blink',
    'red',
    'green',
    'yellow',
    'blue',
    'purple',
    'cyan',
    'gray',
    'strip',
]


def _colored(color, *args):
    return '\x1b[{0}m{1}\x1b[0m'.format(color, ' '.join([str(arg) for arg in args]))


def none(*args):
    return ' '.join([str(arg) for arg in args])


def bold(*args):
    return _colored('1', *args)


def underline(*args):
    return _colored('4', *args)


def blink(*args):
    return _colored('5', *args)


def red(*args, bold=True):
    return _colored('1;31' if bold else '31', *args)


def green(*args, bold=True):
    return _colored('1;32' if bold else '32', *args)


def yellow(*args, bold=True):
    return _colored('1;33' if bold else '33', *args)


def blue(*args, bold=True):
    return _colored('1;34' if bold else '34', *args)


def purple(*args, bold=True):
    return _colored('1;35' if bold else '35', *args)


def cyan(*args, bold=True):
    return _colored('1;36' if bold else '36', *args)


def gray(*args, bold=True):
    return _colored('1;90' if bold else '90', *args)


def strip(value):
    return re.sub(rf'{"\x1b"}\[(1;)?\d+m', '', value)


def findall(value):
    colors = {
        '31': 'red',
        '32': 'green',
        '33': 'yellow',
        '34': 'blue',
        '35': 'purple',
        '36': 'cyan',
        '90': 'gray',
    }

    result = []

    for m in re.findall(rf'{"\x1b"}\[(?:1;)?(\d+)m', value):
        color = colors.get(m)

        if color != None and color not in result:
            result.append(color)

    return list(result)
