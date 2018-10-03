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
