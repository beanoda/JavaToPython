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
    value: AnyStr


@dataclasses.dataclass
class Float(object):
    value: AnyStr


@dataclasses.dataclass
class Factor(object):
    value: Union[Integer, Float]


@dataclasses.dataclass
class Term(object):
    left: Factor
    operator: Operator
    right: Factor


@dataclasses.dataclass
class Expression(object):
    left: Term
    operator: Operator
    right: Term


@dataclasses.dataclass
class Operator(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
