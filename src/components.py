from __future__ import annotations

"""
This module contains classes that represent parts of
the Python language

For instance, there is a component (class) for an Expression,
for a While Loop, and for a Function.
"""


import dataclasses
from typing import *
from enum import Enum


@dataclasses.dataclass
class BinaryOperation(object):
    """
    I have decided to opt for few arithmetic classes
    and implement order of operations through the parser's
    precedence instead of writing a bunch of classes
    just for order of operations
    """

    left: Union[Factor, AnyStr]
    operation: Operator
    right: Union[Factor, AnyStr]

    def __repr__(self):
        return "(" + repr(self.left) + \
               self.operation.value + repr(self.right) + ")"


@dataclasses.dataclass
class Factor(object):
    value: AnyStr

    def __repr__(self):
        return self.value


@dataclasses.dataclass
class Operator(Enum):
    """
    *Operator* is an enum that contains *Operators* used
    inside of *Terms* and *Expressions*
    """

    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
