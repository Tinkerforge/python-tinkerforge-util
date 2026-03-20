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
import subprocess
import collections

NotifyContext = collections.namedtuple('NotifyContext', 'title icon_path id_')


def notify(title, message, icon_path=None):
    version = [int(x) for x in re.search(r'(\d+)\.(\d+)\.(\d+)', subprocess.check_output(['notify-send', '--version'], text=True)).groups()]
    args = ['notify-send']

    if version >= [0, 8, 0]:
        args += ['-p']

    args += ['-t', '3600000']

    if icon_path != None:
        args += ['-i', icon_path]

    args += [title, message]

    id_ = subprocess.check_output(args, text=True).strip()

    if version >= [0, 8, 0]:
        return NotifyContext(title, icon_path, id_)

    return None


def notify_clear(ctx):
    if ctx == None:
        return

    args = ['notify-send', '-r', ctx.id_, '-t', '1']

    if ctx.icon_path != None:
        args += ['-i', ctx.icon_path]

    args += [ctx.title, 'clear']

    subprocess.check_call(args)
