"""
This module contains the lexer.

It's important that the tuple of tokens be imported where it is needed.
Ply is weird and requires it.

This lexer is also an alternative specification opposed to piling
all the code into a single file
"""


literals = ["+", "-", "*", "/"]
tokens = (
    "INT",  # INT short for Integer,
    "FLOAT",
)

# Java's doubles are just floats in Python
# Java's floats are difficult because they have an f appended to them
# ill implement Java's floats later
t_FLOAT = r"\d+\.\d+"

# Java has bytes, shorts, ints, and longs which are all just integers
# inside of Python
t_INT = r"\d+"
