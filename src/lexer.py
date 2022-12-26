"""
This module contains the lexer.

It's important that the tuple of tokens be imported where it is needed.
Ply is weird and requires it.

This lexer is also an alternative specification opposed to piling
all the code into a single file
"""


literals = [
    "+", "-", "*", "/",  # Arithmetic
]
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

# Tabs matter in Python but in Java, they do not
# There might be an issue here later on when I start parsing files
t_ignore = " \t\n\r"


# Ill further implement this later
def t_error(t):
    print(f"Unknown Character {t.value}")
    t.lexer.skip(1)
