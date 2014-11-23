#!/usr/bin/python
# Filename: lines.py
# Author: sakeven(https://github.com/sakeven/)
#   Copyright (C) 2014  sakeven
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import sys


def walk_dir(path):
    cnt = 0

    for root, dirs, files in os.walk(path):
        for filename in files:
            ext = os.path.splitext(filename)[1][1:]
            if ext == suffix:
                print root + '/' + filename
                f = file(root + '/' + filename, 'r')
                for line in f:
                    cnt += 1
                f.close()

    return cnt

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print 'argv error!\nusage: lines.py extensions [project_path]'
        exit()
    global suffix
    suffix = sys.argv[1]
    path = '.'
    if len(sys.argv) > 2:
        path = sys.argv[2]
    print suffix, path
    print walk_dir(path), 'lines in total!'
