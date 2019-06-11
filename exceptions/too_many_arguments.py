



class TooManyArguments(Exception):


    def __init__(self, message, line, function, extra_arguments):
        super(TooManyArguments, self).__init__(message)
        self.line = line
        self.function = function
        self.extra_arguments = extra_arguments