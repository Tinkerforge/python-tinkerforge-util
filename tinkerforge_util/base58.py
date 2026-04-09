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

BASE58_ALPHABET = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'


def base58_encode(value):
    encoded = ''

    while value >= 58:
        div, mod = divmod(value, 58)
        encoded = BASE58_ALPHABET[mod] + encoded
        value = div

    return BASE58_ALPHABET[value] + encoded


def base58_decode(encoded):
    value = 0
    column_multiplier = 1

    for c in encoded[::-1]:
        try:
            column = BASE58_ALPHABET.index(c)
        except ValueError:
            raise Exception(f'Invalid character {repr(c)} in {repr(encoded)}')

        value += column * column_multiplier
        column_multiplier *= 58

    return value
