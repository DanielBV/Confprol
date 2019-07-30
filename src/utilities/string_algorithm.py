


def left_shift_string(string, positions):
    return string[positions:] + string[0:positions]

def right_shift_string( string, positions):
    return string[len(string ) -positions:] + string[0:len(string ) -positions]

def string_algorithm(text: str):

    value = left_shift_string(text, 2)
    half = len(value) // 2

    value = value[0:half] + "".join(reversed(value[half:]))

    first_half = right_shift_string(value[:half], 3)

    value = value[half:] + first_half

    return value