from __future__ import annotations

"""
This module contains classes that represent parts of
the Python language

For instance, there is a component (class) for an Integer,
for a Float, and for a Function.
"""


import dataclasses
from typing import *
from enum import Enum


@dataclasses.dataclass
class Integer(object):
    """
    *Integer* represents a Python integer

    - **value**: a field that stores the integer value as a string
    """

    value: AnyStr


@dataclasses.dataclass
class Float(object):
    """
    _Float_ represents a Python float

    - **value**: a field that stores the float value as a string
    """

    value: AnyStr


@dataclasses.dataclass
class Factor(object):
    """
    *Factors* are the building blocks of *Terms* and
    *Expressions*

    - **value**: is an *Integer* or a *Float*
    """

    value: Union[Integer, Float]

    def __repr__(self):
        return self.value


@dataclasses.dataclass
class Term(object):
    """
    *Terms* amalgamate two *Factors* together using a
    multiplication (*) or division (/) operator

    - **left**: is a *Factor*

    - **operator**: is an *Operator* (either MULTIPLY or DIVIDE)

    - **right**: is a *Factor*
    """

    left: Factor
    operator: Operator
    right: Factor

    def __repr__(self):
        if self.operator is Operator.MULTIPLY:
            return f"{self.left}*{self.right}"
        return f"{self.left}/{self.right}"


@dataclasses.dataclass
class Expression(object):
    """
    *Expressions* can get quite complex. *Terms* and
    *Factors* are their primary components along with
    *Operators*, however, *Expressions* can contain other
    *Expressions*

    - **left**: is a *Term*
    - **operator**: is an *Operator* (either PLUS or MINUS)
    - **right** is a *Term*
    """

    left: Term
    operator: Operator
    right: Term


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
