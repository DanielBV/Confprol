

class ArgumentsMissing(Exception):

    def __init__(self, message,line,function, missing_arguments):
        super(ArgumentsMissing, self).__init__(message)
        self.line = line
        self.function = function
        self.missing_arguments = missing_arguments