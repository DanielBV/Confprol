
from .confprol_exception import ConfprolException


class TooManyArguments(ConfprolException):


    def __init__(self, function, extra_arguments):
        self.function = function
        self.extra_arguments = extra_arguments
        
        super(TooManyArguments, self).__init__("TooManyArgumentsException")

    def get_message(self):
        return f" Too many arguments  {self.extra_arguments} in function {self.function}"