#!/usr/bin/env python3

from sys import argv as arguments
from trans import util2 as util

translatedFile = open('.compiled.py', 'a+')

with open(arguments[1], 'r') as file:

    lines = util.removeComments(file)
    cmds = util.toExe(lines)

    #for l in lines:
    #    print(l)
    # commands = util.toExe()
