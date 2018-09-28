t = 'global path\n'
a = 'path = path + ", {}"'
r = 'path = path[:-2]'

path = 'g'

MODULES = {
    '(': t + a.format('('),  # open parentesis
    '[': t + a.format('['),  # open array
    '{': t + a.format('{'),  # open bracket
    ')': t + r,              # close parentesis
    ']': t + r,              # close array
    '}': t + r,              # close bracket
    '!': t + a.format('!'),  # not
    '<': t + a.format('<'),  # less
    '>': t + a.format('>'),  # greater
    '=': t + a.format('='),  # equals
    '+': t + a.format('+'),  # plus
    '-': t + a.format('-'),  # minus
    '*': t + a.format('*'),  # multiply
    '/': t + a.format('/'),  # divide
    '.': t + a.format('.'),  # dot
    "'": t + a.format("'"),  # string
    # '"': t + a.format('"'),  # string2
    # ',': t + a.format(','),  # coma
    '$': t + a.format('$'),  # unknown
    '~': t + a.format('~'),  # access arguments
    '@': t + a.format('@'),  # literal mode
    '?': t + a.format('?'),  # option choose
    '&': t + a.format('&'),  # and
    '|': t + a.format('|'),  # or
    '=>': t + a.format('f') # arrow function
}
    # 'and': t + a.format('&'),
    # 'or',

del t, r, a

def toTokens(content):
    tokens = []
    token = ''

    path = ''
    isCommentLine = False
    isCommentWord = False
    isCommentMult = False

    length = len(content)
    for int in range(length):
        char = content[int]

        # avoid comments (# line) (-- word) (<-- multiline -->)
        if isCommentLine or isCommentWord or isCommentMult:
            if char == ' ' or char == ',':
                isCommentWord = False
            if content[int-2] == '-' and content[int-1] == '-' and char == '>':
                isCommentMult = False
            if char == '\n':
                isCommentLine = False
            continue
        else:
            if char == '#':
                isCommentLine = True
            elif char == '-' and content[int+1] == '-':
                isCommentWord = True
            elif char == '<' and content[int+1] == '-' and content[int+2] == '-':
                isCommentMult = True
            elif char == ' ' or char == '\n' or char in MODULES:
                if not token == '':
                    tokens.append(token)
                token = ''
                if char in MODULES:
                    tokens.append(char)
            # elif not char == ';':
            else:
                if char == ';':
                    tokens.append(token)
                    tokens.append(char)
                    token = ''
                else: token = token + char
    return tokens


def execute(token):
    pass


def getPath(token):

    if token in MODULES:
        exec(MODULES[token])
    else:
        raise TypeError('PEDANTE: ' + token)

    return path
