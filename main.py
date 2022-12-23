"""
Main module which interacts with the source directory
"""

from src import lexer
from ply import lex


def tokenize(input_data: str):
    """ Tests the lexer given input """

    built_lexer = lex.lex(module=lexer)
    built_lexer.input(input_data)

    # Get tokens
    while True:
        token = built_lexer.token()
        if token is None:
            break

        print(token)


if __name__ == "__main__":
    while True:
        data = input(">>> ")
        tokenize(data)
