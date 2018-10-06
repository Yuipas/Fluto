from grammar import tokens

class Lexer(object):

    def __init__(self, text):

        self.text = text
        self.pos = 0
        self.currentChar = text[self.pos]


    def error(self, ms = ""):
        raise Exception(ms)

    def advance(self):
        self.pos = self.pos + 1

        if self.pos < len(self.text):
            self.currentChar = self.text[self.pos]
        else:
            self.currentChar = None

    def number(self):
        """Return a number (multidigit, float, integer)"""
        n = ""
        while self.currentChar is not None and (self.currentChar.isdigit() or self.currentChar == '.'):
            n += self.currentChar
            self.advance()
        return float(n)

    def nextToken(self):
        """Analyze text looking for next token."""

        while self.currentChar is not None:

            if self.currentChar.isspace():
                self.advance()
                continue

            if self.currentChar.isdigit():
                token = tokens.Token(tokens.NUMBER, self.number())
                return token

            if self.currentChar == '+':
                token = tokens.Token(tokens.PLUS, "+")
                self.advance()
                return token

            if self.currentChar == '-':
                token = tokens.Token(tokens.MINUS, "-")
                self.advance()
                return token

            if self.currentChar == '*':
                token = tokens.Token(tokens.MULT, "*")
                self.advance()
                return token

            if self.currentChar == '/':
                token = tokens.Token(tokens.DIV, "/")
                self.advance()
                return token

            if self.currentChar == '(':
                token = tokens.Token(tokens.POPEN, "(")
                self.advance()
                return token

            if self.currentChar == ')':
                token = tokens.Token(tokens.PCLOSE, ")")
                self.advance()
                return token

            self.error("Unknown: character '{CHAR}'".format(CHAR = self.currentChar))

        return tokens.Token(tokens.EOF, None)
