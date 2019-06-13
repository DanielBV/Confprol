


class FunctionNotDefined(Exception):

    def __init__(self, function, line):
        self.function = function
        self.line = line
