#!/usr/bin/env python3

from grammar import (
    interpreter,
    lexer
)

def main():

    while True:
        code = input('!> ')

        if not code:
            continue

        fluto_lexer = lexer.Lexer(code)
        fluto_interpreter = interpreter.Interpreter(fluto_lexer)
        result = fluto_interpreter.expr()

        print(result)

if __name__ == '__main__':
    main()
