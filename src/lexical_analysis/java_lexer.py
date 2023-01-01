from typing import Tuple


tokens = []

# Constants used in regex and tokens. If it dont start w/ t, it's a
# constant
HEX_DIGIT = r"[0-9a-fA-F]"

# UnicodeEscape encapsulates UnicodeMarker because it is a simple rule
UNICODE_ESCAPE = r"\\u+[0-9a-fA-F]{4}"

# It says any unicode character. So non-specific that it hurts me
RAW_INPUT_CHARACTER = r"[\S\s]"
UNICODE_INPUT_CHARACTER = fr"{UNICODE_ESCAPE}|{RAW_INPUT_CHARACTER}"

# Matches LF, CR, or CRLF
LINE_TERMINATOR = r"\n|\r|(\r\n)"
INPUT_CHARACTER = fr"{UNICODE_INPUT_CHARACTER}"
