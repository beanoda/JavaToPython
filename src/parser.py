"""
This module contains the parser.

The way I will keep everything organized is by applying the django
philosophy: "Fat models, skinny views". The aim is to pack as much
into the parser as possible to give the transpiler as an easier time
"""


# The parser must have this tuple inside of the scope at all times
from src.lexer import tokens
from src import components


precedence = (
    ('left', '+', '-'),  # Level 1
    ('left', '*', '/'),  # Level 2
    ('right', 'UMINUS'),  # Level 3; Uminus = unary minus
)


def p_program(p):
    """
    program : expression
            | var_assignment
    """
    p[0] = p[1]


def p_expression(p):
    """
    expression : expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
               | INT
               | FLOAT
               | '-' expression %prec UMINUS
    """

    if p[1] == "-":
        # UMINUS is not a token nor is it a rule.
        # This just tells the parser to use the precedence
        # designated for UMINUS and apply it to this rule
        p[0] = components.Factor(p[2], True)
    elif len(p.slice) < 3:
        p[0] = components.Factor(p[1])
    else:
        if p[2] == "+":
            operator = components.Operator.PLUS
        elif p[2] == "-":
            operator = components.Operator.MINUS
        elif p[2] == "*":
            operator = components.Operator.MULTIPLY
        else:
            operator = components.Operator.DIVIDE

        p[0] = components.BinaryOperation(p[1], operator, p[3])


def p_var_assignment(p):
    """
    var_assignment : INT ID '=' expression
    """

    p[0] = components.VariableAssignment(p[2], p[4])
