


class VariableNotDefined(Exception):

    def __init__(self, variable_name, line):
        self.variable_name = variable_name
        self.line = line
