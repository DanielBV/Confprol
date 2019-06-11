

class DuplicatedParameter(Exception):

    def __init__(self, function_name, duplicated_parameters, line):
        self.function_name = function_name
        self.duplicated_parameters = duplicated_parameters
        self.line = line

