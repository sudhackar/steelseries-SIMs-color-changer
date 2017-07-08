#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  change.py
#
#  Copyright 2017 payatu <sudhakar@payatu>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import hid
from tkcolorpicker import askcolor


def set_color(device, r, g, b):
    device.set_nonblocking(1)

    device.write([0x01, 0x00, 0x95, 0x02, 0x80, 0xbf, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    device.write([0x01, 0x00, 0x80, 0x02, 0x52, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    device.write([0x01, 0x00, 0x83, 0x03, r, g, b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    device.write([0x01, 0x00, 0x93, 0x02, 0x03, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])


def main(args):
    print "Opening device"
    try:
        device = hid.device(0x1038, 0x1222)
    except IOError:
        print "Device missing"
        return
    try:
        ((r, g, b), html) = askcolor(title="Choose the color you want on your headphones")
    except TypeError:
        print "Window closed"
        return
    set_color(device, r, g, b)
    device.close()
    print "Color written"
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
