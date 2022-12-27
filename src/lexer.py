"""
This module contains the lexer.

It's important that the tuple of tokens be imported where it is needed.
Ply is weird and requires it.

This lexer is also an alternative specification opposed to piling
all the code into a single file
"""


# These are keywords and # cannot be identifiers
reserved = {
    "abstract": "ABSTRACT",
    "assert": "ASSERT",
    "boolean": "BOOLEAN",
    "break": "BREAK",
    "byte": "BYTE",
    "case": "CASE",
    "catch": "CATCH",
    "char": "CHAR",
    "class": "CLASS",
    "continue": "CONTINUE",
    "default": "DEFAULT",
    "do": "DO",
    "double": "DOUBLE",
    "else": "ELSE",
    "enum": "ENUM",
    "extends": "EXTENDS",
    "final": "FINAL",
    "finally": "FINALLY",
    "float": "FLOAT",
    "for": "FOR",
    "if": "IF",
    "implements": "IMPLEMENTS",
    "import": "IMPORT",
    "instanceof": "INSTANCEOF",
    "int": "INT",
    "interface": "INTERFACE",
    "long": "LONG",
    "native": "NATIVE",
    "new": "NEW",
    "package": "PACKAGE",
    "private": "PRIVATE",
    "protected": "PROTECTED",
    "public": "PUBLIC",
    "return": "RETURN",
    "short": "SHORT",
    "static": "STATIC",
    "strictfp": "STRICTFP",
    "super": "SUPER",
    "switch": "SWITCH",
    "synchronized": "SYNCHRONIZED",
    "this": "THIS",
    "throw": "THROW",
    "throws": "THROWS",
    "transient": "TRANSIENT",
    "try": "TRY",
    "void": "VOID",
    "volatile": "VOLATILE",
    "while": "WHILE",

    # Useless; reserved for future use
    "const": "CONST",
    "goto": "GOTO",

    # Literals that cannot be used for keywords
    "true": "TRUE",
    "false": "FALSE",
    "null": "NULL",
}

literals = [
    "+", "-", "*", "/",  # Arithmetic
    "=",  # Assignment/Comparison
]

tokens = (
    "INT",  # short for Integer,
    "FLOAT",

    "ID",  # short for Identifier
) + tuple(reserved.values())

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


def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""

    t.type = reserved.get(t.value, "ID")
    return t


# Ill further implement this later
def t_error(t):
    print(f"Unknown Character {t.value}")
    t.lexer.skip(1)
