#!/usr/bin/python
# Filename: lines.py

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
        print 'argv error!\nuseage: python lines.py extionsions [path]'
        exit()
    global suffix
    suffix = sys.argv[1]
    path = '.'
    if len(sys.argv) > 2:
        path = sys.argv[2]
    print suffix, path
    print walk_dir(path), 'lines in total!'
