


def left_shift_string(string, positions):
    return string[positions:] + string[0:positions]

def right_shift_string( string, positions):
    return string[len(string ) -positions:] + string[0:len(string ) -positions]

def string_algorithm(text: str):

    text = apply_double_quotes_escape_character(text)

    value = left_shift_string(text, 2)
    half = len(value) // 2

    value = value[0:half] + "".join(reversed(value[half:]))

    first_half = right_shift_string(value[:half], 3)

    value = value[half:] + first_half

    return apply_escape_characters(value)


def apply_double_quotes_escape_character(string):
    return string.replace(r"\"","\"")

def apply_escape_characters(string:str):
    return string.replace(r"\n", "\n")
