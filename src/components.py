from __future__ import annotations

"""
This module contains classes that represent parts of
the Python language

For instance, there is a component (class) for an Integer,
for a Float, and for a Function.
"""


from dataclasses import dataclass
from typing import *
import enum


@dataclass
class Integer(object):
    value: int


@dataclass
class Float(object):
    value: AnyStr


@dataclass
class Factor(object):
    value: Union[Integer, Float]


@dataclass
class Term(object):
    left: Factor
    operator: Operator
    right: Factor


@dataclass
class Expression(object):
    left: Term
    operator: Operator
    right: Term


@dataclass
class Operator(enum.Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
