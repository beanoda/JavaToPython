"""
This module contains the parser.

The way I will keep everything organized is by applying the django
philosophy: "Fat models, skinny views". The aim is to pack as much
into the parser as possible to give the transpiler as an easier time
"""


# The parser must have this tuple inside of the scope at all times
from src.lexer import tokens
from src import components


def p_program(p):
    """
    program : factor
    """
    p[0] = p[1]


def p_factor(p):
    """
    factor : INT
           | FLOAT
    """

    # Integer and Float classes may be redundant
    p[0] = components.Factor(p[1])

