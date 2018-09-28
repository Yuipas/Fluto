#!/usr/bin/env python3

from trans import MODULES

def removeComments(raw):

    commentLine = False
    commentWord = False
    commentMult = False

    inString = False

    newCont = []

    for line in raw.readlines():

        nline = ''

        commentLine = False
        commentWord = False

        # remove unnecesary newlines
        if line.endswith('\n'):
            line = line[:-1]

        for i in range(len(line)):
            char = line[i]

            if commentLine:
                break
            elif commentWord:
                if char == ' ' or char == '\t':
                    commentWord = False
                continue
            elif commentMult:
                if i >= 2 and line[i - 2] == '-' and line[i - 1] == '-' and char == '>':
                    commentMult = False
                continue

            if char == '\'' or char == '"' and i != 0 and line[i-1] == '\\':
                inString = not inString
            elif inString == False:

                if char == '#':
                    commentLine = True
                    continue
                elif char == '-' and line[i + 1] == '-':
                    commentWord = True
                    continue
                elif char == '<' and line[i + 1] == '-' and line[i + 2] == '-':
                    commentMult = True
                    continue

            nline += char

        newCont.append(nline)

    return newCont

def toTokens(lines):
    pass


def toExe(lines):

    cmds = []
    command = []


    return cmds
