from grammar import (
    lexer,
    tokens,
    interpreter
)

def main():
    while True:
        text = input("ƒ> ")
        if not text:
            continue

        fLexer = lexer.Lexer(text)
        fInterpreter = interpreter.Interpreter(fLexer)
        result = fInterpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
