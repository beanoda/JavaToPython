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
    program : expression
    """
    p[0] = p[1]


def p_expression_bin_op(p):
    """
    expression : expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
    """

    p[0] = components.BinaryOperation(p[1], components.Operator.PLUS, p[3])


def p_expression_factor(p):
    """
    expression : INT
               | FLOAT
    """

    p[0] = components.Factor(p[1])
