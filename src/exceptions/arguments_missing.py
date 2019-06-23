

from .confprol_exception import ConfprolException

class ArgumentsMissing(ConfprolException):

    def __init__(self,function:str, missing_arguments):

        self.function = function
        self.missing_arguments = missing_arguments

        super(ArgumentsMissing, self).__init__("ArgumentsMissingException")

    def get_message(self):
        return f" Missing arguments  {self.missing_arguments} in function {self.function}"
