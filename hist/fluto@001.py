#############
##  TOKEN  ##
#############

class Token(object):


    def __init__(self, type, value):

        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(type = self.type, value = repr(self.value))

    __repr__ = __str__



#############
##  LEXER  ##
#############


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





###################
##  Interpreter  ##
###################

class Interpreter(object):

    def __init__(self, lexer):

        self.currentToken = lexer.nextToken()
        self.lexer = lexer

    def error(self, why = 'Invalid syntax'):
        raise Exception('Exception ({})'.format(why))


    def eat(self, types):

        if type(types) == str:
            if self.currentToken.type == types:
                self.currentToken = self.lexer.nextToken()
        elif self.currentToken.type in types:
            self.currentToken = self.lexer.nextToken()
        else:
            self.error("Expected {exp}, recived {rec}".format(exp = types, rec = self.currentToken.type))

    def getTerm(self):
        token = self.currentToken
        self.eat(NUMBER)
        return token


    def expr(self):

        result = float(self.getTerm().value)

        while self.currentToken.type is not EOF:

            if self.currentToken.type is PLUS:
                self.eat(PLUS)
                term = float(self.getTerm().value)
                result = result + term

            elif self.currentToken.type is MINUS:
                self.eat(MINUS)
                term = float(self.getTerm().value)
                result = result - term
            elif self.currentToken.type is MULT:
                self.eat(MULT)
                term = float(self.getTerm().value)
                result = result * term
            elif self.currentToken.type is DIV:
                self.eat(DIV)
                term = float(self.getTerm().value)
                result = result / term


        return result

############
##  Main  ##
############

def main():

    while True:
        code = input('!> ')

        if not code:
            continue

        fluto_lexer = Lexer(code)
        fluto_interpreter = Interpreter(fluto_lexer)
        result = fluto_interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
