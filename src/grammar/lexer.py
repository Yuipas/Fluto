EOF = "EOF"
NUMBER = "NUMBER"
PLUS, MINUS, MULT, DIV = "PLUS", "MINUS", "MULT", "DIV"
SIGNS = ("+", "-", "*", "/")

class Lexer(object):

    def __init__(self, text):

        self.script = text
        self.position = 0
        self.currentChar = self.script[self.position]


    def error(self, why = 'Invalid character'):
        raise Exception('Exception ({})'.format(why))

    def advance(self):
        """Advance in self.script"""

        self.position += 1

        if self.position < len(self.script):
            self.currentChar = self.script[self.position]
        else:
            self.currentChar = None

    def getNum(self):
        """Return a (multidigit/float/int) number consumed from the input."""

        num = ""

        while self.currentChar is not None and (self.currentChar.isdigit() or self.currentChar == '.'):
            num += self.currentChar
            self.advance()

        return num


    def nextToken(self):
        """Lexical analyzer

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """

        while self.currentChar is not None:

            if self.currentChar.isspace():
                self.advance()
                continue

            if self.currentChar.isdigit():
                return Token(NUMBER, self.getNum()) # from token.py

            if self.currentChar in SIGNS:
                if self.currentChar == '+':
                    self.advance()
                    return Token(PLUS, "+")
                elif self.currentChar == '-':
                    self.advance()
                    return Token(MINUS, "-")
                elif self.currentChar == '*':
                    self.advance()
                    return Token(MULT, "*")
                elif self.currentChar == '/':
                    self.advance()
                    return Token(DIV, "/")


            self.error("Unrecognized / invalid character: " + str(self.currentChar))

        return Token(EOF, None)
