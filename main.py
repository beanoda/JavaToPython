"""
Main module which interacts with the source directory
"""

from src.lexical_analysis import java_lexer
from ply import lex, yacc


def tokenize(input_data: str) -> None:
    """ Tests the lexer given input """

    built_lexer = lex.lex(module=java_lexer)
    built_lexer.input(input_data)

    # Get tokens
    while True:
        token = built_lexer.token()
        if token is None:
            break

        print(token)


def parse(input_data: str) -> None:
    lexer, parser = 0
    built_lexer = lex.lex(module=lexer)
    built_parser = yacc.yacc(module=parser)
    print(built_parser.parse(input_data, lexer=built_lexer))


if __name__ == "__main__":
    while True:
        data = input(">>> ")
        tokenize(data)
