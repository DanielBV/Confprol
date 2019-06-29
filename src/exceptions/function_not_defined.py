
from .confprol_exception import  ConfprolException

class FunctionNotDefined(ConfprolException):

    def __init__(self, function):
        self.function = function
        super(FunctionNotDefined, self).__init__("FunctionNotDefinedException")

    def get_message(self):
        return f"Function {self.function} not defined."


