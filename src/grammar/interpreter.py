from grammar import ( # weird things happen in python
    lexer,
    tokens
)

class Interpreter(object):

    def __init__(self, lexer):

        self.currentToken = lexer.nextToken()
        self.lexer = lexer

    def error(self, msg = ""):
        raise Exception(msg)

    def eat(self, tokenType):
        if self.currentToken.type is tokenType:
            self.currentToken = self.lexer.nextToken()
        else:
            self.error("Expected \"{EXP}\", got \"{GOT}\" at {POS}".format(EXP = tokenType, GOT = self.currentToken, POS = self.lexer.pos))

    def factor(self):
        token = self.currentToken
        if token.type is tokens.NUMBER:
            self.eat(tokens.NUMBER)
        elif token.type is tokens.POPEN:
            self.eat(tokens.POPEN)
            result = self.expr()
            self.eat(tokens.PCLOSE)
            return result

            # closing = self.lexer.text.rfind(")", self.lexer.pos)
            # newexpr = self.lexer.text[self.lexer.pos:closing]
            #
            # while self.currentToken.type is not tokens.PCLOSE:
            #     self.currentToken = self.lexer.nextToken()
            #
            # self.eat(tokens.PCLOSE)
            # tLexer = lexer.Lexer(newexpr)
            # tInterpreter = Interpreter(tLexer)
            # result = tInterpreter.expr()
            # return result

        return token.value

    def term(self):
        result = self.factor()

        ttype = self.currentToken.type
        while ttype in (tokens.MULT, tokens.DIV):
            ttype = self.currentToken.type

            if ttype is tokens.MULT:
                self.eat(tokens.MULT)
                val = self.factor()
                result = result * val

            if ttype is tokens.DIV:
                self.eat(tokens.DIV)
                val = self.factor()
                result = result / val

        return result


    def expr(self):
        """Parse and interpret"""

        result = self.term()

        while self.currentToken.type in (tokens.PLUS, tokens.MINUS): # is not tokens.EOF:
            if self.currentToken.type is tokens.PLUS:
                self.eat(tokens.PLUS)
                result = result + self.term()

            elif self.currentToken.type is tokens.MINUS:
                self.eat(tokens.MINUS)
                result = result - self.term()
            else:
                self.error("Unexpected \"{GOT}\".".format(GOT = self.currentToken))

        return result
