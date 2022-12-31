"""
Main module which interacts with the source directory
"""

from src import lexer, parser
from ply import lex, yacc


def tokenize(input_data: str) -> None:
    """ Tests the lexer given input """

    built_lexer = lex.lex(module=lexer)
    built_lexer.input(input_data)

    # Get tokens
    while True:
        token = built_lexer.token()
        if token is None:
            break

        print(token)


def parse(input_data: str) -> None:
    built_lexer = lex.lex(module=lexer)
    built_parser = yacc.yacc(module=parser)
    print(built_parser.parse(input_data, lexer=built_lexer))


if __name__ == "__main__":
    while True:
        data = input(">>> ")
        tokenize(data)
