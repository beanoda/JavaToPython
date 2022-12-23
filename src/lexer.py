"""
This module contains the lexer.

It's important that the tuple of tokens be imported where it is needed.
Ply is weird and requires it.

This lexer is also an alternative specification opposed to piling
all the code into a single file
"""


tokens = (
    "INT",  # INT short for Integer
)

# It's important this is placed after FLOAT
t_INT = r"\d+"
