EOF = "EOF" # EOF = EndOfFile
NUMBER = "NUMBER"
PLUS, MINUS = "PLUS", "MINUS"
MULT, DIV = "MULT", "DIV"
POPEN, PCLOSE = "POPEN", "PCLOSE"

class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "{TYPE}: '{VALUE}'".format(TYPE = self.type, VALUE = self.value)

    __repr__ = __str__
