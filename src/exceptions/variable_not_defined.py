
from .confprol_exception import ConfprolException

class VariableNotDefined(ConfprolException):

    def __init__(self, variable_name):
        self.variable_name = variable_name

        super(VariableNotDefined, self).__init__("VariableNotDefinedException")

    def get_message(self):
        return f"The variable {self.variable_name} is not defined."